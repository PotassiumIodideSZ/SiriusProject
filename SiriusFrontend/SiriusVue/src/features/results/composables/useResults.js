import { computed } from 'vue'
import { useResultsStore } from '../stores/resultsStore'

export function useResults() {
  const resultsStore = useResultsStore()
  
  const results = computed(() => resultsStore.results)
  const recommendations = computed(() => resultsStore.recommendations)
  const riskScore = computed(() => resultsStore.riskScore)
  const error = computed(() => resultsStore.error)
  const isLoading = computed(() => resultsStore.isLoading)
  
  const fetchResults = async (surveyId) => {
    await resultsStore.fetchResults(surveyId)
  }
  
  const fetchRecommendations = async (surveyId) => {
    await resultsStore.fetchRecommendations(surveyId)
  }
  
  const calculateRiskScore = (answers) => {
    return resultsStore.calculateRiskScore(answers)
  }
  
  const resetResults = () => {
    resultsStore.resetResults()
  }
  
  return {
    results,
    recommendations,
    riskScore,
    error,
    isLoading,
    fetchResults,
    fetchRecommendations,
    calculateRiskScore,
    resetResults
  }
}
