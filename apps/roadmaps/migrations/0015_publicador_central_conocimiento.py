# Registra secuencias y publicaciones inmutables del distribuidor central.
from django.db import migrations, models


def crear_contadores_iniciales(apps, schema_editor):
    Secuencia = apps.get_model("roadmaps", "SecuenciaPublicacionConocimiento")
    Secuencia.objects.get_or_create(channel="stable", defaults={"siguiente": 1})
    Secuencia.objects.get_or_create(channel="beta", defaults={"siguiente": 1})


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0014_contenido_activo_y_snapshot_intentos"),
    ]

    operations = [
        migrations.CreateModel(
            name="SecuenciaPublicacionConocimiento",
            fields=[
                ("channel", models.CharField(
                    choices=[("stable", "Stable"), ("beta", "Beta")],
                    max_length=16, primary_key=True, serialize=False,
                )),
                ("siguiente", models.PositiveBigIntegerField(default=1)),
            ],
            options={
                "verbose_name": "secuencia de publicación de conocimiento",
                "verbose_name_plural": "secuencias de publicación de conocimiento",
            },
        ),
        migrations.CreateModel(
            name="PublicacionPaqueteConocimiento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("package_id", models.UUIDField(unique=True)),
                ("package_version", models.CharField(max_length=40)),
                ("channel", models.CharField(choices=[("stable", "Stable"), ("beta", "Beta")], max_length=16)),
                ("sequence", models.PositiveBigIntegerField()),
                ("content_schema_version", models.PositiveSmallIntegerField(default=1)),
                ("package_sha256", models.CharField(max_length=64)),
                ("manifest_sha256", models.CharField(max_length=64)),
                ("signature_key_id", models.CharField(max_length=80)),
                ("package_url", models.URLField(max_length=2048)),
                ("package_filename", models.CharField(max_length=180)),
                ("manifest_filename", models.CharField(max_length=180)),
                ("signature_filename", models.CharField(max_length=180)),
                ("published_at", models.DateTimeField()),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "publicación de paquete de conocimiento",
                "verbose_name_plural": "publicaciones de paquetes de conocimiento",
                "ordering": ["channel", "-sequence"],
            },
        ),
        migrations.RunPython(crear_contadores_iniciales, migrations.RunPython.noop),
        migrations.AddConstraint(
            model_name="publicacionpaqueteconocimiento",
            constraint=models.UniqueConstraint(
                fields=("channel", "sequence"),
                name="publicacion_secuencia_canal_unica",
            ),
        ),
    ]
