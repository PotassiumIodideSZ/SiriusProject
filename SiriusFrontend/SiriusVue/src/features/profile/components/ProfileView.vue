<template>
  <div class="min-h-screen py-10 px-4 sm:px-6 lg:px-8 max-w-5xl mx-auto space-y-8">
    <!-- Top Action Bar -->
    <div class="flex items-center justify-between border-b border-ink-200 pb-4">
      <div class="space-y-1">
        <div class="badge-amber">ЛИЧНЫЙ КАБИНЕТ</div>
        <h1 class="text-2xl sm:text-3xl font-serif font-bold text-ink-950 tracking-tight">
          Профиль инвестора
        </h1>
      </div>
      <div class="flex items-center gap-3">
        <router-link 
          v-if="investmentProfile && riskScore > 0"
          to="/results" 
          class="px-4 py-2 rounded-xl bg-ink-950 hover:bg-ink-800 text-amber-300 text-xs font-mono shadow-sm transition-all flex items-center gap-2"
        >
          <i class="fas fa-chart-line text-xs"></i>
          <span>Интерактивный паспорт</span>
        </router-link>

        <router-link 
          to="/survey" 
          class="px-4 py-2 rounded-xl bg-white hover:bg-paper-50 text-ink-700 hover:text-ink-950 border border-ink-200 text-xs font-mono shadow-sm transition-all flex items-center gap-2"
        >
          <i class="fas fa-redo-alt text-xs"></i>
          <span>{{ investmentProfile ? 'Пересдать тест' : 'Пройти тест' }}</span>
        </router-link>
      </div>
    </div>

    <!-- Profile Header Card -->
    <div class="academic-card p-6 sm:p-8 bg-white space-y-6">
      <div class="flex flex-col sm:flex-row items-center sm:items-start gap-6 sm:gap-8">
        <!-- Monogram Avatar in Academic Stamp style -->
        <div class="w-20 h-20 rounded-2xl bg-ink-950 flex items-center justify-center text-amber-300 font-serif font-bold text-2xl shadow-sm border border-ink-800 flex-shrink-0">
          {{ avatarLetter }}
        </div>

        <!-- User Information -->
        <div class="flex-1 text-center sm:text-left space-y-2">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 class="text-2xl font-serif font-bold text-ink-950 tracking-tight">
                {{ profile ? `${profile.first_name || ''} ${profile.last_name || ''}`.trim() || profile.username : 'Загрузка...' }}
              </h2>
              <div class="text-xs font-mono text-ink-500 mt-0.5 flex flex-wrap items-center justify-center sm:justify-start gap-3">
                <span>{{ profile?.email || 'Авторизованный профиль инвестора' }}</span>
                <span class="text-ink-300">·</span>
                <span class="text-academic-amber font-semibold">@{{ profile?.username }}</span>
              </div>
            </div>

            <!-- Quick Stats Chips -->
            <div class="flex items-center justify-center gap-2 text-xs font-mono">
              <span class="px-3 py-1.5 rounded-lg bg-paper-50 border border-ink-200 text-ink-700">
                Статус: <strong class="text-ink-950">{{ investmentProfile ? 'Профиль откалиброван' : 'Новый аккаунт' }}</strong>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State (No test completed yet) -->
    <div v-if="!investmentProfile || riskScore === 0" class="academic-card p-8 sm:p-14 text-center space-y-6 bg-white border-amber-300/80 shadow-sm">
      <div class="w-16 h-16 rounded-2xl bg-amber-50 border border-amber-200 flex items-center justify-center text-academic-amber mx-auto text-2xl">
        <i class="fas fa-brain"></i>
      </div>
      <div class="space-y-2 max-w-lg mx-auto">
        <h3 class="text-2xl font-serif font-bold text-ink-950">
          Инвестиционный паспорт еще не сформирован
        </h3>
        <p class="text-sm text-ink-600 leading-relaxed">
          Пройдите когнитивную диагностику из 12 поведенческих дилемм, чтобы ИИ-модель определила ваш психотип, построила радар компетенций и сформировала защитную структуру портфеля.
        </p>
      </div>

      <div class="pt-2">
        <router-link 
          to="/survey" 
          class="px-8 py-3.5 rounded-xl bg-ink-950 hover:bg-ink-800 text-amber-300 font-sans font-medium text-sm shadow-md inline-flex items-center gap-2 transition-all active:scale-[0.98]"
        >
          <span>Пройти диагностику (12 дилемм · ~2.5 мин)</span>
          <i class="fas fa-arrow-right text-xs"></i>
        </router-link>
      </div>
    </div>

    <!-- Loaded Profile with Archetype and Mini-Radar -->
    <div v-else class="space-y-8">
      <!-- ROW 1: ARCHETYPE & MINI-RADAR (EQUAL HEIGHT ALIGNMENT) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        <!-- Col 1: Archetype & Risk Score (6 cols) -->
        <div class="lg:col-span-6 academic-card p-6 sm:p-8 flex flex-col justify-between space-y-6 bg-white">
          <div class="space-y-6">
            <div class="flex items-center justify-between border-b border-ink-200 pb-3">
              <span class="badge-amber">ИНВЕСТИЦИОННЫЙ ПСИХОТИП</span>
              <span class="text-xs font-mono text-ink-400">ИИ-кластеризация</span>
            </div>

            <!-- Archetype Highlight Box -->
            <div class="p-5 rounded-2xl bg-amber-50/60 border border-amber-200/90 space-y-3">
              <div class="flex items-center gap-2.5 text-academic-amber font-mono text-xs font-bold uppercase tracking-wider">
                <i class="fas fa-fingerprint text-sm"></i>
                <span>{{ archetype?.title || 'Осознанный инвестор' }}</span>
              </div>
              <p class="text-xs sm:text-sm text-ink-800 leading-relaxed font-sans">
                {{ archetype?.description || getCategoryDescription(riskCategory) }}
              </p>
            </div>

            <!-- Score & Category Row -->
            <div class="flex items-center gap-6 p-4 rounded-xl bg-paper-50 border border-ink-200">
              <div class="relative w-20 h-20 flex-shrink-0">
                <svg class="w-full h-full transform -rotate-90">
                  <circle cx="40" cy="40" r="34" stroke="#E7E5E4" stroke-width="7" fill="none" />
                  <circle 
                    cx="40" 
                    cy="40" 
                    r="34" 
                    stroke="#B45309" 
                    stroke-width="7" 
                    stroke-linecap="round" 
                    fill="none" 
                    :stroke-dasharray="circumference" 
                    :stroke-dashoffset="dashOffset" 
                    class="transition-all duration-1000 ease-out" 
                  />
                </svg>
                <div class="absolute inset-0 flex items-center justify-center">
                  <span class="text-lg font-mono font-bold text-ink-950">{{ riskScore }}%</span>
                </div>
              </div>

              <div class="space-y-1.5 flex-1">
                <div class="text-[11px] font-mono text-ink-500 uppercase">Толерантность к риску:</div>
                <div class="inline-block px-3.5 py-1 rounded-lg text-xs font-mono font-bold uppercase tracking-wider border shadow-sm" :class="getCategoryBadgeClass(riskCategory)">
                  {{ getCategoryLabel(riskCategory) }}
                </div>
              </div>
            </div>
          </div>

          <!-- Key Traits Badges -->
          <div v-if="keyTraits && keyTraits.length > 0" class="space-y-2 pt-3 border-t border-ink-100 mt-auto">
            <div class="text-[11px] font-mono text-ink-500 uppercase">Психологические маркеры:</div>
            <div class="flex flex-wrap gap-2">
              <span 
                v-for="(trait, idx) in keyTraits" 
                :key="idx"
                class="px-2.5 py-1 rounded-lg text-xs font-mono bg-paper-50 border border-ink-200 text-ink-800"
              >
                {{ trait }}
              </span>
            </div>
          </div>
        </div>

        <!-- Col 2: Cognitive Mini-Radar (6 cols) -->
        <div class="lg:col-span-6 academic-card p-6 sm:p-8 flex flex-col justify-between space-y-6 bg-white">
          <div class="space-y-6">
            <div class="flex items-center justify-between border-b border-ink-200 pb-3">
              <div>
                <h3 class="text-lg font-serif font-bold text-ink-950">Радар характера</h3>
                <p class="text-xs text-ink-500 font-mono">4 вектора принятия решений</p>
              </div>
              <span class="badge-amber">Когнитивный профиль</span>
            </div>

            <!-- Mini Radar SVG -->
            <div class="flex flex-col sm:flex-row items-center justify-center gap-6 py-2">
              <div class="relative w-52 h-52 flex-shrink-0">
                <svg viewBox="0 0 200 200" class="w-full h-full">
                  <!-- Guide polygons -->
                  <polygon points="100,20 180,100 100,180 20,100" fill="none" stroke="#E7E5E4" stroke-width="1" />
                  <polygon points="100,45 155,100 100,155 45,100" fill="none" stroke="#E7E5E4" stroke-width="1" />
                  <polygon points="100,70 130,100 100,130 70,100" fill="none" stroke="#E7E5E4" stroke-width="1" />
                  <!-- Axes lines -->
                  <line x1="100" y1="20" x2="100" y2="180" stroke="#D6D3D1" stroke-width="1" stroke-dasharray="2" />
                  <line x1="20" y1="100" x2="180" y2="100" stroke="#D6D3D1" stroke-width="1" stroke-dasharray="2" />
                  
                  <!-- Dynamic Radar Polygon -->
                  <polygon 
                    :points="radarPoints" 
                    fill="rgba(180, 83, 9, 0.22)" 
                    stroke="#B45309" 
                    stroke-width="2" 
                    stroke-linejoin="round"
                    class="transition-all duration-700 ease-out"
                  />
                  <!-- Points -->
                  <circle :cx="radarValues.top.x" :cy="radarValues.top.y" r="3.5" fill="#B45309" stroke="#FFF" stroke-width="1.5" />
                  <circle :cx="radarValues.right.x" :cy="radarValues.right.y" r="3.5" fill="#B45309" stroke="#FFF" stroke-width="1.5" />
                  <circle :cx="radarValues.bottom.x" :cy="radarValues.bottom.y" r="3.5" fill="#B45309" stroke="#FFF" stroke-width="1.5" />
                  <circle :cx="radarValues.left.x" :cy="radarValues.left.y" r="3.5" fill="#B45309" stroke="#FFF" stroke-width="1.5" />
                </svg>
              </div>

              <!-- Axis List -->
              <div class="space-y-3 w-full text-xs font-mono">
                <div class="flex items-center justify-between p-2.5 rounded-lg bg-paper-50 border border-ink-100">
                  <span class="text-ink-600">Емкость:</span>
                  <span class="text-academic-amber font-bold">{{ effectiveRadarScores.capacity }}%</span>
                </div>
                <div class="flex items-center justify-between p-2.5 rounded-lg bg-paper-50 border border-ink-100">
                  <span class="text-ink-600">Стойкость:</span>
                  <span class="text-academic-amber font-bold">{{ effectiveRadarScores.stress_resistance }}%</span>
                </div>
                <div class="flex items-center justify-between p-2.5 rounded-lg bg-paper-50 border border-ink-100">
                  <span class="text-ink-600">FOMO-контроль:</span>
                  <span class="text-academic-amber font-bold">{{ effectiveRadarScores.fomo_control }}%</span>
                </div>
                <div class="flex items-center justify-between p-2.5 rounded-lg bg-paper-50 border border-ink-100">
                  <span class="text-ink-600">Дисциплина:</span>
                  <span class="text-academic-amber font-bold">{{ effectiveRadarScores.discipline }}%</span>
                </div>
              </div>
            </div>
          </div>

          <div class="pt-3 border-t border-ink-100 text-xs font-mono text-ink-400 flex items-center justify-between mt-auto">
            <span>Модель когнитивного отклика</span>
            <router-link to="/results" class="text-academic-amber hover:underline flex items-center gap-1 font-semibold">
              <span>Подробнее</span>
              <i class="fas fa-chevron-right text-[10px]"></i>
            </router-link>
          </div>
        </div>
      </div>

      <!-- ROW 2: ASSET ALLOCATION BAR & CARDS -->
      <div v-if="assetAllocation && Object.keys(assetAllocation).length > 0" class="academic-card p-6 sm:p-8 space-y-6 bg-white">
        <div class="flex items-center justify-between border-b border-ink-200 pb-3">
          <div>
            <h3 class="text-lg font-serif font-bold text-ink-950">Модельное распределение капитала</h3>
            <p class="text-xs text-ink-500 font-mono">Базовые пропорции рекомендованного портфеля</p>
          </div>
          <router-link to="/results" class="text-xs font-mono text-academic-amber hover:underline flex items-center gap-1 font-semibold">
            <span>Стресс-тест портфеля</span>
            <i class="fas fa-arrow-right text-[10px]"></i>
          </router-link>
        </div>

        <!-- Allocation Multi-Bar -->
        <div class="w-full h-3 rounded-full overflow-hidden flex bg-ink-100">
          <div class="bg-amber-600 h-full transition-all duration-700" :style="{ width: `${assetAllocation.stocks || 0}%` }" title="Акции"></div>
          <div class="bg-sky-600 h-full transition-all duration-700" :style="{ width: `${assetAllocation.bonds || 0}%` }" title="Облигации"></div>
          <div class="bg-emerald-600 h-full transition-all duration-700" :style="{ width: `${assetAllocation.cash || 0}%` }" title="Ликвидность"></div>
          <div class="bg-purple-600 h-full transition-all duration-700" :style="{ width: `${assetAllocation.alternatives || 0}%` }" title="Альтернативы"></div>
        </div>

        <!-- 4 Grid Cards -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <div class="p-3.5 rounded-xl bg-paper-50 border border-ink-200 space-y-1">
            <div class="flex items-center gap-1.5 text-xs text-amber-700 font-mono">
              <span class="w-2 h-2 rounded-full bg-amber-600"></span>
              <span>Акции</span>
            </div>
            <div class="text-2xl font-mono font-bold text-ink-950">{{ assetAllocation.stocks || 0 }}%</div>
          </div>

          <div class="p-3.5 rounded-xl bg-paper-50 border border-ink-200 space-y-1">
            <div class="flex items-center gap-1.5 text-xs text-sky-700 font-mono">
              <span class="w-2 h-2 rounded-full bg-sky-600"></span>
              <span>Облигации</span>
            </div>
            <div class="text-2xl font-mono font-bold text-ink-950">{{ assetAllocation.bonds || 0 }}%</div>
          </div>

          <div class="p-3.5 rounded-xl bg-paper-50 border border-ink-200 space-y-1">
            <div class="flex items-center gap-1.5 text-xs text-emerald-700 font-mono">
              <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
              <span>Ликвидность</span>
            </div>
            <div class="text-2xl font-mono font-bold text-ink-950">{{ assetAllocation.cash || 0 }}%</div>
          </div>

          <div class="p-3.5 rounded-xl bg-paper-50 border border-ink-200 space-y-1">
            <div class="flex items-center gap-1.5 text-xs text-purple-700 font-mono">
              <span class="w-2 h-2 rounded-full bg-purple-600"></span>
              <span>Альтернативы</span>
            </div>
            <div class="text-2xl font-mono font-bold text-ink-950">{{ assetAllocation.alternatives || 0 }}%</div>
          </div>
        </div>
      </div>

      <!-- ROW 3: BEHAVIORAL TRAPS QUICK GLANCE -->
      <div v-if="behavioralTraps && behavioralTraps.length > 0" class="academic-card p-6 sm:p-8 space-y-4 bg-white border-amber-300/80">
        <div class="flex items-center justify-between border-b border-ink-200 pb-3">
          <div class="space-y-0.5">
            <div class="badge-amber">ЗОЛОТЫЕ ПРАВИЛА ИНВЕСТОРА</div>
            <h3 class="text-lg font-serif font-bold text-ink-950">Защита от персональных когнитивных ловушек</h3>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-1">
          <div 
            v-for="(trap, i) in behavioralTraps" 
            :key="i"
            class="p-4 rounded-xl border border-ink-200 bg-paper-50 space-y-2"
          >
            <div class="flex items-center gap-2">
              <span class="w-5 h-5 rounded-md bg-amber-200 text-amber-900 text-xs font-mono font-bold flex items-center justify-center">!</span>
              <div class="text-sm font-serif font-bold text-ink-950">{{ trap.trap }}</div>
            </div>
            <p class="text-xs text-ink-700 leading-relaxed font-sans">{{ trap.warning }}</p>
            <div class="text-xs font-mono text-academic-amber font-semibold pt-1 border-t border-ink-100 flex items-start gap-1">
              <i class="fas fa-shield-alt text-[10px] mt-0.5"></i>
              <span>Правило: {{ trap.rule }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useProfile } from '../composables/useProfile'

