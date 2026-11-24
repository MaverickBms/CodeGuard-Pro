# Política de ramas — CodeGuard Pro

## Ramas principales

| Rama | Propósito | Contenido esperado |
|---|---|---|
| `main` | Aplicación / proyecto | Código fuente de la app (Electron + Django), scripts, tests, configuración de build. |
| `documentation` | Documentación | Documentación técnica, auditorías, matrices, guías, informes y decisiones. |
| `release/1.0.0-final` | Estabilización 1.0.0 | Rama activa de PR #17; correcciones y validación de release. No fusionar sin cierre de validación. |
| `release/1.0.0` | Base de release 1.0.0 | Base estable de la línea 1.0.0. |

## Ramas de trabajo / PR

| Rama | Estado | Nota |
|---|---|---|
| `feature/mundo-codeguard` | PR #15 abierto | No modificar desde tareas de 1.0.0. |
| `assets/mundo-codeguard-character-library` | PR #16 abierto | No modificar desde tareas de 1.0.0. |
| `content/ascenso-stage-0-learning-method` | Histórica/trabajo | Mantener hasta decidir merge/cierre. |
| `test/phase-2-electron-integration` | Histórica/pruebas | Mantener hasta decidir archivo/cierre. |

## Reglas

- No borrar ramas remotas con PR abierto o historial no evaluado.
- No hacer force-push sobre ramas compartidas sin coordinación explícita.
- `release/1.0.0-final` no se fusiona hasta completar validación.
- PR #15 y #16 no se tocan desde trabajo de 1.0.0.
- Los cambios de docs de release se reflejan en `documentation`; los cambios de app en `main`/rama de release correspondiente.
- Limpiar refs remotas obsoletas con `git remote prune origin` cuando sea seguro.
