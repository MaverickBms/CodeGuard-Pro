"""Pruebas del modo de sincronización aislada del servidor empaquetado."""

import os
import sys
from unittest.mock import patch

import django
from django.test import SimpleTestCase

import server_entry


class ServerEntrySyncModeTests(SimpleTestCase):
    """Comprueba que --sync-knowledge no arranque ni migre el servidor web."""

    def test_sync_mode_dispatches_command_without_starting_server(self):
        with (
            patch.dict(
                os.environ,
                {
                    "DJANGO_SETTINGS_MODULE": "config.settings.desktop",
                    "CODEGUARD_SYNC_CHANNEL": "beta",
                    "CODEGUARD_SYNC_FORCE": "1",
                },
            ),
            patch.object(sys, "argv", ["CodeGuardServer", "--sync-knowledge"]),
            patch.object(django, "setup") as django_setup,
            patch("django.core.management.call_command") as call_command,
        ):
            result = server_entry.main()

        self.assertEqual(result, 0)
        django_setup.assert_called_once_with()
        call_command.assert_called_once_with(
            "sincronizar_conocimiento",
            channel="beta",
            force=True,
            verbosity=1,
        )

    def test_sync_mode_defaults_to_stable_and_not_forced(self):
        with (
            patch.dict(
                os.environ,
                {
                    "DJANGO_SETTINGS_MODULE": "config.settings.desktop",
                    "CODEGUARD_SYNC_CHANNEL": "",
                    "CODEGUARD_SYNC_FORCE": "0",
                },
            ),
            patch.object(sys, "argv", ["CodeGuardServer", "--sync-knowledge"]),
            patch.object(django, "setup"),
            patch("django.core.management.call_command") as call_command,
        ):
            result = server_entry.main()

        self.assertEqual(result, 0)
        call_command.assert_called_once_with(
            "sincronizar_conocimiento",
            channel="stable",
            force=False,
            verbosity=1,
        )


class ServerEntryRestoreModeTests(SimpleTestCase):
    """El modo --restore-backup restaura sin arrancar Waitress ni migrar."""

    def test_restore_mode_invokes_restore_and_exits(self):
        with (
            patch.object(
                sys,
                "argv",
                ["CodeGuardServer", "--restore-backup", "/tmp/copia.zip"],
            ),
            patch.object(django, "setup"),
            patch(
                "apps.core.restore.restore_backup",
                return_value={
                    "applied_migrations": 10,
                    "pending_migrations": 2,
                    "manifest": {},
                    "rollback_path": None,
                },
            ) as restore_backup,
        ):
            result = server_entry.main()

        self.assertEqual(result, 0)
        restore_backup.assert_called_once()
        args, kwargs = restore_backup.call_args
        self.assertEqual(args[0], "/tmp/copia.zip")
        self.assertTrue(kwargs["confirm"])

    def test_restore_mode_reports_failure_without_starting_server(self):
        with (
            patch.object(
                sys,
                "argv",
                ["CodeGuardServer", "--restore-backup", "/tmp/copia.zip"],
            ),
            patch.object(django, "setup"),
            patch(
                "apps.core.restore.restore_backup",
                side_effect=ValueError("copia inválida"),
            ),
        ):
            result = server_entry.main()

        self.assertEqual(result, 8)


class ServerEntryInitializationTests(SimpleTestCase):
    """La inicialización normal delega en el arranque idempotente auditado."""

    def test_initialization_delegates_to_bootstrap_without_recreate(self):
        resultado = {
            "migraciones_pendientes": 0,
            "roadmap_cargado": False,
            "roadmap_reutilizado": True,
            "etapas": 33,
            "modulos": 212,
            "lecciones": 1946,
            "prerrequisitos": 7,
            "sobrantes": 0,
            "milisegundos": 80,
        }
        with patch(
            "apps.roadmaps.bootstrap.preparar_perfil_local",
            return_value=resultado,
        ) as preparar:
            devuelto = server_entry._initialize_database()

        self.assertEqual(devuelto, resultado)
        preparar.assert_called_once_with()

    def test_initialization_never_uses_recreate(self):
        with patch(
            "apps.roadmaps.bootstrap.preparar_perfil_local",
            return_value={"roadmap_cargado": False, "milisegundos": 1},
        ) as preparar:
            server_entry._initialize_database()

        self.assertNotIn("--recrear", str(preparar.call_args_list))
