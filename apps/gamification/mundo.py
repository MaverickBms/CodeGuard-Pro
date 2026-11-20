"""Reglas del Mundo CodeGuard: región piloto, misiones e interacciones.

El mundo es una capa de gamificación motivacional. No concede aprobaciones
académicas ni modifica resultados: la fuente de verdad del progreso sigue siendo
``apps.roadmaps``. Las recompensas son cosméticas o monedas internas.
"""
from __future__ import annotations

from datetime import datetime, timezone

from django.core.exceptions import ValidationError
from django.db import transaction
from django.urls import reverse

from .models import EstadoMundo, ItemInventario
from .services import acreditar_monedas

REGIONES = {
    "aldea-metodo": {
        "id": "aldea-metodo",
        "nombre": "Aldea del Método",
        "descripcion": (
            "Una aldea tranquila donde se aprende a estudiar, investigar y "
            "depurar. Sus habitantes acompañan la primera etapa de ASCENSO."
        ),
        "ancho": 30,
        "alto": 20,
        "spawn": {"x": 15, "y": 12},
        "etapa": 0,
    },
    "biblioteca-aldear": {
        "id": "biblioteca-aldear",
        "nombre": "Biblioteca de la Aldea",
        "descripcion": (
            "Un interior tranquilo con documentación, tutoriales y foros. "
            "El Bibliotecario Byte y Nexo esperan aquí."
        ),
        "ancho": 30,
        "alto": 20,
        "spawn": {"x": 15, "y": 17},
        "etapa": 0,
    },
}

OBJETOS = {
    "insignia-metodo": {
        "nombre": "Insignia del Método",
        "rareza": "plata",
        "descripcion": "Reconocimiento por completar el primer circuito de la aldea.",
    },
    "marca-bibliotecario": {
        "nombre": "Marca del Bibliotecario",
        "rareza": "cobre",
        "descripcion": "Sello de quien consulta las fuentes antes de concluir.",
    },
    "chip-depurador": {
        "nombre": "Chip depurador",
        "rareza": "oro",
        "descripcion": "Símbolo de haber encontrado errores con evidencia.",
    },
    "nucleo-logico": {
        "nombre": "Núcleo lógico",
        "rareza": "oro",
        "descripcion": "Símbolo de haber resuelto un problema con condiciones y evidencia.",
    },
    "brujula-aldear": {
        "nombre": "Brújula de la aldea",
        "rareza": "cobre",
        "descripcion": "Objeto narrativo que orienta la exploración.",
    },
}

INTERACCIONES = {
    "ada": {
        "bandera": "hablado-ada",
        "nombre": "Mentora Ada",
        "texto": (
            "Ada: «Estudiar no es acumular páginas leídas. Antes de avanzar, "
            "comprueba qué puedes explicar sin mirar. La terminal de la plaza "
            "guarda una práctica de recuperación; vuelve cuando la hayas leído.»"
        ),
    },
    "terminal": {
        "bandera": "usado-terminal",
        "nombre": "Terminal de práctica",
        "texto": (
            "La terminal muestra una pregunta: «¿Qué diferencia hay entre "
            "reconocer una respuesta y recuperarla?». La respondes en voz alta "
            "y la pantalla registra tu intento."
        ),
    },
    "byte": {
        "bandera": "hablado-byte",
        "nombre": "Bibliotecario Byte",
        "texto": (
            "Byte: «Toda afirmación necesita una fuente. Revisa las tres "
            "estanterías de la biblioteca y anota qué puedes verificar.»"
        ),
    },
    "estanteria-1": {
        "bandera": "estanteria-1",
        "nombre": "Estantería de documentación",
        "texto": "Encuentras documentación oficial del lenguaje. Tiene fecha y versión.",
    },
    "estanteria-2": {
        "bandera": "estanteria-2",
        "nombre": "Estantería de tutoriales",
        "texto": "Un tutorial explica una versión anterior. Debes comprobar su vigencia.",
    },
    "estanteria-3": {
        "bandera": "estanteria-3",
        "nombre": "Estantería de foros",
        "texto": "Una respuesta de foro puede orientar, pero no sustituye una especificación.",
    },
    "nexo": {
        "bandera": "hablado-nexo",
        "nombre": "Nexo, mentor de lógica",
        "texto": (
            "Nexo: «Una condición mal formulada puede parecer correcta. "
            "Tu reto es razonar el caso, no memorizar una respuesta.»"
        ),
    },
    "guardian": {
        "bandera": "hablado-guardian",
        "nombre": "Guardián del Error",
        "texto": (
            "Guardián: «Todo programa puede fallar. Tu reto es encontrar el "
            "error con evidencia, no adivinarlo. ¿Aceptas el desafío?»"
        ),
    },
    "cartel": {
        "bandera": "leido-cartel",
        "nombre": "Cartel de bienvenida",
        "texto": "«Mundo CodeGuard — Aldea del Método. Aprender también es explorar.»",
    },
    "cofre": {
        "bandera": "abierto-cofre",
        "nombre": "Cofre de la aldea",
        "texto": "Dentro encuentras una brújula narrativa. No otorga ventajas académicas.",
    },
}

