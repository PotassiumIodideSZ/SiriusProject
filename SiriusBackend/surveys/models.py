from django.db import models
from authentication.models import User


class SurveyQuestion(models.Model):
    """
    Model for storing survey questions that can be enabled/disabled.
    Supports single-choice options with text and weight values.
    """
    text = models.CharField(max_length=500, verbose_name='Question text')
    order = models.IntegerField(default=0, verbose_name='Display order')
    category = models.CharField(
        max_length=50,
        default='general',
        verbose_name='Question Category',
        help_text='e.g., horizon, capacity, stress, behavioral'
    )
    options = models.JSONField(
        default=list,
        blank=True,
        verbose_name='Answer Options',
        help_text='List of options: [{"value": 1, "text": "...", "score": 20}]'
    )
    is_enabled = models.BooleanField(default=True, verbose_name='Is enabled')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        ordering = ['order']
        verbose_name = 'Survey Question'
        verbose_name_plural = 'Survey Questions'

    def __str__(self):
        return f'{self.order}. {self.text}'


class Questionnaire(models.Model):
    """
    Model for storing user's survey responses.
    Each questionnaire contains multiple QuestionAnswer records.
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending (Calculation in progress)'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questionnaires',
        verbose_name='User'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='COMPLETED',
        verbose_name='Calculation Status'
    )
    error_message = models.TextField(blank=True, null=True, verbose_name='Error message if failed')
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name='Completed at')

    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'
        ordering = ['-completed_at']

    def __str__(self):
        return f'Questionnaire {self.id} - {self.user.username} ({self.status})'
    
    @property
    def answers_count(self):
        """Return the number of answers in this questionnaire."""
        return self.answers.count()


class QuestionAnswer(models.Model):
    """
    Model for storing individual answers to survey questions.
    Links a questionnaire to a question with the user's answer value.
    """
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Questionnaire'
    )
    question = models.ForeignKey(
        SurveyQuestion,
        on_delete=models.PROTECT,
        related_name='answers',
        verbose_name='Question'
    )
    answer_value = models.PositiveSmallIntegerField(
        verbose_name='Answer value',
        help_text='Answer value (e.g. 1-5 or option index)'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Question Answer'
        verbose_name_plural = 'Question Answers'
        ordering = ['question__order']
        unique_together = ['questionnaire', 'question']  # One answer per question per questionnaire

    def __str__(self):
        return f'Q{self.question.id}: {self.answer_value} (Questionnaire {self.questionnaire.id})'
