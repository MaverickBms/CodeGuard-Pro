"""URLs del módulo de gamificación."""

from django.urls import path

from . import views

app_name = "gamification"

urlpatterns = [
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/avatar/", views.guardar_avatar, name="guardar_avatar"),
    path("mundo/", views.mundo, name="mundo"),
    path("mundo/mapa/", views.mapa_mundo, name="mapa_mundo"),
    path("mundo/estado/", views.guardar_mundo, name="guardar_mundo"),
    path("mundo/interaccion/", views.interactuar_mundo, name="interactuar_mundo"),
    path("mundo/mision/", views.completar_mision_mundo, name="completar_mision_mundo"),
]
