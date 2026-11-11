# Generated for the interactive learning core.
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roadmaps", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContenidoLeccion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("objetivos_aprendizaje", models.TextField(blank=True, verbose_name="objetivos de aprendizaje")),
                ("teoria_tecnica", models.TextField(blank=True, help_text="Explicación rigurosa del concepto, terminología y fundamentos.", verbose_name="teoría técnica")),
                ("explicacion_sencilla", models.TextField(blank=True, help_text="Explicación clara, gradual y sin asumir conocimientos no presentados.", verbose_name="explicación sencilla")),
                ("notas", models.TextField(blank=True, verbose_name="notas complementarias")),
                ("publicado", models.BooleanField(default=False, verbose_name="publicado")),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("actualizado_en", models.DateTimeField(auto_now=True)),
                ("leccion", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="contenido", to="roadmaps.leccion", verbose_name="lección")),
            ],
            options={"verbose_name": "contenido de lección", "verbose_name_plural": "contenidos de lecciones"},
        ),
        migrations.CreateModel(
            name="EjemploLeccion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=180, verbose_name="título")),
                ("contexto", models.TextField(blank=True, verbose_name="contexto")),
                ("lenguaje", models.CharField(blank=True, max_length=40, verbose_name="lenguaje")),
                ("codigo", models.TextField(blank=True, verbose_name="código")),
                ("salida_esperada", models.TextField(blank=True, verbose_name="salida esperada")),
                ("explicacion", models.TextField(blank=True, verbose_name="explicación paso a paso")),
                ("orden", models.PositiveSmallIntegerField(default=0, verbose_name="orden")),
                ("publicado", models.BooleanField(default=True, verbose_name="publicado")),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("actualizado_en", models.DateTimeField(auto_now=True)),
                ("leccion", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="ejemplos", to="roadmaps.leccion", verbose_name="lección")),
            ],
            options={"verbose_name": "ejemplo de lección", "verbose_name_plural": "ejemplos de lección", "ordering": ["orden", "id"]},
        ),
        migrations.CreateModel(
            name="EjercicioLeccion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=180, verbose_name="título")),
                ("enunciado", models.TextField(verbose_name="enunciado")),
                ("instrucciones", models.TextField(blank=True, verbose_name="instrucciones")),
                ("lenguaje", models.CharField(blank=True, max_length=40, verbose_name="lenguaje")),
                ("nivel", models.CharField(choices=[("basico", "Básico"), ("intermedio", "Intermedio"), ("avanzado", "Avanzado")], default="basico", max_length=16, verbose_name="nivel")),
                ("codigo_inicial", models.TextField(blank=True, verbose_name="código inicial")),
                ("pista_1", models.TextField(blank=True, verbose_name="pista 1")),
                ("pista_2", models.TextField(blank=True, verbose_name="pista 2")),
                ("pista_3", models.TextField(blank=True, verbose_name="pista 3")),
                ("obligatorio", models.BooleanField(default=True, verbose_name="obligatorio")),
                ("orden", models.PositiveSmallIntegerField(default=0, verbose_name="orden")),
                ("publicado", models.BooleanField(default=True, verbose_name="publicado")),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("actualizado_en", models.DateTimeField(auto_now=True)),
                ("leccion", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="ejercicios", to="roadmaps.leccion", verbose_name="lección")),
            ],
            options={"verbose_name": "ejercicio de lección", "verbose_name_plural": "ejercicios de lección", "ordering": ["orden", "id"]},
        ),
    ]
