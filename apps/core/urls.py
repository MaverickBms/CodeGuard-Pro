"""URLs del módulo core (panel principal y navegación)."""

from django.urls import path

from apps.core import backup_views, views

app_name = "core"

urlpatterns = [
    path("", views.panel, name="panel"),
    path("backups/", backup_views.backups, name="backups"),
]
