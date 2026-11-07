"""CodeGuard Pro URL configuration."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("apps.accounts.urls")),
    path("roadmaps/", include("apps.roadmaps.urls")),
    path("", include("apps.core.urls")),
]

# El admin solo se expone cuando está instalado (desarrollo). La aplicación
# empaquetada no lo incluye para reducir la superficie de ataque.
if "django.contrib.admin" in settings.INSTALLED_APPS:
    urlpatterns.insert(0, path("admin/", admin.site.urls))
