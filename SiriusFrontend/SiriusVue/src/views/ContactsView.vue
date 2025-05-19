<template>
  <div class="max-w-2xl mx-auto py-10 px-2 sm:py-16 sm:px-4 text-center text-white">
    <h1 class="text-2xl sm:text-3xl font-bold text-purple-600 mb-4 sm:mb-6">Контакты</h1>
    <p class="mb-3 sm:mb-4">Свяжитесь с нами по любым вопросам или предложениям!</p>
    <div class="mb-4 sm:mb-6">
      <div class="mb-2"><b>Email:</b> <a href="mailto:support@invest.ru" class="text-purple-500 hover:underline">support@invest.ru</a></div>
      <div class="mb-2"><b>Телефон:</b> <a href="tel:+78001234567" class="text-purple-500 hover:underline">+7 (800) 123-45-67</a></div>
      <div><b>Адрес:</b>г. Челябинск, проспект Ленина, д. 76 </div>
    </div>
    <form class="bg-gray-900 rounded-lg p-4 sm:p-6 shadow-md mx-auto max-w-md">
      <div class="mb-3 sm:mb-4">
        <input type="text" placeholder="Ваше имя" class="w-full px-3 py-2 rounded border border-gray-700 bg-gray-800 text-white focus:outline-none focus:border-purple-500 text-sm sm:text-base" />
      </div>
      <div class="mb-3 sm:mb-4">
        <input type="email" placeholder="Ваш email" class="w-full px-3 py-2 rounded border border-gray-700 bg-gray-800 text-white focus:outline-none focus:border-purple-500 text-sm sm:text-base" />
      </div>
      <div class="mb-3 sm:mb-4">
        <textarea placeholder="Ваше сообщение" rows="4" class="w-full px-3 py-2 rounded border border-gray-700 bg-gray-800 text-white focus:outline-none focus:border-purple-500 text-sm sm:text-base"></textarea>
      </div>
      <button type="submit" class="bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 sm:py-2 sm:px-6 rounded transition text-sm sm:text-base">Отправить</button>
    </form>
    <div class="mt-6 sm:mt-8 flex justify-center gap-4 sm:gap-6">
      <a href="#" class="text-purple-400 hover:text-purple-600 text-xl sm:text-2xl"><i class="fab fa-vk"></i></a>
      <a href="#" class="text-purple-400 hover:text-purple-600 text-xl sm:text-2xl"><i class="fab fa-telegram"></i></a>
    </div>
  </div>
</template>

<script setup>
// Форма обратной связи не отправляет данные, только UI
</script> 