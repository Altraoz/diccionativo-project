# vocabulario/models.py
from django.db import models
from django.urls import reverse

class Word(models.Model):
    term = models.CharField(max_length=100, help_text="La palabra en la lengua indígena")
    translation = models.CharField(max_length=150, help_text="Traducción de la palabra")
    language = models.CharField(max_length=50, help_text="Nombre de la lengua indígena")
    example = models.TextField(blank=True, null=True, help_text="Ejemplo de uso de la palabra")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.term

    def get_absolute_url(self):
        return reverse("word_detail", kwargs={"pk": self.pk})