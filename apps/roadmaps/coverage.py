"""Cobertura académica y estado editorial por lección.

El progreso del estudiante (Progreso) y el progreso editorial del contenido son
dimensiones distintas. Este módulo calcula la segunda sin modificar datos.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field

from .models import (
    ContenidoLeccion,
    ContenidoLeccionActivo,
    Leccion,
    RecursoAudiovisual,
    VersionContenidoLeccion,
)

_COBERTURA_CACHE: dict[int, tuple[float, "Cobertura"]] = {}
_COBERTURA_TTL_S = 60.0

ESTADOS = (
    "pendiente",
    "en_desarrollo",
    "borrador",
    "revision",
    "aprobada",
    "publicada",
)

ETIQUETAS = {
    "pendiente": "Pendiente",
    "en_desarrollo": "En desarrollo",
    "borrador": "Borrador",
    "revision": "En revisión",
    "aprobada": "Aprobada",
    "publicada": "Publicada",
}

_ESTADO_VERSION = {
    "borrador": "borrador",
    "revision": "revision",
    "aprobada": "aprobada",
    "publicada": "publicada",
    "sustituida": "borrador",
    "retirada": "pendiente",
}

_ETIQUETA_VERSION = {
    "borrador": "Borrador",
    "revision": "En revisión",
    "aprobada": "Aprobada",
    "publicada": "Publicada",
    "sustituida": "Sustituida",
    "retirada": "Retirada",
}


@dataclass
class Cobertura:
    total: int = 0
    pendiente: int = 0
    en_desarrollo: int = 0
    borrador: int = 0
    revision: int = 0
    aprobada: int = 0
    publicada: int = 0
    con_video: int = 0
    con_fuentes: int = 0
    por_etapa: list[dict] = field(default_factory=list)
    por_estado: dict = field(default_factory=dict)

    @property
    def desarrolladas(self) -> int:
        return self.total - self.pendiente

    @property
    def revisadas(self) -> int:
        return self.aprobada + self.publicada

    @property
    def publicadas(self) -> int:
        return self.publicada

    def as_dict(self) -> dict:
        return {
            "total": self.total,
            "pendiente": self.pendiente,
            "en_desarrollo": self.en_desarrollo,
            "borrador": self.borrador,
            "revision": self.revision,
            "aprobada": self.aprobada,
            "publicada": self.publicada,
            "desarrolladas": self.desarrolladas,
            "revisadas": self.revisadas,
            "con_video": self.con_video,
            "con_fuentes": self.con_fuentes,
            "por_estado": dict(self.por_estado),
            "por_etapa": self.por_etapa,
        }


def _mapas_editoriales(roadmap):
    lecciones = list(
        Leccion.objects.filter(modulo__etapa__roadmap=roadmap)
        .select_related("modulo__etapa")
        .order_by("modulo__etapa__numero", "modulo__orden", "orden", "id")
    )
    contenidos_ids = set(
        ContenidoLeccion.objects.filter(
            leccion__modulo__etapa__roadmap=roadmap
        ).values_list("leccion_id", flat=True)
    )
    versiones = {}
    for fila in (
        VersionContenidoLeccion.objects.filter(
            leccion__modulo__etapa__roadmap=roadmap
        )
        .order_by("leccion_id", "-numero_version")
        .values("leccion_id", "estado", "numero_version")
    ):
        versiones.setdefault(
            fila["leccion_id"],
            {
                "estado": fila["estado"],
                "numero_version": fila["numero_version"],
                "estado_display": _ETIQUETA_VERSION.get(fila["estado"], fila["estado"]),
            },
        )
    activos = set(
        ContenidoLeccionActivo.objects.filter(
            leccion__modulo__etapa__roadmap=roadmap
        ).values_list("leccion_id", flat=True)
    )
    fuentes_por_leccion = set(
        VersionContenidoLeccion.objects.filter(
            leccion__modulo__etapa__roadmap=roadmap,
            referencias__isnull=False,
        ).values_list("leccion_id", flat=True)
    )
    videos_por_leccion = set(
        RecursoAudiovisual.objects.filter(
            leccion__modulo__etapa__roadmap=roadmap,
            estado_revision="aprobado",
            disponible=True,
        ).values_list("leccion_id", flat=True)
    )
    return lecciones, contenidos_ids, versiones, activos, fuentes_por_leccion, videos_por_leccion


def _estado(leccion_id, contenidos_ids, versiones, activos):
    if leccion_id in activos:
        return "publicada", versiones.get(leccion_id)
    version = versiones.get(leccion_id)
    if version is not None:
        return _ESTADO_VERSION.get(version.get("estado"), "borrador"), version
    if leccion_id in contenidos_ids:
        return "en_desarrollo", None
    return "pendiente", None


def invalidar_cache_cobertura(roadmap_id: int | None = None) -> None:
    if roadmap_id is None:
        _COBERTURA_CACHE.clear()
    else:
        _COBERTURA_CACHE.pop(roadmap_id, None)


def calcular_cobertura(roadmap) -> Cobertura:
    if roadmap is None:
        return Cobertura(por_estado={estado: 0 for estado in ESTADOS})

    ahora = time.monotonic()
    cacheada = _COBERTURA_CACHE.get(roadmap.id)
    if cacheada and ahora - cacheada[0] < _COBERTURA_TTL_S:
        return cacheada[1]

    (
        lecciones,
        contenidos,
        versiones,
        activos,
        fuentes_por_leccion,
        videos_por_leccion,
    ) = _mapas_editoriales(roadmap)

    cobertura = Cobertura(total=len(lecciones))
    por_etapa: dict[int, dict] = {}
    for leccion in lecciones:
        estado, version = _estado(leccion.id, contenidos, versiones, activos)
        setattr(cobertura, estado, getattr(cobertura, estado) + 1)
        if leccion.id in videos_por_leccion:
            cobertura.con_video += 1
        if leccion.id in fuentes_por_leccion:
            cobertura.con_fuentes += 1

        etapa = leccion.modulo.etapa
        fila = por_etapa.setdefault(
            etapa.numero,
            {
                "numero": etapa.numero,
                "titulo": etapa.titulo,
                "total": 0,
                **{clave: 0 for clave in ESTADOS},
            },
        )
        fila["total"] += 1
        fila[estado] += 1
        fila["desarrolladas"] = fila["total"] - fila["pendiente"]

    cobertura.por_etapa = [por_etapa[numero] for numero in sorted(por_etapa)]
    cobertura.por_estado = {estado: getattr(cobertura, estado) for estado in ESTADOS}
    _COBERTURA_CACHE[roadmap.id] = (ahora, cobertura)
    return cobertura


def detalle_editorial(leccion: Leccion) -> dict:
    """Estado editorial de una lección concreta para el editor local."""
    contenido = getattr(leccion, "contenido", None)
    version = (
        VersionContenidoLeccion.objects.filter(leccion=leccion)
        .order_by("-numero_version")
        .first()
    )
    activo = ContenidoLeccionActivo.objects.filter(leccion=leccion).first()
    estado = (
        "publicada"
        if activo
        else _ESTADO_VERSION.get(version.estado, "borrador")
        if version
        else "en_desarrollo"
        if contenido
        else "pendiente"
    )
    return {
        "estado": estado,
        "etiqueta": ETIQUETAS.get(estado, estado),
        "contenido": contenido,
        "version": version,
        "publicada": bool(activo),
        "videos": list(leccion.recursos_audiovisuales.all()),
        "fuentes": (
            list(version.referencias.select_related("fuente"))
            if version
            else []
        ),
    }


class _VersionInfo:
    __slots__ = ("numero_version", "estado")

    def __init__(self, numero_version, estado):
        self.numero_version = numero_version
        self.estado = estado

    def get_estado_display(self):
        return _ETIQUETA_VERSION.get(self.estado, self.estado)


def _version_info(version):
    if version is None:
        return None
    if isinstance(version, dict):
        return _VersionInfo(version.get("numero_version"), version.get("estado"))
    return version


def mapa_estados(roadmap) -> dict:
    """Mapa por lección para listados editoriales sin consultas N+1."""
    if roadmap is None:
        return {}
    (
        lecciones,
        contenidos_ids,
        versiones,
        activos,
        fuentes_por_leccion,
        videos_por_leccion,
    ) = _mapas_editoriales(roadmap)
    resultado = {}
    for leccion in lecciones:
        estado, version = _estado(leccion.id, contenidos_ids, versiones, activos)
        resultado[leccion.id] = {
            "estado": estado,
            "etiqueta": ETIQUETAS.get(estado, estado),
            "version": _version_info(version),
            "contenido": None,
            "tiene_fuentes": leccion.id in fuentes_por_leccion,
            "tiene_video": leccion.id in videos_por_leccion,
        }
    return resultado
