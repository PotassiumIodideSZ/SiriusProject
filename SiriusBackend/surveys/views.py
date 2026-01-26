from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
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


@extend_schema(
    summary='Submit survey answers',
    tags=['Surveys'],
    request={
        'type': 'object',
        'properties': {
            'answers': {
                'type': 'array',
                'items': {'type': 'integer'},
                'description': 'Array of answer values (1-5) for each question'
            }
        }
    },
    responses={
        201: {'description': 'Survey submitted successfully'},
        400: {'description': 'Invalid data'}
    }
)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def submit_survey(request):
    """
    Submit survey answers and create a new questionnaire record.
    """
    answers = request.data.get('answers', [])
    
    if not answers:
        return Response(
            {'error': 'No answers provided'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Validate each answer is between 1 and 5
    for i, answer in enumerate(answers):
        if answer is None or not (1 <= answer <= 5):
            return Response(
                {'error': f'Invalid answer at position {i + 1}: must be between 1 and 5'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    # Create questionnaire with answers
    questionnaire = Questionnaire.objects.create(
        user=request.user,
        questions={'answers': answers}
    )
    
    serializer = QuestionnaireSerializer(questionnaire)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
