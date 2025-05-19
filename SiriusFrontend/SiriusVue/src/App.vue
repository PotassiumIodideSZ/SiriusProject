<template>
  <div class="min-h-screen bg-[#0F0F0F] flex flex-col relative overflow-hidden">
    <TheHeader class="relative z-10" />
    <main class="flex-1 relative z-10">
      <router-view />
    </main>
    <TheFooter class="relative z-10" />
    <BackgroundCircles />
  </div>
</template>

<script setup>
import TheHeader from './components/layout/TheHeader.vue'
import TheFooter from './components/layout/TheFooter.vue'
import BackgroundCircles from './components/common/BackgroundCircles.vue'
</script>