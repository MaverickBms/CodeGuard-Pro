"""URLs de la biblioteca documental."""

from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("importar/", views.importar, name="importar"),
    path("<int:pk>/", views.detalle, name="detalle"),
    path("<int:pk>/archivo/", views.archivo, name="archivo"),
    path("<int:pk>/estado/", views.cambiar_estado, name="cambiar_estado"),
]
