# CodeGuard Pro — Plan de desarrollo

**Producto:** CodeGuard Pro  
**Versión:** 1.0  
**Estrategia:** Incrementos verificables (según `IEEE830(1).md`, Sección 14)

---

## Estado actual: Incremento 1 — Núcleo funcional

**Estado:** ✅ Implementado y verificado

### Qué se implementó (incremento 1)

1. Estructura base Django (proyecto `config`, apps `core`, `accounts`, `audit`).
2. Configuración local (settings base + desarrollo, `.env.example`).
3. Base de datos SQLite con migraciones (aplicadas desde base vacía).
4. Autenticación local con contraseña maestra (Argon2).
5. Configuración inicial guiada (setup): usuario, contraseña, aceptación de términos.
6. Frase de rescate de alta entropía (≥128 bits), mostrada una sola vez, hash Argon2, un uso.
7. Sesiones server-side con timeout de inactividad (15 min defecto).
8. Panel principal protegido (`@login_required`) con navegación principal.
9. Middleware de seguridad: sesión por inactividad, cabeceras CSP/X-Frame/etc., redirección setup.
10. Registro de auditoría de accesos (`AuditLog`).
11. Logging a consola y archivo (`logs/codeguard.log`).
12. Plantillas con Bootstrap 5 y HTMX locales (sin CDN).
13. Pruebas manuales de flujo: login, panel, logout, acceso protegido.
14. Documentación: arquitectura, modelo de datos, seguridad, instalación, trazabilidad.

### Criterios de aceptación del incremento 1

| Criterio | Verificación | Resultado |
|---|---|---|
| La aplicación arranca | `runserver 127.0.0.1:8000` | ✅ |
| La base de datos se crea | `migrate` desde vacío | ✅ |
| Las migraciones funcionan | `makemigrations` + `migrate` | ✅ |
| El usuario inicial puede crearse | `crear_usuario_inicial` | ✅ |
| El login funciona | POST `/accounts/login/` → 302 | ✅ |
| Las rutas protegidas requieren auth | GET `/` sin login → 302 a login | ✅ |
| El servidor escucha en 127.0.0.1 (Waitress + WhiteNoise) | `ss -ltnp` / `python server_entry.py` | ✅ |
| No depende de CDN | recursos en `/static/` | ✅ |
| No necesita conexión externa para el núcleo | offline | ✅ |

### Hardening aplicado (intervención de auditoría — CG-001 a CG-010)

- `DEBUG=False` por defecto; desarrollo con `DEBUG=True` (solo en `config/settings/development.py`).
- CSP estricta (sin `unsafe-inline` en scripts) + middleware de cabeceras de seguridad.
- Sesiones con timeout por inactividad y registro en auditoría.
- Autenticación local completa: setup, login, logout, rescate, cambio de contraseña.
- Servidor local exclusivo en `127.0.0.1` con Waitress + WhiteNoise.
- Suite de pruebas automatizadas: 31 tests OK (auth, panel, roadmaps, auditoría).
- Modelo de usuario custom `accounts.Usuario` activo (`AUTH_USER_MODEL`) con migración de datos
  que preservó al usuario existente.

---

## Incremento 2 — Roadmap académico (pendiente)

- Las 33 etapas ASCENSO (0 a 32) desde el roadmap 3.1.
- Estados: desarrollada / no desarrollada (visibles).
- Dependencias entre etapas.
- Módulos, lecciones, actividades, prerrequisitos.
- Progreso por elemento.
- Verificación contra ASCENSO 3.1.

### Bloqueo: RF-006 / RS-017 (N de intentos) — pendiente de propietario.
Esto no bloquea el incremento 2 (afecta al módulo Identidad, no al Académico).

---

## Incremento 3 — Competencias y evaluaciones (pendiente)

- Competencias, niveles, criterios, reglas combinables.
- Evaluaciones (MC, abiertas, ejercicios, proyectos), rúbricas, intentos, resultados.
- Validación automática de criterios.

---

## Incremento 4 — Biblioteca documental y conocimiento (pendiente)

- Importación PDF, metadatos, extracción de texto, detección de duplicados/dañados/protegidos.
- FTS5, fragmentos, conceptos, relaciones, trazabilidad documental.

---

## Incremento 5 — Evidencias y laboratorios (pendiente)

- Archivos de evidencia, hash SHA-256, verificación de integridad, portafolio.
- Guías de laboratorio, pasos, comandos, resultados, capturas.

---

## Incremento 6 — Administración y vigencia (pendiente)

- Backups manuales (tar.gz), validación, restauración segura.
- Auditoría, limpieza temporal, vigencia documental, revisión manual.

---

## Reglas para considerar terminado un incremento

1. Funcionalidad implementada.
2. Requisitos asociados identificados.
3. Criterios de aceptación cumplidos.
4. Pruebas correspondientes pasan.
5. No errores críticos conocidos.
6. Documentación actualizada.
7. Funciona offline cuando corresponde.
8. Seguridad comprobada.
9. Cambios registrados.

No usar "terminado"/"100% funcional" sin evidencia.
