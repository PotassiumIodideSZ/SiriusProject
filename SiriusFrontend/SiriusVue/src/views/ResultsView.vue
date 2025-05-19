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
      <div class="flex" style="align-items: flex-start;">
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
              <span class="text-4xl font-bold text-white">{{ percentage }}%</span>
            </div>
            <div class="text-gray-400 text-center mt-4">Готовность к риску</div>
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
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Процент готовности к риску (в реальном приложении будет получен из API или пропсов)
const percentage = ref(72)

// Рекомендации (в реальном приложении будут получены из API)
const recommendations = ref([
  'Нейросеть находится в разработке. Подробная информация появится позже.',
])

// Расчеты для кругового прогресса
const circumference = computed(() => 2 * Math.PI * 92)
const dashOffset = computed(() => 
  circumference.value - (percentage.value / 100) * circumference.value
)
</script>

<style scoped>
/* Добавьте дополнительные стили, если необходимо */
circle {
  transition: stroke-dashoffset 1s ease-in-out;
}
</style> 