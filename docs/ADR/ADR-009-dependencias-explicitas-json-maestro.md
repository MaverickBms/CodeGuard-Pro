# ADR-009 — Mover DEPENDENCIAS_EXPLICITAS a datos del JSON maestro

**Estado:** Propuesto  
**Fecha:** 16 de noviembre de 2026  
**Decisor:** Subagente 1 — Arquitectura y Backend  
**Fase:** Fase 1 (estabilización pre-Fase 2)  
**Relacionado:** `apps/roadmaps/services.py`, `apps/roadmaps/data/ascenso_3_1.json`, `apps/roadmaps/models.py` (`Prerrequisito`, `Etapa.esta_bloqueada_para`), `docs/ARQUITECTURA.md`

## Contexto

El módulo `apps.roadmaps.services` define `DEPENDENCIAS_EXPLICITAS`, un diccionario hardcodeado en Python que mapea números de etapa a sus prerrequisitos documentados en ASCENSO 3.1. La función `cargar_ascenso()`:

1. Carga las etapas desde el JSON maestro (`apps/roadmaps/data/ascenso_3_1.json`).
2. Borra y recrea los `Prerrequisito` de la BD usando exclusivamente `DEPENDENCIAS_EXPLICITAS`, ignorando cualquier dato de dependencias que pudiera venir en el JSON.

Esto genera tres capas potenciales de verdad para las dependencias entre etapas:

1. El JSON maestro de ASCENSO 3.1 (documento oficial).
2. `DEPENDENCIAS_EXPLICITAS` hardcodeado en `services.py`.
3. El modelo `Prerrequisito` en la base de datos.

Además, el docstring de `models.py` establece: *"este módulo no inventa etapas ni dependencias"*. El hardcode en `services.py` contradice ese principio al inyectar dependencias que no provienen del documento maestro.

## Problema

- Las dependencias entre etapas están definidas en código Python (`services.py`) en lugar del documento maestro oficial.
- `cargar_ascenso()` ignora posibles prerrequisitos declarados en el JSON maestro.
- Tres capas (JSON, hardcode Python, modelo BD) sin una única fuente de verdad clara.
- Cualquier cambio en dependencias requiere modificar código Python y hacer despliegue, en lugar de actualizar el JSON de datos.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Decisión |
|---|---|---|---|
| 1. Mantener `DEPENDENCIAS_EXPLICITAS` hardcodeado | Sin cambios inmediatos, bajo riesgo. | Contradice "no inventar dependencias"; dependencias fuera del documento maestro; tres capas de verdad. | Rechazada. |
| 2. Leer prerrequisitos del JSON maestro en `cargar_ascenso()` | Única fuente de verdad en el documento oficial; consistente con el docstring de `models.py`; cambios de dependencia sin tocar código. | Requiere actualizar `apps/roadmaps/data/ascenso_3_1.json` para incluir las dependencias (7 relaciones actuales); `cargar_ascenso()` debe parsear la nueva estructura. | **Adoptada**. |
| 3. Usar solo el modelo `Prerrequisito` y poblar desde JSON | Centraliza en BD; el JSON sería origen inicial. | Sigue requiriendo parsear el JSON; no elimina la carga inicial desde el documento maestro. | Rechazada (no resuelve la raíz: el origen debe ser el JSON). |

## Decisión adoptada

Mover `DEPENDENCIAS_EXPLICITAS` del código Python (`apps/roadmaps/services.py`) a los datos del JSON maestro (`apps/roadmaps/data/ascenso_3_1.json`), y modificar `cargar_ascenso()` para leer las dependencias desde ahí en lugar del diccionario hardcodeado.

Estructura propuesta en el JSON (por etapa):

```json
{
  "numero": 10,
  "titulo": "...",
  "prerrequisitos": [
    {
      "etapa_requerida": 9,
      "justificacion": "..."
    }
  ],
  ...
}
```

En `cargar_ascenso()`:

1. Tras crear o actualizar cada `Etapa`, leer `datos_etapa.get("prerrequisitos", [])`.
2. Borrar los `Prerrequisito` existentes del roadmap (comportamiento actual de reconstrucción).
3. Crear `Prerrequisito` para cada entrada del JSON, validando que la etapa requerida exista.
4. Eliminar `DEPENDENCIAS_EXPLICITAS` de `services.py`.

## Justificación

- Única fuente de verdad para las dependencias: el documento maestro oficial de ASCENSO 3.1.
- Consiste con el docstring de `models.py`: *"este módulo no inventa etapas ni dependencias"*.
- Cambios en dependencias requieren editar solo el JSON de datos, no código Python.
- Compatible con `AUTH_DISABLED = True`: no cambia el comportamiento funcional, solo el origen de las dependencias.
- No rompe la v1 local: las 7 relaciones existentes se migran al JSON y el modelo `Prerrequisito` se popula igual que antes.

## Consecuencias

Positivas:

- Eliminación de `DEPENDENCIAS_EXPLICITAS` (código muerto duro reducido).
- Las dependencias viajan con el documento maestro, versionadas junto al contenido.
- `Etapa.esta_bloqueada_para()` sigue funcionando sobre el modelo `Prerrequisito`, ahora poblado desde el JSON.

Negativas / costes aceptados:

- `apps/roadmaps/data/ascenso_3_1.json` debe actualizarse para incluir el campo `prerrequisitos` en las etapas 10, 15 y 31 (y cualquier otra con dependencias).
- `cargar_ascenso()` debe parsear y validar la nueva estructura (etapa requerida existente, justificación opcional).
- Cualquier prueba que asuma `DEPENDENCIAS_EXPLICITAS` en `services.py` debe actualizarse.

## Implicaciones futuras

- Permite editar dependencias entre ediciones del roadmap sin tocar código Python (solo datos).
- Facilita importar dependencias desde futuras versiones del documento maestro ASCENSO (3.2, 3.3, etc.) sin cambios de código.
- Coherente con el flujo editorial: las dependencias son parte del contenido académico, no de la lógica de aplicación.

## Verificación pendiente

- Inspeccionar `apps/roadmaps/data/ascenso_3_1.json` para confirmar la estructura actual y determinar dónde añadir `prerrequisitos`.
- Migrar las 7 relaciones de `DEPENDENCIAS_EXPLICITAS` al JSON (etapas 10→9, 15→13, 31→{3,4,7,8,21}).
- Modificar `cargar_ascenso()` para leer prerrequisitos del JSON y eliminar `DEPENDENCIAS_EXPLICITAS`.
- Ejecutar `python manage.py test` tras el cambio para confirmar 197 pruebas OK.
- Verificar que `Etapa.esta_bloqueada_para()` siga funcionando con prerrequisitos cargados desde JSON.

---
*ADR registrado sin modificar código Python. La aplicación al código requiere cambios en `apps/roadmaps/services.py` y `apps/roadmaps/data/ascenso_3_1.json`.*