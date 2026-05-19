"""
Risk Calculator Module

This module provides AI-based risk score calculation from questionnaire answers
using the Polza AI API (DeepSeek model). It includes validation, normalization,
and a retry mechanism for robustness.
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
    Calculate risk score from questionnaire answers using AI.
    
    Args:
        answers: List of dictionaries containing question_id and answer_value
                 Example: [{'question_id': 1, 'answer_value': 5}, ...]
    
    Returns:
        Dictionary containing:
        - risk_score: Integer from 0-100
        - risk_category: One of 'Conservative', 'Moderate', 'Growth', 'Aggressive'
        - asset_allocation: Dict with percentage allocations
        - recommendations: List of recommendation strings
        - key_traits: List of trait strings
    """
    return _calculate_risk_score_with_ai(answers)


def _build_ai_prompt(answers: List[Dict[str, Any]]) -> tuple:
    """Build the system and user prompts for the AI."""
    
    system_prompt = """Ты — ведущий финансовый советник и эксперт по поведенческой экономике. Твоя задача — проанализировать психологический профиль клиента на основе его ответов на тест и выдать строго структурированный JSON с инвестиционным профилем.
    
ВАЖНО: Отвечай ТОЛЬКО валидным JSON-объектом, без Markdown-разметки (без ```json), без пояснительного текста до или после JSON.

Структура JSON должна быть строго такой:
{
  "risk_score": <число от 0 до 100>,
  "risk_category": "<строго одно из: Conservative, Moderate, Growth, Aggressive>",
  "asset_allocation": {
    "stocks": <число, %>,
    "bonds": <число, %>,
    "cash": <число, %>,
    "alternatives": <число, %>
  },
  "recommendations": [
    "<персонализированный совет 1>",
    "<совет 2>",
    "<совет 3>",
    "<совет 4>",
    "<совет 5>"
  ],
  "key_traits": [
    "<психологическая черта 1>",
    "<черта 2>",
    "<черта 3>",
    "<черта 4>"
  ]
}

Правила расчета:
1. risk_score: высчитывается на основе толерантности к риску. Учитывай логику, эмоциональный контроль, независимость и силу воли.
2. risk_category:
   - 0-30: Conservative
   - 31-60: Moderate
   - 61-80: Growth
   - 81-100: Aggressive
3. asset_allocation: Сумма значений stocks + bonds + cash + alternatives ДОЛЖНА БЫТЬ РОВНО 100.
4. recommendations: 5 предложений. Тон: профессиональный, персонализированный на основе ответов. Без эмодзи.
5. key_traits: 4 психологических характеристики клиента, вытекающие из его ответов."""

    # Fetch question texts
    question_ids = [a['question_id'] for a in answers]
    questions_map = {q.id: q.text for q in SurveyQuestion.objects.filter(id__in=question_ids)}
    
    user_prompt = "Пользователь ответил на тест. Шкала: 1 — Категорически не согласен, 5 — Полностью согласен (если вопрос подразумевает степень согласия). Вот его ответы:\n\n"
    
    for answer in answers:
        q_id = answer['question_id']
        val = answer['answer_value']
        text = questions_map.get(q_id, f"Вопрос {q_id}")
        user_prompt += f"- Вопрос: \"{text}\" -> Ответ: {val}\n"
        
    user_prompt += "\nСформируй JSON-профиль на основе этих данных."
    
    return system_prompt, user_prompt


