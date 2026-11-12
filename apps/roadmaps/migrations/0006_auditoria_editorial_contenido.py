# Metadatos de revisión y publicación editorial.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0005_fuentes_y_versiones_contenido"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="versioncontenidoleccion",
            name="revisada_por",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="versiones_contenido_revisadas",
                to=settings.AUTH_USER_MODEL,
                verbose_name="revisada por",
            ),
        ),
        migrations.AddField(
            model_name="versioncontenidoleccion",
            name="publicada_por",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="versiones_contenido_publicadas",
                to=settings.AUTH_USER_MODEL,
                verbose_name="publicada por",
            ),
        ),
    ]
