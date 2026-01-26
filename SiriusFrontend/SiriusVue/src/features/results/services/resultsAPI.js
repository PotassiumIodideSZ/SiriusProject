import api from '@/core/api/axiosInstance'
import { API_ENDPOINTS } from '@/core/config/constants'

export const resultsAPI = {
  async getResults(surveyId) {
    const response = await api.get(`${API_ENDPOINTS.RESULTS.GET}${surveyId}/`)
    return response.data
  },

  async getRecommendations(surveyId) {
    const response = await api.get(`${API_ENDPOINTS.RESULTS.RECOMMENDATIONS}${surveyId}/`)
    return response.data
  }
}
