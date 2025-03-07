from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, CustomUser, Profile
from django import forms



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "age", "role")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remover la opción "administrador" de las choices del campo role
        role_field = self.fields.get("role")
        if role_field:
            role_field.choices = [choice for choice in role_field.choices if choice[0] != "administrador"]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "age")

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "preferences"]
        widgets = {
            "preferences": forms.Textarea(attrs={"rows": 3}),
        }