const { 
  profile, 
  riskScore, 
  investmentProfile, 
  riskCategory, 
  assetAllocation, 
  archetype,
  radarScores,
  behavioralTraps,
  keyTraits,
  fetchProfile, 
  fetchInvestmentProfile 
} = useProfile()

onMounted(async () => {
  if (!profile.value) {
    await fetchProfile()
  }
  await fetchInvestmentProfile()
})

const avatarLetter = computed(() => {
  if (profile.value?.first_name) {
    return profile.value.first_name[0].toUpperCase()
  }
  if (profile.value?.username) {
    return profile.value.username[0].toUpperCase()
  }
  return 'U'
})

// Circular Gauge
const circumference = computed(() => 2 * Math.PI * 34)
const dashOffset = computed(() => 
  circumference.value - ((riskScore.value || 0) / 100) * circumference.value
)

// Radar Scores
const effectiveRadarScores = computed(() => {
  if (radarScores.value && typeof radarScores.value === 'object') {
    return {
      capacity: radarScores.value.capacity ?? 70,
      stress_resistance: radarScores.value.stress_resistance ?? 60,
      fomo_control: radarScores.value.fomo_control ?? 65,
      discipline: radarScores.value.discipline ?? 75
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

const getCategoryDescription = (category) => {
  const descs = {
    'Conservative': 'Приоритет сохранности капитала, минимальная волатильность за счет высокой доли надежных облигаций.',
    'Moderate': 'Баланс между доходностью и стабильностью. Оптимальное соотношение долевых и долговых инструментов.',
    'Growth': 'Акцент на прирост капитала в долгосрочной перспективе, высокая доля акций компаний с устойчивым бизнесом.',
    'Aggressive': 'Максимизация доходности, высокая устойчивость к волатильности, использование рискованных активов.'
  }
  return descs[category] || ''
}
</script>
