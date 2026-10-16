<template>
  <div class="relative w-full space-y-4">
    <!-- Header: Title + Point Filters -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-2 border-b border-ink-100">
      <div>
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-academic-amber"></span>
          <span class="font-serif font-bold text-base text-ink-950">
            Индекс S&P 500 (Кризис 2007–2010 гг.) — Свечной анализ поведения
          </span>
        </div>
        <p class="text-xs text-ink-500 font-mono mt-0.5">
          Реальные помесячные свечи (OHLC) · Выберите точку на графике или фазу снизу
        </p>
      </div>

      <!-- Marker Toggles -->
      <div class="flex flex-wrap items-center gap-2 text-xs font-mono">
        <button
          @click="toggleCrowd"
          class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border transition-all cursor-pointer"
          :class="showCrowd 
            ? 'bg-rose-50 border-rose-300 text-rose-800 shadow-sm font-semibold' 
            : 'bg-white border-ink-200 text-ink-400 hover:text-ink-700'"
        >
          <span class="w-2 h-2 rounded-full" :class="showCrowd ? 'bg-rose-600' : 'bg-ink-300'"></span>
          <span>Ошибки толпы (красные точки)</span>
        </button>

        <button
          @click="toggleRational"
          class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border transition-all cursor-pointer"
          :class="showRational 
            ? 'bg-emerald-50 border-emerald-300 text-emerald-800 shadow-sm font-semibold' 
            : 'bg-white border-ink-200 text-ink-400 hover:text-ink-700'"
        >
          <span class="w-2 h-2 rounded-full" :class="showRational ? 'bg-emerald-600' : 'bg-ink-300'"></span>
          <span>Входы инвестора (зеленые точки)</span>
        </button>
      </div>
    </div>

    <!-- Chart Container (Clean, no floating overlays covering data) -->
    <div class="relative w-full rounded-2xl border border-ink-200 bg-white p-2 sm:p-4 shadow-sm">
      <!-- ECharts Canvas Container -->
      <div ref="chartDom" class="w-full h-[360px] sm:h-[400px]"></div>

      <!-- Bottom Legend -->
      <div class="flex flex-wrap items-center justify-between gap-3 pt-3 border-t border-ink-100 text-[11px] font-mono text-ink-500">
        <div class="flex items-center gap-4">
          <span class="flex items-center gap-1.5">
            <span class="w-3 h-3 rounded-sm bg-emerald-500 inline-block"></span>
            <span class="text-ink-700">Рост месяца (Бычья свеча)</span>
          </span>
          <span class="flex items-center gap-1.5">
            <span class="w-3 h-3 rounded-sm bg-rose-500 inline-block"></span>
            <span class="text-ink-700">Падение месяца (Медвежья свеча)</span>
          </span>
        </div>
        <div class="flex items-center gap-4">
          <span class="text-rose-700 font-medium flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-600 inline-block"></span>
            Красные точки: ошибки толпы
          </span>
          <span class="text-emerald-700 font-medium flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-600 inline-block"></span>
            Зеленые точки: выверенные входы
          </span>
        </div>
      </div>
    </div>

    <!-- Phase Selector Button Tabs (Synced with the active point) -->
    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2.5 pt-1">
      <button 
        v-for="(phase, index) in phases" 
        :key="index"
        @click="selectPhase(index)"
        class="p-3 rounded-xl text-left border transition-all text-xs cursor-pointer"
        :class="activePhase === index 
          ? 'bg-amber-50/90 border-academic-amber text-ink-950 shadow-sm ring-1 ring-academic-amber/40' 
          : 'bg-white border-ink-200 text-ink-600 hover:text-ink-950 hover:border-ink-300 hover:bg-paper-50'"
      >
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-mono font-bold" :class="activePhase === index ? 'text-academic-amber' : 'text-ink-400'">
            0{{ index + 1 }} · {{ phase.dateLabel }}
          </span>
          <span 
            class="text-[9px] font-mono px-1 rounded font-semibold"
            :class="phase.type === 'crowd' ? 'bg-rose-100 text-rose-800' : 'bg-emerald-100 text-emerald-800'"
          >
            {{ phase.type === 'crowd' ? 'Толпа' : 'Инвестор' }}
          </span>
        </div>
        <div class="font-serif font-bold mt-1 text-xs sm:text-sm text-ink-900 leading-snug">
          {{ phase.shortTitle }}
        </div>
        <div class="text-[11px] font-mono text-ink-500 mt-0.5 truncate">
          {{ phase.priceLabel }}
        </div>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  phases: {
    type: Array,
    required: true
  },
  activePhase: {
    type: Number,
    default: 0
  }
})

const emit = defineEmits(['select-phase'])

