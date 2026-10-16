from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import SurveyQuestion, Questionnaire, QuestionAnswer
from .serializers import (
    SurveyQuestionSerializer,
    QuestionnaireSerializer,
    SurveySubmitSerializer
)
from .risk_calculator import calculate_risk_score
from recommendations.models import InvestmentProfile


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


class SurveyQuestionListView(APIView):
    """
    API view to retrieve all enabled survey questions.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary='Get all enabled survey questions',
        tags=['Surveys'],
        responses={200: SurveyQuestionSerializer(many=True)}
    )
    def get(self, request):
        """
        Return all enabled survey questions ordered by their order field.
        """
        questions = SurveyQuestion.objects.filter(is_enabled=True).order_by('order')
        serializer = SurveyQuestionSerializer(questions, many=True)
        return Response({
            'questions': serializer.data
        })


import threading
import logging

logger = logging.getLogger(__name__)


def _run_async_calculation(questionnaire_id, user_id, answers_data):
    """Background worker function for asynchronous LLM/fallback calculation."""
    from django.contrib.auth import get_user_model
    User = get_user_model()
    try:
        questionnaire = Questionnaire.objects.get(id=questionnaire_id)
        user = User.objects.get(id=user_id)

        risk_profile = calculate_risk_score(answers_data)

        # Update or create investment profile for the user
        InvestmentProfile.objects.update_or_create(
            user=user,
            defaults={
                'risk_score': risk_profile['risk_score'],
                'risk_category': risk_profile['risk_category'],
                'archetype': risk_profile.get('archetype'),
                'radar_scores': risk_profile.get('radar_scores'),
                'behavioral_traps': risk_profile.get('behavioral_traps'),
                'asset_allocation': risk_profile['asset_allocation'],
                'recommendations': risk_profile['recommendations'],
                'key_traits': risk_profile['key_traits']
            }
        )

        questionnaire.status = 'COMPLETED'
        questionnaire.save(update_fields=['status'])
        logger.info(f"Questionnaire {questionnaire_id} processed successfully.")
    except Exception as e:
        logger.exception(f"Error processing questionnaire {questionnaire_id}: {str(e)}")
        try:
            q = Questionnaire.objects.get(id=questionnaire_id)
            q.status = 'FAILED'
            q.error_message = str(e)
            q.save(update_fields=['status', 'error_message'])
        except Exception:
            pass


class SurveySubmitView(APIView):
    """
    API view to submit survey responses.
    Creates questionnaire in PENDING status, queues async calculation,
    and returns questionnaire_id for frontend polling.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary='Submit survey responses',
        tags=['Surveys'],
        request=SurveySubmitSerializer,
        responses={
            201: {'type': 'object', 'properties': {
                'success': {'type': 'boolean'},
                'questionnaire_id': {'type': 'integer'},
                'status': {'type': 'string'},
                'message': {'type': 'string'}
            }}
        }
    )
    def post(self, request):
        """
        Submit survey responses for the current user.
        Creates Questionnaire with QuestionAnswer records, triggers background calculation.
        """
        serializer = SurveySubmitSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        answers_data = serializer.validated_data['answers']
        user = request.user

        # Extract question IDs from the answers
        question_ids = [answer['question_id'] for answer in answers_data]

        # Validate that all question IDs exist and are enabled
        questions = SurveyQuestion.objects.filter(id__in=question_ids, is_enabled=True)
        valid_question_ids = set(questions.values_list('id', flat=True))
        
        invalid_ids = set(question_ids) - valid_question_ids
        if invalid_ids:
            return Response(
                {'error': f'Questions not found or disabled: {sorted(invalid_ids)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a new questionnaire in PENDING status
        questionnaire = Questionnaire.objects.create(user=user, status='PENDING')

        # Create QuestionAnswer records
        answer_objects = [
            QuestionAnswer(
                questionnaire=questionnaire,
                question_id=answer['question_id'],
                answer_value=answer['answer_value']
            )
            for answer in answers_data
        ]
        QuestionAnswer.objects.bulk_create(answer_objects)

        # Start calculation asynchronously in background thread
        thread = threading.Thread(
            target=_run_async_calculation,
            args=(questionnaire.id, user.id, answers_data),
            daemon=True
        )
        thread.start()

        return Response({
            'success': True,
            'questionnaire_id': questionnaire.id,
            'status': 'PENDING',
            'message': 'Анкета принята, расчет профиля запущен',
            'answers_count': len(answers_data)
        }, status=status.HTTP_201_CREATED)


class QuestionnaireStatusView(APIView):
    """
    Polling endpoint to check status of a questionnaire calculation.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary='Check questionnaire calculation status',
        tags=['Surveys'],
        responses={
            200: {'type': 'object', 'properties': {
                'id': {'type': 'integer'},
                'status': {'type': 'string'},
                'error_message': {'type': 'string'},
                'is_completed': {'type': 'boolean'},
                'profile': {'type': 'object'}
            }}
        }
    )
    def get(self, request, pk):
        try:
            questionnaire = Questionnaire.objects.get(id=pk, user=request.user)
        except Questionnaire.DoesNotExist:
            return Response({'error': 'Анкета не найдена'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'id': questionnaire.id,
            'status': questionnaire.status,
            'is_completed': questionnaire.status == 'COMPLETED',
            'error_message': questionnaire.error_message,
        }

        if questionnaire.status == 'COMPLETED':
            try:
                profile = InvestmentProfile.objects.get(user=request.user)
                from recommendations.serializers import InvestmentProfileSerializer
                data['profile'] = InvestmentProfileSerializer(profile).data
            except InvestmentProfile.DoesNotExist:
                pass

        return Response(data)


class SurveyHistoryView(APIView):
    """
    API view to retrieve user's survey history.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary='Get user survey history',
        tags=['Surveys'],
        responses={200: QuestionnaireSerializer(many=True)}
    )
    def get(self, request):
        """
        Return all questionnaires for the current user.
        """
        questionnaires = Questionnaire.objects.filter(user=request.user)
        serializer = QuestionnaireSerializer(questionnaires, many=True)
        return Response({
            'questionnaires': serializer.data
        })
