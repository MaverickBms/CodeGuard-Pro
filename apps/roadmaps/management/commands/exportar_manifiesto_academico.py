"""Exporta un manifiesto curricular de solo lectura para preparar importaciones editoriales.

El comando no crea UUID, no modifica modelos y no exporta progreso ni datos de usuarios.
"""
from __future__ import annotations

import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from apps.roadmaps.models import (
    EjemploLeccion,
    EjercicioLeccion,
    ContenidoLeccion,
    ContenidoLeccionActivo,
    FuenteConocimiento,
    Roadmap,
    VersionContenidoLeccion,
)


class Command(BaseCommand):
    help = (
        "Exporta UUID y metadatos curriculares de ASCENSO en JSON. "
        "Solo lectura; no exporta contenido privado ni modifica la base de datos."
    )

    def add_arguments(self, parser):
        parser.add_argument("--nombre", required=True, help="Nombre exacto del roadmap.")
        parser.add_argument("--edicion", required=True, help="Edición exacta del roadmap.")
        parser.add_argument(
            "--salida",
            help="Ruta de salida. Si se omite, escribe el JSON por stdout.",
        )
        parser.add_argument(
            "--incluir-fuentes",
            action="store_true",
            help="Incluye el catálogo de fuentes registradas, sin credenciales ni datos de usuario.",
        )

    def handle(self, *args, **options):
        try:
            roadmap = Roadmap.objects.get(
                nombre=options["nombre"],
                edicion=options["edicion"],
            )
        except Roadmap.DoesNotExist as exc:
            raise CommandError("No existe un roadmap con ese nombre y edición.") from exc
        except Roadmap.MultipleObjectsReturned as exc:
            raise CommandError("La selección del roadmap no es única.") from exc

        stages = []
        lesson_count = 0
        module_count = 0
        example_count = 0
        exercise_count = 0
        legacy_body_count = 0
        active_content_count = 0
        version_state_counts = {
            state: 0 for state, _label in VersionContenidoLeccion.ESTADOS
        }

        queryset = roadmap.etapas.prefetch_related(
            "modulos__lecciones__ejemplos",
            "modulos__lecciones__ejercicios",
            "modulos__lecciones__contenido",
            "modulos__lecciones__contenido_activo__version",
            "modulos__lecciones__versiones_contenido",
        ).order_by("orden", "numero")

        for stage in queryset:
            modules = []
            for module in stage.modulos.all().order_by("orden", "numero"):
                module_count += 1
                lessons = []
                for lesson in module.lecciones.all().order_by("orden", "id"):
                    lesson_count += 1
                    examples = [
                        {
                            "uuid": str(item.clave_contenido),
                            "titulo": item.titulo,
                            "orden": item.orden,
                        }
                        for item in lesson.ejemplos.all()
                    ]
                    exercises = [
                        {
                            "uuid": str(item.clave_contenido),
                            "titulo": item.titulo,
                            "nivel": item.nivel,
                            "orden": item.orden,
                        }
                        for item in lesson.ejercicios.all()
                    ]
                    example_count += len(examples)
                    exercise_count += len(exercises)
                    try:
                        legacy = lesson.contenido
                    except ContenidoLeccion.DoesNotExist:
                        legacy = None
                    try:
                        active = lesson.contenido_activo
                    except ContenidoLeccionActivo.DoesNotExist:
                        active = None
                    versions = [
                        {
                            "clave": str(version.clave),
                            "numero_version": version.numero_version,
                            "estado": version.estado,
                            "sha256": version.sha256,
                        }
                        for version in sorted(
                            lesson.versiones_contenido.all(),
                            key=lambda item: item.numero_version,
                        )
                    ]
                    for version in versions:
                        version_state_counts[version["estado"]] += 1
                    if legacy and (legacy.objetivos_aprendizaje.strip()
                                   or legacy.teoria_tecnica.strip()
                                   or legacy.explicacion_sencilla.strip()):
                        legacy_body_count += 1
                    if active:
                        active_content_count += 1
                    lessons.append(
                        {
                            "id_local": lesson.pk,
                            "uuid": str(lesson.clave_contenido),
                            "titulo": lesson.titulo,
                            "descripcion": lesson.descripcion,
                            "tipo": lesson.tipo,
                            "orden": lesson.orden,
                            "contenido_legacy": {
                                "existe": legacy is not None,
                                "tiene_cuerpo": bool(
                                    legacy and (
                                        legacy.objetivos_aprendizaje.strip()
                                        or legacy.teoria_tecnica.strip()
                                        or legacy.explicacion_sencilla.strip()
                                    )
                                ),
                                "publicado": legacy.publicado if legacy else False,
                            },
                            "contenido_activo": ({
                                "uuid_version": str(active.version.clave),
                                "numero_version": active.version.numero_version,
                                "estado": active.version.estado,
                            } if active else None),
                            "versiones": versions,
                            "ejemplos": examples,
                            "ejercicios": exercises,
                        }
                    )
                modules.append(
                    {
                        "numero": module.numero,
                        "titulo": module.titulo,
                        "objetivo": module.objetivo,
                        "orden": module.orden,
                        "lecciones": lessons,
                    }
                )
            stages.append(
                {
                    "numero": stage.numero,
                    "titulo": stage.titulo,
                    "objetivo": stage.objetivo,
                    "prioridad": stage.prioridad,
                    "proyecto": stage.proyecto,
                    "modulos": modules,
                }
            )

        payload = {
            "schema": "codeguard-academic-manifest-v1",
            "solo_lectura": True,
            "roadmap": {
                "nombre": roadmap.nombre,
                "edicion": roadmap.edicion,
                "fuente": roadmap.fuente,
                "sha256_fuente": roadmap.sha256_fuente,
            },
            "resumen": {
                "etapas": len(stages),
                "modulos": module_count,
                "lecciones": lesson_count,
                "ejemplos": example_count,
                "ejercicios": exercise_count,
                "lecciones_con_cuerpo_legacy": legacy_body_count,
                "lecciones_con_contenido_activo": active_content_count,
                "versiones_por_estado": version_state_counts,
            },
            "etapas": stages,
        }

        if options["incluir_fuentes"]:
            payload["fuentes"] = [
                {
                    "uuid": str(source.clave),
                    "publicador": source.publicador,
                    "titulo": source.titulo,
                    "url_canonica": source.url_canonica,
                    "edicion": source.edicion,
                    "identificador_licencia": source.identificador_licencia,
                    "url_licencia": source.url_licencia,
                    "estado_revision_licencia": source.estado_revision_licencia,
                    "evidencia_licencia": source.evidencia_licencia,
                    "alcance_licencia": source.alcance_licencia,
                    "nota_revision_licencia": source.nota_revision_licencia,
                    "activa": source.activa,
                }
                for source in FuenteConocimiento.objects.all().order_by(
                    "publicador", "titulo"
                )
            ]

        rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        destination = options.get("salida")
        if not destination:
            self.stdout.write(rendered, ending="")
            return

        path = Path(destination).expanduser()
        if path.is_symlink():
            raise CommandError("La ruta de salida no puede ser un enlace simbólico.")
        if path.exists():
            raise CommandError("El archivo de salida ya existe; elija otra ruta.")
        if not path.parent.exists() or not path.parent.is_dir():
            raise CommandError("El directorio de salida debe existir.")
        try:
            with path.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(rendered)
        except OSError as exc:
            raise CommandError("No se pudo escribir el manifiesto.") from exc
        self.stdout.write(self.style.SUCCESS(
            f"Manifiesto exportado: {path} "
            f"({lesson_count} lecciones; base de datos sin modificaciones)."
        ))
