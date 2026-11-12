"""Validación e importación transaccional de documentos académicos JSON v1."""

from __future__ import annotations

import hashlib
import json
import uuid
from pathlib import Path

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Max

from .models import (
    EjemploLeccion,
    EjercicioLeccion,
    FuenteConocimiento,
    Leccion,
    ReferenciaFuenteContenido,
    VersionContenidoLeccion,
)

MAX_DOCUMENT_BYTES = 2 * 1024 * 1024
MAX_DOCUMENTS = 500
MAX_EXAMPLES = 50
MAX_EXERCISES = 50
MAX_SOURCES = 20
SCHEMA_VERSION = 1

TOP_KEYS = {"schema_version", "resumen_cambios", "snapshot", "fuentes"}
SNAPSHOT_KEYS = {"esquema_version", "leccion", "contenido", "ejemplos", "ejercicios"}
LESSON_KEYS = {"clave", "titulo", "descripcion", "tipo"}
CONTENT_KEYS = {"objetivos_aprendizaje", "teoria_tecnica", "explicacion_sencilla", "notas"}
EXAMPLE_KEYS = {"clave", "titulo", "contexto", "lenguaje", "codigo", "salida_esperada", "explicacion", "orden"}
EXERCISE_KEYS = {"clave", "titulo", "enunciado", "instrucciones", "lenguaje", "nivel", "codigo_inicial", "obligatorio", "orden"}
SOURCE_KEYS = {"clave", "rol", "localizador", "nota_atribucion", "uso_declarado"}
SOURCE_ROLES = {choice[0] for choice in ReferenciaFuenteContenido.ROLES}
SOURCE_USES = {choice[0] for choice in ReferenciaFuenteContenido.USOS_DECLARADOS}


class ImportContentError(Exception):
    """Error de contrato o integridad del paquete de contenido."""


def _pairs_without_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ImportContentError(f"Clave JSON duplicada: {key}")
        result[key] = value
    return result


def _expect_keys(value, expected, path):
    if not isinstance(value, dict):
        raise ImportContentError(f"{path}: se esperaba un objeto JSON.")
    missing = expected - set(value)
    unknown = set(value) - expected
    if missing:
        raise ImportContentError(f"{path}: faltan propiedades: {', '.join(sorted(missing))}.")
    if unknown:
        raise ImportContentError(f"{path}: propiedades no admitidas: {', '.join(sorted(unknown))}.")


def _string(value, path, *, required=False, max_length=None):
    if not isinstance(value, str):
        raise ImportContentError(f"{path}: debe ser texto.")
    if required and not value.strip():
        raise ImportContentError(f"{path}: no puede estar vacío.")
    if max_length is not None and len(value) > max_length:
        raise ImportContentError(f"{path}: supera {max_length} caracteres.")
    return value


def _uuid(value, path):
    if not isinstance(value, str):
        raise ImportContentError(f"{path}: UUID debe ser texto canónico.")
    try:
        parsed = uuid.UUID(value)
    except (ValueError, TypeError, AttributeError) as exc:
        raise ImportContentError(f"{path}: UUID inválido.") from exc
    if str(parsed) != value:
        raise ImportContentError(f"{path}: use el UUID canónico en minúsculas.")
    return parsed


def _integer(value, path):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ImportContentError(f"{path}: debe ser un entero no negativo.")
    return value


def _load_json(path):
    if path.is_symlink() or not path.is_file() or path.suffix.lower() != ".json":
        raise ImportContentError(f"{path.name}: solo se admiten archivos JSON regulares, sin symlinks.")
    size = path.stat().st_size
    if size > MAX_DOCUMENT_BYTES:
        raise ImportContentError(f"{path.name}: supera el límite de 2 MiB.")
    try:
        raw = path.read_text(encoding="utf-8")
        parsed = json.loads(raw, object_pairs_hook=_pairs_without_duplicates)
        def depth(value):
            if isinstance(value, dict):
                return 1 + max((depth(item) for item in value.values()), default=0)
            if isinstance(value, list):
                return 1 + max((depth(item) for item in value), default=0)
            return 0
        if depth(parsed) > 8:
            raise ImportContentError(f"{path.name}: profundidad JSON superior a 8.")
        return parsed
    except UnicodeDecodeError as exc:
        raise ImportContentError(f"{path.name}: el archivo no es UTF-8 válido.") from exc
    except json.JSONDecodeError as exc:
        raise ImportContentError(f"{path.name}: JSON inválido en línea {exc.lineno}, columna {exc.colno}.") from exc
    except (OSError, RecursionError) as exc:
        raise ImportContentError(f"{path.name}: no se pudo leer o procesar el documento de forma segura.") from exc


