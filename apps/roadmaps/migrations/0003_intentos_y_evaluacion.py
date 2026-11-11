# Generated for deterministic exercise attempts and evaluation.
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("roadmaps", "0002_contenido_leccion"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConfiguracionEvaluacion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tipo", models.CharField(choices=[("respuesta_exacta", "Respuesta de texto exacta"), ("codigo_contiene", "Comprobación estática de fragmentos de código")], max_length=30, verbose_name="tipo de evaluador")),
                ("configuracion", models.JSONField(blank=True, default=dict, help_text="No se envía al navegador del estudiante.", verbose_name="configuración privada del evaluador")),
                ("version", models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name="versión del evaluador")),
                ("activo", models.BooleanField(default=True, verbose_name="activo")),
                ("actualizado_en", models.DateTimeField(auto_now=True)),
                ("ejercicio", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="configuracion_evaluacion", to="roadmaps.ejercicioleccion")),
            ],
            options={"verbose_name": "configuración de evaluación", "verbose_name_plural": "configuraciones de evaluación"},
        ),
        migrations.CreateModel(
            name="IntentoEjercicio",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("respuesta", models.TextField(verbose_name="respuesta enviada")),
                ("resultado", models.CharField(choices=[("pendiente_revision", "Pendiente de revisión"), ("aprobado", "Aprobado"), ("no_aprobado", "Aún no aprobado")], default="pendiente_revision", max_length=24, verbose_name="resultado")),
                ("puntuacion", models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name="puntuación")),
                ("retroalimentacion", models.TextField(blank=True, verbose_name="retroalimentación")),
                ("detalles", models.JSONField(blank=True, default=dict, verbose_name="detalles del resultado")),
                ("version_evaluacion", models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="versión del evaluador")),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("evaluado_en", models.DateTimeField(blank=True, null=True)),
                ("ejercicio", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="intentos", to="roadmaps.ejercicioleccion")),
                ("usuario", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="intentos_ejercicios", to=settings.AUTH_USER_MODEL, verbose_name="usuario")),
            ],
            options={"verbose_name": "intento de ejercicio", "verbose_name_plural": "intentos de ejercicios", "ordering": ["-creado_en", "-id"]},
        ),
        migrations.AddIndex(
            model_name="intentoejercicio",
            index=models.Index(fields=["usuario", "ejercicio", "-creado_en"], name="intento_user_ejercicio_idx"),
        ),
        migrations.AddConstraint(
            model_name="intentoejercicio",
            constraint=models.CheckConstraint(
                condition=models.Q(puntuacion__isnull=True) | models.Q(puntuacion__gte=0, puntuacion__lte=100),
                name="intento_puntuacion_0_100",
            ),
        ),
    ]
