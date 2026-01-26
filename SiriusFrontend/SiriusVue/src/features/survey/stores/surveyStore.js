import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { surveyAPI } from '../services/surveyAPI'
import { SURVEY_OPTIONS } from '@/core/config/constants'

export const useSurveyStore = defineStore('survey', () => {
  const router = useRouter()
  
  const questions = ref([
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
  ])
  
  const currentQuestionIndex = ref(0)
  const answers = ref(new Array(questions.value.length).fill(null))
  const isCompleted = ref(false)
  const error = ref(null)

  const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])
  const progress = computed(() => ((currentQuestionIndex.value + 1) / questions.value.length * 100).toFixed(0))
  const isLastQuestion = computed(() => currentQuestionIndex.value === questions.value.length - 1)
  const canMoveNext = computed(() => answers.value[currentQuestionIndex.value] !== null)

  const nextQuestion = () => {
    if (currentQuestionIndex.value < questions.value.length - 1) {
      currentQuestionIndex.value++
    }
  }

  const previousQuestion = () => {
    if (currentQuestionIndex.value > 0) {
      currentQuestionIndex.value--
    }
  }

  const submitAnswer = (answer) => {
    answers.value[currentQuestionIndex.value] = answer
  }

  const finishSurvey = async () => {
    try {
      error.value = null
      const result = await surveyAPI.submitSurvey(answers.value)
      isCompleted.value = true
      router.push('/results')
      return result
    } catch (err) {
      error.value = err.response?.data || 'Произошла ошибка при отправке опроса'
      console.error('Ошибка при отправке опроса:', err)
    }
  }

  const resetSurvey = () => {
    currentQuestionIndex.value = 0
    answers.value = new Array(questions.value.length).fill(null)
    isCompleted.value = false
    error.value = null
  }

  return {
    questions,
    currentQuestionIndex,
    answers,
    isCompleted,
    error,
    currentQuestion,
    progress,
    isLastQuestion,
    canMoveNext,
    nextQuestion,
    previousQuestion,
    submitAnswer,
    finishSurvey,
    resetSurvey
  }
})
