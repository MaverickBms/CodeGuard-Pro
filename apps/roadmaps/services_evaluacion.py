"""Servicios de evaluación y corrección automática (Fase 4, ADR-011).

Evalúa quizzes de forma determinista para formatos objetivos y marca revisión
controlada para formatos abiertos. No ejecuta código del estudiante y no utiliza
IA para decidir la aprobación académica.
"""

from __future__ import annotations

import re
from typing import Any

from django.core.exceptions import ValidationError
from django.db import transaction

from apps.audit.services import registrar_evento

from .models import CumplimientoCriterio, CriterioFinalizacion, Progreso
from .models_evaluacion import Pregunta, Quiz, ResultadoEvaluacion, ResultadoPregunta
from .services import etapas_completadas


def _normalizar_texto(valor: Any, *, colapsar_espacios: bool = True) -> str:
    texto = "" if valor is None else str(valor)
    texto = texto.strip()
    if colapsar_espacios:
        texto = re.sub(r"\s+", " ", texto)
    return texto


def _extraer_respuesta_usuario(respuestas_usuario: dict, pregunta: Pregunta) -> Any:
    """Obtiene la respuesta enviada para una pregunta por id u orden."""
    if not isinstance(respuestas_usuario, dict):
        return None
    for clave in (str(pregunta.id), pregunta.id, str(pregunta.orden), pregunta.orden):
        if clave in respuestas_usuario:
            return respuestas_usuario[clave]
    return None


def _tema_repaso(pregunta: Pregunta) -> str:
    if pregunta.leccion_id:
        try:
            return str(pregunta.leccion)
        except Exception:
            return f"Lección {pregunta.leccion_id}"
    return pregunta.enunciado.strip()[:120]


def _evaluar_seleccion(pregunta: Pregunta, respuesta_usuario: Any) -> dict:
    datos = pregunta.datos_respuesta if isinstance(pregunta.datos_respuesta, dict) else {}
    opciones = datos.get("opciones", [])
    if not isinstance(opciones, list):
        opciones = []

    indices_correctos: list[int] = []
    valores_correctos: set[str] = set()
    for idx, opcion in enumerate(opciones):
        if isinstance(opcion, dict) and opcion.get("correcta"):
            indices_correctos.append(idx)
            valor = opcion.get("valor", opcion.get("texto", idx))
            valores_correctos.add(_normalizar_texto(valor))

    seleccion = respuesta_usuario
    if isinstance(seleccion, dict):
        seleccion = seleccion.get("opcion", seleccion.get("valor", seleccion.get("respuesta")))

    if seleccion is None:
        es_correcta = False
    elif isinstance(seleccion, int):
        es_correcta = seleccion in indices_correctos
    elif isinstance(seleccion, str) and seleccion.isdigit():
        es_correcta = int(seleccion) in indices_correctos
    else:
        es_correcta = _normalizar_texto(seleccion) in valores_correctos

    return {
        "correcta": es_correcta,
        "puntuacion": 100 if es_correcta else 0,
        "requiere_revision": False,
        "retroalimentacion": "Respuesta correcta." if es_correcta else "Respuesta incorrecta. Revisa el concepto asociado.",
    }


def _evaluar_respuesta(pregunta: Pregunta, respuesta_usuario: Any) -> dict:
    datos = pregunta.datos_respuesta if isinstance(pregunta.datos_respuesta, dict) else {}
    esperada = datos.get("respuesta_esperada", "")
    sensible_mayusculas = bool(datos.get("sensible_mayusculas", False))
    normalizar_espacios = datos.get("normalizar_espacios", True) is not False

    enviada = respuesta_usuario
    if isinstance(enviada, dict):
        enviada = enviada.get("texto", enviada.get("respuesta", enviada.get("valor")))

    texto_enviado = _normalizar_texto(enviada, colapsar_espacios=normalizar_espacios)
    texto_esperado = _normalizar_texto(esperada, colapsar_espacios=normalizar_espacios)
    if not sensible_mayusculas:
        texto_enviado = texto_enviado.casefold()
        texto_esperado = texto_esperado.casefold()

    es_correcta = bool(texto_esperado) and texto_enviado == texto_esperado
    return {
        "correcta": es_correcta,
        "puntuacion": 100 if es_correcta else 0,
        "requiere_revision": False,
        "retroalimentacion": "Respuesta correcta." if es_correcta else "Respuesta incorrecta. Revisa el contenido del módulo.",
    }


