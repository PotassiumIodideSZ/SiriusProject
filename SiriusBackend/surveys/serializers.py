from rest_framework import serializers
from .models import SurveyQuestion, Questionnaire, QuestionAnswer


class SurveyQuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for SurveyQuestion model.
    """
    class Meta:
        model = SurveyQuestion
        fields = ['id', 'text', 'order', 'is_enabled', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class QuestionAnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for QuestionAnswer model.
    """
    question_text = serializers.CharField(source='question.text', read_only=True)
    question_order = serializers.IntegerField(source='question.order', read_only=True)

    class Meta:
        model = QuestionAnswer
        fields = ['id', 'question', 'question_text', 'question_order', 'answer_value', 'created_at']
        read_only_fields = ['id', 'created_at']


class QuestionnaireSerializer(serializers.ModelSerializer):
    """
    Serializer for Questionnaire model.
    """
    answers_count = serializers.ReadOnlyField()
    answers = QuestionAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Questionnaire
        fields = ['id', 'user', 'completed_at', 'answers_count', 'answers']
        read_only_fields = ['id', 'user', 'completed_at']


class QuestionAnswerCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a single question answer.
    """
    class Meta:
        model = QuestionAnswer
        fields = ['question', 'answer_value']

    def validate_answer_value(self, value):
        """Validate that answer_value is between 1 and 5."""
        if not isinstance(value, int) or value < 1 or value > 5:
            raise serializers.ValidationError(
                "Answer value must be an integer between 1 and 5"
            )
        return value


class SurveySubmitSerializer(serializers.Serializer):
    """
    Serializer for submitting survey responses.
    Expects answers as a list of objects with question_id and answer_value.
    """
    answers = serializers.ListField(
        child=serializers.DictField(),
        help_text="List of answer objects: [{'question_id': 1, 'answer_value': 5}, ...]"
    )

    def validate_answers(self, value):
        """Validate that answers is a valid list with correct structure."""
        if not isinstance(value, list):
            raise serializers.ValidationError("Answers must be a list")
        
        if len(value) == 0:
            raise serializers.ValidationError("At least one answer is required")
        
        # Check for duplicate question IDs
        question_ids = []
        for answer in value:
            if not isinstance(answer, dict):
                raise serializers.ValidationError("Each answer must be an object")
            
            if 'question_id' not in answer or 'answer_value' not in answer:
                raise serializers.ValidationError(
                    "Each answer must contain 'question_id' and 'answer_value'"
                )
            
            question_id = answer['question_id']
            if not isinstance(question_id, int):
                raise serializers.ValidationError("question_id must be an integer")
            
            if question_id in question_ids:
                raise serializers.ValidationError(
                    f"Duplicate question_id: {question_id}"
                )
            question_ids.append(question_id)
        
        return value
