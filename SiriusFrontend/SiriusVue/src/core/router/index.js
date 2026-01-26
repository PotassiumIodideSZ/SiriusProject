import { createRouter, createWebHistory } from 'vue-router'
import { surveyRoutes } from '@/features/survey/routes'
import { profileRoutes } from '@/features/profile/routes'
import { resultsRoutes } from '@/features/results/routes'

// Static routes
const staticRoutes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomeView.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/AboutView.vue')
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: () => import('@/views/ContactsView.vue')
  }
]

// Feature routes (будут добавлены позже)
// import { authRoutes } from '@/features/auth/routes'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    ...staticRoutes,
    // ...authRoutes,
    ...surveyRoutes,
    ...profileRoutes,
    ...resultsRoutes
  ]
})

// Navigation guards
router.beforeEach(async (to, from, next) => {
  const isAuthenticated = localStorage.getItem('token')
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Home', query: { redirect: to.fullPath } })
  } else {
    next()
  }
})

export default router
