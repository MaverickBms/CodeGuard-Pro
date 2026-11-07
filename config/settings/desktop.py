"""Settings para el servidor Django empaquetado con Electron.

Se usa cuando ``DJANGO_SETTINGS_MODULE=config.settings.desktop``. La aplicación
Electron inicia el binario del servidor, le pasa un puerto libre en
``CODEGUARD_PORT`` y un directorio de datos escribible en ``CODEGUARD_DATA_DIR``.

Características:
- ``DEBUG=False`` y hosts limitados a loopback.
- La base de datos, los logs y los medios viven en ``CODEGUARD_DATA_DIR``.
- Los archivos estáticos se sirven con WhiteNoise desde el propio proceso local;
  no se abre ningún puerto externo.
"""

from .base import *  # noqa: F401,F403

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "[::1]"]

# La aplicación es monousuario y local; no hay TLS ni dominio público.
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = []

# Endurecimiento adicional para el proceso local.
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "no-referrer"
X_FRAME_OPTIONS = "DENY"

# El servidor empaquetado no necesita el admin de Django: config/urls.py solo lo
# registra si está instalado. Así se reduce el tamaño y la superficie de ataque.
INSTALLED_APPS = [app for app in INSTALLED_APPS if app != "django.contrib.admin"]  # noqa: F405

# El servidor empaquetado usa WhiteNoise y sirve los recursos locales desde el
# directorio estático de la aplicación, evitando depender de runserver.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "config.middleware.CabecerasSeguridadMiddleware",
    "config.middleware.SesionInactividadMiddleware",
]
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / "static"

LOGGING["handlers"]["file"]["filename"] = LOG_DIR / "server.log"  # noqa: F405
