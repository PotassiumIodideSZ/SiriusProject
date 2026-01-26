from django.db import models
from authentication.models import User


class SurveyQuestion(models.Model):
    """
    Model for storing survey questions that can be enabled/disabled.
    """
    text = models.CharField(max_length=500, verbose_name='Question text')
    order = models.IntegerField(default=0, verbose_name='Display order')
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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questionnaires',
        verbose_name='User'
    )
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name='Completed at')

    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'
        ordering = ['-completed_at']

    def __str__(self):
        return f'Questionnaire {self.id} - {self.user.username}'
    
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
        help_text='Answer value between 1 and 5'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Question Answer'
        verbose_name_plural = 'Question Answers'
        ordering = ['question__order']
        unique_together = ['questionnaire', 'question']  # One answer per question per questionnaire

    def __str__(self):
        return f'Q{self.question.id}: {self.answer_value} (Questionnaire {self.questionnaire.id})'
    
    def clean(self):
        """Validate that answer_value is between 1 and 5."""
        from django.core.exceptions import ValidationError
        if not 1 <= self.answer_value <= 5:
            raise ValidationError({'answer_value': 'Answer value must be between 1 and 5'})
