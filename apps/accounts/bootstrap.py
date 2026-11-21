"""Propietario local del perfil monousuario.

La autenticación permanece desactivada (decisión del propietario). Aun así,
Django necesita una fila de usuario para asociar progreso, intentos,
evidencias, gamificación y auditoría. En un perfil limpio no existía ninguna,
por lo que todas las operaciones de escritura quedaban bloqueadas.

Este módulo crea, solo cuando ``AUTH_DISABLED`` está activo, un propietario
local sin contraseña utilizable. No crea sesiones, no reactiva el login y no
expone credenciales. Si ya existe cualquier usuario activo, se reutiliza.
"""

from __future__ import annotations

import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.utils import timezone

from apps.audit.services import registrar_evento

logger = logging.getLogger("codeguard")

USERNAME_PROPIETARIO_LOCAL = "propietario-local"


def asegurar_propietario_local():
    """Devuelve el propietario local, creándolo una sola vez si falta.

    Es idempotente y seguro ante dos procesos concurrentes: el nombre de
    usuario es único y, si otra ejecución gana la carrera, se recupera la fila
    existente. No modifica usuarios existentes ni sus contraseñas.
    """
    if not getattr(settings, "AUTH_DISABLED", False):
        return None

    Usuario = get_user_model()
    usuario = Usuario.objects.filter(is_active=True).order_by("id").first()
    if usuario is not None:
        _asegurar_permiso_editorial(usuario)
        _marcar_configuracion_inicial()
        return usuario

    try:
        with transaction.atomic():
            usuario = Usuario.objects.create_user(
                username=USERNAME_PROPIETARIO_LOCAL,
                password=None,
            )
            usuario.fecha_configuracion_inicial = timezone.now()
            usuario.is_staff = True
            usuario.save(update_fields=["fecha_configuracion_inicial", "is_staff"])
            registrar_evento(
                "perfil_local_inicializado",
                usuario=usuario,
                descripcion=(
                    "Propietario local creado para el modo sin autenticación. "
                    "No se establecieron credenciales de acceso."
                ),
            )
    except IntegrityError:
        usuario = (
            Usuario.objects.filter(is_active=True).order_by("id").first()
        )
        if usuario is None:
            raise

    _asegurar_permiso_editorial(usuario)
    _marcar_configuracion_inicial()
    logger.info("Propietario local disponible: %s", usuario.pk)
    return usuario


def _asegurar_permiso_editorial(usuario) -> None:
    """El propietario local puede administrar el flujo editorial sin login.

    ``is_staff`` no activa autenticación ni sesiones: solo habilita las
    transiciones editoriales auditadas del modo monousuario. La aplicación
    empaquetada no instala el admin de Django.
    """
    if usuario.is_staff:
        return
    usuario.is_staff = True
    usuario.save(update_fields=["is_staff"])


def _marcar_configuracion_inicial() -> None:
    """Refleja que el modo local no requiere asistente de configuración."""
    from apps.core.models import ConfiguracionSistema

    configuracion = ConfiguracionSistema.cargar()
    if not configuracion.configuracion_inicial_completada:
        configuracion.configuracion_inicial_completada = True
        configuracion.save(update_fields=["configuracion_inicial_completada"])
