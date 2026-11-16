# ADR-006 — Unificar contadores del roadmap

**Estado:** Propuesto  
**Fecha:** 16 de noviembre de 2026  
**Decisor:** Subagente 1 — Arquitectura y Backend  
**Fase:** Fase 1 (estabilización pre-Fase 2)  
**Relacionado:** `apps/roadmaps/models.py`, `apps/roadmaps/services.py`, `docs/ARQUITECTURA.md`

## Contexto

El módulo `apps.roadmaps` define dos fuentes de verdad para las mismas estadísticas del roadmap:

1. Propiedades del modelo `Roadmap` en `apps/roadmaps/models.py`:
   - `total_etapas`, `total_modulos`, `total_lecciones`, `total_proyectos`.

2. Función `resumen_roadmap()` en `apps/roadmaps/services.py`, que consulta exactamente los mismos contadores mediante cuatro consultas separadas a `Etapa`, `Modulo` y `Leccion`.

Ambas implementaciones devuelven resultados equivalentes pero están dispersas en dos módulos, lo que genera duplicación lógica y riesgo de inconsistencia si se modifica una y no la otra.

## Problema

- Duplicación de lógica de contadores entre `models.py` y `services.py`.
- Dos puntos de modificación para la misma regla de negocio (¿cuántas etapas/módulos/lecciones/proyectos tiene un roadmap?).
- `resumen_roadmap()` lanza 4 consultas separadas que podrían evitarse si se reutilizan las propiedades del modelo o una única consulta agregada.
- Las vistas (`apps/roadmaps/views.py`) usan `resumen_roadmap()` para el panel de listado, acoplando la presentación a una función de servicio duplicada.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Decisión |
|---|---|---|---|
| 1. Mantener ambas implementaciones | Sin cambios inmediatos, bajo riesgo a corto plazo. | Duplicación persistente, riesgo de inconsistencia futura. | Rechazada. |
| 2. Eliminar `resumen_roadmap()` y usar propiedades del modelo `Roadmap` | Única fuente de verdad en el modelo, menos código, las propiedades ya existen y están testeadas. | Las vistas que llaman a `resumen_roadmap()` deben actualizarse para usar las propiedades o un nuevo agregado. | **Adoptada**. |
| 3. Eliminar propiedades del modelo y centralizar todo en `resumen_roadmap()` | Centraliza en services.py (capa de lógica de negocio). | Rompe el encapsulamiento del modelo; las propiedades son parte de la API pública de `Roadmap` y pueden usarse desde otros módulos. | Rechazada. |

## Decisión adoptada

Eliminar `resumen_roadmap()` de `apps/roadmaps/services.py` y reutilizar las propiedades del modelo `Roadmap`:

- `roadmap.total_etapas`
- `roadmap.total_modulos`
- `roadmap.total_lecciones`
- `roadmap.total_proyectos`
- `roadmap.etapas.values("prioridad").annotate(total=Count("id"))` (para `por_prioridad`)

Las vistas (`apps/roadmaps/views.lista`) se actualizan para consumir directamente las propiedades del modelo en lugar de llamar a `resumen_roadmap()`.

## Justificación

- El modelo `Roadmap` es el lugar natural para definir estadísticas propias del roadmap (encapsulamiento de dominio).
- Elimina la duplicación lógica identificada en la revisión de arquitectura.
- Reduce el número de consultas si se combina con `prefetch_related` en la vista.
- Compatible con `AUTH_DISABLED = True`: no cambia el comportamiento funcional, solo el origen de los datos contados.
- No rompe la v1 local: las propiedades del modelo ya existen y se mantienen.

## Consecuencias

Positivas:

- Única fuente de verdad para contadores del roadmap.
- Menos código mantenido (se elimina una función completa).
- Las pruebas existentes de `services.py` que cubran `resumen_roadmap()` pueden redirigirse a las propiedades del modelo.

Negativas / costes aceptados:

- `apps/roadmaps/views.py` y posiblemente pruebas deben actualizarse para dejar de importar/usar `resumen_roadmap()`.
- Cualquier código externo (scripts, shell de Django) que importe `resumen_roadmap()` dejará de funcionar; debe buscarse en el repositorio antes de eliminar.

## Implicaciones futuras

- Facilita añadir una capa de caché de lectura para los contadores del panel en un solo lugar (el modelo).
- Prepara la extracción de `Roadmap` como servicio independiente: la lógica de contadores viaja con el modelo, no con una función de servicio suelta.
- Si en el futuro se necesitan contadores más complejos (por usuario, por canal), el modelo es el punto de extensión adecuado.

## Verificación pendiente

- Buscar todas las referencias a `resumen_roadmap` en el repositorio antes de eliminar.
- Ejecutar `python manage.py test` tras el cambio para confirmar 197 pruebas OK.
- Confirmar que `views.lista` sigue renderizando el resumen correctamente (etapas, módulos, lecciones, proyectos, por prioridad).

---
*ADR registrado sin modificar código Python. La aplicación al código requiere cambios en `apps/roadmaps/services.py` y `apps/roadmaps/views.py`.*