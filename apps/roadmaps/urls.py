"""URLs del módulo académico (roadmap ASCENSO)."""

from django.urls import path

from . import views

app_name = "roadmaps"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("etapa/<int:numero>/", views.detalle, name="detalle"),
    path("etapa/<int:numero>/marcar/", views.marcar_etapa_view, name="marcar_etapa"),
    path(
        "leccion/<int:leccion_id>/marcar/",
        views.marcar_leccion_view,
        name="marcar_leccion",
    ),
]
