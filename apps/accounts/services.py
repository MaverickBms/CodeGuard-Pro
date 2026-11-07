"""Servicios del módulo de identidad y acceso.

Gestiona la creación del usuario inicial, la frase de rescate de alta entropía
y la validación de credenciales. Toda la lógica sensible vive aquí, no en las
vistas.
"""

import secrets
import string

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password
from django.db import transaction
from django.utils import timezone

from apps.accounts.models import FraseRescate, Usuario
from apps.audit.services import registrar_evento

# Alfabeto seguro para la frase de rescate: mayúsculas, minúsculas, dígitos y
# símbolos. No se incluyen caracteres ambiguos (0, O, 1, l) para evitar errores
# de lectura por parte del usuario.
_RESCATE_ALFABETO = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"


def generar_frase_rescate(longitud: int = 32) -> str:
    """Genera una frase de rescate de alta entropía (≥128 bits).

    Con 32 caracteres sobre un alfabeto de ~80 símbolos se obtienen
    aproximadamente 32 * log2(80) ≈ 201 bits de entropía, muy por encima de
    los 128 bits exigidos por RF-004 y RS-003.
    """
    return "".join(secrets.choice(_RESCATE_ALFABETO) for _ in range(longitud))


def crear_usuario_inicial(
    username: str,
    password: str,
    email: str = "",
    *,
    ip: str | None = None,
    user_agent: str = "",
) -> Usuario:
    """Crea el usuario inicial y su frase de rescate.

    Devuelve el usuario creado. La frase de rescate generada se devuelve por
    separado al llamante para que se muestre una sola vez (RF-004).
    """
    if Usuario.objects.exists():
        raise RuntimeError("El usuario inicial ya existe.")

    usuario = Usuario.objects.create_user(
        username=username,
        email=email,
        password=password,
    )
    usuario.fecha_configuracion_inicial = timezone.now()
    usuario.save(update_fields=["fecha_configuracion_inicial"])

    frase_texto = generar_frase_rescate()
    FraseRescate.objects.create(
        usuario=usuario,
        hash_argon2=make_password(frase_texto),
    )

    registrar_evento(
        "setup_inicial",
        usuario=usuario,
        descripcion="Configuración inicial completada: usuario y frase de rescate creados.",
        ip=ip,
        user_agent=user_agent,
    )
    return usuario, frase_texto


def verificar_frase_rescate(usuario: Usuario, frase_texto: str) -> bool:
    """Valida una frase de rescate contra su hash Argon2 sin consumirla.

    La invalidación (marcado de uso) se delega en la operación de cambio de
    contraseña para que una frase solo se consuma cuando el nuevo contraseña se
    establezca correctamente (RF-004 / CG-003).
    """
    try:
        frase = FraseRescate.objects.filter(usuario=usuario, usada=False).latest("creada_en")
    except FraseRescate.DoesNotExist:
        return False

    return bool(frase_texto) and check_password(frase_texto, frase.hash_argon2)


def _invalidar_frase_rescate(frase: FraseRescate) -> None:
    """Marca la frase de rescate como usada e inválida (un solo uso, RF-004)."""
    frase.usada = True
    frase.fecha_uso = timezone.now()
    frase.save(update_fields=["usada", "fecha_uso"])


def cambiar_contrasena_por_frase(
    usuario: Usuario,
    frase_texto: str,
    nueva_password: str,
) -> bool:
    """Cambio de contraseña maestra tras validar la frase de rescate.

    Ejecuta el flujo completo de forma atómica: valida la frase, establece la
    nueva contraseña (Argon2) e invalida la frase solo si todo el proceso tuvo
    éxito. Si la frase es inválida o ya fue usada, no se modifica nada (la frase
    no se consume y la contraseña no cambia).
    """
    with transaction.atomic():
        try:
            frase = FraseRescate.objects.filter(usuario=usuario, usada=False).latest("creada_en")
        except FraseRescate.DoesNotExist:
            return False

        if not check_password(frase_texto, frase.hash_argon2):
            return False

        usuario.set_password(nueva_password)
        usuario.save(update_fields=["password"])

        _invalidar_frase_rescate(frase)

        registrar_evento(
            "uso_frase_rescate",
            usuario=usuario,
            descripcion="Frase de rescate utilizada e invalidada (un solo uso).",
            ip=None,
            user_agent="",
        )

        registrar_evento(
            "cambio_contraseña",
            usuario=usuario,
            descripcion="Contraseña maestra cambiada mediante frase de rescate.",
            ip=None,
            user_agent="",
        )
    return True


def autenticar_usuario(username: str, password: str) -> Usuario | None:
    """Autentica al usuario con contraseña maestra (Argon2)."""
    return authenticate(username=username, password=password)
