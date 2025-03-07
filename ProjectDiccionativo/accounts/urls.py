# accounts/urls.py
from django.urls import path
from .views import SignUpView, profile_update
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", profile_update, name="profile"),

    # Cambio de contraseña
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    # Resetear contraseña
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
