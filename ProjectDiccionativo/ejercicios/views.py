# ejercicios/views.py
from django.views.generic import FormView
from vocabulario.models import Word
import logging
import json
from django.http import JsonResponse
from django import forms
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Exercise
from .forms import MultipleChoiceForm, MatchingEjercicioForm, ExerciseForm
from .mixins import ProfessorOrAdminRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
logger = logging.getLogger(__name__)

class MatchingAnswerForm(forms.Form):
    """
    Formulario para responder (no para editar) un ejercicio de emparejamiento.
    Contiene dos campos hidden para words_json y correct_answer,
    así como un campo answer para la respuesta del estudiante.
    """
    words_json = forms.CharField(widget=forms.HiddenInput(), required=False)
    correct_answer = forms.CharField(widget=forms.HiddenInput(), required=False)
    # El campo answer se usará para recolectar la respuesta generada por el usuario.
    answer = forms.CharField(widget=forms.HiddenInput(), required=False)


class ExerciseAnswerView(LoginRequiredMixin, FormView):
    """
    Vista para que el estudiante responda un ejercicio.
    Si es emparejamiento se usa MatchingAnswerForm y una plantilla especial.
    Si no, se usa MultipleChoiceForm y se devuelve la respuesta en JSON.
    """
    form_class = MultipleChoiceForm  # Por defecto, para ejercicios de selección
    template_name = "ejercicios/exercise_answer.html"
    
    def dispatch(self, request, *args, **kwargs):
        self.exercise = get_object_or_404(Exercise, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_class(self):
        if self.exercise.exercise_type == "emparejamiento":
            return MatchingAnswerForm
        return MultipleChoiceForm
    
    def get_template_names(self):
        if self.exercise.exercise_type == "emparejamiento":
            return ["ejercicios/matching_exercise_answer.html"]
        return ["ejercicios/exercise_answer.html"]
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.exercise.exercise_type == "emparejamiento":
            words_json_str = json.dumps(self.exercise.words_json or [])
            correct_answer_str = json.dumps(self.exercise.correct_answer or [])
            kwargs['initial'] = {
                'words_json': words_json_str,
                'correct_answer': correct_answer_str,
            }
        else:
            kwargs['options'] = self.exercise.options or []
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercise'] = self.exercise
        return context
    
    def form_valid(self, form):
        # Caso de Selección (no emparejamiento)
        if self.exercise.exercise_type != "emparejamiento":
            selected_answer = form.cleaned_data.get('answer')
            # Aseguramos que correct_answer se trate como una lista
            correct_answer = self.exercise.correct_answer
            if isinstance(correct_answer, str):
                try:
                    correct_answer = json.loads(correct_answer)
                except Exception:
                    correct_answer = []
            # Comprobamos que la respuesta seleccionada sea la esperada
            if correct_answer and selected_answer == correct_answer[0]:
                return JsonResponse({
                    "correct": True,
                    "correct_answer": selected_answer,
                }, status=200)
            else:
                correct_value = correct_answer[0] if correct_answer else "desconocida"
                return JsonResponse({
                    "correct": False,
                    "correct_answer": correct_value
                }, status=200)
        else:
            # Caso de Emparejamiento
            user_answer = form.cleaned_data.get('answer')  # Se espera en formato JSON
            if user_answer:
                try:
                    user_answer_parsed = json.loads(user_answer)
                except json.JSONDecodeError:
                    user_answer_parsed = []
                if user_answer_parsed == self.exercise.correct_answer:
                    return JsonResponse({
                        "correct": True,
                        "correct_answer": user_answer_parsed,
                    }, status=200)
                else:
                    correct_value = self.exercise.correct_answer[0] if self.exercise.correct_answer else "desconocida"
                    return JsonResponse({
                        "correct": False,
                        "correct_answer": correct_value
                    }, status=200)
            else:
                return JsonResponse({
                    "correct": False,
                    "error": "No se recibió ninguna respuesta."
                }, status=400)
    
    def form_invalid(self, form):
        return JsonResponse({
            "correct": False,
            "error": "Formulario inválido"
        }, status=400)


class ProfessorOrAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.role == "profesor")

