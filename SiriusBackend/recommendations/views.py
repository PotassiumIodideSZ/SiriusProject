from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Recommendation, InvestmentProfile
from .serializers import RecommendationSerializer, InvestmentProfileSerializer


@extend_schema_view(
    list=extend_schema(summary='List all recommendations', tags=['Recommendations']),
    retrieve=extend_schema(summary='Get recommendation details', tags=['Recommendations']),
    create=extend_schema(summary='Create new recommendation', tags=['Recommendations']),
    update=extend_schema(summary='Update recommendation', tags=['Recommendations']),
    partial_update=extend_schema(summary='Partially update recommendation', tags=['Recommendations']),
    destroy=extend_schema(summary='Delete recommendation', tags=['Recommendations']),
)
class RecommendationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Recommendation model.
    Provides CRUD operations for recommendation management.
    Users can only access their own recommendations.
    """
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter queryset to only return current user's recommendations.
        """
        return Recommendation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set user to current authenticated user.
        """
        serializer.save(user=self.request.user)


class InvestmentProfileView(APIView):
    """
    API view to retrieve the current user's investment profile.
    Returns the latest risk analysis and recommendations.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary='Get user investment profile',
        tags=['Recommendations'],
        responses={
            200: InvestmentProfileSerializer,
            404: {'description': 'No investment profile found'}
        }
    )
    def get(self, request):
        """
        Return the current user's investment profile.
        If no profile exists, returns 404.
        """
        try:
            profile = InvestmentProfile.objects.get(user=request.user)
            serializer = InvestmentProfileSerializer(profile)
            return Response(serializer.data)
        except InvestmentProfile.DoesNotExist:
            return Response(
                {'error': 'Инвестиционный профиль не найден. Пожалуйста, сначала пройдите опрос.'},
                status=status.HTTP_404_NOT_FOUND
            )
