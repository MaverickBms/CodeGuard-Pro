# CodeGuard Pro — Seguridad

**Producto:** CodeGuard Pro  
**Versión:** 2.0 (Incremento 1 + Fase 2 parcialmente implementada)  
**SRS de referencia:** `IEEE830(1).md` v2.0 — Sección 3.5 (RS-001 a RS-020)  
**Rama de trabajo:** `docs/phase-2-hybrid-knowledge-sync`

---

## 1. Principios

La seguridad es un requisito fundamental. La aplicación está diseñada bajo el modelo de
confianza cero para el entorno local: solo el usuario legítimo tiene acceso, todo pasa por
autenticación (cuando está activada), y no se asume que la red local es segura.

CodeGuard es **offline-first**: no requiere Internet para sus funcionalidades esenciales.
Cualquier conexión futura a un servicio central de conocimiento será opcional, pull-only y
validada criptográficamente.

---

## 2. Requisitos de seguridad implementados

| ID | Requisito | Cómo se implementa | Estado |
|---|---|---|---|
| RS-001 | Autenticación local obligatoria | Todas las vistas requieren login cuando `AUTH_DISABLED = False`. Temporalmente desactivado (`AUTH_DISABLED = True`): la aplicación abre directamente el panel principal. La implementación original se conserva y puede reactivarse. Ver `docs/MODO_SIN_AUTENTICACION.md`. | ⚠️ Temporalmente desactivado |
| RS-002 | Argon2 para contraseñas | `AUTH_PASSWORD_HASHERS` con Argon2 primero | ✅ |
| RS-003 | Frase de rescate ≥128 bits, hash, un uso | `generar_frase_rescate()` (32 caracteres, ~201 bits), hash Argon2, `usada`. La frase no se consume al validar: solo se invalida al completar exitosamente el cambio de contraseña (flujo atómico). | ✅ |
| RS-004 | Bind 127.0.0.1 | Servidor WSGI local (Waitress) en `127.0.0.1:<puerto>`; `ALLOWED_HOSTS` solo localhost | ✅ |
| RS-005 | Validación de archivos | Pendiente (incremento de evidencias) | ⏳ |
| RS-006 | Archivos fuera de web root | Pendiente (incremento de evidencias) | ⏳ |
| RS-007 | Backup íntegro (hash + validación) | Pendiente (incremento de backups) | ⏳ |
| RS-008 | Cifrado de backup | Propuesto, no aprobado | ⏳ |
| RS-009 | Timeout de sesión probado | Middleware `SesionInactividadMiddleware` (15 min defecto). La comprobación de expiración se realiza antes de ejecutar la vista. | ✅ |
| RS-010 | CSRF | `CsrfViewMiddleware` + token en forms | ✅ |
| RS-011 | XSS | Escape de salida en plantillas + CSP estricta | ✅ |
| RS-012 | SQLi | ORM de Django (consultas parametrizadas) | ✅ |
| RS-013 | Cabeceras de seguridad | `CabecerasSeguridadMiddleware` (CSP, X-Frame, etc.) | ✅ |
| RS-014 | Auditoría de eventos | `AuditLog` + `registrar_evento()` en servicios | ✅ |
| RS-015 | Documentar límites de LUKS | En este documento y `docs/INSTALACION.md` | ✅ |
| RS-016 | Política de contraseñas | Mínimo 8 caracteres en `SetupInicialForm` | ✅ |
| RS-017 | Bloqueo N intentos | 5 intentos fallidos consecutivos bloquean la cuenta 15 min (`intentos_fallidos`, `bloqueado_hasta` en `Usuario`). Reinicio tras login exitoso. Registro en auditoría (`acceso_denegado`). Mensajes genéricos sin revelar existencia de usuario. | ✅ |
| RS-018 | Minimización de datos | Solo campos necesarios; sin telemetría | ✅ |
| RS-019 | Dependencias actualizadas | `requirements.txt` con versiones exactas (Django 5.2.19, cryptography 46.0.3, etc.) | ✅ |
| RS-020 | Errores no expuestos | `DEBUG=False` por defecto; mensajes genéricos | ✅ |
| RS-021 | Firmas digitales Ed25519 | `cryptography==46.0.3` para verificación de manifiestos de conocimiento | ✅ (rama de trabajo) |
| RS-022 | Validación de paquetes ZIP | `validate_package_archive()`: límites de tamaño, traversal, symlinks, hashes | ✅ (rama de trabajo) |

---

## 3. Middlewares de seguridad

