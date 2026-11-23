# Seguridad de CodeGuard Pro 1.0.0

**Fecha:** 2026-11-21
**Alcance:** aplicación local monousuario (Electron + Django + SQLite).
**Modelo de amenaza:** usuario local legítimo, contenido de terceros importado
(PDF, paquetes de conocimiento) y páginas web externas que intenten interactuar
con el servidor loopback. No se contempla un atacante con control físico o con
privilegios de sistema sobre el equipo.

## 1. Superficie de ataque

| Componente | Exposición |
|---|---|
| Waitress/Django | Solo `127.0.0.1`; puerto libre asignado por Electron |
| Electron renderer | Context isolation, sandbox, sin Node.js |
| IPC | Solo desde el origen HTTP exacto de la ejecución |
| Biblioteca | PDFs locales bajo `MEDIA_ROOT` |
| Backups | ZIP seleccionado por el usuario; validación previa |
| Tutor | Ollama en loopback; sin hosts remotos |
| Sincronización | HTTPS opt-in, allowlist y firma Ed25519; falla cerrada |

## 2. Identidad local y permisos

La autenticación permanece desactivada a propósito (`AUTH_DISABLED = True`):

- No hay login, sesión de usuario ni credenciales maestras en uso.
- El arranque resuelve un **propietario local explícito** mediante
  `Usuario.es_propietario_local`.
- Si hay varias cuentas activas y ninguna es inequívoca, no se selecciona ni se
  eleva ninguna. El perfil queda en lectura y los servicios de escritura
  rechazan operaciones.
- El nombre reservado heredado `propietario-local` se acepta como identidad
  explícita de compatibilidad.
- Cuando `AUTH_DISABLED=True`, la identidad de escritura proviene únicamente
  de `request.usuario_local`; una sesión Django heredada nunca se usa como
  respaldo si el propietario no puede resolverse.
- Solo el propietario marcado recibe `is_staff` para el flujo editorial local.
  Una cuenta ordinaria no se eleva por existir.
- El admin de Django no se instala en el paquete de escritorio.

**Limitación aceptada:** cualquier proceso del mismo usuario puede acceder a los
archivos del perfil. Esto es inherente a una aplicación local sin autenticación
de sistema operativo. No se declara protección frente a un usuario con control
del equipo.

## 3. Seguridad web

Implementado y probado:

- `ALLOWED_HOSTS` restringido a loopback.
- CSRF activo en todos los POST; `Referrer-Policy: same-origin` para que
  Chromium envíe un origen válido.
- CSP: `default-src 'self'`, `script-src 'self'`, `object-src 'none'`,
  `frame-ancestors` explícito; sin CDN.
- `X-Frame-Options: DENY` salvo el visor PDF del mismo origen.
- `X-Content-Type-Options: nosniff`.
- `Permissions-Policy` sin cámara, micrófono ni geolocalización.
- `Cache-Control: no-store` en páginas con datos.
- Cookies de sesión `HttpOnly` y `SameSite=Lax` por defecto de Django. En
  escritorio no hay TLS porque el canal es loopback; no se activa
  `SESSION_COOKIE_SECURE` para no romper el HTTP local.
- Mensajes y contenido académico escapados; el filtro `academico` escapa antes
  de convertir un subconjunto de Markdown.
- Plantillas sin scripts inline; scripts servidos localmente.
- Las respuestas de error no exponen rutas, SQL ni trazas al renderer.

## 4. Validación de entradas y archivos

- PDF: extensión `.pdf`, firma `%PDF-`, máximo 50 MB, nombre saneado y SHA-256.
- Duplicados por SHA-256 rechazados en la vista y protegidos por una restricción única condicional en SQLite; la base de datos cierra la carrera entre procesos.
- Si la restricción detecta un conflicto concurrente, se elimina el archivo escrito por el intento perdedor y se muestra un error de duplicado. Otros errores de integridad no se ocultan.
- El visor sirve únicamente rutas resueltas dentro de `MEDIA_ROOT`.
- Rangos HTTP validados; respuestas 416 con `Content-Range`.
- Respuestas de ejercicios limitadas a 20.000 caracteres.
- Evidencias limitadas a 5.000 caracteres.
- URLs de video solo HTTPS de YouTube, con ID válido.
- Fuentes/licencias con evidencia HTTPS y revisión auditada.
- Backups: ZIP sin rutas absolutas, `..`, enlaces simbólicos, cifrado ni
  duplicados; límites de entradas y tamaño; CRC, hashes y SQLite verificados.

