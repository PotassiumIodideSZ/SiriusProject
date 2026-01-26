from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Questionnaire
from .serializers import QuestionnaireSerializer


@extend_schema_view(
    list=extend_schema(summary='List all questionnaires', tags=['Surveys']),
    retrieve=extend_schema(summary='Get questionnaire details', tags=['Surveys']),
    create=extend_schema(summary='Create new questionnaire', tags=['Surveys']),
    update=extend_schema(summary='Update questionnaire', tags=['Surveys']),
    partial_update=extend_schema(summary='Partially update questionnaire', tags=['Surveys']),
    destroy=extend_schema(summary='Delete questionnaire', tags=['Surveys']),
)
class QuestionnaireViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Questionnaire model.
    Provides CRUD operations for questionnaire management.
    Users can only access their own questionnaires.
    """
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter queryset to only return the current user's questionnaires.
        """
        return Questionnaire.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the user to the current authenticated user.
        """
        serializer.save(user=self.request.user)