def _validate_and_normalize_ai_response(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and normalize the AI JSON response."""
    
    # Check required keys
    required_keys = ['risk_score', 'risk_category', 'asset_allocation', 'recommendations', 'key_traits']
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key in AI response: {key}")
            
    # Normalize risk_score
    try:
        score = int(data['risk_score'])
        data['risk_score'] = max(0, min(100, score))
    except (ValueError, TypeError):
        raise ValueError("risk_score must be an integer")
        
    # Normalize risk_category
    valid_categories = ['Conservative', 'Moderate', 'Growth', 'Aggressive']
    if data['risk_category'] not in valid_categories:
        # Try to infer from score if category is invalid
        score = data['risk_score']
        if score <= 30: data['risk_category'] = 'Conservative'
        elif score <= 60: data['risk_category'] = 'Moderate'
        elif score <= 80: data['risk_category'] = 'Growth'
        else: data['risk_category'] = 'Aggressive'
        
    # Normalize asset_allocation
    alloc = data.get('asset_allocation', {})
    required_assets = ['stocks', 'bonds', 'cash', 'alternatives']
    total = 0
    
    # Ensure all keys exist and are numbers
    for asset in required_assets:
        try:
            val = float(alloc.get(asset, 0))
            alloc[asset] = val
            total += val
        except (ValueError, TypeError):
            alloc[asset] = 0
            
    # Normalize to 100%
    if total == 0:
        alloc = {'stocks': 45, 'bonds': 35, 'cash': 15, 'alternatives': 5}
    elif abs(total - 100) > 0.1:
        for asset in required_assets:
            alloc[asset] = round((alloc[asset] / total) * 100)
            
        # Fix rounding errors to make exact 100
        current_total = sum(alloc.values())
        if current_total != 100:
            diff = 100 - current_total
            # Add difference to the largest asset class
            largest_asset = max(alloc.keys(), key=lambda k: alloc[k])
            alloc[largest_asset] += diff
            
    data['asset_allocation'] = alloc
    
    # Ensure lists are lists
    if not isinstance(data.get('recommendations'), list):
        data['recommendations'] = ["Обратитесь к финансовому консультанту для детального плана."]
    if not isinstance(data.get('key_traits'), list):
        data['key_traits'] = ["Требуется дополнительный анализ"]
        
    return data


def _calculate_risk_score_with_ai(answers: List[Dict[str, Any]], max_retries: int = 3) -> Dict[str, Any]:
    """Call Polza AI API with retry logic."""
    
    if not settings.POLZA_API_KEY:
        logger.warning("POLZA_API_KEY not set. Using fallback calculation.")
        return _fallback_calculate_risk_score(answers)
        
    system_prompt, user_prompt = _build_ai_prompt(answers)
    
    headers = {
        "Authorization": f"Bearer {settings.POLZA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": settings.POLZA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2, # Low temperature for more consistent, JSON-compliant output
        # Some models support response_format, adding it if supported by Polza/DeepSeek API
        "response_format": {"type": "json_object"}
    }
    
    url = f"{settings.POLZA_BASE_URL.rstrip('/')}/chat/completions"
    
    for attempt in range(max_retries):
        try:
            logger.info(f"Calling AI API (attempt {attempt + 1}/{max_retries})")
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            
            result_json = response.json()
            content = result_json['choices'][0]['message']['content'].strip()
            
            # Clean up potential markdown formatting if the model ignored the system prompt
            if content.startswith('```json'):
                content = content[7:]
            if content.endswith('```'):
                content = content[:-3]
            content = content.strip()
            
            parsed_data = json.loads(content)
            
            # Validate and normalize
            validated_data = _validate_and_normalize_ai_response(parsed_data)
            logger.info("AI risk score calculation successful")
            return validated_data
            
        except (requests.RequestException, json.JSONDecodeError, ValueError, KeyError) as e:
            logger.warning(f"AI calculation failed on attempt {attempt + 1}: {str(e)}")
            if attempt < max_retries - 1:
                # Wait before retrying
                time.sleep(1.5 * (attempt + 1))
            else:
                logger.error("All AI calculation attempts failed. Using fallback.")
                return _fallback_calculate_risk_score(answers)


def _fallback_calculate_risk_score(answers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Fallback formula-based calculation in case AI completely fails.
    (This is the original implementation)
    """
    
    # Initialize scores for each category
    logic_score = 0
    emotional_score = 0
    independence_score = 0
    willpower_score = 0
    
    # Count answers in each category
    logic_count = 0
    emotional_count = 0
    independence_count = 0
    willpower_count = 0
    
    # Process each answer
    for answer in answers:
        question_id = answer.get('question_id')
        answer_value = answer.get('answer_value', 3)  # Default to neutral
        
        # Normalize answer value (1-5) to score (0-100)
        # 1 = Fully agree (low risk) -> 0
        # 5 = Fully disagree (high risk) -> 100
        normalized_score = ((answer_value - 1) / 4) * 100
        
        # Categorize by question ID
        if 1 <= question_id <= 7:
            logic_score += normalized_score
            logic_count += 1
        elif 8 <= question_id <= 12:
            emotional_score += normalized_score
            emotional_count += 1
        elif 13 <= question_id <= 17:
            independence_score += normalized_score
            independence_count += 1
        elif 18 <= question_id <= 23:
            willpower_score += normalized_score
            willpower_count += 1
    
    # Calculate average scores for each category
    logic_avg = logic_score / logic_count if logic_count > 0 else 50
    emotional_avg = emotional_score / emotional_count if emotional_count > 0 else 50
    independence_avg = independence_score / independence_count if independence_count > 0 else 50
    willpower_avg = willpower_score / willpower_count if willpower_count > 0 else 50
    
    # Calculate overall risk score with weighted formula
    # Weights based on importance for investment decisions
    weights = {
        'logic': 0.25,        # Analytical thinking
        'emotional': 0.30,    # Emotional stability (most important)
        'independence': 0.20, # Independence in decisions
        'willpower': 0.25     # Persistence and leadership
    }
    
    overall_score = (
        logic_avg * weights['logic'] +
        emotional_avg * weights['emotional'] +
        independence_avg * weights['independence'] +
        willpower_avg * weights['willpower']
    )
    
    # Round to nearest integer
    risk_score = int(round(overall_score))
    
    # Determine risk category
    if risk_score <= 30:
        risk_category = 'Conservative'
    elif risk_score <= 60:
        risk_category = 'Moderate'
    elif risk_score <= 80:
        risk_category = 'Growth'
    else:
        risk_category = 'Aggressive'
    
    # Generate asset allocation based on risk category
    asset_allocation = _generate_asset_allocation(risk_category)
    
    # Generate recommendations based on risk category
    recommendations = _generate_recommendations(risk_category)
    
    # Generate key traits based on scores
    key_traits = _generate_key_traits(logic_avg, emotional_avg, independence_avg, willpower_avg)
    
    return {
        'risk_score': risk_score,
        'risk_category': risk_category,
        'asset_allocation': asset_allocation,
        'recommendations': recommendations,
        'key_traits': key_traits
    }


def _generate_asset_allocation(risk_category: str) -> Dict[str, int]:
    """
    Generate asset allocation percentages based on risk category.
    
    Args:
        risk_category: One of 'Conservative', 'Moderate', 'Growth', 'Aggressive'
    
    Returns:
        Dictionary with allocation percentages for stocks, bonds, cash, alternatives
    """
    allocations = {
        'Conservative': {
            'stocks': 20,
            'bonds': 50,
            'cash': 25,
            'alternatives': 5
        },
        'Moderate': {
            'stocks': 45,
            'bonds': 35,
            'cash': 15,
            'alternatives': 5
        },
        'Growth': {
            'stocks': 65,
            'bonds': 20,
            'cash': 10,
            'alternatives': 5
        },
        'Aggressive': {
            'stocks': 80,
            'bonds': 10,
            'cash': 5,
            'alternatives': 5
        }
    }
    
    return allocations.get(risk_category, allocations['Moderate'])


def _generate_recommendations(risk_category: str) -> List[str]:
    """
    Generate investment recommendations based on risk category.
    
    Args:
        risk_category: One of 'Conservative', 'Moderate', 'Growth', 'Aggressive'
    
    Returns:
        List of recommendation strings
    """
    recommendations = {
        'Conservative': [
            'Приоритет сохранения капитала над высокой доходностью',
            'Сосредоточьтесь на государственных облигациях и высококачественных корпоративных облигациях',
            'Поддерживайте значительные денежные резервы для ликвидности',
            'Рассмотрите дивидендные акции крупных компаний (blue-chip)',
            'Избегайте спекулятивных инвестиций и высоковолатильных активов',
            'Регулярная ребалансировка портфеля для сохранения консервативного распределения'
        ],
        'Moderate': [
            'Поддерживайте сбалансированный подход между ростом и стабильностью',
            'Диверсифицируйте портфель по разным классам активов',
            'Включите смесь акций роста и акций стоимости',
            'Инвестируйте как в государственные, так и в корпоративные облигации',
            'Поддерживайте умеренные денежные резервы для возможностей',
            'Рассмотрите индексные фонды для широкого охвата рынка',
            'Проверяйте портфель ежеквартально и ребалансируйте ежегодно'
        ],
        'Growth': [
            'Сосредоточьтесь на приросте капитала с умеренным риском',
            'Выделите значительную часть в акции роста',
            'Включите инвестиции в развивающиеся рынки',
            'Рассмотрите отраслевые ETF для целевого экспонирования',
            'Поддерживайте меньшую денежную позицию для тактических возможностей',
            'Используйте усреднение долларовой стоимости для регулярных инвестиций',
            'Следите за рыночными условиями и корректируйте распределение соответствующим образом'
        ],
        'Aggressive': [
            'Максимизируйте потенциал роста с высокой толерантностью к риску',
            'Значительное распределение в акции и акции роста',
            'Включите акции малого капитала и международные акции',
            'Рассмотрите альтернативные инвестиции (криптовалюта, стартапы и т.д.)',
            'Используйте кредитное плечо с осторожностью для повышения доходности',
            'Активная торговля и стратегии рыночного тайминга',
            'Примите более высокую волатильность ради потенциально более высокой доходности'
        ]
    }
    
    return recommendations.get(risk_category, recommendations['Moderate'])


def _generate_key_traits(
    logic_avg: float,
    emotional_avg: float,
    independence_avg: float,
    willpower_avg: float
) -> List[str]:
    """
    Generate key personality traits based on category scores.
    
    Args:
        logic_avg: Average logic score (0-100)
        emotional_avg: Average emotional control score (0-100)
        independence_avg: Average independence score (0-100)
        willpower_avg: Average willpower score (0-100)
    
    Returns:
        List of trait strings
    """
    traits = []
    
    # Logic traits
    if logic_avg >= 70:
        traits.append('Аналитический мыслитель')
    elif logic_avg >= 40:
        traits.append('Сбалансированный принимающий решения')
    else:
        traits.append('Интуитивный принимающий решения')
    
    # Emotional traits
    if emotional_avg >= 70:
        traits.append('Эмоционально стабильный')
    elif emotional_avg >= 40:
        traits.append('Умеренно эмоциональный')
    else:
        traits.append('Эмоционально реактивный')
    
    # Independence traits
    if independence_avg >= 70:
        traits.append('Самостоятельно принимающий решения')
    elif independence_avg >= 40:
        traits.append('Полусамостоятельный')
    else:
        traits.append('Ищет внешнего подтверждения')
    
    # Willpower traits
    if willpower_avg >= 70:
        traits.append('Сильная решимость')
    elif willpower_avg >= 40:
        traits.append('Умеренное упорство')
    else:
        traits.append('Нуждается в мотивационной поддержке')
    
    return traits

# The calculate_risk_score_with_ai is now the main entry point via _calculate_risk_score_with_ai
# keeping this for backwards compatibility if any other module imports it directly
def calculate_risk_score_with_ai(answers: List[Dict[str, Any]]) -> Dict[str, Any]:
    return calculate_risk_score(answers)
