"""Carga trazable de quizzes/exámenes desde archivos JSON (Fase 4).

Formato orientado a authoring: cada quiz referencia etapa/módulo del roadmap
y cada pregunta incluye objetivo y contenido/fuente para trazabilidad.
"""

from __future__ import annotations

import json
from pathlib import Path

from django.db import transaction

from .models import Etapa, Modulo, Roadmap
from .models_evaluacion import Pregunta, Quiz

RUTA_DATOS_QUIZZES = Path(__file__).resolve().parent / "data" / "quizzes.json"


def _resolver_quiz_contexto(roadmap: Roadmap, datos: dict) -> tuple[Etapa | None, Modulo | None]:
    etapa = None
    modulo = None
    etapa_numero = datos.get("etapa_numero")
    modulo_numero = datos.get("modulo_numero")
    if etapa_numero is not None:
        etapa = Etapa.objects.filter(roadmap=roadmap, numero=int(etapa_numero)).first()
    if modulo_numero and etapa_numero is not None:
        modulo = Modulo.objects.filter(etapa__roadmap=roadmap, etapa__numero=int(etapa_numero), numero=str(modulo_numero)).first()
        if modulo and etapa is None:
            etapa = modulo.etapa
    elif modulo_numero and etapa is None:
        modulo = Modulo.objects.filter(etapa__roadmap=roadmap, numero=str(modulo_numero)).first()
        if modulo:
            etapa = modulo.etapa
    return etapa, modulo


@transaction.atomic
def cargar_quizzes(ruta: str | Path | None = None, *, roadmap: Roadmap | None = None, reemplazar: bool = False) -> dict:
    """Carga o actualiza quizzes desde un JSON trazable.

    - ``reemplazar=True`` elimina preguntas existentes del quiz versionado antes
      de recargar (no elimina resultados históricos).
    - No fuerza publicación: respeta ``estado`` del archivo.
    - Requisito académico (≥15 preguntas en quiz de módulo) se valida como
      advertencia cuando el estado es publicado; se permite borrador/piloto.
    """
    ruta_datos = Path(ruta) if ruta else RUTA_DATOS_QUIZZES
    with open(ruta_datos, encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if roadmap is None:
        roadmap = Roadmap.objects.filter(activo=True).order_by("-actualizado_en").first()
    if roadmap is None:
        raise ValueError("No hay un roadmap activo para asociar los quizzes.")

    items = datos.get("quizzes", datos if isinstance(datos, list) else [])
    resumen = {"quizzes": 0, "preguntas": 0, "advertencias": []}

    for item in items:
        etapa, modulo = _resolver_quiz_contexto(roadmap, item)
        tipo = item.get("tipo", Quiz.TIPO_QUIZ)
        version = int(item.get("version", 1))

        lookup = {"version": version}
        if modulo is not None:
            lookup["modulo"] = modulo
            lookup["etapa"] = None
        elif etapa is not None and tipo == Quiz.TIPO_EXAMEN:
            lookup["etapa"] = etapa
            lookup["modulo"] = modulo  # puede ser None
        elif etapa is not None:
            lookup["etapa"] = etapa
            lookup["modulo"] = None
        else:
            resumen["advertencias"].append(
                f"Quiz '{item.get('nombre','?')}': sin etapa/módulo resoluble, omitido."
            )
            continue

        defaults = {
            "nombre": item.get("nombre", "Quiz"),
            "tipo": tipo,
            "umbral_aprobacion": int(item.get("umbral_aprobacion", 70)),
            "estado": item.get("estado", Quiz.ESTADO_BORRADOR),
        }
        # asegurar etapa coherente
        if modulo is not None and etapa is None:
            etapa = modulo.etapa
        if etapa is not None and "etapa" in lookup and lookup.get("etapa") is None and tipo != Quiz.TIPO_EXAMEN:
            lookup["etapa"] = etapa

        quiz, _ = Quiz.objects.update_or_create(defaults={**defaults, "etapa": etapa if (tipo == Quiz.TIPO_EXAMEN or etapa) else None, "modulo": modulo}, **lookup)

        preguntas = item.get("preguntas", [])
        if reemplazar:
            quiz.preguntas.all().delete()

        for idx, p in enumerate(preguntas, start=1):
            datos_respuesta = dict(p.get("datos_respuesta", {}) or {})
            # Metadatos trazables (authoring): no afectan la corrección automática.
            meta = {}
            if p.get("objetivo"):
                meta["objetivo"] = p.get("objetivo")
            if p.get("contenido") or p.get("fuente"):
                meta["contenido_fuente"] = p.get("contenido") or p.get("fuente")
            if p.get("retroalimentacion_base"):
                meta["retroalimentacion_base"] = p.get("retroalimentacion_base")
            if meta:
                datos_respuesta["_meta_trazabilidad"] = meta

            Pregunta.objects.update_or_create(
                quiz=quiz,
                orden=int(p.get("orden", idx)),
                defaults={
                    "formato": p.get("formato", Pregunta.FORMATO_RESPUESTA),
                    "enunciado": p.get("enunciado", ""),
                    "datos_respuesta": datos_respuesta,
                },
            )
        resumen["quizzes"] += 1
        resumen["preguntas"] += len(preguntas)

        if quiz.estado == Quiz.ESTADO_PUBLICADO and quiz.tipo == Quiz.TIPO_QUIZ and len(preguntas) < 15:
            resumen["advertencias"].append(
                f"Quiz publicado '{quiz.nombre}' (módulo) tiene {len(preguntas)} preguntas (<15)."
            )

    return resumen
