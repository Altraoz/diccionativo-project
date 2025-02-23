# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "age", "role", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información personal", {"fields": ("first_name", "last_name", "email", "age", "role")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "age", "role", "password1", "password2"),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Si el usuario que edita no es superusuario, eliminar la opción "administrador" en el campo "role"
        if not request.user.is_superuser:
            role_field = form.base_fields.get("role")
            if role_field:
                role_field.choices = [choice for choice in role_field.choices if choice[0] != "administrador"]
        return form

admin.site.register(CustomUser, CustomUserAdmin)

