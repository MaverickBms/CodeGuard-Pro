"""Registra una fuente documental para el flujo editorial de conocimiento."""

from urllib.parse import urlsplit

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError, transaction
from django.utils import timezone

from apps.roadmaps.models import FuenteConocimiento


class Command(BaseCommand):
    help = (
        "Registra una fuente documental. El registro no verifica por sí mismo "
        "su autoridad, vigencia ni condiciones de reutilización."
    )

    def add_arguments(self, parser):
        parser.add_argument("--publicador", required=True, help="Organización o autor responsable")
        parser.add_argument("--titulo", required=True, help="Título de la documentación o estándar")
        parser.add_argument("--url", required=True, help="URL canónica HTTPS")
        parser.add_argument("--edicion", default="", help="Edición, versión o fecha identificable")
        parser.add_argument("--licencia-id", default="", help="Identificador de licencia, por ejemplo SPDX")
        parser.add_argument("--licencia-url", default="", help="URL de las condiciones de licencia")
        parser.add_argument("--notas", default="", help="Notas editoriales para la revisión")

    @transaction.atomic
    def handle(self, *args, **options):
        url = options["url"].strip()
        try:
            parsed = urlsplit(url)
            hostname = parsed.hostname
        except ValueError as exc:
            raise CommandError("--url no es una URL válida.") from exc
        if parsed.scheme.lower() != "https" or not hostname:
            raise CommandError("--url debe ser una URL HTTPS absoluta con un dominio válido.")
        if parsed.username or parsed.password:
            raise CommandError("--url no puede contener credenciales.")

        publicador = options["publicador"].strip()
        titulo = options["titulo"].strip()
        if not publicador or not titulo:
            raise CommandError("--publicador y --titulo no pueden estar vacíos.")

        edicion = options["edicion"].strip()
        if FuenteConocimiento.objects.filter(url_canonica=url, edicion=edicion).exists():
            raise CommandError(
                "Ya existe una fuente registrada con esa URL canónica y edición."
            )

        fuente = FuenteConocimiento(
            publicador=publicador,
            titulo=titulo,
            url_canonica=url,
            edicion=edicion,
            identificador_licencia=options["licencia_id"].strip(),
            url_licencia=options["licencia_url"].strip(),
            consultada_en=timezone.now(),
            notas=options["notas"].strip(),
            activa=True,
        )
        try:
            fuente.full_clean()
            fuente.save()
        except ValidationError as exc:
            raise CommandError("; ".join(exc.messages)) from exc
        except IntegrityError as exc:
            raise CommandError(
                "La fuente ya existe o incumple una restricción de integridad."
            ) from exc

        self.stdout.write(self.style.SUCCESS(
            f"Fuente registrada: ID={fuente.pk}, UUID={fuente.clave}, "
            f"publicador={fuente.publicador}, título={fuente.titulo}"
        ))
        self.stdout.write(self.style.WARNING(
            "Registro creado, no verificado: un editor debe comprobar autoridad, "
            "vigencia, edición y licencia antes de usarlo en contenido publicable."
        ))
