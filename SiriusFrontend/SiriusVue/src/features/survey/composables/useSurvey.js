import { computed } from 'vue'
import { useSurveyStore } from '../stores/surveyStore'
import { SURVEY_OPTIONS } from '@/core/config/constants'

export function useSurvey() {
  const surveyStore = useSurveyStore()
  
  const questions = computed(() => surveyStore.questions)
  const currentQuestion = computed(() => surveyStore.currentQuestion)
  const currentQuestionIndex = computed(() => surveyStore.currentQuestionIndex)
  const progress = computed(() => surveyStore.progress)
  const answers = computed(() => surveyStore.answers)
  const isLastQuestion = computed(() => surveyStore.isLastQuestion)
  const canMoveNext = computed(() => surveyStore.canMoveNext)
  const error = computed(() => surveyStore.error)
  
  const startSurvey = () => {
    surveyStore.resetSurvey()
  }
  
  const nextQuestion = () => {
    surveyStore.nextQuestion()
  }
  
  const previousQuestion = () => {
    surveyStore.previousQuestion()
  }
  
  const submitAnswer = (answer) => {
    surveyStore.submitAnswer(answer)
  }
  
  const finishSurvey = async () => {
    return await surveyStore.finishSurvey()
  }
  
  return {
    questions,
    currentQuestion,
    currentQuestionIndex,
    progress,
    answers,
    isLastQuestion,
    canMoveNext,
    error,
    startSurvey,
    nextQuestion,
    previousQuestion,
    submitAnswer,
    finishSurvey
  }
}
