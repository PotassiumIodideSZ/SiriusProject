from django.contrib import admin
from .models import Recommendation


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    """
    Custom admin for Recommendation model.
    """
    list_display = ['id', 'user', 'recommendation_text', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user__username', 'recommendation_text']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
