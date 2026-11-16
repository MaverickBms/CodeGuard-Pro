# ADR-008 — Combinar consultas de progreso

**Estado:** Propuesto  
**Fecha:** 16 de noviembre de 2026  
**Decisor:** Subagente 1 — Arquitectura y Backend  
**Fase:** Fase 1 (estabilización pre-Fase 2)  
**Relacionado:** `apps/roadmaps/services.py`, `apps/roadmaps/views.py`, `docs/ARQUITECTURA.md`

## Contexto

El módulo `apps.roadmaps.services` expone tres funciones de consulta sobre el modelo `Progreso`:

- `etapas_completadas(usuario, roadmap)`: consulta etapas con `estado="completado"` y null en `modulo`/`leccion`/`actividad`.
- `mapa_progreso_etapas(usuario, roadmap)`: consulta progreso a nivel de etapa indexado por `etapa_id`.
- `mapa_progreso_lecciones(usuario, etapa)`: consulta progreso de lecciones indexado por `leccion_id`.

Cada función lanza una consulta separada a la tabla `Progreso`. En `views.lista` y `views.detalle` se invocan varias de estas funciones por petición, generando múltiples rondas a SQLite para datos que podrían obtenerse en una sola consulta.

## Problema

- Hasta 3 consultas separadas a `Progreso` por vista (etapas completadas, progreso por etapa, progreso por lección).
- Cada consulta implica sobrecarga de ORM de Django, construcción de QuerySet y viaje de red/IO al fichero SQLite.
- En el panel de listado (`views.lista`) se cargan las 33 etapas y se consulta progreso para cada una; multiplicar consultas afecta al tiempo de respuesta, aunque el volumen de datos sea pequeño hoy.
- La lógica de filtrado por `usuario`, `etapa__roadmap`, `modulo__isnull`, `leccion__isnull`, `actividad__isnull` se repite en las tres funciones.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Decisión |
|---|---|---|---|
| 1. Mantener las 3 consultas separadas | Código simple y claro por función. | Múltiples rondas a SQLite, lógica de filtrado duplicada. | Rechazada para estabilización. |
| 2. Una sola consulta con `prefetch_related` / `select_related` y indexar en Python | Una ronda a la base de datos, menos sobrecarga de ORM, filtrado centralizado. | Lógica ligeramente más compleja en Python (indexar resultados por `etapa_id` / `leccion_id`). | **Adoptada**. |
| 3. Consultas agregadas con `annotate` / `aggregate` | Minimiza filas devueltas. | Pierde la capacidad de devolver objetos `Progreso` individuales por clave; menos flexible para vistas. | Rechazada (las vistas necesitan objetos `Progreso`). |

## Decisión adoptada

Consolidar la lectura de progreso en una única consulta que recupere todas las filas relevantes de `Progreso` para un usuario y roadmap (o etapa), usando `select_related("etapa")`, `prefetch_related` cuando sea necesario, e indexar los resultados en memoria por `etapa_id` y `leccion_id`.

Concretamente:

- `etapas_completadas(usuario, roadmap)`: una consulta filtrando `estado="completado"` y null en relaciones hijas, devolviendo `set` de números de etapa.
- `mapa_progreso_etapas(usuario, roadmap)`: una consulta con `select_related("etapa")`, indexando por `etapa_id`.
- `mapa_progreso_lecciones(usuario, etapa)`: una consulta con `select_related("leccion")`, indexando por `leccion_id`.

O, alternativamente, una única función interna `_obtener_progresos(usuario, roadmap)` que devuelva todo y las tres funciones públicas se construyan sobre ella en memoria.

## Justificación

- Reduce el número de rondas a SQLite, relevante en disco local y aún más en futuros escenarios de escritura concurrente (WAL activado, ADR-005).
- Centraliza el filtrado común (`usuario`, `etapa__roadmap`, null en relaciones hijas) en un solo punto.
- Compatible con `AUTH_DISABLED = True`: no cambia el comportamiento funcional, solo la forma de obtener los datos.
- No rompe la v1 local: las firmas públicas de las funciones se mantienen; solo cambia la implementación interna.

## Consecuencias

Positivas:

- Menos consultas a la base de datos por vista de panel/detalle.
- Lógica de filtrado centralizada, menor riesgo de inconsistencia entre las tres funciones.
- Mejor tiempo de respuesta en el panel de listado (33 etapas).

Negativas / costes aceptados:

- La implementación interna es ligeramente más compleja (indexación en Python).
- Las pruebas unitarias que mockeen cada consulta por separado pueden necesitar ajuste.

## Implicaciones futuras

- Prepara la base para multiusuario: el filtrado por usuario es más crítico y centralizarlo evita omisiones.
- Facilita añadir `prefetch_related("etapa__modulo__lecciones")` si se necesitan progresos anidados en una sola consulta.
- Compatible con una posible capa de caché de progreso por usuario.

## Verificación pendiente

- Ejecutar `python manage.py test` tras el cambio para confirmar 197 pruebas OK.
- Verificar que `views.lista` y `views.detalle` siguen recibiendo `completadas`, `progreso_actual` y `progresos_lecciones` correctamente.
- Comprobar que el comportamiento de `etapas_completadas`, `mapa_progreso_etapas` y `mapa_progreso_lecciones` es idéntico antes y después (mismas claves, mismos objetos `Progreso`).

---
*ADR registrado sin modificar código Python. La aplicación al código requiere cambios en `apps/roadmaps/services.py`.*