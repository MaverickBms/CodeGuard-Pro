# CodeGuard Pro — Plan de pruebas

**Producto:** CodeGuard Pro  
**Versión:** 1.0  
**Entorno de medida:** HP 240 14 G10, Fedora 44, i3-N305, ~1.3 GB RAM libre, SSD NVMe

---

## 1. Entorno de medición (RNF-003)

El objetivo de "menos de 300 MB de RAM en reposo" es un **objetivo a validar**, no una garantía.

| Parámetro | Valor |
|---|---|
| Equipo | HP 240 14 G10 |
| CPU | Intel Core i3-N305 (8/8 hilos) |
| RAM total | 7.5 GB |
| RAM libre observada | ~1.3 GB |
| Almacenamiento | SSD NVMe 238.5 GB (108 GB libres) |
| SO | Fedora Linux 44 Workstation |
| Python | 3.14.8 |
| Django | 5.2.19 |

Procedimiento de medición de RAM en reposo:
1. Arrancar el servidor WSGI local (Waitress) con `DEBUG=False`.
2. Medir RSS del proceso Python tras 5 minutos de inactividad (`ps` / `psutil`).
3. Repetir 3 veces y reportar promedio.

---

## 2. Pruebas funcionales (incremento 1)

| ID | Prueba | Caso | Resultado esperado | Estado |
|---|---|---|---|---|
| T-001 | Login | Credenciales válidas | Acceso al panel (200) | ✅ Verificado (automática: `test_login_redirige_a_panel_si_autentica`) |
| T-002 | Expiración de sesión | Inactividad > 15 min | Redirección a login | ✅ Verificado (automática: `test_sesion_expira_por_inactividad`) |
| T-003 | Configuración inicial | Primer arranque sin usuario | Redirección a `/accounts/setup/` | ✅ Verificado (vista: usuario existente → login) |
| T-004 | Frase de rescate | Crear y mostrar una vez | Frase generada, hash almacenado, no texto plano | ✅ Verificado (servicio) |
| T-005 | Auditoría de accesos | Login/logout | Entradas en `AuditLog` | ✅ Verificado (servicio/vistas) |
| T-200 | Offline | Desconectar red | Core funciona sin Internet | ✅ Arquitectura |
| T-201 | Bind 127.0.0.1 | `ss -ltnp` | Solo 127.0.0.1:8000 | ✅ Verificado |

---

## 2.1 Pruebas funcionales de autenticación (implementadas en esta intervención)

| ID | Prueba | Caso | Resultado esperado | Estado |
|---|---|---|---|---|
| T-006 | Login correcto | POST `/accounts/login/` con credenciales válidas | Redirección a panel (302 → `/`) | ✅ Automática |
| T-007 | Login incorrecto | POST con contraseña inválida | Re-render del login con error (200) | ✅ Automática |
| T-008 | Login repetido | GET `/accounts/login/` autenticado | Redirección a panel (302) | ✅ Automática |
| T-009 | Logout | POST `/accounts/logout/` | Redirección a panel + sesión cerrada | ✅ Automática |
| T-010 | Cambio de contraseña | POST con datos válidos | Redirección + `check_password` | ✅ Automática |
| T-011 | Frase de rescate inválida | POST con frase incorrecta | Re-render con error (200) | ✅ Automática |
| T-012 | Frase de rescate válida | POST con frase válida | Redirección a `/accounts/rescate/exito/` | ✅ Automática |

---

## 3. Pruebas de seguridad (pendientes de automatizar)

