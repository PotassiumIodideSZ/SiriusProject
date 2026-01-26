from django.contrib import admin
from .models import SurveyQuestion, Questionnaire, QuestionAnswer


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    """
    Custom admin for SurveyQuestion model.
    """
    list_display = ['id', 'order', 'text', 'is_enabled', 'created_at']
    list_filter = ['is_enabled', 'created_at']
    search_fields = ['text']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order']


class QuestionAnswerInline(admin.TabularInline):
    """
    Inline admin for QuestionAnswer to display answers within Questionnaire.
    """
    model = QuestionAnswer
    extra = 0
    readonly_fields = ['question', 'answer_value', 'created_at']
    can_delete = False


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    """
    Custom admin for Questionnaire model.
    """
    list_display = ['id', 'user', 'answers_count', 'completed_at']
    list_filter = ['completed_at', 'user']
    search_fields = ['user__username']
    readonly_fields = ['completed_at', 'answers_count']
    ordering = ['-completed_at']
    inlines = [QuestionAnswerInline]
    
    def answers_count(self, obj):
        return obj.answers.count()
    answers_count.short_description = 'Answers Count'


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    """
    Custom admin for QuestionAnswer model.
    """
    list_display = ['id', 'questionnaire', 'question', 'answer_value', 'created_at']
    list_filter = ['answer_value', 'created_at', 'question']
    search_fields = ['questionnaire__user__username', 'question__text']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
