"""Pruebas de restricciones del registro local de distribución."""
import hashlib
import uuid
from datetime import datetime, timezone

from django.db import IntegrityError, transaction
from django.test import TestCase

from apps.roadmaps.models import EstadoSincronizacion, PaqueteConocimientoInstalado


class RegistroPaquetesTests(TestCase):
    def crear_paquete(self, *, sequence, estado="verificado"):
        digest = hashlib.sha256(f"package-{sequence}".encode()).hexdigest()
        return PaqueteConocimientoInstalado.objects.create(
            package_id=uuid.uuid4(),
            package_version=f"2026.11.{sequence}",
            channel="stable",
            sequence=sequence,
            content_schema_version=1,
            sha256=digest,
            manifest_sha256=hashlib.sha256(f"manifest-{sequence}".encode()).hexdigest(),
            signature_key_id="release-key-2026",
            published_at=datetime(2026, 11, 11, tzinfo=timezone.utc),
            estado=estado,
        )

    def test_registra_historial_y_estado_por_canal(self):
        package = self.crear_paquete(sequence=1, estado="activo")
        state = EstadoSincronizacion.objects.create(channel="stable", active_package=package)
        self.assertEqual(state.active_package, package)
        self.assertEqual(PaqueteConocimientoInstalado.objects.filter(channel="stable").count(), 1)

    def test_un_solo_paquete_puede_estar_activo_por_canal(self):
        self.crear_paquete(sequence=1, estado="activo")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                self.crear_paquete(sequence=2, estado="activo")

    def test_secuencia_es_unica_por_canal(self):
        self.crear_paquete(sequence=1)
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                self.crear_paquete(sequence=1)

    def test_estado_de_sincronizacion_no_puede_borrar_paquete_referenciado(self):
        package = self.crear_paquete(sequence=1, estado="activo")
        EstadoSincronizacion.objects.create(channel="stable", active_package=package)
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                package.delete()
