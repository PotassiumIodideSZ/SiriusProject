import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { resultsAPI } from '../services/resultsAPI'

export const useResultsStore = defineStore('results', () => {
  const results = ref(null)
  const recommendations = ref([])
  const riskScore = ref(0)
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
    error.value = null
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
})
