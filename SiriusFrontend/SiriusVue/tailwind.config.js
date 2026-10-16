/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        serif: ['Newsreader', 'Georgia', 'serif'],
        display: ['Newsreader', 'Georgia', 'serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      colors: {
        paper: {
          50: '#FDFCF9',
          100: '#FAF7F2',
          200: '#F4EFEA',
          300: '#EBE4DC',
          400: '#DFD6C9',
        },
        ink: {
          950: '#111113',
          900: '#1C1917',
          800: '#292524',
          700: '#44403C',
          600: '#57534E',
          500: '#78716C',
          400: '#A8A29E',
          300: '#D6D3D1',
          200: '#E7E5E4',
          100: '#F5F5F4',
        },
        academic: {
          amber: '#B45309',
          'amber-hover': '#92400E',
          'amber-light': '#D97706',
          'amber-bg': '#FEF3C7',
          navy: '#1E3A8A',
          sage: '#15803D',
          crimson: '#B91C1C',
        }
      }
    },
  },
  plugins: [],
}