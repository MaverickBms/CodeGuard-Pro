# Informe de aceptación — Fase 3: Tutor inteligente local

**Producto:** CodeGuard Pro  
**Fase:** 3 — Tutor inteligente local  
**Estado del informe:** Borrador  
**Elaborado por:** Subagente 4 (Documentación, Integración y QA)  
**Fecha:** 16 de noviembre de 2026  
**Rama de referencia:** `chore/stabilizacion-pre-fase-2`  
**Commit de referencia:** `606e501` (ADR-010 — Tutor IA local)  

---

## 1. Resumen ejecutivo

La Fase 3 (Tutor inteligente local) está **en progreso — parcialmente implementada**, según la decisión técnica **ADR-010** (aprobada el 16-11-2026 y registrada en `docs/ADR/ADR-010-tutor-ia-local.md`).

Se implementó la app Django `apps/tutoring` con migración 0001, servicios de tutoría (comunicación con Ollama local, degradación a reglas estáticas, límite de 3 pistas por ejercicio) y API JSON local `/tutoria/*` (estado, iniciar sesión de tutoría, entregar pista, analizar intento).

La suite de pruebas del tutor cuenta con **9 pruebas** (`apps.tutoring.tests.test_tutoria`); la línea base total del proyecto asciende a **206 pruebas OK** (197 del núcleo + 9 de la app tutoring).

El presente informe se mantiene en **borrador**: la Fase 3 **no está aceptada formalmente** hasta completar la validación con Ollama en ejecución real y verificar los criterios de aceptación restantes.

---

## 2. Alcance verificado

| Funcionalidad | Estado | Evidencia |
|---|---|---|
| Decisión ADR-010 (tutor IA local vía Ollama) | ✅ Aprobada | `docs/ADR/ADR-010-tutor-ia-local.md` |
| App `apps/tutoring` (modelos, servicios, vistas, URLs) | ✅ Implementada | `apps/tutoring/` + migración 0001 |
| API `/tutoria/estado/` | ✅ Implementada | `apps/tutoring/urls.py` → `views.tutoria_estado` |
| API `/tutoria/ejercicio/<id>/iniciar/` | ✅ Implementada | `views.tutoria_iniciar` |
| API `/tutoria/ejercicio/<id>/pista/` | ✅ Implementada | `views.tutoria_pista` |
| API `/tutoria/ejercicio/<id>/analizar/` | ✅ Implementada | `views.tutoria_analizar` |
| Límite de 3 pistas por ejercicio | ✅ Implementado | `services.entregar_pista` + `SesionTutoria` |
| Degradación a reglas estáticas sin Ollama | ✅ Implementado (probado en tests) | `test_entrega_pista_cae_a_reglas_estaticas_sin_ollama` |
| Tutor no ejecuta código del estudiante | ✅ Por diseño | `services._llamar_ollama` solo analiza texto |
| Evaluación determinista como fuente de verdad | ✅ Por diseño | `services.analizar_intento` no decide la aprobación |

---

## 3. Criterios de aceptación

| ID | Criterio | Resultado | Observación |
|----|----------|-----------|-------------|
| C-1 | El tutor explica errores de sintaxis, lógica y enfoque | ⏳ Pendiente de verificación | Implementación presentada; falta validar con modelo real |
| C-2 | Respeta el límite de tres pistas | ✅ Verificado | Cubierto por `apps/tutoring` (9 pruebas) |
| C-3 | No entrega directamente la solución | ⚠️ Parcial (por diseño; verificación en runtime pendiente) | Restricciones en prompt del sistema |
| C-4 | Puede funcionar sin conexión si el modelo local está disponible | ⚠️ Parcial (degradación probada en tests; runtime con Ollama pendiente) | Modo sin IA operativo |
| C-5 | Sus recomendaciones no alteran directamente las calificaciones ni la progresión | ✅ Por diseño | El validador determinista mantiene la fuente de verdad |

> **Nota:** los criterios marcados como pendientes o parciales **no deben** considerarse cumplidos hasta la validación requerida.

