# ejercicios/urls.py
from django.urls import path
from .views import (
    ChooseExerciseTypeView,
    MatchingExerciseCreateView,
    ExerciseListView,
    ExerciseDetailView,
    ExerciseCreateView,
    ExerciseUpdateView,
    ExerciseDeleteView,
    ExerciseAnswerView,
)

urlpatterns = [
    path("", ExerciseListView.as_view(), name="exercise_list"),
    # Nueva ruta para elegir el tipo de ejercicio
    path("new/choose/", ChooseExerciseTypeView.as_view(), name="choose_exercise_type"),
    # Ruta para ejercicios generales (selección, etc.)
    path("new/", ExerciseCreateView.as_view(), name="exercise_create"),
    # Ruta específica para ejercicios de emparejamiento:
    path("new/matching/", MatchingExerciseCreateView.as_view(), name="matching_exercise_create"),
    path("<int:pk>/", ExerciseDetailView.as_view(), name="exercise_detail"),
    path("<int:pk>/edit/", ExerciseUpdateView.as_view(), name="exercise_update"),
    path("<int:pk>/delete/", ExerciseDeleteView.as_view(), name="exercise_delete"),
    path("<int:pk>/answer/", ExerciseAnswerView.as_view(), name="exercise_answer"),
]
