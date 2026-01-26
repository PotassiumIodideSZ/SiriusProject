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
