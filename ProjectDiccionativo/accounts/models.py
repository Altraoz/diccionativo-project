# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("estudiante", "Estudiante"),
        ("profesor", "Profesor"),
        ("administrador", "Administrador"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="estudiante")
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True, help_text="Breve descripción sobre ti")
    preferences = models.JSONField(blank=True, null=True, help_text="Configuración personalizada")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
