"""Pruebas del publicador central de paquetes de conocimiento."""
import base64
import os
import tempfile
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
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
    ContenidoLeccionActivo,
    Etapa,
    FuenteConocimiento,
    Leccion,
    Modulo,
    Roadmap,
    SecuenciaPublicacionConocimiento,
)
from apps.roadmaps.publisher import (
    PublicationError,
    _build_deterministic_zip,
    publicar_paquete_conocimiento,
)
from apps.roadmaps.distribution import (
    validate_package_archive,
    verify_signed_manifest,
)


class PublicadorConocimientoTests(TestCase):
    def setUp(self):
        self.editor = get_user_model().objects.create_user(
            username="editor_publicador",
            password="ClaveSegura123!",
            is_staff=True,
            is_active=True,
        )
        roadmap = Roadmap.objects.create(nombre="ASCENSO publicador", edicion="test")
        etapa = Etapa.objects.create(roadmap=roadmap, numero=0, titulo="Fundamentos")
        modulo = Modulo.objects.create(etapa=etapa, numero="0.1", titulo="Introducción")
        self.leccion = Leccion.objects.create(modulo=modulo, titulo="Variables")
        ContenidoLeccion.objects.create(
            leccion=self.leccion,
            objetivos_aprendizaje="Comprender variables.",
            teoria_tecnica="Una variable enlaza un nombre con un objeto.",
            explicacion_sencilla="Un nombre permite referirse a un valor.",
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
        self.assertTrue(
            ContenidoLeccionActivo.objects.filter(version=version).exists()
        )
        self.private_key = Ed25519PrivateKey.generate()
        self.temp = tempfile.TemporaryDirectory()
        self.key_path = Path(self.temp.name) / "signing-key.pem"
        self.output = Path(self.temp.name) / "artifacts"
        self.key_path.write_bytes(self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        ))
        os.chmod(self.key_path, 0o600)

    def tearDown(self):
        self.temp.cleanup()

    def publish(self):
        return publicar_paquete_conocimiento(
            channel="stable",
            package_version="1.0.0",
            minimum_app_version="1.0.0",
            base_url="https://cdn.codeguard.example/stable",
            allowed_hosts={"cdn.codeguard.example"},
            key_id="test-ed25519",
            private_key_path=self.key_path,
            output_directory=self.output,
        )

    def test_publicacion_genera_zip_manifiesto_y_firma_verificables(self):
        result = self.publish()
        manifest_bytes = Path(result["manifest_path"]).read_bytes()
        signature = Path(result["signature_path"]).read_bytes()
        package_bytes = Path(result["package_path"]).read_bytes()
        public_key = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        verified = verify_signed_manifest(
            manifest_bytes,
            signature,
            trusted_public_keys={
                "test-ed25519": base64.b64encode(public_key).decode("ascii")
            },
            allowed_hosts={"cdn.codeguard.example"},
            expected_channel="stable",
            app_version="1.0.0",
        )
        archive = validate_package_archive(package_bytes, manifest=verified["manifest"])
        self.assertEqual(result["lesson_count"], 1)
        self.assertEqual(len(archive["payloads"]), 1)
        self.assertEqual(len(archive["sources"]), 1)
        source = next(iter(archive["sources"].values()))
        self.assertEqual(source["clave"], str(self.fuente.clave))
        self.assertEqual(source["estado_revision_licencia"], "compatible")
        self.assertEqual(source["url_canonica"], self.fuente.url_canonica)
        self.assertNotIn("revisada_por", source)
        self.assertEqual(archive["index"]["schema_version"], 2)
        self.assertEqual(result["release"].sequence, 1)

    def test_publicaciones_incrementan_secuencia_y_no_sobrescriben_artefactos(self):
        first = self.publish()
        second = self.publish()
        self.assertEqual(first["release"].sequence, 1)
        self.assertEqual(second["release"].sequence, 2)
        self.assertNotEqual(first["package_path"], second["package_path"])
        self.assertTrue(Path(first["manifest_path"]).exists())
        self.assertTrue(Path(second["manifest_path"]).exists())

    def test_cambio_de_decision_de_licencia_bloquea_publicacion(self):
        self.fuente.estado_revision_licencia = "requiere_permiso"
        self.fuente.evidencia_licencia = "https://docs.python.org/3/license.html"
        self.fuente.alcance_licencia = ""
        self.fuente.nota_revision_licencia = "Cambio posterior."
        self.fuente.save(update_fields=[
            "estado_revision_licencia", "evidencia_licencia",
            "alcance_licencia", "nota_revision_licencia",
        ])
        with self.assertRaisesMessage(PublicationError, "cambió"):
            self.publish()

    def test_clave_con_permisos_abiertos_se_rechaza(self):
        os.chmod(self.key_path, 0o644)
        with self.assertRaisesMessage(PublicationError, "permisos exclusivos"):
            self.publish()

    def test_zip_es_reproducible_con_identidad_y_contenido_iguales(self):
        package_id = "6b9f5b77-4a4d-4a9d-a8aa-1b29d3b3a111"
        documents = [(str(self.leccion.clave_contenido), b'{"lesson":"same"}')]
        first = _build_deterministic_zip(package_id, "1.0.0", documents)
        second = _build_deterministic_zip(package_id, "1.0.0", documents)
        self.assertEqual(first, second)

    def test_contador_rechaza_saltos_manuales(self):
        counter = SecuenciaPublicacionConocimiento.objects.get(channel="stable")
        counter.siguiente += 5
        with self.assertRaises(ValidationError):
            counter.save()
        counter.refresh_from_db()
        self.assertEqual(counter.siguiente, 1)

    def test_canales_mantienen_secuencias_independientes(self):
        stable = self.publish()
        beta = publicar_paquete_conocimiento(
            channel="beta",
            package_version="1.0.0",
            minimum_app_version="1.0.0",
            base_url="https://cdn.codeguard.example/beta",
            allowed_hosts={"cdn.codeguard.example"},
            key_id="test-ed25519",
            private_key_path=self.key_path,
            output_directory=self.output,
        )
        self.assertEqual(stable["release"].sequence, 1)
        self.assertEqual(beta["release"].sequence, 1)
