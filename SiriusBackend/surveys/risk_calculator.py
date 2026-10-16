"""
Risk Calculator Module - Behavioral & Financial AI Analyzer

Calculates investor risk score, cognitive radar metrics (capacity, stress resistance,
fomo control, discipline), archetype, behavioral traps, and asset allocation.
Uses Polza AI (DeepSeek) with a deterministic fallback based on answer weights.
"""

import json
import logging
import requests
import time
from typing import List, Dict, Any
from django.conf import settings
from .models import SurveyQuestion

logger = logging.getLogger(__name__)


def calculate_risk_score(answers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Main entry point to calculate risk profile from answers.
    First tries LLM via Polza AI; if unavailable or failing, uses robust fallback.
    """
    return _calculate_risk_score_with_ai(answers)


def _build_ai_prompt(answers: List[Dict[str, Any]]) -> tuple:
    """Build system and user prompts for behavioral financial analysis."""
    
    system_prompt = """Ты — ведущий финансовый советник (Senior Wealth Advisor) и эксперт по поведенческим финансам (Behavioral Economics).
Твоя задача — провести глубокий анализ финансового и психологического профиля частного инвестора по его ответам на ситуационные дилеммы и вернуть строго валидный JSON.

ВАЖНО: Отвечай ТОЛЬКО валидным JSON-объектом, без Markdown (без ```json), без вводных или заключительных слов.

Структура JSON строго следующая:
{
  "risk_score": <число от 0 до 100>,
  "risk_category": "<строго одно из: Conservative, Moderate, Growth, Aggressive>",
  "archetype": {
    "title": "<Яркое название инвестиционного психотипа, напр. 'Стратегический архитектор' / 'Осторожный хранитель' / 'Прагматичный рантье' / 'Импульсивный первооткрыватель'>",
    "description": "<2-3 емких предложения, раскрывающих сильные стороны характера и его инвестиционную суть>"
  },
  "radar_scores": {
    "capacity": <число от 0 до 100, финансовая емкость и горизонт>,
    "stress_resistance": <число от 0 до 100, хладнокровие при просадках и волатильности>,
    "fomo_control": <число от 0 до 100, независимость от хайпа и стадного инстинкта>,
    "discipline": <число от 0 до 100, волевая дисциплина, следование стратегии без суеты>
  },
  "behavioral_traps": [
    {
      "trap": "<Название когнитивного искажения, выявленного по ответам, напр. 'Неприятие потерь' / 'Синдром упущенной выгоды (FOMO)' / 'Иллюзия контроля'>",
      "warning": "<В чем конкретно опасность для этого инвестора>",
      "rule": "<Одно четкое золотое правило защиты от этой ошибки>"
    },
    {
      "trap": "<Вторая ловушка>",
      "warning": "<Предупреждение>",
      "rule": "<Защитное правило>"
    }
  ],
  "asset_allocation": {
    "stocks": <число %, акции и долевые активы>,
    "bonds": <число %, облигации и фонды ликвидности>,
    "cash": <число %, подушка и кэш-резерв>,
    "alternatives": <число %, золото, сырье, крипта, венчур>
  },
  "recommendations": [
    "<Конкретный прикладной совет 1>",
    "<Совет 2>",
    "<Совет 3>",
    "<Совет 4>",
    "<Совет 5>"
  ],
  "key_traits": [
    "<Черта 1, напр. 'Высокий горизонт планирования'>",
    "<Черта 2>",
    "<Черта 3>",
    "<Черта 4>"
  ]
}

Правила расчета:
1. radar_scores: каждая ось от 0 до 100 отражает реальные ответы пользователя.
2. risk_score: интегральный показатель готовности к риску (согласован с radar_scores).
3. asset_allocation: сумма stocks + bonds + cash + alternatives ДОЛЖНА БЫТЬ В ТОЧНОСТИ РАВНА 100.
4. recommendations: практические советы по формированию портфеля на основе его горизонта и целей. Тон: академический, уважительный, без клише и эмодзи.
"""

    # Fetch question metadata and options
    q_ids = [a['question_id'] for a in answers]
    questions = {q.id: q for q in SurveyQuestion.objects.filter(id__in=q_ids)}

    user_prompt = "Инвестор ответил на следующие ситуационные вопросы финансового и поведенческого теста:\n\n"

    for answer in answers:
        q_id = answer['question_id']
        val = answer['answer_value']
        question = questions.get(q_id)
        if not question:
            continue

        chosen_text = f"Вариант #{val}"
        if question.options and isinstance(question.options, list):
            for opt in question.options:
                if opt.get('value') == val:
                    chosen_text = f"\"{opt.get('text', '')}\""
                    break

        user_prompt += f"Вопрос (Категория: {question.category}): {question.text}\n"
        user_prompt += f"Выбранный ответ: {chosen_text} (код: {val})\n\n"

    user_prompt += "Сформируй глубокий инвестиционный паспорт в формате JSON строго по указанной схеме."
    return system_prompt, user_prompt


def _validate_and_normalize_ai_response(data: Dict[str, Any], raw_answers: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Validate and normalize the AI JSON response."""
    
    # Normalize risk_score
    try:
        score = int(data.get('risk_score', 50))
        data['risk_score'] = max(0, min(100, score))
    except (ValueError, TypeError):
        data['risk_score'] = 50

    # Normalize category
    valid_categories = ['Conservative', 'Moderate', 'Growth', 'Aggressive']
    score = data['risk_score']
    if data.get('risk_category') not in valid_categories:
        if score <= 30: data['risk_category'] = 'Conservative'
        elif score <= 60: data['risk_category'] = 'Moderate'
        elif score <= 80: data['risk_category'] = 'Growth'
        else: data['risk_category'] = 'Aggressive'

    # Normalize radar_scores
    radar = data.get('radar_scores', {})
    if not isinstance(radar, dict):
        radar = {}
    default_radar = {
        'capacity': max(10, min(95, score + 5)),
        'stress_resistance': max(10, min(95, score - 5)),
        'fomo_control': 65,
        'discipline': 70
    }
    for axis in ['capacity', 'stress_resistance', 'fomo_control', 'discipline']:
        try:
            val = int(radar.get(axis, default_radar[axis]))
            radar[axis] = max(0, min(100, val))
        except (ValueError, TypeError):
            radar[axis] = default_radar[axis]
    data['radar_scores'] = radar

    # Normalize archetype
    archetype = data.get('archetype', {})
    if not isinstance(archetype, dict) or not archetype.get('title'):
        title_map = {
            'Conservative': 'Осторожный хранитель капитала',
            'Moderate': 'Сбалансированный прагматик',
            'Growth': 'Стратегический архитектор роста',
            'Aggressive': 'Динамичный венчурный исследователь'
        }
        data['archetype'] = {
            'title': title_map.get(data['risk_category'], 'Осознанный инвестор'),
            'description': 'Вы ориентированы на систематический подход к инвестициям с учетом баланса надежности и доходности.'
        }

    # Normalize behavioral_traps
    traps = data.get('behavioral_traps', [])
    if not isinstance(traps, list) or len(traps) == 0:
        data['behavioral_traps'] = [
            {
                'trap': 'Иллюзия контроля и чрезмерный оптимизм',
                'warning': 'Попытка предугадать локальные движения рынка часто приводит к лишним комиссиям и упущенной прибыли.',
                'rule': 'Следовать регулярному графику ребалансировки вместо спекулятивных сделок.'
            }
        ]

    # Normalize asset_allocation to exactly 100%
    alloc = data.get('asset_allocation', {})
    if not isinstance(alloc, dict):
        alloc = {}
    required_assets = ['stocks', 'bonds', 'cash', 'alternatives']
    total = 0
    clean_alloc = {}
    for asset in required_assets:
        try:
            val = float(alloc.get(asset, 0))
            clean_alloc[asset] = val
            total += val
        except (ValueError, TypeError):
            clean_alloc[asset] = 0

    if total == 0:
        clean_alloc = {'stocks': 45, 'bonds': 35, 'cash': 15, 'alternatives': 5}
    else:
        for asset in required_assets:
            clean_alloc[asset] = round((clean_alloc[asset] / total) * 100)
        current_sum = sum(clean_alloc.values())
        if current_sum != 100:
            diff = 100 - current_sum
            largest_asset = max(clean_alloc.keys(), key=lambda k: clean_alloc[k])
            clean_alloc[largest_asset] += diff
    data['asset_allocation'] = clean_alloc

    # Ensure lists
    if not isinstance(data.get('recommendations'), list) or not data['recommendations']:
        data['recommendations'] = [
            'Сформируйте резервный фонд ликвидности на 3-6 месяцев перед покупкой рисковых активов.',
            'Используйте фонды широкого рынка акций для обеспечения страновой и отраслевой диверсификации.',
            'Проводите регулярную ребалансировку портфеля не чаще одного раза в полгода.'
        ]
    if not isinstance(data.get('key_traits'), list) or not data['key_traits']:
        data['key_traits'] = ['Рациональный подход', 'Умение удерживать горизонт', 'Высокая автономия']

    return data


def _calculate_risk_score_with_ai(answers: List[Dict[str, Any]], max_retries: int = 2) -> Dict[str, Any]:
    """Call Polza AI API with retry logic; fall back to deterministic scoring on failure."""
    
    if not getattr(settings, 'POLZA_API_KEY', None):
        logger.warning("POLZA_API_KEY not configured. Using deterministic fallback calculation.")
        return _fallback_calculate_risk_score(answers)

    system_prompt, user_prompt = _build_ai_prompt(answers)

    headers = {
        "Authorization": f"Bearer {settings.POLZA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": getattr(settings, 'POLZA_MODEL', 'deepseek/deepseek-v4-flash'),
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2,
        "response_format": {"type": "json_object"}
    }

    url = f"{settings.POLZA_BASE_URL.rstrip('/')}/chat/completions"

    for attempt in range(max_retries):
        try:
            logger.info(f"Calling Polza AI (attempt {attempt + 1}/{max_retries})")
            response = requests.post(url, headers=headers, json=payload, timeout=45)
            response.raise_for_status()

            result_json = response.json()
            content = result_json['choices'][0]['message']['content'].strip()

            if content.startswith('```json'):
                content = content[7:]
            if content.endswith('```'):
                content = content[:-3]
            content = content.strip()

            parsed_data = json.loads(content)
            validated = _validate_and_normalize_ai_response(parsed_data, answers)
            logger.info("AI behavioral risk calculation successful")
            return validated

        except Exception as e:
            logger.warning(f"AI calculation failed on attempt {attempt + 1}: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(1.0 * (attempt + 1))
            else:
                logger.error("All AI calculation attempts failed. Proceeding with fallback formula.")
                return _fallback_calculate_risk_score(answers)


def _fallback_calculate_risk_score(answers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Deterministic calculation if AI service is unavailable.
    Calculates 4 axes directly from question categories and option scores.
    """
    q_ids = [a['question_id'] for a in answers]
    questions = {q.id: q for q in SurveyQuestion.objects.filter(id__in=q_ids)}

    category_scores = {
        'capacity': [],
        'stress': [],
        'behavioral': [],
        'discipline': []
    }

    for a in answers:
        q_id = a.get('question_id')
        val = a.get('answer_value', 1)
        q = questions.get(q_id)
        if not q:
            continue

        # Look up option score if defined, otherwise derive from value
        score = 50
        if q.options and isinstance(q.options, list):
            for opt in q.options:
                if opt.get('value') == val:
                    score = opt.get('score', 50)
                    break
        else:
            score = ((val - 1) / 4) * 100

        cat = q.category if q.category in category_scores else 'capacity'
        category_scores[cat].append(score)

    def avg(lst, default=50):
        return sum(lst) / len(lst) if lst else default

    capacity = int(round(avg(category_scores['capacity'], 60)))
    stress_res = int(round(avg(category_scores['stress'], 50)))
    fomo_control = int(round(avg(category_scores['behavioral'], 60)))
    discipline = int(round(avg(category_scores['discipline'], 65)))

    overall_score = int(round(capacity * 0.35 + stress_res * 0.35 + fomo_control * 0.15 + discipline * 0.15))

    if overall_score <= 30:
        risk_category = 'Conservative'
        title = 'Осторожный хранитель капитала'
        description = 'Ваш главный приоритет — сохранность средств и минимальная волатильность. Вы комфортно чувствуете себя с защитными инструментами.'
        alloc = {'stocks': 20, 'bonds': 50, 'cash': 25, 'alternatives': 5}
    elif overall_score <= 60:
        risk_category = 'Moderate'
        title = 'Сбалансированный прагматик'
        description = 'Вы взвешенно сочетаете инструменты с фиксированной доходностью и надежные акции, стремясь умеренно опережать инфляцию.'
        alloc = {'stocks': 45, 'bonds': 35, 'cash': 15, 'alternatives': 5}
    elif overall_score <= 80:
        risk_category = 'Growth'
        title = 'Стратегический архитектор роста'
        description = 'Вы готовы переносить рыночные колебания ради долгосрочного приумножения капитала и осознанно принимаете расчетный риск.'
        alloc = {'stocks': 65, 'bonds': 20, 'cash': 10, 'alternatives': 5}
    else:
        risk_category = 'Aggressive'
        title = 'Динамичный венчурный исследователь'
        description = 'Вы стремитесь к максимальной доходности, не боитесь глубоких коррекций и открыты к высоковолатильным и альтернативным активам.'
        alloc = {'stocks': 80, 'bonds': 10, 'cash': 5, 'alternatives': 5}

    return {
        'risk_score': overall_score,
        'risk_category': risk_category,
        'archetype': {
            'title': title,
            'description': description
        },
        'radar_scores': {
            'capacity': capacity,
            'stress_resistance': stress_res,
            'fomo_control': fomo_control,
            'discipline': discipline
        },
        'behavioral_traps': [
            {
                'trap': 'Эмоциональный импульс на коррекциях',
                'warning': 'Внезапные колебания рынка могут провоцировать спонтанные действия, нарушающие план.',
                'rule': 'Соблюдайте правило 48 часов перед совершением незапланированных покупок или продаж.'
            }
        ],
        'asset_allocation': alloc,
        'recommendations': [
            'Сформируйте резервный фонд ликвидности на 3-6 месяцев перед покупкой рисковых активов.',
            'Используйте фонды широкого рынка акций для обеспечения страновой и отраслевой диверсификации.',
            'Проводите регулярную ребалансировку портфеля не чаще одного раза в полгода.'
        ],
        'key_traits': ['Системность', 'Осознанность в риске', 'Горизонтное планирование']
    }
