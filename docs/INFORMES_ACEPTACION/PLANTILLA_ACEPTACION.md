# Plantilla — Informe de aceptación de fase

**Producto:** CodeGuard Pro  
**Fase:** [N.º] — [Nombre]  
**Estado del informe:** Borrador / En revisión / Aprobado / Rechazado  
**Elaborado por:** Subagente 4 — Documentación, Integración y QA  
**Fecha:** [YYYY-MM-DD]  
**Rama de referencia:** [nombre de rama]  
**Commit de referencia:** [hash]  

---

## 1. Resumen ejecutivo

Breve descripción de qué se entregó en esta fase, qué se verificó y el veredicto global (cumple / no cumple / cumple con salvedades).

---

## 2. Alcance verificado

Listado de funcionalidades incluidas en la fase y su estado:

| Funcionalidad | Implementada | Pruebas | Estado | Evidencia |
|---------------|--------------|---------|--------|-----------|
| — | — | — | — | — |

---

## 3. Criterios de aceptación

| ID | Criterio | Resultado | Observación |
|----|----------|-----------|-------------|
| — | — | ✅ / ❌ / ⚠️ | — |

---

## 4. Pruebas ejecutadas

| Suite / Prueba | Casos | Pasan | Fallan | Entorno | Fecha |
|----------------|-------|-------|--------|---------|-------|
| `apps.core` | — | — | — | development | — |
| `apps.accounts` | — | — | — | development | — |
| `apps.audit` | — | — | — | development | — |
| `apps.roadmaps` | — | — | — | development | — |
| Pruebas manuales GUI | — | — | — | Electron + Waitress | — |

Comando de ejecución:
```bash
python manage.py test apps.core apps.accounts apps.audit apps.roadmaps --settings=config.settings.development
```

---

## 5. Documentación revisada

| Documento | Coherente | Actualizado | Observación |
|-----------|-----------|-------------|-------------|
| `docs/PLAN_DESARROLLO.md` | — | — | — |
| `docs/ARQUITECTURA.md` | — | — | — |
| `docs/MODELO_DATOS.md` | — | — | — |
| `docs/MATRIZ_TRAZABILIDAD.md` | — | — | — |
| `docs/SEGURIDAD.md` | — | — | — |
| `docs/PLAN_PRUEBAS.md` | — | — | — |
| `docs/SEGUIMIENTO_TEMPORAL_USUARIO.md` | — | — | — |

---

## 6. Problemas encontrados

| ID | Descripción | Severidad | Impacto | Resolución / Pendiente |
|----|-------------|-----------|---------|------------------------|
| — | — | — | — | — |

---

## 7. Decisiones técnicas

| ID | Decisión | Motivo | Alternativas descartadas | Consecuencias |
|----|----------|--------|--------------------------|---------------|
| — | — | — | — | — |

---

## 8. Aspectos pendientes

Listado de trabajo que queda para dar por cerrada la fase:

1. —
2. —

---

## 9. Veredicto de aceptación

- [ ] Cumple todos los criterios de aceptación
- [ ] Cumple con salvedades (ver sección 6)
- [ ] No cumple (ver sección 6)

**Firma:** Subagente 4 — Documentación, Integración y QA  
**Fecha:** [YYYY-MM-DD]
