# ejercicios/admin.py
from django.contrib import admin
from .models import Exercise
from .forms import ExerciseForm

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    form = ExerciseForm  # O podrías usar lógica para detectar el tipo y usar el formulario correspondiente
    list_display = ("get_words_display", "exercise_type", "question", "submitted_at")
    list_filter = ("exercise_type", "submitted_at")
    search_fields = ("question",)
    raw_id_fields = ['words_m2m']  # Para ejercicios de selección

    def get_words_display(self, obj):
        if obj.exercise_type == "emparejamiento":
            try:
                pairs = obj.words_json
                return ", ".join(f"{pair[0]} - {pair[1]}" for pair in pairs)
            except Exception:
                return "Error en formato"
        else:
            return ", ".join(word.term for word in obj.words_m2m.all())
    get_words_display.short_description = "Palabras"

