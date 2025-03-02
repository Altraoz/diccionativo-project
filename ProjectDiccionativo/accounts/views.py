# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserUpdateForm, ProfileForm
from .models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def profile_update(request):
    # 🔹 Asegurarse de que el usuario tenga un perfil
    profile, created = Profile.objects.get_or_create(user=request.user)

    user_form = CustomUserUpdateForm(instance=request.user)
    profile_form = ProfileForm(instance=profile)

    if request.method == "POST":
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    return render(request, "accounts/profile_update.html", {"user_form": user_form, "profile_form": profile_form})