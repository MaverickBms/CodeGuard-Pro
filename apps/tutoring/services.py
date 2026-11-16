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
import urllib.error
import urllib.request
from typing import Optional

from django.conf import settings
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


def _llamar_ollama(sistema: str, usuario: str, modelo: Optional[str] = None) -> str:
    """Envía una solicitud a Ollama y devuelve la respuesta de texto.

    Usa exclusivamente la librería estándar (urllib) para no añadir
    dependencias externas al proyecto.

    Lanza ``TutorNoDisponible`` si Ollama no responde o devuelve error.
    """
    url = f"{TUTOR_BASE_URL}/api/chat"
    payload = json.dumps(
        {
            "model": modelo or TUTOR_MODEL,
            "messages": [
                {"role": "system", "content": sistema},
                {"role": "user", "content": usuario},
            ],
            "stream": False,
            "options": {"temperature": 0.4, "num_predict": 500},
        }
    ).encode("utf-8")

    requisito = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(requisito, timeout=TUTOR_TIMEOUT_SECONDS) as respuesta:
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
    """Entrega una pista al estudiante para un ejercicio.

    Respeta el límite de 3 pistas por ejercicio. Devuelve un diccionario con:
    - exito: bool
    - pista: str (contenido de la pista)
    - numero: int (número de pista entregada)
    - restantes: int (pistas que quedan)
    - error: str (si no se pudo entregar)
    """
    sesion = obtener_sesion(usuario, ejercicio)

    if sesion.limite_alcanzado:
        return {
            "exito": False,
            "error": "Límite de 3 pistas alcanzado para este ejercicio.",
            "restantes": 0,
        }

    numero_pista = sesion.pistas_utilizadas + 1

    contexto = (
        f"Ejercicio: {ejercicio.titulo}\n"
        f"Enunciado: {ejercicio.enunciado}\n"
        f"Instrucciones: {ejercicio.instrucciones or 'Sin instrucciones adicionales.'}\n"
        f"Lenguaje: {ejercicio.lenguaje or 'No especificado'}\n"
        f"Nivel: {ejercicio.nivel}\n"
        f"Pista #{numero_pista} de 3, tipo: {tipo_pista}\n"
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
            sistema=_sistema_tutor(),
            usuario=contexto,
        )
    except TutorNoDisponible:
        contenido_pista = _pista_estatica(ejercicio, numero_pista)

    PistaTutoria.objects.create(
        sesion=sesion,
        tipo=tipo_pista,
        contenido=contenido_pista,
        numero_pista=numero_pista,
    )

    sesion.pistas_utilizadas = numero_pista
    sesion.ultima_pista_en = timezone.now()
    sesion.save(
        update_fields=["pistas_utilizadas", "ultima_pista_en", "actualizada_en"]
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
    contexto = (
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


def esta_disponible() -> bool:
    """Devuelve True si Ollama responde y el tutor IA está disponible."""
    try:
        _llamar_ollama(
            sistema="Responde solo con la palabra: ok.",
            usuario="ok",
        )
        return True
    except TutorNoDisponible:
        return False
