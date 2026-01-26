import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { profileAPI } from '../services/profileAPI'

export const useProfileStore = defineStore('profile', () => {
  const profile = ref(null)
  const stats = ref({})
  const history = ref([])
  const error = ref(null)
  const isLoading = ref(false)

  const riskScore = computed(() => stats.value?.risk_score || 0)
  const surveysCompleted = computed(() => history.value?.length || 0)

  const fetchProfile = async () => {
    try {
      isLoading.value = true
      error.value = null
      const data = await profileAPI.getProfile()
      profile.value = data
    } catch (err) {
      error.value = err.response?.data || 'Ошибка при получении профиля'
      console.error('Ошибка при получении профиля:', err)
    } finally {
      isLoading.value = false
    }
  }

  const updateProfile = async (data) => {
    try {
      isLoading.value = true
      error.value = null
      const result = await profileAPI.updateProfile(data)
      profile.value = result
      return result
    } catch (err) {
      error.value = err.response?.data || 'Ошибка при обновлении профиля'
      console.error('Ошибка при обновлении профиля:', err)
      throw err
    } finally {
      isLoading.value = false
    }
  }

  const fetchHistory = async () => {
    try {
      isLoading.value = true
      error.value = null
      const data = await profileAPI.getHistory()
      history.value = data
    } catch (err) {
      error.value = err.response?.data || 'Ошибка при получении истории'
      console.error('Ошибка при получении истории:', err)
    } finally {
      isLoading.value = false
    }
  }

  const fetchStats = async () => {
    try {
      isLoading.value = true
      error.value = null
      const data = await profileAPI.getStats()
      stats.value = data
    } catch (err) {
      error.value = err.response?.data || 'Ошибка при получении статистики'
      console.error('Ошибка при получении статистики:', err)
    } finally {
      isLoading.value = false
    }
  }

  return {
    profile,
    stats,
    history,
    error,
    isLoading,
    riskScore,
    surveysCompleted,
    fetchProfile,
    updateProfile,
    fetchHistory,
    fetchStats
  }
})
