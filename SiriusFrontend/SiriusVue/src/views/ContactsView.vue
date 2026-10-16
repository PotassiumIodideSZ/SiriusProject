<template>
  <div class="max-w-5xl mx-auto py-12 px-4 sm:px-6 lg:px-8 space-y-16">
    <!-- Header -->
    <div class="space-y-4">
      <div class="badge-amber">НАУЧНЫЙ БАЗИС И МЕТОД</div>
      <h1 class="text-3xl sm:text-5xl font-serif font-bold text-ink-950 tracking-tight leading-[1.15]">
        Методология когнитивного моделирования
      </h1>
      <p class="text-base sm:text-lg text-ink-700 leading-relaxed max-w-3xl">
        Как рассчитывается психологический профиль инвестора, почему 12 дилемм эффективнее классических тестов и как устроена матрица когнитивных искажений.
      </p>
    </div>

    <!-- Academic Foundations: 3 Nobel Laureates -->
    <div class="space-y-6">
      <div class="space-y-1">
        <div class="badge-amber">ТЕОРЕТИЧЕСКИЙ ФУНДАМЕНТ</div>
        <h2 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950">
          Три столпа поведенческих финансов
        </h2>
        <p class="text-sm text-ink-600 max-w-2xl">
          Математический аппарат платформы базируется на открытиях лауреатов Нобелевской премии по экономике:
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Theory 1: Prospect Theory -->
        <div class="academic-card p-6 sm:p-7 space-y-4 bg-white flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold text-academic-amber px-2.5 py-1 rounded bg-amber-50 border border-amber-200">
                1979 · 2002
              </span>
              <span class="text-[11px] font-mono text-ink-400">Нобелевская премия</span>
            </div>
            <h3 class="text-lg font-serif font-bold text-ink-950">
              Теория перспектив
            </h3>
            <div class="text-xs font-mono text-ink-500">
              Даниэль Канеман & Амос Тверски
            </div>
            <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
              Люди асимметрично реагируют на риски: боль от потери 100 000 ₽ субъективно переживается в <strong class="text-ink-950">2.5 раза острее</strong>, чем радость от приобретения аналогичной суммы. Это толкает инвесторов к импульсивным продажам на дне и удержанию безнадежных убытков.
            </p>
          </div>
          <div class="pt-3 border-t border-ink-100 text-[11px] font-mono text-academic-amber font-semibold">
            Ключевой фактор: Ось стресс-стойкости
          </div>
        </div>

        <!-- Theory 2: Mental Accounting -->
        <div class="academic-card p-6 sm:p-7 space-y-4 bg-white flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold text-academic-amber px-2.5 py-1 rounded bg-amber-50 border border-amber-200">
                1985 · 2017
              </span>
              <span class="text-[11px] font-mono text-ink-400">Нобелевская премия</span>
            </div>
            <h3 class="text-lg font-serif font-bold text-ink-950">
              Ментальный учет (Mental Accounting)
            </h3>
            <div class="text-xs font-mono text-ink-500">
              Ричард Талер
            </div>
            <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
              Деньги не являются однородными в восприятии человека. Прибыль с акций воспринимается как «деньги казино», что провоцирует опасные сверхрисковые ставки. Sirius объединяет весь капитал в строгие балансирующие правила.
            </p>
          </div>
          <div class="pt-3 border-t border-ink-100 text-[11px] font-mono text-academic-amber font-semibold">
            Ключевой фактор: Ось финансовой емкости
          </div>
        </div>

        <!-- Theory 3: Irrational Exuberance -->
        <div class="academic-card p-6 sm:p-7 space-y-4 bg-white flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold text-academic-amber px-2.5 py-1 rounded bg-amber-50 border border-amber-200">
                2000 · 2013
              </span>
              <span class="text-[11px] font-mono text-ink-400">Нобелевская премия</span>
            </div>
            <h3 class="text-lg font-serif font-bold text-ink-950">
              Иррациональный оптимизм и толпа
            </h3>
            <div class="text-xs font-mono text-ink-500">
              Роберт Шиллер
            </div>
            <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
              Рыночные пузыри и мании формируются стадным поведением и социальным заражением (FOMO). Наш тест выявляет восприимчивость к информационному шуму и чужим «успешным сделкам».
            </p>
          </div>
          <div class="pt-3 border-t border-ink-100 text-[11px] font-mono text-academic-amber font-semibold">
            Ключевой фактор: Ось автономии от хайпа
          </div>
        </div>
      </div>
    </div>

    <!-- The 12 Dilemma Matrix -->
    <div class="academic-card p-6 sm:p-10 space-y-6 bg-white">
      <div class="space-y-1">
        <div class="badge-amber">СТРУКТУРА ОПРОСА</div>
        <h2 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950">
          Матрица 12 ситуационных дилемм
        </h2>
        <p class="text-xs sm:text-sm text-ink-600 max-w-2xl">
          Вместо самооценки вроде «Любите ли вы рисковать?» мы погружаем инвестора в модели реальных кризисных ситуаций:
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
        <div class="p-4 rounded-xl bg-paper-50 border border-ink-200 space-y-2">
          <div class="flex items-center gap-2 text-academic-amber font-mono text-xs font-bold">
            <span class="w-5 h-5 rounded-full bg-amber-100 flex items-center justify-center text-[11px]">I</span>
            <span>Дилеммы стресса и просадки (Q1 – Q3)</span>
          </div>
          <p class="text-xs text-ink-700 leading-relaxed">
            Рыночный обвал -30%, резкое падение котировок ключевого актива, тревожный новостной фон. Измеряется склонность к экстренной продаже на самом дне.
          </p>
        </div>

        <div class="p-4 rounded-xl bg-paper-50 border border-ink-200 space-y-2">
          <div class="flex items-center gap-2 text-academic-amber font-mono text-xs font-bold">
            <span class="w-5 h-5 rounded-full bg-amber-100 flex items-center justify-center text-[11px]">II</span>
            <span>Дилеммы социального давления и FOMO (Q4 – Q6)</span>
          </div>
          <p class="text-xs text-ink-700 leading-relaxed">
            Взрывной рост хайпового актива, советы «гуру» из соцсетей, истории знакомых о сверхприбылях. Проверяется способность не покупать на вершине.
          </p>
        </div>

        <div class="p-4 rounded-xl bg-paper-50 border border-ink-200 space-y-2">
          <div class="flex items-center gap-2 text-academic-amber font-mono text-xs font-bold">
            <span class="w-5 h-5 rounded-full bg-amber-100 flex items-center justify-center text-[11px]">III</span>
            <span>Дилеммы аллокации и распределения (Q7 – Q9)</span>
          </div>
          <p class="text-xs text-ink-700 leading-relaxed">
            Поступление крупного бонуса, распределение между защитными облигациями и акциями, правила фиксации бумажного убытка.
          </p>
        </div>

        <div class="p-4 rounded-xl bg-paper-50 border border-ink-200 space-y-2">
          <div class="flex items-center gap-2 text-academic-amber font-mono text-xs font-bold">
            <span class="w-5 h-5 rounded-full bg-amber-100 flex items-center justify-center text-[11px]">IV</span>
            <span>Дилеммы горизонта и дисциплины (Q10 – Q12)</span>
          </div>
          <p class="text-xs text-ink-700 leading-relaxed">
            3 года изнуряющего бокового тренда без явного роста, ребалансировка портфеля по графику вопреки эмоциям, устойчивость к спекуляциям.
          </p>
        </div>
      </div>
    </div>

    <!-- INTERACTIVE COGNITIVE BIASES EXPLORER -->
    <div class="academic-card p-6 sm:p-10 space-y-8 bg-white border-amber-300/80 shadow-sm">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-ink-200 pb-4">
        <div class="space-y-1">
          <div class="badge-amber">ИНТЕРАКТИВНЫЙ АТЛАС</div>
          <h2 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950">
            5 ключевых когнитивных ловушек
          </h2>
          <p class="text-xs sm:text-sm text-ink-600">
            Нажмите на искажение, чтобы изучить его механизм, исторический прецедент и защитное правило:
          </p>
        </div>
      </div>

      <!-- Bias Tabs -->
      <div class="flex flex-wrap gap-2">
        <button 
          v-for="(bias, idx) in cognitiveBiases" 
          :key="bias.id"
          @click="activeBiasIndex = idx"
          class="px-3.5 py-2 rounded-xl text-xs font-mono border transition-all"
          :class="activeBiasIndex === idx 
            ? 'bg-ink-950 text-amber-300 border-ink-950 font-bold shadow-sm' 
            : 'bg-paper-50 text-ink-700 border-ink-200 hover:bg-white hover:text-ink-950'"
        >
          {{ bias.shortName }}
        </button>
      </div>

      <!-- Active Bias Detailed Card -->
      <div class="p-6 sm:p-8 rounded-2xl bg-paper-50/80 border border-ink-200 space-y-6 transition-all">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-ink-200/70 pb-4">
          <div>
            <span class="text-xs font-mono text-academic-amber font-semibold uppercase tracking-wider">
              {{ currentBias.category }}
            </span>
            <h3 class="text-xl sm:text-2xl font-serif font-bold text-ink-950 mt-1">
              {{ currentBias.fullName }}
            </h3>
          </div>
          <span class="px-3 py-1 rounded-full text-xs font-mono font-medium bg-red-50 text-academic-crimson border border-red-200 self-start sm:self-auto">
            Опасность для портфеля: {{ currentBias.riskLevel }}
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs sm:text-sm">
          <!-- Column 1: Mechanism -->
          <div class="space-y-2">
            <div class="text-[11px] font-mono text-ink-400 uppercase tracking-wider font-semibold">
              Психологический механизм:
            </div>
            <p class="text-ink-800 leading-relaxed">
              {{ currentBias.mechanism }}
            </p>
          </div>

          <!-- Column 2: Historical Precedent -->
          <div class="space-y-2">
            <div class="text-[11px] font-mono text-ink-400 uppercase tracking-wider font-semibold">
              Исторический прецедент:
            </div>
            <p class="text-ink-800 leading-relaxed">
              {{ currentBias.precedent }}
            </p>
          </div>

          <!-- Column 3: Defense Protocol -->
          <div class="space-y-2 p-4 rounded-xl bg-amber-50/70 border border-amber-200/80">
            <div class="text-[11px] font-mono text-academic-amber uppercase tracking-wider font-bold flex items-center gap-1.5">
              <i class="fas fa-shield-alt"></i>
              <span>Защитный протокол Sirius:</span>
            </div>
            <p class="text-ink-900 font-mono text-xs leading-relaxed font-medium">
              {{ currentBias.defenseProtocol }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Feedback & Academic Inquiries -->
    <div class="academic-card p-6 sm:p-10 space-y-6 bg-white">
      <div class="space-y-1">
        <div class="badge-amber">ОБРАТНАЯ СВЯЗЬ И ОБСУЖДЕНИЕ</div>
        <h2 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950">
          Вопросы и предложения по методологии
        </h2>
        <p class="text-sm text-ink-600 leading-relaxed max-w-2xl">
          Проект находится в стадии исследовательской разработки. Если у вас есть предложения по калибровке дилемм, расчету психотипов или вы хотите обсудить формулы и стресс-модели — напишите нам через форму ниже.
        </p>
      </div>

      <!-- Feedback Sent State -->
      <div v-if="feedbackSent" class="p-8 rounded-2xl bg-amber-50/70 border border-amber-200 text-center space-y-3 max-w-xl">
        <div class="w-12 h-12 rounded-full bg-academic-amber text-white flex items-center justify-center mx-auto text-xl">
          <i class="fas fa-check"></i>
        </div>
        <h3 class="text-lg font-serif font-bold text-ink-950">Сообщение отправлено</h3>
        <p class="text-xs sm:text-sm text-ink-700 max-w-md mx-auto">
          Спасибо за обратную связь! Ваше мнение помогает калибровать когнитивные дилеммы и совершенствовать математическую модель.
        </p>
        <button 
          @click="resetFeedback" 
          class="px-4 py-2 rounded-xl bg-white border border-ink-200 text-xs font-mono text-ink-800 hover:bg-paper-50 transition"
        >
          Отправить еще сообщение
        </button>
      </div>

      <!-- Feedback Form -->
      <form v-else @submit.prevent="submitFeedback" class="space-y-4 max-w-xl">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="space-y-1">
            <label class="text-xs font-mono text-ink-600">Ваше имя</label>
            <input 
              v-model="feedbackForm.name"
              type="text" 
              required
              placeholder="Константин" 
              class="w-full px-3.5 py-2.5 rounded-xl border border-ink-200 bg-paper-50 text-ink-900 text-xs sm:text-sm focus:outline-none focus:border-academic-amber focus:bg-white transition"
            />
          </div>
          <div class="space-y-1">
            <label class="text-xs font-mono text-ink-600">Email для ответа</label>
            <input 
              v-model="feedbackForm.email"
              type="email" 
              required
              placeholder="name@example.com" 
              class="w-full px-3.5 py-2.5 rounded-xl border border-ink-200 bg-paper-50 text-ink-900 text-xs sm:text-sm focus:outline-none focus:border-academic-amber focus:bg-white transition"
            />
          </div>
        </div>

        <div class="space-y-1">
          <label class="text-xs font-mono text-ink-600">Тема обращения</label>
          <select 
            v-model="feedbackForm.topic"
            class="w-full px-3.5 py-2.5 rounded-xl border border-ink-200 bg-paper-50 text-ink-900 text-xs sm:text-sm focus:outline-none focus:border-academic-amber focus:bg-white transition"
          >
            <option value="methodology">Вопрос или замечание по методологии</option>
            <option value="dilemma">Предложение по формулировке дилемм</option>
            <option value="scoring">Вопрос по расчету риск-индекса и радара</option>
            <option value="collaboration">Сотрудничество и предложения</option>
            <option value="other">Другое</option>
          </select>
        </div>

        <div class="space-y-1">
          <label class="text-xs font-mono text-ink-600">Сообщение</label>
          <textarea 
            v-model="feedbackForm.message"
            required
            rows="4" 
            placeholder="Опишите ваше предложение или вопрос..." 
            class="w-full px-3.5 py-2.5 rounded-xl border border-ink-200 bg-paper-50 text-ink-900 text-xs sm:text-sm focus:outline-none focus:border-academic-amber focus:bg-white transition"
          ></textarea>
        </div>

        <div class="pt-1">
          <button 
            type="submit" 
            class="px-6 py-3 rounded-xl bg-ink-950 hover:bg-ink-800 text-amber-300 font-sans font-medium text-xs sm:text-sm shadow-sm transition-all active:scale-[0.98] flex items-center gap-2"
          >
            <span>Отправить сообщение</span>
            <i class="fas fa-paper-plane text-xs"></i>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

const activeBiasIndex = ref(0)
const feedbackSent = ref(false)

const feedbackForm = reactive({
  name: '',
  email: '',
  topic: 'methodology',
  message: ''
})

const submitFeedback = () => {
  // Store feedback message locally
  try {
    const list = JSON.parse(localStorage.getItem('user_feedback') || '[]')
    list.push({ ...feedbackForm, date: new Date().toISOString() })
    localStorage.setItem('user_feedback', JSON.stringify(list))
  } catch (e) {
    console.warn('Feedback save warning:', e)
  }
  feedbackSent.value = true
}

const resetFeedback = () => {
  feedbackForm.name = ''
  feedbackForm.email = ''
  feedbackForm.topic = 'methodology'
  feedbackForm.message = ''
  feedbackSent.value = false
}

const cognitiveBiases = [
  {
    id: 'loss_aversion',
    shortName: 'Неприятие потерь',
    fullName: 'Неприятие потерь (Loss Aversion)',
    category: 'Фундаментальное искажение Канемана-Тверски',
    riskLevel: 'Критический',
    mechanism: 'Мозг воспринимает убыток как физическую угрозу. Инвестор затягивает продажу неудачного актива, надеясь «выйти хотя бы в безубыток», превращая временную коррекцию в катастрофическую потерю 80–90% депозита.',
    precedent: 'Крах технологических акций пузыря доткомов (2000–2002) и массовое банкротство ритейл-инвесторов, державших падающие бумаги до конца.',
    defenseProtocol: '«Правило жесткого стоп-приказа и переоценки тезиса: если инвестиционный фундамент компании разрушен, позиция закрывается независимо от накопленного убытка».'
  },
  {
    id: 'fomo',
    shortName: 'Синдром FOMO',
    fullName: 'Синдром упущенной выгоды (FOMO)',
    category: 'Стадный эффект и социальное давление',
    riskLevel: 'Высокий',
    mechanism: 'Видя стремительный рост малопонятного актива и читая отчеты знакомых о легких деньгах, инвестор капитулирует перед жадностью и входит максимальным объемом на самом пике ралли.',
    precedent: 'Пик мем-акций и спекулятивных активов в ноябре 2021 года, когда приток розничных покупателей на хаях привел к последующей просадке портфелей на 70%.',
    defenseProtocol: '«Фильтр 48 часов и запрет на вход после ралли >50%: активы, показавшие параболический рост, исключаются из покупок до формирования консолидации».'
  },
  {
    id: 'sunk_cost',
    shortName: 'Невозвратные затраты',
    fullName: 'Ловушка невозвратных затрат (Sunk Cost Fallacy)',
    category: 'Психологическая привязанность к прошлым вложениям',
    riskLevel: 'Высокий',
    mechanism: 'Инвестор продолжает направлять свежий капитал в убыточный проект или акцию только потому, что туда уже было вложено много денег и сил, вместо поиска более доходных альтернатив.',
    precedent: 'Многократное неконтролируемое усреднение позиций в банкротящихся компаниях (Enron, Lehman Brothers, Wirecard).',
    defenseProtocol: '«Принцип чистой страницы: задайте себе вопрос — вложил бы я деньги в эту компанию сегодня с нуля? Если ответ отрицательный, усреднение запрещено».'
  },
  {
    id: 'overconfidence',
    shortName: 'Самоуверенность',
    fullName: 'Избыточная самоуверенность (Overconfidence Bias)',
    category: 'Иллюзия превосходства над рынком',
    riskLevel: 'Умеренно-высокий',
    mechanism: 'Серия удачных сделок на растущем «бычьем» рынке приписывается исключительно собственному гению, а не общему тренду. Это ведет к завышению рисков, плечам и игнорированию диверсификации.',
    precedent: 'Рынок 2020–2021 годов: миллионы новичков с плечами считали себя профессиональными трейдерами, пока ужесточение ставки ФРС не вызвало маржин-коллы.',
    defenseProtocol: '«Ограничение максимальной доли одного эмитента 5–7% от капитала и обязательный запрет маржинальных плеч в долгосрочном портфеле».'
  },
  {
    id: 'anchoring',
    shortName: 'Эффект якоря',
    fullName: 'Эффект якоря (Anchoring Bias)',
    category: 'Фиксация на исторической цене',
    riskLevel: 'Средний',
    mechanism: 'Инвестор психологически привязывается к историческому максимуму цены (например, $200 за акцию) и считает цену $120 «дешевой», игнорируя изменившуюся бизнес-реальность эмитента.',
    precedent: 'Покупка акций падающих телекомов и розничных сетей, которые потеряли рыночную долю, но казались «дешевыми» относительно своих пиков.',
    defenseProtocol: '«Оценка по текущим финансовым мультипликаторам и свободному денежному потоку, а не по графику прошлой максимальной цены».'
  }
]

const currentBias = computed(() => cognitiveBiases[activeBiasIndex.value])
</script>