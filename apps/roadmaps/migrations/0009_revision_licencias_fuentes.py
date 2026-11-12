# Revisión auditable de licencias y uso declarado de fuentes.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0008_auditoria_envio_revision"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="fuenteconocimiento",
            name="estado_revision_licencia",
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
                verbose_name="estado de revisión de licencia",
            ),
        ),
        migrations.AddField(
            model_name="fuenteconocimiento",
            name="evidencia_licencia",
            field=models.URLField(blank=True, max_length=1000, verbose_name="evidencia de revisión de licencia"),
        ),
        migrations.AddField(
            model_name="fuenteconocimiento",
            name="alcance_licencia",
            field=models.TextField(blank=True, verbose_name="alcance autorizado"),
        ),
        migrations.AddField(
            model_name="fuenteconocimiento",
            name="nota_revision_licencia",
            field=models.TextField(blank=True, verbose_name="decisión editorial de licencia"),
        ),
        migrations.AddField(
            model_name="fuenteconocimiento",
            name="revisada_por",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="fuentes_licencia_revisadas",
                to=settings.AUTH_USER_MODEL,
                verbose_name="licencia revisada por",
            ),
        ),
        migrations.AddField(
            model_name="fuenteconocimiento",
            name="revisada_en",
            field=models.DateTimeField(blank=True, null=True, verbose_name="licencia revisada el"),
        ),
        migrations.AddField(
            model_name="referenciafuentecontenido",
            name="uso_declarado",
            field=models.CharField(
                choices=[
                    ("original", "Contenido original de CodeGuard"),
                    ("cita_breve", "Cita breve atribuida"),
                    ("adaptacion", "Adaptación de la fuente"),
                    ("reproduccion", "Reproducción de material"),
                ],
                default="original",
                max_length=16,
                verbose_name="uso declarado de la fuente",
            ),
        ),
    ]
