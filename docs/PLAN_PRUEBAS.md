# CodeGuard Pro — Plan de pruebas

**Producto:** CodeGuard Pro  
**Versión:** 1.0  
**Entorno de medida:** HP 240 14 G10, Fedora 44, i3-N305, ~1.3 GB RAM libre, SSD NVMe

> **Nota:** El sistema de autenticación está temporalmente desactivado
> (`AUTH_DISABLED = True`). Las pruebas de autenticación original se conservan
> y se verifican con `override_settings(AUTH_DISABLED=False)`. Las nuevas pruebas
> del modo sin autenticación usan `override_settings(AUTH_DISABLED=True)`.

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

## 2.1 Pruebas funcionales de autenticación y recuperación (implementadas en esta intervención)

| ID | Prueba | Caso | Resultado esperado | Estado |
|---|---|---|---|---|
| T-006 | Login correcto | POST `/accounts/login/` con credenciales válidas | Redirección a panel (302 → `/`) | ✅ Automática |
| T-007 | Login incorrecto | POST con contraseña inválida | Re-render del login con error (200) | ✅ Automática |
| T-008 | Login repetido | GET `/accounts/login/` autenticado | Redirección a panel (302) | ✅ Automática |
| T-009 | Logout POST | POST `/accounts/logout/` | Redirección a panel + sesión cerrada | ✅ Automática |
| T-009b | Logout GET | GET `/accounts/logout/` | 405 Method Not Allowed, sesión no cierra | ✅ Automática |
| T-010 | Cambio de contraseña | POST con datos válidos | Redirección + `check_password` | ✅ Automática |
| T-010b | Nueva = actual | POST con contraseña idéntica a la actual | Error de validación, sin cambio | ✅ Automática |
| T-011 | Frase de rescate inválida | POST con frase incorrecta | Re-render con error (200) | ✅ Automática |
| T-012 | Frase de rescate válida | POST con frase válida | Redirección a `/accounts/rescate/resetear/` | ✅ Automática |
| T-013 | Frase no se consume al validar | Validar frase sin completar reset | Frase sigue `usada=False` | ✅ Automática |
| T-014 | Reset completo | Frase válida + nueva contraseña | Contraseña cambia, frase se invalida | ✅ Automática |
| T-015 | Frase ya usada | Reutilizar frase después del reset | Rechazada, sin cambio de contraseña | ✅ Automática |
| T-016 | Sesión vencida GET | GET a vista protegida con sesión expirada | Redirección a login, vista no ejecutada | ✅ Automática |
| T-017 | Sesión vencida POST | POST a vista protegida con sesión expirada | Redirección a login, operación no ejecutada | ✅ Automática |
| T-018 | Renovación de actividad | Petición válida renueva `ultima_actividad` | Marca de tiempo actualizada | ✅ Automática |
| T-019 | Setup válido | POST con datos correctos | Usuario creado, frase generada, éxito renderizado | ✅ Automática |
| T-020 | Setup contraseñas diferentes | POST con contraseñas no coincidentes | Error de formulario, sin usuario | ✅ Automática |
| T-021 | Setup contraseña corta | POST con < 8 caracteres | Error de formulario, sin usuario | ✅ Automática |
| T-022 | Setup términos no aceptados | POST sin aceptar términos | Error de formulario, sin usuario | ✅ Automática |
| T-023 | Bloqueo tras 5 fallos | 5 POST de login con contraseña incorrecta | Cuenta bloqueada 15 min, evento de auditoría | ✅ Automática |
| T-024 | Login durante bloqueo | POST dentro de ventana de bloqueo | Rechazado sin comprobar contraseña | ✅ Automática |
| T-025 | Reinicio tras éxito | Login exitoso después de bloqueo vencido | `intentos_fallidos` = 0, `bloqueado_hasta` = null | ✅ Automática |
| T-026 | Mensaje genérico | Login fallido con usuario inexistente | "Usuario o contraseña incorrectos" sin revelar existencia | ✅ Automática |
| T-027 | Bloqueo expira | Simular 15 min (mocking del reloj) | Se permite nuevo intento de login | ✅ Automática (`test_bloqueo_expira_tras_quince_minutos`) |

