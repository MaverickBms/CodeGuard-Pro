"""Casos de uso de entrega y evaluación de ejercicios.

Este módulo NO ejecuta código del estudiante. Solo compara texto o comprueba
la presencia/ausencia de fragmentos estáticos. La ejecución real requerirá un
sandbox aislado y no debe añadirse al proceso Django.
"""

from __future__ import annotations

import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone

from apps.audit.services import registrar_evento

from .models import (
    ContenidoLeccionActivo, ContenidoLeccionPaquete, EstadoSincronizacion,
    EjercicioLeccion, Progreso,
)
from .models_attempts import ConfiguracionEvaluacion, IntentoEjercicio
from .services import recalcular_progreso_etapa

MAX_RESPUESTA_CARACTERES = 20000


def _normalizar(texto: str) -> str:
    """Colapsa espacios consecutivos sin alterar el contenido léxico."""
    return re.sub(r"\s+", " ", texto.strip())


def _evaluar_configuracion(configuracion: ConfiguracionEvaluacion, respuesta: str) -> dict:
    datos = configuracion.configuracion
    if not isinstance(datos, dict):
        raise ValidationError("La configuración del evaluador debe ser un objeto.")

    if configuracion.tipo == "respuesta_exacta":
        esperada = datos.get("respuesta_esperada")
        if not isinstance(esperada, str) or not esperada.strip():
            raise ValidationError("El evaluador exacto necesita una respuesta_esperada válida.")
        sensible = datos.get("sensible_mayusculas", True)
        normalizar_espacios = datos.get("normalizar_espacios", True)
        if not isinstance(sensible, bool) or not isinstance(normalizar_espacios, bool):
            raise ValidationError("Las opciones del evaluador exacto deben ser booleanas.")

        enviada = _normalizar(respuesta) if normalizar_espacios else respuesta.strip()
        correcta = _normalizar(esperada) if normalizar_espacios else esperada.strip()
        if not sensible:
            enviada, correcta = enviada.casefold(), correcta.casefold()
        aprobado = enviada == correcta
        return {
            "resultado": "aprobado" if aprobado else "no_aprobado",
            "puntuacion": 100 if aprobado else 0,
            "retroalimentacion": (
                "Respuesta correcta. Has cumplido el criterio configurado."
                if aprobado
                else "La respuesta todavía no coincide con el criterio esperado. Revisa el concepto y vuelve a intentarlo."
            ),
            "detalles": {"coincidencia_exacta": aprobado},
        }

    if configuracion.tipo == "codigo_contiene":
        requeridos = datos.get("fragmentos_requeridos")
        prohibidos = datos.get("fragmentos_prohibidos", [])
        if (
            not isinstance(requeridos, list)
            or not requeridos
            or any(not isinstance(item, str) or not item for item in requeridos)
        ):
            raise ValidationError("El evaluador de código necesita fragmentos_requeridos válidos.")
        if (
            not isinstance(prohibidos, list)
            or any(not isinstance(item, str) or not item for item in prohibidos)
        ):
            raise ValidationError("fragmentos_prohibidos debe ser una lista de textos no vacíos.")
        if len(requeridos) > 50 or len(prohibidos) > 50:
            raise ValidationError("El evaluador admite como máximo 50 fragmentos por categoría.")

        encontrados = sum(fragmento in respuesta for fragmento in requeridos)
        detectados = sum(fragmento in respuesta for fragmento in prohibidos)
        aprobado = encontrados == len(requeridos) and detectados == 0
        puntuacion = round(100 * encontrados / len(requeridos))
        if detectados:
            puntuacion = 0
        return {
            "resultado": "criterios_cumplidos" if aprobado else "no_aprobado",
            "puntuacion": puntuacion,
            "retroalimentacion": (
                "La comprobación estática encontró todos los elementos requeridos; esto no constituye una aprobación académica."
                if aprobado
                else "La comprobación estática detectó elementos pendientes o no permitidos. Esto no equivale a ejecutar ni verificar el comportamiento del programa."
            ),
            "detalles": {
                "fragmentos_requeridos_encontrados": encontrados,
                "total_fragmentos_requeridos": len(requeridos),
                "fragmentos_prohibidos_detectados": detectados,
                "tipo_comprobacion": "estatica",
            },
        }

    raise ValidationError("El tipo de evaluador no está soportado.")


