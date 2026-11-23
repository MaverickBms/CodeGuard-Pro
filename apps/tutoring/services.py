"""Servicios del tutor inteligente local (Fase 3).

Se comunica con Ollama local (``http://localhost:11434``) para obtener
explicaciones y pistas sin ejecutar código del estudiante. Si Ollama no está
disponible, se degrada a respuestas basadas en reglas estáticas.

El tutor nunca ejecuta código del estudiante, nunca revela la solución
completa y nunca decide la aprobación académica (fuente de verdad: el validador
determinista).
"""

from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.request
from typing import Optional
from urllib.parse import urlsplit

from django.conf import settings
from django.db import transaction
from django.db.models import F
from django.utils import timezone

from apps.audit.services import registrar_evento

from .models import IntentoTutoria, PistaTutoria, SesionTutoria

logger = logging.getLogger("codeguard")

TUTOR_MODEL = settings.CODEGUARD_TUTOR_MODEL
TUTOR_BASE_URL = settings.CODEGUARD_TUTOR_BASE_URL
TUTOR_TIMEOUT_SECONDS = int(settings.CODEGUARD_TUTOR_TIMEOUT)
LIMITE_PISTAS_TUTORIA = 3
TIPOS_PISTA = ("orientacion", "estrategia", "concretizacion")


