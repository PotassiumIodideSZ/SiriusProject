<template>
  <footer class="w-full border-t border-ink-200 bg-paper-200/60 py-8 mt-16 text-ink-600 text-xs font-mono">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-4">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <img src="/logo.png" alt="Psy Otkliq" class="w-7 h-7 object-contain" />
          <span class="text-ink-900 font-semibold font-serif text-sm">Psy Otkliq</span>
          <span class="text-ink-300">|</span>
          <span class="text-ink-600">Когнитивное моделирование инвестиционного риск-профиля</span>
        </div>

        <!-- Navigation Links in Footer -->
        <nav class="flex items-center gap-4 text-xs font-mono text-ink-600">
          <router-link to="/" class="hover:text-ink-950 transition-colors">Главная</router-link>
          <span class="text-ink-300">·</span>
          <router-link to="/about" class="hover:text-ink-950 transition-colors">О проекте</router-link>
          <span class="text-ink-300">·</span>
          <router-link to="/contacts" class="hover:text-ink-950 transition-colors">Методология</router-link>
          <span class="text-ink-300">·</span>
          <router-link to="/survey" class="text-academic-amber hover:underline font-semibold">Пройти тест (12 дилемм)</router-link>
        </nav>
      </div>

      <div class="flex flex-col sm:flex-row items-center justify-between gap-2 pt-4 border-t border-ink-200/60 text-[11px] text-ink-500">
        <div>
          Исследовательская платформа поведенческой экономики и LLM-скоринга
        </div>
        <div class="text-center sm:text-right">
          © 2026 Psy Otkliq · 12 ситуационных дилемм и 4D когнитивная радар-карта
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
// Academic clean footer
</script>
