"""Garantiza referencias idempotentes únicas en transacciones de monedas."""

from django.db import migrations, models
from django.db.models import Count, Q


def comprobar_referencias_existentes(apps, schema_editor):
    TransaccionMoneda = apps.get_model("gamification", "TransaccionMoneda")
    duplicada = (
        TransaccionMoneda.objects.exclude(referencia="")
        .values("usuario_id", "tipo", "referencia")
        .annotate(total=Count("id"))
        .filter(total__gt=1)
        .first()
    )
    if duplicada:
        raise RuntimeError(
            "No se puede aplicar gamification.0004_unique_transaction_reference: "
            "hay referencias de transacción duplicadas. "
            f"Usuario={duplicada['usuario_id']}, tipo={duplicada['tipo']}, "
            f"referencia={duplicada['referencia']!r}. "
            "Conservar una transacción por referencia y reconciliar los saldos "
            "antes de volver a ejecutar la migración."
        )


class Migration(migrations.Migration):
    dependencies = [("gamification", "0003_misiones_rachas")]

    operations = [
        migrations.RunPython(comprobar_referencias_existentes, migrations.RunPython.noop),
        migrations.AddConstraint(
            model_name="transaccionmoneda",
            constraint=models.UniqueConstraint(
                fields=("usuario", "tipo", "referencia"),
                condition=~Q(referencia=""),
                name="gamif_tx_ref_unica",
            ),
        ),
    ]
