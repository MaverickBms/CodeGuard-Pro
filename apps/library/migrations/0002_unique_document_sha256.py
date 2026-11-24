"""Impide duplicados de contenido PDF incluso bajo concurrencia.

La comprobación de duplicados en la vista mejora el mensaje al usuario, pero
solo una restricción de base de datos puede cerrar la carrera entre procesos.
Los registros históricos sin SHA-256 quedan fuera de la restricción.
"""

from django.db import migrations, models
from django.db.models import Count


def comprobar_hashes_duplicados(apps, schema_editor):
    Documento = apps.get_model("library", "DocumentoBiblioteca")
    alias = schema_editor.connection.alias
    duplicados = list(
        Documento.objects.using(alias).exclude(sha256="")
        .values("sha256")
        .annotate(total=Count("id"))
        .filter(total__gt=1)
        .order_by("-total")[:5]
    )
    if duplicados:
        ejemplos = ", ".join(
            f"{fila['sha256'][:12]}… ({fila['total']} registros)"
            for fila in duplicados
        )
        raise RuntimeError(
            "No se puede activar la unicidad SHA-256 de la biblioteca porque "
            f"hay documentos duplicados históricos: {ejemplos}. "
            "Conserva los archivos y resuelve esos registros antes de migrar."
        )


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_biblioteca_documental"),
    ]

    operations = [
        migrations.RunPython(
            comprobar_hashes_duplicados,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RemoveIndex(
            model_name="documentobiblioteca",
            name="library_doc_sha256_7c5c9d_idx",
        ),
        migrations.AddConstraint(
            model_name="documentobiblioteca",
            constraint=models.UniqueConstraint(
                fields=("sha256",),
                condition=models.Q(("sha256__gt", "")),
                name="library_unique_document_sha256",
            ),
        ),
    ]
