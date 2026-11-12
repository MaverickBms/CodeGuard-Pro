"""Pruebas del contrato criptográfico y estructural de distribución."""
import base64
import hashlib
import io
import json
import stat
import uuid
import zipfile

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from django.test import SimpleTestCase

from apps.roadmaps.distribution import (
    DistributionError,
    validate_manifest_structure,
    validate_package_archive,
    verify_signed_manifest,
)


class DistribucionFirmadaTests(SimpleTestCase):
    def setUp(self):
        self.private_key = Ed25519PrivateKey.generate()
        public_bytes = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        self.trusted_keys = {"test-key-1": base64.b64encode(public_bytes).decode("ascii")}
        self.package_id = str(uuid.uuid4())
        self.lesson_id = str(uuid.uuid4())
        self.allowed_hosts = {"cdn.codeguard.example"}

    def manifest_dict(self, *, sequence=10, package=None):
        package_bytes = b"placeholder"
        return {
            "manifest_version": 1,
            "channel": "stable",
            "sequence": sequence,
            "published_at": "2026-11-11T18:00:00Z",
            "minimum_app_version": "1.0.0",
            "content_schema_version": 1,
            "package": package or {
                "package_id": self.package_id,
                "package_version": "2026.11.1",
                "url": "https://cdn.codeguard.example/stable/package.zip",
                "size_bytes": len(package_bytes),
                "sha256": hashlib.sha256(package_bytes).hexdigest(),
            },
            "key_id": "test-key-1",
        }

    def sign(self, manifest):
        raw = json.dumps(manifest, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        signature = base64.b64encode(self.private_key.sign(raw))
        return raw, signature

    def verify(self, raw, signature, **kwargs):
        return verify_signed_manifest(
            raw,
            signature,
            trusted_public_keys=self.trusted_keys,
            allowed_hosts=self.allowed_hosts,
            expected_channel="stable",
            app_version="1.0.0",
            **kwargs,
        )

    def build_zip(self, *, extra=None, indexed_path=None, symlink=False):
        payload_path = indexed_path or f"payload/lessons/{self.lesson_id}.json"
        document = {
            "schema_version": 1,
            "resumen_cambios": "Versión de prueba.",
            "snapshot": {
                "esquema_version": 1,
                "leccion": {
                    "clave": self.lesson_id,
                    "titulo": "Variables",
                    "descripcion": "Introducción",
                    "tipo": "concepto",
                },
                "contenido": {
                    "objetivos_aprendizaje": "Comprender variables.",
                    "teoria_tecnica": "Una variable enlaza un nombre con un objeto.",
                    "explicacion_sencilla": "Un nombre permite referirse a un valor.",
                    "notas": "",
                },
                "ejemplos": [],
                "ejercicios": [],
            },
            "fuentes": [{
                "clave": str(uuid.uuid4()),
                "rol": "principal",
                "localizador": "Sección de referencia",
                "nota_atribucion": "Referencia conceptual.",
                "uso_declarado": "original",
            }],
        }
        payload = json.dumps(document, separators=(",", ":")).encode("utf-8")
        index = {
            "schema_version": 1,
            "package_id": self.package_id,
            "package_version": "2026.11.1",
            "content_schema_version": 1,
            "files": [{
                "path": payload_path,
                "size_bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }],
        }
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("package-index.json", json.dumps(index, separators=(",", ":")))
            if symlink:
                info = zipfile.ZipInfo(payload_path)
                info.create_system = 3
                info.external_attr = (stat.S_IFLNK | 0o777) << 16
                archive.writestr(info, "target")
            else:
                archive.writestr(payload_path, payload)
            if extra:
                archive.writestr(extra[0], extra[1])
        return buffer.getvalue()

    def manifest_for_zip(self, package_bytes):
        manifest = self.manifest_dict(package={
            "package_id": self.package_id,
            "package_version": "2026.11.1",
            "url": "https://cdn.codeguard.example/stable/package.zip",
            "size_bytes": len(package_bytes),
            "sha256": hashlib.sha256(package_bytes).hexdigest(),
        })
        return manifest

    def test_manifest_firmado_se_verifica(self):
        raw, signature = self.sign(self.manifest_dict())
        result = self.verify(raw, signature)
        self.assertFalse(result["unchanged"])
        self.assertEqual(result["manifest"]["sequence"], 10)

    def test_firma_alterada_se_rechaza(self):
        raw, signature = self.sign(self.manifest_dict())
        altered = signature[:-2] + (b"AA" if signature[-2:] != b"AA" else b"BB")
        with self.assertRaisesMessage(DistributionError, "firma"):
            self.verify(raw, altered)

    def test_clave_no_confiable_se_rechaza(self):
        raw, signature = self.sign(self.manifest_dict())
        manifest = json.loads(raw)
        manifest["key_id"] = "unknown"
        raw_unknown, signature_unknown = self.sign(manifest)
        with self.assertRaisesMessage(DistributionError, "almacén de confianza"):
            self.verify(raw_unknown, signature_unknown)

    def test_manifiesto_rechaza_host_no_autorizado(self):
        manifest = self.manifest_dict()
        manifest["package"]["url"] = "https://attacker.example/package.zip"
        raw, signature = self.sign(manifest)
        with self.assertRaisesMessage(DistributionError, "host autorizado"):
            self.verify(raw, signature)


    def test_manifiesto_rechaza_semver_invalido(self):
        manifest = self.manifest_dict()
        manifest["minimum_app_version"] = "01.0.0"
        raw, signature = self.sign(manifest)
        with self.assertRaisesMessage(DistributionError, "SemVer"):
            self.verify(raw, signature)

    def test_manifiesto_rechaza_claves_json_duplicadas(self):
        raw = b'{"manifest_version":1,"manifest_version":1}'
        with self.assertRaisesMessage(DistributionError, "duplicada"):
            validate_manifest_structure(raw, allowed_hosts=self.allowed_hosts)

    def test_manifiesto_rechaza_downgrade_y_replay_modificado(self):
        manifest = self.manifest_dict(sequence=9)
        raw, signature = self.sign(manifest)
        with self.assertRaisesMessage(DistributionError, "antiguo"):
            self.verify(raw, signature, current_sequence=10, current_manifest_sha256="a" * 64)

        manifest = self.manifest_dict(sequence=10)
        raw, signature = self.sign(manifest)
        with self.assertRaisesMessage(DistributionError, "secuencia"):
            self.verify(raw, signature, current_sequence=10, current_manifest_sha256="b" * 64)

    def test_mismo_manifiesto_instalado_es_no_op(self):
        raw, signature = self.sign(self.manifest_dict(sequence=10))
        digest = hashlib.sha256(raw).hexdigest()
        result = self.verify(raw, signature, current_sequence=10, current_manifest_sha256=digest)
        self.assertTrue(result["unchanged"])

    def test_version_minima_de_aplicacion(self):
        manifest = self.manifest_dict()
        manifest["minimum_app_version"] = "2.0.0"
        raw, signature = self.sign(manifest)
        with self.assertRaisesMessage(DistributionError, "más reciente"):
            self.verify(raw, signature)

    def test_paquete_zip_valido(self):
        package_bytes = self.build_zip()
        manifest = self.manifest_for_zip(package_bytes)
        result = validate_package_archive(package_bytes, manifest=manifest)
        self.assertEqual(len(result["payloads"]), 1)
        self.assertIn(f"payload/lessons/{self.lesson_id}.json", result["payloads"])


    def test_manifiesto_rechaza_esquema_transporte_y_credenciales(self):
        for url in (
            "http://cdn.codeguard.example/package.zip",
            "https://user:secret@cdn.codeguard.example/package.zip",
            "https://@cdn.codeguard.example/package.zip",
            "https://cdn.codeguard.example:8443/package.zip",
        ):
            with self.subTest(url=url):
                manifest = self.manifest_dict()
                manifest["package"]["url"] = url
                raw, signature = self.sign(manifest)
                with self.assertRaises(DistributionError):
                    self.verify(raw, signature)

    def test_paquete_rechaza_uuid_de_archivo_distinto_al_snapshot(self):
        other_lesson = str(uuid.uuid4())
        package_bytes = self.build_zip(indexed_path=f"payload/lessons/{other_lesson}.json")
        manifest = self.manifest_for_zip(package_bytes)
        with self.assertRaisesMessage(DistributionError, "no coincide"):
            validate_package_archive(package_bytes, manifest=manifest)

    def test_paquete_rechaza_hash_incorrecto(self):
        package_bytes = self.build_zip()
        manifest = self.manifest_for_zip(package_bytes)
        manifest["package"]["sha256"] = "0" * 64
        with self.assertRaisesMessage(DistributionError, "SHA-256"):
            validate_package_archive(package_bytes, manifest=manifest)

    def test_paquete_rechaza_ruta_traversal(self):
        package_bytes = self.build_zip(extra=("../outside.txt", b"x"))
        manifest = self.manifest_for_zip(package_bytes)
        with self.assertRaisesMessage(DistributionError, "ruta"):
            validate_package_archive(package_bytes, manifest=manifest)

    def test_paquete_rechaza_symlink(self):
        package_bytes = self.build_zip(symlink=True)
        manifest = self.manifest_for_zip(package_bytes)
        with self.assertRaisesMessage(DistributionError, "tipo de archivo"):
            validate_package_archive(package_bytes, manifest=manifest)

    def test_paquete_rechaza_archivo_no_declarado(self):
        package_bytes = self.build_zip(extra=("payload/extra.json", b"{}"))
        manifest = self.manifest_for_zip(package_bytes)
        with self.assertRaisesMessage(DistributionError, "no declarados"):
            validate_package_archive(package_bytes, manifest=manifest)

    def build_zip_with_source_catalog(
        self,
        *,
        include_source=True,
        source_url="https://docs.python.org/3/reference/",
        license_state="compatible",
        usage="original",
    ):
        original = self.build_zip()
        buffer = io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(original), "r") as source_archive:
            payload_info = next(
                info for info in source_archive.infolist()
                if info.filename.startswith("payload/lessons/")
            )
            document = json.loads(source_archive.read(payload_info.filename))
            source_uuid = document["fuentes"][0]["clave"]
            document["fuentes"][0]["uso_declarado"] = usage
            updated_payload = json.dumps(
                document, separators=(",", ":")
            ).encode("utf-8")
            with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as target:
                for info in source_archive.infolist():
                    payload = source_archive.read(info.filename)
                    if info.filename == "package-index.json":
                        index = json.loads(payload)
                        index["schema_version"] = 2
                        index["files"][0]["size_bytes"] = len(updated_payload)
                        index["files"][0]["sha256"] = hashlib.sha256(updated_payload).hexdigest()
                        if include_source:
                            index["sources"] = [{
                                "clave": source_uuid,
                                "publicador": "Python Software Foundation",
                                "titulo": "Python Language Reference",
                                "url_canonica": source_url,
                                "edicion": "3",
                                "identificador_licencia": "PSF-2.0",
                                "url_licencia": "https://docs.python.org/3/license.html",
                                "estado_revision_licencia": license_state,
                                "evidencia_licencia": "https://docs.python.org/3/license.html",
                                "alcance_licencia": "Redistribución con atribución." if license_state == "compatible" else "",
                                "nota_revision_licencia": "Revisión editorial documentada.",
                                "revisada_en": "2026-11-12T10:00:00+00:00",
                            }]
                        payload = json.dumps(index, separators=(",", ":")).encode("utf-8")
                    elif info.filename == payload_info.filename:
                        payload = updated_payload
                    target.writestr(info.filename, payload)
        return buffer.getvalue()

    def test_indice_v2_valida_catalogo_de_fuentes(self):
        package_bytes = self.build_zip_with_source_catalog()
        result = validate_package_archive(
            package_bytes, manifest=self.manifest_for_zip(package_bytes)
        )
        self.assertEqual(len(result["sources"]), 1)
        self.assertEqual(
            result["sources"][next(iter(result["sources"]))]["estado_revision_licencia"],
            "compatible",
        )

    def test_indice_v2_rechaza_catalogo_incompleto(self):
        package_bytes = self.build_zip_with_source_catalog(include_source=False)
        with self.assertRaisesMessage(DistributionError, "no coincide exactamente"):
            validate_package_archive(
                package_bytes, manifest=self.manifest_for_zip(package_bytes)
            )

    def test_indice_v2_rechaza_solo_referencia_con_uso_adaptado(self):
        package_bytes = self.build_zip_with_source_catalog(
            license_state="solo_referencia",
            usage="adaptacion",
        )
        with self.assertRaisesMessage(DistributionError, "solo permite contenido original"):
            validate_package_archive(
                package_bytes, manifest=self.manifest_for_zip(package_bytes)
            )

    def test_indice_v2_rechaza_url_http_en_catalogo(self):
        package_bytes = self.build_zip_with_source_catalog(
            source_url="http://docs.python.org/3/reference/"
        )
        with self.assertRaisesMessage(DistributionError, "URL HTTPS"):
            validate_package_archive(
                package_bytes, manifest=self.manifest_for_zip(package_bytes)
            )
