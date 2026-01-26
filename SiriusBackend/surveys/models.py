from django.db import models
from authentication.models import User


class Questionnaire(models.Model):
    """
    Questionnaire model for storing user survey responses.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questionnaires',
        verbose_name='User'
    )
    question1 = models.CharField(max_length=255, verbose_name='Question 1')
    question2 = models.CharField(max_length=255, verbose_name='Question 2')
    # Add more questions as needed
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'
        ordering = ['-created_at']

    def __str__(self):
        return f'Questionnaire {self.id} - {self.user.username}'
