# ejercicios/views.py
from django.views.generic import FormView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Exercise
from .forms import MultipleChoiceForm, MatchingExerciseForm, ExerciseForm
from .mixins import ProfessorOrAdminRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ExerciseAnswerView(LoginRequiredMixin, FormView):
    template_name = "ejercicios/exercise_answer.html"
    form_class = MultipleChoiceForm

    def dispatch(self, request, *args, **kwargs):
        # Obtenemos el ejercicio
        self.exercise = get_object_or_404(Exercise, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Se pasan las opciones definidas en el ejercicio; se asume que exercise.options es una lista
        kwargs['options'] = self.exercise.options or []
        return kwargs

    def form_valid(self, form):
        selected_answer = form.cleaned_data.get('answer')
        if selected_answer == self.exercise.correct_answer:
            messages.success(self.request, "¡Respuesta correcta!")
        else:
            messages.error(self.request, "Respuesta incorrecta. Inténtalo de nuevo.")
        # Puedes redirigir a la misma página o a otra, por ejemplo, al detalle del ejercicio:
        return redirect(reverse("exercise_answer", kwargs={"pk": self.exercise.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercise'] = self.exercise  # Para usarlo en la plantilla
        return context

class ProfessorOrAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.role == "profesor")

class MatchingExerciseCreateView(LoginRequiredMixin, ProfessorOrAdminRequiredMixin, CreateView):
    model = Exercise
    form_class = MatchingExerciseForm
    template_name = "ejercicios/matching_exercise_form.html"

    def form_valid(self, form):
        # Asigna el usuario que crea el ejercicio
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Ejercicio de emparejamiento creado correctamente.")
        return response
# Para que cualquier usuario autenticado (estudiante, profesor, admin) pueda ver los ejercicios:
class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = "ejercicios/exercise_list.html"
    context_object_name = "exercises"

class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = "ejercicios/exercise_detail.html"

# Sólo profesores y administradores pueden crear ejercicios:
class ExerciseCreateView(LoginRequiredMixin, ProfessorOrAdminRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "ejercicios/exercise_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user  # Asigna el usuario creador
        return super().form_valid(form)

# De igual manera, para actualizar:
class ExerciseUpdateView(LoginRequiredMixin, ProfessorOrAdminRequiredMixin, UpdateView):
    model = Exercise
    template_name = "ejercicios/exercise_form.html"
    fields = ["words", "exercise_type", "question", "options", "correct_answer"]

# Y para eliminar:
class ExerciseDeleteView(LoginRequiredMixin, ProfessorOrAdminRequiredMixin, DeleteView):
    model = Exercise
    template_name = "ejercicios/exercise_confirm_delete.html"
    success_url = "/ejercicios/"