---

## 2.2 Pruebas funcionales de modo sin autenticación (esta intervención)

| ID | Prueba | Caso | Resultado esperado | Estado |
|---|---|---|---|---|
| T-500 | Panel directo | GET `/` sin credenciales | Panel (200), sin redirección a login | ✅ Automática |
| T-501 | No redirección a login | Cualquier vista principal | 200, nunca redirige a `/accounts/login/` | ✅ Automática |
| T-502 | Rutas de auth desactivadas | GET/POST `/accounts/login/`, `/accounts/setup/`, `/accounts/logout/`, `/accounts/rescate/`, `/accounts/rescate/resetear/`, `/accounts/cambiar-contraseña/` | Redirección al panel (302) | ✅ Automática |
| T-503 | Login POST no autentica | POST `/accounts/login/` con credenciales | Redirección al panel, no inicia sesión | ✅ Automática |
| T-504 | Sin botón de logout | Navegación visible | No aparece "Cerrar sesión" ni `accounts:logout` | ✅ Automática |
| T-505 | request.user anónimo | Cualquier petición | `request.user` es `AnonymousUser` | ✅ Automática |
| T-506 | Auditoría actor nulo | Acceso al panel | Evento `acceso_panel` con `usuario=None` | ✅ Automática |
| T-507 | Progreso con propietario local | Marcar lección sin login | Progreso guardado con usuario local | ✅ Automática |
| T-508 | 12 temas presentes | Selector de temas | 12 `data-theme` en el HTML | ✅ Automática |

## 3. Pruebas de seguridad (pendientes de automatizar)

| ID | Prueba | Caso | Resultado esperado | Estado |
|---|---|---|---|---|
| T-300 | Acceso anónimo | GET a vista principal sin login | Panel (200), sin redirección (auth desactivada) | ✅ Verificado (automática: `test_panel_abre_directamente_sin_autenticacion`) |
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

El incremento 1 se considera terminado con las pruebas automatizadas implementadas:
- Autenticación: login correcto/incorrecto/repetido (T-006 a T-008).
- Cierre de sesión: POST cierra, GET devuelve 405 (T-009, T-009b).
- Cambio de contraseña: válido y no-reutilización (T-010, T-010b).
- Recuperación: frase válida/inválida, no-consumo al validar, reset completo, frase ya usada (T-011 a T-015).
- Expiración por inactividad: GET y POST en vista protegida (T-016, T-017).
- Renovación de actividad (T-018).
- Setup inicial: válido e inválido (contraseñas diferentes, corta, términos) (T-019 a T-022).
- Bloqueo por intentos fallidos (RS-017): bloqueo tras 5 fallos, rechazo durante bloqueo, reinicio tras éxito, mensaje genérico (T-023 a T-026).
- Auditoría: login/logout/inactividad/setup/cambio de contraseña/uso de frase/acceso denegado (`apps/audit/tests/test_audit.py`).
- Operaciones académicas con sesión vencida (`apps/roadmaps/tests/test_roadmaps.py`).

Total: **53 tests automatizados pasando** (`apps.accounts`, `apps.audit`, `apps.core`, `apps.roadmaps`).

Las pruebas de seguridad restantes (CSRF, XSS, validación de archivos, acceso no autorizado, path traversal, archivos maliciosos, exposición de secretos) siguen pendientes en sus respectivos incrementos.

La prueba T-027 (bloqueo expira tras 15 min) requiere espera real y se valida manualmente.

---

## 6.1 Pruebas del incremento de identidad y evidencias

> **Estado: implementadas en código; pendientes de ejecución en el entorno local.**

