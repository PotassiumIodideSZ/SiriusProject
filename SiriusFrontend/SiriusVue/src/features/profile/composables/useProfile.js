import { computed } from 'vue'
import { useProfileStore } from '../stores/profileStore'

export function useProfile() {
  const profileStore = useProfileStore()
  
  const profile = computed(() => profileStore.profile)
  const stats = computed(() => profileStore.stats)
  const history = computed(() => profileStore.history)
  const error = computed(() => profileStore.error)
  const isLoading = computed(() => profileStore.isLoading)
  const riskScore = computed(() => profileStore.riskScore)
  const surveysCompleted = computed(() => profileStore.surveysCompleted)
  
  const fetchProfile = async () => {
    await profileStore.fetchProfile()
  }
  
  const updateProfile = async (data) => {
    return await profileStore.updateProfile(data)
  }
  
  const fetchHistory = async () => {
    await profileStore.fetchHistory()
  }
  
  const fetchStats = async () => {
    await profileStore.fetchStats()
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
}
