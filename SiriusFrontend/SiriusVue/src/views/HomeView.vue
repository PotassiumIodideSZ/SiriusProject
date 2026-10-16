<template>
  <div class="space-y-20 sm:space-y-32 py-8 sm:py-14">
    <!-- ================================================================= -->
    <!-- SECTION 1: HERO WITH INTERACTIVE COGNITIVE RADAR                  -->
    <!-- ================================================================= -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
        <!-- LEFT: Editorial Pitch -->
        <div class="lg:col-span-6 space-y-6 sm:space-y-8">
          <!-- Scholarly Headline in Newsreader Serif -->
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-serif font-semibold text-ink-950 tracking-tight leading-[1.12]">
            Какая инвестиционная стратегия выдержит ваш характер?
          </h1>

          <!-- Academic Editorial Copy -->
          <p class="text-base sm:text-lg text-ink-700 font-normal leading-relaxed max-w-xl">
            Традиционные финансовые анкеты оценивают лишь текущий доход и формальный срок. Мы исследуем нейрокогнитивный отклик: устойчивость к рыночной панике, независимость от спекулятивного ажиотажа и способность следовать долгосрочной дисциплине.
          </p>

          <!-- Primary Actions -->
          <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 pt-1">
            <button 
              @click="handleStart"
              class="px-8 py-4 rounded-xl font-sans font-medium text-base bg-ink-950 hover:bg-ink-800 text-amber-300 shadow-md shadow-ink-950/10 hover:shadow-lg transition-all active:scale-[0.98] flex items-center justify-center gap-3 group"
            >
              <span>Пройти диагностику (12 дилемм)</span>
              <i class="fas fa-arrow-right text-xs group-hover:translate-x-1 transition-transform"></i>
            </button>
          </div>

          <!-- Bottom Micro-specs in Swiss Style -->
          <div class="pt-6 grid grid-cols-3 gap-4 border-t border-ink-200 text-xs font-mono">
            <div>
              <div class="text-ink-400">Признаки (Features):</div>
              <div class="text-ink-900 font-semibold mt-0.5">12 дилемм</div>
            </div>
            <div>
              <div class="text-ink-400">Длительность:</div>
              <div class="text-academic-amber font-semibold mt-0.5">~2.5 минуты</div>
            </div>
            <div>
              <div class="text-ink-400">Анализ:</div>
              <div class="text-ink-900 font-semibold mt-0.5">ИИ-модель</div>
            </div>
          </div>
        </div>

        <!-- RIGHT: LIVE COGNITIVE RADAR & ARCHETYPE SIMULATOR -->
        <div class="lg:col-span-6">
          <div class="academic-card p-6 sm:p-7 space-y-5 bg-white border-ink-200 shadow-sm">
            <!-- Header with Presets -->
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-ink-200/70 pb-3">
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-academic-amber animate-pulse"></span>
                <span class="text-xs font-mono font-bold text-ink-900 uppercase tracking-wider">
                  Когнитивный профиль · Модель
                </span>
              </div>
              <!-- Presets -->
              <div class="flex flex-wrap gap-1.5">
                <button 
                  v-for="preset in presets" 
                  :key="preset.id"
                  @click="applyPreset(preset)"
                  class="px-2.5 py-1 rounded-lg text-[11px] font-mono border transition-all"
                  :class="activePresetId === preset.id 
                    ? 'bg-ink-950 text-amber-300 border-ink-950 font-semibold' 
                    : 'bg-paper-50 text-ink-600 border-ink-200 hover:bg-white hover:text-ink-900'"
                >
                  {{ preset.label }}
                </button>
              </div>
            </div>

            <!-- CENTRAL COGNITIVE RADAR SVG -->
            <div class="relative w-full h-56 sm:h-60 flex items-center justify-center bg-paper-50/70 rounded-xl border border-ink-200/60 p-2 overflow-hidden">
              <svg viewBox="0 0 340 240" class="w-full h-full max-w-[340px]">
                <!-- Radar Guideline Diamond Rings -->
                <polygon points="170,30 270,120 170,210 70,120" fill="none" stroke="#E7E5E4" stroke-width="1" />
                <polygon points="170,52 245,120 170,188 95,120" fill="none" stroke="#E7E5E4" stroke-width="1" />
                <polygon points="170,75 220,120 170,165 120,120" fill="none" stroke="#E7E5E4" stroke-width="1" />
                <polygon points="170,98 195,120 170,142 145,120" fill="none" stroke="#E7E5E4" stroke-width="1" />

                <!-- Axes Lines -->
                <line x1="170" y1="30" x2="170" y2="210" stroke="#D6D3D1" stroke-width="1" stroke-dasharray="2" />
                <line x1="70" y1="120" x2="270" y2="120" stroke="#D6D3D1" stroke-width="1" stroke-dasharray="2" />

                <!-- Center point -->
                <circle cx="170" cy="120" r="2.5" fill="#A8A29E" />

                <!-- Axis Edge Labels -->
                <text x="170" y="20" text-anchor="middle" fill="#57534E" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600">
                  АНАЛИТИЧЕСКИЙ КОНТРОЛЬ
                </text>
                <text x="276" y="123" text-anchor="start" fill="#57534E" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600">
                  АВТОНОМИЯ
                </text>
                <text x="170" y="226" text-anchor="middle" fill="#57534E" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600">
                  ГОРИЗОНТ
                </text>
                <text x="64" y="123" text-anchor="end" fill="#57534E" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600">
                  СТОЙКОСТЬ
                </text>

                <!-- Dynamic Morphing Radar Polygon -->
                <polygon 
                  :points="radarPoints" 
                  fill="rgba(180, 83, 9, 0.16)" 
                  stroke="#B45309" 
                  stroke-width="2" 
                  stroke-linejoin="round"
                  class="transition-all duration-300 ease-out"
                />

                <!-- Point Markers with value tooltips -->
                <!-- Top (Logic) -->
                <circle :cx="radarCoords.top.x" :cy="radarCoords.top.y" r="4" fill="#B45309" stroke="#FFF" stroke-width="1.5" class="transition-all duration-300" />
                <text :x="radarCoords.top.x" :y="radarCoords.top.y - 7" text-anchor="middle" fill="#92400E" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold">
                  {{ vectors.logic }}%
                </text>

                <!-- Right (Autonomy) -->
                <circle :cx="radarCoords.right.x" :cy="radarCoords.right.y" r="4" fill="#B45309" stroke="#FFF" stroke-width="1.5" class="transition-all duration-300" />
                <text :x="radarCoords.right.x + 8" :y="radarCoords.right.y - 4" text-anchor="start" fill="#92400E" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold">
                  {{ vectors.autonomy }}%
                </text>

                <!-- Bottom (Horizon) -->
                <circle :cx="radarCoords.bottom.x" :cy="radarCoords.bottom.y" r="4" fill="#B45309" stroke="#FFF" stroke-width="1.5" class="transition-all duration-300" />
                <text :x="radarCoords.bottom.x" :y="radarCoords.bottom.y + 12" text-anchor="middle" fill="#92400E" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold">
                  {{ vectors.horizon }}%
                </text>

                <!-- Left (Drawdown resilience) -->
                <circle :cx="radarCoords.left.x" :cy="radarCoords.left.y" r="4" fill="#B45309" stroke="#FFF" stroke-width="1.5" class="transition-all duration-300" />
                <text :x="radarCoords.left.x - 8" :y="radarCoords.left.y - 4" text-anchor="end" fill="#92400E" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold">
                  {{ vectors.drawdown }}%
                </text>
              </svg>
            </div>

            <!-- 4 SLIDERS IN COMPACT 2x2 GRID -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-1">
              <!-- Vector 1: Logic -->
              <div class="space-y-1 bg-paper-50/60 p-2.5 rounded-xl border border-ink-200/60">
                <div class="flex justify-between items-center text-[11px] font-mono">
                  <span class="text-ink-700">1. Логика vs Импульс:</span>
                  <span class="text-academic-amber font-bold">{{ vectors.logic }}%</span>
                </div>
                <input 
                  type="range" 
                  min="20" 
                  max="100" 
                  step="5"
                  v-model.number="vectors.logic"
                  @input="activePresetId = null"
                  class="academic-range"
                />
              </div>

              <!-- Vector 2: Autonomy -->
              <div class="space-y-1 bg-paper-50/60 p-2.5 rounded-xl border border-ink-200/60">
                <div class="flex justify-between items-center text-[11px] font-mono">
                  <span class="text-ink-700">2. Иммунитет к толпе:</span>
                  <span class="text-academic-amber font-bold">{{ vectors.autonomy }}%</span>
                </div>
                <input 
                  type="range" 
                  min="20" 
                  max="100" 
                  step="5"
                  v-model.number="vectors.autonomy"
                  @input="activePresetId = null"
                  class="academic-range"
                />
              </div>

              <!-- Vector 3: Horizon -->
              <div class="space-y-1 bg-paper-50/60 p-2.5 rounded-xl border border-ink-200/60">
                <div class="flex justify-between items-center text-[11px] font-mono">
                  <span class="text-ink-700">3. Горизонт терпения:</span>
                  <span class="text-academic-amber font-bold">{{ vectors.horizon }}%</span>
                </div>
                <input 
                  type="range" 
                  min="20" 
                  max="100" 
                  step="5"
                  v-model.number="vectors.horizon"
                  @input="activePresetId = null"
                  class="academic-range"
                />
              </div>

              <!-- Vector 4: Drawdown Resilience -->
              <div class="space-y-1 bg-paper-50/60 p-2.5 rounded-xl border border-ink-200/60">
                <div class="flex justify-between items-center text-[11px] font-mono">
                  <span class="text-ink-700">4. Стойкость к просадкам:</span>
                  <span class="text-academic-amber font-bold">{{ vectors.drawdown }}%</span>
                </div>
                <input 
                  type="range" 
                  min="20" 
                  max="100" 
                  step="5"
                  v-model.number="vectors.drawdown"
                  @input="activePresetId = null"
                  class="academic-range"
                />
              </div>
            </div>

            <!-- RESULTING ARCHETYPE & ASSET MIX PANEL -->
            <div class="p-4 rounded-xl bg-paper-50 border border-ink-200 space-y-3.5">
              <!-- Archetype & Secondary Risk Tag -->
              <div class="flex items-center justify-between">
                <div>
                  <div class="text-[10px] font-mono text-ink-400 uppercase tracking-wider">Форма психотипа:</div>
                  <div class="text-base sm:text-lg font-serif font-bold text-ink-950 mt-0.5">
                    {{ currentProfile.name }}
                  </div>
                </div>
                <div class="text-right">
                  <div class="text-[10px] font-mono text-ink-400 uppercase tracking-wider">Индекс риска:</div>
                  <div class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-amber-100 text-academic-amber inline-block mt-0.5">
                    {{ calculatedRiskScore }}%
                  </div>
                </div>
              </div>

              <!-- Proportional Asset Bar -->
              <div class="space-y-1.5">
                <div class="flex justify-between text-[11px] font-mono text-ink-600">
                  <span>Расчетный портфель:</span>
                  <span>{{ calculatedAlloc.stocks }}% Акции / {{ calculatedAlloc.bonds }}% Облигации / {{ calculatedAlloc.cash }}% Ликвидность</span>
                </div>
                <div class="w-full h-2 rounded-full overflow-hidden flex bg-ink-100">
                  <div 
                    class="bg-amber-600 h-full transition-all duration-300"
                    :style="{ width: `${calculatedAlloc.stocks}%` }"
                    title="Акции"
                  ></div>
                  <div 
                    class="bg-sky-600 h-full transition-all duration-300"
                    :style="{ width: `${calculatedAlloc.bonds}%` }"
                    title="Облигации"
                  ></div>
                  <div 
                    class="bg-emerald-600 h-full transition-all duration-300"
                    :style="{ width: `${calculatedAlloc.cash}%` }"
                    title="Ликвидность"
                  ></div>
                </div>
              </div>

              <!-- Strengths & Behavioral Pitfall -->
              <div class="pt-2 border-t border-ink-200/60 grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                <div class="text-ink-700 leading-snug">
                  <span class="font-bold text-academic-sage font-mono text-[10px] block uppercase">Сильная сторона:</span>
                  {{ currentProfile.strength }}
                </div>
                <div class="text-ink-700 leading-snug">
                  <span class="font-bold text-academic-amber font-mono text-[10px] block uppercase">Слабое место:</span>
                  {{ currentProfile.weakness }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- SECTION 2: THE ANATOMY OF MARKET CYCLE DYNAMICS                   -->
    <!-- ================================================================= -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <div class="space-y-2.5 max-w-3xl">
        <div class="badge-amber">
          РЕАЛЬНЫЙ КЕЙС: ИНДЕКС S&P 500 (КРИЗИС 2007–2010 ГГ.)
        </div>
        <h2 class="text-3xl sm:text-4xl font-serif font-bold text-ink-950 tracking-tight">
          Анатомия рыночного цикла: точки входа толпы и когнитивные ловушки
        </h2>
        <p class="text-ink-600 text-base leading-relaxed">
          Сопоставление реальной исторической траектории индекса S&P 500 и индекса эмоционального фона инвесторов (жадность / паника). Нажмите на контрольные фазы, чтобы увидеть, где толпа входила на максимумах и капитулировала на дне:
        </p>
      </div>

      <!-- PROFESSIONAL CHART.JS GRAPHIC CONTAINER -->
      <div class="academic-card p-6 sm:p-8 space-y-6">
        <!-- Interactive Chart.js Component -->
        <MarketCycleChart 
          :phases="cyclePhases" 
          :active-phase="activePhaseIndex"
          @select-phase="activePhaseIndex = $event"
        />

        <!-- Active Phase Deep-Dive Triad Card (Outside the chart) -->
        <div class="p-6 rounded-2xl bg-paper-50 border border-ink-200 space-y-4">
          <!-- Active Phase Top Summary Bar -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-ink-200/80">
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <span 
                  class="text-[10px] font-mono px-2 py-0.5 rounded font-bold uppercase tracking-wider"
                  :class="currentPhase.type === 'crowd' ? 'bg-rose-100 text-rose-800 border border-rose-200' : 'bg-emerald-100 text-emerald-800 border border-emerald-200'"
                >
                  {{ currentPhase.type === 'crowd' ? 'Красная точка: Ошибка толпы' : 'Зеленая точка: Рациональный шаг' }}
                </span>
                <span class="text-xs font-mono font-semibold text-ink-600">{{ currentPhase.dateLabel }} · {{ currentPhase.priceLabel }}</span>
              </div>
              <h3 class="text-lg sm:text-xl font-serif font-bold text-ink-950">
                {{ currentPhase.title }}
              </h3>
            </div>
            <div class="text-xs font-mono font-medium px-3 py-1.5 rounded-lg bg-white border border-ink-200 text-ink-700 self-start sm:self-auto shadow-sm">
              {{ currentPhase.sentimentTag }}
            </div>
          </div>

          <!-- Deep-Dive 3 Columns: State, Trap, Defense Protocol -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-1">
            <!-- Col 1: Psychological Mindset -->
            <div class="space-y-2">
              <div class="text-[10px] font-mono text-academic-amber uppercase tracking-wider font-semibold">
                Психологическое состояние:
              </div>
              <div class="text-base font-serif font-bold text-ink-950 leading-snug">
                {{ currentPhase.emotionalState }}
              </div>
              <p class="text-xs text-ink-700 leading-relaxed pt-1">
                {{ currentPhase.behavior }}
              </p>
            </div>

            <!-- Col 2: Cognitive Bias Trap -->
            <div class="space-y-2">
              <div class="text-[10px] font-mono text-academic-crimson uppercase tracking-wider font-semibold">
                Когнитивная ловушка:
              </div>
              <div class="text-base font-serif font-bold text-ink-950 leading-snug">
                {{ currentPhase.biasName }}
              </div>
              <p class="text-xs text-ink-700 leading-relaxed pt-1">
                {{ currentPhase.biasDesc }}
              </p>
            </div>

            <!-- Col 3: Behavioral Defense Protocol -->
            <div class="space-y-2">
              <div class="text-[10px] font-mono text-academic-sage uppercase tracking-wider font-semibold">
                Защитный протокол инвестора:
              </div>
              <div class="text-base font-serif font-bold text-ink-950 leading-snug">
                {{ currentPhase.protocolTitle }}
              </div>
              <p class="text-xs text-ink-700 leading-relaxed pt-1">
                {{ currentPhase.protocolText }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ================================================================= -->
    <!-- SECTION 3: BOTTOM CALL TO ACTION                                  -->
    <!-- ================================================================= -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="academic-card p-8 sm:p-14 text-center space-y-6 bg-gradient-to-b from-white to-paper-50 border-ink-200">
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono font-medium bg-amber-50 text-academic-amber border border-amber-200 mx-auto">
          НАУЧНЫЙ ПОДХОД К КАПИТАЛУ
        </div>
        <h2 class="text-3xl sm:text-4xl font-serif font-bold text-ink-950 max-w-2xl mx-auto">
          Готовы проверить свою устойчивость к реальным колебаниям рынка?
        </h2>
        <p class="text-sm sm:text-base text-ink-600 max-w-xl mx-auto leading-relaxed">
          Тест из 12 дилемм выявит ваши персональные когнитивные слепые зоны и сформирует математически сбалансированный инвестиционный портфель.
        </p>
        <div class="pt-2">
          <button 
            @click="handleStart"
            class="px-10 py-4 rounded-xl font-sans font-medium text-base bg-ink-950 hover:bg-ink-800 text-amber-300 shadow-md shadow-ink-950/10 hover:shadow-lg transition-all active:scale-[0.98] inline-flex items-center gap-3"
          >
            <span>Начать диагностику</span>
            <i class="fas fa-arrow-right text-xs"></i>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/features/auth/stores/authStore'
import MarketCycleChart from '@/components/MarketCycleChart.vue'

const router = useRouter()
const authStore = useAuthStore()

const handleStart = () => {
  if (authStore.isAuthenticated) {
    router.push('/survey')
  } else {
    authStore.showLoginModal = true
  }
}

// =======================================================================
// COGNITIVE RADAR HERO SIMULATOR
// =======================================================================
// 4 vectors (0..100)
const vectors = reactive({
  logic: 75,     // Top (Analytical control vs Emotion)
  autonomy: 60,  // Right (Independence vs Herd mentality)
  horizon: 70,   // Bottom (Time horizon & Patience)
  drawdown: 50   // Left (Stress & Drawdown resilience)
})

const activePresetId = ref('balanced')

const presets = [
  { id: 'conservative', label: 'Консервативный', logic: 85, autonomy: 45, horizon: 40, drawdown: 30 },
  { id: 'balanced', label: 'Сбалансированный', logic: 75, autonomy: 65, horizon: 70, drawdown: 55 },
  { id: 'growth', label: 'Оптимист роста', logic: 70, autonomy: 75, horizon: 85, drawdown: 75 },
  { id: 'aggressive', label: 'Агрессивный', logic: 60, autonomy: 85, horizon: 90, drawdown: 90 }
]

const applyPreset = (preset) => {
  activePresetId.value = preset.id
  vectors.logic = preset.logic
  vectors.autonomy = preset.autonomy
  vectors.horizon = preset.horizon
  vectors.drawdown = preset.drawdown
}

// Radar Geometry Math (Center 170, 120, Radius 90)
const radarCoords = computed(() => {
  const cx = 170
  const cy = 120
  const maxR = 90

  return {
    top: { x: cx, y: cy - (vectors.logic / 100) * maxR },
    right: { x: cx + (vectors.autonomy / 100) * maxR, y: cy },
    bottom: { x: cx, y: cy + (vectors.horizon / 100) * maxR },
    left: { x: cx - (vectors.drawdown / 100) * maxR, y: cy }
  }
})

const radarPoints = computed(() => {
  const c = radarCoords.value
  return `${c.top.x},${c.top.y} ${c.right.x},${c.right.y} ${c.bottom.x},${c.bottom.y} ${c.left.x},${c.left.y}`
})

// Risk Score (secondary metric)
const calculatedRiskScore = computed(() => {
  const raw = (vectors.drawdown * 0.35) + (vectors.autonomy * 0.25) + (vectors.horizon * 0.20) + (vectors.logic * 0.20)
  return Math.min(95, Math.max(15, Math.round(raw)))
})

// Asset Allocation recomputed from vector shape
const calculatedAlloc = computed(() => {
  const score = calculatedRiskScore.value
  let stocks, bonds, cash
  if (score < 40) {
    stocks = 20
    bonds = 60
    cash = 20
  } else if (score < 62) {
    stocks = 45
    bonds = 40
    cash = 15
  } else if (score < 80) {
    stocks = 65
    bonds = 25
    cash = 10
  } else {
    stocks = 80
    bonds = 15
    cash = 5
  }
  return { stocks, bonds, cash }
})

// Dominant Archetype Classification from polygon geometry
const currentProfile = computed(() => {
  const score = calculatedRiskScore.value

  if (score < 40) {
    return {
      name: 'Консервативный инвестор (Защитный)',
      strength: 'Максимальная защита капитала и минимальный психологический стресс при рыночной волатильности.',
      weakness: 'Риск отставания от инфляции при длительном нахождении в защитных инструментах.'
    }
  }

  if (score < 62) {
    return {
      name: 'Сбалансированный инвестор (Умеренный)',
      strength: 'Гармоничный баланс между приростом капитала и контролем эмоционального напряжения.',
      weakness: 'Склонность к сомнениям в точках экстремальной рыночной неопределенности.'
    }
  }

  if (score < 80) {
    return {
      name: 'Оптимист роста (Стратегический)',
      strength: 'Высокая автономия мышления и готовность дисциплинированно пересиживать глубокие коррекции.',
      weakness: 'Периодическая недооценка краткосрочных рисков ликвидности.'
    }
  }

  return {
    name: 'Агрессивный инвестор (Максимальный риск)',
    strength: 'Высочайший аппетит к риску и нацеленность на опережающую долгосрочную доходность.',
    weakness: 'Склонность к избыточной самоуверенности на пиках рыночного ажиотажа.'
  }
})

// =======================================================================
// MARKET CYCLE PHASES DATA
// =======================================================================
const activePhaseIndex = ref(0)

const cyclePhases = [
  {
    shortTitle: 'Пик и эйфория',
    dateLabel: 'Окт 2007',
    priceLabel: '1549 п. (High 1576)',
    type: 'crowd',
    targetDate: '2007-10-01',
    title: '1. Октябрь 2007 г. — Исторический максимум (1549 п.)',
    biasLabel: 'Жадность толпы',
    sentimentLevel: 'greed',
    sentimentTag: 'Жадность: 92/100',
    emotionalState: '«Рынок на вечном подъеме, недвижимость надежна, надо входить полным объемом»',
    behavior: 'Массовый приток розничных инвесторов на абсолютных пиках котировок. Покупка дорогих акций с кредитным плечом.',
    biasName: 'Иллюзия бесконечного роста и стадный инстинкт',
    biasDesc: 'Экстраполяция недавней прибыльности в будущее и страх упустить растущий тренд без оглядки на перегретость мультипликаторов.',
    protocolTitle: 'Фиксация прибыли и ребалансировка',
    protocolText: 'Плановое снижение доли акций в пользу надежных краткосрочных бондов при экстремальном отклонении цены вверх от 200-дневной средней.'
  },
  {
    shortTitle: 'Ложный отскок',
    dateLabel: 'Май 2008',
    priceLabel: '1400 п.',
    type: 'crowd',
    targetDate: '2008-05-01',
    title: '2. Май 2008 г. — Ложный отскок и отрицание (1400 п.)',
    biasLabel: 'Отрицание риска',
    sentimentLevel: 'calm',
    sentimentTag: 'Нейтрально: 55/100',
    emotionalState: '«Кризис ипотеки позади, это рядовая просадка, сейчас отскочим на новые рекорды»',
    behavior: 'Попытка агрессивно выкупать каждое снижение без анализа ухудшения системной ликвидности и краха инвестбанков.',
    biasName: 'Неприятие потерь и эффект подтверждения',
    biasDesc: 'Инвестор ищет только оптимистичные комментарии в СМИ и игнорирует сигналы фундаментального кризиса ликвидности.',
    protocolTitle: 'Аудит качества эмитентов',
    protocolText: 'Оценка долговой нагрузки компаний и отказ от усреднения убыточных позиций в цикличных и закредитованных секторах.'
  },
  {
    shortTitle: 'Крах Lehman',
    dateLabel: 'Ноя 2008',
    priceLabel: '896 п.',
    type: 'crowd',
    targetDate: '2008-11-01',
    title: '3. Ноябрь 2008 г. — Крах Lehman Brothers и шок (896 п.)',
    biasLabel: 'Шок и паника',
    sentimentLevel: 'fear',
    sentimentTag: 'Страх: 25/100',
    emotionalState: '«Финансовая система рушится, банки банкротятся, спасти хоть какие-то крохи»',
    behavior: 'Массовое закрытие позиций по маржин-коллам, принудительные ликвидации портфелей, паралич принятия решений.',
    biasName: 'Каскадная паника и близорукое неприятие потерь',
    biasDesc: 'Резкое сокращение горизонта планирования с 10 лет до 1 дня. Эмоциональный центр мозга подавляет аналитический расчет.',
    protocolTitle: 'Защитный мораторий на импульсивные действия',
    protocolText: 'Принудительная пауза 48 часов перед совершением любых экстренных сделок для исключения продажи активов на эмоциональном пике стресса.'
  },
  {
    shortTitle: 'Дно и капитуляция',
    dateLabel: 'Мар 2009',
    priceLabel: '676 п. (Low 666)',
    type: 'rational',
    targetDate: '2009-03-01',
    title: '4. Март 2009 г. — Историческое дно капитуляции (676 п.)',
    biasLabel: 'Точка разворота',
    sentimentLevel: 'fear',
    sentimentTag: 'Паника толпы: 8/100',
    emotionalState: 'Толпа кричит: «Акции больше никогда не вырастут!». Рациональный инвестор планомерно заходит на распродаже.',
    behavior: 'Пока толпа в ужасе сбрасывает бумаги на ценовом минимуме 666 п., хладнокровный инвестор методично выкупает фундаментально дешевые акции.',
    biasName: 'Максимальная боль потерь vs Оппортунизм',
    biasDesc: 'Психологический слом толпы: невыносимость наблюдения бумажного убытка заставляет отдавать активы умным деньгам.',
    protocolTitle: 'Рациональный оппортунизм Баффета',
    protocolText: '«Покупай, когда на улицах льется кровь». Регулярный плановый набор индексных долей на фазе ультрадешевых фундаментальных оценок.'
  },
  {
    shortTitle: 'Восстановление',
    dateLabel: 'Окт 2009',
    priceLabel: '1036 п.',
    type: 'rational',
    targetDate: '2009-10-01',
    title: '5. Октябрь 2009 г. — Мощный отскок и подтверждение тренда (1036 п.)',
    biasLabel: 'Тренд вверх',
    sentimentLevel: 'calm',
    sentimentTag: 'Скепсис: 40/100',
    emotionalState: '«Это ловушка для дураков, вот-вот упадем ниже 500». Инвестор: следование за подтвержденным трендом.',
    behavior: 'Толпа сидит в наличных деньгах и депозитах, упуская +50% роста. Системный инвестор наращивает позицию по тренду.',
    biasName: 'Посттравматическое якорение на кризисе',
    biasDesc: 'Пережитый стресс блокирует рациональные инвестиции даже тогда, когда макроэкономические стимулы и ликвидность уже развернули рынок.',
    protocolTitle: 'Системное усреднение DCA (Dollar-Cost Averaging)',
    protocolText: 'Автоматические равные регулярные инвестиции по фиксированному графику исключают попытки угадать идеальное время входа.'
  }
]

const currentPhase = computed(() => cyclePhases[activePhaseIndex.value])
</script>