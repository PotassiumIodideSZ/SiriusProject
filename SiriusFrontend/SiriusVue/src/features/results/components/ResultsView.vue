<template>
  <div class="min-h-screen py-8 px-4">
    <div class="max-w-4xl mx-auto relative">
      <!-- Кнопка для возврата на главную в правом верхнем углу секции -->
      <router-link 
        to="/" 
        class="absolute top-0 right-0 bg-[#232323] hover:bg-[#2A2A2A] text-white p-2 rounded-full transition flex items-center justify-center"
        style="z-index: 10;"
      >
        <i class="fas fa-home"></i>
      </router-link>
      
      <!-- Loading state -->
      <div v-if="isLoading" class="flex items-center justify-center h-64">
        <div class="text-white text-xl">Загрузка результатов...</div>
      </div>
      
      <!-- Error state -->
      <div v-else-if="error" class="flex items-center justify-center h-64">
        <div class="text-red-400 text-xl">{{ error }}</div>
      </div>
      
      <!-- Results content -->
      <div v-else class="flex" style="align-items: flex-start;">
        <!-- Левая часть с результатом -->
        <div class="w-[30%] pr-8 flex flex-col items-center">
          <h1 class="text-3xl font-bold text-white mb-8">Результат</h1>
          <div class="relative w-48 h-48">
            <!-- Круговой прогресс -->
            <svg class="w-full h-full transform -rotate-90">
              <circle
                cx="96"
                cy="96"
                r="92"
                stroke="#232323"
                stroke-width="8"
                fill="none"
              />
              <circle
                cx="96"
                cy="96"
                r="92"
                stroke="#8B5CF6"
                stroke-width="8"
                fill="none"
                :stroke-dasharray="circumference"
                :stroke-dashoffset="dashOffset"
                class="transition-all duration-1000 ease-in-out"
              />
            </svg>
            <!-- Процент в центре -->
            <div class="absolute inset-0 flex items-center justify-center">
              <span class="text-4xl font-bold text-white">{{ riskScore }}%</span>
            </div>
            <div class="text-gray-400 text-center mt-4">Готовность к риску</div>
          </div>
          
          <!-- Risk Category Badge -->
          <div v-if="riskCategory" class="mt-6 px-4 py-2 rounded-full text-white font-semibold" :class="getCategoryColorClass(riskCategory)">
            {{ getCategoryLabel(riskCategory) }}
          </div>
          
          <!-- Key Traits -->
          <div v-if="keyTraits && keyTraits.length > 0" class="mt-6 w-full">
            <h3 class="text-lg font-semibold text-white mb-3">Ключевые черты:</h3>
            <ul class="space-y-2">
              <li 
                v-for="(trait, index) in keyTraits" 
                :key="index"
                class="text-gray-300 text-sm"
              >
                • {{ trait }}
              </li>
            </ul>
          </div>
        </div>

        <!-- Перегородка -->
        <div class="h-64 w-px bg-gray-600 mx-4"></div>

        <!-- Правая часть с рекомендациями -->
        <div class="w-[70%] pl-8">
          <h2 class="text-2xl font-semibold text-white mb-6">Рекомендации:</h2>
          <ul class="space-y-4">
            <li 
              v-for="(recommendation, index) in recommendations" 
              :key="index"
              class="flex items-center gap-3 text-gray-200"
            >
              <div class="w-2 h-2 rounded-full bg-purple-500"></div>
              {{ recommendation }}
            </li>
          </ul>
          
          <!-- Asset Allocation -->
          <div v-if="assetAllocation" class="mt-8">
            <h3 class="text-xl font-semibold text-white mb-4">Распределение активов:</h3>
            <div class="grid grid-cols-2 gap-4">
              <div 
                v-for="(percentage, asset) in assetAllocation" 
                :key="asset"
                class="bg-[#232323] p-4 rounded-lg"
              >
                <div class="text-gray-400 text-sm capitalize">{{ getAssetLabel(asset) }}</div>
                <div class="text-2xl font-bold text-white">{{ percentage }}%</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useResults } from '../composables/useResults'

const { 
  riskScore, 
  riskCategory, 
  recommendations, 
  assetAllocation, 
  keyTraits, 
  error, 
  isLoading,
  loadInvestmentProfileFromStorage,
  fetchInvestmentProfile 
} = useResults()

// Load investment profile on mount
onMounted(async () => {
  // First try to load from storage (from survey submission)
  const loadedFromStorage = loadInvestmentProfileFromStorage()
  
  // If not in storage, fetch from API
  if (!loadedFromStorage) {
    try {
      await fetchInvestmentProfile()
    } catch (err) {
      console.error('Failed to load investment profile:', err)
    }
  }
})

// Расчеты для кругового прогресса
const circumference = computed(() => 2 * Math.PI * 92)
const dashOffset = computed(() => 
  circumference.value - (riskScore.value / 100) * circumference.value
)

// Helper functions
const getCategoryLabel = (category) => {
  const labels = {
    'Conservative': 'Консервативный',
    'Moderate': 'Умеренный',
    'Growth': 'Рост',
    'Aggressive': 'Агрессивный'
  }
  return labels[category] || category
}

const getCategoryColorClass = (category) => {
  const colors = {
    'Conservative': 'bg-blue-500',
    'Moderate': 'bg-green-500',
    'Growth': 'bg-yellow-500',
    'Aggressive': 'bg-red-500'
  }
  return colors[category] || 'bg-purple-500'
}

const getAssetLabel = (asset) => {
  const labels = {
    'stocks': 'Акции',
    'bonds': 'Облигации',
    'cash': 'Наличные',
    'alternatives': 'Альтернативные'
  }
  return labels[asset] || asset
}
</script>

<style scoped>
/* Добавьте дополнительные стили, если необходимо */
circle {
  transition: stroke-dashoffset 1s ease-in-out;
}
</style>