const chartDom = ref(null)
let chartInstance = null

const showCrowd = ref(true)
const showRational = ref(true)

const toggleCrowd = () => {
  showCrowd.value = !showCrowd.value
  renderChart()
}

const toggleRational = () => {
  showRational.value = !showRational.value
  renderChart()
}

// Real Monthly S&P 500 Historical Data (2007 - 2010)
// Format: [Open, Close, Lowest, Highest]
const dates = [
  'Июн 07', 'Июл 07', 'Авг 07', 'Сен 07', 'Окт 07', 'Ноя 07', 'Дек 07',
  'Янв 08', 'Фев 08', 'Мар 08', 'Апр 08', 'Май 08', 'Июн 08', 'Июл 08', 'Авг 08', 'Сен 08', 'Окт 08', 'Ноя 08', 'Дек 08',
  'Янв 09', 'Фев 09', 'Мар 09', 'Апр 09', 'Май 09', 'Июн 09', 'Июл 09', 'Авг 09', 'Сен 09', 'Окт 09', 'Ноя 09', 'Дек 09',
  'Янв 10', 'Фев 10', 'Мар 10', 'Апр 10'
]

const candleData = [
  // 2007
  [1530.6, 1503.4, 1487.1, 1540.5], // Июн 07
  [1503.4, 1455.3, 1431.1, 1555.9], // Июл 07
  [1455.3, 1474.0, 1370.6, 1502.1], // Авг 07
  [1474.0, 1526.8, 1452.8, 1531.8], // Сен 07
  [1526.8, 1549.4, 1494.2, 1576.1], // Окт 07 (index 4 - PEAK)
  [1549.4, 1481.1, 1406.1, 1553.1], // Ноя 07
  [1481.1, 1468.4, 1452.9, 1523.6], // Дек 07 (index 6 - HEDGE)

  // 2008
  [1468.4, 1378.6, 1270.0, 1471.8], // Янв 08
  [1378.6, 1330.6, 1313.2, 1396.1], // Фев 08
  [1330.6, 1322.7, 1256.9, 1360.0], // Мар 08 (Bear Stearns)
  [1322.7, 1385.6, 1322.7, 1404.9], // Апр 08
  [1385.6, 1400.4, 1377.7, 1440.2], // Май 08 (index 11 - TRAP)
  [1400.4, 1280.0, 1272.2, 1404.2], // Июн 08
  [1280.0, 1267.4, 1200.4, 1291.6], // Июл 08
  [1267.4, 1282.8, 1261.4, 1313.1], // Авг 08
  [1282.8, 1166.4, 1106.4, 1303.0], // Сен 08 (Lehman)
  [1166.4, 968.8, 839.8, 1166.4],  // Окт 08
  [968.8, 896.2, 741.0, 1005.6],   // Ноя 08 (index 17 - PANIC)
  [896.2, 903.3, 805.8, 918.7],    // Дек 08

  // 2009
  [903.3, 825.9, 805.2, 943.8],    // Янв 09
  [825.9, 735.1, 735.1, 868.5],    // Фев 09
  [735.1, 797.9, 666.8, 832.9],    // Мар 09 (index 21 - DEVIL BOTTOM 666)
  [797.9, 872.8, 783.3, 888.7],    // Апр 09
  [872.8, 919.1, 872.8, 930.2],    // Май 09
  [919.1, 919.3, 888.1, 956.2],    // Июн 09
  [919.3, 987.5, 869.3, 996.2],    // Июл 09
  [987.5, 1020.6, 979.7, 1039.1],  // Авг 09
  [1020.6, 1057.1, 994.4, 1071.7], // Сен 09
  [1057.1, 1036.2, 1019.9, 1101.4],// Окт 09 (index 28 - REBOUND / SKEPTICISM)
  [1036.2, 1095.6, 1029.4, 1113.7],// Ноя 09
  [1095.6, 1115.1, 1085.9, 1130.4],// Дек 09

  // 2010
  [1115.1, 1073.9, 1071.6, 1150.5],// Янв 10
  [1073.9, 1104.5, 1044.5, 1112.4],// Фев 10
  [1104.5, 1169.4, 1115.8, 1180.7],// Мар 10
  [1169.4, 1186.7, 1170.7, 1219.8] // Апр 10
]

// Map phase indexes to dates
const phaseDateMap = [
  'Окт 07', // Phase 0: Окт 2007 (Peak)
  'Май 08', // Phase 1: Май 2008 (Bull trap)
  'Ноя 08', // Phase 2: Ноя 2008 (Panic)
  'Мар 09', // Phase 3: Мар 2009 (Capitulation / Rebound)
  'Окт 09'  // Phase 4: Окт 2009 (Rebound skepticism)
]

