"""Ejecuta una transición controlada del flujo editorial."""
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from apps.roadmaps.knowledge import (
    aprobar_version_contenido,
    enviar_version_a_revision,
    publicar_version_contenido,
    retirar_version_publicada,
)


class Command(BaseCommand):
    help = "Envía, aprueba, publica o retira una versión de contenido."

    def add_arguments(self, parser):
        parser.add_argument("accion", choices=("enviar-revision", "aprobar", "publicar", "retirar"))
        parser.add_argument("--version", type=int, required=True, help="ID de la versión")
        parser.add_argument("--usuario", required=True, help="Usuario editorial activo")
        parser.add_argument("--motivo", default="", help="Motivo obligatorio al retirar")

    def handle(self, *args, **options):
        User = get_user_model()
        try:
            actor = User.objects.get(username=options["usuario"])
        except User.DoesNotExist as exc:
            raise CommandError("No existe el usuario editorial indicado.") from exc

        accion = options["accion"]
        version_id = options["version"]
        try:
            if accion == "enviar-revision":
                version = enviar_version_a_revision(version_id, actor=actor)
            elif accion == "aprobar":
                version = aprobar_version_contenido(version_id, actor=actor)
            elif accion == "publicar":
                version = publicar_version_contenido(version_id, actor=actor)
            else:
                if not options["motivo"].strip():
                    raise CommandError("--motivo es obligatorio para retirar una publicación.")
                version = retirar_version_publicada(version_id, actor=actor, motivo=options["motivo"])
        except ValidationError as exc:
            raise CommandError("; ".join(exc.messages)) from exc
        except Exception as exc:
            if isinstance(exc, CommandError):
                raise
            raise CommandError(str(exc)) from exc

        self.stdout.write(self.style.SUCCESS(
            f"Versión {version.pk}: estado={version.estado}, "
            f"lección={version.leccion_id}, versión={version.numero_version}"
        ))
