from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    QuestionnaireViewSet,
    SurveyQuestionListView,
    SurveySubmitView,
    SurveyHistoryView
)

router = DefaultRouter()
router.register(r'questionnaires', QuestionnaireViewSet, basename='questionnaire')

urlpatterns = [
    path('questions/', SurveyQuestionListView.as_view(), name='survey-questions'),
    path('submit/', SurveySubmitView.as_view(), name='survey-submit'),
    path('history/', SurveyHistoryView.as_view(), name='survey-history'),
    path('', include(router.urls)),
]
