export const profileRoutes = [
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../components/ProfileView.vue'),
    meta: { requiresAuth: true }
  }
]
