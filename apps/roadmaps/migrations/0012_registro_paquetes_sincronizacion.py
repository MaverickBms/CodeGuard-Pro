# Registra los paquetes firmados y el estado local de sincronización por canal.
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("roadmaps", "0011_autoria_version_contenido"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaqueteConocimientoInstalado",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("package_id", models.UUIDField(unique=True, verbose_name="UUID del paquete")),
                ("package_version", models.CharField(max_length=40, verbose_name="versión del paquete")),
                ("channel", models.CharField(choices=[("stable", "Stable"), ("beta", "Beta")], max_length=16, verbose_name="canal")),
                ("sequence", models.PositiveBigIntegerField(verbose_name="secuencia monotónica")),
                ("content_schema_version", models.PositiveSmallIntegerField(verbose_name="versión del esquema")),
                ("sha256", models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(r"^[0-9a-f]{64}$", "Debe ser un SHA-256 hexadecimal en minúsculas.")], verbose_name="SHA-256 del ZIP")),
                ("manifest_sha256", models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(r"^[0-9a-f]{64}$", "Debe ser un SHA-256 hexadecimal en minúsculas.")], verbose_name="SHA-256 del manifiesto")),
                ("signature_key_id", models.CharField(max_length=80, verbose_name="identificador de clave de firma")),
                ("published_at", models.DateTimeField(verbose_name="publicado el")),
                ("installed_at", models.DateTimeField(blank=True, null=True, verbose_name="instalado el")),
                ("estado", models.CharField(choices=[("descargado", "Descargado"), ("verificado", "Verificado"), ("activo", "Activo"), ("rechazado", "Rechazado"), ("sustituido", "Sustituido")], default="descargado", max_length=16)),
                ("error_code", models.CharField(blank=True, max_length=80, verbose_name="código de error")),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "paquete de conocimiento instalado",
                "verbose_name_plural": "paquetes de conocimiento instalados",
                "ordering": ["channel", "-sequence"],
            },
        ),
        migrations.AddConstraint(
            model_name="paqueteconocimientoinstalado",
            constraint=models.UniqueConstraint(fields=("channel", "sequence"), name="paquete_secuencia_canal_unica"),
        ),
        migrations.AddIndex(
            model_name="paqueteconocimientoinstalado",
            index=models.Index(fields=["channel", "-sequence"], name="paquete_canal_seq_idx"),
        ),
        migrations.CreateModel(
            name="EstadoSincronizacion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("channel", models.CharField(choices=[("stable", "Stable"), ("beta", "Beta")], max_length=16, unique=True)),
                ("last_check_at", models.DateTimeField(blank=True, null=True, verbose_name="última comprobación")),
                ("last_success_at", models.DateTimeField(blank=True, null=True, verbose_name="última sincronización correcta")),
                ("manifest_etag", models.CharField(blank=True, max_length=255, verbose_name="ETag del manifiesto")),
                ("last_error_code", models.CharField(blank=True, max_length=80, verbose_name="último código de error")),
                ("next_check_after", models.DateTimeField(blank=True, null=True, verbose_name="próxima comprobación permitida")),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("active_package", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name="canales_activos", to="roadmaps.paqueteconocimientoinstalado", verbose_name="paquete activo")),
            ],
            options={
                "verbose_name": "estado de sincronización",
                "verbose_name_plural": "estados de sincronización",
            },
        ),
    ]
