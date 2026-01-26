import api from '@/core/api/axiosInstance'
import { API_ENDPOINTS } from '@/core/config/constants'

export const profileAPI = {
  async getProfile() {
    const response = await api.get(API_ENDPOINTS.PROFILE.GET)
    return response.data
  },

  async updateProfile(data) {
    const response = await api.put(API_ENDPOINTS.PROFILE.UPDATE, data)
    return response.data
  },

  async getHistory() {
    const response = await api.get(API_ENDPOINTS.PROFILE.HISTORY)
    return response.data
  },

  async getStats() {
    const response = await api.get(API_ENDPOINTS.PROFILE.STATS)
    return response.data
  },

  async getInvestmentProfile() {
    const response = await api.get(API_ENDPOINTS.RESULTS.INVESTMENT_PROFILE)
    return response.data
  }
}
