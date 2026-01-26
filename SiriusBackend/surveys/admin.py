from django.contrib import admin
from .models import Questionnaire


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    """
    Custom admin for Questionnaire model.
    """
    list_display = ['id', 'user', 'question1', 'question2', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user__username', 'question1', 'question2']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
