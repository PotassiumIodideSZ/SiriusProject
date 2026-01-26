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


class SurveySubmitView(APIView):
    """
    API view to submit survey responses.
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
                'message': {'type': 'string'},
                'risk_profile': {'type': 'object'}
            }}
        }
    )
    def post(self, request):
        """
        Submit survey responses for the current user.
        Creates a Questionnaire with QuestionAnswer records and calculates risk profile.
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
            # Provide more detailed error information
            disabled_questions = SurveyQuestion.objects.filter(id__in=question_ids, is_enabled=False)
            disabled_ids = set(disabled_questions.values_list('id', flat=True))
            missing_ids = invalid_ids - disabled_ids
            
            error_parts = []
            if missing_ids:
                error_parts.append(f'not found: {sorted(missing_ids)}')
            if disabled_ids:
                error_parts.append(f'disabled: {sorted(disabled_ids)}')
            
            return Response(
                {'error': f'Questions with ids {"; ".join(error_parts)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a new questionnaire
        questionnaire = Questionnaire.objects.create(user=user)

        # Create QuestionAnswer records
        answer_objects = []
        for answer_data in answers_data:
            question_id = answer_data['question_id']
            answer_value = answer_data['answer_value']
            
            answer_objects.append(
                QuestionAnswer(
                    questionnaire=questionnaire,
                    question_id=question_id,
                    answer_value=answer_value
                )
            )
        
        # Bulk create all answers
        QuestionAnswer.objects.bulk_create(answer_objects)

        # Calculate risk profile using the risk calculator
        risk_profile = calculate_risk_score(answers_data)

        # Update or create investment profile for the user
        # This ensures only the latest result is stored per user
        investment_profile, created = InvestmentProfile.objects.update_or_create(
            user=user,
            defaults={
                'risk_score': risk_profile['risk_score'],
                'risk_category': risk_profile['risk_category'],
                'asset_allocation': risk_profile['asset_allocation'],
                'recommendations': risk_profile['recommendations'],
                'key_traits': risk_profile['key_traits']
            }
        )

        return Response({
            'success': True,
            'questionnaire_id': questionnaire.id,
            'message': 'Survey submitted successfully',
            'answers_count': len(answers_data),
            'risk_profile': risk_profile
        }, status=status.HTTP_201_CREATED)


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
