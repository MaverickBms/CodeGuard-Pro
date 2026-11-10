"""Servicios del módulo académico.

Centralizan la carga idempotente del roadmap oficial, el cálculo de
prerrequisitos y el registro de progreso. Las vistas y los comandos de gestión
no deben duplicar esta lógica.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from django.db import transaction
from django.db.models import Count, Q

from apps.audit.services import registrar_evento

from .models import (
    CriterioFinalizacion,
    Etapa,
    Leccion,
    Modulo,
    Prerrequisito,
    Progreso,
    Roadmap,
)

RUTA_DATOS_ASCENSO = Path(__file__).resolve().parent / "data" / "ascenso_3_1.json"

NOTA_MVP = (
    "Estado pendiente de la decisión P-002 (selección de etapas para el MVP). "
    "El documento maestro define las 33 etapas; la propuesta registrada en la "
    "documentación del proyecto es desarrollar en el MVP las etapas 0, 1, 2, 3, "
    "8, 17 y 21, sin eliminar las restantes del roadmap."
)

# Dependencias explícitas documentadas en ASCENSO 3.1.
# No se agregan dependencias inferidas para no inventar contenido.
DEPENDENCIAS_EXPLICITAS: dict[int, list[tuple[int, str]]] = {
    10: [
        (
            9,
            "El documento indica que la ampliación de bases de datos desarrolla "
            "las etapas 9 y 10 y que se debe dominar SQL antes de pasar a los "
            "modelos documentales y a la caché.",
        )
    ],
    15: [
        (
            13,
            "La secuencia oficial sitúa Internet, HTTP y APIs (etapa 13) antes de "
            "Backend II: Node.js y NestJS (etapa 15).",
        )
    ],
    31: [
        (
            3,
            "La etapa 31 requiere conocimientos anteriores de programación y Java.",
        ),
        (
            4,
            "La etapa 31 requiere conocimientos anteriores de programación orientada "
            "a objetos.",
        ),
        (
            7,
            "La etapa 31 requiere conocimientos anteriores de sistemas operativos.",
        ),
        (
            8,
            "La etapa 31 requiere conocimientos anteriores de redes.",
        ),
        (
            21,
            "La etapa 31 requiere conocimientos anteriores de seguridad.",
        ),
    ],
}


def _fecha(valor: str | None) -> date | None:
    if not valor:
        return None
    try:
        return date.fromisoformat(valor)
    except ValueError:
        return None


@transaction.atomic
def cargar_ascenso(ruta: str | Path | None = None, *, recrear: bool = False) -> Roadmap:
    """Carga el JSON oficial de ASCENSO 3.1 de forma idempotente.

    ``recrear=True`` elimina el roadmap existente y su contenido (incluido el
    progreso asociado) antes de volver a sembrarlo. Por defecto se actualiza
    sin borrar el avance del usuario.
    """
    ruta = Path(ruta) if ruta else RUTA_DATOS_ASCENSO
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    meta = datos.get("metadata", {})

    nombre = meta.get("nombre", "PROYECTO ASCENSO — Roadmap Maestro Consolidado")
    edicion = meta.get("edicion", "3.1")

    if recrear:
        Roadmap.objects.filter(nombre=nombre, edicion=edicion).delete()

    roadmap, _ = Roadmap.objects.update_or_create(
        nombre=nombre,
        edicion=edicion,
        defaults={
            "fecha_consolidacion": _fecha(meta.get("fecha_consolidacion")),
            "fuente": meta.get("fuente", ""),
            "sha256_fuente": meta.get("sha256_fuente", ""),
            "activo": True,
        },
    )

    etapas_por_numero: dict[int, Etapa] = {}

    for datos_etapa in datos.get("etapas", []):
        numero = int(datos_etapa["numero"])
        etapa, _ = Etapa.objects.update_or_create(
            roadmap=roadmap,
            numero=numero,
            defaults={
                "titulo": datos_etapa.get("titulo", ""),
                "bloque": datos_etapa.get("bloque", ""),
                "seccion": datos_etapa.get("seccion", ""),
                "prioridad": datos_etapa.get("prioridad", "P1"),
                "prioridad_detalle": datos_etapa.get("prioridad_detalle", ""),
                "objetivo": datos_etapa.get("objetivo", ""),
                "proyecto": datos_etapa.get("proyecto", ""),
                "proyecto_titulo": datos_etapa.get("proyecto_titulo", ""),
                "notas": "\n".join(datos_etapa.get("notas", [])),
                "nota_mvp": NOTA_MVP,
                "desarrollada_en_mvp": False,
                "orden": numero,
            },
        )
        etapas_por_numero[numero] = etapa

        for orden_modulo, datos_modulo in enumerate(
            datos_etapa.get("modulos", []), start=1
        ):
            modulo, _ = Modulo.objects.update_or_create(
                etapa=etapa,
                numero=datos_modulo.get("numero", ""),
                defaults={
                    "titulo": datos_modulo.get("titulo", ""),
                    "orden": orden_modulo,
                },
            )
            for orden_leccion, titulo in enumerate(
                datos_modulo.get("lecciones", []), start=1
            ):
                Leccion.objects.update_or_create(
                    modulo=modulo,
                    titulo=titulo,
                    defaults={"orden": orden_leccion, "tipo": "concepto"},
                )

        if datos_etapa.get("proyecto"):
            CriterioFinalizacion.objects.update_or_create(
                etapa=etapa,
                titulo="Proyecto de la etapa",
                defaults={
                    "descripcion": datos_etapa["proyecto"],
                    "tipo": "proyecto",
                    "obligatorio": True,
                    "orden": 1,
                },
            )

    # Las dependencias se reconstruyen para mantener exactitud con la fuente.
    Prerrequisito.objects.filter(etapa__roadmap=roadmap).delete()
    for numero, dependencias in DEPENDENCIAS_EXPLICITAS.items():
        etapa = etapas_por_numero.get(numero)
        if not etapa:
            continue
        for numero_requerido, justificacion in dependencias:
            requerida = etapas_por_numero.get(numero_requerido)
            if not requerida:
                continue
            Prerrequisito.objects.create(
                etapa=etapa,
                etapa_requerida=requerida,
                justificacion=justificacion,
                documentado=True,
            )

    return roadmap


def roadmap_activo() -> Roadmap | None:
    """Devuelve el roadmap activo más reciente, si existe."""
    return Roadmap.objects.filter(activo=True).order_by("-actualizado_en").first()


def resumen_roadmap(roadmap: Roadmap) -> dict:
    """Estadísticas descriptivas del roadmap para el panel de listado."""
    etapas = roadmap.etapas.all()
    return {
        "total_etapas": etapas.count(),
        "total_modulos": Modulo.objects.filter(etapa__roadmap=roadmap).count(),
        "total_lecciones": Leccion.objects.filter(modulo__etapa__roadmap=roadmap).count(),
        "total_proyectos": etapas.exclude(proyecto="").count(),
        "por_prioridad": {
            fila["prioridad"]: fila["total"]
            for fila in etapas.values("prioridad").annotate(total=Count("id"))
        },
    }


def etapas_completadas(usuario, roadmap: Roadmap) -> set[int]:
    """Números de etapa con progreso de etapa marcado como completado."""
    if not usuario or not usuario.is_authenticated:
        return set()
    return set(
        Progreso.objects.filter(
            usuario=usuario,
            etapa__roadmap=roadmap,
            modulo__isnull=True,
            leccion__isnull=True,
            actividad__isnull=True,
            estado="completado",
        ).values_list("etapa__numero", flat=True)
    )


def mapa_progreso_etapas(usuario, roadmap: Roadmap) -> dict[int, Progreso]:
    """Progreso a nivel de etapa indexado por ``etapa_id``."""
    if not usuario or not usuario.is_authenticated:
        return {}
    filas = Progreso.objects.filter(
        usuario=usuario,
        etapa__roadmap=roadmap,
        modulo__isnull=True,
        leccion__isnull=True,
        actividad__isnull=True,
    )
    return {fila.etapa_id: fila for fila in filas}


def mapa_progreso_lecciones(usuario, etapa: Etapa) -> dict[int, Progreso]:
    """Progreso de lecciones indexado por ``leccion_id``."""
    if not usuario or not usuario.is_authenticated:
        return {}
    filas = Progreso.objects.filter(
        usuario=usuario,
        etapa=etapa,
        leccion__isnull=False,
    )
    return {fila.leccion_id: fila for fila in filas if fila.leccion_id}


def progreso_general(usuario, roadmap: Roadmap) -> dict:
    """Porcentaje y conteos de avance del usuario en el roadmap."""
    total = roadmap.etapas.count()
    completadas = len(etapas_completadas(usuario, roadmap))
    return {
        "total": total,
        "completadas": completadas,
        "porcentaje": round(100 * completadas / total) if total else 0,
    }


def _progreso_etapa(usuario, etapa: Etapa) -> Progreso:
    progreso, _ = Progreso.objects.get_or_create(
        usuario=usuario,
        etapa=etapa,
        modulo=None,
        leccion=None,
        actividad=None,
        defaults={"estado": "no_iniciado", "porcentaje": 0},
    )
    return progreso


def recalcular_progreso_etapa(usuario, etapa: Etapa) -> Progreso:
    """Recalcula el porcentaje de etapa a partir de las lecciones completadas.

    Si la etapa fue marcada manualmente como completada, se respeta ese estado
    y no se degrada por alternar lecciones.
    """
    progreso = _progreso_etapa(usuario, etapa)
    if progreso.estado == "completado":
        return progreso

    total = Leccion.objects.filter(modulo__etapa=etapa).count()
    completadas = Progreso.objects.filter(
        usuario=usuario,
        etapa=etapa,
        leccion__isnull=False,
        estado="completado",
    ).count()
    porcentaje = round(100 * completadas / total) if total else 0

    progreso.porcentaje = porcentaje
    if porcentaje == 0:
        progreso.estado = "no_iniciado"
    elif porcentaje >= 100:
        progreso.estado = "completado"
    else:
        progreso.estado = "en_progreso"
    progreso.save()
    return progreso


def marcar_etapa(
    usuario, etapa: Etapa, *, completada: bool = True, actor_auditoria=None
) -> Progreso:
    """Marca o reabre una etapa completa, respetando los prerrequisitos."""
    completadas = etapas_completadas(usuario, etapa.roadmap)
    if completada and etapa.esta_bloqueada_para(completadas):
        raise ValueError("La etapa tiene prerrequisitos sin completar.")

    progreso = _progreso_etapa(usuario, etapa)
    progreso.estado = "completado" if completada else "no_iniciado"
    progreso.save()

    registrar_evento(
        "roadmap_etapa_completada" if completada else "roadmap_etapa_reabierta",
        usuario=actor_auditoria,
        descripcion=f"Etapa {etapa.numero} — {etapa.titulo}",
    )
    return progreso


def marcar_leccion(
    usuario,
    leccion: Leccion,
    *,
    completada: bool = True,
    actor_auditoria=None,
) -> Progreso:
    """Marca o desmarca una lección y recalcula el avance de su etapa."""
    etapa = leccion.modulo.etapa
    progreso, _ = Progreso.objects.get_or_create(
        usuario=usuario,
        etapa=etapa,
        modulo=leccion.modulo,
        leccion=leccion,
        actividad=None,
        defaults={"estado": "no_iniciado", "porcentaje": 0},
    )
    progreso.estado = "completado" if completada else "no_iniciado"
    progreso.save()

    recalcular_progreso_etapa(usuario, etapa)

    registrar_evento(
        "roadmap_leccion_completada" if completada else "roadmap_leccion_reabierta",
        usuario=actor_auditoria,
        descripcion=f"Etapa {etapa.numero} · {leccion.titulo}",
    )
    return progreso


def etapas_por_bloque(roadmap: Roadmap):
    """Etapas agrupadas por bloque/sección para plantillas."""
    return (
        roadmap.etapas.all()
        .values("bloque", "seccion")
        .annotate(total=Count("id"))
        .order_by("bloque")
    )
