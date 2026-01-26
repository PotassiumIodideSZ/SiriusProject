export const resultsRoutes = [
  {
    path: '/results',
    name: 'Results',
    component: () => import('../components/ResultsView.vue'),
    meta: { requiresAuth: true }
  }
]