def _validate_document(document, filename):
    _expect_keys(document, TOP_KEYS, filename)
    if type(document["schema_version"]) is not int or document["schema_version"] != SCHEMA_VERSION:
        raise ImportContentError(f"{filename}.schema_version: versión no soportada.")
    _string(document["resumen_cambios"], f"{filename}.resumen_cambios", max_length=10000)

    snapshot = document["snapshot"]
    _expect_keys(snapshot, SNAPSHOT_KEYS, f"{filename}.snapshot")
    if type(snapshot["esquema_version"]) is not int or snapshot["esquema_version"] != 1:
        raise ImportContentError(f"{filename}.snapshot.esquema_version: versión no soportada.")

    lesson = snapshot["leccion"]
    _expect_keys(lesson, LESSON_KEYS, f"{filename}.snapshot.leccion")
    lesson_uuid = _uuid(lesson["clave"], f"{filename}.snapshot.leccion.clave")
    _string(lesson["titulo"], f"{filename}.snapshot.leccion.titulo", required=True, max_length=220)
    _string(lesson["descripcion"], f"{filename}.snapshot.leccion.descripcion")
    _string(lesson["tipo"], f"{filename}.snapshot.leccion.tipo", required=True, max_length=20)
    if lesson["tipo"] not in {item[0] for item in Leccion.TIPOS}:
        raise ImportContentError(f"{filename}.snapshot.leccion.tipo: tipo curricular no permitido.")

    content = snapshot["contenido"]
    _expect_keys(content, CONTENT_KEYS, f"{filename}.snapshot.contenido")
    for field in CONTENT_KEYS:
        _string(content[field], f"{filename}.snapshot.contenido.{field}", required=field in {
            "objetivos_aprendizaje", "teoria_tecnica", "explicacion_sencilla"
        })

    examples = snapshot["ejemplos"]
    exercises = snapshot["ejercicios"]
    sources = document["fuentes"]
    if not isinstance(examples, list) or len(examples) > MAX_EXAMPLES:
        raise ImportContentError(f"{filename}.snapshot.ejemplos: lista inválida o supera {MAX_EXAMPLES}.")
    if not isinstance(exercises, list) or len(exercises) > MAX_EXERCISES:
        raise ImportContentError(f"{filename}.snapshot.ejercicios: lista inválida o supera {MAX_EXERCISES}.")
    if not isinstance(sources, list) or not 1 <= len(sources) <= MAX_SOURCES:
        raise ImportContentError(f"{filename}.fuentes: debe contener entre 1 y {MAX_SOURCES} referencias.")

    resource_ids = set()
    for index, example in enumerate(examples):
        path = f"{filename}.snapshot.ejemplos[{index}]"
        _expect_keys(example, EXAMPLE_KEYS, path)
        resource_uuid = _uuid(example["clave"], f"{path}.clave")
        if resource_uuid in resource_ids or resource_uuid == lesson_uuid:
            raise ImportContentError(f"{path}.clave: UUID duplicado en el documento.")
        resource_ids.add(resource_uuid)
        _string(example["titulo"], f"{path}.titulo", required=True, max_length=180)
        for field in EXAMPLE_KEYS - {"clave", "titulo", "orden"}:
            _string(example[field], f"{path}.{field}", max_length=40 if field == "lenguaje" else None)
        _integer(example["orden"], f"{path}.orden")

    for index, exercise in enumerate(exercises):
        path = f"{filename}.snapshot.ejercicios[{index}]"
        _expect_keys(exercise, EXERCISE_KEYS, path)
        resource_uuid = _uuid(exercise["clave"], f"{path}.clave")
        if resource_uuid in resource_ids or resource_uuid == lesson_uuid:
            raise ImportContentError(f"{path}.clave: UUID duplicado en el documento.")
        resource_ids.add(resource_uuid)
        _string(exercise["titulo"], f"{path}.titulo", required=True, max_length=180)
        _string(exercise["enunciado"], f"{path}.enunciado", required=True)
        for field in ("instrucciones", "lenguaje", "codigo_inicial"):
            _string(exercise[field], f"{path}.{field}", max_length=40 if field == "lenguaje" else None)
        _string(exercise["nivel"], f"{path}.nivel", required=True, max_length=16)
        if exercise["nivel"] not in {item[0] for item in EjercicioLeccion.NIVELES}:
            raise ImportContentError(f"{path}.nivel: nivel no permitido.")
        if type(exercise["obligatorio"]) is not bool:
            raise ImportContentError(f"{path}.obligatorio: debe ser booleano.")
        _integer(exercise["orden"], f"{path}.orden")

    source_ids = set()
    for index, source in enumerate(sources):
        path = f"{filename}.fuentes[{index}]"
        _expect_keys(source, SOURCE_KEYS, path)
        source_uuid = _uuid(source["clave"], f"{path}.clave")
        if source_uuid in source_ids:
            raise ImportContentError(f"{path}.clave: fuente repetida.")
        source_ids.add(source_uuid)
        _string(source["rol"], f"{path}.rol", required=True, max_length=16)
        _string(source["uso_declarado"], f"{path}.uso_declarado", required=True, max_length=16)
        if source["rol"] not in SOURCE_ROLES:
            raise ImportContentError(f"{path}.rol: rol no permitido.")
        if source["uso_declarado"] not in SOURCE_USES:
            raise ImportContentError(f"{path}.uso_declarado: uso no permitido.")
        _string(source["localizador"], f"{path}.localizador", max_length=500)
        _string(source["nota_atribucion"], f"{path}.nota_atribucion")

    return lesson_uuid


