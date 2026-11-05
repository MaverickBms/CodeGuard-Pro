"""URLs del módulo core (panel principal y navegación)."""

from django.urls import path

from apps.core import views

app_name = "core"

urlpatterns = [
    path("", views.panel, name="panel"),
]