---

## 4. Pruebas ejecutadas

| Suite / Prueba | Casos | Pasan | Fallan | Entorno | Fecha |
|---|---:|---:|---:|---|---|
| `apps.tutoring` (Fase 3) | 9 | ✅ | 0 | development | 16-11-2026 |
| `apps.core` + `apps.accounts` + `apps.audit` + `apps.roadmaps` | 197 | ✅ | 0 | development | 16-11-2026 |
| **Total** | **206** | **206** | **0** | development | 16-11-2026 |

Comando de ejecución:

```bash
.venv/bin/python manage.py test apps.tutoring apps.core apps.accounts apps.audit apps.roadmaps --settings=config.settings.development
```

**Resultado:** OK — 206 pruebas.

Adicionalmente, la app `apps.tutoring` quedó registrada en `INSTALLED_APPS` y su URL incluida en `config/urls.py` bajo el prefijo `tutoria/`.

---

## 5. Documentación revisada

| Documento | Observación |
|---|---|
| `docs/ADR/ADR-010-tutor-ia-local.md` | Revisado — decisión adoptada y verificada en su estructura |
| `docs/PLAN_MAESTRO_CODEGUARD.md` | Actualizado en esta intervención (Fase 3 → En progreso) |
| `docs/PLAN_DESARROLLO.md` | Actualizado en esta intervención (Fase 3 / Incremento 3) |
| `docs/ARQUITECTURA.md` | Actualizado en esta intervención (app `tutoring`) |
| `docs/SEGUIMIENTO_TEMPORAL_USUARIO.md` | Coherente con la nueva fase |
| `docs/INFORMES_ACEPTACION/README.md` | Coherente con la estructura de informes |

---

## 6. Problemas encontrados

| ID | Descripción | Severidad | Impacto | Resolución / Pendiente |
|---|---|---|---|---|
| P-1 | Fase 3 solo implementada parcialmente; falta validación en runtime con Ollama | Alta | No se puede aceptar la fase | Ejecutar `ollama pull qwen2.5-coder:1.5b` y validar API |
| P-2 | Criterios C-1 y C-3 requieren verificación con modelo real | Media | Evidencia incompleta | Probar con Ollama activo |
| P-3 | Criterios C-4 parcialmente verificados (tests); runtime pendiente | Media | Validación incompleta | Probar con Ollama inactivo/activo |

---

## 7. Decisiones técnicas

| ID | Decisión | Motivo | Alternativas descartadas | Consecuencias |
|---|---|---|---|---|
| ADR-010 | Tutor IA local vía Ollama (`qwen2.5-coder:1.5b`) | Offline-first, sin costo, sin envío a terceros | Servicio IA externo (descartado: rompe privacidad/offline); modelo local con Transformers/PyTorch (descartado: consumo excesivo de RAM) | Dependencia de Ollama; degradación a reglas estáticas |

---

## 8. Aspectos pendientes

1. Ejecutar `ollama pull qwen2.5-coder:1.5b` y validar la disponibilidad de la API `/api/chat` local.
2. Validar las APIs `/tutoria/*` en ejecución real con Ollama activo.
3. Verificar criterios de aceptación C-1, C-3 y C-4 en runtime.
4. Elaborar el informe de aceptación formal de la Fase 3 al cerrar la fase.
5. Continuar con Fase 4 (Evaluaciones y progresión académica).

---

## 9. Veredicto de aceptación

- [ ] Cumple todos los criterios de aceptación (criterios pendientes o parcialmente verificados presentes)
- [ ] Cumple con salvedades (ver sección 6)
- [ ] No cumple

**Firma:** Subagente 4 — Documentación, Integración y QA  
**Fecha:** 16 de noviembre de 2026

---

> **Nota:** Este informe está emitido en **borrador** por el Subagente 4 a partir de la implementación parcial documentada (ADR-010, commit `606e501`) y la suite de 9 pruebas. No debe presentarse como aceptación formal de la Fase 3 hasta completar los aspectos pendientes.
