"""Servicios para versionar contenido académico y conservar su procedencia."""

from __future__ import annotations

import hashlib
import json
from typing import Iterable

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Max

from .models import (
    ContenidoLeccion,
    EjemploLeccion,
    EjercicioLeccion,
    FuenteConocimiento,
    Leccion,
    ReferenciaFuenteContenido,
    VersionContenidoLeccion,
)


def _serializar_snapshot(leccion: Leccion, contenido: ContenidoLeccion) -> dict:
    """Construye un snapshot determinista con solo recursos publicados."""
    ejemplos = EjemploLeccion.objects.filter(
        leccion=leccion, publicado=True
    ).order_by("orden", "id")
    ejercicios = EjercicioLeccion.objects.filter(
        leccion=leccion, publicado=True
    ).order_by("orden", "id")

    return {
        "esquema_version": 1,
        "leccion": {
            "clave": str(leccion.clave_contenido),
            "titulo": leccion.titulo,
            "descripcion": leccion.descripcion,
            "tipo": leccion.tipo,
        },
        "contenido": {
            "objetivos_aprendizaje": contenido.objetivos_aprendizaje,
            "teoria_tecnica": contenido.teoria_tecnica,
            "explicacion_sencilla": contenido.explicacion_sencilla,
            "notas": contenido.notas,
        },
        "ejemplos": [
            {
                "clave": str(ejemplo.clave_contenido),
                "titulo": ejemplo.titulo,
                "contexto": ejemplo.contexto,
                "lenguaje": ejemplo.lenguaje,
                "codigo": ejemplo.codigo,
                "salida_esperada": ejemplo.salida_esperada,
                "explicacion": ejemplo.explicacion,
                "orden": ejemplo.orden,
            }
            for ejemplo in ejemplos
        ],
        "ejercicios": [
            {
                "clave": str(ejercicio.clave_contenido),
                "titulo": ejercicio.titulo,
                "enunciado": ejercicio.enunciado,
                "instrucciones": ejercicio.instrucciones,
                "lenguaje": ejercicio.lenguaje,
                "nivel": ejercicio.nivel,
                "codigo_inicial": ejercicio.codigo_inicial,
                "obligatorio": ejercicio.obligatorio,
                "orden": ejercicio.orden,
            }
            for ejercicio in ejercicios
        ],
    }


def crear_version_contenido_leccion(
    leccion: Leccion,
    *,
    resumen_cambios: str = "",
    fuentes: Iterable[tuple[FuenteConocimiento, str, str, str]] = (),
) -> VersionContenidoLeccion:
    """Crea un snapshot borrador determinista; nunca publica ni altera el borrador."""
    with transaction.atomic():
        leccion = Leccion.objects.select_for_update().get(pk=leccion.pk)
        try:
            contenido = ContenidoLeccion.objects.get(leccion=leccion)
        except ContenidoLeccion.DoesNotExist as exc:
            raise ValidationError("La lección todavía no tiene contenido editorial.") from exc

        if not contenido.esta_completo:
            raise ValidationError(
                "No se puede versionar una lección sin teoría técnica y explicación sencilla."
            )

        snapshot = _serializar_snapshot(leccion, contenido)
        representacion = json.dumps(
            snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
        digest = hashlib.sha256(representacion.encode("utf-8")).hexdigest()
        ultima_version = (
            VersionContenidoLeccion.objects.filter(leccion=leccion).aggregate(
                numero=Max("numero_version")
            )["numero"]
            or 0
        )

        version = VersionContenidoLeccion.objects.create(
            leccion=leccion,
            numero_version=ultima_version + 1,
            esquema_version=1,
            estado="borrador",
            snapshot=snapshot,
            sha256=digest,
            resumen_cambios=resumen_cambios,
        )

        for fuente, rol, localizador, nota_atribucion in fuentes:
            if not fuente.activa:
                raise ValidationError(
                    f"La fuente '{fuente}' está inactiva y no puede asociarse a una versión nueva."
                )
            ReferenciaFuenteContenido.objects.create(
                version=version,
                fuente=fuente,
                rol=rol,
                localizador=localizador,
                nota_atribucion=nota_atribucion,
            )

        return version
