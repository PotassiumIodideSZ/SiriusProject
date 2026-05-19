<template>
  <div class="min-h-screen py-8 px-4">
    <!-- Верхний блок -->
    <div class="max-w-4xl mx-auto bg-[#1A1A1A] rounded-xl p-8 mb-8">
      <div class="flex flex-col md:flex-row items-center md:items-start gap-8">
        <!-- Аватар с синей обводкой -->
        <div class="relative">
          <div class="w-32 h-32 rounded-full border-4 border-blue-500 overflow-hidden">
            <img 
              src="/default-avatar.jpg" 
              alt="Профиль"
              class="w-full h-full object-cover"
            />
          </div>
        </div>

        <!-- Информация о пользователе -->
        <div class="flex-1">
          <div class="flex justify-between items-start mb-8">
            <h1 class="text-2xl font-semibold text-white">
              {{ profile ? `${profile.first_name} ${profile.last_name}` : 'Загрузка...' }}
            </h1>
            <router-link 
              to="/survey" 
              class="bg-purple-600 hover:bg-purple-700 text-white px-6 py-2 rounded-lg transition flex items-center gap-2"
            >
              <i class="fas fa-clipboard-list"></i>
              Начать тестирование
            </router-link>
          </div>
          
          <!-- Инвестиционный профиль -->
          <div class="bg-[#232323] rounded-lg p-6 mb-4">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-semibold text-white">Ваш инвестиционный профиль</h3>
            </div>
            
            <!-- Если профиль не загружен или пуст -->
            <div v-if="!investmentProfile || riskScore === 0" class="text-center py-8">
              <div class="text-gray-400 mb-4">
                <i class="fas fa-clipboard-question text-4xl mb-3"></i>
                <p class="text-lg">Вы еще не проходили тестирование</p>
                <p class="text-sm mt-2">Нам нужна информация, чтобы составить ваш инвестиционный профиль</p>
              </div>
              <router-link 
                to="/survey" 
                class="inline-block bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg transition"
              >
                <i class="fas fa-play mr-2"></i>
                Начать тестирование
              </router-link>
            </div>
            
            <!-- Если профиль загружен -->
            <div v-else>
              <div class="flex items-center justify-between mb-4">
                <button 
                  @click="toggleInvestmentProfile"
                  class="text-purple-400 hover:text-purple-300 transition flex items-center gap-2"
                >
                  {{ showInvestmentProfile ? '▲ Скрыть' : '▼ Показать подробности' }}
                </button>
              </div>
              
              <!-- Круговой прогресс и категория -->
              <div class="flex items-center gap-6">
                <div class="relative w-24 h-24">
                  <svg class="w-full h-full transform -rotate-90">
                    <circle
                      cx="48"
                      cy="48"
                      r="44"
                      stroke="#333333"
                      stroke-width="6"
                      fill="none"
                    />
                    <circle
                      cx="48"
                      cy="48"
                      r="44"
                      stroke="#8B5CF6"
                      stroke-width="6"
                      fill="none"
                      :stroke-dasharray="circumference"
                      :stroke-dashoffset="dashOffset"
                      class="transition-all duration-1000 ease-in-out"
                    />
                  </svg>
                  <div class="absolute inset-0 flex items-center justify-center">
                    <span class="text-xl font-bold text-white">{{ riskScore }}%</span>
                  </div>
                </div>
                
                <div v-if="riskCategory" class="flex-1">
                  <div class="text-sm text-gray-400 mb-1">Категория риска:</div>
                  <div 
                    class="inline-block px-4 py-1 rounded-full text-white font-semibold"
                    :class="getCategoryColorClass(riskCategory)"
                  >
                    {{ getCategoryLabel(riskCategory) }}
                  </div>
                </div>
              </div>
              
              <!-- Подробная информация (раскрывается при клике) -->
              <transition name="slide">
                <div v-if="showInvestmentProfile && investmentProfile" class="mt-6 space-y-6">
                  <!-- Ключевые черты -->
                  <div v-if="keyTraits && keyTraits.length > 0">
                    <h4 class="text-md font-semibold text-white mb-3">Ключевые черты:</h4>
                    <ul class="space-y-2">
                      <li 
                        v-for="(trait, index) in keyTraits" 
                        :key="index"
                        class="text-gray-300 text-sm flex items-start gap-2"
                      >
                        <span class="text-purple-400">•</span>
                        {{ trait }}
                      </li>
                    </ul>
                  </div>
                  
                  <!-- Рекомендации -->
                  <div v-if="recommendations && recommendations.length > 0">
                    <h4 class="text-md font-semibold text-white mb-3">Рекомендации:</h4>
                    <ul class="space-y-2">
                      <li 
                        v-for="(recommendation, index) in recommendations" 
                        :key="index"
                        class="text-gray-300 text-sm flex items-start gap-2"
                      >
                        <span class="text-purple-400">•</span>
                        {{ recommendation }}
                      </li>
                    </ul>
                  </div>
                  
                  <!-- Распределение активов -->
                  <div v-if="assetAllocation && Object.keys(assetAllocation).length > 0">
                    <h4 class="text-md font-semibold text-white mb-3">Распределение активов:</h4>
                    <div class="grid grid-cols-2 gap-3">
                      <div 
                        v-for="(percentage, asset) in assetAllocation" 
                        :key="asset"
                        class="bg-[#1A1A1A] p-3 rounded-lg"
                      >
                        <div class="text-gray-400 text-xs capitalize">{{ getAssetLabel(asset) }}</div>
                        <div class="text-lg font-bold text-white">{{ percentage }}%</div>
                      </div>
                    </div>
                  </div>
                </div>
              </transition>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useProfile } from '../composables/useProfile'

const { 
  profile, 
  riskScore, 
  investmentProfile,
  riskCategory,
  keyTraits,
  recommendations,
  assetAllocation,
  fetchProfile,
  fetchInvestmentProfile 
} = useProfile()

const showInvestmentProfile = ref(false)

onMounted(async () => {
  if (!profile.value) {
    await fetchProfile()
  }
  // Fetch investment profile
  await fetchInvestmentProfile()
})

function toggleInvestmentProfile() {
  showInvestmentProfile.value = !showInvestmentProfile.value
}

// Расчеты для кругового прогресса
const circumference = computed(() => 2 * Math.PI * 44)
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
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.slide-enter-active, .slide-leave-active {
  transition: all 0.3s ease-in-out;
  max-height: 1000px;
  opacity: 1;
}
.slide-enter-from, .slide-leave-to {
  max-height: 0;
  opacity: 0;
  overflow: hidden;
}

/* Стили для кругового прогресса */
circle {
  transition: stroke-dashoffset 1s ease-in-out;
}
</style>
