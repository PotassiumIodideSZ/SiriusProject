from rest_framework import serializers
from .models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    """
    Serializer for Questionnaire model.
    """
    class Meta:
        model = Questionnaire
        fields = ['id', 'user', 'question1', 'question2', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