class MatchingExerciseCreateView(LoginRequiredMixin, ProfessorOrAdminRequiredMixin, CreateView):
    model = Exercise
    form_class = MatchingEjercicioForm
    template_name = "ejercicios/matching_exercise_form.html"

    def get_initial(self):
        initial = super().get_initial()
        #initial["exercise_type"] = "emparejamiento"
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_words'] = self.get_form().available_words
        print("DEBUG: Antes de guardar, instancia:", context)
        return context

    def form_valid(self, form):
        print("DEBUG: Antes de guardar, instancia:", form.instance)
        form.instance.user = self.request.user
        form.instance.exercise_type = "emparejamiento"
        response = super().form_valid(form)
        print("DEBUG: Objeto guardado con pk:", self.object.pk)
        messages.success(self.request, "Ejercicio de emparejamiento creado correctamente.")
        return response

    def get_success_url(self):
        # Redirige al detalle del ejercicio tras un guardado exitoso.
        return reverse("exercise_detail", kwargs={"pk": self.object.pk})    
# Para que cualquier usuario autenticado (estudiante, profesor, admin) pueda ver los ejercicios:
class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = "ejercicios/exercise_list.html"
    context_object_name = "exercises"

class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = "ejercicios/exercise_detail.html"

# Sólo profesores y administradores pueden crear ejercicios:
class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "ejercicios/exercise_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 2) Pasamos al contexto las palabras definidas en el form
        context["available_words"] = self.get_form().available_words
        return context

    def form_valid(self, form):
        """ Se ejecuta cuando el formulario es válido """
        print("\n✅ FORMULARIO VÁLIDO, GUARDANDO...\n")
        print(form.cleaned_data)  # Muestra los datos limpios en la consola

        form.instance.exercise_type = "seleccion"
        form.instance.user = self.request.user
        response = super().form_valid(form)

        messages.success(self.request, "Ejercicio de Selección creado correctamente.")
        return response

    def form_invalid(self, form):
        """ Se ejecuta cuando el formulario tiene errores """
        print("\n🔴 ERROR EN EL FORMULARIO 🔴\n")
        for field, errors in form.errors.items():
            print(f"⚠️ {field}: {', '.join(errors)}")

        messages.error(self.request, "Hubo un error en el formulario. Por favor, revisa los campos e inténtalo de nuevo.")

        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse("exercise_detail", kwargs={"pk": self.object.pk})

# De igual manera, para actualizar:
class ExerciseUpdateView(LoginRequiredMixin, ProfessorOrAdminRequiredMixin, UpdateView):
    model = Exercise
    template_name = "ejercicios/exercise_form.html"  # plantilla por defecto

    def get_form_class(self):
        # Según el tipo de ejercicio, retornamos el formulario adecuado.
        if self.object.exercise_type == "emparejamiento":
            return MatchingEjercicioForm
        else:
            return ExerciseForm

    def get_template_names(self):
        if self.object.exercise_type == "emparejamiento":
            return ["ejercicios/matching_exercise_Edit.html"]
        return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Si el ejercicio es de emparejamiento, agregamos available_words al contexto
        if self.object.exercise_type == "emparejamiento":
            from vocabulario.models import Word
            context['available_words'] = Word.objects.all()
        return context
# Y para eliminar:
class ExerciseDeleteView(LoginRequiredMixin, ProfessorOrAdminRequiredMixin, DeleteView):
    model = Exercise
    template_name = "ejercicios/exercise_confirm_delete.html"
    success_url = "/ejercicios/"

class ChooseExerciseTypeView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "ejercicios/choose_exercise_type.html"

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.role == "profesor")