def _evaluar_abierta(pregunta: Pregunta, respuesta_usuario: Any) -> dict:
    """Evalúa formatos abiertos: requiere revisión controlada, sin auto-aprobación."""
    datos = pregunta.datos_respuesta if isinstance(pregunta.datos_respuesta, dict) else {}
    criterios = datos.get("criterios", []) if isinstance(datos.get("criterios"), list) else []

    enviada = respuesta_usuario
    if isinstance(enviada, dict):
        enviada = enviada.get("texto", enviada.get("respuesta", enviada.get("valor")))
    texto = _normalizar_texto(enviada)

    if not texto:
        return {
            "correcta": False,
            "puntuacion": 0,
            "requiere_revision": True,
            "retroalimentacion": "Sin respuesta. La pregunta queda pendiente de revisión controlada.",
        }

    return {
        "correcta": False,
        "puntuacion": 0,
        "requiere_revision": True,
        "retroalimentacion": (
            "Respuesta registrada para revisión controlada. "
            f"Criterios de evaluación: {len(criterios)}."
        ),
    }


def _evaluar_pregunta(pregunta: Pregunta, respuesta_usuario: Any) -> dict:
    if pregunta.formato == Pregunta.FORMATO_SELECCION:
        return _evaluar_seleccion(pregunta, respuesta_usuario)
    if pregunta.formato == Pregunta.FORMATO_RESPUESTA:
        return _evaluar_respuesta(pregunta, respuesta_usuario)
    if pregunta.formato in (Pregunta.FORMATO_INTERPRETACION, Pregunta.FORMATO_RESOLUCION):
        return _evaluar_abierta(pregunta, respuesta_usuario)
    return {
        "correcta": False,
        "puntuacion": 0,
        "requiere_revision": True,
        "retroalimentacion": "Formato de pregunta no evaluable automáticamente.",
    }


