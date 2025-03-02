# vocabulario/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.http import HttpResponse
import openpyxl
from .forms import CSVUploadForm 
from .models import Word
import csv

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

@login_required
def upload_words_csv(request):
    if request.user.role != "profesor" and not request.user.is_superuser:
        messages.error(request, "No tienes permiso para cargar archivos CSV.")
        return redirect("word_list")

    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")

        if not csv_file.name.endswith('.csv'):
            messages.error(request, "El archivo debe tener formato CSV.")
            return redirect("word_list")

        try:
            decoded_file = csv_file.read().decode("utf-8").splitlines()
            reader = csv.reader(decoded_file)
            next(reader)  # Saltar encabezado

            for row in reader:
                term, translation, language, example = row
                Word.objects.create(
                    term=term.strip(),
                    translation=translation.strip(),
                    language=language.strip(),
                    example=example.strip() if example else ""
                )

            messages.success(request, "Palabras cargadas correctamente desde CSV.")
        except Exception as e:
            messages.error(request, f"Ocurrió un error al procesar el archivo: {str(e)}")

    return redirect("word_list")

def download_words_excel(request):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Diccionario"

    # Encabezados
    sheet.append(["Término", "Traducción", "Idioma", "Ejemplo"])

    # Datos
    for word in Word.objects.all():
        sheet.append([word.term, word.translation, word.language, word.example])

    # Configurar respuesta HTTP
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="diccionario.xlsx"'
    workbook.save(response)
    return response
