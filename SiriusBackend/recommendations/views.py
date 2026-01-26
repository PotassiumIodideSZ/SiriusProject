from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Recommendation
from .serializers import RecommendationSerializer


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
