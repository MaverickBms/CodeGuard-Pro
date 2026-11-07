"""Base settings for CodeGuard Pro."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Directorio de datos escribibles. En desarrollo coincide con la raíz del
# proyecto; en la aplicación empaquetada Electron pasa CODEGUARD_DATA_DIR
# apuntando a userData (Windows: %APPDATA%/CodeGuard Pro) para que la base de
# datos, los logs y los medios no se escriban dentro del directorio de
# instalación (que puede ser de solo lectura).
DATA_DIR = Path(os.environ.get("CODEGUARD_DATA_DIR", BASE_DIR)).expanduser().resolve()
DATA_DIR.mkdir(parents=True, exist_ok=True)


def _obtener_secret_key() -> str:
    """Devuelve la clave secreta local, generándola y persistiéndola si falta.

    Nunca se versiona: en desarrollo se guarda en DATA_DIR/.secret_key y en la
    aplicación empaquetada en la carpeta de datos del usuario.
    """
    valor = os.environ.get("DJANGO_SECRET_KEY", "").strip()
    if valor:
        return valor

    archivo = DATA_DIR / ".secret_key"
    if archivo.exists():
        return archivo.read_text(encoding="utf-8").strip()

    from django.core.management.utils import get_random_secret_key

    clave = get_random_secret_key()
    archivo.write_text(clave, encoding="utf-8")
    try:
        archivo.chmod(0o600)
    except OSError:
        pass
    return clave


SECRET_KEY = _obtener_secret_key()

DEBUG = os.environ.get("DJANGO_DEBUG", "True").strip().lower() in {"true", "1", "yes", "on"}

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,[::1]").split(",")
    if host.strip()
]

INSTALLED_APPS = [
    "apps.accounts",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.audit",
    "apps.core",
    "apps.roadmaps",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "config.middleware.CabecerasSeguridadMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATA_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

LANGUAGE_CODE = "es"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = DATA_DIR / "media"
MEDIA_ROOT.mkdir(parents=True, exist_ok=True)

LOG_DIR = DATA_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Mensajes basados en cookies (sin requerir middleware de sesión).
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

USE_TZ = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "codeguard.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "codeguard": {
            "handlers": ["console", "file"],
            "level": os.environ.get("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        "django": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}

# Salvaguarda: los directorios escribibles existen antes de configurar logging.
LOG_DIR.mkdir(parents=True, exist_ok=True)
MEDIA_ROOT.mkdir(parents=True, exist_ok=True)
