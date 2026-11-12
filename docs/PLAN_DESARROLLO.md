# CodeGuard Pro — Plan de desarrollo

**Producto:** CodeGuard Pro  
**Versión:** 2.0  
**Estrategia:** Incrementos verificables (según `IEEE830(1).md`, Sección 14)

---

## Estado actual: Incremento 1 — Núcleo funcional ✅ y Incremento 2 — Roadmap académico y conocimiento versionado 🔄

**Estado:** Incremento 1 implementado y verificado. Incremento 2 parcialmente implementado en `main`; correcciones de consistencia en curso en `fix/phase-2-integrity-learning`, derivada de `main` en `c2ec604`.

---

## Incremento 1 — Núcleo funcional

**Estado:** ✅ Implementado y verificado

### Qué se implementó (incremento 1)

1. Estructura base Django (proyecto `config`, apps `core`, `accounts`, `audit`).
2. Configuración local (settings base + desarrollo, `.env.example`).
3. Base de datos SQLite con migraciones (aplicadas desde base vacía).
4. Autenticación local con contraseña maestra (Argon2).
5. Configuración inicial guiada (setup): usuario, contraseña, aceptación de términos.
6. Frase de rescate de alta entropía (≥128 bits), mostrada una sola vez, hash Argon2, un uso.
7. Sesiones server-side con timeout de inactividad (15 min defecto).
8. Panel principal con navegación principal. Acceso directo sin credenciales mientras `AUTH_DISABLED = True`; protegido con `@login_required` cuando `AUTH_DISABLED = False`.
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
- Modelo de usuario custom `accounts.Usuario` activo (`AUTH_USER_MODEL`) con migración de datos que preservó al usuario existente.

---

## Incremento 2 — Roadmap académico y conocimiento versionado (Fase 2)

**Estado:** 🔄 En curso (base integrada en `main`; correcciones en `fix/phase-2-integrity-learning`)

### Qué se implementó (incremento 2, en rama de trabajo)

1. **Roadmap ASCENSO 3.1:** las 33 etapas (0 a 32) con bloques, secciones, prioridades, objetivos, proyectos y prerrequisitos. Cargable con `python manage.py cargar_ascenso`.
2. **Estructura curricular relacional:** `Roadmap`, `Etapa`, `Modulo`, `Leccion`, `Prerrequisito`.
3. **Contenido académico editable:** `ContenidoLeccion`, `EjemploLeccion`, `EjercicioLeccion` con teoría, ejemplos, ejercicios, estado de publicación y evaluadores.
4. **Claves UUID estables:** `clave_contenido` en `Leccion`, `EjemploLeccion`, `EjercicioLeccion` para identidad portable entre instalaciones (migración 0004).
5. **Catálogo de fuentes documentales:** `FuenteConocimiento` con publicador, título, URL canónica, edición, identificador y URL de licencia, fecha de consulta, estado activo/notas (migración 0005).
6. **Snapshots inmutables de versión de lección:** `VersionContenidoLeccion` con flujo editorial completo (`borrador → revisión → aprobada → publicada → sustituida → retirada`), snapshot JSON, SHA-256, resumen de cambios, metadatos de auditoría (remitente, revisor, publicador, fechas) y protección contra modificación de versiones publicadas (migración 0005).
7. **Referencias de fuente por versión:** `ReferenciaFuenteContenido` con rol, localizador, nota de atribución, FK a fuente y FK a versión (migración 0005).
8. **Auditoría editorial:** envío a revisión, aprobación, publicación, sustitución y retirada con restricciones de transición y metadatos requeridos por estado (migraciones 0006–0008).
9. **Revisión de licencias de fuentes:** estados `compatible`, `solo_referencia`, `requiere_permiso`, `no_reutilizable` con evidencia HTTPS y alcance (migraciones 0009–0010).
10. **Autoría de versiones:** `VersionContenidoLeccion.autoria` con responsable y fecha (migración 0011).
11. **Comandos de gestión:** `cargar_ascenso`, `crear_version_leccion`, `gestionar_version_leccion`, `importar_paquete_contenido`, `registrar_fuente_conocimiento`, `revisar_licencia_fuente`, `validar_paquete_contenido`.
12. **Registro local de paquetes de conocimiento:** `PaqueteConocimientoInstalado` con transiciones controladas, identidad inmutable, un solo activo por canal, secuencia única por canal, protección contra eliminación física y actualización masiva (migración 0012).
13. **Un solo paquete activo por canal:** restricción parcial por `estado=activo` y migración de datos para garantizar unicidad (migración 0013).
14. **Estado de sincronización por canal:** `EstadoSincronizacion` para rastrear la última consulta, éxito, ETag, canal y error (migración 0012).
15. **Verificador de distribución firmada:** validación de manifiesto, firma Ed25519, hash SHA-256, estructura de ZIP, rutas prohibidas y symlinks (`validate_package_archive`, `verify_signed_manifest`).
16. **Pruebas:** 93 pruebas automatizadas confirmadas por el usuario en el estado previo a las correcciones actuales.
17. **Contenido activo:** puntero `ContenidoLeccionActivo` para seleccionar snapshots editoriales publicados sin sobrescribir contenido histórico (migración 0014).
18. **Evidencia de entrega:** cada intento conserva el snapshot del ejercicio presentado y referencia la versión editorial activa cuando corresponde.
19. **Interfaz de ejercicios:** formulario CSRF de entrega, límite de 20.000 caracteres e historial de los últimos tres intentos.
20. **Hardening del registro local:** validación de escrituras masivas y bloqueo de actualizaciones masivas del estado de sincronización.\n21. **Generador de paquetes:** ZIP reproducible, índice interno, manifiesto externo y firma Ed25519 desde snapshots activos; migración 0015 con secuencias por canal y registro inmutable. La migración y pruebas nuevas están pendientes de validación local.

### Qué sigue pendiente (incremento 2, Fase 2)

- Cliente de sincronización de red (consulta de manifiesto, descarga, instalación atómica, rollback).
- Hosting y endpoint HTTPS del distribuidor; el generador local ya produce ZIP, manifiesto y firma, pero no despliega.
- Cliente de sincronización pull-only, descarga, instalación atómica y rollback.
- Integración del almacén de claves públicas y allowlist de producción en el cliente.
- Validación local de la migración 0015 y de las pruebas del publicador; las pruebas históricas no validan estos componentes.

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