# Respuestas privadas del minijuego. Nunca se serializan al cliente.
_RESPUESTAS_DEPURACION = {"q1": 1, "q2": 2, "q3": 0}

# Región mínima exigida para cada interacción. Evita activar banderas de la
# biblioteca desde la aldea (y viceversa) con una petición manipulada.
REGION_POR_INTERACCION = {
    "ada": "aldea-metodo",
    "terminal": "aldea-metodo",
    "guardian": "aldea-metodo",
    "cartel": "aldea-metodo",
    "cofre": "aldea-metodo",
    "byte": "biblioteca-aldear",
    "estanteria-1": "biblioteca-aldear",
    "estanteria-2": "biblioteca-aldear",
    "estanteria-3": "biblioteca-aldear",
    "nexo": "biblioteca-aldear",
}
_PREGUNTAS_DEPURACION = [
    {
        "id": "q1",
        "pregunta": "La prueba falla solo al ejecutarse en el servidor. ¿Qué haces primero?",
        "opciones": [
            "Cambiar el código al azar hasta que pase.",
            "Reproducir el fallo y leer el error con su traza y contexto.",
            "Ignorar la prueba y desplegar.",
        ],
    },
    {
        "id": "q2",
        "pregunta": "¿Cuál es una evidencia útil para localizar un error?",
        "opciones": [
            "Una captura sin datos.",
            "El mensaje de error, la entrada que lo provoca y los pasos reproducibles.",
            "La opinión de alguien que no ejecutó el caso.",
        ],
    },
    {
        "id": "q3",
        "pregunta": "Después de corregir el fallo, ¿qué corresponde?",
        "opciones": [
            "Añadir o ajustar una prueba de regresión y volver a ejecutar la suite.",
            "Borrar la prueba que fallaba.",
            "Declarar terminado sin comprobar nada más.",
        ],
    },
]

_RESPUESTAS_LOGICA = {"q1": 1, "q2": 0, "q3": 2}
_RESPUESTAS_POR_MISION = {
    "desafio-depuracion": _RESPUESTAS_DEPURACION,
    "logica-principal": _RESPUESTAS_LOGICA,
}
_PREGUNTAS_LOGICA = [
    {
        "id": "q1",
        "pregunta": "Un programa debe aceptar edad >= 18 y país == 'ES'. ¿Qué condición es correcta?",
        "opciones": [
            "edad >= 18 OR pais == 'ES'",
            "edad >= 18 AND pais == 'ES'",
            "edad < 18 AND pais == 'ES'",
        ],
    },
    {
        "id": "q2",
        "pregunta": "Si una lista está vacía, ¿qué comprobación evita acceder al primer elemento?",
        "opciones": [
            "Comprobar que la longitud es mayor que cero antes de acceder.",
            "Acceder siempre y confiar en que no falle.",
            "Ordenar la lista y acceder al último.",
        ],
    },
    {
        "id": "q3",
        "pregunta": "¿Qué describe mejor una prueba de regresión?",
        "opciones": [
            "Una prueba que solo comprueba la velocidad.",
            "Una prueba que se elimina cuando falla.",
            "Una prueba que evita que un fallo corregido vuelva a aparecer.",
        ],
    },
]

