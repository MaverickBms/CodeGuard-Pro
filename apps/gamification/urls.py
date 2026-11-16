"""URLs del módulo de gamificación."""

from django.urls import path

from . import views

app_name = "gamification"

urlpatterns = [
    path("perfil/", views.perfil, name="perfil"),
]
