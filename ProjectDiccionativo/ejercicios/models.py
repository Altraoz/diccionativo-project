# ejercicios/models.py
from django.db import models
from vocabulario.models import Word
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Exercise(models.Model):
    EXERCISE_TYPE_CHOICES = (
        ("seleccion", "Selección Múltiple"),
        ("emparejamiento", "Emparejamiento"),
    )

    # Para mantener la flexibilidad, definimos un ManyToMany
    # que permita múltiples palabras en emparejamiento
    words = models.ManyToManyField(
        Word,
        blank=True,
        related_name="exercises",
        help_text="Selecciona las palabras involucradas en este ejercicio."
    )

    exercise_type = models.CharField(
        max_length=20,
        choices=EXERCISE_TYPE_CHOICES
    )
    question = models.TextField()

    options = models.JSONField(
        blank=True,
        null=True,
        help_text="Lista de opciones en formato JSON"
    )

    correct_answer = models.JSONField(
        blank=True,
        null=True,
        help_text="Lista de respuestas correctas en formato JSON",
        default=list  # Esto asigna [] por defecto
    )

    # Los estudiantes a quienes se asigna el ejercicio
    assigned_students = models.ManyToManyField(
        User,
        blank=True,
        limit_choices_to={'role': 'estudiante'},
        related_name="assigned_exercises"
    )

    # Usuario (profesor/admin) que crea el ejercicio
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="created_exercises"
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ejercicio ({self.exercise_type})"

    def get_absolute_url(self):
        return reverse("exercise_detail", kwargs={"pk": self.pk})