MISIONES = {
    "metodo-principal": {
        "nombre": "El método de Ada",
        "tipo": "principal",
        "descripcion": "Habla con Ada, practica en la terminal y vuelve con ella.",
        "requisitos": ["hablado-ada", "usado-terminal"],
        "recompensa": {"objeto": "insignia-metodo", "xp": 25, "monedas": 10},
    },
    "biblioteca-secundaria": {
        "nombre": "Fuentes con criterio",
        "tipo": "secundaria",
        "descripcion": "Revisa las tres estanterías y vuelve con Byte.",
        "requisitos": ["hablado-byte", "estanteria-1", "estanteria-2", "estanteria-3"],
        "recompensa": {"objeto": "marca-bibliotecario", "xp": 15, "monedas": 5},
    },
    "logica-principal": {
        "nombre": "Condiciones del Nexo",
        "tipo": "minijuego",
        "descripcion": "Resuelve el reto de lógica de Nexo en la biblioteca.",
        "requisitos": ["hablado-nexo"],
        "recompensa": {"objeto": "nucleo-logico", "xp": 25, "monedas": 8},
        "minijuego": {"preguntas": _PREGUNTAS_LOGICA},
    },
    "desafio-depuracion": {
        "nombre": "El error en la terminal",
        "tipo": "minijuego",
        "descripcion": "Resuelve el reto de depuración del Guardián del Error.",
        "requisitos": ["hablado-guardian"],
        "recompensa": {"objeto": "chip-depurador", "xp": 30, "monedas": 10},
        "minijuego": {"preguntas": _PREGUNTAS_DEPURACION},
    },
}


def _region(region_id: str) -> dict:
    try:
        return REGIONES[region_id]
    except KeyError as exc:
        raise ValidationError("La región del mundo no es válida.") from exc


def obtener_estado(usuario) -> EstadoMundo:
    if usuario is None:
        raise ValidationError("Se requiere un propietario local para jugar.")
    estado, _ = EstadoMundo.objects.get_or_create(usuario=usuario)
    return estado


def _estado_mision(estado: EstadoMundo, mision_id: str) -> str:
    definicion = MISIONES[mision_id]
    registro = (estado.misiones or {}).get(mision_id) or {}
    if registro.get("estado") == "completada":
        return "completada"
    banderas = estado.banderas or {}
    requisitos = definicion.get("requisitos", [])
    if requisitos and all(banderas.get(req) for req in requisitos):
        return "lista"
    if any(banderas.get(req) for req in requisitos):
        return "en_progreso"
    return "disponible"


def serializar_estado(estado: EstadoMundo) -> dict:
    region = _region(estado.region)
    misiones = []
    for mision_id, definicion in MISIONES.items():
        publica = {
            "id": mision_id,
            "nombre": definicion["nombre"],
            "tipo": definicion["tipo"],
            "descripcion": definicion["descripcion"],
            "requisitos": definicion.get("requisitos", []),
            "recompensa": definicion.get("recompensa", {}),
            "estado": _estado_mision(estado, mision_id),
        }
        if "minijuego" in definicion:
            publica["minijuego"] = definicion["minijuego"]
        misiones.append(publica)

    inventario = []
    for objeto_id in estado.inventario or []:
        objeto = OBJETOS.get(objeto_id)
        if objeto:
            inventario.append({"id": objeto_id, **objeto})

    nivel = 1 + estado.experiencia // 50
    return {
        "region": region,
        "posicion": {"x": estado.x, "y": estado.y, "direccion": estado.direccion},
        "misiones": misiones,
        "banderas": estado.banderas or {},
        "inventario": inventario,
        "experiencia": estado.experiencia,
        "nivel": nivel,
        "xp_siguiente": nivel * 50,
        "tiempo_jugado": estado.tiempo_jugado,
        "audio_silenciado": estado.audio_silenciado,
    }


def contexto_academico(usuario=None) -> dict | None:
    """Resumen de la etapa 0 real, sin inventar relaciones curriculares."""
    from apps.roadmaps.services import etapas_completadas, roadmap_activo

    roadmap = roadmap_activo()
    if roadmap is None:
        return None
    etapa = roadmap.etapas.filter(numero=0).first()
    if etapa is None:
        return None
    completadas = etapas_completadas(usuario, roadmap) if usuario is not None else set()
    return {
        "etapa_numero": etapa.numero,
        "etapa_titulo": etapa.titulo,
        "url": reverse("roadmaps:detalle", args=[etapa.numero]),
        "completada": etapa.numero in completadas,
    }


def guardar_posicion(
    estado: EstadoMundo,
    *,
    region: str,
    x: int,
    y: int,
    direccion: str,
    tiempo_jugado: int,
    audio_silenciado: bool,
) -> EstadoMundo:
    region_def = _region(region)
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValidationError("La posición debe ser entera.")
    if not 0 <= x < region_def["ancho"] or not 0 <= y < region_def["alto"]:
        raise ValidationError("La posición está fuera del mapa.")
    if direccion not in {"up", "down", "left", "right"}:
        raise ValidationError("La dirección no es válida.")
    if not isinstance(tiempo_jugado, int) or not 0 <= tiempo_jugado <= 10_000_000:
        raise ValidationError("El tiempo jugado no es válido.")
    if not isinstance(audio_silenciado, bool):
        raise ValidationError("La preferencia de audio no es válida.")

    estado.region = region
    estado.x = x
    estado.y = y
    estado.direccion = direccion
    estado.tiempo_jugado = tiempo_jugado
    estado.audio_silenciado = audio_silenciado
    estado.save(
        update_fields=[
            "region", "x", "y", "direccion", "tiempo_jugado",
            "audio_silenciado", "actualizado_en",
        ]
    )
    return estado


