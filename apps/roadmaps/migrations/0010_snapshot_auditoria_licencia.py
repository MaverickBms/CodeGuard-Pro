# Conserva una instantánea de la decisión de licencia al iniciar revisión editorial.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0009_revision_licencias_fuentes"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="referenciafuentecontenido",
            name="estado_licencia_snapshot",
            field=models.CharField(
                choices=[
                    ("pendiente", "Pendiente de revisión"),
                    ("compatible", "Reutilización compatible"),
                    ("solo_referencia", "Solo consulta; contenido original"),
                    ("requiere_permiso", "Requiere permiso"),
                    ("no_reutilizable", "No reutilizable"),
                ],
                default="pendiente",
                max_length=20,
                verbose_name="estado de licencia al enviar a revisión",
            ),
        ),
        migrations.AddField(
            model_name="referenciafuentecontenido",
            name="evidencia_licencia_snapshot",
            field=models.URLField(blank=True, max_length=1000, verbose_name="evidencia de licencia al enviar a revisión"),
        ),
        migrations.AddField(
            model_name="referenciafuentecontenido",
            name="alcance_licencia_snapshot",
            field=models.TextField(blank=True, verbose_name="alcance de licencia al enviar a revisión"),
        ),
        migrations.AddField(
            model_name="referenciafuentecontenido",
            name="nota_licencia_snapshot",
            field=models.TextField(blank=True, verbose_name="decisión de licencia al enviar a revisión"),
        ),
        migrations.AddField(
            model_name="referenciafuentecontenido",
            name="licencia_revisada_por_snapshot",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="referencias_licencia_congeladas",
                to=settings.AUTH_USER_MODEL,
                verbose_name="editor de licencia al enviar a revisión",
            ),
        ),
        migrations.AddField(
            model_name="referenciafuentecontenido",
            name="licencia_revisada_en_snapshot",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="fecha de revisión de licencia al enviar a revisión",
            ),
        ),
    ]
