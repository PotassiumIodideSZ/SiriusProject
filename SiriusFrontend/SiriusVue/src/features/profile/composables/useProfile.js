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
  const investmentProfile = computed(() => profileStore.investmentProfile)
  const riskCategory = computed(() => profileStore.riskCategory)
  const keyTraits = computed(() => profileStore.keyTraits)
  const recommendations = computed(() => profileStore.recommendations)
  const assetAllocation = computed(() => profileStore.assetAllocation)
  
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
  
  const fetchInvestmentProfile = async () => {
    return await profileStore.fetchInvestmentProfile()
  }
  
  return {
    profile,
    stats,
    history,
    error,
    isLoading,
    riskScore,
    surveysCompleted,
    investmentProfile,
    riskCategory,
    keyTraits,
    recommendations,
    assetAllocation,
    fetchProfile,
    updateProfile,
    fetchHistory,
    fetchStats,
    fetchInvestmentProfile
  }
}
