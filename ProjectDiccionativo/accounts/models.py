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