| ID | Prueba | Caso | Resultado esperado |
|---|---|---|---|
| DATA-001 | UUID de lección | Crear una lección | Se asigna una clave UUID no nula, única e inmutable |
| DATA-002 | UUID de ejemplo | Crear un ejemplo | Se asigna una clave UUID propia |
| DATA-003 | UUID de ejercicio | Crear ejercicios distintos | Cada ejercicio recibe una clave UUID distinta |
| DATA-004 | Migración de claves | Actualizar una BD con registros existentes | Cada registro obtiene un UUID antes de imponer unicidad y NOT NULL |
| DATA-005 | Protección de ejercicio | Eliminar ejercicio con intentos | La operación se rechaza y los intentos permanecen |
| DATA-006 | Protección de evaluador | Eliminar configuración referenciada por intento | La operación se rechaza y la configuración histórica permanece |
| DATA-007 | Intento sin evaluador | Guardar entrega pendiente | La referencia a configuración puede permanecer nula |

## 6.2 Pruebas del catálogo de fuentes y snapshots

> **Estado: incorporadas al código; pendientes de ejecución local.**

| ID | Prueba | Resultado esperado |
|---|---|---|
| KNOW-001 | Registrar fuente con URL canónica y licencia | Se conserva publicador, edición, licencia y fecha de consulta |
| KNOW-002 | Crear snapshot versionado | Se conserva JSON, UUID, versión y hash |
| KNOW-003 | Asociar fuentes a un snapshot | La atribución identifica fuente, rol y localizador |
| KNOW-004 | Repetir número de versión de una lección | La restricción única rechaza el duplicado |
| KNOW-005 | Publicar dos versiones de una lección | La restricción parcial permite solo una publicada |
| KNOW-006 | Hash con formato inválido | La validación rechaza valores que no sean SHA-256 hexadecimal |
| KNOW-007 | Eliminar una fuente referenciada | La operación se bloquea por PROTECT |
| KNOW-008 | Eliminar una versión referenciada | La operación se bloquea por PROTECT |

## 6.3 Pruebas del servicio de snapshots

> **Estado: incorporadas al código; pendientes de ejecución local.**

| ID | Prueba | Resultado esperado |
|---|---|---|
| SNAP-001 | Generar snapshot desde contenido completo | Se captura contenido, ejemplos y ejercicios publicados |
| SNAP-002 | Recurso no publicado | No se incluye en el snapshot |
| SNAP-003 | Hash canónico | SHA-256 coincide con la serialización determinista |
| SNAP-004 | Nueva versión | Se incrementa el número sin sobrescribir la anterior |
| SNAP-005 | Modificar borrador tras snapshot | La versión anterior conserva el contenido original |
| SNAP-006 | Lección incompleta | Se rechaza la generación |
| SNAP-007 | Fuente inactiva | Se rechaza su asociación |

## 6.4 Pruebas del flujo editorial

> **Estado: incorporadas al código; pendientes de ejecución local.**

| ID | Prueba | Resultado esperado |
|---|---|---|
| EDIT-001 | Publicar un borrador directamente | Se rechaza la transición |
| EDIT-002 | Enviar versión sin fuente o con hash alterado | Se rechaza el envío a revisión |
| EDIT-003 | Transición con usuario no editorial | Se rechaza la operación |
| EDIT-004 | Aprobar una versión en revisión | Se registra revisor y fecha |
| EDIT-005 | Modificar snapshot tras enviar a revisión | El modelo rechaza el cambio |
| EDIT-006 | Publicar una versión aprobada | Se registra publicador y fecha |
| EDIT-007 | Publicar una nueva versión | La anterior pasa a sustituida en la misma transacción |
| EDIT-008 | Retirar publicación sin motivo | Se rechaza la operación |
| EDIT-009 | Retirar publicación con motivo | Se conserva snapshot y motivo |
| EDIT-010 | Publicar dos versiones simultáneas | Solo una versión queda publicada por lección |

## 7. Pruebas previstas para el sistema híbrido de conocimiento (Fase 2)

> **Estado: PENDIENTES.** El sincronizador, el servicio central y los paquetes firmados todavía no están implementados. Estas pruebas definen el contrato que deberá verificarse cuando se construyan.

