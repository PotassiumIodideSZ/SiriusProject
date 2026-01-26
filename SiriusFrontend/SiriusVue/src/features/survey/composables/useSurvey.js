import { computed } from 'vue'
import { useSurveyStore } from '../stores/surveyStore'

export function useSurvey() {
  const surveyStore = useSurveyStore()
  
  const questions = computed(() => surveyStore.questions)
  const currentQuestion = computed(() => surveyStore.currentQuestion)
  const currentQuestionIndex = computed(() => surveyStore.currentQuestionIndex)
  const progress = computed(() => surveyStore.progress)
  const answers = computed(() => surveyStore.answers)
  const isLoading = computed(() => surveyStore.isLoading)
  const isLastQuestion = computed(() => surveyStore.isLastQuestion)
  const canMoveNext = computed(() => surveyStore.canMoveNext)
  const error = computed(() => surveyStore.error)
  
  const startSurvey = async () => {
    surveyStore.resetSurvey()
    return await surveyStore.fetchQuestions()
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
    isLoading,
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
