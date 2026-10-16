<template>
  <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden">
    <!-- Subtle Paper Grid Pattern -->
    <div class="absolute inset-0 paper-grid opacity-60"></div>
    
    <!-- Warm Ambient Light at the top -->
    <div 
      class="absolute -top-40 left-1/2 -translate-x-1/2 w-[900px] h-[500px] rounded-full blur-[160px] opacity-[0.07] pointer-events-none"
      style="background: radial-gradient(circle, #B45309 0%, rgba(180, 83, 9, 0) 70%);"
    ></div>

    <!-- Soft corner vignette -->
    <div 
      class="absolute top-1/2 -right-40 w-[600px] h-[600px] rounded-full blur-[180px] opacity-[0.04] pointer-events-none"
      style="background: radial-gradient(circle, #D97706 0%, rgba(217, 119, 6, 0) 70%);"
    ></div>
  </div>
</template>

<script setup>
// Academic paper ambient background
</script>