- **`SesionInactividadMiddleware`**: expira la sesión tras `sesion_timeout_minutos` de inactividad (RF-002, RS-009). La comprobación se realiza antes de delegar en la vista (`get_response`) para garantizar que una sesión vencida nunca ejecute operaciones protegidas. Los recursos locales (estáticos y medios) no renuevan la sesión. Registra evento `logout_inactividad` en auditoría.
- **`CabecerasSeguridadMiddleware`**: añade a cada respuesta `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Permissions-Policy` restrictiva y una CSP estricta (solo recursos propios, sin CDN; scripts locales sin `unsafe-inline`, estilos con `unsafe-inline` por uso de estilos inline).
- **`AccesoLocalMiddleware`**: resuelve el propietario local en modo sin autenticación (`request.usuario_local`).
- **Redirección de configuración inicial**: implementada en la vista `apps.accounts.setup_inicial`; si no existe usuario, redirige a `/accounts/setup/` (cuando auth está activada).

> Nota: la redirección de primer uso se implementó en la vista (no en un middleware separado). El resto de middlewares descritos corresponden a la implementación actual.

---

## 4. Gestión de secretos

- `DJANGO_SECRET_KEY` se lee de variable de entorno (`.env.example` sin valor real).
- `.env` está en `.gitignore` y no se commitea.
- `SECRET_KEY` se persiste en `DATA_DIR/.secret_key` (permisos 0o600) si no se proporciona por variable de entorno.
- Las contraseñas y la frase de rescate se hashean con Argon2; nunca se escriben en logs.
- Las frases de rescate se muestran una sola vez (sesión efímera) y se invalidan tras uso.
- La clave privada de firma Ed25519 nunca se almacena en el repositorio ni en la base de datos; se suministra externamente en el entorno de publicación.

---

## 5. Seguridad de la distribución de conocimiento (Fase 2)

La rama `docs/phase-2-hybrid-knowledge-sync` incorpora:

- **Verificador de manifiesto firmado:** `verify_signed_manifest()` valida JSON estricto, firma Ed25519 detached, `key_id` resuelto contra claves públicas de confianza, canal, secuencia anti-replay (monotónica), SemVer, fecha ISO-8601, URL HTTPS en allowlist, hash y tamaño.
- **Validador de ZIP:** `validate_package_archive()` verifica el paquete en memoria sin extraer rutas externas. Comprueba índice, recursos declarados, SHA-256, límites de tamaño/compresión, rechaza rutas absolutas, traversal, barras invertidas, directorios, enlaces simbólicos, tipos especiales, nombres duplicados, archivos no declarados, hashes/tamaños incorrectos y UUID repetidos.
- **Registro local de paquetes:** `PaqueteConocimientoInstalado` con transiciones controladas, identidad inmutable, un solo activo por canal, protección contra eliminación física y actualización masiva.
- **Estado de sincronización:** `EstadoSincronizacion` por canal (última comprobación, éxito, ETag, error).

### Límites del validador de paquetes

| Control | Límite |
|---|---|
| Manifiesto JSON | 64 KiB |
| Firma Base64 | 256 bytes |
| Paquete ZIP | 100 MiB |
| Entradas totales | 501 (índice + 500 lecciones) |
| Índice JSON | 1 MiB |
| Documento de lección | 2 MiB |
| Contenido descomprimido total | 100 MiB |
| Ratio de compresión por entrada | 100:1 |

---

## 6. Riesgos conocidos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Backups trasladados sin cifrado | RS-008 (propuesto): documentar y ofrecer cifrado en futuro |
| LUKS solo protege en reposo (dispositivo apagado) | Documentado (RS-015); backups en otro dispositivo no están automáticamente protegidos |
| RAM limitada (~1.3 GB libre) | Django 1 worker, sin DEBUG, batch en PDFs (futuro) |
| Bloqueo de intentos (N indefinido) | Pendiente decisión del propietario (RF-006 / RS-017) |
| Clave privada de firma expuesta | Suministrada externamente, nunca en repositorio ni BD |
| Paquete ZIP malicioso | Validación de límites, traversal, symlinks antes de activar |
| Downgrade/replay de manifiesto | Control de secuencia monotónica por canal |

---

## 7. Reglas operativas de seguridad

- No ejecutar commits, tags ni cambios de rama sin autorización expresa.
- No modificar `data/db.sqlite3` ni datos reales.
- No copiar ni exponer `.env`, `data/.secret_key` ni credenciales.
- Comprobar `git status --porcelain=v1` y `git diff --cached` antes de cualquier operación de staging.
- No alterar los 12 temas visuales sin autorización y verificación de contraste.
- No introducir secretos en la documentación ni en el código.