@transaction.atomic
def evaluar_quiz(usuario, quiz: Quiz, respuestas_usuario: dict) -> ResultadoEvaluacion:
    """Evalúa un quiz, crea la evidencia por pregunta y el resultado global.

    - Formatos objetivos (selección, respuesta): corrección determinista.
    - Formatos abiertos (interpretación, resolución): ``requiere_revision=True``
      y no se auto-aprueban.
    - ``aprobado`` solo es True si no hay revisión pendiente y la puntuación
      alcanza el umbral del quiz.
    """
    if usuario is None or not getattr(usuario, "is_authenticated", False):
        raise ValidationError("Se requiere un usuario autenticado para evaluar el quiz.")
    if respuestas_usuario is None:
        respuestas_usuario = {}
    if not isinstance(respuestas_usuario, dict):
        raise ValidationError("Las respuestas del usuario deben enviarse como un objeto.")

    etapa = quiz.modulo.etapa if quiz.modulo_id else quiz.etapa
    if etapa is not None and etapa.esta_bloqueada_para(
        etapas_completadas(usuario, etapa.roadmap)
    ):
        raise ValidationError(
            "No puedes enviar esta evaluación hasta completar los prerrequisitos de la etapa."
        )

    preguntas = list(quiz.preguntas.all())
    total = len(preguntas)

    detalles_preguntas = []
    suma_puntuacion = 0
    temas_repaso = []
    requiere_revision_global = False

    for pregunta in preguntas:
        respuesta_usuario = _extraer_respuesta_usuario(respuestas_usuario, pregunta)
        evaluacion = _evaluar_pregunta(pregunta, respuesta_usuario)
        puntuacion_pregunta = int(evaluacion.get("puntuacion") or 0)
        suma_puntuacion += puntuacion_pregunta
        requiere_revision = bool(evaluacion.get("requiere_revision"))
        if requiere_revision:
            requiere_revision_global = True
        if (not evaluacion.get("correcta")) or requiere_revision:
            tema = _tema_repaso(pregunta)
            if tema not in temas_repaso:
                temas_repaso.append(tema)
        detalles_preguntas.append(
            {
                "pregunta": pregunta,
                "respuesta": respuesta_usuario,
                "correcta": bool(evaluacion.get("correcta")),
                "puntuacion": puntuacion_pregunta,
                "retroalimentacion": evaluacion.get("retroalimentacion", ""),
                "requiere_revision": requiere_revision,
            }
        )

    puntuacion_total = round(suma_puntuacion / total) if total > 0 else 0
    umbral = quiz.umbral_aprobacion
    aprobado = (not requiere_revision_global) and (puntuacion_total >= umbral)

    if requiere_revision_global:
        retroalimentacion = (
            "Evaluación registrada con preguntas pendientes de revisión controlada. "
            "La aprobación se definirá tras la revisión."
        )
    elif aprobado:
        retroalimentacion = "Evaluación aprobada según el umbral establecido."
    else:
        retroalimentacion = "Evaluación no aprobada. Revisa los temas señalados para repaso."

    resultado = ResultadoEvaluacion.objects.create(
        quiz=quiz,
        usuario=usuario,
        respuestas=respuestas_usuario,
        puntuacion=puntuacion_total,
        aprobado=aprobado,
        umbral_aprobacion=umbral,
        retroalimentacion=retroalimentacion,
        temas_repaso=temas_repaso,
        requiere_revision=requiere_revision_global,
    )

    for detalle in detalles_preguntas:
        ResultadoPregunta.objects.create(
            resultado=resultado,
            pregunta=detalle["pregunta"],
            correcta=detalle["correcta"],
            puntuacion=detalle["puntuacion"],
            respuesta=(
                detalle["respuesta"]
                if isinstance(detalle["respuesta"], dict)
                else {"valor": detalle["respuesta"]}
            ),
            retroalimentacion=detalle["retroalimentacion"],
            requiere_revision=detalle["requiere_revision"],
        )

    registrar_evento(
        "evaluacion_resultado_registrado",
        usuario=usuario,
        descripcion=(
            f"Quiz {quiz.id} ({quiz.nombre}); resultado {resultado.id}; "
            f"puntuación {puntuacion_total}; aprobado={aprobado}; "
            f"requiere_revision={requiere_revision_global}."
        ),
    )

    actualizar_progreso_por_evaluacion(usuario, quiz, resultado)
    return resultado


def actualizar_progreso_por_evaluacion(usuario, quiz: Quiz, resultado: ResultadoEvaluacion) -> Progreso | None:
    """Actualiza el progreso académico cuando una evaluación se aprueba.

    - Si el quiz está asociado a un módulo y el resultado está aprobado
      (sin revisión pendiente), marca el progreso del módulo como completado.
    - Si el quiz es un examen de etapa aprobado, intenta aprobar/homologar
      la etapa mediante criterios verificables (sin completación manual).
    - Registra eventos de auditoría de transiciones académicas.
    """
    if usuario is None or not getattr(usuario, "is_authenticated", False):
        return None
    if not resultado.aprobado or resultado.requiere_revision:
        return None

    progreso_modulo = None
    if quiz.modulo_id is not None:
        modulo = quiz.modulo
        etapa = modulo.etapa
        progreso_modulo, _ = Progreso.objects.get_or_create(
            usuario=usuario,
            etapa=etapa,
            modulo=modulo,
            leccion=None,
            actividad=None,
            defaults={"estado": "no_iniciado", "porcentaje": 0},
        )

        if progreso_modulo.estado != "completado":
            progreso_modulo.estado = "completado"
            progreso_modulo.porcentaje = 100
            from django.utils import timezone

            progreso_modulo.fecha_completado = timezone.now()
            progreso_modulo.save(
                update_fields=["estado", "porcentaje", "fecha_completado", "fecha_actualizacion"]
            )
            registrar_evento(
                "progreso_modulo_completado_por_evaluacion",
                usuario=usuario,
                descripcion=(
                    f"Módulo {modulo.id} ({modulo.titulo}) completado por evaluación; "
                    f"quiz {quiz.id} (v{quiz.version}); resultado {resultado.id}."
                ),
            )
            try:
                from apps.gamification.services import (
                    evaluar_logros_academicos,
                    recompensar_evento_academico,
                )

                recompensar_evento_academico(
                    usuario,
                    "modulo_completado",
                    modulo.id,
                    concepto=f"Módulo completado: {modulo.titulo}",
                    monto=15,
                )
                evaluar_logros_academicos(usuario)
            except Exception:
                pass

    if quiz.etapa_id is not None and quiz.tipo == Quiz.TIPO_EXAMEN:
        aprobar_etapa_por_evaluacion(usuario, quiz.etapa, quiz, resultado)

    return progreso_modulo


