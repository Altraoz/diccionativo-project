# ejercicios/forms.py
import json
from django import forms
from .models import Exercise
from django.contrib.auth import get_user_model
from vocabulario.models import Word

User = get_user_model()

LANGUAGE_CHOICES = [
    ("", "--------"),       # Para que aparezca vacío por defecto
    ("Español", "Español"),
    ("Ingles", "Ingles")
    # Agrega los idiomas que manejes
]

class MultipleChoiceForm(forms.Form):
    answer = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        options = kwargs.pop('options', [])
        super().__init__(*args, **kwargs)
        # Convertimos cada opción en una tupla (opción, opción)
        self.fields['answer'].choices = [(opt, opt) for opt in options]


class ExerciseForm(forms.ModelForm):
    # Campo extra para elegir idioma antes de filtrar las palabras
    selected_language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        required=False,
        label="Selecciona el idioma",
        help_text="Elige primero el idioma para filtrar las palabras."
    )

    class Meta:
        model = Exercise
        fields = [
            "exercise_type",
            "selected_language",  # campo extra (no en el modelo)
            "words",
            "question",
            "options",
            "correct_answer",
            "assigned_students",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Mostramos todas las palabras por defecto
        self.fields["words"].queryset = Word.objects.all()

        # Determinamos si hay un instance para edición
        exercise_type = None
        if self.instance and self.instance.pk:
            # Edición
            exercise_type = self.instance.exercise_type
        else:
            # Creación: revisa los datos ingresados en el form
            exercise_type = self.data.get("exercise_type") or self.initial.get("exercise_type")

        # Tomamos el idioma elegido (si lo hay)
        language_selected = self.data.get("selected_language") or self.initial.get("selected_language")
        if language_selected:
            # Filtramos las palabras según ese idioma
            self.fields["words"].queryset = Word.objects.filter(language=language_selected)

        # Lógica final: si no se ha seleccionado idioma todavía, mostrará todas las palabras
        # o podrías dejarlo vacío:
        #
        # else:
        #    self.fields["words"].queryset = Word.objects.none()

    def clean_words(self):
        words = self.cleaned_data.get("words")
        exercise_type = self.cleaned_data.get("exercise_type")

        if exercise_type == "seleccion":
            if len(words) != 1:
                raise forms.ValidationError(
                    "Para selección múltiple, debes seleccionar exactamente 1 palabra."
                )
        elif exercise_type == "emparejamiento":
            if len(words) < 4:
                raise forms.ValidationError(
                    "Para emparejamiento, debes seleccionar al menos 4 palabras."
                )

        return words

    def clean_options(self):
        options = self.cleaned_data.get("options")
        if options is None:
            return options
        if isinstance(options, str):
            try:
                options = json.loads(options)
            except Exception:
                raise forms.ValidationError("Las opciones deben ser un JSON válido.")
        if not isinstance(options, list):
            raise forms.ValidationError("Las opciones deben ser una lista JSON.")
        return options

    def clean_correct_answer(self):
        correct_answer = self.cleaned_data.get("correct_answer")
        if correct_answer is None:
            return correct_answer
        if isinstance(correct_answer, str):
            try:
                correct_answer = json.loads(correct_answer)
            except Exception:
                raise forms.ValidationError("La respuesta correcta debe ser JSON válido.")
        if not isinstance(correct_answer, list):
            raise forms.ValidationError("La respuesta correcta debe ser una lista JSON.")
        return correct_answer

    def clean(self):
        cleaned_data = super().clean()
        options = cleaned_data.get("options")
        correct_answer = cleaned_data.get("correct_answer")

        if options and correct_answer:
            if len(options) != len(correct_answer):
                raise forms.ValidationError(
                    "La cantidad de respuestas correctas debe coincidir con la cantidad de opciones."
                )
        return cleaned_data

    def clean_options(self):
        options = self.cleaned_data.get("options")
        if options is None:
            return options
        if isinstance(options, str):
            try:
                options = json.loads(options)
            except Exception:
                raise forms.ValidationError("Las opciones deben ser un JSON válido.")
        if not isinstance(options, list):
            raise forms.ValidationError("Las opciones deben ser una lista JSON.")
        return options

    def clean_correct_answer(self):
        correct_answer = self.cleaned_data.get("correct_answer")
        if correct_answer is None:
            return correct_answer
        if isinstance(correct_answer, str):
            try:
                correct_answer = json.loads(correct_answer)
            except Exception:
                raise forms.ValidationError("La respuesta correcta debe ser JSON válido.")
        if not isinstance(correct_answer, list):
            raise forms.ValidationError("La respuesta correcta debe ser una lista JSON.")
        return correct_answer

    def clean(self):
        cleaned_data = super().clean()
        options = cleaned_data.get("options")
        correct_answer = cleaned_data.get("correct_answer")

        if options and correct_answer:
            if len(options) != len(correct_answer):
                raise forms.ValidationError(
                    "La cantidad de respuestas correctas debe coincidir con la cantidad de opciones."
                )
        return cleaned_data

class MatchingExerciseForm(forms.ModelForm):
    # Permite asignar el ejercicio a varios estudiantes
    assigned_students = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(role="estudiante"),
        required=True,
        widget=forms.CheckboxSelectMultiple,
        help_text="Seleccione los estudiantes a quienes asignar este ejercicio."
    )

    class Meta:
        model = Exercise
        fields = ["words", "exercise_type", "question", "options", "correct_answer", "assigned_students"]

    def clean_options(self):
        options = self.cleaned_data.get("options")
        if isinstance(options, str):
            try:
                options = json.loads(options)
            except Exception:
                raise forms.ValidationError("Las opciones deben ser una lista válida en formato JSON.")
        if not isinstance(options, list):
            raise forms.ValidationError("Las opciones deben ser una lista.")
        if len(options) < 4:
            raise forms.ValidationError("Debe haber al menos 4 opciones.")
        return options

    def clean_correct_answer(self):
        correct_answer = self.cleaned_data.get("correct_answer")
        if isinstance(correct_answer, str):
            try:
                correct_answer = json.loads(correct_answer)
            except Exception:
                raise forms.ValidationError("La respuesta correcta debe ser una lista válida en formato JSON.")
        if not isinstance(correct_answer, list):
            raise forms.ValidationError("La respuesta correcta debe ser una lista.")
        return correct_answer

    def clean(self):
        cleaned_data = super().clean()
        options = cleaned_data.get("options")
        correct_answer = cleaned_data.get("correct_answer")
        if options and correct_answer:
            if len(options) != len(correct_answer):
                raise forms.ValidationError("La cantidad de respuestas correctas debe coincidir con la cantidad de opciones.")
        return cleaned_data

