"""Comprueba y descarga actualizaciones firmadas del conocimiento."""
import json
import os

from django.core.management.base import BaseCommand, CommandError

from apps.roadmaps.sync_client import SyncClientError, sincronizar_conocimiento


class Command(BaseCommand):
    help = (
        "Consulta un manifiesto HTTPS y descarga/instala contenido académico firmado. "
        "Nunca transmite progreso ni respuestas del estudiante."
    )

    def add_arguments(self, parser):
        parser.add_argument("--channel", choices=("stable", "beta"), default="stable")
        parser.add_argument("--force", action="store_true", help="Ignora la espera local entre comprobaciones.")

    def handle(self, *args, **options):
        manifest_url = os.environ.get("CODEGUARD_SYNC_MANIFEST_URL", "").strip()
        signature_url = os.environ.get("CODEGUARD_SYNC_SIGNATURE_URL", "").strip()
        app_version = os.environ.get("CODEGUARD_APP_VERSION", "").strip()
        hosts_raw = os.environ.get("CODEGUARD_SYNC_ALLOWED_HOSTS", "")
        keys_raw = os.environ.get("CODEGUARD_SYNC_TRUSTED_PUBLIC_KEYS", "")
        if not all((manifest_url, signature_url, app_version, hosts_raw, keys_raw)):
            raise CommandError(
                "Configura CODEGUARD_SYNC_MANIFEST_URL, CODEGUARD_SYNC_SIGNATURE_URL, "
                "CODEGUARD_APP_VERSION, CODEGUARD_SYNC_ALLOWED_HOSTS y "
                "CODEGUARD_SYNC_TRUSTED_PUBLIC_KEYS."
            )
        try:
            trusted_keys = json.loads(keys_raw)
            if not isinstance(trusted_keys, dict):
                raise ValueError("El almacén de claves debe ser un objeto JSON.")
            timeout = float(os.environ.get("CODEGUARD_SYNC_TIMEOUT", "12"))
            result = sincronizar_conocimiento(
                channel=options["channel"],
                manifest_url=manifest_url,
                signature_url=signature_url,
                trusted_public_keys=trusted_keys,
                allowed_hosts=[host.strip() for host in hosts_raw.split(",") if host.strip()],
                app_version=app_version,
                timeout=timeout,
                force=options["force"],
            )
        except SyncClientError as exc:
            raise CommandError(f"Sincronización no completada [{exc.code}]: {exc}") from exc
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            raise CommandError(f"Configuración de sincronización inválida: {exc}") from exc

        status = result.get("status", "unknown")
        if status == "installed":
            self.stdout.write(self.style.SUCCESS(
                f"Paquete instalado: {result['package'].package_version}; "
                f"lecciones={result.get('lesson_count', 0)}; fuentes={result.get('source_count', 0)}."
            ))
        elif status == "unchanged":
            self.stdout.write(self.style.SUCCESS("El conocimiento local ya está actualizado."))
        elif status == "not_modified":
            self.stdout.write("El servidor confirma que el manifiesto no ha cambiado (HTTP 304).")
        elif status == "deferred":
            self.stdout.write("La comprobación se pospuso según la política local.")
        else:
            self.stdout.write(f"Resultado de sincronización: {status}.")