def _estado_criterios_etapa(usuario, etapa, *, evaluacion_aprobada: bool = False) -> dict:
    """Evalúa criterios de finalización de una etapa para un usuario.

    Reglas explícitas y auditables:
    - Un criterio se considera satisfecho si existe `CumplimientoCriterio`
      satisfecho para (usuario, criterio).
    - En contexto de evaluación aprobada, los criterios obligatorios/opcionales
      de tipo 'evaluacion' pueden considerarse satisfechos si aún no tienen
      registro explícito (y se registran por el flujo de evaluación).
    - Criterios obligatorios no satisfechos bloquean la aprobación automática.
    """
    criterios = list(etapa.criterios.all())
    cumplimientos = {
        c.criterio_id: c
        for c in CumplimientoCriterio.objects.filter(usuario=usuario, criterio__etapa=etapa)
    }

    satisfechos = []
    pendientes_obligatorios = []
    for criterio in criterios:
        cumplimiento = cumplimientos.get(criterio.id)
        esta_satisfecho = bool(cumplimiento and cumplimiento.satisfecho)
        if not esta_satisfecho and evaluacion_aprobada and criterio.tipo == "evaluacion":
            esta_satisfecho = True

        if esta_satisfecho:
            satisfechos.append(criterio)
        elif criterio.obligatorio:
            pendientes_obligatorios.append(criterio)

    return {
        "criterios_totales": len(criterios),
        "satisfechos": satisfechos,
        "pendientes_obligatorios": pendientes_obligatorios,
        "puede_aprobar_etapa": len(pendientes_obligatorios) == 0,
    }


def registrar_cumplimientos_evaluacion(usuario, etapa, quiz: Quiz, resultado: ResultadoEvaluacion) -> None:
    """Registra cumplimiento de criterios de tipo evaluación tras examen aprobado."""
    if not (resultado.aprobado and not resultado.requiere_revision):
        return
    for criterio in etapa.criterios.filter(tipo="evaluacion"):
        CumplimientoCriterio.objects.update_or_create(
            usuario=usuario,
            criterio=criterio,
            defaults={
                "satisfecho": True,
                "origen": "evaluacion",
                "evidencia": f"Examen/quiz aprobado: {quiz.nombre}",
                "referencia": f"quiz:{quiz.id}:resultado:{resultado.id}",
            },
        )


