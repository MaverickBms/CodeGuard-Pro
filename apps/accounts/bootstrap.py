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


def _marcar_como_propietario(usuario) -> None:
    """Marca de forma persistente la cuenta propietaria del perfil local.

    La marca es deliberada y solo la escribe el arranque local. No convierte
    por sí sola a una cuenta en administradora del admin de Django; el modo
    monousuario usa la marca para resolver la identidad local y, únicamente
    para esa cuenta, habilitar las transiciones editoriales auditadas.
    """
    if usuario.es_propietario_local:
        return
    usuario.es_propietario_local = True
    usuario.save(update_fields=["es_propietario_local"])


def _propietario_marcado(Usuario):
    return (
        Usuario.objects.filter(is_active=True, es_propietario_local=True)
        .order_by("id")
        .first()
    )


def obtener_propietario_local():
    """Resuelve el propietario local sin crear ni elevar cuentas.

    Devuelve ``None`` cuando la autenticación está activa, cuando no existe
    una cuenta activa o cuando hay varias cuentas ambiguas y ninguna está
    marcada explícitamente como propietaria. En este último caso el perfil
    sigue siendo legible, pero las escrituras quedan bloqueadas hasta que el
    propietario resuelva la ambigüedad; nunca se elige al azar una cuenta.
    """
    if not getattr(settings, "AUTH_DISABLED", False):
        return None

    Usuario = get_user_model()
    propietario = _propietario_marcado(Usuario)
    if propietario is not None:
        return propietario

    # El nombre reservado es una identificación explícita heredada de las
    # primeras versiones del perfil local; solo se acepta esa cuenta concreta.
    heredado = Usuario.objects.filter(
        is_active=True, username=USERNAME_PROPIETARIO_LOCAL
    ).first()
    if heredado is not None:
        return heredado

    activos = list(
        Usuario.objects.filter(is_active=True).order_by("id").values_list("id", flat=True)[:2]
    )
    if len(activos) == 1:
        # Compatibilidad con perfiles creados antes de existir la marca
        # explícita: solo hay una cuenta activa y no hay ambigüedad.
        return Usuario.objects.get(pk=activos[0])
    return None


def asegurar_propietario_local():
    """Devuelve el propietario local, creándolo una sola vez si falta.

    Es idempotente y seguro ante dos procesos concurrentes: el nombre de
    usuario es único y, si otra ejecución gana la carrera, se recupera la fila
    existente. No modifica contraseñas ni cuentas ajenas.
    """
    if not getattr(settings, "AUTH_DISABLED", False):
        return None

    Usuario = get_user_model()
    usuario = _propietario_marcado(Usuario)
    if usuario is None:
        usuario = obtener_propietario_local()
        if usuario is None:
            activos = list(
                Usuario.objects.filter(is_active=True)
                .order_by("id")
                .values_list("id", flat=True)[:2]
            )
            if len(activos) > 1:
                logger.warning(
                    "Perfil local ambiguo: hay varias cuentas activas y ninguna "
                    "marcada como propietario local. No se elevará ninguna cuenta."
                )
                _marcar_configuracion_inicial()
                return None

    if usuario is not None:
        _marcar_como_propietario(usuario)
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
            usuario.es_propietario_local = True
            usuario.is_staff = True
            usuario.save(
                update_fields=[
                    "fecha_configuracion_inicial",
                    "es_propietario_local",
                    "is_staff",
                ]
            )
            registrar_evento(
                "perfil_local_inicializado",
                usuario=usuario,
                descripcion=(
                    "Propietario local creado para el modo sin autenticación. "
                    "No se establecieron credenciales de acceso."
                ),
            )
    except IntegrityError:
        usuario = _propietario_marcado(Usuario)
        if usuario is None:
            usuario = obtener_propietario_local()
        if usuario is None:
            raise

    _marcar_como_propietario(usuario)
    _asegurar_permiso_editorial(usuario)
    _marcar_configuracion_inicial()
    logger.info("Propietario local disponible: %s", usuario.pk)
    return usuario


def _asegurar_permiso_editorial(usuario) -> None:
    """Habilita el flujo editorial solo para el propietario local explícito.

    ``is_staff`` no activa autenticación ni sesiones: solo habilita las
    transiciones editoriales auditadas del modo monousuario. Una cuenta
    ordinaria o una cuenta de un perfil restaurado no se eleva por el mero
    hecho de existir.
    """
    if not getattr(usuario, "es_propietario_local", False):
        logger.warning(
            "Se intentó habilitar permisos editoriales sobre una cuenta que no "
            "está marcada como propietario local (pk=%s); no se modificó.",
            getattr(usuario, "pk", None),
        )
        return
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