def _validate_against_database(document, filename):
    snapshot = document["snapshot"]
    lesson_uuid = _validate_document(document, filename)
    try:
        lesson = Leccion.objects.select_related("modulo").get(clave_contenido=lesson_uuid)
    except Leccion.DoesNotExist as exc:
        raise ImportContentError(f"{filename}: la lección UUID no existe en ASCENSO.") from exc

    lesson_data = snapshot["leccion"]
    if (lesson.titulo, lesson.descripcion, lesson.tipo) != (
        lesson_data["titulo"], lesson_data["descripcion"], lesson_data["tipo"]
    ):
        raise ImportContentError(f"{filename}: la identidad curricular no coincide con ASCENSO.")

    example_ids = {item["clave"] for item in snapshot["ejemplos"]}
    existing_examples = {
        str(item.clave_contenido): item
        for item in EjemploLeccion.objects.filter(leccion=lesson, clave_contenido__in=example_ids)
    }
    if len(existing_examples) != len(example_ids):
        raise ImportContentError(f"{filename}: uno o más UUID de ejemplo no pertenecen a esta lección.")
    exercise_ids = {item["clave"] for item in snapshot["ejercicios"]}
    existing_exercises = {
        str(item.clave_contenido): item
        for item in EjercicioLeccion.objects.filter(leccion=lesson, clave_contenido__in=exercise_ids)
    }
    if len(existing_exercises) != len(exercise_ids):
        raise ImportContentError(f"{filename}: uno o más UUID de ejercicio no pertenecen a esta lección.")

    source_uuids = [item["clave"] for item in document["fuentes"]]
    sources = {str(item.clave): item for item in FuenteConocimiento.objects.filter(clave__in=source_uuids)}
    if len(sources) != len(source_uuids):
        raise ImportContentError(f"{filename}: una o más fuentes no están registradas.")
    inactive = [source.titulo for source in sources.values() if not source.activa]
    if inactive:
        raise ImportContentError(f"{filename}: contiene fuentes inactivas: {', '.join(inactive)}.")
    warnings = [
        f"Fuente '{sources[item['clave']].titulo}' con licencia '{sources[item['clave']].estado_revision_licencia}'."
        for item in document["fuentes"]
        if sources[item["clave"]].estado_revision_licencia != "compatible"
    ]
    return lesson, sources, warnings


def _same_provenance(version, item):
    expected = {
        (source["clave"], source["rol"], source["uso_declarado"], source["localizador"], source["nota_atribucion"])
        for source in item["document"]["fuentes"]
    }
    existing = set(version.referencias.values_list(
        "fuente__clave", "rol", "uso_declarado", "localizador", "nota_atribucion"
    ))
    return expected == {(str(key), role, usage, locator, note) for key, role, usage, locator, note in existing}

