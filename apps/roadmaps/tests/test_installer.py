"""Pruebas de instalación y rollback de paquetes firmados."""
import base64
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.roadmaps.knowledge import (
    aprobar_version_contenido,
    crear_version_contenido_leccion,
    enviar_version_a_revision,
    publicar_version_contenido,
    revisar_licencia_fuente,
)
from apps.roadmaps.models import (
    ContenidoLeccion,
    ContenidoLeccionPaquete,
    EjemploLeccion,
    EjercicioLeccion,
    EstadoSincronizacion,
    Etapa,
    FuenteConocimiento,
    FuentePaqueteConocimiento,
    Leccion,
    Modulo,
    PaqueteConocimientoInstalado,
    Progreso,
    Roadmap,
)
from apps.roadmaps.publisher import publicar_paquete_conocimiento
from apps.roadmaps.models_attempts import ConfiguracionEvaluacion, IntentoEjercicio
from apps.roadmaps.attempts import registrar_intento_ejercicio
from apps.roadmaps.sync_client import SyncClientError, sincronizar_conocimiento
from apps.roadmaps.installer import (
    InstallationError,
    instalar_paquete_firmado,
    restaurar_paquete_anterior,
)


class InstaladorPaquetesTests(TestCase):
    def setUp(self):
        self.editor = get_user_model().objects.create_user(
            username="editor_instalador",
            password="ClaveSegura123!",
            is_staff=True,
            is_active=True,
        )
        roadmap = Roadmap.objects.create(nombre="ASCENSO instalador", edicion="test")
        etapa = Etapa.objects.create(roadmap=roadmap, numero=0, titulo="Fundamentos")
        modulo = Modulo.objects.create(etapa=etapa, numero="0.1", titulo="Introducción")
        self.leccion = Leccion.objects.create(
            modulo=modulo, titulo="Variables", descripcion="Unidad de variables."
        )
        ContenidoLeccion.objects.create(
            leccion=self.leccion,
            objetivos_aprendizaje="Comprender variables.",
            teoria_tecnica="Una variable enlaza un nombre con un objeto.",
            explicacion_sencilla="Un nombre permite referirse a un valor.",
        )
        EjemploLeccion.objects.create(
            leccion=self.leccion,
            titulo="Asignación",
            contexto="Asignación básica.",
            lenguaje="Python",
            codigo="valor = 3",
            salida_esperada="",
            explicacion="Se asigna un entero.",
        )
        EjercicioLeccion.objects.create(
            leccion=self.leccion,
            titulo="Crear una variable",
            enunciado="Declara una variable llamada total.",
            instrucciones="Usa Python.",
            lenguaje="Python",
            nivel="basico",
            codigo_inicial="",
            obligatorio=True,
            orden=1,
        )
        self.fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation",
            titulo="Python Language Reference",
            url_canonica="https://docs.python.org/3/reference/",
            edicion="3",
        )
        revisar_licencia_fuente(
            self.fuente.pk,
            actor=self.editor,
            estado="compatible",
            evidencia="https://docs.python.org/3/license.html",
            alcance="Redistribución con atribución.",
            nota="Revisión manual de licencia para pruebas.",
        )
        version = crear_version_contenido_leccion(
            self.leccion,
            resumen_cambios="Publicación inicial.",
            fuentes=[(
                self.fuente, "principal", "Assignment statements",
                "Documentación oficial.",
            )],
        )
        enviar_version_a_revision(version.pk, actor=self.editor)
        aprobar_version_contenido(version.pk, actor=self.editor)
        publicar_version_contenido(version.pk, actor=self.editor)

        self.private_key = Ed25519PrivateKey.generate()
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.key_path = self.root / "signing-key.pem"
        self.key_path.write_bytes(self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        ))
        os.chmod(self.key_path, 0o600)
        self.output = self.root / "artifacts"
        self.data = self.root / "local-data"
        self.public_key = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        self.trusted_keys = {
            "test-ed25519": base64.b64encode(self.public_key).decode("ascii")
        }

    def tearDown(self):
        self.temp.cleanup()

    def publicar(self):
        result = publicar_paquete_conocimiento(
            channel="stable",
            package_version="1.0.0",
            minimum_app_version="1.0.0",
            base_url="https://cdn.codeguard.example/stable",
            allowed_hosts={"cdn.codeguard.example"},
            key_id="test-ed25519",
            private_key_path=self.key_path,
            output_directory=self.output,
        )
        return (
            Path(result["manifest_path"]).read_bytes(),
            Path(result["signature_path"]).read_bytes(),
            Path(result["package_path"]).read_bytes(),
        )

    def instalar(self, artifacts):
        manifest, signature, package = artifacts
        return instalar_paquete_firmado(
            manifest,
            signature,
            package,
            trusted_public_keys=self.trusted_keys,
            allowed_hosts={"cdn.codeguard.example"},
            expected_channel="stable",
            app_version="1.0.0",
            manifest_etag='"knowledge-v1"',
        )

    def test_instala_snapshots_catalogo_y_activa_solo_al_final(self):
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            result = self.instalar(self.publicar())

        package = result["package"]
        state = EstadoSincronizacion.objects.get(channel="stable")
        self.assertTrue(result["installed"])
        self.assertEqual(package.estado, "activo")
        self.assertEqual(state.active_package_id, package.pk)
        self.assertEqual(ContenidoLeccionPaquete.objects.filter(paquete=package).count(), 1)
        self.assertEqual(FuentePaqueteConocimiento.objects.filter(paquete=package).count(), 1)
        self.assertTrue((self.data / package.artifact_storage_key).is_file())
        self.assertEqual(package.contenidos_leccion.get().leccion_id, self.leccion.pk)
        self.assertEqual(package.fuentes_catalogo.get().source_uuid, self.fuente.clave)

    def test_repetir_el_mismo_manifiesto_es_idempotente(self):
        artifacts = self.publicar()
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            first = self.instalar(artifacts)
            second = self.instalar(artifacts)

        self.assertTrue(first["installed"])
        self.assertTrue(second["unchanged"])
        self.assertEqual(first["package"].pk, second["package"].pk)
        self.assertEqual(PaqueteConocimientoInstalado.objects.count(), 1)
        self.assertEqual(ContenidoLeccionPaquete.objects.count(), 1)

    def test_catalogo_instalado_no_sobrescribe_fuente_editorial_local(self):
        artifacts = self.publicar()
        self.fuente.titulo = "Título local actualizado"
        self.fuente.save(update_fields=["titulo"])
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            package = self.instalar(artifacts)["package"]

        self.fuente.refresh_from_db()
        catalog_entry = package.fuentes_catalogo.get(source_uuid=self.fuente.clave)
        self.assertEqual(self.fuente.titulo, "Título local actualizado")
        self.assertEqual(catalog_entry.metadatos["titulo"], "Python Language Reference")

    def test_fallo_al_persistir_catalogo_revierte_paquete_y_mantiene_activo_anterior(self):
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            first = self.instalar(self.publicar())["package"]
            second_artifacts = self.publicar()
            with patch(
                "apps.roadmaps.models.EstadoSincronizacion.save",
                side_effect=RuntimeError("fallo simulado al confirmar el puntero activo"),
            ):
                with self.assertRaisesRegex(RuntimeError, "confirmar el puntero"):
                    self.instalar(second_artifacts)

        first.refresh_from_db()
        state = EstadoSincronizacion.objects.get(channel="stable")
        self.assertEqual(first.estado, "activo")
        self.assertEqual(state.active_package_id, first.pk)
        self.assertEqual(PaqueteConocimientoInstalado.objects.count(), 1)
        self.assertEqual(ContenidoLeccionPaquete.objects.count(), 1)
        self.assertEqual(FuentePaqueteConocimiento.objects.count(), 1)

    def test_secuencia_anterior_se_rechaza_sin_cambiar_paquete_activo(self):
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            first_artifacts = self.publicar()
            second_artifacts = self.publicar()
            first = self.instalar(first_artifacts)["package"]
            second = self.instalar(second_artifacts)["package"]
            with self.assertRaisesMessage(InstallationError, "manifiesto antiguo"):
                self.instalar(first_artifacts)

        state = EstadoSincronizacion.objects.get(channel="stable")
        first.refresh_from_db()
        self.assertEqual(state.active_package_id, second.pk)
        self.assertEqual(first.estado, "sustituido")
        self.assertEqual(second.estado, "activo")
        self.assertEqual(PaqueteConocimientoInstalado.objects.count(), 2)

    def test_hash_de_zip_incorrecto_no_deja_registros(self):
        manifest, signature, package = self.publicar()
        altered_package = package[:-1] + bytes([package[-1] ^ 0x01])
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            with self.assertRaisesMessage(InstallationError, "SHA-256 del paquete"):
                instalar_paquete_firmado(
                    manifest,
                    signature,
                    altered_package,
                    trusted_public_keys=self.trusted_keys,
                    allowed_hosts={"cdn.codeguard.example"},
                    expected_channel="stable",
                    app_version="1.0.0",
                )

        self.assertEqual(PaqueteConocimientoInstalado.objects.count(), 0)
        self.assertEqual(ContenidoLeccionPaquete.objects.count(), 0)
        self.assertFalse((self.data / "knowledge-packages").exists())

    def test_cliente_http_instala_solo_despues_de_verificar_manifiesto(self):
        artifacts = self.publicar()
        manifest, signature, package_bytes = artifacts
        package_url = json.loads(manifest)["package"]["url"]
        requested = []

        def fake_fetch(url, **kwargs):
            requested.append(url)
            if url.endswith("/manifest.json"):
                return manifest, '"release-1"'
            if url.endswith("/manifest.ed25519"):
                return signature, ""
            if url == package_url:
                return package_bytes, ""
            raise AssertionError(f"URL inesperada: {url}")

        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            with patch("apps.roadmaps.sync_client._fetch_bytes", side_effect=fake_fetch):
                result = sincronizar_conocimiento(
                    channel="stable",
                    manifest_url="https://cdn.codeguard.example/stable/manifest.json",
                    signature_url="https://cdn.codeguard.example/stable/manifest.ed25519",
                    trusted_public_keys=self.trusted_keys,
                    allowed_hosts={"cdn.codeguard.example"},
                    app_version="1.0.0",
                )

        self.assertEqual(result["status"], "installed")
        self.assertEqual(requested, [
            "https://cdn.codeguard.example/stable/manifest.json",
            "https://cdn.codeguard.example/stable/manifest.ed25519",
            package_url,
        ])
        state = EstadoSincronizacion.objects.get(channel="stable")
        self.assertEqual(state.manifest_etag, '"release-1"')
        self.assertEqual(state.active_package_id, result["package"].pk)

    def test_cliente_http_no_descarga_zip_si_la_firma_es_invalida(self):
        manifest, signature, _package = self.publicar()
        requested = []

        def fake_fetch(url, **kwargs):
            requested.append(url)
            if url.endswith("/manifest.json"):
                return manifest, '"release-1"'
            return b"firma-alterada", ""

        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            with patch("apps.roadmaps.sync_client._fetch_bytes", side_effect=fake_fetch):
                with self.assertRaisesRegex(SyncClientError, "firma"):
                    sincronizar_conocimiento(
                        channel="stable",
                        manifest_url="https://cdn.codeguard.example/stable/manifest.json",
                        signature_url="https://cdn.codeguard.example/stable/manifest.ed25519",
                        trusted_public_keys=self.trusted_keys,
                        allowed_hosts={"cdn.codeguard.example"},
                        app_version="1.0.0",
                    )

        self.assertEqual(len(requested), 2)
        self.assertFalse(PaqueteConocimientoInstalado.objects.exists())
        state = EstadoSincronizacion.objects.get(channel="stable")
        self.assertEqual(state.last_error_code, "manifest_rejected")

    def test_cliente_http_usa_etag_y_acepta_304_sin_descargar(self):
        state = EstadoSincronizacion.objects.create(
            channel="stable", manifest_etag='"cached-release"'
        )
        with patch("apps.roadmaps.sync_client._fetch_bytes", return_value=(None, '"cached-release"')) as fetch:
            result = sincronizar_conocimiento(
                channel="stable",
                manifest_url="https://cdn.codeguard.example/stable/manifest.json",
                signature_url="https://cdn.codeguard.example/stable/manifest.ed25519",
                trusted_public_keys=self.trusted_keys,
                allowed_hosts={"cdn.codeguard.example"},
                app_version="1.0.0",
            )

        self.assertEqual(result["status"], "not_modified")
        fetch.assert_called_once()
        self.assertIn("If-None-Match", fetch.call_args.kwargs["headers"])
        state.refresh_from_db()
        self.assertIsNotNone(state.last_check_at)
        self.assertEqual(state.last_error_code, "")

    def test_cliente_http_sin_claves_confiables_falla_sin_conectar(self):
        with patch("apps.roadmaps.sync_client._fetch_bytes") as fetch:
            with self.assertRaisesRegex(SyncClientError, "claves públicas"):
                sincronizar_conocimiento(
                    channel="stable",
                    manifest_url="https://cdn.codeguard.example/stable/manifest.json",
                    signature_url="https://cdn.codeguard.example/stable/manifest.ed25519",
                    trusted_public_keys={},
                    allowed_hosts={"cdn.codeguard.example"},
                    app_version="1.0.0",
                )
        fetch.assert_not_called()
        self.assertFalse(EstadoSincronizacion.objects.exists())

    def test_cliente_http_rechaza_endpoint_fuera_de_allowlist_sin_conectar(self):
        with patch("apps.roadmaps.sync_client._fetch_bytes") as fetch:
            with self.assertRaisesRegex(SyncClientError, "host autorizado"):
                sincronizar_conocimiento(
                    channel="stable",
                    manifest_url="https://evil.example/manifest.json",
                    signature_url="https://cdn.codeguard.example/stable/manifest.ed25519",
                    trusted_public_keys=self.trusted_keys,
                    allowed_hosts={"cdn.codeguard.example"},
                    app_version="1.0.0",
                )
        fetch.assert_not_called()
        self.assertFalse(EstadoSincronizacion.objects.exists())

    def test_rollback_reactiva_paquete_anterior_sin_eliminar_evidencia(self):
        ejercicio = self.leccion.ejercicios.get()
        ConfiguracionEvaluacion.objects.create(
            ejercicio=ejercicio,
            tipo="respuesta_exacta",
            configuracion={"respuesta_esperada": "total = 5"},
            permite_completar_leccion=True,
        )
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            first = self.instalar(self.publicar())["package"]
            intento = registrar_intento_ejercicio(
                self.editor, ejercicio, "total = 5", actor_auditoria=self.editor
            )
            second = self.instalar(self.publicar())["package"]
            restored = restaurar_paquete_anterior(
                channel="stable", package_id=first.package_id
            )

        first.refresh_from_db()
        second.refresh_from_db()
        intento.refresh_from_db()
        state = EstadoSincronizacion.objects.get(channel="stable")
        self.assertEqual(restored.pk, first.pk)
        self.assertEqual(first.estado, "activo")
        self.assertEqual(second.estado, "sustituido")
        self.assertEqual(state.active_package_id, first.pk)
        self.assertEqual(first.contenidos_leccion.count(), 1)
        self.assertEqual(intento.paquete_contenido_id, first.pk)
        self.assertTrue(IntentoEjercicio.objects.filter(pk=intento.pk).exists())

    def test_intento_usa_snapshot_del_paquete_y_conserva_evidencia(self):
        ejercicio = self.leccion.ejercicios.get()
        ConfiguracionEvaluacion.objects.create(
            ejercicio=ejercicio,
            tipo="respuesta_exacta",
            configuracion={"respuesta_esperada": "total = 5"},
            permite_completar_leccion=True,
        )
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            package = self.instalar(self.publicar())["package"]
            intento = registrar_intento_ejercicio(
                self.editor,
                ejercicio,
                "total = 5",
                actor_auditoria=self.editor,
            )

        intento.refresh_from_db()
        self.assertEqual(intento.resultado, "aprobado")
        self.assertEqual(intento.paquete_contenido_id, package.pk)
        self.assertIsNone(intento.version_contenido_id)
        self.assertEqual(
            intento.snapshot_ejercicio["enunciado"],
            "Declara una variable llamada total.",
        )
        progreso = Progreso.objects.get(usuario=self.editor, leccion=self.leccion)
        self.assertEqual(progreso.estado, "completado")
        self.assertTrue(IntentoEjercicio.objects.filter(pk=intento.pk).exists())

    def test_firma_invalida_no_crea_registro_ni_activa_contenido(self):
        manifest, signature, package = self.publicar()
        invalid_signature = b"invalid"
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            with self.assertRaises(InstallationError):
                instalar_paquete_firmado(
                    manifest,
                    invalid_signature,
                    package,
                    trusted_public_keys=self.trusted_keys,
                    allowed_hosts={"cdn.codeguard.example"},
                    expected_channel="stable",
                    app_version="1.0.0",
                )

        self.assertEqual(PaqueteConocimientoInstalado.objects.count(), 0)
        self.assertEqual(EstadoSincronizacion.objects.count(), 0)
        self.assertFalse((self.data / "knowledge-packages").exists())

    def test_conflicto_curricular_aborta_sin_modificar_fuentes_locales(self):
        artifacts = self.publicar()
        self.leccion.descripcion = "Descripción local divergente."
        self.leccion.save(update_fields=["descripcion"])
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            with self.assertRaisesMessage(InstallationError, "identidad curricular difiere"):
                self.instalar(artifacts)

        self.fuente.refresh_from_db()
        self.assertEqual(self.fuente.titulo, "Python Language Reference")
        self.assertEqual(PaqueteConocimientoInstalado.objects.count(), 0)
        self.assertEqual(ContenidoLeccionPaquete.objects.count(), 0)
