# ejercicios/forms.py

import json
from django import forms
from django.contrib.auth import get_user_model
from vocabulario.models import Word
from django.core.exceptions import ValidationError
from .models import Exercise

User = get_user_model()

LANGUAGE_CHOICES = [
    ("", "--------"),       # Para que aparezca vacío por defecto
    ("Español", "Español"),
    ("Ingles", "Ingles"),
    # Agrega aquí otros idiomas que manejes
]

class MultipleChoiceForm(forms.Form):
    """
    Formulario simple para responder un ejercicio de Selección Múltiple.
    Recibe una lista de opciones mediante el constructor y renderiza
    radio buttons con la opción 'answer'.
    """
    answer = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        options = kwargs.pop('options', [])
        super().__init__(*args, **kwargs)
        # Convertimos cada opción en una tupla (opción, opción)
        self.fields['answer'].choices = [(opt, opt) for opt in options]


class ExerciseForm(forms.ModelForm):   
    
    class Meta:
        model = Exercise
        fields = [
            "exercise_type",
            "words_m2m",
            "question",
            "options",
            "correct_answer",
            "assigned_students",
        ]
        widgets = {
            "exercise_type": forms.HiddenInput(),
            "options": forms.HiddenInput(),
            "correct_answer": forms.HiddenInput(),
            "question": forms.TextInput(attrs={"class": "form-control"}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Definimos las palabras disponibles para usarlas en el template.
        self.available_words = Word.objects.all()

        # Ajustamos el label y el help text para el campo de la palabra indígena.
        self.fields["words_m2m"].label = "Seleccione la palabra en la lengua indígena del ejercicio"
        self.fields["words_m2m"].help_text = "Debes escoger exactamente 1 palabra"
        
        # Eliminamos el campo 'exercise_type' del form, ya que se maneja de forma oculta.
        self.fields.pop("exercise_type", None)
    
    def clean_words_m2m(self):
        value = self.cleaned_data.get("words_m2m")
        if not value:
            raise ValidationError("Debes seleccionar una palabra en la lengua indígena.")
        # Si 'value' es un QuerySet (o similar), se espera que contenga exactamente 1 elemento.
        if hasattr(value, "count"):
            if value.count() != 1:
                raise ValidationError("Debes seleccionar exactamente 1 palabra en la lengua indígena.")
            return list(value)
        # En caso de ser un valor único (por ejemplo, un string con el ID)
        try:
            word = Word.objects.get(pk=value)
        except Word.DoesNotExist:
            raise ValidationError("La palabra seleccionada no es válida.")
        return [word]
    
    def clean_options(self):
        data = self.cleaned_data.get("options") or "[]"
        if isinstance(data, list):
            parsed = data
        else:
            try:
                parsed = json.loads(data)
            except json.JSONDecodeError:
                raise ValidationError("Las opciones deben ser un JSON válido.")
        if not isinstance(parsed, list):
            raise ValidationError("Las opciones deben ser una lista JSON.")
        if len(parsed) < 1:
            raise ValidationError("Agrega al menos 1 opción en español.")
        return parsed
    
    def clean_correct_answer(self):
        data = self.cleaned_data.get("correct_answer") or "[]"
        if isinstance(data, list):
            parsed = data
        else:
            try:
                parsed = json.loads(data)
            except json.JSONDecodeError:
                raise ValidationError("La respuesta correcta debe ser un JSON válido.")
        if not isinstance(parsed, list) or len(parsed) != 1:
            raise ValidationError("La respuesta correcta debe ser una lista con un único elemento.")
        return parsed
    
    def clean(self):
        cleaned_data = super().clean()
        options_str = cleaned_data.get("options") or "[]"
        correct_str = cleaned_data.get("correct_answer") or "[]"
        try:
            options = json.loads(options_str) if isinstance(options_str, str) else options_str
            correct_list = json.loads(correct_str) if isinstance(correct_str, str) else correct_str
        except Exception:
            return cleaned_data  # Las validaciones individuales ya han informado el error.
        if correct_list:
            correct_value = correct_list[0]
            if correct_value not in options:
                raise ValidationError("La respuesta correcta no coincide con las opciones agregadas.")
        return cleaned_data

User = get_user_model()

class MatchingEjercicioForm(forms.ModelForm):
    """
    Formulario específico para crear ejercicios de emparejamiento.
    Se espera que el campo 'words_json' contenga una lista de pares de palabras,
    por ejemplo: [["gato", "cat"], ["perro", "dog"], ["sol", "sun"], ["luna", "moon"]]
    
    El campo 'correct_answer' debe ser una lista de pares de índices que indiquen
    el emparejamiento correcto, por ejemplo: [[0, 1], [1, 0], [2, 3], [3, 2]]
    """
    class Meta:
        model = Exercise
        fields = [
            "exercise_type",
            "words_json",  # Se almacenarán los pares en formato JSON
            "question",
            "correct_answer",
            "assigned_students"
        ]
        widgets = {
            # Se ocultan para que el usuario no los modifique manualmente
            'words_json': forms.HiddenInput(),
            'correct_answer': forms.HiddenInput(),
            'exercise_type': forms.HiddenInput(),
            'question': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'words_json': 'Se llenará automáticamente con los pares agregados.',
            'correct_answer': 'Se llenará automáticamente con la definición de respuesta correcta.'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes definir aquí una variable para pasar las palabras disponibles a la plantilla.
        self.available_words = Word.objects.all()
        self.fields.pop("exercise_type", None)
    
    # Se mantienen las validaciones existentes (clean_words_json, clean_correct_answer, clean)
    def clean_words_json(self):
        data = self.cleaned_data.get('words_json')
        print("Tipo de data (words_json):", type(data))
        # Si ya es una lista, no lo decodificamos
        if isinstance(data, list):
            parsed = data
        else:
            try:
                parsed = json.loads(data)
            except json.JSONDecodeError:
                raise ValidationError("Formato JSON inválido en palabras.")
        
        if not isinstance(parsed, list):
            raise ValidationError("Las palabras deben ser una lista de pares.")
        
        if len(parsed) < 4:
            raise ValidationError("Debe ingresar al menos 4 pares de palabras.")
        
        for pair in parsed:
            if not isinstance(pair, (list, tuple)):
                raise ValidationError("Cada par debe ser una lista o tupla.")
            if len(pair) != 2:
                raise ValidationError("Cada par debe contener exactamente dos elementos.")
            if not all(isinstance(item, str) for item in pair):
                raise ValidationError("Cada elemento en el par debe ser una cadena de texto.")
        
        print("Parsed words_json:", parsed)
        return parsed

    def clean_correct_answer(self):
        data = self.cleaned_data.get('correct_answer')
        
        # Si ya es una lista, usamos directamente
        if isinstance(data, list):
            parsed = data
        else:
            try:
                parsed = json.loads(data)
            except json.JSONDecodeError:
                raise ValidationError("Formato JSON inválido en respuesta correcta.")
        
        if not isinstance(parsed, list):
            raise ValidationError("La respuesta correcta debe ser una lista de pares de índices.")
        
        for pair in parsed:
            if not isinstance(pair, (list, tuple)):
                raise ValidationError("Cada elemento de la respuesta debe ser una lista o tupla.")
            if len(pair) != 2:
                raise ValidationError("Cada par en la respuesta correcta debe contener exactamente 2 índices.")
            for index in pair:
                if not isinstance(index, int):
                    raise ValidationError("Los índices en la respuesta correcta deben ser enteros.")
        
        print(parsed)
        return parsed

    def clean(self):
        cleaned_data = super().clean()
        exercise_type = cleaned_data.get("exercise_type")
        if exercise_type == "emparejamiento":
            words = cleaned_data.get("words_json")
            correct_answer = cleaned_data.get("correct_answer")
            if words is None:
                raise ValidationError("Se requiere ingresar los pares de palabras.")
            if correct_answer is None:
                raise ValidationError("Se requiere especificar la respuesta correcta.")
            num_pairs = len(words)
            if len(correct_answer) != num_pairs:
                raise ValidationError("La cantidad de pares en la respuesta correcta debe coincidir con la cantidad de pares de palabras.")
            for pair in correct_answer:
                for index in pair:
                    if index < 0 or index >= num_pairs:
                        raise ValidationError("Los índices en la respuesta correcta deben estar dentro del rango de pares de palabras.")
        return cleaned_data

