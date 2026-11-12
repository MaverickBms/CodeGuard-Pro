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





    def test_ciclo_editorial_revisa_aprueba_y_publica_versiones(self):
        from django.core.exceptions import ValidationError
        from apps.roadmaps.knowledge import (
            aprobar_version_contenido,
            crear_version_contenido_leccion,
            enviar_version_a_revision,
            publicar_version_contenido,
        )
        from apps.roadmaps.models import ContenidoLeccion, EjemploLeccion, FuenteConocimiento

        editor = get_user_model().objects.create_user(
            username="editor", password="ClaveSegura123!", is_staff=True, is_active=True
        )
        ContenidoLeccion.objects.create(
            leccion=self.leccion,
            teoria_tecnica="Una variable enlaza un nombre con un objeto.",
            explicacion_sencilla="Un nombre permite referirse a un valor.",
        )
        EjemploLeccion.objects.create(
            leccion=self.leccion, titulo="Asignación", codigo="nombre = 'Ada'", publicado=True
        )
        fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation",
            titulo="Python Language Reference",
            url_canonica="https://docs.python.org/3/reference/",
            edicion="3",
        )

        primera = crear_version_contenido_leccion(
            self.leccion, fuentes=[(fuente, "principal", "Assignment statements", "Fuente oficial")]
        )
        with self.assertRaises(ValidationError):
            publicar_version_contenido(primera.pk, actor=editor)

        primera = enviar_version_a_revision(primera.pk, actor=editor)
        self.assertEqual(primera.enviada_por, editor)
        self.assertIsNotNone(primera.enviada_en)
        with self.assertRaises(ValidationError):
            primera.snapshot["contenido"]["teoria_tecnica"] = "Alterado"
            primera.save()

        aprobar_version_contenido(primera.pk, actor=editor)
        primera = publicar_version_contenido(primera.pk, actor=editor)
        self.assertEqual(primera.estado, "publicada")
        self.assertEqual(primera.revisada_por, editor)
        self.assertEqual(primera.publicada_por, editor)
        self.assertIsNotNone(primera.publicada_en)

        ContenidoLeccion.objects.filter(leccion=self.leccion).update(
            teoria_tecnica="Una variable asocia un identificador con un objeto."
        )
        segunda = crear_version_contenido_leccion(
            self.leccion, fuentes=[(fuente, "principal", "Names", "Fuente oficial")]
        )
        enviar_version_a_revision(segunda.pk, actor=editor)
        aprobar_version_contenido(segunda.pk, actor=editor)
        segunda = publicar_version_contenido(segunda.pk, actor=editor)

        primera.refresh_from_db()
        self.assertEqual(segunda.estado, "publicada")
        self.assertEqual(primera.estado, "sustituida")
        self.assertEqual(
            self.leccion.versiones_contenido.filter(estado="publicada").count(), 1
        )

    def test_transicion_editorial_exige_usuario_staff_activo(self):
        from django.core.exceptions import ValidationError
        from apps.roadmaps.knowledge import enviar_version_a_revision

        with self.assertRaises(ValidationError):
            enviar_version_a_revision(1, actor=self.usuario)

    def test_retirada_exige_motivo_y_conserva_snapshot(self):
        from django.core.exceptions import ValidationError
        from apps.roadmaps.knowledge import (
            aprobar_version_contenido,
            crear_version_contenido_leccion,
            enviar_version_a_revision,
            publicar_version_contenido,
            retirar_version_publicada,
        )
        from apps.roadmaps.models import ContenidoLeccion, FuenteConocimiento

        editor = get_user_model().objects.create_user(
            username="editor_retiro", password="ClaveSegura123!", is_staff=True
        )
        ContenidoLeccion.objects.create(
            leccion=self.leccion,
            teoria_tecnica="Teoría técnica.",
            explicacion_sencilla="Explicación sencilla.",
        )
        fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation",
            titulo="Python Docs",
            url_canonica="https://docs.python.org/3/",
        )
        version = crear_version_contenido_leccion(
            self.leccion, fuentes=[(fuente, "principal", "", "")]
        )
        enviar_version_a_revision(version.pk, actor=editor)
        aprobar_version_contenido(version.pk, actor=editor)
        publicar_version_contenido(version.pk, actor=editor)
        snapshot_original = version.snapshot

        with self.assertRaises(ValidationError):
            retirar_version_publicada(version.pk, actor=editor, motivo=" ")
        retirada = retirar_version_publicada(
            version.pk, actor=editor, motivo="La referencia requiere actualización."
        )
        self.assertEqual(retirada.estado, "retirada")
        self.assertEqual(retirada.snapshot, snapshot_original)
        self.assertEqual(retirada.motivo_retiro, "La referencia requiere actualización.")
        self.assertEqual(retirada.retirada_por, editor)
        self.assertIsNotNone(retirada.retirada_en)
        self.assertEqual(retirada.revisada_por, editor)

    def test_servicio_crea_snapshot_determinista_con_fuentes_y_recursos_publicados(self):
        import hashlib
        import json
        from apps.roadmaps.knowledge import crear_version_contenido_leccion
        from apps.roadmaps.models import (
            ContenidoLeccion,
            EjemploLeccion,
            FuenteConocimiento,
        )

        ContenidoLeccion.objects.create(
            leccion=self.leccion,
            objetivos_aprendizaje="Comprender variables",
            teoria_tecnica="Una variable enlaza un nombre con un objeto.",
            explicacion_sencilla="Un nombre permite referirse a un valor.",
            publicado=True,
        )
        EjemploLeccion.objects.create(
            leccion=self.leccion,
            titulo="Asignación",
            codigo="nombre = 'Ada'",
            publicado=True,
        )
        EjemploLeccion.objects.create(
            leccion=self.leccion,
            titulo="Borrador no publicado",
            codigo="secreto = True",
            publicado=False,
        )
        fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation",
            titulo="Python Language Reference",
            url_canonica="https://docs.python.org/3/reference/",
            edicion="3",
        )

        version = crear_version_contenido_leccion(
            self.leccion,
            resumen_cambios="Primera versión editorial",
            fuentes=[(fuente, "principal", "Assignment statements", "Referencia del lenguaje")],
        )
        serializado = json.dumps(
            version.snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )

        self.assertEqual(version.numero_version, 1)
        self.assertEqual(version.estado, "borrador")
        self.assertEqual(version.sha256, hashlib.sha256(serializado.encode("utf-8")).hexdigest())
        self.assertEqual(len(version.snapshot["ejemplos"]), 1)
        self.assertEqual(version.fuentes.get(), fuente)

        ContenidoLeccion.objects.filter(leccion=self.leccion).update(
            teoria_tecnica="Texto revisado posteriormente."
        )
        segunda = crear_version_contenido_leccion(self.leccion)
        self.assertEqual(segunda.numero_version, 2)
        self.assertIn("Una variable enlaza", version.snapshot["contenido"]["teoria_tecnica"])

    def test_servicio_no_versiona_leccion_sin_contenido_completo(self):
        from django.core.exceptions import ValidationError
        from apps.roadmaps.knowledge import crear_version_contenido_leccion
        from apps.roadmaps.models import ContenidoLeccion

        ContenidoLeccion.objects.create(
            leccion=self.leccion,
            teoria_tecnica="Solo teoría, falta explicación sencilla.",
        )
        with self.assertRaises(ValidationError):
            crear_version_contenido_leccion(self.leccion)

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
            estado="borrador",
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


    def test_hash_snapshot_rechaza_formato_invalido(self):
        from django.core.exceptions import ValidationError
        from apps.roadmaps.models import VersionContenidoLeccion

        version = VersionContenidoLeccion(
            leccion=self.leccion,
            numero_version=1,
            snapshot={"teoria_tecnica": "Contenido"},
            sha256="no-es-un-hash",
        )
        with self.assertRaises(ValidationError):
            version.full_clean()

    def test_versiones_no_admiten_mutaciones_masivas(self):
        from django.core.exceptions import ValidationError
        from apps.roadmaps.models import VersionContenidoLeccion

        version = VersionContenidoLeccion.objects.create(
            leccion=self.leccion,
            numero_version=1,
            snapshot={"contenido": "original"},
            sha256="b" * 64,
        )
        with self.assertRaises(ValidationError):
            VersionContenidoLeccion.objects.filter(pk=version.pk).update(
                snapshot={"contenido": "alterado"}
            )
        with self.assertRaises(ValidationError):
            VersionContenidoLeccion.objects.filter(pk=version.pk).delete()
        with self.assertRaises(ValidationError):
            VersionContenidoLeccion.objects.bulk_create([
                VersionContenidoLeccion(
                    leccion=self.leccion,
                    numero_version=2,
                    estado="publicada",
                    snapshot={"contenido": "no permitido"},
                    sha256="c" * 64,
                )
            ])

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


    def test_comando_crear_version_genera_borrador_con_fuente(self):
        from io import StringIO
        from django.core.management import call_command
        from apps.roadmaps.models import ContenidoLeccion, FuenteConocimiento, VersionContenidoLeccion

        ContenidoLeccion.objects.create(
            leccion=self.leccion, teoria_tecnica="Teoría técnica.",
            explicacion_sencilla="Explicación sencilla.",
        )
        fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation", titulo="Python Docs",
            url_canonica="https://docs.python.org/3/",
        )
        salida = StringIO()
        call_command(
            "crear_version_leccion", leccion=self.leccion.pk,
            fuente_id=[fuente.pk], resumen="Primera versión", stdout=salida,
        )
        version = VersionContenidoLeccion.objects.get(leccion=self.leccion)
        self.assertEqual(version.estado, "borrador")
        self.assertEqual(version.fuentes.get(), fuente)
        self.assertIn("Versión borrador creada", salida.getvalue())

    def test_comando_gestionar_version_envia_a_revision(self):
        from io import StringIO
        from django.core.management import call_command
        from apps.roadmaps.models import ContenidoLeccion, FuenteConocimiento
        from apps.roadmaps.knowledge import crear_version_contenido_leccion

        editor = get_user_model().objects.create_user(
            username="editor_cli", password="ClaveSegura123!", is_staff=True
        )
        ContenidoLeccion.objects.create(
            leccion=self.leccion, teoria_tecnica="Teoría técnica.",
            explicacion_sencilla="Explicación sencilla.",
        )
        fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation", titulo="Python Docs",
            url_canonica="https://docs.python.org/3/",
        )
        version = crear_version_contenido_leccion(
            self.leccion, fuentes=[(fuente, "principal", "", "")]
        )
        salida = StringIO()
        call_command(
            "gestionar_version_leccion", "enviar-revision",
            version=version.pk, usuario=editor.username, stdout=salida,
        )
        version.refresh_from_db()
        self.assertEqual(version.estado, "revision")
        self.assertEqual(version.enviada_por, editor)
        self.assertIn("estado=revision", salida.getvalue())

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