## 5. Electron

- `contextIsolation: true`, `sandbox: true`, `nodeIntegration: false`.
- `preload.js` expone una API mínima; no expone `ipcRenderer` ni `require`.
- Cada canal IPC comprueba origen, host y puerto exactos.
- `setWindowOpenHandler` deniega ventanas nuevas.
- `will-navigate` solo permite el origen Django de la ejecución.
- Enlaces externos: solo HTTPS, sin credenciales, hash ni esquemas peligrosos.
- Restauración: ZIP regular, confirmación explícita, servidor detenido y
  reinicio.
- Cierre: termina el proceso Django y su grupo; no deja puertos ni procesos
  huérfanos en las pruebas realizadas.

## 6. Backups y restauración

- El backup se crea con snapshot consistente de SQLite.
- Se excluyen `.secret_key`, logs y WAL/SHM.
- El destino debe estar fuera del perfil y no existir previamente.
- Se verifica el ZIP completo antes de publicarlo.
- La restauración extrae a staging, valida esquema y publica con rollback.
- Se conserva una copia de reversión del perfil anterior.
- Se probó una restauración real sobre un perfil aislado y se comprobaron
  progreso, intentos y documento archivado.

## 7. Tutor y sincronización

- Ollama solo se acepta en `localhost`, `127.0.0.1` o `::1`, por HTTP y sin
  credenciales ni rutas adicionales.
- No se siguen redirecciones; se desactivan proxies.
- Timeout acotado y fallback determinista.
- El tutor no aprueba evaluaciones ni ejecuta código.
- La sincronización remota está desactivada por configuración ausente. Sin
  endpoint, allowlist y claves públicas, el proceso falla cerrado y no conecta.

## 8. Dependencias

| Comprobación | Resultado |
|---|---|
| `pip-audit -r requirements.txt` | Sin vulnerabilidades conocidas |
| `npm audit --omit=dev --audit-level=high` | 0 vulnerabilidades de producción |
| `npm audit` completo | 6 moderadas en la cadena de build de `electron-builder` |
| `pip check` | Sin conflictos |
| `manage.py check` | 0 incidencias |

Las 6 alertas moderadas de `npm audit` pertenecen a herramientas de empaquetado
(`electron-builder`/`minimatch`), no al runtime empaquetado. No se aplicó
`npm audit fix --force` porque propone una degradación no verificada. Queda como
riesgo de cadena de suministro de desarrollo, no de ejecución del producto.

## 9. Riesgos pendientes

1. **Sin sandbox de código:** no se ejecuta código del estudiante.
2. **Respuestas abiertas:** quedan pendientes de revisión; no se autoaprueban,
   pero no existe todavía una interfaz docente de revisión.
3. **Windows físico:** la seguridad del instalador se validó en CI, no en un
   equipo limpio.
4. **Sincronización remota:** no hay infraestructura de producción.
5. **Usuario con control del equipo:** puede modificar SQLite y archivos. El
   diseño no promete integridad frente al propietario del sistema operativo.
6. **Duplicados históricos de PDF:** la migración de unicidad comprueba los datos
   existentes y se detiene sin borrar documentos si detecta hashes repetidos; el
   propietario debe resolverlos conservando los archivos.
7. **Artefactos sin firma de código:** los hashes SHA-256 verifican integridad,
   pero no autentican al editor. Windows SmartScreen puede advertir. La firma
   Authenticode/AppImage queda pendiente.

## 10. Conclusión

No se encontraron vulnerabilidades críticas o altas sin mitigar en el alcance
local. Las protecciones existentes se conservaron y se reforzaron la identidad
local, la distinción de revisiones de video y el CI. Los riesgos residuales están
documentados y no se presentan como resueltos.
