"""URLs del módulo de gamificación."""

from django.urls import path

from . import views

app_name = "gamification"

urlpatterns = [
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/avatar/", views.guardar_avatar, name="guardar_avatar"),
]