| ID | Prueba | Caso | Resultado esperado |
|---|---|---|---|
| SYNC-001 | Arranque offline | Iniciar la aplicación sin conexión | El núcleo local abre sin esperar al servicio central |
| SYNC-002 | Consulta offline | Abrir una lección instalada sin red | Contenido y recursos disponibles desde almacenamiento local |
| SYNC-003 | Manifiesto disponible | Conexión activa y nueva versión publicada | Se detecta una actualización compatible sin bloquear la interfaz |
| SYNC-004 | Sin cambios | Manifiesto y versión local coinciden | No se descarga ni reinstala contenido innecesariamente |
| SYNC-005 | Timeout | Servicio central no responde | Se conserva la versión local y el estudio continúa |
| SYNC-006 | Descarga interrumpida | Cortar conexión durante descarga | Paquete temporal incompleto no se activa; se puede reintentar |
| SYNC-007 | Hash inválido | Alterar un byte del paquete | Rechazo de instalación y registro del error |
| SYNC-008 | Firma inválida | Firma no verificable o clave desconocida | Rechazo del paquete |
| SYNC-009 | Esquema incompatible | Paquete con versión de esquema no soportada | Rechazo seguro sin reemplazar el contenido actual |
| SYNC-010 | Aplicación incompatible | Paquete exige versión de app superior | No se instala; se informa la incompatibilidad |
| SYNC-011 | Tamaño/rutas maliciosas | Paquete excede límites o contiene path traversal | Rechazo antes de escribir fuera del área temporal |
| SYNC-012 | Instalación atómica | Fallo durante activación | La versión anterior permanece activa |
| SYNC-013 | Rollback | Restaurar versión previa | Contenido anterior vuelve a estar disponible y se registra la operación |
| SYNC-014 | Preservación de progreso | Actualizar una lección con intentos existentes | Progreso, intentos, preferencias y notas permanecen intactos |
| SYNC-015 | Trazabilidad de intentos | Revisar intento creado antes de actualización | Se conserva versión de contenido y evaluador originales |
| SYNC-016 | Privacidad | Inspeccionar tráfico de sincronización | No se transmiten respuestas, código, calificaciones ni datos personales |
| SYNC-017 | Retiro de contenido | Publicar aviso de retirada/sustitución | Se advierte al estudiante sin borrar evidencias históricas |
| SYNC-018 | Detección editorial | Cambiar fuente externa sin aprobación editorial | Se genera propuesta/aviso; no se publica automáticamente |
| SYNC-019 | Reintento/backoff | Servicio intermitente | Reintentos limitados sin bucle agresivo ni bloqueo del usuario |
| SYNC-020 | Electron y desarrollo | Ejecutar en ambos modos | Mismo comportamiento de sincronización y almacenamiento local |
| SYNC-021 | Firma y hash sin circularidad | Manifiesto externo firmado declara hash del ZIP | Firma y hash se verifican sin que el manifiesto forme parte del ZIP hasheado |
| SYNC-022 | Anti-replay/downgrade | Se presenta manifiesto válido con sequence inferior o repetida con contenido distinto | Cliente rechaza la publicación antigua o inconsistente |
| SYNC-023 | Redirección de host | URL o redirección apunta a host no permitido | Descarga rechazada |
| SYNC-024 | ZIP malicioso | Entradas con traversal, symlink, duplicados o ratio/tamaño excesivo | Rechazo antes de escribir fuera del staging |
| SYNC-025 | Reanudación segura | Descarga incompleta o archivo temporal previo alterado | Se descarta o valida de nuevo; nunca se activa parcialmente |
| SYNC-026 | Sincronización concurrente | Se inician dos comprobaciones simultáneas | Solo una puede instalar; la otra espera o termina sin alterar el contenido activo |

La prueba T-200 de funcionamiento offline debe distinguir el núcleo local (que no depende de Internet) de la consulta de actualizaciones (que sí requiere conectividad). La sincronización debe probarse como función opcional, no como requisito de arranque.
