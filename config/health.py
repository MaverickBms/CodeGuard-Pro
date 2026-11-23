"""Endpoint de disponibilidad local para Electron."""

from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from apps.roadmaps.models import Etapa, Leccion, Modulo, Roadmap

# Cachear solo el estado "migraciones OK": el executor es costoso y las
# migraciones no se aplican mientras el servidor está sirviendo. El roadmap
# se sigue comprobando para no reportar listo ante un perfil incompleto.
_MIGRATIONS_OK = False


def mark_ready() -> None:
    """Marca migraciones como listas tras un arranque verificado."""
    global _MIGRATIONS_OK
    _MIGRATIONS_OK = True


def reset_ready() -> None:
    """Uso en tests: limpia el caché de disponibilidad."""
    global _MIGRATIONS_OK
    _MIGRATIONS_OK = False


@require_GET
def healthz(_request):
    """Confirma que DB, migraciones y catálogo académico están listos."""
    global _MIGRATIONS_OK
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        if not _MIGRATIONS_OK:
            executor = MigrationExecutor(connection)
            pending_migrations = executor.migration_plan(
                executor.loader.graph.leaf_nodes()
            )
            if pending_migrations:
                return JsonResponse(
                    {
                        "status": "starting",
                        "database": "ok",
                        "migrations": "pending",
                        "roadmap": "unknown",
                    },
                    status=503,
                )
            _MIGRATIONS_OK = True

        roadmap = (
            Roadmap.objects.filter(activo=True).order_by("-actualizado_en").first()
        )
        if roadmap is None:
            return JsonResponse(
                {"status": "starting", "database": "ok", "migrations": "ok", "roadmap": "missing"},
                status=503,
            )

        # Un roadmap vacío no es un perfil operativo: Electron debe seguir
        # esperando (o mostrar el error de inicialización) en lugar de abrir
        # una interfaz sin etapas, módulos ni lecciones.
        if (
            not Etapa.objects.filter(roadmap=roadmap).exists()
            or not Modulo.objects.filter(etapa__roadmap=roadmap).exists()
            or not Leccion.objects.filter(modulo__etapa__roadmap=roadmap).exists()
        ):
            return JsonResponse(
                {"status": "starting", "database": "ok", "migrations": "ok", "roadmap": "incomplete"},
                status=503,
            )

        return JsonResponse(
            {"status": "ok", "database": "ok", "migrations": "ok", "roadmap": "ok"}
        )
    except Exception:
        _MIGRATIONS_OK = False
        # No exponer rutas, SQL, nombres de tablas ni detalles internos al renderer.
        return JsonResponse(
            {"status": "starting", "database": "unavailable", "migrations": "unknown", "roadmap": "unknown"},
            status=503,
        )
