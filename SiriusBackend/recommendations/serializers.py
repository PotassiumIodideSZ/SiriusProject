from rest_framework import serializers
from .models import Recommendation, InvestmentProfile


class RecommendationSerializer(serializers.ModelSerializer):
    """
    Serializer for Recommendation model.
    """
    class Meta:
        model = Recommendation
        fields = ['id', 'user', 'recommendation_text', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class InvestmentProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for InvestmentProfile model.
    Returns the complete investment profile with cognitive radar and archetype.
    """
    class Meta:
        model = InvestmentProfile
        fields = [
            'id',
            'user',
            'risk_score',
            'risk_category',
            'archetype',
            'radar_scores',
            'behavioral_traps',
            'asset_allocation',
            'recommendations',
            'key_traits',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
