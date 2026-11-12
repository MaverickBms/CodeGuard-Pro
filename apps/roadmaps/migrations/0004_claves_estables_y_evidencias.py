# Identificadores portables para el contenido y protección de evidencias académicas.
import uuid

import django.db.models.deletion
from django.db import migrations, models


def asignar_claves_contenido(apps, schema_editor):
    """Asigna una identidad UUID permanente a cada recurso preexistente."""
    alias = schema_editor.connection.alias
    for nombre in ("Leccion", "EjemploLeccion", "EjercicioLeccion"):
        modelo = apps.get_model("roadmaps", nombre)
        for recurso in modelo.objects.using(alias).filter(clave_contenido__isnull=True).iterator():
            recurso.clave_contenido = uuid.uuid4()
            recurso.save(using=alias, update_fields=["clave_contenido"])


class Migration(migrations.Migration):
    dependencies = [("roadmaps", "0003_intentos_y_evaluacion")]

    operations = [
        migrations.AddField(
            model_name="leccion", name="clave_contenido",
            field=models.UUIDField(null=True, editable=False, verbose_name="clave estable de contenido"),
        ),
        migrations.AddField(
            model_name="ejemploleccion", name="clave_contenido",
            field=models.UUIDField(null=True, editable=False, verbose_name="clave estable de contenido"),
        ),
        migrations.AddField(
            model_name="ejercicioleccion", name="clave_contenido",
            field=models.UUIDField(null=True, editable=False, verbose_name="clave estable de contenido"),
        ),
        migrations.RunPython(asignar_claves_contenido, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="leccion", name="clave_contenido",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="clave estable de contenido"),
        ),
        migrations.AlterField(
            model_name="ejemploleccion", name="clave_contenido",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="clave estable de contenido"),
        ),
        migrations.AlterField(
            model_name="ejercicioleccion", name="clave_contenido",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="clave estable de contenido"),
        ),
        migrations.AlterField(
            model_name="configuracionevaluacion", name="ejercicio",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="configuraciones_evaluacion", to="roadmaps.ejercicioleccion", verbose_name="ejercicio"),
        ),
        migrations.AlterField(
            model_name="intentoejercicio", name="ejercicio",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="intentos", to="roadmaps.ejercicioleccion", verbose_name="ejercicio"),
        ),
        migrations.AlterField(
            model_name="intentoejercicio", name="configuracion_evaluacion",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="intentos", to="roadmaps.configuracionevaluacion", verbose_name="configuración aplicada"),
        ),
    ]
