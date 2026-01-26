import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { resultsAPI } from '../services/resultsAPI'

export const useResultsStore = defineStore('results', () => {
  const results = ref(null)
  const recommendations = ref([])
  const riskScore = ref(0)
  const riskCategory = ref('')
  const assetAllocation = ref(null)
  const keyTraits = ref([])
  const error = ref(null)
  const isLoading = ref(false)

  const fetchResults = async (surveyId) => {
    try {
      isLoading.value = true
      error.value = null
      const data = await resultsAPI.getResults(surveyId)
      results.value = data
      riskScore.value = data.risk_score || 0
    } catch (err) {
      error.value = err.response?.data || 'Ошибка при получении результатов'
      console.error('Ошибка при получении результатов:', err)
    } finally {
      isLoading.value = false
    }
  }

  const fetchRecommendations = async (surveyId) => {
    try {
      isLoading.value = true
      error.value = null
      const data = await resultsAPI.getRecommendations(surveyId)
      recommendations.value = data
    } catch (err) {
      error.value = err.response?.data || 'Ошибка при получении рекомендаций'
      console.error('Ошибка при получении рекомендаций:', err)
    } finally {
      isLoading.value = false
    }
  }

  const fetchInvestmentProfile = async () => {
    try {
      isLoading.value = true
      error.value = null
      const data = await resultsAPI.getInvestmentProfile()
      
      // Store all profile data
      results.value = data
      riskScore.value = data.risk_score || 0
      riskCategory.value = data.risk_category || ''
      recommendations.value = data.recommendations || []
      assetAllocation.value = data.asset_allocation || null
      keyTraits.value = data.key_traits || []
      
      return data
    } catch (err) {
      error.value = err.response?.data || 'Ошибка при получении инвестиционного профиля'
      console.error('Ошибка при получении инвестиционного профиля:', err)
      throw err
    } finally {
      isLoading.value = false
    }
  }

  const loadInvestmentProfileFromStorage = () => {
    const profile = resultsAPI.getInvestmentProfileFromStorage()
    if (profile) {
      results.value = profile
      riskScore.value = profile.risk_score || 0
      riskCategory.value = profile.risk_category || ''
      recommendations.value = profile.recommendations || []
      assetAllocation.value = profile.asset_allocation || null
      keyTraits.value = profile.key_traits || []
      return true
    }
    return false
  }

  const calculateRiskScore = (answers) => {
    // Простая логика для расчета риска
    // В реальном приложении это будет сделано на бэкенде
    const totalScore = answers.reduce((sum, answer) => sum + answer, 0)
    const maxScore = answers.length * 5
    const percentage = Math.round((totalScore / maxScore) * 100)
    return percentage
  }

  const resetResults = () => {
    results.value = null
    recommendations.value = []
    riskScore.value = 0
    riskCategory.value = ''
    assetAllocation.value = null
    keyTraits.value = []
    error.value = null
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
})
