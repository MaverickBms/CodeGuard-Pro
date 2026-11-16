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


class ServerEntryInitializationTests(SimpleTestCase):
    """La inicialización normal debe ser idempotente y preservar el progreso."""

    def test_initialization_runs_migrations_then_loads_without_recreate(self):
        with patch("django.core.management.call_command") as call_command:
            server_entry._initialize_database()

        self.assertEqual(
            call_command.call_args_list,
            [
                (("migrate",), {"interactive": False, "verbosity": 1}),
                (("cargar_ascenso",), {"verbosity": 1}),
            ],
        )
        self.assertNotIn(
            "--recrear",
            str(call_command.call_args_list),
        )
