import api from '@/core/api/axiosInstance'
import { API_ENDPOINTS } from '@/core/config/constants'

export const surveyAPI = {
  async getQuestions() {
    const response = await api.get(API_ENDPOINTS.SURVEY.QUESTIONS)
    return response.data
  },

  async submitSurvey(answers) {
    const response = await api.post(API_ENDPOINTS.SURVEY.SUBMIT, { answers })
    return response.data
  },

  async getSurveyHistory() {
    const response = await api.get(API_ENDPOINTS.SURVEY.HISTORY)
    return response.data
  }
}