def _completar_leccion_si_corresponde(usuario, leccion, actor_auditoria=None) -> bool:
    """Completa la lección solo si todos los ejercicios obligatorios de la versión activa tienen evidencia aprobada."""
    channel = getattr(settings, "CODEGUARD_KNOWLEDGE_CHANNEL", "stable")
    sync_state = (
        EstadoSincronizacion.objects.select_related("active_package")
        .filter(channel=channel, active_package__isnull=False)
        .first()
    )
    package = sync_state.active_package if sync_state else None
    puntero_activo = None
    if package:
        installed = ContenidoLeccionPaquete.objects.filter(
            paquete=package, leccion=leccion
        ).first()
        if installed is None:
            return False
        claves_requeridas = [
            item.get("clave")
            for item in installed.documento["snapshot"].get("ejercicios", [])
            if item.get("obligatorio")
        ]
    else:
        puntero_activo = (
            ContenidoLeccionActivo.objects.select_related("version")
            .filter(leccion=leccion)
            .first()
        )
        claves_requeridas = [
            item.get("clave")
            for item in puntero_activo.version.snapshot.get("ejercicios", [])
            if item.get("obligatorio")
        ] if puntero_activo else []

    if package or puntero_activo:
        ejercicios_por_clave = {
            str(item.clave_contenido): item for item in leccion.ejercicios.all()
        }
        if not claves_requeridas or any(clave not in ejercicios_por_clave for clave in claves_requeridas):
            return False
        requeridos = [ejercicios_por_clave[clave] for clave in claves_requeridas]
    else:
        requeridos = list(leccion.ejercicios.filter(obligatorio=True))
        if not requeridos or any(not ejercicio.publicado for ejercicio in requeridos):
            return False

    for ejercicio in requeridos:
        configuracion = ejercicio.configuraciones_evaluacion.filter(
            activo=True, permite_completar_leccion=True
        ).order_by("-version").first()
        if configuracion is None:
            return False
        evidencia = IntentoEjercicio.objects.filter(
            usuario=usuario,
            ejercicio=ejercicio,
            configuracion_evaluacion=configuracion,
            resultado="aprobado",
        )
        if package:
            evidencia = evidencia.filter(paquete_contenido=package)
        if not evidencia.exists():
            return False

    progreso, _ = Progreso.objects.get_or_create(
        usuario=usuario,
        etapa=leccion.modulo.etapa,
        modulo=leccion.modulo,
        leccion=leccion,
        actividad=None,
        defaults={"estado": "no_iniciado", "porcentaje": 0},
    )
    if progreso.estado == "completado":
        return False

    progreso.estado = "completado"
    progreso.porcentaje = 100
    progreso.fecha_completado = timezone.now()
    progreso.save()

    recalcular_progreso_etapa(usuario, leccion.modulo.etapa)
    registrar_evento(
        "roadmap_leccion_completada_por_evidencia",
        usuario=actor_auditoria,
        descripcion=f"Lección {leccion.id} completada tras aprobar {len(requeridos)} ejercicio(s).",
    )
    return True


