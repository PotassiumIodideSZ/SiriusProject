import { computed } from 'vue'
import { useResultsStore } from '../stores/resultsStore'

export function useResults() {
  const resultsStore = useResultsStore()
  
  const results = computed(() => resultsStore.results)
  const recommendations = computed(() => resultsStore.recommendations)
  const riskScore = computed(() => resultsStore.riskScore)
  const riskCategory = computed(() => resultsStore.riskCategory)
  const assetAllocation = computed(() => resultsStore.assetAllocation)
  const keyTraits = computed(() => resultsStore.keyTraits)
  const error = computed(() => resultsStore.error)
  const isLoading = computed(() => resultsStore.isLoading)
  
  const fetchResults = async (surveyId) => {
    await resultsStore.fetchResults(surveyId)
  }
  
  const fetchRecommendations = async (surveyId) => {
    await resultsStore.fetchRecommendations(surveyId)
  }
  
  const fetchInvestmentProfile = async () => {
    return await resultsStore.fetchInvestmentProfile()
  }
  
  const loadInvestmentProfileFromStorage = () => {
    return resultsStore.loadInvestmentProfileFromStorage()
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
    riskCategory,
    assetAllocation,
    keyTraits,
    error,
    isLoading,
    fetchResults,
    fetchRecommendations,
    fetchInvestmentProfile,
    loadInvestmentProfileFromStorage,
    calculateRiskScore,
    resetResults
  }
}