def validar_directorio_contenido(directory):
    """Valida el lote completo sin escribir en la base de datos."""
    supplied_root = Path(directory).expanduser()
    if supplied_root.is_symlink():
        raise ImportContentError("El directorio de entrada no puede ser un symlink.")
    root = supplied_root.resolve()
    if not root.exists() or not root.is_dir():
        raise ImportContentError("El directorio de entrada no existe o no es un directorio regular.")
    paths = sorted(root.iterdir(), key=lambda item: item.name)
    if not paths or len(paths) > MAX_DOCUMENTS:
        raise ImportContentError(f"El lote debe contener entre 1 y {MAX_DOCUMENTS} archivos.")
    if any(path.is_symlink() or not path.is_file() or path.suffix.lower() != ".json" for path in paths):
        raise ImportContentError("El directorio solo puede contener archivos JSON regulares; no se admiten subdirectorios ni symlinks.")

    validated = []
    errors = []
    warnings = []
    seen_lessons = set()
    seen_resources = set()
    for path in paths:
        try:
            document = _load_json(path)
            lesson_uuid = _validate_document(document, path.name)
            if lesson_uuid in seen_lessons:
                raise ImportContentError("La misma lección aparece más de una vez en el lote.")
            if str(lesson_uuid) in seen_resources:
                raise ImportContentError("El UUID de la lección ya fue asignado a otro recurso del lote.")
            seen_lessons.add(lesson_uuid)
            for item in document["snapshot"]["ejemplos"] + document["snapshot"]["ejercicios"]:
                resource_uuid = item["clave"]
                if resource_uuid in seen_resources or uuid.UUID(resource_uuid) in seen_lessons:
                    raise ImportContentError(f"UUID de recurso repetido o reasignado en el lote: {resource_uuid}.")
                seen_resources.add(resource_uuid)
            lesson, sources, doc_warnings = _validate_against_database(document, path.name)
            canonical = json.dumps(document["snapshot"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
            duplicate = any(
                _same_provenance(version, {"document": document})
                for version in VersionContenidoLeccion.objects.filter(leccion=lesson, sha256=digest)
            )
            validated.append({
                "filename": path.name,
                "document": document,
                "lesson": lesson,
                "sources": sources,
                "sha256": digest,
                "duplicate": duplicate,
                "warnings": doc_warnings,
            })
            warnings.extend(f"{path.name}: {warning}" for warning in doc_warnings)
        except (ImportContentError, ValidationError) as exc:
            errors.append(f"{path.name}: {exc}")
    return {
        "documents": len(paths),
        "valid": len(validated),
        "errors": errors,
        "warnings": warnings,
        "items": validated if not errors else [],
    }


@transaction.atomic
def importar_documentos_validados(report, *, actor):
    """Crea borradores y referencias; no modifica el contenido activo ni publica."""
    if not getattr(actor, "is_authenticated", False) or not getattr(actor, "is_active", False) or not getattr(actor, "is_staff", False):
        raise ValidationError("La importación requiere un editor activo (is_staff).")
    if report["errors"] or len(report["items"]) != report["documents"]:
        raise ValidationError("El lote tiene errores o no fue validado íntegramente.")

    created = []
    duplicates = []
    for item in report["items"]:
        lesson = Leccion.objects.select_for_update().get(pk=item["lesson"].pk)
        candidates = VersionContenidoLeccion.objects.filter(leccion=lesson, sha256=item["sha256"])
        existing = next((version for version in candidates if _same_provenance(version, item)), None)
        if existing:
            duplicates.append(existing)
            continue
        latest = VersionContenidoLeccion.objects.filter(leccion=lesson).aggregate(value=Max("numero_version"))["value"] or 0
        version = VersionContenidoLeccion.objects.create(
            leccion=lesson,
            numero_version=latest + 1,
            esquema_version=item["document"]["snapshot"]["esquema_version"],
            estado="borrador",
            snapshot=item["document"]["snapshot"],
            sha256=item["sha256"],
            resumen_cambios=item["document"]["resumen_cambios"],
        )
        for source_data in item["document"]["fuentes"]:
            referencia = ReferenciaFuenteContenido(
                version=version,
                fuente=item["sources"][source_data["clave"]],
                rol=source_data["rol"],
                uso_declarado=source_data["uso_declarado"],
                localizador=source_data["localizador"],
                nota_atribucion=source_data["nota_atribucion"],
            )
            referencia.full_clean()
            referencia.save()
        created.append(version)
    return {"created": created, "duplicates": duplicates}
