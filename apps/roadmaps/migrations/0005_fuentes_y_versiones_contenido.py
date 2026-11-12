# Catálogo de fuentes y snapshots versionados de contenido académico.
import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("roadmaps", "0004_claves_estables_y_evidencias")]

    operations = [
        migrations.CreateModel(
            name="FuenteConocimiento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("clave", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("publicador", models.CharField(max_length=180, verbose_name="publicador")),
                ("titulo", models.CharField(max_length=240, verbose_name="título de la fuente")),
                ("url_canonica", models.URLField(max_length=1000, verbose_name="URL canónica")),
                ("edicion", models.CharField(blank=True, max_length=100, verbose_name="edición o versión")),
                ("identificador_licencia", models.CharField(blank=True, max_length=120, verbose_name="identificador de licencia")),
                ("url_licencia", models.URLField(blank=True, max_length=1000, verbose_name="URL de licencia")),
                ("consultada_en", models.DateTimeField(blank=True, null=True, verbose_name="consultada el")),
                ("activa", models.BooleanField(default=True, verbose_name="fuente activa")),
                ("notas", models.TextField(blank=True, verbose_name="notas editoriales")),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name": "fuente de conocimiento", "verbose_name_plural": "fuentes de conocimiento", "ordering": ["publicador", "titulo"]},
        ),
        migrations.CreateModel(
            name="VersionContenidoLeccion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("clave", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("numero_version", models.PositiveIntegerField(verbose_name="número de versión")),
                ("esquema_version", models.PositiveSmallIntegerField(default=1, verbose_name="versión del esquema")),
                ("estado", models.CharField(choices=[("borrador", "Borrador"), ("revision", "En revisión"), ("aprobada", "Aprobada"), ("publicada", "Publicada"), ("sustituida", "Sustituida"), ("retirada", "Retirada")], default="borrador", max_length=12)),
                ("snapshot", models.JSONField(verbose_name="snapshot académico")),
                ("sha256", models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(r"^[0-9a-f]{64}$", "Debe ser un SHA-256 hexadecimal en minúsculas.")], verbose_name="SHA-256 del snapshot")),
                ("resumen_cambios", models.TextField(blank=True, verbose_name="resumen de cambios")),
                ("motivo_retiro", models.TextField(blank=True, verbose_name="motivo de retiro")),
                ("revisada_en", models.DateTimeField(blank=True, null=True, verbose_name="revisada el")),
                ("publicada_en", models.DateTimeField(blank=True, null=True, verbose_name="publicada el")),
                ("creada_en", models.DateTimeField(auto_now_add=True)),
                ("leccion", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="versiones_contenido", to="roadmaps.leccion", verbose_name="lección")),
                ("fuentes", models.ManyToManyField(blank=True, related_name="versiones", through="roadmaps.ReferenciaFuenteContenido", to="roadmaps.fuenteconocimiento")),
            ],
            options={"verbose_name": "versión de contenido de lección", "verbose_name_plural": "versiones de contenido de lección", "ordering": ["leccion_id", "-numero_version"]},
        ),
        migrations.CreateModel(
            name="ReferenciaFuenteContenido",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("rol", models.CharField(choices=[("principal", "Fuente principal"), ("complementaria", "Fuente complementaria"), ("normativa", "Especificación o norma")], default="principal", max_length=16)),
                ("localizador", models.CharField(blank=True, max_length=500, verbose_name="sección o localizador")),
                ("nota_atribucion", models.TextField(blank=True, verbose_name="nota de atribución")),
                ("fuente", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="referencias_contenido", to="roadmaps.fuenteconocimiento")),
                ("version", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="referencias", to="roadmaps.versioncontenidoleccion")),
            ],
            options={"verbose_name": "referencia de fuente de contenido", "verbose_name_plural": "referencias de fuentes de contenido"},
        ),
        migrations.AddConstraint(
            model_name="fuenteconocimiento",
            constraint=models.UniqueConstraint(fields=("url_canonica", "edicion"), name="fuente_unica_url_edicion"),
        ),
        migrations.AddConstraint(
            model_name="versioncontenidoleccion",
            constraint=models.UniqueConstraint(fields=("leccion", "numero_version"), name="contenido_version_unica_leccion"),
        ),
        migrations.AddConstraint(
            model_name="versioncontenidoleccion",
            constraint=models.UniqueConstraint(condition=models.Q(("estado", "publicada")), fields=("leccion",), name="contenido_una_publicada_por_leccion"),
        ),
        migrations.AddIndex(
            model_name="versioncontenidoleccion",
            index=models.Index(fields=["estado", "publicada_en"], name="contenido_estado_pub_idx"),
        ),
        migrations.AddConstraint(
            model_name="referenciafuentecontenido",
            constraint=models.UniqueConstraint(fields=("version", "fuente"), name="referencia_fuente_unica_version"),
        ),
    ]
