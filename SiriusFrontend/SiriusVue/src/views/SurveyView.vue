<template>
  <div class="min-h-screen py-8 px-4">
    <div class="max-w-3xl mx-auto">
      <h1 class="text-3xl font-bold text-white text-center mb-8">Анкета</h1>
      
      <!-- Карточка с вопросом -->
      <div class="bg-[#1A1A1A] rounded-xl p-8">
        <!-- Счетчик вопросов -->
        <div class="flex justify-between items-center mb-6">
          <span class="text-gray-400">
            Вопрос {{ currentQuestionIndex + 1 }} из {{ questions.length }}
          </span>
          <!-- Прогресс-бар -->
          <div class="w-48 h-2 bg-[#232323] rounded-full overflow-hidden">
            <div 
              class="h-full bg-purple-600 transition-all duration-300"
              :style="{ width: `${(currentQuestionIndex + 1) / questions.length * 100}%` }"
            ></div>
          </div>
        </div>

        <h2 class="text-xl text-white mb-6">{{ questions[currentQuestionIndex].text }}</h2>
        
        <!-- Варианты ответов -->
        <div class="space-y-4 mb-8">
          <label 
            v-for="(option, index) in options" 
            :key="index"
            class="flex items-center gap-3 p-4 rounded-lg bg-[#232323] hover:bg-[#2A2A2A] cursor-pointer transition"
          >
            <input 
              type="radio" 
              :name="'question'" 
              :value="option.value"
              v-model="answers[currentQuestionIndex]"
              class="w-4 h-4 text-purple-600 focus:ring-purple-500"
            />
            <span class="text-gray-200">{{ option.text }}</span>
          </label>
        </div>

        <!-- Навигационные кнопки -->
        <div class="flex justify-between items-center">
          <button 
            @click="previousQuestion" 
            :disabled="currentQuestionIndex === 0"
            class="px-6 py-2 bg-purple-600 hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-lg transition flex items-center gap-2"
          >
            <i class="fas fa-arrow-left"></i>
            Назад
          </button>

          <!-- Кнопка Далее/Завершить -->
          <button 
            @click="isLastQuestion ? finishSurvey() : nextQuestion()" 
            :disabled="!canMoveNext"
            class="px-6 py-2 bg-purple-600 hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-lg transition flex items-center gap-2"
          >
            {{ isLastQuestion ? 'Завершить' : 'Далее' }}
            <i :class="isLastQuestion ? 'fas fa-check' : 'fas fa-arrow-right'"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const questions = [
  { text: 'Ваши логические умозаключения чаще всего обоснованны и правильны?' },
  { text: 'Влияет ли чужое мнение на ваше мышление?' },
  { text: 'Вы строите свою жизнь на основе обдуманных решений?' },
  { text: 'Вы доверяете логическим умозаключениям?' },
  { text: 'Появление оригинальной сильной идеи доставляет вам радость?' },
  { text: 'Во время дискуссий вы чувствуете себя уверенно?' },
  { text: 'Вас можно назвать вдумчивым человеком?' },
  { text: 'Вас можно назвать эмоциональным человеком?' },
  { text: 'Вы верите астрологам?' },
  { text: 'Вас можно назвать суеверным человеком?' },
  { text: 'Ваши чувства и эмоции управляют вами?' },
  { text: 'Вы склонны к резкой смене настроения?' },
  { text: 'Вы стремитесь обладать чем-либо или кем-либо единолично и безраздельно?' },
  { text: 'Вас можно назвать скупым человеком?' },
  { text: 'Вас можно назвать ответственным человеком?' },
  { text: 'Вам легко дается руководить деятельностью других людей?' },
  { text: 'Вас можно назвать независимым человеком?' },
  { text: 'Способны ли вы самостоятельно и своевременно принимать ответственные решения?' },
  { text: 'Свое поведение вы держите под контролем?' },
  { text: 'Можно ли вас назвать настойчивым человеком?' },
  { text: 'Начатые дела вы доводите до конца?' },
  { text: 'Обладаете ли вы волевыми качествами?' },
  { text: 'Вы можете вести за собой других людей?' }
]

const options = [
  { value: 1, text: 'Полностью согласен' },
  { value: 2, text: 'Скорее согласен' },
  { value: 3, text: 'Затрудняюсь ответить' },
  { value: 4, text: 'Скорее не согласен' },
  { value: 5, text: 'Полностью не согласен' }
]

const currentQuestionIndex = ref(0)
const answers = ref(new Array(questions.length).fill(null))

const isLastQuestion = computed(() => {
  return currentQuestionIndex.value === questions.length - 1
})

const canMoveNext = computed(() => {
  return answers.value[currentQuestionIndex.value] !== null
})

const nextQuestion = () => {
  if (currentQuestionIndex.value < questions.length - 1) {
    currentQuestionIndex.value++
  }
}

const previousQuestion = () => {
  if (currentQuestionIndex.value > 0) {
    currentQuestionIndex.value--
  }
}

const finishSurvey = () => {
  // Проверяем, что на все вопросы даны ответы
  if (answers.value.every(answer => answer !== null)) {
    // Здесь можно добавить логику обработки ответов
    console.log('Ответы:', answers.value)
    // Переходим на страницу результатов
    router.push('/results')
  }
}
</script>

<style scoped>
/* Стилизация radio кнопок */
input[type="radio"] {
  @apply appearance-none w-4 h-4 rounded-full border-2 border-gray-400;
}

input[type="radio"]:checked {
  @apply border-purple-500 bg-purple-500;
}

input[type="radio"]:checked::after {
  content: "";
  @apply block w-2 h-2 mx-auto mt-0.5 bg-white rounded-full;
}
</style> 