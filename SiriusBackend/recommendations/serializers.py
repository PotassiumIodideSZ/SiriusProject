from rest_framework import serializers
from .models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    """
    Serializer for Recommendation model.
    """
    class Meta:
        model = Recommendation
        fields = ['id', 'user', 'recommendation_text', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
