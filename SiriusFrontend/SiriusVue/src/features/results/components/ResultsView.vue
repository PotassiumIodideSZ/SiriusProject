<template>
  <div class="min-h-screen py-10 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto space-y-10">
    <!-- Top Action Bar -->
    <div class="flex items-center justify-between border-b border-ink-200 pb-6">
      <div class="space-y-1">
        <div class="badge-amber">РЕЗУЛЬТАТЫ ML-СКОРИНГА</div>
        <h1 class="text-2xl sm:text-4xl font-serif font-bold text-ink-950 tracking-tight">
          Паспорт инвестиционного профиля
        </h1>
      </div>
      <router-link 
        to="/" 
        class="px-4 py-2 rounded-xl bg-white hover:bg-paper-50 text-ink-700 hover:text-ink-950 border border-ink-200 text-xs font-mono shadow-sm transition-all flex items-center gap-2"
      >
        <i class="fas fa-home text-xs"></i>
        <span>На главную</span>
      </router-link>
    </div>
    
    <!-- Loading State -->
    <div v-if="isLoading" class="academic-card p-16 text-center space-y-4">
      <div class="inline-block w-10 h-10 border-2 border-academic-amber border-t-transparent rounded-full animate-spin"></div>
      <div class="text-ink-950 text-base font-serif font-bold">ML-модель рассчитывает скоринг и профиль...</div>
      <div class="text-ink-500 text-xs font-mono">Кластеризация признаков и расчет риск-профиля</div>
    </div>
    
    <!-- Error State -->
    <div v-else-if="error" class="academic-card p-10 text-center space-y-4 border-red-200">
      <div class="text-academic-crimson text-base font-mono">{{ error }}</div>
      <button 
        @click="fetchInvestmentProfile" 
        class="px-6 py-2.5 rounded-xl bg-ink-100 hover:bg-ink-200 text-ink-800 text-xs font-mono transition"
      >
        Обновить профиль
      </button>
    </div>
    
    <!-- Main Results Container -->
    <div v-else class="space-y-10">
      <!-- ROW 1: PRIMARY METRICS, COGNITIVE RADAR & ASSET ALLOCATION -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        <!-- Col 1: Circular Score Card & Archetype (5 cols) -->
        <div class="lg:col-span-5 academic-card p-6 sm:p-8 flex flex-col justify-between space-y-6 bg-white">
          <div class="space-y-6 flex flex-col items-center text-center">
            <div class="text-xs font-mono text-ink-500 uppercase tracking-wider">Интегральный риск-индекс</div>
            
            <!-- Circular SVG Gauge -->
            <div class="relative w-44 h-44 sm:w-48 sm:h-48">
              <svg class="w-full h-full transform -rotate-90">
                <circle
                  cx="96"
                  cy="96"
                  r="80"
                  stroke="#E7E5E4"
                  stroke-width="11"
                  fill="none"
                />
                <circle
                  cx="96"
                  cy="96"
                  r="80"
                  stroke="url(#amberGradient)"
                  stroke-width="11"
                  stroke-linecap="round"
                  fill="none"
                  :stroke-dasharray="circumference"
                  :stroke-dashoffset="dashOffset"
                  class="transition-all duration-1000 ease-out"
                />
                <defs>
                  <linearGradient id="amberGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#D97706" />
                    <stop offset="100%" stop-color="#B45309" />
                  </linearGradient>
                </defs>
              </svg>
              <!-- Center Percent -->
              <div class="absolute inset-0 flex flex-col items-center justify-center">
                <span class="text-4xl sm:text-5xl font-mono font-bold text-ink-950 tracking-tighter">{{ riskScore }}%</span>
                <span class="text-[10px] font-mono text-ink-400 mt-0.5 uppercase tracking-wider">ГОТОВНОСТЬ</span>
              </div>
            </div>

            <!-- Category Pill -->
            <div class="flex flex-col items-center gap-1.5 w-full">
              <div 
                class="px-4 py-1.5 rounded-xl text-xs font-mono font-bold uppercase tracking-wider border shadow-sm"
                :class="getCategoryBadgeClass(riskCategory)"
              >
                {{ getCategoryLabel(riskCategory) }}
              </div>
              <span class="text-[11px] text-ink-500 font-mono">Категория инвестиционного профиля</span>
            </div>

            <!-- Archetype Feature Box -->
            <div v-if="archetype" class="w-full text-left pt-4 border-t border-ink-200 space-y-2 bg-amber-50/60 p-4 rounded-xl border border-amber-200/90">
              <div class="flex items-center gap-2 text-academic-amber font-mono text-xs font-semibold">
                <i class="fas fa-fingerprint"></i>
                <span>Инвестиционный психотип:</span>
              </div>
              <div class="text-base font-serif font-bold text-ink-950">
                {{ archetype.title }}
              </div>
              <p class="text-xs text-ink-700 leading-relaxed font-sans">
                {{ archetype.description }}
              </p>
            </div>
          </div>

          <!-- Key Personality Traits -->
          <div v-if="keyTraits && keyTraits.length > 0" class="w-full text-left pt-4 border-t border-ink-100 space-y-2 mt-auto">
            <div class="text-[11px] font-mono text-ink-500 uppercase tracking-wider">Психологические маркеры:</div>
            <div class="flex flex-wrap gap-2">
              <span 
                v-for="(trait, index) in keyTraits" 
                :key="index"
                class="px-2.5 py-1 rounded-lg text-xs font-mono bg-paper-50 border border-ink-200 text-ink-800"
              >
                {{ trait }}
              </span>
            </div>
          </div>
        </div>

        <!-- Col 2: Cognitive Radar Card & Asset Allocation (7 cols) -->
        <div class="lg:col-span-7 flex flex-col justify-between space-y-6">
          <!-- Card 2A: Cognitive Radar -->
          <div class="academic-card p-6 sm:p-7 space-y-5 bg-white">
            <div class="flex items-center justify-between border-b border-ink-200 pb-3">
              <div>
                <h3 class="text-xl font-serif font-bold text-ink-950">Когнитивная радар-карта</h3>
                <p class="text-xs text-ink-500 font-mono">4 вектора принятия инвестиционных решений</p>
              </div>
              <span class="badge-amber">Радар характера</span>
            </div>

            <!-- Radar SVG & Legend in Balanced Row -->
            <div class="flex flex-col sm:flex-row items-center justify-center gap-6 py-1">
              <div class="relative w-52 h-52 flex-shrink-0">
                <svg viewBox="0 0 200 200" class="w-full h-full">
                  <!-- Radar Web Background Circles -->
                  <polygon points="100,20 180,100 100,180 20,100" fill="none" stroke="#E7E5E4" stroke-width="1" />
                  <polygon points="100,45 155,100 100,155 45,100" fill="none" stroke="#E7E5E4" stroke-width="1" />
                  <polygon points="100,70 130,100 100,130 70,100" fill="none" stroke="#E7E5E4" stroke-width="1" />
                  <!-- Axes lines -->
                  <line x1="100" y1="20" x2="100" y2="180" stroke="#D6D3D1" stroke-width="1" stroke-dasharray="2" />
                  <line x1="20" y1="100" x2="180" y2="100" stroke="#D6D3D1" stroke-width="1" stroke-dasharray="2" />
                  
                  <!-- Dynamic Radar Shape -->
                  <polygon 
                    :points="radarPoints" 
                    fill="rgba(180, 83, 9, 0.22)" 
                    stroke="#B45309" 
                    stroke-width="2" 
                    stroke-linejoin="round"
                    class="transition-all duration-700 ease-out"
                  />
                  <!-- Axis Points -->
                  <circle :cx="radarValues.top.x" :cy="radarValues.top.y" r="4" fill="#B45309" stroke="#FFF" stroke-width="1.5" />
                  <circle :cx="radarValues.right.x" :cy="radarValues.right.y" r="4" fill="#B45309" stroke="#FFF" stroke-width="1.5" />
                  <circle :cx="radarValues.bottom.x" :cy="radarValues.bottom.y" r="4" fill="#B45309" stroke="#FFF" stroke-width="1.5" />
                  <circle :cx="radarValues.left.x" :cy="radarValues.left.y" r="4" fill="#B45309" stroke="#FFF" stroke-width="1.5" />
                </svg>
              </div>

              <!-- Radar Legend & Axis Breakdown -->
              <div class="space-y-2.5 w-full">
                <div class="p-2.5 rounded-lg bg-paper-50 border border-ink-100 flex items-center justify-between text-xs font-mono">
                  <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-academic-amber"></span>
                    <span class="text-ink-700 font-medium">Финансовая емкость:</span>
                  </div>
                  <span class="text-academic-amber font-bold text-sm">{{ effectiveRadarScores.capacity }}%</span>
                </div>

                <div class="p-2.5 rounded-lg bg-paper-50 border border-ink-100 flex items-center justify-between text-xs font-mono">
                  <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-academic-amber"></span>
                    <span class="text-ink-700 font-medium">Эмоциональная стойкость:</span>
                  </div>
                  <span class="text-academic-amber font-bold text-sm">{{ effectiveRadarScores.stress_resistance }}%</span>
                </div>

                <div class="p-2.5 rounded-lg bg-paper-50 border border-ink-100 flex items-center justify-between text-xs font-mono">
                  <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-academic-amber"></span>
                    <span class="text-ink-700 font-medium">Автономия от хайпа (FOMO):</span>
                  </div>
                  <span class="text-academic-amber font-bold text-sm">{{ effectiveRadarScores.fomo_control }}%</span>
                </div>

                <div class="p-2.5 rounded-lg bg-paper-50 border border-ink-100 flex items-center justify-between text-xs font-mono">
                  <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-academic-amber"></span>
                    <span class="text-ink-700 font-medium">Стратегическая дисциплина:</span>
                  </div>
                  <span class="text-academic-amber font-bold text-sm">{{ effectiveRadarScores.discipline }}%</span>
                </div>
              </div>
            </div>

            <div class="pt-3 border-t border-ink-100 text-xs font-mono text-ink-500 flex items-center justify-between">
              <span>Калибровка на основе 12 дилемм</span>
              <span class="text-academic-amber font-semibold">4 вектора мышления</span>
            </div>
          </div>

          <!-- Card 2B: Model Asset Allocation (In Right Column) -->
          <div v-if="assetAllocation" class="academic-card p-6 sm:p-7 space-y-4 bg-white flex-1 flex flex-col justify-between">
            <div class="flex items-center justify-between border-b border-ink-200 pb-3">
              <div>
                <h3 class="text-xl font-serif font-bold text-ink-950">Модельное распределение активов</h3>
                <p class="text-xs text-ink-500 font-mono">Рекомендованная структура инвестиционного портфеля</p>
              </div>
              <span class="badge-amber">Asset Allocation</span>
            </div>

            <!-- Proportional Bar -->
            <div class="w-full h-3 rounded-full overflow-hidden flex bg-ink-100">
              <div 
                class="bg-amber-600 h-full transition-all duration-700" 
                :style="{ width: `${assetAllocation.stocks || 0}%` }"
                title="Акции"
              ></div>
              <div 
                class="bg-sky-600 h-full transition-all duration-700" 
                :style="{ width: `${assetAllocation.bonds || 0}%` }"
                title="Облигации"
              ></div>
              <div 
                class="bg-emerald-600 h-full transition-all duration-700" 
                :style="{ width: `${assetAllocation.cash || 0}%` }"
                title="Ликвидность"
              ></div>
              <div 
                class="bg-purple-600 h-full transition-all duration-700" 
                :style="{ width: `${assetAllocation.alternatives || 0}%` }"
                title="Альтернативы"
              ></div>
            </div>

            <!-- Asset Grid (4 columns) -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
              <div class="p-3 rounded-xl bg-paper-50 border border-ink-200 space-y-0.5">
                <div class="flex items-center gap-1.5 text-xs text-amber-700 font-mono">
                  <span class="w-2 h-2 rounded-full bg-amber-600"></span>
                  <span>Акции</span>
                </div>
                <div class="text-2xl font-mono font-bold text-ink-950">{{ assetAllocation.stocks || 0 }}%</div>
              </div>

              <div class="p-3 rounded-xl bg-paper-50 border border-ink-200 space-y-0.5">
                <div class="flex items-center gap-1.5 text-xs text-sky-700 font-mono">
                  <span class="w-2 h-2 rounded-full bg-sky-600"></span>
                  <span>Облигации</span>
                </div>
                <div class="text-2xl font-mono font-bold text-ink-950">{{ assetAllocation.bonds || 0 }}%</div>
              </div>

              <div class="p-3 rounded-xl bg-paper-50 border border-ink-200 space-y-0.5">
                <div class="flex items-center gap-1.5 text-xs text-emerald-700 font-mono">
                  <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
                  <span>Ликвидность</span>
                </div>
                <div class="text-2xl font-mono font-bold text-ink-950">{{ assetAllocation.cash || 0 }}%</div>
              </div>

              <div class="p-3 rounded-xl bg-paper-50 border border-ink-200 space-y-0.5">
                <div class="flex items-center gap-1.5 text-xs text-purple-700 font-mono">
                  <span class="w-2 h-2 rounded-full bg-purple-600"></span>
                  <span>Альтернативы</span>
                </div>
                <div class="text-2xl font-mono font-bold text-ink-950">{{ assetAllocation.alternatives || 0 }}%</div>
              </div>
            </div>

            <div class="pt-3 border-t border-ink-100 text-xs font-mono text-ink-500 flex items-center justify-between">
              <span>Сбалансировано по Марковицу</span>
              <span class="text-ink-700 font-semibold">Горизонт: от 3 лет</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ROW 2: ИНТЕРАКТИВНЫЙ СИМУЛЯТОР РЫНОЧНОГО ШОКА -->
      <section class="academic-card p-6 sm:p-10 space-y-8 border-academic-amber/40 bg-gradient-to-b from-white to-paper-50">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-ink-200 pb-6">
          <div class="space-y-1">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono font-medium bg-red-50 text-academic-crimson border border-red-200">
              <span class="w-1.5 h-1.5 rounded-full bg-academic-crimson"></span>
              <span>СТРЕСС-ТЕСТИРОВАНИЕ ПОРТФЕЛЯ</span>
            </div>
            <h2 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950">
              Симулятор поведения при рыночном спаде
            </h2>
            <p class="text-xs sm:text-sm text-ink-600">
              Подвигайте ползунок просадки рынка, чтобы смоделировать вашу психологическую реакцию и защитную емкость портфеля.
            </p>
          </div>
          
          <!-- Preset buttons -->
          <div class="flex flex-wrap gap-2">
            <button 
              @click="marketDrop = 10" 
              class="px-3 py-1.5 rounded-lg text-xs font-mono border transition-all"
              :class="marketDrop === 10 ? 'bg-ink-950 text-amber-300 font-semibold border-ink-950' : 'bg-white text-ink-700 border-ink-200 hover:bg-paper-50'"
            >
              -10% Коррекция
            </button>
            <button 
              @click="marketDrop = 20" 
              class="px-3 py-1.5 rounded-lg text-xs font-mono border transition-all"
              :class="marketDrop === 20 ? 'bg-ink-950 text-amber-300 font-semibold border-ink-950' : 'bg-white text-ink-700 border-ink-200 hover:bg-paper-50'"
            >
              -20% Медвежий тренд
            </button>
            <button 
              @click="marketDrop = 35" 
              class="px-3 py-1.5 rounded-lg text-xs font-mono border transition-all"
              :class="marketDrop === 35 ? 'bg-ink-950 text-amber-300 font-semibold border-ink-950' : 'bg-white text-ink-700 border-ink-200 hover:bg-paper-50'"
            >
              -35% Кризис 2008/2022
            </button>
            <button 
              @click="marketDrop = 50" 
              class="px-3 py-1.5 rounded-lg text-xs font-mono border transition-all"
              :class="marketDrop === 50 ? 'bg-academic-crimson text-white font-semibold border-academic-crimson' : 'bg-white text-ink-700 border-ink-200 hover:bg-paper-50'"
            >
              -50% Исторический шок
            </button>
          </div>
        </div>

        <!-- Slider Control -->
        <div class="space-y-4">
          <div class="flex justify-between items-center text-sm font-mono">
            <span class="text-ink-600">Падение индекса акций:</span>
            <span class="text-2xl font-bold font-mono text-academic-crimson">-{{ marketDrop }}%</span>
          </div>
          <input 
            type="range" 
            min="0" 
            max="50" 
            step="1"
            v-model.number="marketDrop"
            class="w-full h-2 bg-ink-100 rounded-lg appearance-none cursor-pointer accent-amber-700"
          />
          <div class="flex justify-between text-[11px] font-mono text-ink-400">
            <span>0% (Стабильность)</span>
            <span>-25% (Кризис)</span>
            <span>-50% (Историческое дно)</span>
          </div>
        </div>

        <!-- Simulation 3-Col Output -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-2">
          <!-- Metric 1: Portfolio Drawdown -->
          <div class="p-5 space-y-2 rounded-xl border border-ink-200 bg-white">
            <div class="text-xs font-mono text-ink-500">Фактическая просадка вашего портфеля</div>
            <div class="text-3xl font-mono font-bold text-academic-amber">-{{ portfolioDrawdown }}%</div>
            <p class="text-xs text-ink-600 leading-relaxed">
              Благодаря облигациям и ликвидности вы сберегли <span class="text-academic-sage font-semibold">+{{ capitalSaved }}%</span> капитала по сравнению с рынком.
            </p>
          </div>

          <!-- Metric 2: Panic Index -->
          <div class="p-5 space-y-2 rounded-xl border border-ink-200 bg-white">
            <div class="text-xs font-mono text-ink-500">Психологический индекс тревоги</div>
            <div class="flex items-center gap-2">
              <span class="text-3xl font-mono font-bold" :class="panicIndexColor">{{ panicIndex }}%</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-semibold" :class="panicBadgeClass">
                {{ panicZoneLabel }}
              </span>
            </div>
            <p class="text-xs text-ink-600 leading-relaxed">
              {{ panicDescription }}
            </p>
          </div>

          <!-- Metric 3: Behavioral Protocol -->
          <div class="p-5 space-y-2 rounded-xl border border-amber-300/80 bg-amber-50/60">
            <div class="text-xs font-mono text-academic-amber flex items-center gap-1.5 font-semibold">
              <i class="fas fa-shield-alt"></i>
              <span>Защитный поведенческий протокол</span>
            </div>
            <div class="text-sm font-semibold text-ink-950 font-serif">Рекомендация при этом уровне стресса:</div>
            <p class="text-xs text-ink-800 leading-relaxed font-mono">
              {{ behavioralRule }}
            </p>
          </div>
        </div>
      </section>

      <!-- ROW 3: ПОВЕДЕНЧЕСКИЕ ЛОВУШКИ И КОГНИТИВНЫЕ ИСКАЖЕНИЯ -->
      <div v-if="behavioralTraps && behavioralTraps.length > 0" class="academic-card p-6 sm:p-8 space-y-6 border-amber-300/80 bg-white shadow-sm">
        <div class="flex items-center justify-between">
          <div class="space-y-1">
            <div class="badge-amber">ПОВЕДЕНЧЕСКАЯ ЭКОНОМИКА</div>
            <h3 class="text-xl sm:text-2xl font-bold text-ink-950 font-serif">
              Выявленные когнитивные искажения (Biases)
            </h3>
            <p class="text-xs text-ink-500 font-mono">
              Ловушки мышления, которые могут снижать доходность вашего портфеля
            </p>
          </div>
          <span class="text-xl text-academic-amber">
            <i class="fas fa-brain"></i>
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div 
            v-for="(item, index) in behavioralTraps" 
            :key="index"
            class="p-5 rounded-xl border border-ink-200 bg-paper-50 space-y-3 hover:border-amber-400 hover:bg-white transition-all"
          >
            <div class="flex items-center gap-2">
              <span class="w-6 h-6 rounded-lg bg-amber-100 text-amber-800 font-mono text-xs font-bold flex items-center justify-center">
                !
              </span>
              <h4 class="text-base font-serif font-bold text-ink-950">
                {{ item.trap }}
              </h4>
            </div>

            <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
              {{ item.warning }}
            </p>

            <div class="pt-2 border-t border-ink-100 text-xs font-mono text-academic-amber font-semibold flex items-start gap-1.5">
              <i class="fas fa-check-circle mt-0.5"></i>
              <span>Защитное правило: {{ item.rule }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ROW 4: AI ACTIONABLE RECOMMENDATIONS -->
      <div v-if="recommendations && recommendations.length > 0" class="academic-card p-6 sm:p-8 space-y-6">
        <div class="flex items-center justify-between">
          <div class="space-y-1">
            <div class="badge-amber">ПРАКТИЧЕСКИЕ ШАГИ</div>
            <h3 class="text-xl sm:text-2xl font-bold text-ink-950 font-serif">
              Персональные рекомендации аналитической модели
            </h3>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div 
            v-for="(rec, index) in recommendations" 
            :key="index"
            class="p-4 rounded-xl bg-paper-50 border border-ink-200 hover:border-ink-300 hover:bg-white transition-all flex items-start gap-3.5 group"
          >
            <div class="w-7 h-7 rounded-lg bg-amber-100 text-academic-amber font-mono text-xs font-bold flex items-center justify-center flex-shrink-0 group-hover:bg-ink-950 group-hover:text-amber-300 transition-colors">
              0{{ index + 1 }}
            </div>
            <p class="text-sm text-ink-800 leading-relaxed">
              {{ rec }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useResults } from '../composables/useResults'

const { 
  riskScore, 
  riskCategory, 
  archetype,
  radarScores: backendRadarScores,
  behavioralTraps,
  recommendations, 
  assetAllocation, 
  keyTraits, 
  error, 
  isLoading,
  loadInvestmentProfileFromStorage,
  fetchInvestmentProfile 
} = useResults()

// Load profile on mount
onMounted(async () => {
  const loaded = loadInvestmentProfileFromStorage()
  if (!loaded) {
    try {
      await fetchInvestmentProfile()
    } catch (err) {
      console.error('Failed to load profile:', err)
    }
  }
})

// Circular Progress
const circumference = computed(() => 2 * Math.PI * 96)
const dashOffset = computed(() => 
  circumference.value - (riskScore.value / 100) * circumference.value
)

// 4 Cognitive Radar Calculations (Uses LLM data when available)
const effectiveRadarScores = computed(() => {
  if (backendRadarScores.value && typeof backendRadarScores.value === 'object') {
    return {
      capacity: backendRadarScores.value.capacity ?? 70,
      stress_resistance: backendRadarScores.value.stress_resistance ?? 60,
      fomo_control: backendRadarScores.value.fomo_control ?? 65,
      discipline: backendRadarScores.value.discipline ?? 75
    }
  }
  const score = riskScore.value || 50
  return {
    capacity: Math.min(95, Math.max(35, Math.round(score * 0.7 + 25))),
    stress_resistance: Math.min(95, Math.max(30, Math.round(100 - score * 0.4))),
    fomo_control: Math.min(95, Math.max(35, Math.round(score * 0.8 + 15))),
    discipline: Math.min(95, Math.max(40, Math.round(score * 0.6 + 35)))
  }
})

const radarValues = computed(() => {
  const center = 100
  const maxR = 75
  const s = effectiveRadarScores.value
  
  return {
    top: { x: center, y: center - (s.capacity / 100) * maxR },
    right: { x: center + (s.fomo_control / 100) * maxR, y: center },
    bottom: { x: center, y: center + (s.stress_resistance / 100) * maxR },
    left: { x: center - (s.discipline / 100) * maxR, y: center }
  }
})

const radarPoints = computed(() => {
  const v = radarValues.value
  return `${v.top.x},${v.top.y} ${v.right.x},${v.right.y} ${v.bottom.x},${v.bottom.y} ${v.left.x},${v.left.y}`
})

// STRESS SIMULATOR STATE & MATH
const marketDrop = ref(20)

const portfolioDrawdown = computed(() => {
  const alloc = assetAllocation.value || { stocks: 50, bonds: 35, cash: 15, alternatives: 0 }
  const stocksLoss = (alloc.stocks || 50) * (marketDrop.value / 100)
  const bondsLoss = (alloc.bonds || 35) * (marketDrop.value * 0.1 / 100)
  const altLoss = (alloc.alternatives || 0) * (marketDrop.value * 0.5 / 100)
  const totalLoss = stocksLoss + bondsLoss + altLoss
  return Math.round(totalLoss * 10) / 10
})

const capitalSaved = computed(() => {
  const saved = marketDrop.value - portfolioDrawdown.value
  return Math.max(0, Math.round(saved * 10) / 10)
})

const panicIndex = computed(() => {
  const emotionalityFactor = (100 - (effectiveRadarScores.value.stress_resistance || 50)) / 100
  const dropFactor = marketDrop.value / 50
  const index = Math.round((dropFactor * 0.6 + emotionalityFactor * 0.4) * 100)
  return Math.min(99, Math.max(5, index))
})

const panicIndexColor = computed(() => {
  if (panicIndex.value < 35) return 'text-academic-sage'
  if (panicIndex.value < 70) return 'text-academic-amber'
  return 'text-academic-crimson'
})

const panicBadgeClass = computed(() => {
  if (panicIndex.value < 35) return 'bg-emerald-50 text-academic-sage border border-emerald-200'
  if (panicIndex.value < 70) return 'bg-amber-50 text-academic-amber border border-amber-200'
  return 'bg-red-50 text-academic-crimson border border-red-200'
})

const panicZoneLabel = computed(() => {
  if (panicIndex.value < 35) return 'Зона хладнокровия'
  if (panicIndex.value < 70) return 'Зона дискомфорта'
  return 'Критический риск паники'
})

const panicDescription = computed(() => {
  if (panicIndex.value < 35) {
    return 'Вы сохраняете эмоциональный баланс. Риск спонтанных импульсивных продаж минимален.'
  }
  if (panicIndex.value < 70) {
    return 'Появляется сильное желание «спасти остаток капитала». Высока вероятность ошибок при чтении новостей.'
  }
  return 'Острая душевная боль от потерь. 87% инвесторов с такими маркерами капитулируют и фиксируют убыток на самом дне.'
})

const behavioralRule = computed(() => {
  if (panicIndex.value < 35) {
    return '«Дисциплинированная ребалансировка: используйте избыток ликвидности для планового выкупа качественных подешевевших активов».';
  }
  if (panicIndex.value < 70) {
    return '«Правило 48 часов: отключите уведомления брокера. Любые сделки одобряйте только через двое суток после возникновения первого импульса».';
  }
  return '«Жесткий психологический стоп: зафиксируйте запрет на экстренный выход в деньги. Помните, что рыночный цикл всегда восстанавливается».';
})

// Helpers
const getCategoryLabel = (category) => {
  const labels = {
    'Conservative': 'Консервативный профиль',
    'Moderate': 'Умеренно-сбалансированный',
    'Growth': 'Профиль роста (Growth)',
    'Aggressive': 'Агрессивный инвестор'
  }
  return labels[category] || category || 'Умеренный профиль'
}

const getCategoryBadgeClass = (category) => {
  const classes = {
    'Conservative': 'bg-sky-50 text-sky-800 border-sky-200',
    'Moderate': 'bg-emerald-50 text-emerald-800 border-emerald-200',
    'Growth': 'bg-amber-50 text-amber-900 border-amber-300',
    'Aggressive': 'bg-red-50 text-red-900 border-red-200'
  }
  return classes[category] || 'bg-amber-50 text-amber-900 border-amber-300'
}
</script>
