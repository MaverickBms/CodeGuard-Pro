# Conserva snapshots y catálogos instalados por paquete, sin alterar el flujo editorial.
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0015_publicador_central_conocimiento"),
    ]

    operations = [
        migrations.AddField(
            model_name="paqueteconocimientoinstalado",
            name="artifact_storage_key",
            field=models.CharField(
                blank=True,
                default="",
                max_length=255,
                verbose_name="clave relativa del artefacto local",
            ),
        ),
        migrations.CreateModel(
            name="ContenidoLeccionPaquete",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("documento", models.JSONField()),
                ("sha256", models.CharField(max_length=64)),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("leccion", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="contenidos_paquete",
                    to="roadmaps.leccion",
                )),
                ("paquete", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="contenidos_leccion",
                    to="roadmaps.paqueteconocimientoinstalado",
                )),
            ],
            options={
                "verbose_name": "snapshot de lección instalado",
                "verbose_name_plural": "snapshots de lección instalados",
            },
        ),
        migrations.CreateModel(
            name="FuentePaqueteConocimiento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("source_uuid", models.UUIDField()),
                ("metadatos", models.JSONField()),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("paquete", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="fuentes_catalogo",
                    to="roadmaps.paqueteconocimientoinstalado",
                )),
            ],
            options={
                "verbose_name": "fuente de paquete de conocimiento",
                "verbose_name_plural": "fuentes de paquetes de conocimiento",
            },
        ),
        migrations.AddField(
            model_name="intentoejercicio",
            name="paquete_contenido",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="intentos",
                to="roadmaps.paqueteconocimientoinstalado",
                verbose_name="paquete académico presentado",
            ),
        ),
        migrations.AddConstraint(
            model_name="contenidoleccionpaquete",
            constraint=models.UniqueConstraint(
                fields=("paquete", "leccion"),
                name="contenido_paquete_leccion_unico",
            ),
        ),
        migrations.AddConstraint(
            model_name="fuentepaqueteconocimiento",
            constraint=models.UniqueConstraint(
                fields=("paquete", "source_uuid"),
                name="fuente_uuid_paquete_unica",
            ),
        ),
    ]
