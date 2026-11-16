# ADR-012 — Gamificación y economía de recompensas (Fase 5)

**Estado:** Aprobado (base técnica)  
**Fecha:** 16 de noviembre de 2026  
**Decisor:** Orquestador / CodeGuard Pro Tech Lead  
**Fase:** 5 — Gamificación y economía de recompensas  
**Relacionado:** `docs/PLAN_MAESTRO_CODEGUARD.md` (Fase 5), `apps/gamification/`

## Contexto

La Fase 5 introduce motivación y continuidad (logros, misiones, rachas, moneda virtual, inventario con rangos) sin que las recompensas sustituyan ni alteren el aprendizaje ni las aprobaciones académicas.

## Decisión adoptada

1. **Nueva app `apps/gamification`** para aislar el dominio de recompensas del dominio académico (`roadmaps`), manteniendo acoplamiento bajo y auditoría.
2. **Modelos base (incremento inicial)**:
   - `PerfilGamificacion`: saldo de moneda, racha y contadores por usuario (1:1 lógico).
   - `Logro`: definición de logro verificable (clave única, condición, recompensa).
   - `LogroObtenido`: instancia otorgada a usuario (única por logro+usuario para evitar duplicados).
   - `TransaccionMoneda`: historial auditable de ganancias/gastos (idempotencia por referencia).
   - `ItemInventario`: objeto otorgado con rareza (cobre, plata, oro, diamante, legendario, arcano) y origen.
3. **Reglas de integridad**: transacciones atómicas, constraints de unicidad, recompensas no duplicables, economía no altera progreso académico.
4. **Sin mecánicas prohibidas**: sin compra de resultados/pistas, sin apuestas, sin cajas de botín pagadas.

## Consecuencias

- Base de datos y servicios preparados para misiones, rachas y mapa narrativo (Fases 6-7).
- Requiere integración futura con eventos académicos (ej. completar módulo/lección) mediante señales o servicios explícitos.
- La UI de gamificación se implementará en incrementos posteriores.

## Verificación

- Migración inicial de `apps.gamification`, pruebas de unicidad/no duplicación y consistencia de saldo.
