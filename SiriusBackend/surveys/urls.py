from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionnaireViewSet, submit_survey

router = DefaultRouter()
router.register(r'questionnaires', QuestionnaireViewSet, basename='questionnaire')

urlpatterns = [
    path('', include(router.urls)),
    path('submit/', submit_survey, name='submit-survey'),
]