// Pure clean dots on the candles:
// - Red circle points for crowd errors
// - Green circle points for rational moves
const buildMarkPoints = () => {
  const points = []

  // 1. CROWD MISTAKES (Clean Red Dots)
  if (showCrowd.value) {
    points.push(
      {
        name: 'Пик FOMO',
        phaseIndex: 0,
        coord: ['Окт 07', 1576.1],
        symbol: 'circle',
        symbolSize: props.activePhase === 0 ? 18 : 12,
        itemStyle: {
          color: '#e11d48', // rose-600
          borderColor: '#ffffff',
          borderWidth: 2,
          shadowBlur: props.activePhase === 0 ? 10 : 3,
          shadowColor: 'rgba(225, 29, 72, 0.5)'
        },
        label: { show: false }
      },
      {
        name: 'Бычья ловушка',
        phaseIndex: 1,
        coord: ['Май 08', 1440.2],
        symbol: 'circle',
        symbolSize: props.activePhase === 1 ? 18 : 12,
        itemStyle: {
          color: '#e11d48',
          borderColor: '#ffffff',
          borderWidth: 2,
          shadowBlur: props.activePhase === 1 ? 10 : 3,
          shadowColor: 'rgba(225, 29, 72, 0.5)'
        },
        label: { show: false }
      },
      {
        name: 'Паника Lehman',
        phaseIndex: 2,
        coord: ['Ноя 08', 741.0],
        symbol: 'circle',
        symbolSize: props.activePhase === 2 ? 18 : 12,
        itemStyle: {
          color: '#e11d48',
          borderColor: '#ffffff',
          borderWidth: 2,
          shadowBlur: props.activePhase === 2 ? 10 : 3,
          shadowColor: 'rgba(225, 29, 72, 0.5)'
        },
        label: { show: false }
      },
      {
        name: 'Капитуляция на дне',
        phaseIndex: 3,
        coord: ['Мар 09', 666.8],
        symbol: 'circle',
        symbolSize: props.activePhase === 3 ? 18 : 12,
        itemStyle: {
          color: '#e11d48',
          borderColor: '#ffffff',
          borderWidth: 2,
          shadowBlur: props.activePhase === 3 ? 10 : 3,
          shadowColor: 'rgba(225, 29, 72, 0.5)'
        },
        label: { show: false }
      },
      {
        name: 'Неверие в тренд',
        phaseIndex: 4,
        coord: ['Окт 09', 1101.4],
        symbol: 'circle',
        symbolSize: props.activePhase === 4 ? 18 : 12,
        itemStyle: {
          color: '#e11d48',
          borderColor: '#ffffff',
          borderWidth: 2,
          shadowBlur: props.activePhase === 4 ? 10 : 3,
          shadowColor: 'rgba(225, 29, 72, 0.5)'
        },
        label: { show: false }
      }
    )
  }

  // 2. RATIONAL MOVES (Clean Green Dots)
  if (showRational.value) {
    points.push(
      {
        name: 'Хедж инвестора',
        phaseIndex: 1, // Bound to Phase 1 (Ложный отскок / защита)
        coord: ['Дек 07', 1523.6],
        symbol: 'circle',
        symbolSize: props.activePhase === 1 ? 18 : 12,
        itemStyle: {
          color: '#059669', // emerald-600
          borderColor: '#ffffff',
          borderWidth: 2,
          shadowBlur: props.activePhase === 1 ? 10 : 3,
          shadowColor: 'rgba(5, 150, 105, 0.5)'
        },
        label: { show: false }
      },
      {
        name: 'Выкуп дна инвестором',
        phaseIndex: 3,
        coord: ['Мар 09', 797.9],
        symbol: 'circle',
        symbolSize: props.activePhase === 3 ? 18 : 12,
        itemStyle: {
          color: '#059669',
          borderColor: '#ffffff',
          borderWidth: 2,
          shadowBlur: props.activePhase === 3 ? 10 : 3,
          shadowColor: 'rgba(5, 150, 105, 0.5)'
        },
        label: { show: false }
      },
      {
        name: 'Вход по тренду',
        phaseIndex: 4,
        coord: ['Окт 09', 1036.2],
        symbol: 'circle',
        symbolSize: props.activePhase === 4 ? 18 : 12,
        itemStyle: {
          color: '#059669',
          borderColor: '#ffffff',
          borderWidth: 2,
          shadowBlur: props.activePhase === 4 ? 10 : 3,
          shadowColor: 'rgba(5, 150, 105, 0.5)'
        },
        label: { show: false }
      }
    )
  }

  return points
}