| ID | Prueba | Caso | Resultado esperado | Estado |
|---|---|---|---|---|
| T-300 | Acceso anónimo | GET a vista protegida sin login | Redirección a login (302) | ✅ Verificado |
| T-301 | Argon2 | Contraseña almacenada | Hash Argon2 (no texto plano) | ✅ Por código |
| T-302 | Frase de rescate | Usar frase dos veces | Segunda vez rechazada (usada) | ⏳ |
| T-303 | Bind | Servidor en 0.0.0.0 | No permitido; solo 127.0.0.1 | ✅ Verificado |
| T-304 | Validación de archivos | Subir archivo malicioso | Rechazado | ⏳ (incremento evidencias) |
| T-305 | Acceso directo a evidencias | URL directa sin auth | Redirección a login | ⏳ (incremento evidencias) |
| T-306 | Path traversal | `../` en nombre de archivo | Rechazado | ⏳ (incremento backups) |
| T-307 | Archivos maliciosos | Backup con rutas peligrosas | Rechazado en validación | ⏳ (incremento backups) |
| T-308 | Protección de sesiones | Cookie robada / fijación | HttpOnly, SameSite=Lax | ✅ Configurado |
| T-309 | CSRF | POST sin token | 403 | ✅ Middleware |
| T-310 | XSS | Inyectar script en entrada | Escape de salida + CSP | ✅ Configurado |
| T-311 | SQLi | Inyección SQL en formulario | ORM parametrizado | ✅ Django ORM |
| T-312 | Cabeceras | Respuesta HTTP | CSP, X-Frame-Options, etc. | ✅ Verificado |
| T-313 | Auditoría | Evento de seguridad | Entrada en `AuditLog` | ✅ Verificado |
| T-314 | LUKS límites | Documentar | Doc. de límites de cifrado en reposo | ✅ Documentado |
| T-315 | Política de contraseñas | Contraseña < 8 caracteres | Rechazada en setup | ✅ Form |
| T-316 | Bloqueo N intentos | N fallos → bloqueo | Pendiente (N sin definir) | ⏳ |
| T-317 | Minimización | Datos sensibles mínimos | Sin telemetría, logs sin secretos | ✅ |
| T-318 | Dependencias | `requirements.txt` | Versiones exactas fijadas | ✅ |
| T-319 | Errores internos | `DEBUG=False` | Mensajes genéricos, no traceback | ✅ |

---

## 4. Pruebas de integridad (pendientes)

| ID | Prueba | Caso | Estado |
|---|---|---|---|
| T-401 | Migraciones desde vacío | `migrate` en BD vacía | ✅ Verificado |
| T-402 | Restricciones de datos | FK, unique, not null | ⏳ |
| T-403 | Integridad documental | Hash, duplicados | ⏳ (incremento biblioteca) |
| T-404 | Integridad de evidencias | SHA-256 | ⏳ (incremento evidencias) |
| T-405 | Integridad de backups | Hash pre/post, validación | ⏳ (incremento backups) |

---

## 5. Pruebas de rendimiento (pendientes de medir)

| ID | Prueba | Objetivo | Estado |
|---|---|---|---|
| T-202 | Tiempo de inicio | Arranque rápido | ⏳ |
| T-203 | RAM en reposo | < 300 MB (objetivo a validar) | ⏳ |
| T-204 | Búsqueda FTS5 | < 2 s para hasta 50 libros | ⏳ (incremento biblioteca) |
| T-205 | Importación por lotes | Memoria controlada | ⏳ (incremento biblioteca) |
| T-206 | Consultas principales | Sin N+1 | ⏳ |
| T-207 | Navegación | Responsiva en 1366x768 | ⏳ (UI) |

---

## 6. Pruebas pendientes tras el incremento 1

El incremento 1 se considera terminado con las pruebas manuales verificadas (login, panel,
logout, acceso protegido, bind 127.0.0.1, sin CDN). Las pruebas automatizadas completas (T-002
en adelante) se implementarán en `tests/` a medida que avance cada incremento.

Con la intervención actual se completaron las pruebas automatizadas de autenticación, cierre de
sesión, cambio de contraseña, frase de rescate y expiración por inactividad (T-006 a T-012 y
T-002). No se declara un requisito como implementado sin evidencia de prueba. Las pruebas de
seguridad restantes (CSRF, XSS, validación de archivos, acceso no autorizado, path traversal,
archivos maliciosos, exposición de secretos) siguen pendientes en sus respectivos incrementos.
