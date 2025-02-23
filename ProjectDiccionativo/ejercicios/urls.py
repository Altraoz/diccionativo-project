# ejercicios/urls.py
from django.urls import path
from .views import (
    MatchingExerciseCreateView,
    ExerciseListView,
    ExerciseDetailView,
    ExerciseCreateView,
    ExerciseUpdateView,
    ExerciseDeleteView,
    ExerciseAnswerView,  # Importamos la vista de respuesta
)

urlpatterns = [
    path("", ExerciseListView.as_view(), name="exercise_list"),
    path("new/", ExerciseCreateView.as_view(), name="exercise_create"),
    path("<int:pk>/", ExerciseDetailView.as_view(), name="exercise_detail"),
    path("<int:pk>/edit/", ExerciseUpdateView.as_view(), name="exercise_update"),
    path("<int:pk>/delete/", ExerciseDeleteView.as_view(), name="exercise_delete"),
    # Ruta para que el estudiante responda el ejercicio de selección múltiple:
    path("<int:pk>/answer/", ExerciseAnswerView.as_view(), name="exercise_answer"),
]
