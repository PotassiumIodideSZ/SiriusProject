from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecommendationViewSet, InvestmentProfileView

router = DefaultRouter()
router.register(r'recommendations', RecommendationViewSet, basename='recommendation')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', InvestmentProfileView.as_view(), name='investment-profile'),
]
