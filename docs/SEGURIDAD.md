# CodeGuard Pro — Seguridad

**Producto:** CodeGuard Pro  
**Versión:** 1.0 (MVP, primer incremento)  
**SRS de referencia:** `IEEE830(1).md` v2.0 — Sección 3.5 (RS-001 a RS-020)

---

## 1. Principios

La seguridad es un requisito fundamental. La aplicación está diseñada bajo el modelo de
confianza cero para el entorno local: solo el usuario legítimo tiene acceso, todo pasa por
autenticación, y no se asume que la red local es segura.

---

## 2. Requisitos de seguridad implementados (incremento 1)

| ID | Requisito | Cómo se implementa | Estado |
|---|---|---|---|
| RS-001 | Autenticación local obligatoria | Todas las vistas requieren login cuando `AUTH_DISABLED = False`. Temporalmente desactivado (`AUTH_DISABLED = True`): la aplicación abre directamente el panel principal sin credenciales. La implementación original se conserva y puede reactivarse. Ver `docs/MODO_SIN_AUTENTICACION.md`. | ⚠️ Temporalmente desactivado |
| RS-002 | Argon2 para contraseñas | `AUTH_PASSWORD_HASHERS` con Argon2 primero | ✅ |
| RS-003 | Frase de rescate ≥128 bits, hash, un uso | `generar_frase_rescate()` (32 caracteres, ~201 bits), hash Argon2, `usada`. La frase **no se consume al validar**: solo se invalida al completar exitosamente el cambio de contraseña (flujo atómico en `cambiar_contrasena_por_frase`). | ✅ |
| RS-004 | Bind 127.0.0.1 | Servidor WSGI local (Waitress) en `127.0.0.1:<puerto>`; `ALLOWED_HOSTS` solo localhost | ✅ |
| RS-005 | Validación de archivos | Pendiente (incremento de evidencias) | ⏳ |
| RS-006 | Archivos fuera de web root | Pendiente (incremento de evidencias) | ⏳ |
| RS-007 | Backup íntegro (hash + validación) | Pendiente (incremento de backups) | ⏳ |
| RS-008 | Cifrado de backup | Propuesto, no aprobado | ⏳ |
| RS-009 | Timeout de sesión probado | Middleware `SesionInactividadMiddleware` (15 min defecto). La comprobación de expiración se realiza **antes** de ejecutar la vista; los recursos estáticos y multimedia no renuevan la sesión. | ✅ |
| RS-010 | CSRF | `CsrfViewMiddleware` + token en forms | ✅ |
| RS-011 | XSS | Escape de salida en plantillas + CSP | ✅ |
| RS-012 | SQLi | ORM de Django (consultas parametrizadas) | ✅ |
| RS-013 | Cabeceras de seguridad | `CabecerasSeguridadMiddleware` (CSP, X-Frame, etc.) | ✅ |
| RS-014 | Auditoría de eventos | `AuditLog` + `registrar_evento()` en servicios | ✅ |
| RS-015 | Documentar límites de LUKS | En este documento y `docs/INSTALACION.md` | ✅ |
| RS-016 | Política de contraseñas | Mínimo 8 caracteres en `SetupInicialForm` | ✅ |
| RS-017 | Bloqueo N intentos | 5 intentos fallidos consecutivos bloquean la cuenta 15 min (`intentos_fallidos`, `bloqueado_hasta` en `Usuario`). Reinicio tras login exitoso. Registro de intentos y bloqueos en auditoría (`acceso_denegado`). Mensajes genéricos sin revelar existencia de usuario. | ✅ |
| RS-018 | Minimización de datos | Solo campos necesarios; sin telemetría | ✅ |
| RS-019 | Dependencias actualizadas | `requirements.txt` con versiones exactas | ✅ |
| RS-020 | Errores no expuestos | `DEBUG=False` por defecto; mensajes genéricos | ✅ |

---

## 3. Middlewares de seguridad

- **`SesionInactividadMiddleware`**: expira la sesión tras `sesion_timeout_minutos` de
  inactividad (RF-002, RS-009). La comprobación se realiza **antes** de delegar en la vista
  (`get_response`) para garantizar que una sesión vencida nunca ejecute operaciones protegidas.
  Los recursos locales (estáticos y medios) no renuevan la sesión. Registra evento
  `logout_inactividad` en auditoría.
- **`CabecerasSeguridadMiddleware`**: añade a cada respuesta `X-Frame-Options: DENY`,
  `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Permissions-Policy`
  restrictiva y una CSP estricta (solo recursos propios, sin CDN; scripts locales sin
  `unsafe-inline`, estilos con `unsafe-inline` por uso de estilos inline).
- **Redirección de configuración inicial**: implementada en la vista `apps.accounts.setup_inicial`;
  si no existe usuario, redirige a `/accounts/setup/`.

> Nota: la redirección de primer uso se implementó en la vista (no en un middleware separado).
> El resto de middlewares descritos corresponden a la implementación actual.

---

## 4. Gestión de secretos

- `DJANGO_SECRET_KEY` se lee de variable de entorno (`.env.example` sin valor real).
- `.env` está en `.gitignore` y no se commitea.
- Las contraseñas y la frase de rescate se hashean con Argon2; nunca se escriben en logs.
- Las frases de rescate se muestran una sola vez (sesión efímera) y se invalidan tras uso.

---

## 5. Riesgos conocidos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Backups trasladados sin cifrado | RS-008 (propuesto): documentar y ofrecer cifrado en futuro |
| LUKS solo protege en reposo (dispositivo apagado) | Documentado (RS-015); backups en otro dispositivo no están automáticamente protegidos |
| RAM limitada (~1.3 GB libre) | Django 1 worker, sin DEBUG, batch en PDFs (futuro) |
| Bloqueo de intentos (N indefinido) | Pendiente decisión del propietario (RF-006 / RS-017) |

---

## 6. Pruebas de seguridad pendientes

Ver `docs/PLAN_PRUEBAS.md` (CSRF, XSS, validación de archivos, acceso no autorizado,
path traversal, archivos maliciosos, exposición de secretos).

---

### Autenticación temporalmente desactivada

El sistema de autenticación (RS-001, RS-003, RS-009, RS-010, RS-017 y relacionados)
está **temporalmente desactivado** (`AUTH_DISABLED = True`). No se han eliminado
modelos, migraciones ni datos. La implementación original se conserva íntegramente
y puede reactivarse con autorización expresa del propietario del proyecto.
Ver `docs/MODO_SIN_AUTENTICACION.md`.
