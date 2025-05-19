from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Questionnaire, Recommendation

# Регистрация кастомной модели пользователя
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Регистрация модели Questionnaire
@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('user', 'question1', 'question2', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'question1', 'question2')
    raw_id_fields = ('user',)  # Полезно, если у вас много пользователей

# Регистрация модели Recommendation
@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommendation_text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'recommendation_text')
    raw_id_fields = ('user',)