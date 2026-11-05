"""Servicios del módulo de auditoría.

Centraliza el registro de eventos de seguridad para evitar duplicar lógica en
las vistas y mantener la trazabilidad exigida por RF-005 y RS-014.
"""

from apps.audit.models import AuditLog


def registrar_evento(
    evento: str,
    *,
    usuario=None,
    descripcion: str = "",
    ip: str | None = None,
    user_agent: str = "",
) -> AuditLog:
    """Crea una entrada de auditoría y la devuelve."""
    return AuditLog.objects.create(
        usuario=usuario,
        evento=evento,
        descripcion=descripcion,
        ip=ip,
        user_agent=user_agent[:512],
    )
