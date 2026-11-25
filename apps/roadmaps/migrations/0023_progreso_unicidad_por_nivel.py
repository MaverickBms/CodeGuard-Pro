"""Enforce uniqueness for each nullable progress level."""

from django.db import migrations, models
from django.db.models import Count


def comprobar_progresos_duplicados(apps, schema_editor):
    Progreso = apps.get_model("roadmaps", "Progreso")
    manager = Progreso.objects.using(schema_editor.connection.alias)
    niveles = (
        (
            {"modulo__isnull": True, "leccion__isnull": True, "actividad__isnull": True},
            ("usuario_id", "etapa_id"),
            "etapa",
        ),
        (
            {"modulo__isnull": False, "leccion__isnull": True, "actividad__isnull": True},
            ("usuario_id", "modulo_id"),
            "módulo",
        ),
        (
            {"leccion__isnull": False, "actividad__isnull": True},
            ("usuario_id", "leccion_id"),
            "lección",
        ),
        (
            {"actividad__isnull": False},
            ("usuario_id", "actividad_id"),
            "actividad",
        ),
    )
    for filtros, campos, etiqueta in niveles:
        duplicados = (
            manager.filter(**filtros)
            .values(*campos)
            .annotate(total=Count("pk"))
            .filter(total__gt=1)
        )
        if duplicados.exists():
            raise RuntimeError(
                "No se puede aplicar la unicidad del progreso: existen registros "
                f"duplicados por {etiqueta}. No se ha eliminado ni modificado "
                "ningún dato. Resuelve los duplicados conservando el estado y "
                "la fecha más recientes y vuelve a ejecutar las migraciones."
            )


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0022_recursoaudiovisual_revision_pedagogica"),
    ]

    operations = [
        migrations.RunPython(
            comprobar_progresos_duplicados,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RemoveConstraint(
            model_name="progreso",
            name="progreso_unico_por_objetivo",
        ),
        migrations.AddConstraint(
            model_name="progreso",
            constraint=models.UniqueConstraint(
                fields=("usuario", "etapa"),
                condition=models.Q(
                    modulo__isnull=True,
                    leccion__isnull=True,
                    actividad__isnull=True,
                ),
                name="progreso_unico_etapa",
            ),
        ),
        migrations.AddConstraint(
            model_name="progreso",
            constraint=models.UniqueConstraint(
                fields=("usuario", "modulo"),
                condition=models.Q(
                    modulo__isnull=False,
                    leccion__isnull=True,
                    actividad__isnull=True,
                ),
                name="progreso_unico_modulo",
            ),
        ),
        migrations.AddConstraint(
            model_name="progreso",
            constraint=models.UniqueConstraint(
                fields=("usuario", "leccion"),
                condition=models.Q(
                    leccion__isnull=False,
                    actividad__isnull=True,
                ),
                name="progreso_unico_leccion",
            ),
        ),
        migrations.AddConstraint(
            model_name="progreso",
            constraint=models.UniqueConstraint(
                fields=("usuario", "actividad"),
                condition=models.Q(actividad__isnull=False),
                name="progreso_unico_actividad",
            ),
        ),
    ]
