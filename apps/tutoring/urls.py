"""URLs del módulo de tutoría inteligente local (Fase 3)."""

from django.urls import path

from . import views

app_name = "tutoring"

urlpatterns = [
    path("estado/", views.tutoria_estado, name="estado"),
    path(
        "ejercicio/<int:ejercicio_id>/iniciar/",
        views.tutoria_iniciar,
        name="iniciar",
    ),
    path(
        "ejercicio/<int:ejercicio_id>/pista/",
        views.tutoria_pista,
        name="pista",
    ),
    path(
        "ejercicio/<int:ejercicio_id>/analizar/",
        views.tutoria_analizar,
        name="analizar",
    ),
]
