"""
URL configuration for ProjectDiccionativo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# diccionativo/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),

    # Rutas para la autenticación (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # Rutas personalizadas para el registro (signup) u otras vistas de accounts
    path('accounts/', include('accounts.urls')),

    # Rutas para el diccionario (vocabulario)
    path('vocabulario/', include('vocabulario.urls')),

    # Rutas para los ejercicios interactivos
    path('ejercicios/', include('ejercicios.urls')),

    # Página de inicio: se utiliza un TemplateView con la plantilla "home.html"
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]

