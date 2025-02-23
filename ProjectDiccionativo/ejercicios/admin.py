# ejercicios/admin.py
from django.contrib import admin
from .models import Exercise
from .forms import ExerciseForm

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    form = ExerciseForm
    list_display = ("get_words", "exercise_type", "question", "submitted_at")
    list_filter = ("exercise_type", "submitted_at")
    search_fields = ("question",)

    # Para que aparezca el botón “+” y el cuadro emergente, usas raw_id_fields o autocomplete_fields:
    raw_id_fields = ['words']

    def get_words(self, obj):
        """Devuelve una cadena con los términos de las palabras separadas por comas."""
        return ", ".join(word.term for word in obj.words.all())
    get_words.short_description = "Palabras"
