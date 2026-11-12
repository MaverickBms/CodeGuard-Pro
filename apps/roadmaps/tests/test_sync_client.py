"""Pruebas del transporte HTTPS del cliente de sincronización."""
import io
import tempfile
import urllib.error
from datetime import timedelta
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from django.test import SimpleTestCase, TestCase, override_settings
from django.utils import timezone

from apps.roadmaps.models import EstadoSincronizacion

from apps.roadmaps.sync_client import (
    SyncClientError,
    _fetch_bytes,
    _retry_delay_for_state,
    _channel_sync_lock,
    _record_failure,
    _validate_endpoint,
)


class FakeResponse:
    status = 200

    def __init__(self, body, *, headers=None, url="https://cdn.codeguard.example/test"):
        self.body = io.BytesIO(body)
        self.headers = headers or {}
        self.url = url

    def read(self, size=-1):
        return self.body.read(size)

    def geturl(self):
        return self.url

    def getcode(self):
        return self.status

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class TransporteSyncTests(SimpleTestCase):
    allowed_hosts = {"cdn.codeguard.example"}

    def test_endpoint_exige_https_y_host_allowlist(self):
        for url in (
            "http://cdn.codeguard.example/manifest.json",
            "https://evil.example/manifest.json",
            "https://usuario@cdn.codeguard.example/manifest.json",
            "https://cdn.codeguard.example:8443/manifest.json",
            "https://cdn.codeguard.example/manifest.json#fragmento",
        ):
            with self.subTest(url=url):
                with self.assertRaises(SyncClientError):
                    _validate_endpoint(url, allowed_hosts=self.allowed_hosts, label="test")

    def test_descarga_respeta_limite_de_bytes(self):
        response = FakeResponse(b"12345", headers={"Content-Length": "5"}, url="https://cdn.codeguard.example/package.zip")
        with patch("apps.roadmaps.sync_client._open_url", return_value=response):
            with self.assertRaisesRegex(SyncClientError, "límite"):
                _fetch_bytes(
                    "https://cdn.codeguard.example/package.zip",
                    allowed_hosts=self.allowed_hosts,
                    timeout=3,
                    max_bytes=4,
                )

    def test_descarga_exige_tamano_firmado(self):
        response = FakeResponse(b"1234", headers={"Content-Length": "4"}, url="https://cdn.codeguard.example/package.zip")
        with patch("apps.roadmaps.sync_client._open_url", return_value=response):
            with self.assertRaisesRegex(SyncClientError, "tamaño"):
                _fetch_bytes(
                    "https://cdn.codeguard.example/package.zip",
                    allowed_hosts=self.allowed_hosts,
                    timeout=3,
                    max_bytes=10,
                    expected_size=5,
                )

    def test_descarga_rechaza_url_final_distinta(self):
        response = FakeResponse(
            b"data",
            headers={"Content-Length": "4"},
            url="https://other.example/package.zip",
        )
        with patch("apps.roadmaps.sync_client._open_url", return_value=response):
            with self.assertRaisesRegex(SyncClientError, "cambió de URL"):
                _fetch_bytes(
                    "https://cdn.codeguard.example/package.zip",
                    allowed_hosts=self.allowed_hosts,
                    timeout=3,
                    max_bytes=10,
                )

    def test_descarga_rechaza_redireccion_http(self):
        error = urllib.error.HTTPError(
            "https://cdn.codeguard.example/manifest.json",
            302,
            "Found",
            {},
            io.BytesIO(),
        )
        with patch("apps.roadmaps.sync_client._open_url", side_effect=error):
            with self.assertRaisesRegex(SyncClientError, "redirigir"):
                _fetch_bytes(
                    "https://cdn.codeguard.example/manifest.json",
                    allowed_hosts=self.allowed_hosts,
                    timeout=3,
                    max_bytes=1024,
                )

    def test_peticion_saliente_es_get_sin_cookies_ni_cuerpo(self):
        response = FakeResponse(
            b"ok",
            headers={"Content-Length": "2"},
            url="https://cdn.codeguard.example/manifest.json",
        )
        captured = {}

        def fake_open(request, *, timeout):
            captured["request"] = request
            captured["timeout"] = timeout
            return response

        with patch("apps.roadmaps.sync_client._open_url", side_effect=fake_open):
            payload, _etag = _fetch_bytes(
                "https://cdn.codeguard.example/manifest.json",
                allowed_hosts=self.allowed_hosts,
                timeout=7,
                max_bytes=20,
            )

        request = captured["request"]
        self.assertEqual(payload, b"ok")
        self.assertEqual(request.get_method(), "GET")
        self.assertIsNone(request.data)
        self.assertNotIn("Cookie", request.headers)
        self.assertNotIn("Authorization", request.headers)
        self.assertEqual(captured["timeout"], 7)

    def test_timeout_se_convierte_en_error_de_red_controlado(self):
        with patch("apps.roadmaps.sync_client._open_url", side_effect=TimeoutError()):
            with self.assertRaises(SyncClientError) as context:
                _fetch_bytes(
                    "https://cdn.codeguard.example/manifest.json",
                    allowed_hosts=self.allowed_hosts,
                    timeout=1,
                    max_bytes=1024,
                )
        self.assertEqual(context.exception.code, "network_error")

    def test_http_304_solo_se_acepta_si_se_solicito_condicionalmente(self):
        error = urllib.error.HTTPError(
            "https://cdn.codeguard.example/manifest.json",
            304,
            "Not Modified",
            {"ETag": '"v1"'},
            io.BytesIO(),
        )
        with patch("apps.roadmaps.sync_client._open_url", side_effect=error):
            with self.assertRaisesRegex(SyncClientError, "sin una descarga condicional"):
                _fetch_bytes(
                    "https://cdn.codeguard.example/package.zip",
                    allowed_hosts=self.allowed_hosts,
                    timeout=3,
                    max_bytes=1024,
                )
            result = _fetch_bytes(
                "https://cdn.codeguard.example/manifest.json",
                allowed_hosts=self.allowed_hosts,
                timeout=3,
                max_bytes=1024,
                headers={"If-None-Match": '"v1"'},
                allow_not_modified=True,
            )
        self.assertEqual(result, (None, '"v1"'))



