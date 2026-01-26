export const surveyRoutes = [
  {
    path: '/survey',
    name: 'Survey',
    component: () => import('../components/SurveyView.vue'),
    meta: { requiresAuth: true }
  }
]
