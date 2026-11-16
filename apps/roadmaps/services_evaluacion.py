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

from .models_evaluacion import Pregunta, Quiz, ResultadoEvaluacion, ResultadoPregunta


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

    return resultado