def _intentar_completar_etapa(usuario, etapa, *, evaluacion_aprobada: bool = False, origen_evento: str = "", contexto: str = "") -> Progreso | None:
    """Completa la etapa si prerequisitos y criterios obligatorios están satisfechos."""
    from django.utils import timezone

    from .models import Progreso
    from .services import etapas_completadas

    roadmap = etapa.roadmap
    completadas = etapas_completadas(usuario, roadmap)
    if etapa.esta_bloqueada_para(completadas):
        return None

    estado_criterios = _estado_criterios_etapa(usuario, etapa, evaluacion_aprobada=evaluacion_aprobada)
    progreso, _ = Progreso.objects.get_or_create(
        usuario=usuario,
        etapa=etapa,
        modulo=None,
        leccion=None,
        actividad=None,
        defaults={"estado": "no_iniciado", "porcentaje": 0},
    )

    if not estado_criterios["puede_aprobar_etapa"]:
        pendientes = [
            f"{c.get_tipo_display()}: {c.titulo}"
            for c in estado_criterios["pendientes_obligatorios"]
        ]
        if progreso.estado == "no_iniciado":
            progreso.estado = "en_progreso"
            progreso.porcentaje = max(progreso.porcentaje, 0)
            progreso.save(update_fields=["estado", "porcentaje", "fecha_actualizacion"])
        if origen_evento:
            registrar_evento(
                origen_evento,
                usuario=usuario,
                descripcion=(
                    f"Etapa {etapa.numero} ({etapa.titulo}) con evidencia parcial; "
                    f"pendiente de criterios obligatorios: {', '.join(pendientes) if pendientes else 'sin detalle'}. "
                    f"{contexto}".strip()
                ),
            )
        return progreso

    if progreso.estado != "completado":
        progreso.estado = "completado"
        progreso.porcentaje = 100
        progreso.fecha_completado = timezone.now()
        progreso.save(
            update_fields=["estado", "porcentaje", "fecha_completado", "fecha_actualizacion"]
        )
        registrar_evento(
            "etapa_completada_por_criterios",
            usuario=usuario,
            descripcion=(
                f"Etapa {etapa.numero} ({etapa.titulo}) completada: criterios obligatorios satisfechos "
                f"({len(estado_criterios['satisfechos'])}) y prerrequisitos cumplidos. {contexto}".strip()
            ),
        )
        try:
            from apps.gamification.services import (
                evaluar_logros_academicos,
                recompensar_evento_academico,
            )

            recompensar_evento_academico(
                usuario,
                "etapa_completada",
                etapa.id,
                concepto=f"Etapa completada: {etapa.numero} — {etapa.titulo}",
                monto=50,
            )
            evaluar_logros_academicos(usuario)
        except Exception:
            pass
    return progreso


def aprobar_etapa_por_evaluacion(usuario, etapa, quiz: Quiz, resultado: ResultadoEvaluacion) -> Progreso | None:
    """Aprueba u homologa una etapa cuando se cumple una evaluación verificable.

    Reglas explícitas y auditables:
    - Requiere resultado aprobado, sin revisión pendiente y umbral cumplido.
    - Requiere prerrequisitos completados.
    - Registra cumplimientos de criterios tipo 'evaluacion'.
    - Completa la etapa solo si no quedan criterios obligatorios pendientes.
    """
    if usuario is None or not getattr(usuario, "is_authenticated", False):
        return None
    if not resultado.aprobado or resultado.requiere_revision:
        return None
    if resultado.puntuacion is None or resultado.puntuacion < quiz.umbral_aprobacion:
        return None

    registrar_cumplimientos_evaluacion(usuario, etapa, quiz, resultado)
    contexto = (
        f"Evaluación aprobada: quiz/examen {quiz.id} (v{quiz.version}), "
        f"resultado {resultado.id}, {resultado.puntuacion}% >= {quiz.umbral_aprobacion}%."
    )
    return _intentar_completar_etapa(
        usuario,
        etapa,
        evaluacion_aprobada=True,
        origen_evento="etapa_homologacion_pendiente_criterios",
        contexto=contexto,
    )


@transaction.atomic
def registrar_cumplimiento_criterio(
    usuario,
    criterio: CriterioFinalizacion,
    *,
    evidencia: str = "",
    origen: str = "manual",
    referencia: str = "",
) -> CumplimientoCriterio:
    """Registra evidencia de cumplimiento de un criterio y reevalúa la etapa."""
    if usuario is None or not getattr(usuario, "is_authenticated", False):
        raise ValidationError("Se requiere un usuario autenticado.")

    cumplimiento, _ = CumplimientoCriterio.objects.update_or_create(
        usuario=usuario,
        criterio=criterio,
        defaults={
            "satisfecho": True,
            "origen": origen,
            "evidencia": evidencia or "",
            "referencia": referencia or "",
        },
    )
    registrar_evento(
        "criterio_finalizacion_cumplido",
        usuario=usuario,
        descripcion=(
            f"Criterio cumplido: etapa {criterio.etapa.numero}, "
            f"'{criterio.titulo}' ({criterio.get_tipo_display()}); origen={origen}."
        ),
    )
    _intentar_completar_etapa(
        usuario,
        criterio.etapa,
        origen_evento="etapa_homologacion_pendiente_criterios",
        contexto=f"Criterio registrado: {criterio.titulo}.",
    )
    return cumplimiento
