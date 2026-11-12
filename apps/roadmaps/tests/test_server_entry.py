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
