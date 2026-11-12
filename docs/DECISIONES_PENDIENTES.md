# CodeGuard Pro — Decisiones pendientes

**Producto:** CodeGuard Pro  
**Versión:** 1.1  
**Estado:** Decisiones técnicas y de producto pendientes de definición  
**Rama de trabajo:** `docs/phase-2-hybrid-knowledge-sync`

---

## 1. Decisiones de producto (requieren al propietario)

| ID | Decisión | Contexto | Opciones | Recomendación |
|---|---|---|---|---|
| P-001 | Valor de N para bloqueo tras intentos fallidos (RF-006 / RS-017) | El SRS deja N sin definir; no se debe inventar | N=3, N=5, N=10 | Pendiente de propietario. Arquitectura preparada para hacerlo configurable. |
| P-002 | Selección de etapas ASCENSO para el MVP | El SRS menciona (0,1,2,3,8,17,21) solo como propuesta | Todas las 33 visibles; subset desarrollado | Representar las 33 etapas (RF-010/011) y desarrollar según prioridad ASCENSO 3.1. |
| P-003 | Cifrado de backup (RF-105 / RS-008) | Propuesto, no aprobado | Con cifrado / sin cifrado | Documentar recomendación y riesgos; implementar si el propietario aprueba. |

---

## 2. Decisiones técnicas autónomas (registradas)

| ID | Decisión | Justificación |
|---|---|---|
| T-001 | Django 5.2.19 LTS | Versión con soporte vigente, compatible con Python 3.14 y Argon2. |
| T-002 | SQLite con FTS5 | Monousuario, sin proceso servidor, rápido en NVMe, verificado en entorno real. |
| T-003 | HTMX + Bootstrap 5 locales (sin CDN) | Offline-first, sin dependencia de Internet, bajo consumo. |
| T-004 | Modelo de usuario personalizado (`accounts.Usuario`) — **RESUELTA (CG-002)** | Activado con `AUTH_USER_MODEL = "accounts.Usuario"`; la migración de datos preservó al usuario existente (tabla `auth_user` → `accounts_usuario`). Permite campos específicos (tiempo de sesión, fecha de setup) sin romper auth de Django. |
| T-005 | Middleware propio para sesión, seguridad y setup | Centraliza lógica transversal sin acoplar vistas. |
| T-006 | `ConfiguracionSistema` como singleton (pk=1) | Configuración global sencilla sin tabla de parámetros por ahora. |
| T-007 | Estructura de apps por dominio (`core`, `accounts`, `audit`, ...) | Monolito modular con responsabilidades delimitadas, sin apps innecesarias. |

---

## 3. Decisiones de arquitectura/producto aprobadas para la Fase 2

| ID | Decisión | Resolución | Alcance y límites |
|---|---|---|---|
| P-004 | Actualización del conocimiento académico | **RESUELTA por el propietario (11-11-2026): modelo híbrido.** Un servidor central distribuye contenido revisado y versionado; el cliente sincroniza automáticamente cuando hay conexión y conserva el contenido local. | Forma parte de la Fase 2. Sincronización pull-only por HTTPS; el cliente valida firma, hash, esquema y compatibilidad; instalación atómica y rollback. No se suben progreso, intentos, código, calificaciones ni datos personales. La detección de cambios en fuentes no publica contenido sin revisión editorial. Véase `docs/ADR/ADR-004-sincronizacion-hibrida-conocimiento.md`. |

## 4. Cómo resolver una decisión pendiente

1. El propietario define el valor o la opción.
2. Se registra en este archivo (marcar como resuelta).
3. Se implementa en el siguiente incremento correspondiente.
4. No se bloquea el resto del desarrollo por decisiones que solo afectan a un módulo.
