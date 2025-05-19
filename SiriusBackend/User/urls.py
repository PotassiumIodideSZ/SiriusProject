from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, QuestionnaireViewSet, RecommendationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'questionnaires', QuestionnaireViewSet)
router.register(r'recommendations', RecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]