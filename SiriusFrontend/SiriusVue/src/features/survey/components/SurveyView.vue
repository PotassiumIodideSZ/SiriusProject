<template>
  <div class="min-h-[85vh] py-10 px-4 sm:px-6 flex items-center justify-center">
    <div class="max-w-3xl w-full mx-auto space-y-6">
      <!-- Top Title -->
      <div class="text-center space-y-2">
        <div class="badge-amber">КОГНИТИВНЫЙ ИНВЕСТ-ПРОФИЛЬ</div>
        <h1 class="text-3xl sm:text-4xl font-serif font-bold text-ink-950 tracking-tight">
          Диагностика инвестиционного характера
        </h1>
        <p class="text-xs sm:text-sm text-ink-500 font-mono">
          12 поведенческих дилемм · Радар мышления · Риск-паспорт
        </p>
      </div>
      
      <!-- Polling / Calculating State (Animated Editorial Screen) -->
      <div v-if="isCalculating" class="academic-card p-10 sm:p-14 text-center space-y-6 bg-white border-amber-300 shadow-md">
        <div class="relative w-20 h-20 mx-auto flex items-center justify-center">
          <div class="absolute inset-0 rounded-full border-4 border-amber-200 border-t-amber-600 animate-spin"></div>
          <i class="fas fa-brain text-2xl text-academic-amber"></i>
        </div>

        <div class="space-y-2">
          <h3 class="text-xl sm:text-2xl font-serif font-bold text-ink-950">
            ИИ-модель формирует инвестиционный паспорт
          </h3>
          <p class="text-xs sm:text-sm font-mono text-academic-amber font-semibold animate-pulse">
            {{ pollingStatus || 'Обработка ответов и расчет когнитивной радар-карты...' }}
          </p>
        </div>

        <div class="max-w-md mx-auto pt-4 border-t border-ink-100 text-xs font-mono text-ink-400 space-y-1">
          <div>· Калибровка осей: емкость, стойкость, автономия, дисциплина</div>
          <div>· Подбор оптимальной структуры портфеля (Asset Allocation)</div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-else-if="isLoading && (!questions || questions.length === 0)" class="academic-card p-12 text-center space-y-4">
        <div class="inline-block w-8 h-8 border-2 border-academic-amber border-t-transparent rounded-full animate-spin"></div>
        <div class="text-ink-600 font-mono text-sm">Загрузка вопросов диагностики...</div>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="academic-card p-8 text-center space-y-4 border-red-200">
        <div class="text-academic-crimson text-sm font-mono">{{ error }}</div>
        <button 
          @click="startSurvey" 
          class="px-6 py-2.5 bg-ink-100 hover:bg-ink-200 text-ink-800 rounded-xl text-xs font-mono transition"
        >
          Попробовать снова
        </button>
      </div>

      <!-- No Questions -->
      <div v-else-if="questions.length === 0" class="academic-card p-8 text-center">
        <div class="text-ink-500 text-sm font-mono">Нет доступных вопросов</div>
      </div>

      <!-- Survey Card -->
      <div v-else class="academic-card p-6 sm:p-10 space-y-8 bg-white border-ink-200 shadow-sm">
        <!-- Header Counter & Progress -->
        <div class="space-y-3">
          <div class="flex justify-between items-center text-xs font-mono">
            <span class="text-academic-amber font-semibold">
              ДИЛЕММА {{ currentQuestionIndex + 1 }} ИЗ {{ questions.length }}
            </span>
            <span class="text-ink-400">
              {{ Math.round(progress) }}% пройдено
            </span>
          </div>

          <!-- Progress Bar -->
          <div class="w-full h-1.5 bg-ink-100 rounded-full overflow-hidden">
            <div 
              class="h-full bg-academic-amber transition-all duration-300 rounded-full"
              :style="{ width: `${progress}%` }"
            ></div>
          </div>
        </div>

        <!-- Question Category Badge -->
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-md text-[10px] font-mono uppercase tracking-wider bg-paper-100 text-ink-600 border border-ink-200">
            {{ getCategoryName(currentQuestion?.category) }}
          </span>
        </div>

        <!-- Question Text in Newsreader Serif -->
        <div class="min-h-[60px] flex items-center">
          <h2 class="text-xl sm:text-2xl font-serif font-bold text-ink-950 leading-snug">
            {{ currentQuestion?.text }}
          </h2>
        </div>
        
        <!-- Options List -->
        <div class="space-y-3">
          <label 
            v-for="(option, index) in currentOptions" 
            :key="index"
            class="flex items-start justify-between p-4 rounded-xl border transition-all cursor-pointer group select-none"
            :class="answers[currentQuestionIndex] === option.value 
              ? 'bg-amber-50/80 border-academic-amber shadow-sm ring-1 ring-amber-400/40' 
              : 'bg-paper-50/70 border-ink-200/80 hover:bg-white hover:border-ink-300'"
          >
            <div class="flex items-start gap-3.5 pr-3">
              <input 
                type="radio" 
                :name="'question_' + currentQuestionIndex" 
                :value="option.value"
                v-model="answers[currentQuestionIndex]"
                class="sr-only"
              />
              <div 
                class="w-5 h-5 mt-0.5 rounded-full border flex-shrink-0 flex items-center justify-center transition-colors"
                :class="answers[currentQuestionIndex] === option.value 
                  ? 'border-academic-amber bg-academic-amber' 
                  : 'border-ink-300 group-hover:border-ink-500 bg-white'"
              >
                <div 
                  v-if="answers[currentQuestionIndex] === option.value" 
                  class="w-2 h-2 rounded-full bg-white"
                ></div>
              </div>
              <span 
                class="text-sm font-medium leading-relaxed transition-colors"
                :class="answers[currentQuestionIndex] === option.value ? 'text-ink-950 font-semibold' : 'text-ink-700 group-hover:text-ink-900'"
              >
                {{ option.text }}
              </span>
            </div>
            <span class="text-xs font-mono text-ink-400 group-hover:text-ink-600 flex-shrink-0 mt-0.5">
              {{ String.fromCharCode(65 + index) }}
            </span>
          </label>
        </div>

        <!-- Navigation Buttons -->
        <div class="flex justify-between items-center pt-4 border-t border-ink-200">
          <button 
            @click="previousQuestion" 
            :disabled="currentQuestionIndex === 0 || isLoading || isCalculating"
            class="px-5 py-2.5 bg-ink-100 hover:bg-ink-200 disabled:opacity-40 disabled:cursor-not-allowed text-ink-700 hover:text-ink-950 rounded-xl text-xs font-mono transition-all flex items-center gap-2"
          >
            <i class="fas fa-arrow-left text-xs"></i>
            <span>Назад</span>
          </button>

          <button 
            @click="isLastQuestion ? finishSurvey() : nextQuestion()" 
            :disabled="!canMoveNext || isLoading || isCalculating"
            class="px-6 py-2.5 bg-ink-950 hover:bg-ink-800 disabled:opacity-40 disabled:cursor-not-allowed text-amber-300 font-sans font-medium rounded-xl text-sm transition-all shadow-sm active:scale-[0.98] flex items-center gap-2"
          >
            <span>{{ isLastQuestion ? 'Сформировать паспорт и радар-карту' : 'Следующий вопрос' }}</span>
            <i :class="isLastQuestion ? 'fas fa-chart-line' : 'fas fa-arrow-right'" class="text-xs"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useSurvey } from '../composables/useSurvey'

