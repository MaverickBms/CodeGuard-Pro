"""URLs del módulo académico (roadmap ASCENSO)."""

from django.urls import path

from . import editorial_views, views

app_name = "roadmaps"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("conocimiento/", views.conocimiento, name="conocimiento"),
    path("cobertura/", editorial_views.cobertura, name="cobertura"),
    path("editorial/", editorial_views.editorial, name="editorial"),
    path("editorial/fuentes/", editorial_views.editorial_fuentes, name="editorial_fuentes"),
    path("editorial/leccion/<int:leccion_id>/", editorial_views.editorial_leccion, name="editorial_leccion"),
    path("evaluaciones/", views.evaluaciones, name="evaluaciones"),
    path("evidencias/", views.evidencias, name="evidencias"),
    path("etapa/<int:numero>/", views.detalle, name="detalle"),
    path("leccion/<int:leccion_id>/", views.leccion_detalle, name="leccion_detalle"),
    path("ejercicio/<int:ejercicio_id>/intento/", views.enviar_intento_view, name="enviar_intento"),
    path("etapa/<int:numero>/marcar/", views.marcar_etapa_view, name="marcar_etapa"),
    path(
        "etapa/<int:numero>/criterio/<int:criterio_id>/registrar/",
        views.registrar_criterio_view,
        name="registrar_criterio",
    ),
    path(
        "leccion/<int:leccion_id>/marcar/",
        views.marcar_leccion_view,
        name="marcar_leccion",
    ),
    path("quiz/<int:quiz_id>/", views.quiz_detalle, name="quiz_detalle"),
    path(
        "quiz/<int:quiz_id>/resultado/<int:resultado_id>/",
        views.quiz_resultado,
        name="quiz_resultado",
    ),
    path(
        "quiz/<int:quiz_id>/historial/",
        views.quiz_historial,
        name="quiz_historial",
    ),
]