@transaction.atomic
def registrar_intento_ejercicio(
    usuario,
    ejercicio: EjercicioLeccion,
    respuesta: str,
    *,
    actor_auditoria=None,
) -> IntentoEjercicio:
    """Guarda una entrega y aplica el evaluador estático configurado, si existe."""
    if usuario is None or not getattr(usuario, "is_authenticated", False):
        raise ValidationError("No existe un usuario propietario para guardar el intento.")
    if not isinstance(respuesta, str) or not respuesta.strip():
        raise ValidationError("Escribe una respuesta antes de enviar el intento.")
    if len(respuesta) > MAX_RESPUESTA_CARACTERES:
        raise ValidationError(
            f"La respuesta supera el límite de {MAX_RESPUESTA_CARACTERES} caracteres."
        )

    channel = getattr(settings, "CODEGUARD_KNOWLEDGE_CHANNEL", "stable")
    sync_state = (
        EstadoSincronizacion.objects.select_related("active_package")
        .filter(channel=channel, active_package__isnull=False)
        .first()
    )
    paquete_contenido = sync_state.active_package if sync_state else None
    contenido_instalado = None
    puntero_activo = None
    if paquete_contenido:
        contenido_instalado = ContenidoLeccionPaquete.objects.filter(
            paquete=paquete_contenido, leccion=ejercicio.leccion
        ).first()
        if contenido_instalado is None:
            raise ValidationError("La lección no está incluida en el paquete académico activo.")
        version_contenido = None
        snapshot_ejercicio = next(
            (
                item for item in contenido_instalado.documento["snapshot"].get("ejercicios", [])
                if item.get("clave") == str(ejercicio.clave_contenido)
            ),
            None,
        )
        if snapshot_ejercicio is None:
            raise ValidationError("El ejercicio no pertenece al paquete académico activo.")
    else:
        puntero_activo = (
            ContenidoLeccionActivo.objects.select_related("version")
            .filter(leccion=ejercicio.leccion)
            .first()
        )
        version_contenido = puntero_activo.version if puntero_activo else None
    if not paquete_contenido and version_contenido is None:
        if ejercicio.leccion.versiones_contenido.filter(
            estado__in=["publicada", "sustituida", "retirada"]
        ).exists():
            raise ValidationError("La lección no tiene una versión académica activa.")
        if not ejercicio.publicado:
            raise ValidationError("Este ejercicio no está publicado.")
    if not paquete_contenido and version_contenido is not None:
        snapshot_ejercicio = next(
            (
                item for item in version_contenido.snapshot.get("ejercicios", [])
                if item.get("clave") == str(ejercicio.clave_contenido)
            ),
            None,
        )
        if snapshot_ejercicio is None:
            raise ValidationError(
                "El ejercicio no pertenece a la versión académica activa de esta lección."
            )
    elif not paquete_contenido:
        # Compatibilidad: conserva el enunciado exacto de ejercicios anteriores al versionado activo.
        snapshot_ejercicio = {
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

    configuracion = ejercicio.configuraciones_evaluacion.filter(
        activo=True
    ).order_by("-version").first()

    if configuracion is None or not configuracion.activo:
        evaluacion = {
            "resultado": "pendiente_revision",
            "puntuacion": None,
            "retroalimentacion": "Entrega guardada. Este ejercicio todavía no tiene un evaluador automático activo.",
            "detalles": {"tipo_comprobacion": "sin_configurar"},
        }
        version = None
        evaluado_en = None
    else:
        evaluacion = _evaluar_configuracion(configuracion, respuesta)
        version = configuracion.version
        evaluado_en = timezone.now()

    intento = IntentoEjercicio.objects.create(
        ejercicio=ejercicio,
        usuario=usuario,
        respuesta=respuesta,
        version_contenido=version_contenido,
        paquete_contenido=paquete_contenido,
        snapshot_ejercicio=snapshot_ejercicio,
        resultado=evaluacion["resultado"],
        puntuacion=evaluacion["puntuacion"],
        retroalimentacion=evaluacion["retroalimentacion"],
        detalles=evaluacion["detalles"],
        configuracion_evaluacion=configuracion,
        version_evaluacion=version,
        evaluado_en=evaluado_en,
    )

    registrar_evento(
        "roadmap_ejercicio_intento_registrado",
        usuario=actor_auditoria,
        descripcion=(
            f"Ejercicio {ejercicio.id}; intento {intento.id}; "
            f"resultado {intento.resultado}."
        ),
    )

    if intento.resultado == "aprobado":
        _completar_leccion_si_corresponde(
            usuario, ejercicio.leccion, actor_auditoria=actor_auditoria
        )

    return intento