const {
  currentQuestion,
  currentQuestionIndex,
  questions,
  progress,
  answers,
  isLoading,
  isCalculating,
  pollingStatus,
  isLastQuestion,
  canMoveNext,
  error,
  startSurvey,
  nextQuestion,
  previousQuestion,
  finishSurvey
} = useSurvey()

const currentOptions = computed(() => {
  if (currentQuestion.value?.options && currentQuestion.value.options.length > 0) {
    return currentQuestion.value.options
  }
  return [
    { value: 1, text: 'Полностью согласен' },
    { value: 2, text: 'Скорее согласен' },
    { value: 3, text: 'Затрудняюсь ответить' },
    { value: 4, text: 'Скорее не согласен' },
    { value: 5, text: 'Полностью не согласен' }
  ]
})

const getCategoryName = (category) => {
  const map = {
    'capacity': 'ФИНАНСОВЫЙ ФУНДАМЕНТ И ГОРИЗОНТ',
    'stress': 'СТРЕСС-ТЕСТИРОВАНИЕ И РИСК-АППЕТИТ',
    'behavioral': 'ПОВЕДЕНЧЕСКИЕ ПАТТЕРНЫ И FOMO',
    'discipline': 'СТРАТЕГИЧЕСКАЯ ДИСЦИПЛИНА'
  }
  return map[category] || 'ИНВЕСТИЦИОННАЯ ДИЛЕММА'
}

onMounted(() => {
  startSurvey()
})
</script>
