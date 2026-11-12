# Registro de quién envía una versión al proceso de revisión.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0007_auditoria_retiro_contenido"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="versioncontenidoleccion",
            name="enviada_por",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="versiones_contenido_enviadas",
                to=settings.AUTH_USER_MODEL,
                verbose_name="enviada por",
            ),
        ),
        migrations.AddField(
            model_name="versioncontenidoleccion",
            name="enviada_en",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="enviada a revisión el",
            ),
        ),
    ]
