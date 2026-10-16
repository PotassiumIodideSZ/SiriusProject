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

  const pollingStatus = ref(null)
  const isCalculating = ref(false)

  const finishSurvey = async () => {
    try {
      isLoading.value = true
      isCalculating.value = true
      pollingStatus.value = 'Отправка ответов на сервер...'
      error.value = null
      
      // Transform answers to format: [{question_id: 1, answer_value: 5}, ...]
      const answersArray = []
      questions.value.forEach((question, index) => {
        answersArray.push({
          question_id: question.id,
          answer_value: answers.value[index]
        })
      })
      
      const result = await surveyAPI.submitSurvey(answersArray)
      const qId = result.questionnaire_id

      if (!qId) {
        throw new Error('Не получен идентификатор анкеты')
      }

      // Start polling
      pollingStatus.value = 'Запущен ИИ-анализ инвестиционного профиля...'
      const maxAttempts = 30
      let attempts = 0
      let completedProfile = null

      while (attempts < maxAttempts) {
        attempts++
        if (attempts === 2) {
          pollingStatus.value = 'Изучение финансовой емкости и горизонта...'
        } else if (attempts === 4) {
          pollingStatus.value = 'Стресс-тестирование психологической стойкости...'
        } else if (attempts === 7) {
          pollingStatus.value = 'Построение когнитивной радар-карты и портфеля...'
        }

        await new Promise(resolve => setTimeout(resolve, 2000))

        try {
          const statusData = await surveyAPI.getSurveyStatus(qId)
          if (statusData.is_completed) {
            completedProfile = statusData.profile
            break
          } else if (statusData.status === 'FAILED') {
            throw new Error(statusData.error_message || 'Ошибка расчета на сервере')
          }
        } catch (pollErr) {
          console.warn('Ошибка поллинга (повтор):', pollErr)
        }
      }

      if (completedProfile) {
        localStorage.setItem('riskProfile', JSON.stringify(completedProfile))
      }

      isCompleted.value = true
      router.push('/results')
      return result
    } catch (err) {
      error.value = err.response?.data?.error || err.message || 'Произошла ошибка при обработке опроса'
      console.error('Ошибка при отправке опроса:', err)
      throw err
    } finally {
      isLoading.value = false
      isCalculating.value = false
      pollingStatus.value = null
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
    isCalculating,
    pollingStatus,
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
