"""Add the dashboard access event to the audit event choices."""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("audit", "0002_alter_auditlog_evento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auditlog",
            name="evento",
            field=models.CharField(
                choices=[
                    ("login_exitoso", "Inicio de sesión exitoso"),
                    ("login_fallido", "Inicio de sesión fallido"),
                    ("logout", "Cierre de sesión"),
                    ("logout_inactividad", "Cierre de sesión por inactividad"),
                    ("setup_inicial", "Configuración inicial completada"),
                    ("cambio_contraseña", "Cambio de contraseña"),
                    ("uso_frase_rescate", "Uso de frase de rescate"),
                    ("acceso_denegado", "Acceso denegado a vista protegida"),
                    ("acceso_panel", "Acceso al panel principal"),
                    ("backup_creado", "Backup creado"),
                    ("backup_restaurado", "Backup restaurado"),
                    ("error_importacion", "Error de importación de documento"),
                    ("roadmap_etapa_completada", "Etapa del roadmap completada"),
                    ("roadmap_etapa_reabierta", "Etapa del roadmap reabierta"),
                    ("roadmap_leccion_completada", "Lección del roadmap completada"),
                    ("roadmap_leccion_reabierta", "Lección del roadmap reabierta"),
                ],
                max_length=40,
                verbose_name="evento",
            ),
        ),
    ]
