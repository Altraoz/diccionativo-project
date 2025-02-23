# vocabulario/admin.py
from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    search_fields = ['term']
    list_display = ['term', 'translation', 'language', 'created_at']
