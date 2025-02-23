# vocabulario/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .models import Word

# Vista para listar palabras (accesible para todos)
class WordListView(ListView):
    model = Word
    template_name = "vocabulario/word_list.html"
    context_object_name = "words"

# Vista para el detalle de una palabra (accesible para todos)
class WordDetailView(DetailView):
    model = Word
    template_name = "vocabulario/word_detail.html"

# Mixin para restringir el acceso a profesores
class ProfessorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # Asume que el campo 'role' de tu usuario tiene el valor "profesor" para los profesores
        return self.request.user.is_authenticated and self.request.user.role == "profesor"

# Vista para crear una nueva palabra (solo para profesores)
class WordCreateView(LoginRequiredMixin, ProfessorRequiredMixin, CreateView):
    model = Word
    template_name = "vocabulario/word_form.html"
    fields = ['term', 'translation', 'language', 'example']

# Vista para actualizar una palabra (solo para profesores)
class ProfessorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        # Solo permite si es superusuario o si su rol es "profesor"
        return user.is_authenticated and (user.is_superuser or user.role == "profesor")

    def handle_no_permission(self):
        raise PermissionDenied("No tienes permisos para editar esta palabra.")

class WordUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Word
    template_name = "vocabulario/word_form.html"
    fields = ['term', 'translation', 'language', 'example']

# Vista para eliminar una palabra (solo para profesores)
class WordDeleteView(LoginRequiredMixin, ProfessorRequiredMixin, DeleteView):
    model = Word
    template_name = "vocabulario/word_confirm_delete.html"
    success_url = reverse_lazy("word_list")
