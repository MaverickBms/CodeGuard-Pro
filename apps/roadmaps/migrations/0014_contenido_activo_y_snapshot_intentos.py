# Crea el puntero de contenido publicado y conserva la presentación histórica de intentos.
from django.db import migrations, models
import django.db.models.deletion


def conservar_evidencia_historica(apps, schema_editor):
    Intento = apps.get_model("roadmaps", "IntentoEjercicio")
    Version = apps.get_model("roadmaps", "VersionContenidoLeccion")
    Puntero = apps.get_model("roadmaps", "ContenidoLeccionActivo")

    ultimo_id = 0
    while True:
        lote = list(
            Intento.objects.filter(pk__gt=ultimo_id)
            .select_related("ejercicio")
            .order_by("pk")[:200]
        )
        if not lote:
            break
        for intento in lote:
            ejercicio = intento.ejercicio
            intento.snapshot_ejercicio = {
                "clave": str(ejercicio.clave_contenido),
                "titulo": ejercicio.titulo,
                "enunciado": ejercicio.enunciado,
                "instrucciones": ejercicio.instrucciones,
                "lenguaje": ejercicio.lenguaje,
                "nivel": ejercicio.nivel,
                "codigo_inicial": ejercicio.codigo_inicial,
                "obligatorio": ejercicio.obligatorio,
                "orden": ejercicio.orden,
                "origen": "migracion_historica",
            }
        Intento.objects.bulk_update(lote, ["snapshot_ejercicio"], batch_size=200)
        ultimo_id = lote[-1].pk

    for version in Version.objects.filter(estado="publicada").iterator():
        Puntero.objects.get_or_create(
            leccion_id=version.leccion_id,
            defaults={"version_id": version.pk},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0013_un_paquete_activo_por_canal"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContenidoLeccionActivo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("activado_en", models.DateTimeField(auto_now=True, verbose_name="activado el")),
                ("leccion", models.OneToOneField(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="contenido_activo",
                    to="roadmaps.leccion",
                    verbose_name="lección",
                )),
                ("version", models.OneToOneField(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="puntero_activo",
                    to="roadmaps.versioncontenidoleccion",
                    verbose_name="versión publicada activa",
                )),
            ],
            options={
                "verbose_name": "contenido activo de lección",
                "verbose_name_plural": "contenidos activos de lección",
            },
        ),
        migrations.AddField(
            model_name="intentoejercicio",
            name="version_contenido",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="intentos",
                to="roadmaps.versioncontenidoleccion",
                verbose_name="versión académica presentada",
            ),
        ),
        migrations.AddField(
            model_name="intentoejercicio",
            name="snapshot_ejercicio",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="Conserva el enunciado exacto aunque el contenido editable cambie.",
                verbose_name="snapshot del ejercicio presentado",
            ),
        ),
        migrations.RunPython(conservar_evidencia_historica, migrations.RunPython.noop),
    ]
