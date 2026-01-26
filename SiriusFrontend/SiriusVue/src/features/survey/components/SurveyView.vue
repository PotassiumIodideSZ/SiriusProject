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
              :style="{ width: `${progress}%` }"
            ></div>
          </div>
        </div>

        <h2 class="text-xl text-white mb-6">{{ currentQuestion.text }}</h2>
        
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
import { computed } from 'vue'
import { useSurvey } from '../composables/useSurvey'
import { SURVEY_OPTIONS } from '@/core/config/constants'

const {
  currentQuestion,
  currentQuestionIndex,
  questions,
  progress,
  answers,
  isLastQuestion,
  canMoveNext,
  nextQuestion,
  previousQuestion,
  finishSurvey
} = useSurvey()

const options = SURVEY_OPTIONS
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
