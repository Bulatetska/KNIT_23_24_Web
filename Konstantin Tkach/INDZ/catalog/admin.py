from django.contrib import admin
from .models import Game, Review

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Колонки, які буде видно в списку ігор
    list_display = ('title', 'category', 'author_name', 'created_at')
    # Фільтрація за категорією справа
    list_filter = ('category', 'created_at')
    # Пошук за назвою та автором
    search_fields = ('title', 'author_name')
    # Порядок сортування
    ordering = ('-created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Тепер замість "Review object" ти бачитимеш автора і гру
    list_display = ('author_name', 'game', 'created_at')
    list_filter = ('game', 'created_at')
    search_fields = ('author_name', 'text')