"""Pruebas del ciclo de entrega y evaluación segura de ejercicios."""

from django.contrib.auth import get_user_model
from django.core.exceptions import ProtectedError, ValidationError
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.roadmaps.models import (
    ConfiguracionEvaluacion,
    EjercicioLeccion,
    Etapa,
    IntentoEjercicio,
    Leccion,
    Modulo,
    Progreso,
    Roadmap,
)
from apps.roadmaps.attempts import registrar_intento_ejercicio


@override_settings(AUTH_DISABLED=True)
class IntentosEjercicioTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="estudiante", password="ClaveSegura123!"
        )
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO pruebas", edicion="test")
        self.etapa = Etapa.objects.create(
            roadmap=self.roadmap, numero=0, titulo="Fundamentos"
        )
        self.modulo = Modulo.objects.create(
            etapa=self.etapa, numero="0.1", titulo="Introducción"
        )
        self.leccion = Leccion.objects.create(
            modulo=self.modulo, titulo="Variables"
        )
        self.ejercicio = EjercicioLeccion.objects.create(
            leccion=self.leccion,
            titulo="Declara una variable",
            enunciado="Declara una variable llamada nombre.",
            lenguaje="Python",
            publicado=True,
        )

    def test_evaluador_exacto_registra_intento_aprobado(self):
        ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio,
            tipo="respuesta_exacta",
            configuracion={
                "respuesta_esperada": "nombre = 'Ada'",
                "normalizar_espacios": True,
            },
        )

        intento = registrar_intento_ejercicio(
            self.usuario, self.ejercicio, "nombre   = 'Ada'"
        )

        self.assertEqual(intento.resultado, "aprobado")
        self.assertEqual(intento.puntuacion, 100)
        self.assertEqual(intento.version_evaluacion, 1)
        self.assertIsNotNone(intento.evaluado_en)

    def test_evaluador_exacto_rechaza_respuesta_incorrecta(self):
        ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio,
            tipo="respuesta_exacta",
            configuracion={"respuesta_esperada": "nombre = 'Ada'"},
        )

        intento = registrar_intento_ejercicio(
            self.usuario, self.ejercicio, "nombre = 'Grace'"
        )

        self.assertEqual(intento.resultado, "no_aprobado")
        self.assertEqual(intento.puntuacion, 0)

    def test_evaluador_de_codigo_es_estatico_y_reproducible(self):
        ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio,
            tipo="codigo_contiene",
            configuracion={
                "fragmentos_requeridos": ["nombre =", "print(nombre)"],
                "fragmentos_prohibidos": ["eval("],
            },
        )

        intento = registrar_intento_ejercicio(
            self.usuario, self.ejercicio, "nombre = 'Ada'\nprint(nombre)"
        )

        self.assertEqual(intento.resultado, "criterios_cumplidos")
        self.assertEqual(intento.detalles["tipo_comprobacion"], "estatica")
        self.assertEqual(intento.puntuacion, 100)

    def test_fragmento_prohibido_impide_aprobacion(self):
        ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio,
            tipo="codigo_contiene",
            configuracion={
                "fragmentos_requeridos": ["nombre ="],
                "fragmentos_prohibidos": ["eval("],
            },
        )

        intento = registrar_intento_ejercicio(
            self.usuario, self.ejercicio, "nombre = eval('Ada')"
        )

        self.assertEqual(intento.resultado, "no_aprobado")
        self.assertEqual(intento.puntuacion, 0)

    def test_sin_evaluador_guarda_entrega_pendiente(self):
        intento = registrar_intento_ejercicio(
            self.usuario, self.ejercicio, "nombre = 'Ada'"
        )

        self.assertEqual(intento.resultado, "pendiente_revision")
        self.assertIsNone(intento.puntuacion)
        self.assertIsNone(intento.evaluado_en)

    def test_configuracion_invalida_no_crea_intento(self):
        ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio,
            tipo="respuesta_exacta",
            configuracion={"respuesta_esperada": ""},
        )

        with self.assertRaises(ValidationError):
            registrar_intento_ejercicio(
                self.usuario, self.ejercicio, "respuesta cualquiera"
            )

        self.assertFalse(IntentoEjercicio.objects.filter(ejercicio=self.ejercicio).exists())

    def test_limite_de_caracteres_se_aplica_antes_de_guardar(self):
        with self.assertRaises(ValidationError):
            registrar_intento_ejercicio(
                self.usuario, self.ejercicio, "x" * 20001
            )
        self.assertFalse(IntentoEjercicio.objects.filter(ejercicio=self.ejercicio).exists())

    def test_leccion_se_completa_al_aprobar_todos_los_ejercicios_obligatorios(self):
        segundo = EjercicioLeccion.objects.create(
            leccion=self.leccion,
            titulo="Muestra la variable",
            enunciado="Muestra el valor de nombre.",
            publicado=True,
        )
        ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio,
            tipo="respuesta_exacta",
            configuracion={"respuesta_esperada": "nombre = 'Ada'"},
            permite_completar_leccion=True,
        )
        ConfiguracionEvaluacion.objects.create(
            ejercicio=segundo,
            tipo="respuesta_exacta",
            configuracion={"respuesta_esperada": "print(nombre)"},
            permite_completar_leccion=True,
        )

        registrar_intento_ejercicio(self.usuario, self.ejercicio, "nombre = 'Ada'")
        progreso = Progreso.objects.filter(usuario=self.usuario, leccion=self.leccion).first()
        self.assertIsNone(progreso)

        registrar_intento_ejercicio(self.usuario, segundo, "print(nombre)")
        progreso = Progreso.objects.get(usuario=self.usuario, leccion=self.leccion)
        self.assertEqual(progreso.estado, "completado")
        self.assertEqual(progreso.porcentaje, 100)
        self.assertIsNotNone(progreso.fecha_completado)

    def test_comprobacion_estatica_no_completa_la_leccion_por_defecto(self):
        ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio,
            tipo="codigo_contiene",
            configuracion={"fragmentos_requeridos": ["nombre ="]},
        )

        intento = registrar_intento_ejercicio(
            self.usuario, self.ejercicio, "nombre = 'Ada'"
        )

        self.assertEqual(intento.resultado, "criterios_cumplidos")
        self.assertFalse(
            Progreso.objects.filter(usuario=self.usuario, leccion=self.leccion).exists()
        )

    def test_ejercicio_no_publicado_no_admite_entrega(self):
        self.ejercicio.publicado = False
        self.ejercicio.save(update_fields=["publicado"])

        with self.assertRaises(ValidationError):
            registrar_intento_ejercicio(self.usuario, self.ejercicio, "respuesta")

        self.assertFalse(IntentoEjercicio.objects.filter(ejercicio=self.ejercicio).exists())



    def test_version_contenido_conserva_snapshot_y_fuente(self):
        from apps.roadmaps.models import (
            FuenteConocimiento,
            ReferenciaFuenteContenido,
            VersionContenidoLeccion,
        )

        fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation",
            titulo="Python Language Reference",
            url_canonica="https://docs.python.org/3/reference/",
            edicion="3",
            identificador_licencia="PSF-2.0",
            url_licencia="https://docs.python.org/3/license.html",
        )
        version = VersionContenidoLeccion.objects.create(
            leccion=self.leccion,
            numero_version=1,
            estado="revision",
            snapshot={
                "objetivos": ["Comprender variables"],
                "teoria_tecnica": "Una variable enlaza un nombre con un objeto.",
                "ejemplos": [],
                "ejercicios": [],
            },
            sha256="a" * 64,
        )
        referencia = ReferenciaFuenteContenido.objects.create(
            version=version, fuente=fuente, rol="principal"
        )

        self.assertEqual(version.fuentes.get(), fuente)
        self.assertEqual(referencia.version.snapshot["objetivos"][0], "Comprender variables")
        self.assertEqual(version.sha256, "a" * 64)

    def test_no_se_permiten_dos_versiones_publicadas_para_una_leccion(self):
        from django.db import IntegrityError, transaction
        from apps.roadmaps.models import VersionContenidoLeccion

        datos = {
            "leccion": self.leccion,
            "estado": "publicada",
            "snapshot": {"teoria_tecnica": "Contenido aprobado"},
            "sha256": "b" * 64,
        }
        VersionContenidoLeccion.objects.create(numero_version=1, **datos)
        with self.assertRaises(IntegrityError), transaction.atomic():
            VersionContenidoLeccion.objects.create(numero_version=2, **datos)

    def test_recursos_didacticos_tienen_identificadores_uuid_estables(self):
        from apps.roadmaps.models import EjemploLeccion

        ejemplo = EjemploLeccion.objects.create(
            leccion=self.leccion, titulo="Ejemplo de variable", codigo="nombre = 'Ada'"
        )
        segundo = EjercicioLeccion.objects.create(
            leccion=self.leccion, titulo="Segundo ejercicio", enunciado="Declara otra variable."
        )
        for recurso in (self.leccion, ejemplo, self.ejercicio, segundo):
            with self.subTest(recurso=recurso):
                self.assertIsNotNone(recurso.clave_contenido)
                self.assertEqual(recurso.clave_contenido.version, 4)
        self.assertNotEqual(self.ejercicio.clave_contenido, segundo.clave_contenido)

    def test_no_se_puede_eliminar_ejercicio_con_intentos_historicos(self):
        IntentoEjercicio.objects.create(
            ejercicio=self.ejercicio, usuario=self.usuario, respuesta="nombre = 'Ada'"
        )
        with self.assertRaises(ProtectedError):
            self.ejercicio.delete()
        self.assertTrue(IntentoEjercicio.objects.filter(ejercicio=self.ejercicio).exists())

    def test_no_se_puede_eliminar_evaluador_referenciado_por_intento(self):
        evaluador = ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio, tipo="respuesta_exacta",
            configuracion={"respuesta_esperada": "nombre = 'Ada'"},
        )
        IntentoEjercicio.objects.create(
            ejercicio=self.ejercicio, usuario=self.usuario, respuesta="nombre = 'Ada'",
            configuracion_evaluacion=evaluador, version_evaluacion=evaluador.version,
        )
        with self.assertRaises(ProtectedError):
            evaluador.delete()
        self.assertTrue(ConfiguracionEvaluacion.objects.filter(pk=evaluador.pk).exists())

    def test_vista_guarda_intento_y_muestra_historial(self):
        ConfiguracionEvaluacion.objects.create(
            ejercicio=self.ejercicio,
            tipo="respuesta_exacta",
            configuracion={"respuesta_esperada": "nombre = 'Ada'"},
        )

        response = self.client.post(
            reverse("roadmaps:enviar_intento", args=[self.ejercicio.id]),
            {"respuesta": "nombre = 'Ada'"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            IntentoEjercicio.objects.filter(
                usuario=self.usuario, ejercicio=self.ejercicio, resultado="aprobado"
            ).exists()
        )
        response = self.client.get(
            reverse("roadmaps:leccion_detalle", args=[self.leccion.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Últimos intentos")
        self.assertContains(response, "Aprobado")
