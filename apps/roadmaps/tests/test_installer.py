"""Pruebas de instalación y rollback de paquetes firmados."""
import base64
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

    def test_rollback_reactiva_paquete_anterior_sin_eliminar_evidencia(self):
        with patch.dict(os.environ, {"CODEGUARD_DATA_DIR": str(self.data)}):
            first = self.instalar(self.publicar())["package"]
            second = self.instalar(self.publicar())["package"]
            restored = restaurar_paquete_anterior(
                channel="stable", package_id=first.package_id
            )

        first.refresh_from_db()
        second.refresh_from_db()
        state = EstadoSincronizacion.objects.get(channel="stable")
        self.assertEqual(restored.pk, first.pk)
        self.assertEqual(first.estado, "activo")
        self.assertEqual(second.estado, "sustituido")
        self.assertEqual(state.active_package_id, first.pk)
        self.assertEqual(first.contenidos_leccion.count(), 1)

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
