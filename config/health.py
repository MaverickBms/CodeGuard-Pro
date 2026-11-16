"""Endpoint de disponibilidad local para Electron."""

from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from apps.roadmaps.models import Roadmap


@require_GET
def healthz(_request):
    """Confirma que DB, migraciones y catálogo académico están listos."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        executor = MigrationExecutor(connection)
        pending_migrations = executor.migration_plan(
            executor.loader.graph.leaf_nodes()
        )
        if pending_migrations:
            return JsonResponse(
                {"status": "starting", "database": "ok", "migrations": "pending", "roadmap": "unknown"},
                status=503,
            )

        if not Roadmap.objects.filter(activo=True).exists():
            return JsonResponse(
                {"status": "starting", "database": "ok", "migrations": "ok", "roadmap": "missing"},
                status=503,
            )

        return JsonResponse(
            {"status": "ok", "database": "ok", "migrations": "ok", "roadmap": "ok"}
        )
    except Exception:
        # No exponer rutas, SQL, nombres de tablas ni detalles internos al renderer.
        return JsonResponse(
            {"status": "starting", "database": "unavailable", "migrations": "unknown", "roadmap": "unknown"},
            status=503,
        )
