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
              {{ user ? `${user.first_name} ${user.last_name}` : 'Загрузка...' }}
            </h1>
            <router-link 
              to="/survey" 
              class="bg-purple-600 hover:bg-purple-700 text-white px-6 py-2 rounded-lg transition flex items-center gap-2"
            >
              <i class="fas fa-clipboard-list"></i>
              Начать тестирование
            </router-link>
          </div>
          
          <!-- Статистика -->
          <div class="flex flex-wrap gap-8 justify-center">
            <div class="text-center">
              <div class="text-3xl font-bold text-blue-500">72%</div>
              <div class="text-sm text-gray-400">Склонность к риску</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-purple-500">3</div>
              <div class="text-sm text-gray-400">Пройдено тестов</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Нижний блок - История анализов -->
    <div class="max-w-4xl mx-auto">
      <h2 class="text-xl font-semibold text-white mb-6">История</h2>
      
      <!-- Список анализов -->
      <div class="space-y-4">
        <div 
          v-for="(analysis, index) in analyses" 
          :key="index"
          class="bg-[#1A1A1A] rounded-lg p-4 hover:bg-[#232323] transition cursor-pointer"
          @click="toggleAnalysis(index)"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-4">
              <div class="w-2 h-2 rounded-full" :class="analysis.statusColor"></div>
              <span class="text-white">{{ analysis.name }}</span>
            </div>
            <div class="text-gray-400">{{ analysis.date }}</div>
          </div>
          <transition name="fade">
            <div v-if="analysis.open" class="mt-4 bg-[#232323] rounded p-4 text-gray-300 text-sm">
              <span>Нейросеть находится в разработке. Подробная информация появится позже.</span>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAuthStore } from '@/stores/authStore'

const authStore = useAuthStore()
const user = computed(() => authStore.user)

onMounted(async () => {
  if (!user.value) {
    await authStore.fetchUserData()
  }
})

const analyses = ref([
  {
    name: 'Анализ 1',
    date: '12.03.2024',
    statusColor: 'bg-green-500',
    open: false
  },
  {
    name: 'Анализ 2',
    date: '14.03.2024',
    statusColor: 'bg-blue-500',
    open: false
  },
  {
    name: 'Анализ 3',
    date: '15.03.2024',
    statusColor: 'bg-purple-500',
    open: false
  }
])

function toggleAnalysis(index) {
  analyses.value[index].open = !analyses.value[index].open
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style> 