class PoliticaReintentosTests(SimpleTestCase):
    def test_backoff_inicia_en_quince_minutos_y_duplica(self):
        now = timezone.now()
        state = SimpleNamespace(
            last_error_code="",
            last_check_at=None,
            next_check_after=None,
        )
        self.assertEqual(_retry_delay_for_state(state), timedelta(minutes=15))

        state.last_error_code = "network_error"
        state.last_check_at = now
        state.next_check_after = now + timedelta(minutes=15)
        self.assertEqual(_retry_delay_for_state(state), timedelta(minutes=30))

    def test_backoff_no_supera_veinticuatro_horas(self):
        now = timezone.now()
        state = SimpleNamespace(
            last_error_code="network_error",
            last_check_at=now,
            next_check_after=now + timedelta(hours=20),
        )
        self.assertEqual(_retry_delay_for_state(state), timedelta(hours=24))


class BloqueoSincronizacionTests(TestCase):
    def test_un_solo_proceso_puede_sincronizar_el_mismo_canal(self):
        with tempfile.TemporaryDirectory() as directory:
            with override_settings(DATA_DIR=Path(directory)):
                with _channel_sync_lock("stable"):
                    with self.assertRaises(SyncClientError) as context:
                        with _channel_sync_lock("stable"):
                            pass
                self.assertEqual(context.exception.code, "sync_in_progress")



class PersistenciaBackoffTests(TestCase):
    def test_persistencia_duplica_intervalo_tras_fallos_consecutivos(self):
        from unittest.mock import patch

        from django.utils import timezone

        now = timezone.now()
        EstadoSincronizacion.objects.create(channel="stable")
        with patch("apps.roadmaps.sync_client.timezone.now", return_value=now):
            _record_failure("stable", "network_error")

        state = EstadoSincronizacion.objects.get(channel="stable")
        self.assertEqual(state.next_check_after, now + timedelta(minutes=15))

        second_attempt = now + timedelta(minutes=15)
        with patch("apps.roadmaps.sync_client.timezone.now", return_value=second_attempt):
            _record_failure("stable", "network_error")

        state.refresh_from_db()
        self.assertEqual(state.next_check_after, second_attempt + timedelta(minutes=30))
