import api from '@/core/api/axiosInstance'
import { API_ENDPOINTS, STORAGE_KEYS } from '@/core/config/constants'

export const resultsAPI = {
  async getResults(surveyId) {
    const response = await api.get(`${API_ENDPOINTS.RESULTS.GET}${surveyId}/`)
    return response.data
  },

  async getRecommendations(surveyId) {
    const response = await api.get(`${API_ENDPOINTS.RESULTS.RECOMMENDATIONS}${surveyId}/`)
    return response.data
  },

  async getInvestmentProfile() {
    const response = await api.get(API_ENDPOINTS.RESULTS.INVESTMENT_PROFILE)
    return response.data
  },

  getInvestmentProfileFromStorage() {
    const stored = localStorage.getItem(STORAGE_KEYS.RISK_PROFILE)
    return stored ? JSON.parse(stored) : null
  },

  clearInvestmentProfileFromStorage() {
    localStorage.removeItem(STORAGE_KEYS.RISK_PROFILE)
  }
}
