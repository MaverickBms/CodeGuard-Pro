# ADR-007 — Extraer servicio de resolución de contenido activo

**Estado:** Propuesto  
**Fecha:** 16 de noviembre de 2026  
**Decisor:** Subagente 1 — Arquitectura y Backend  
**Fase:** Fase 1 (estabilización pre-Fase 2)  
**Relacionado:** `apps/roadmaps/services.py`, `apps/roadmaps/views.py`, `apps/roadmaps/attempts.py`, `docs/ARQUITECTURA.md`

## Contexto

CodeGuard Pro soporta dos orígenes de contenido didáctico para una lección:

1. **Paquete de conocimiento instalado activo** (`ContenidoLeccionPaquete` vinculado a `PaqueteConocimientoInstalado.estado = "activo"`): snapshot académico inmutable instalado desde un paquete firmado y verificado.
2. **Puntero editorial activo** (`ContenidoLeccionActivo` vinculado a `VersionContenidoLeccion.estado = "publicada"`): versión editorial publicada localmente mediante el flujo editorial.

La lógica para decidir qué origen usar y para construir los objetos de contenido, ejemplos y ejercicios está duplicada en tres sitios:

- `apps/roadmaps/views.py`, función `leccion_detalle` (líneas ~329–406).
- `apps/roadmaps/attempts.py`, función `_completar_leccion_si_corresponde` (líneas ~106–137).
- `apps/roadmaps/attempts.py`, función `registrar_intento_ejercicio` (líneas ~211–274).

Cada sitio reimplementa la bifurcación paquete/puntero, la construcción de `SimpleNamespace` para ejemplos y ejercicios, y el mapeo de UUID de ejercicios.

## Problema

- Duplicación de lógica de resolución de contenido activo en tres módulos.
- Riesgo de inconsistencia: un cambio en los campos del snapshot (por ejemplo, añadir un campo a ejemplos) debe reflejarse en los tres sitios.
- Dificulta testear la regla de resolución de forma aislada (requiere invocar vistas o registrar intentos).
- Acopla las vistas y los casos de uso de intentos a los detalles de almacenamiento de contenido.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Decisión |
|---|---|---|---|
| 1. Mantener la duplicación | Sin cambios inmediatos. | Duplicación persistente, riesgo de inconsistencia, difícil de testear. | Rechazada. |
| 2. Extraer función `obtener_contenido_activo(leccion, canal)` en `apps/roadmaps/services.py` | Única fuente de verdad, reutilizable desde vistas, CLI, comandos o API futura, testeable de forma aislada. | Requiere refactorizar los tres sitios de llamada para usar la nueva función. | **Adoptada**. |
| 3. Mover la lógica a un método del modelo `Leccion` | Encapsula en el dominio de la lección. | Mezcla responsabilidades de modelo con lógica de aplicación (canal, paquete vs puntero); el modelo no debería conocer `EstadoSincronizacion`. | Rechazada. |

## Decisión adoptada

Crear una función `obtener_contenido_activo(leccion, canal)` en `apps/roadmaps/services.py` que:

- Reciba una instancia `Leccion` y el canal de conocimiento (`settings.CODEGUARD_KNOWLEDGE_CHANNEL` por defecto).
- Consulte `EstadoSincronizacion` para el canal y determine si hay `PaqueteConocimientoInstalado.estado = "activo"`.
- Si hay paquete activo: devuelva el snapshot, ejemplos y ejercicios de `ContenidoLeccionPaquete`.
- Si no hay paquete activo: devuelva el snapshot, ejemplos y ejercicios de `ContenidoLeccionActivo` (puntero editorial publicado).
- Devuelva una estructura consistente (diccionario o namedtuple) con: `contenido`, `ejemplos`, `ejercicios`, `origen` ("paquete" | "editorial" | "ninguno"), y metadatos de versión.

Las vistas y `attempts.py` se actualizan para llamar a esta función en lugar de reimplementar la bifurcación.

## Justificación

- Centraliza la regla de negocio "¿de qué origen se sirve el contenido de esta lección?" en un solo servicio.
- Elimina la duplicación lógica identificada en la revisión de arquitectura.
- Hace testeable la resolución de contenido de forma unitaria (sin necesidad de renderizar vistas ni registrar intentos).
- Compatible con `AUTH_DISABLED = True`: no cambia el comportamiento funcional, solo el origen del código.
- No rompe la v1 local: el comportamiento de resolución (paquete prioritario sobre editorial) se mantiene.

## Consecuencias

Positivas:

- Única fuente de verdad para la resolución de contenido activo.
- Menos código duplicado (se eliminan ~80 líneas de lógica repetida).
- Más fácil de mantener y extender (por ejemplo, añadir un tercer origen de contenido).

Negativas / costes aceptados:

- Requiere refactorizar `views.leccion_detalle`, `attempts._completar_leccion_si_corresponde` y `attempts.registrar_intento_ejercicio`.
- Los tres sitios deben adaptarse a la interfaz de retorno de la nueva función.

## Implicaciones futuras

- Base natural para exponer una API de contenido (REST o interna) sin duplicar la resolución.
- Útil para multiusuario: la función puede extenderse para resolver contenido por usuario/canal sin tocar vistas.
- Facilita añadir caché de lectura del contenido activo por lección.

## Verificación pendiente

- Diseñar la firma y el tipo de retorno de `obtener_contenido_activo` antes de implementar.
- Refactorizar los tres sitios de llamada y ejecutar `python manage.py test` (197 pruebas OK).
- Confirmar que el comportamiento de `leccion_detalle`, `_completar_leccion_si_corresponde` y `registrar_intento_ejercicio` es idéntico antes y después.

---
*ADR registrado sin modificar código Python. La aplicación al código requiere cambios en `apps/roadmaps/services.py`, `apps/roadmaps/views.py` y `apps/roadmaps/attempts.py`.*