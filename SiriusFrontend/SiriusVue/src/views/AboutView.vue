<template>
  <div class="max-w-5xl mx-auto py-12 px-4 sm:px-6 lg:px-8 space-y-16">
    <!-- Header -->
    <div class="space-y-4">
      <div class="badge-amber">ИССЛЕДОВАНИЕ И МЕТОДОЛОГИЯ</div>
      <h1 class="text-3xl sm:text-5xl font-serif font-bold text-ink-950 tracking-tight leading-[1.15]">
        О платформе когнитивного риск-профилирования
      </h1>
      <p class="text-base sm:text-lg text-ink-700 leading-relaxed max-w-3xl">
        Sirius (Psy Otkliq) — исследовательская аналитическая платформа, созданная на стыке поведенческой экономики (Behavioral Finance), когнитивной психологии и больших языковых моделей (LLM). Наша цель — заменить устаревшие формальные анкеты глубоким стресс-анализом реального характера инвестора.
      </p>
    </div>

    <!-- The Problem: Why Traditional Questionnaires Fail -->
    <div class="academic-card p-6 sm:p-10 space-y-6 bg-white">
      <div class="flex items-center gap-2 text-academic-amber font-mono text-xs font-bold uppercase tracking-wider">
        <i class="fas fa-exclamation-triangle"></i>
        <span>Проблема индустрии</span>
      </div>
      <h2 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950">
        Почему классические банковские анкеты приводят к потерям капитала?
      </h2>
      <p class="text-sm sm:text-base text-ink-700 leading-relaxed">
        Традиционный финансовый консалтинг опирается на 3–5 опросных пунктов: возраст, текущий доход и абстрактный вопрос «Готовы ли вы к риску?». Находясь в кабинете финансового консультанта в спокойном состоянии, 95% людей искренне отвечают «Да, я хладнокровен».
      </p>
      <p class="text-sm sm:text-base text-ink-700 leading-relaxed">
        Однако академические исследования и биржевая статистика подтверждают: более <strong class="text-ink-950">87% финансовых потерь</strong> частных инвесторов обусловлены не макроэкономикой и не ошибками аналитиков, а когнитивными сбоями: паникой при рыночной коррекции, покупкой перегретых активов на пике хайпа (FOMO) и неспособностью психологически зафиксировать убыток.
      </p>
      
      <div class="p-5 rounded-2xl bg-amber-50/70 border border-amber-200/90 text-amber-950 text-sm font-serif italic leading-relaxed flex items-start gap-3">
        <span class="text-2xl text-academic-amber not-italic leading-none">“</span>
        <div>
          «Главная проблема инвестора — и даже его злейший враг — это он сам. Чем больше мы полагаемся на эмоциональную уверенность вместо понимания когнитивных ловушек, тем ближе неизбежная капитуляция на самом дне рынка».
          <div class="text-xs font-mono font-semibold text-ink-600 not-italic mt-2">— Бенджамин Грэм & Даниэль Канеман</div>
        </div>
      </div>
    </div>

    <!-- Comparison Table: Traditional vs Sirius Cognitive Platform -->
    <div class="academic-card p-6 sm:p-10 space-y-6 bg-white overflow-hidden">
      <div class="space-y-1">
        <div class="badge-amber">ЭВОЛЮЦИЯ ПОДХОДА</div>
        <h3 class="text-xl sm:text-2xl font-serif font-bold text-ink-950">
          Сравнение: Формальный банковский скоринг vs Модель Sirius
        </h3>
        <p class="text-xs text-ink-500 font-mono">
          Качественный переход от абстрактных деклараций к поведенческому моделированию
        </p>
      </div>

      <div class="overflow-x-auto pt-2">
        <table class="w-full text-left text-xs sm:text-sm border-collapse">
          <thead>
            <tr class="border-b border-ink-200 text-ink-400 font-mono uppercase text-[11px]">
              <th class="py-3 px-4 font-semibold">Параметр оценки</th>
              <th class="py-3 px-4 font-semibold text-ink-500 bg-paper-50 rounded-t-lg">Классическая анкета банка</th>
              <th class="py-3 px-4 font-semibold text-academic-amber bg-amber-50/60 rounded-t-lg">Когнитивная модель Sirius</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-ink-100 text-ink-800">
            <tr>
              <td class="py-3.5 px-4 font-medium text-ink-950">Формат дилемм</td>
              <td class="py-3.5 px-4 bg-paper-50/50 text-ink-600">3–5 абстрактных вопросов («Ваш доход?», «Срок?»)</td>
              <td class="py-3.5 px-4 bg-amber-50/30 text-ink-950 font-medium">12 реалистичных стрессовых дилемм с выбором конкретного действия</td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-medium text-ink-950">Метрика профиля</td>
              <td class="py-3.5 px-4 bg-paper-50/50 text-ink-600">Одномерная шкала (Консервативный / Агрессивный)</td>
              <td class="py-3.5 px-4 bg-amber-50/30 text-ink-950 font-medium">4D когнитивный радар (Емкость, Стойкость, FOMO, Дисциплина)</td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-medium text-ink-950">Учет психологии</td>
              <td class="py-3.5 px-4 bg-paper-50/50 text-ink-600">Полное игнорирование эмоционального фактора</td>
              <td class="py-3.5 px-4 bg-amber-50/30 text-ink-950 font-medium">Детекция 5 ключевых когнитивных искажений и ловушек мышления</td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-medium text-ink-950">Аналитический движок</td>
              <td class="py-3.5 px-4 bg-paper-50/50 text-ink-600">Простая сумма баллов по жесткой таблице</td>
              <td class="py-3.5 px-4 bg-amber-50/30 text-ink-950 font-medium">Нейросетевая когнитивная кластеризация + детерминированный алгоритм</td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-medium text-ink-950">Рекомендации</td>
              <td class="py-3.5 px-4 bg-paper-50/50 text-ink-600">Шаблонное предложение инвестиционного фонда</td>
              <td class="py-3.5 px-4 bg-amber-50/30 text-ink-950 font-medium">Персональный инвестиционный психотип + защитный протокол при кризисах</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- The 4 Cognitive Vectors Grid -->
    <div class="space-y-6">
      <div class="space-y-1">
        <div class="badge-amber">4 ВЕКТОРА МЫШЛЕНИЯ</div>
        <h2 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950">
          Четыре оси когнитивной устойчивости
        </h2>
        <p class="text-sm text-ink-600 max-w-2xl">
          Каждый ответ в тесте калибрует многомерный вектор инвестора. Мы не вешаем ярлыки, а измеряем реальные оси баланса:
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Vector 1 -->
        <div class="academic-card p-6 sm:p-7 space-y-3 bg-white hover:border-amber-400 transition-all">
          <div class="flex items-center justify-between">
            <span class="w-8 h-8 rounded-lg bg-amber-100 text-academic-amber font-mono text-sm font-bold flex items-center justify-center">
              01
            </span>
            <span class="text-xs font-mono text-ink-400 uppercase">Ось емкости</span>
          </div>
          <h3 class="text-lg font-serif font-bold text-ink-950">
            Финансовая емкость риска (Capacity)
          </h3>
          <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
            Объективная способность капитала переносить просадки. Оценивает наличие подушки безопасности, стабильность денежного потока и независимость базового уровня жизни от текущих колебаний портфеля.
          </p>
        </div>

        <!-- Vector 2 -->
        <div class="academic-card p-6 sm:p-7 space-y-3 bg-white hover:border-amber-400 transition-all">
          <div class="flex items-center justify-between">
            <span class="w-8 h-8 rounded-lg bg-amber-100 text-academic-amber font-mono text-sm font-bold flex items-center justify-center">
              02
            </span>
            <span class="text-xs font-mono text-ink-400 uppercase">Ось стресса</span>
          </div>
          <h3 class="text-lg font-serif font-bold text-ink-950">
            Эмоциональная стойкость (Stress Resilience)
          </h3>
          <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
            Психологический болевой порог при падении стоимости активов на 20–40%. Измеряет вероятность импульсивной капитуляции и фиксации убытка на самом дне рыночного спада под влиянием тревожных новостей.
          </p>
        </div>

        <!-- Vector 3 -->
        <div class="academic-card p-6 sm:p-7 space-y-3 bg-white hover:border-amber-400 transition-all">
          <div class="flex items-center justify-between">
            <span class="w-8 h-8 rounded-lg bg-amber-100 text-academic-amber font-mono text-sm font-bold flex items-center justify-center">
              03
            </span>
            <span class="text-xs font-mono text-ink-400 uppercase">Ось автономии</span>
          </div>
          <h3 class="text-lg font-serif font-bold text-ink-950">
            Автономия от хайпа (FOMO Control)
          </h3>
          <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
            Иммунитет к социальному доказательству и спекулятивному ажиотажу. Способность хладнокровно проходить мимо активов, которые взлетели на сотни процентов, не поддаваясь стадному инстинкту толпы.
          </p>
        </div>

        <!-- Vector 4 -->
        <div class="academic-card p-6 sm:p-7 space-y-3 bg-white hover:border-amber-400 transition-all">
          <div class="flex items-center justify-between">
            <span class="w-8 h-8 rounded-lg bg-amber-100 text-academic-amber font-mono text-sm font-bold flex items-center justify-center">
              04
            </span>
            <span class="text-xs font-mono text-ink-400 uppercase">Ось дисциплины</span>
          </div>
          <h3 class="text-lg font-serif font-bold text-ink-950">
            Стратегическая дисциплина (Discipline)
          </h3>
          <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
            Способность годами следовать выбранной стратегии вопреки рыночному шуму и боковому тренду, регулярно проводить плановую ребалансировку и не совершать спонтанных сделок.
          </p>
        </div>
      </div>
    </div>

    <!-- The 4-Step Analytical Pipeline -->
    <div class="academic-card p-6 sm:p-10 space-y-8 bg-white">
      <div class="space-y-1">
        <div class="badge-amber">АРХИТЕКТУРА СИСТЕМЫ</div>
        <h2 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950">
          Как устроена обработка и расчет
        </h2>
        <p class="text-xs text-ink-500 font-mono">
          От заполнения дилемм до формирования защитного протокола
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="p-5 rounded-xl bg-paper-50 border border-ink-200 space-y-2">
          <div class="text-xs font-mono text-academic-amber font-bold">ШАГ 01</div>
          <div class="text-base font-serif font-bold text-ink-950">12 дилемм</div>
          <p class="text-xs text-ink-600 leading-relaxed">
            Инвестор выбирает варианты поведения в реалистичных рыночных шоках и фазах ажиотажа.
          </p>
        </div>

        <div class="p-5 rounded-xl bg-paper-50 border border-ink-200 space-y-2">
          <div class="text-xs font-mono text-academic-amber font-bold">ШАГ 02</div>
          <div class="text-base font-serif font-bold text-ink-950">ИИ-анализ</div>
          <p class="text-xs text-ink-600 leading-relaxed">
            Аналитическая модель ИИ исследует структуру ответов на скрытые противоречия и когнитивные искажения.
          </p>
        </div>

        <div class="p-5 rounded-xl bg-paper-50 border border-ink-200 space-y-2">
          <div class="text-xs font-mono text-academic-amber font-bold">ШАГ 03</div>
          <div class="text-base font-serif font-bold text-ink-950">4D Радар-карта</div>
          <p class="text-xs text-ink-600 leading-relaxed">
            Калибруются 4 вектора мышления и определяется один из 8 инвестиционных психотипов.
          </p>
        </div>

        <div class="p-5 rounded-xl bg-paper-50 border border-ink-200 space-y-2">
          <div class="text-xs font-mono text-academic-amber font-bold">ШАГ 04</div>
          <div class="text-base font-serif font-bold text-ink-950">Стресс-модель</div>
          <p class="text-xs text-ink-600 leading-relaxed">
            Формируется модельный портфель и персональный протокол действий при рыночных спадах.
          </p>
        </div>
      </div>
    </div>

    <!-- Tech Stack -->
    <div class="academic-card p-6 sm:p-8 space-y-4 bg-white">
      <div class="text-xs font-mono text-ink-500 uppercase tracking-wider">Технологический стек платформы</div>
      <div class="flex flex-wrap gap-2 text-xs font-mono text-ink-700">
        <span class="px-3 py-1.5 rounded-lg bg-paper-50 border border-ink-200 font-semibold text-ink-900">Python 3.12</span>
        <span class="px-3 py-1.5 rounded-lg bg-paper-50 border border-ink-200">Django 5 + REST Framework</span>
        <span class="px-3 py-1.5 rounded-lg bg-paper-50 border border-ink-200 font-semibold text-academic-amber">AI Cognitive Scoring Engine</span>
        <span class="px-3 py-1.5 rounded-lg bg-paper-50 border border-ink-200">Vue 3.5 + Pinia + Vite</span>
        <span class="px-3 py-1.5 rounded-lg bg-paper-50 border border-ink-200">Tailwind CSS (Swiss Editorial Theme)</span>
        <span class="px-3 py-1.5 rounded-lg bg-paper-50 border border-ink-200">SVG Cognitive Radar Engine</span>
        <span class="px-3 py-1.5 rounded-lg bg-paper-50 border border-ink-200">PostgreSQL 16 / Nginx</span>
      </div>
    </div>

    <!-- Bottom CTA Bar -->
    <div class="p-8 sm:p-12 rounded-2xl bg-gradient-to-r from-ink-950 to-ink-900 text-white flex flex-col sm:flex-row items-center justify-between gap-6 shadow-xl">
      <div class="space-y-2 text-center sm:text-left">
        <h3 class="text-2xl font-serif font-bold text-amber-300">
          Узнайте свой когнитивный профиль
        </h3>
        <p class="text-xs sm:text-sm text-ink-300 max-w-md">
          12 поведенческих дилемм займут около 2.5 минут и защитят ваш капитал от импульсивных решений.
        </p>
      </div>

      <div class="flex items-center gap-3">
        <router-link 
          to="/survey" 
          class="px-6 py-3.5 rounded-xl bg-academic-amber hover:bg-amber-600 text-white font-sans font-medium text-sm transition-all shadow-md active:scale-[0.98]"
        >
          Пройти диагностику
        </router-link>
        <router-link 
          to="/contacts" 
          class="px-5 py-3.5 rounded-xl bg-ink-800 hover:bg-ink-700 text-ink-200 font-mono text-xs border border-ink-700 transition-all"
        >
          Методология
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
// Academic clean AboutView for Sirius Cognitive Investment Intelligence
</script>