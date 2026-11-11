"""URLs del módulo académico (roadmap ASCENSO)."""

from django.urls import path

from . import views

app_name = "roadmaps"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("etapa/<int:numero>/", views.detalle, name="detalle"),
    path("leccion/<int:leccion_id>/", views.leccion_detalle, name="leccion_detalle"),
    path("ejercicio/<int:ejercicio_id>/intento/", views.enviar_intento_view, name="enviar_intento"),
    path("etapa/<int:numero>/marcar/", views.marcar_etapa_view, name="marcar_etapa"),
    path(
        "leccion/<int:leccion_id>/marcar/",
        views.marcar_leccion_view,
        name="marcar_leccion",
    ),
]
