<template>
  <div class="min-h-screen text-white flex flex-col justify-center gap-10 sm:gap-16">
    <!-- ВЕРХНИЙ БЛОК -->
    <section class="flex flex-col md:flex-row items-center justify-between container mx-auto max-w-[1100px] py-6 sm:py-12 gap-6 sm:gap-8 px-2 sm:px-0">
      <!-- Текст слева (70%) -->
      <div class="w-full md:w-[70%] space-y-4 sm:space-y-6">
        <h1 class="text-2xl sm:text-4xl md:text-5xl font-bold leading-tight">
          Наша нейросеть<br />
          проведет вас в новый<br />
          мир возможностей!
        </h1>
        <p class="text-sm sm:text-md text-gray-300 italic">
          Не упустите возможность сделать первый шаг к успешным инвестициям!
        </p>
      </div>
      <!-- Картинка справа (30%) -->
      <div class="w-full md:w-[30%] flex justify-center items-center">
        <img 
          src="/Main1Section.jpg.svg" 
          alt="Инвестиционный график" 
          class="w-40 sm:w-full max-w-[200px] sm:max-w-[300px] h-auto"
        />
      </div>
    </section>

    <!-- НИЖНИЙ БЛОК -->
    <section class="flex flex-col md:flex-row items-start justify-between container mx-auto max-w-[1100px] py-4 sm:py-8 gap-6 sm:gap-8 px-2 sm:px-0">
      <!-- Левая часть: текст и кнопка -->
      <div class="flex-1 flex flex-col items-center justify-center gap-2 sm:gap-4 mx-auto">
        <div class="bg-[#232323] bg-opacity-90 rounded-lg p-4 sm:p-6 py-4 sm:py-5 max-w-xl my-2 sm:my-4">
          <p class="text-gray-200 text-sm sm:text-base">
            Вы сможете пройти тест, который поможет определить, какая инвестиционная стратегия подходит именно вам. Независимо от вашего опыта или знаний в области инвестиций, наш тест предоставит вам персонализированные рекомендации, чтобы вы могли уверенно двигаться к своим финансовым целям.
          </p>
        </div>
        <div class="flex justify-center mb-8 sm:mb-12">
          <button class="bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 sm:py-3 px-6 sm:px-10 rounded-lg text-base sm:text-lg transition" @click="handleStart">
            Начать
          </button>
        </div>
      </div>
      <!-- Правая часть: текст над картинкой и картинка -->
      <div class="flex-1 flex flex-col items-center justify-center gap-2 sm:gap-4 mx-auto">
        <div class="text-purple-400 font-bold text-base sm:text-lg mb-1 sm:mb-2 text-center">Готовы начать свой инвестиционный путь?</div>
        <img
          src="/Main2Section.jpg" 
          alt="Инвестиции"
          class="rounded-lg w-48 sm:w-80 border border-purple-700 shadow-lg"
        />
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const router = useRouter()
const authStore = useAuthStore()

const handleStart = () => {
  if (authStore.isAuthenticated) {
    router.push('/survey')
  } else {
    // Открываем модальное окно логина
    authStore.showLoginModal = true
  }
}
</script>