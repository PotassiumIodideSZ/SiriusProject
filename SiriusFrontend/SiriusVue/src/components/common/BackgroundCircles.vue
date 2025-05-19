<template>
  <div class="fixed inset-0 pointer-events-none z-0" style="z-index:0">
    <svg v-for="circle in circles" :key="circle.id"
         :style="{
           position: 'absolute',
           left: circle.left + '%',
           top: circle.top + '%',
           width: size + 'px',
           height: size + 'px',
           opacity: circle.opacity,
           filter: 'blur(' + circle.blur + 'px)',
           zIndex: 0
         }"
         :width="size" :height="size">
      <circle :cx="size/2" :cy="size/2" :r="size/2 - circle.strokeWidth/2" :stroke="circle.color" :stroke-width="circle.strokeWidth" fill="none" />
    </svg>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const circles = ref([])
const size = 100 // размер круга (px)
const count = 12 // количество кругов

function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min
}

function randomFloat(min, max) {
  return Math.random() * (max - min) + min
}

function generateNonOverlappingPositions(count, size) {
  const positions = []
  let attempts = 0
  while (positions.length < count && attempts < 200) {
    const left = randomInt(2, 98)
    const top = randomInt(2, 98)
    // Проверка на пересечение
    let overlaps = false
    for (const pos of positions) {
      const dx = (left - pos.left) * window.innerWidth / 100
      const dy = (top - pos.top) * window.innerHeight / 100
      const dist = Math.sqrt(dx*dx + dy*dy)
      if (dist < size) {
        overlaps = true
        break
      }
    }
    if (!overlaps) {
      positions.push({ left, top })
    }
    attempts++
  }
  return positions
}

onMounted(() => {
  const colors = ['#232323']
  const positions = generateNonOverlappingPositions(count, size)
  const arr = positions.map((pos, i) => ({
    id: i,
    left: pos.left,
    top: pos.top,
    opacity: randomFloat(0.10, 0.16),
    blur: randomInt(0, 2) * 2,
    color: colors[0],
    strokeWidth: randomInt(6, 18)
  }))
  circles.value = arr
})
</script> 