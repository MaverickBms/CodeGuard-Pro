"""Publica un paquete inmutable de snapshots académicos aprobados."""
import os

from django.core.management.base import BaseCommand, CommandError

from apps.roadmaps.publisher import PublicationError, publicar_paquete_conocimiento


class Command(BaseCommand):
    help = (
        "Construye y firma un paquete de conocimiento desde las versiones "
        "editoriales activas. No realiza despliegue remoto."
    )

    def add_arguments(self, parser):
        parser.add_argument("--channel", choices=("stable", "beta"), required=True)
        parser.add_argument("--package-version", required=True)
        parser.add_argument("--minimum-app-version", required=True)
        parser.add_argument("--base-url", required=True, help="Base HTTPS del artefacto, sin nombre de archivo")
        parser.add_argument("--allowed-host", action="append", required=True, help="Host HTTPS permitido; puede repetirse")
        parser.add_argument("--key-id", required=True)
        parser.add_argument("--private-key", required=True, help="Ruta externa al repositorio de la clave PEM Ed25519")
        parser.add_argument("--output-directory", required=True)
        parser.add_argument(
            "--key-password-env",
            default="",
            help="Variable de entorno opcional que contiene la contraseña de la clave PEM",
        )

    def handle(self, *args, **options):
        password = None
        env_name = options["key_password_env"].strip()
        if env_name:
            password = os.environ.get(env_name)
            if password is None:
                raise CommandError(f"No existe la variable de entorno {env_name}.")
        try:
            result = publicar_paquete_conocimiento(
                channel=options["channel"],
                package_version=options["package_version"],
                minimum_app_version=options["minimum_app_version"],
                base_url=options["base_url"],
                allowed_hosts=options["allowed_host"],
                key_id=options["key_id"],
                private_key_path=options["private_key"],
                output_directory=options["output_directory"],
                key_password=password,
            )
        except (ValueError, OSError) as exc:
            raise CommandError(str(exc)) from exc

        release = result["release"]
        self.stdout.write(self.style.SUCCESS(
            f"Publicación creada: canal={release.channel}, secuencia={release.sequence}, "
            f"paquete={release.package_id}, versión={release.package_version}"
        ))
        self.stdout.write(f"Lecciones: {result['lesson_count']}")
        self.stdout.write(f"ZIP: {result['package_path']}")
        self.stdout.write(f"Manifiesto: {result['manifest_path']}")
        self.stdout.write(f"Firma: {result['signature_path']}")
        self.stdout.write(f"SHA-256 ZIP: {result['package_sha256']}")
        self.stdout.write(f"SHA-256 manifiesto: {result['manifest_sha256']}")
        self.stdout.write(self.style.WARNING(
            "Los artefactos quedaron en el directorio local indicado. "
            "Aún no se han subido a un servidor ni se ha habilitado un endpoint público."
        ))
