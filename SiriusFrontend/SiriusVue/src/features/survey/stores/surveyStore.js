import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { surveyAPI } from '../services/surveyAPI'

export const useSurveyStore = defineStore('survey', () => {
  const router = useRouter()
  
  const questions = ref([])
  const currentQuestionIndex = ref(0)
  const answers = ref([])
  const isLoading = ref(false)
  const isCompleted = ref(false)
  const error = ref(null)

  const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])
  const progress = computed(() => ((currentQuestionIndex.value + 1) / questions.value.length * 100).toFixed(0))
  const isLastQuestion = computed(() => currentQuestionIndex.value === questions.value.length - 1)
  const canMoveNext = computed(() => answers.value[currentQuestionIndex.value] !== null)

  const fetchQuestions = async () => {
    try {
      isLoading.value = true
      error.value = null
      const data = await surveyAPI.getQuestions()
      questions.value = data.questions || []
      // Initialize answers array with null values
      answers.value = new Array(questions.value.length).fill(null)
      return questions.value
    } catch (err) {
      error.value = err.response?.data?.detail || 'Не удалось загрузить вопросы'
      console.error('Ошибка при загрузке вопросов:', err)
      throw err
    } finally {
      isLoading.value = false
    }
  }

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
      isLoading.value = true
      error.value = null
      
      // Transform answers to new format: [{question_id: 1, answer_value: 5}, ...]
      const answersArray = []
      questions.value.forEach((question, index) => {
        answersArray.push({
          question_id: question.id,
          answer_value: answers.value[index]
        })
      })
      
      const result = await surveyAPI.submitSurvey(answersArray)
      isCompleted.value = true
      router.push('/results')
      return result
    } catch (err) {
      error.value = err.response?.data?.detail || 'Произошла ошибка при отправке опроса'
      console.error('Ошибка при отправке опроса:', err)
      throw err
    } finally {
      isLoading.value = false
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
    isLoading,
    isCompleted,
    error,
    currentQuestion,
    progress,
    isLastQuestion,
    canMoveNext,
    fetchQuestions,
    nextQuestion,
    previousQuestion,
    submitAnswer,
    finishSurvey,
    resetSurvey
  }
})
