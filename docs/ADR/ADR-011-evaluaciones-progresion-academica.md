# ADR-011 — Evaluaciones y progresión académica (Fase 4)

**Estado:** Aprobado  
**Fecha:** 16 de noviembre de 2026  
**Decisor:** Orquestador / CodeGuard Pro Tech Lead (con plan del Subagente 1 — Arquitectura y Backend)  
**Fase:** 4 — Evaluaciones y progresión académica  
**Relacionado:** `docs/PLAN_MAESTRO_CODEGUARD.md` (sección Fase 4), `apps/roadmaps/models.py`, `apps/roadmaps/attempts.py`, `apps/tutoring/`

## Contexto

La Fase 4 requiere medir el aprendizaje de manera consistente y controlar la progresión académica por dominio demostrado. El plan del Subagente 1 (S1) analizó la fase y propuso:

- Los quizzes de módulo requieren ≥15 preguntas con objetivos/contenidos reales (authoring académico pendiente en el JSON maestro).
- Los exámenes de etapa aplican umbral de aprobación ≥70 %.
- La suspensión produce diagnóstico y ruta de repaso; sin auto-aprobación.
- La homologación usa el mismo estándar de evaluación (fuente determinista, umbral, registro).
- Las transiciones académicas se registran en auditoría.

## Decisión adoptada

1. **Los modelos de evaluación se incorporan en el módulo existente `apps/roadmaps`** (no se crea una nueva app `apps/evaluaciones`), reutilizando el patrón de entidades ya presentes:
   - `Evaluacion`/`Quiz`: quiz de módulo con configuración (umbral, tipos de pregunta, versionado).
   - `Pregunta`: pregunta con formato (selección, respuesta, interpretación de código, resolución de problemas) y vínculo a objetivo/contenido.
   - `ResultadoEvaluacion`: resultado por intento/evidencia.
2. **No se duplica** la lógica de `IntentoEjercicio` ni `ConfiguracionEvaluacion`; se reutilizan con criterios configurables para quizzes.
3. **Umbral de aprobación (≥70 %) versionado** por quiz/examen (configurable, no hardcodeado globalmente).
4. **Sin rutas de auto-cierre**: los quizzes requieren responder; los resultados solo se computan con evidencia respondida.

## Alternativas consideradas

| Alternativa | Decisión |
|---|---|
| Nueva app `apps/evaluaciones` | Descartada en esta fase por mantener el monolito modular actual (ADR-001: unificar responsabilidades por dominio). |
| Usar solo `IntentoEjercicio`/`ConfiguracionEvaluacion` | Aceptada parcialmente como base; se requieren campos de formato/umbral para quizzes. |
| Autor contenido ≥15 preguntas por módulo en JSON maestro | Requiere authoring; pendiente como requisito previo. |

## Consecuencias

- Nuevas entidades de evaluación con migración derivada (patrón validado).
- El flujo de progresión reutiliza `Progreso` (módulo/etapa completado por dominio demostrado).
- El evaluator determinista (Fase 2) sigue siendo la fuente de verdad; el tutor IA (Fase 3) explica, no decide.
- Los quizzes no requieren IA para su corrección.

## Verificación esperada (Fase 4)

- Suite de pruebas con nuevos modelos (patrón 206 OK base).
- `manage.py check`, `makemigrations --check`.

---

*ADR registrado. La implementación corresponde a la ETAPA B de la Fase 4 (ver `docs/SEGUIMIENTO_TEMPORAL_USUARIO.md`).*
