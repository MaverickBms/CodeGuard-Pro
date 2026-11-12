# Impide que un canal tenga más de un paquete activo.
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0012_registro_paquetes_sincronizacion"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="paqueteconocimientoinstalado",
            constraint=models.UniqueConstraint(
                condition=models.Q(("estado", "activo")),
                fields=("channel",),
                name="paquete_un_activo_por_canal",
            ),
        ),
    ]