class TutorNoDisponible(Exception):
    """El tutor IA no está disponible (Ollama no responde)."""


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Impide que una petición con código del estudiante siga redirecciones."""

    def redirect_request(self, request, response, code, message, headers, new_url):
        return None


def _url_ollama_local() -> str:
    """Valida que el tutor solo pueda enviar datos a Ollama en loopback."""
    try:
        parsed = urlsplit(TUTOR_BASE_URL)
        hostname = (parsed.hostname or "").lower()
        port = parsed.port
    except ValueError as exc:
        raise TutorNoDisponible("La URL local del tutor no es válida.") from exc

    if (
        parsed.scheme != "http"
        or hostname not in {"localhost", "127.0.0.1", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
        or port == 0
    ):
        raise TutorNoDisponible(
            "El tutor solo admite una instancia Ollama local (localhost/loopback)."
        )

    return TUTOR_BASE_URL.rstrip("/") + "/api/chat"


def _llamar_ollama(
    sistema: str,
    usuario: str,
    modelo: Optional[str] = None,
    *,
    timeout: float | None = None,
) -> str:
    """Envía una solicitud a Ollama y devuelve la respuesta de texto.

    Usa exclusivamente la librería estándar (urllib) para no añadir
    dependencias externas al proyecto.

    Lanza ``TutorNoDisponible`` si Ollama no responde o devuelve error.
    """
    url = _url_ollama_local()
    payload = json.dumps(
        {
            "model": modelo or TUTOR_MODEL,
            "messages": [
                {"role": "system", "content": sistema},
                {"role": "user", "content": usuario},
            ],
            "stream": False,
            "keep_alive": "5m",
            "options": {"temperature": 0.3, "num_predict": 90},
        }
    ).encode("utf-8")

    requisito = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({}),
            _NoRedirectHandler(),
        )
        with opener.open(
            requisito, timeout=timeout if timeout is not None else TUTOR_TIMEOUT_SECONDS
        ) as respuesta:
            datos = json.loads(respuesta.read().decode("utf-8"))
        return str((datos.get("message") or {}).get("content") or "").strip()
    except Exception as exc:  # noqa: BLE001 — degradación controlada del tutor
        logger.warning("Tutor IA (Ollama) no disponible: %s", exc)
        raise TutorNoDisponible("El tutor IA no está disponible en este momento.") from exc


def _sistema_tutor() -> str:
    """Devuelve el prompt del sistema para el tutor."""
    return (
        "Eres un tutor de programación para CodeGuard Pro. Tu rol es ACOMPAÑAR, "
        "no resolver. Reglas estrictas:\n"
        "1. Nunca entregues la solución completa ni el código final del ejercicio.\n"
        "2. Máximo 3 pistas por ejercicio. Si ya se entregaron 3, no des más.\n"
        "3. Explica errores de sintaxis, lógica y enfoque de forma gradual.\n"
        "4. Relaciona el intento del estudiante con el objetivo del ejercicio.\n"
        "5. Sé claro sobre qué es una respuesta del tutor y qué es del validador automático.\n"
        "6. No decidas la aprobación académica; eso corresponde al evaluador determinista.\n"
        "7. Responde en español, de forma concisa y pedagógica.\n"
        "8. No ejecutes ni sugieras ejecutar código arbitrario del estudiante.\n"
    )


def _sistema_tutor_pista() -> str:
    """Prompt compacto para reducir latencia en equipos sin GPU."""
    return (
        "Eres un tutor de programación en español. Da una sola pista concreta, "
        "máximo dos frases, basada en el enunciado. No reveles la solución, no "
        "escribas el código final y no decidas la aprobación académica."
    )


def obtener_sesion(usuario, ejercicio) -> SesionTutoria:
    """Obtiene o crea la sesión de tutoría para un usuario y ejercicio."""
    sesion, _ = SesionTutoria.objects.get_or_create(
        usuario=usuario,
        ejercicio=ejercicio,
    )
    return sesion


def _pista_estatica(ejercicio, numero_pista: int) -> str:
    """Devuelve una pista basada en reglas estáticas cuando Ollama no está disponible."""
    pista = (getattr(ejercicio, f"pista_{numero_pista}", "") or "").strip()
    if not pista:
        pista = (
            f"Revisa el enunciado del ejercicio '{ejercicio.titulo}' y los "
            f"ejemplos de la lección antes de intentarlo de nuevo."
        )
    return pista


def entregar_pista(usuario, ejercicio, tipo_pista: str = "orientacion") -> dict:
    """Entrega una pista y reserva su número de forma atómica por sesión.

    La llamada al modelo ocurre fuera de la transacción. El contador se incrementa
    mediante una actualización condicional dentro de una transacción de escritura;
    así SQLite serializa las reservas y no permite superar el límite ni duplicar
    el número de pista.
    """
    sesion = obtener_sesion(usuario, ejercicio)

    if sesion.limite_alcanzado:
        return {
            "exito": False,
            "error": "Límite de 3 pistas alcanzado para este ejercicio.",
            "restantes": 0,
        }

    contexto = (
        f"Ejercicio: {ejercicio.titulo}\\n"
        f"Enunciado: {ejercicio.enunciado}\\n"
        f"Instrucciones: {ejercicio.instrucciones or 'Sin instrucciones adicionales.'}\\n"
        f"Lenguaje: {ejercicio.lenguaje or 'No especificado'}\\n"
        f"Nivel: {ejercicio.nivel}\\n"
        "Entrega una pista gradual, sin revelar la solución completa. "
        "Máximo tres pistas en total para este ejercicio.\\n"
    )

    if tipo_pista == "orientacion":
        contexto += (
            "La estudiante necesita orientación hacia el concepto relevante. "
            "No des la solución, solo señala la zona o concepto a revisar."
        )
    elif tipo_pista == "estrategia":
        contexto += (
            "La estudiante necesita una estrategia o enfoque posible para resolver. "
            "Sugiere un camino sin escribir el código final."
        )
    elif tipo_pista == "concretizacion":
        contexto += (
            "La estudiante necesita una orientación más concreta, pero AÚN ASÍ "
            "no entregues la solución completa ni el código final."
        )

    try:
        contenido_pista = _llamar_ollama(
            sistema=_sistema_tutor_pista(),
            usuario=contexto,
        )
        if not contenido_pista or not contenido_pista.strip():
            contenido_pista = None
    except TutorNoDisponible:
        contenido_pista = None

    with transaction.atomic():
        reservada = SesionTutoria.objects.filter(
            pk=sesion.pk,
            pistas_utilizadas__lt=LIMITE_PISTAS_TUTORIA,
        ).update(
            pistas_utilizadas=F("pistas_utilizadas") + 1,
            ultima_pista_en=timezone.now(),
        )

        if not reservada:
            return {
                "exito": False,
                "error": "Límite de 3 pistas alcanzado para este ejercicio.",
                "restantes": 0,
            }

        sesion.refresh_from_db(fields=["pistas_utilizadas"])
        numero_pista = sesion.pistas_utilizadas
        if contenido_pista is None:
            contenido_pista = _pista_estatica(ejercicio, numero_pista)

        PistaTutoria.objects.create(
            sesion=sesion,
            tipo=tipo_pista,
            contenido=contenido_pista,
            numero_pista=numero_pista,
        )

    registrar_evento(
        "tutoria_pista_entregada",
        usuario=usuario,
        descripcion=f"Ejercicio {ejercicio.titulo} — pista {numero_pista}/{LIMITE_PISTAS_TUTORIA}",
    )

    return {
        "exito": True,
        "pista": contenido_pista,
        "numero": numero_pista,
        "restantes": max(0, LIMITE_PISTAS_TUTORIA - numero_pista),
    }


def analizar_intento(usuario, ejercicio, intento_ejercicio) -> IntentoTutoria:
    """Analiza un intento de ejercicio y registra la respuesta del tutor.

    El tutor explica el resultado de la evaluación determinista, pero nunca
    decide la aprobación académica.
    """
    resultado_evaluacion = (
        "aprobado"
        if intento_ejercicio.resultado == "aprobado"
        else "no_aprobado"
        if intento_ejercicio.resultado == "no_aprobado"
        else "pendiente_revision"
    )
    contenido_leccion = getattr(ejercicio.leccion, "contenido", None)
    objetivos = (
        (contenido_leccion.objetivos_aprendizaje or "").strip()[:300]
        if contenido_leccion is not None
        else ""
    )
    contexto = (
        f"Etapa: {ejercicio.leccion.modulo.etapa.numero}\n"
        f"Módulo: {ejercicio.leccion.modulo.titulo}\n"
        f"Lección: {ejercicio.leccion.titulo}\n"
        f"Objetivos: {objetivos or 'No declarados.'}\n"
        f"Ejercicio: {ejercicio.titulo}\n"
        f"Enunciado: {ejercicio.enunciado}\n"
        f"Intento del estudiante: {intento_ejercicio.respuesta}\n"
        f"Resultado del validador automático: {resultado_evaluacion}\n"
        f"Retroalimentación del validador: {intento_ejercicio.retroalimentacion}\n"
        "Explica al estudiante qué indica el resultado, qué puede revisar y "
        "qué conceptos le conviene repasar. NO entregues la solución completa."
    )

    try:
        analisis = _llamar_ollama(
            sistema=_sistema_tutor(),
            usuario=contexto,
        )
    except TutorNoDisponible:
        analisis = (
            f"El validador automático indica que el ejercicio '{ejercicio.titulo}' "
            f"está {resultado_evaluacion}. "
            f"{intento_ejercicio.retroalimentacion or ''} "
            "Si necesitas ayuda, intenta de nuevo o revisa los ejemplos de la lección."
        )

    return IntentoTutoria.objects.create(
        usuario=usuario,
        ejercicio=ejercicio,
        intento_ejercicio=intento_ejercicio,
        resultado_evaluacion=resultado_evaluacion,
        analisis_tutor=analisis,
    )


ESTADO_CACHE_SEGUNDOS = 30
_estado_cache: dict = {"checked_at": 0.0, "valor": None}


def _listar_modelos(timeout: float = 2.0) -> list[str]:
    """Consulta /api/tags sin generar texto ni cargar un modelo en memoria."""
    _url_ollama_local()  # Valida esquema, host loopback y ausencia de credenciales.
    url = TUTOR_BASE_URL.rstrip("/") + "/api/tags"
    requisito = urllib.request.Request(
        url,
        headers={"Accept": "application/json"},
        method="GET",
    )
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({}),
        _NoRedirectHandler(),
    )
    try:
        with opener.open(requisito, timeout=timeout) as respuesta:
            datos = json.loads(respuesta.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 — el estado nunca rompe la interfaz
        logger.info("Tutor IA: Ollama no responde al listado de modelos: %s", exc)
        raise TutorNoDisponible(
            "Ollama no está disponible en el puerto local configurado."
        ) from exc

    modelos = datos.get("models") if isinstance(datos, dict) else None
    if not isinstance(modelos, list):
        raise TutorNoDisponible("Ollama devolvió un listado de modelos no válido.")
    return [
        str(item.get("name", "")).strip()
        for item in modelos
        if isinstance(item, dict) and str(item.get("name", "")).strip()
    ]


def _modelo_instalado(modelos: list[str], modelo: str) -> bool:
    return any(
        nombre == modelo or nombre.startswith(f"{modelo}:")
        for nombre in modelos
    )


def estado_tutor(*, forzar: bool = False, timeout: float = 2.0) -> dict:
    """Estado operativo del tutor local con caché breve.

    Distingue entre Ollama no disponible y Ollama disponible sin el modelo
    configurado. En ambos casos la aplicación sigue operativa con pistas
    deterministas locales.
    """
    ahora = time.monotonic()
    if (
        not forzar
        and _estado_cache["valor"] is not None
        and ahora - _estado_cache["checked_at"] < ESTADO_CACHE_SEGUNDOS
    ):
        return dict(_estado_cache["valor"])

    try:
        modelos = _listar_modelos(timeout=timeout)
    except TutorNoDisponible:
        valor = {
            "disponible": False,
            "ollama": False,
            "modelo": TUTOR_MODEL,
            "modelo_instalado": False,
            "modo": "determinista",
        }
    else:
        instalado = _modelo_instalado(modelos, TUTOR_MODEL)
        valor = {
            "disponible": instalado,
            "ollama": True,
            "modelo": TUTOR_MODEL,
            "modelo_instalado": instalado,
            "modo": "ollama" if instalado else "determinista",
        }

    _estado_cache["checked_at"] = ahora
    _estado_cache["valor"] = dict(valor)
    return valor


def esta_disponible() -> bool:
    """Devuelve True si Ollama responde y el modelo configurado está instalado."""
    return bool(estado_tutor()["disponible"])