@transaction.atomic
def interactuar(estado: EstadoMundo, objeto: str) -> dict:
    interaccion = INTERACCIONES.get(objeto)
    if interaccion is None:
        raise ValidationError("El objeto interactivo no existe.")
    region_esperada = REGION_POR_INTERACCION.get(objeto)
    if region_esperada and estado.region != region_esperada:
        raise ValidationError("No estás en la región de ese objeto interactivo.")
    banderas = dict(estado.banderas or {})
    banderas[interaccion["bandera"]] = True
    estado.banderas = banderas
    estado.save(update_fields=["banderas", "actualizado_en"])
    return {
        "objeto": objeto,
        "nombre": interaccion["nombre"],
        "texto": interaccion["texto"],
        "nueva": True,
    }


def _validar_respuestas(mision_id: str, respuestas) -> int:
    esperadas = _RESPUESTAS_POR_MISION.get(mision_id)
    if esperadas is None:
        raise ValidationError("La misión no tiene un minijuego validable.")
    if not isinstance(respuestas, dict):
        raise ValidationError("Las respuestas del minijuego no son válidas.")
    if set(respuestas) != set(esperadas):
        raise ValidationError("Faltan respuestas del minijuego.")
    aciertos = 0
    for clave, esperada in esperadas.items():
        valor = respuestas.get(clave)
        if not isinstance(valor, int):
            raise ValidationError("Cada respuesta debe ser una opción entera.")
        if valor == esperada:
            aciertos += 1
    if aciertos < len(esperadas):
        raise ValidationError("El desafío requiere acertar todas las preguntas.")
    return aciertos


@transaction.atomic
def completar_mision(estado: EstadoMundo, mision_id: str, respuestas=None) -> tuple[EstadoMundo, bool, dict]:
    definicion = MISIONES.get(mision_id)
    if definicion is None:
        raise ValidationError("La misión no existe.")

    # Bloquea la fila para que dos solicitudes concurrentes no dupliquen XP,
    # inventario ni recompensas.
    estado = EstadoMundo.objects.select_for_update().get(pk=estado.pk)
    misiones = dict(estado.misiones or {})
    if (misiones.get(mision_id) or {}).get("estado") == "completada":
        return estado, False, {"mensaje": "La misión ya estaba completada."}

    if _estado_mision(estado, mision_id) != "lista":
        raise ValidationError("La misión todavía no está disponible o le faltan pasos.")

    puntuacion = None
    if "minijuego" in definicion:
        puntuacion = _validar_respuestas(mision_id, respuestas)

    recompensa = definicion.get("recompensa", {})
    inventario = list(estado.inventario or [])
    objeto_id = recompensa.get("objeto")
    if objeto_id and objeto_id not in inventario and objeto_id in OBJETOS:
        inventario.append(objeto_id)
        ItemInventario.objects.get_or_create(
            usuario=estado.usuario,
            origen=f"mundo:{mision_id}",
            defaults={
                "nombre": OBJETOS[objeto_id]["nombre"],
                "rareza": OBJETOS[objeto_id]["rareza"],
                "descripcion": OBJETOS[objeto_id]["descripcion"],
            },
        )

    misiones[mision_id] = {
        "estado": "completada",
        "completada_en": datetime.now(timezone.utc).isoformat(),
        "puntuacion": puntuacion,
    }
    estado.misiones = misiones
    estado.inventario = inventario
    estado.experiencia += int(recompensa.get("xp", 0))
    estado.save(
        update_fields=["misiones", "inventario", "experiencia", "actualizado_en"]
    )

    monedas = int(recompensa.get("monedas", 0))
    if monedas > 0:
        acreditar_monedas(
            estado.usuario,
            monedas,
            concepto=f"Mundo CodeGuard: {definicion['nombre']}",
            referencia=f"mundo:mision:{mision_id}:usuario:{estado.usuario_id}",
        )

    return estado, True, {"mensaje": "Misión completada.", "xp": int(recompensa.get("xp", 0))}
