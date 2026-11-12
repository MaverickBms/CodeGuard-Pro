"""Registra una decisión editorial auditada sobre la licencia de una fuente."""

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

from apps.roadmaps.knowledge import revisar_licencia_fuente


class Command(BaseCommand):
    help = "Revisa la licencia de una fuente; no consulta ni verifica automáticamente la URL."

    def add_arguments(self, parser):
        parser.add_argument("--fuente-id", type=int, required=True)
        parser.add_argument("--usuario", required=True, help="Username de un editor activo")
        parser.add_argument(
            "--estado",
            required=True,
            choices=["compatible", "solo_referencia", "requiere_permiso", "no_reutilizable"],
        )
        parser.add_argument("--evidencia", required=True, help="URL HTTPS o referencia verificable")
        parser.add_argument("--alcance", default="", help="Alcance permitido; obligatorio para compatible")
        parser.add_argument("--nota", required=True, help="Justificación de la decisión editorial")

    def handle(self, *args, **options):
        User = get_user_model()
        try:
            actor = User.objects.get(username=options["usuario"], is_active=True, is_staff=True)
            fuente = revisar_licencia_fuente(
                options["fuente_id"],
                actor=actor,
                estado=options["estado"],
                evidencia=options["evidencia"],
                alcance=options["alcance"],
                nota=options["nota"],
            )
        except User.DoesNotExist as exc:
            raise CommandError("El usuario debe existir y ser editor activo (is_staff).") from exc
        except (ValidationError, ValueError) as exc:
            mensaje = "; ".join(exc.messages) if isinstance(exc, ValidationError) else str(exc)
            raise CommandError(mensaje) from exc
        except Exception as exc:
            raise CommandError(str(exc)) from exc

        self.stdout.write(self.style.SUCCESS(
            f"Licencia revisada: fuente={fuente.pk}, estado={fuente.estado_revision_licencia}, "
            f"editor={actor.username}, fecha={fuente.revisada_en.isoformat()}"
        ))