const renderChart = () => {
  if (!chartInstance) return

  const option = {
    animation: true,
    backgroundColor: '#ffffff',
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        lineStyle: {
          color: '#94a3b8',
          type: 'dashed'
        }
      },
      backgroundColor: 'rgba(255, 255, 255, 0.96)',
      borderColor: '#e2e8f0',
      borderWidth: 1,
      padding: [8, 12],
      textStyle: {
        color: '#0f172a',
        fontFamily: 'JetBrains Mono, monospace',
        fontSize: 11
      },
      formatter: function (params) {
        const item = params[0]
        if (!item) return ''
        const date = item.name
        const values = item.data // [open, close, lowest, highest]
        const open = values[1]
        const close = values[2]
        const lowest = values[3]
        const highest = values[4]
        const diff = (close - open).toFixed(1)
        const pct = (((close - open) / open) * 100).toFixed(2)
        const isUp = close >= open

        return `
          <div style="font-weight: bold; margin-bottom: 4px; border-bottom: 1px solid #e2e8f0; padding-bottom: 3px;">
            S&P 500 · ${date}
          </div>
          <div>Открытие: <span style="font-family: monospace; font-weight: bold;">${open}</span></div>
          <div>Закрытие: <span style="font-family: monospace; font-weight: bold; color: ${isUp ? '#10b981' : '#ef4444'};">${close}</span> (${diff > 0 ? '+' : ''}${diff} / ${pct}%)</div>
          <div>Минимум: <span style="font-family: monospace;">${lowest}</span></div>
          <div>Максимум: <span style="font-family: monospace;">${highest}</span></div>
        `
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '8%',
      top: '8%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: dates,
      scale: true,
      boundaryGap: true,
      axisLine: { lineStyle: { color: '#cbd5e1' } },
      axisLabel: {
        color: '#64748b',
        fontSize: 10,
        fontFamily: 'JetBrains Mono, monospace'
      },
      splitLine: {
        show: true,
        lineStyle: { color: '#f8fafc' }
      }
    },
    yAxis: {
      scale: true,
      position: 'right',
      axisLine: { lineStyle: { color: '#cbd5e1' } },
      axisLabel: {
        color: '#64748b',
        fontSize: 10,
        fontFamily: 'JetBrains Mono, monospace',
        formatter: '{value} п.'
      },
      splitLine: {
        show: true,
        lineStyle: { color: '#f1f5f9' }
      }
    },
    series: [
      {
        name: 'S&P 500 OHLC',
        type: 'candlestick',
        data: candleData,
        itemStyle: {
          color: '#10b981',        // Green for bullish candle
          color0: '#ef4444',       // Red for bearish candle
          borderColor: '#10b981',
          borderColor0: '#ef4444'
        },
        markPoint: {
          data: buildMarkPoints()
        },
        markLine: {
          symbol: ['none', 'none'],
          silent: true,
          data: [
            {
              yAxis: 1550,
              lineStyle: { color: '#f43f5e', type: 'dashed', width: 1 },
              label: { position: 'start', formatter: 'Пик 2007 (1550 п.)', color: '#e11d48', fontSize: 10 }
            },
            {
              yAxis: 676,
              lineStyle: { color: '#0284c7', type: 'dashed', width: 1 },
              label: { position: 'start', formatter: 'Дно 2009 (666 п.)', color: '#0284c7', fontSize: 10 }
            }
          ]
        }
      }
    ]
  }

  chartInstance.setOption(option, true)
}

const selectPhase = (index) => {
  emit('select-phase', index)
  
  if (!chartInstance) return
  renderChart()

  const targetDate = phaseDateMap[index]
  if (targetDate) {
    chartInstance.dispatchAction({
      type: 'showTip',
      seriesIndex: 0,
      name: targetDate
    })
  }
}

let resizeHandler = null

onMounted(() => {
  if (chartDom.value) {
    chartInstance = echarts.init(chartDom.value)
    renderChart()

    // Clicking a point on the chart also activates that phase
    chartInstance.on('click', function (params) {
      if (params.componentType === 'markPoint' && params.data.phaseIndex !== undefined) {
        selectPhase(params.data.phaseIndex)
      } else if (params.name) {
        const foundIndex = phaseDateMap.indexOf(params.name)
        if (foundIndex !== -1) {
          selectPhase(foundIndex)
        }
      }
    })

    resizeHandler = () => {
      if (chartInstance) {
        chartInstance.resize()
      }
    }
    window.addEventListener('resize', resizeHandler)
  }
})

onBeforeUnmount(() => {
  if (resizeHandler) {
    window.removeEventListener('resize', resizeHandler)
  }
  if (chartInstance) {
    chartInstance.dispose()
    chartInstance = null
  }
})

watch(() => props.activePhase, (newIndex) => {
  selectPhase(newIndex)
})
</script>
