from django.db import models
from authentication.models import User


class Recommendation(models.Model):
    """
    Recommendation model for storing user recommendations.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recommendations',
        verbose_name='User'
    )
    recommendation_text = models.TextField(verbose_name='Recommendation text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'
        ordering = ['-created_at']

    def __str__(self):
        return f'Recommendation {self.id} - {self.user.username}'


class InvestmentProfile(models.Model):
    """
    Stores the latest investment profile for each user.
    Contains risk score, category, asset allocation, and recommendations.
    This model is designed to store only the latest result per user.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='investment_profile',
        verbose_name='User'
    )
    risk_score = models.IntegerField(
        verbose_name='Risk score (0-100)',
        help_text='Calculated risk tolerance score from questionnaire'
    )
    risk_category = models.CharField(
        max_length=20,
        choices=[
            ('Conservative', 'Conservative (0-30%)'),
            ('Moderate', 'Moderate (31-60%)'),
            ('Growth', 'Growth (61-80%)'),
            ('Aggressive', 'Aggressive (81-100%)')
        ],
        verbose_name='Risk category'
    )
    archetype = models.JSONField(
        verbose_name='Investor Archetype',
        blank=True,
        null=True,
        help_text='{"title": "Стратегический капиталист", "description": "..."}'
    )
    radar_scores = models.JSONField(
        verbose_name='Cognitive Radar Scores',
        blank=True,
        null=True,
        help_text='{"capacity": 80, "stress_resistance": 65, "fomo_control": 70, "discipline": 75}'
    )
    behavioral_traps = models.JSONField(
        verbose_name='Behavioral Traps & Biases',
        blank=True,
        null=True,
        help_text='List of identified biases and warning rules'
    )
    asset_allocation = models.JSONField(
        verbose_name='Asset allocation',
        help_text='JSON object with allocation percentages: {"stocks": 60, "bonds": 25, "cash": 10, "alternatives": 5}'
    )
    recommendations = models.JSONField(
        verbose_name='Investment recommendations',
        help_text='JSON array of recommendation strings'
    )
    key_traits = models.JSONField(
        verbose_name='Key personality traits',
        help_text='JSON array of trait strings'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name = 'Investment Profile'
        verbose_name_plural = 'Investment Profiles'
        ordering = ['-updated_at']

    def __str__(self):
        return f'Investment Profile - {self.user.username} ({self.risk_category})'
