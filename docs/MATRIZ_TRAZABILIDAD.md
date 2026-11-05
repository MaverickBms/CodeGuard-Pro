# CodeGuard Pro — Matriz de trazabilidad

**Producto:** CodeGuard Pro  
**Versión:** 1.0 (MVP, primer incremento)  
**SRS de referencia:** `IEEE830(1).md` v2.0 — Sección 5

---

## 1. Nota metodológica

La matriz relaciona: **Requisito → Módulo → Componente → Prueba → Estado**.

La existencia de un identificador de prueba (T-xxx) en el SRS no implica que la prueba ya esté
implementada. Un requisito solo se marca como "Implementado" cuando hay evidencia (código +
prueba que pasa).

---

## 2. Requisitos del incremento 1 (núcleo funcional)

| ID | Descripción | Módulo | Componente | Prueba | Estado |
|---|---|---|---|---|---|
| RF-001 | Autenticación local | Identidad | `apps.accounts` (login) | T-001 | ✅ Implementado |
| RF-002 | Cierre por inactividad | Identidad | Middleware `SesionInactividad` | T-002 | ✅ Implementado |
| RF-003 | Configuración inicial | Identidad | `apps.accounts` (setup) | T-003 | ✅ Implementado |
| RF-004 | Frase de rescate (hash, un uso) | Identidad | `apps.accounts` (servicios) | T-004 | ✅ Implementado |
| RF-005 | Auditoría de accesos | Identidad | `apps.audit` (AuditLog) | T-005 | ✅ Implementado |
| RF-006 | Bloqueo tras N fallos | Identidad | (pendiente de N) | T-006 | ⏳ Pendiente (N sin definir) |
| RS-001 | Auth obligatoria | Global | Middleware auth | T-300 | ✅ Implementado |
| RS-002 | Argon2 | Identidad | `AUTH_PASSWORD_HASHERS` | T-301 | ✅ Implementado |
| RS-003 | Frase de rescate segura | Identidad | `apps.accounts` (servicios) | T-302 | ✅ Implementado |
| RS-004 | Bind 127.0.0.1 | Global | `runserver 127.0.0.1` | T-303 | ✅ Implementado |
| RS-009 | Timeout probado | Identidad | Middleware sesión | T-308 | ✅ Implementado |
| RS-010 | CSRF | Global | `CsrfViewMiddleware` | T-309 | ✅ Implementado |
| RS-011 | XSS + CSP | Global | Middleware cabeceras + plantillas | T-310 | ✅ Implementado |
| RS-012 | SQLi | Global | ORM Django | T-311 | ✅ Implementado |
| RS-013 | Cabeceras de seguridad | Global | `CabecerasSeguridadMiddleware` | T-312 | ✅ Implementado |
| RS-014 | Auditoría | Global | `apps.audit` | T-313 | ✅ Implementado |
| RS-016 | Política de contraseñas | Identidad | `SetupInicialForm` (≥8) | T-315 | ✅ Implementado |
| RS-017 | Bloqueo N intentos | Identidad | (pendiente) | T-316 | ⏳ Pendiente |
| RS-020 | Errores no expuestos | Global | `DEBUG=False` por defecto | T-319 | ✅ Implementado |
| RNF-001 | Offline | Global | Sin dependencia de red | T-200 | ✅ Implementado |
| RNF-002 | Bind 127.0.0.1 | Global | Servidor local | T-201 | ✅ Implementado |
| RNF-007 | MVT | Global | Estructura Django | T-206 | ✅ Implementado |
| RNF-009 | CSRF/XSS/SQLi | Global | Middlewares + ORM | T-208 | ✅ Implementado |
| RNF-015 | Assets locales | UI | `/static/` sin CDN | T-214 | ✅ Implementado |
| RNF-017 | Logging | Global | `logging` + `logs/codeguard.log` | T-216 | ✅ Implementado |
| RNF-018 | Sin telemetría | Global | Sin llamadas externas | T-217 | ✅ Implementado |

---

## 3. Requisitos pendientes de implementación (próximos incrementos)

| ID | Descripción | Módulo | Estado | Nota |
|---|---|---|---|---|
| RF-010 a RF-017 | Roadmap ASCENSO | Académico | ⏳ Pendiente | Incremento 2 |
| RF-020 a RF-029 | Competencias | Competencias | ⏳ Pendiente | Incremento 3 |
| RF-030 a RF-044 | Biblioteca documental | Documental | ⏳ Pendiente | Incremento 4 |
| RF-050 a RF-056 | Base de conocimiento | Conocimiento | ⏳ Pendiente | Incremento 4 |
| RF-060 a RF-071 | Evaluaciones | Evaluación | ⏳ Pendiente | Incremento 3 |
| RF-080 a RF-089 | Evidencias | Evidencias | ⏳ Pendiente | Incremento 5 |
| RF-090 a RF-097 | Laboratorios | Laboratorios | ⏳ Pendiente | Incremento 5 |
| RF-100 a RF-109 | Backups y administración | Administración | ⏳ Pendiente | Incremento 6 |
| RF-110 a RF-115 | Vigencia y revisión | Vigencia | ⏳ Pendiente | Incremento 6 |
| RF-120 a RF-123 | Ética | Ética | ⏳ Pendiente | Incremento 6 |

---

## 4. Requisitos propuestos (no aprobados para implementar)

| ID | Descripción | Estado | Nota |
|---|---|---|---|
| RF-018 | Tiempo por actividad | PROPUESTO | No implementar sin autorización |
| RF-019 | Rutas personalizadas | FUT / PROPUESTO | Etapa posterior |
| RF-026 | Anulación manual de criterios | PROPUESTO | No implementar sin autorización |
| RF-028 | Panel de competencias | PROPUESTO | No implementar sin autorización |
| RF-055 | Duplicados/conflictos de conceptos | PROPUESTO | No implementar sin autorización |
| RF-064 | Demostraciones de competencia | PROPUESTO | No implementar sin autorización |
| RF-071 | Informe de evaluación | PROPUESTO | No implementar sin autorización |
| RF-089 | Exportar portafolio | FUT / PROPUESTO | Etapa posterior |
| RF-095 | Entorno/contexto de laboratorio | PROPUESTO | No implementar sin autorización |
| RF-096 | Informe de laboratorio | PROPUESTO | No implementar sin autorización |
| RF-101 | Backup automático | PROPUESTO | No implementar sin autorización |
| RF-105 | Cifrado de backup | PROPUESTO | Documentado, pendiente de aprobación |
| RF-106 | Exportar formato abierto | PROPUESTO | No implementar sin autorización |
| RF-112 | Alerta de obsolescencia | PROPUESTO | No implementar sin autorización |
| RF-115 | Historial de cambios de contenido | PROPUESTO | No implementar sin autorización |

---

## 5. Evidencia del incremento 1

El incremento 1 se considera terminado cuando se cumple la lista de verificación de
`docs/PLAN_DESARROLLO.md` y pasan las pruebas de `docs/PLAN_PRUEBAS.md`.
