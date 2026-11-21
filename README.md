# 🛡️ CodeGuard Pro

> **Tu formación técnica, siempre offline y siempre tuya.**

**CodeGuard Pro** es una plataforma educativa personal, local y **offline-first** que organiza tu roadmap de aprendizaje, gestiona etapas y lecciones, registra tu progreso verificado y documenta tus evidencias.

El núcleo corre en tu propio equipo: un servidor **Django** local + una aplicación de escritorio **Electron**, con **SQLite**. CodeGuard es **offline-first**: no requiere Internet para abrir la aplicación, estudiar con el contenido disponible ni consultar el progreso local.

El roadmap ASCENSO 3.1 (33 etapas) se instala automáticamente en el primer arranque y se verifica sin reconstruirse en los siguientes. La aplicación incluye panel, roadmap, lecciones, evaluaciones, evidencias, biblioteca documental de PDFs, tutoría IA local (Ollama), gamificación, base de conocimiento de solo lectura y copias de seguridad. Consulta el plan maestro en la rama `documentation` para distinguir lo implementado de lo que sigue en progreso. El flujo editorial de conocimiento versionado (fuentes, snapshots, referencias, envío a revisión, aprobación, publicación, sustitución y retirada) está implementado mediante comandos de gestión (`crear_version_leccion`, `gestionar_version_leccion`, `registrar_fuente_conocimiento`, `revisar_licencia_fuente`). El registro local de paquetes de conocimiento y el verificador de distribución firmada (Ed25519) están implementados (`PaqueteConocimientoInstalado`, `EstadoSincronizacion`, `validate_package_archive`, `verify_signed_manifest`).

La iteración de finalización del 21-11-2026 validó el perfil limpio, el arranque, los formularios CSRF dentro de Electron, la biblioteca PDF, el benchmark de rendimiento y la restauración transaccional. La aceptación en hardware Windows físico sigue pendiente. El detalle está en [docs/INFORME_FINAL_1.0.0.md](docs/INFORME_FINAL_1.0.0.md).

El cliente de sincronización pull-only por HTTPS, el comando `sincronizar_conocimiento`, el publicador local y la integración de comprobaciones periódicas con Electron están implementados. **La distribución remota de producción sigue pendiente**: no hay hosting/endpoint público, allowlist ni claves públicas de producción configuradas. Sin esa configuración, el cliente falla cerrado y no realiza conexiones. No se contempla subir progreso, intentos, código ni datos personales del estudiante.

> **Documentación extendida:** la documentación técnica detallada (arquitectura, ADRs, planes, seguridad, modelo de datos, informes QA, etc.) se mantiene en la rama [`documentation`](https://github.com/MaverickBms/CodeGuard-Pro/tree/documentation). La rama `main` se centra en el código y la operación del proyecto.

---

## 📖 Manual de uso

### 1. Primer arranque y apertura de la aplicación

Al abrir la aplicación se inicia directamente en el **panel principal**.
No se solicita usuario ni contraseña. El sistema de autenticación está
**temporal y opcionalmente desactivado** para uso local directo (ver detalles en la rama `documentation`).

En un perfil limpio, el arranque crea una sola vez el **propietario local**
necesario para asociar progreso, intentos y evidencias. No crea credenciales de
acceso ni reactiva el login. El primer arranque aplica las migraciones e instala
ASCENSO 3.1; los siguientes verifican la integridad y reutilizan el contenido.

El sistema completo de autenticación (usuario, contraseña maestra, frase de
rescate, bloqueo por intentos y cierre de sesión) se **conserva íntegro** en el
código, modelos y migraciones, y puede reactivarse con autorización expresa
del propietario del proyecto.

### 2. Panel principal

Dashboard con resumen de progreso real del roadmap (etapas, módulos y
lecciones completadas), próxima actividad sugerida, actividad reciente,
módulos del MVP y estado del sistema. Todos los datos provienen de la base de
datos.

### 3. Roadmap ASCENSO

- Listado de las **33 etapas** oficiales con filtros (bloque, prioridad, búsqueda).
- Detalle de etapa: módulos, lecciones, proyecto, criterios, prerrequisitos.
- Progreso de lecciones mediante evidencias de ejercicios aprobados.
- Etapas completadas únicamente al cumplir sus criterios verificables.
- Bloqueo de etapas cuyos prerrequisitos no estén completados.

### 4. Evaluaciones y evidencias

- **Evaluaciones:** índice de quizzes y exámenes publicados de la ruta activa,
  con etapa, módulo, umbral, número de preguntas y estado del último intento.
- **Evidencias:** portafolio local de criterios de finalización registrados y
  lista de criterios obligatorios pendientes, con enlace a la etapa.
- Las evidencias de proyecto/manual son declaraciones del estudiante; las
  evaluaciones automáticas se califican por separado.

### 5. Biblioteca documental

- Importación de PDFs con validación de extensión, firma `%PDF-`, tamaño
  máximo de 50 MB y SHA-256; los duplicados se rechazan.
- Metadatos editables (título, autor, categoría, descripción y etiquetas),
  búsqueda, filtros, paginación y archivo/restauración.
- Visor PDF integrado con soporte de rangos HTTP. El archivo se sirve desde el
  servidor local y nunca se envía a Internet.
- Los PDFs se guardan en `media/biblioteca/` dentro del perfil del usuario y se
  incluyen en las copias de seguridad.

### 6. Temas visuales

12 temas con las 12 paletas oficiales (P01–P12): claro (P01), oscuro (P02),
alto contraste (P04), retro-pixel (P05), cyberpunk (P03), fantasía (P07),
ciencia ficción (P08), guerrero (P06), mago (P09), pícaro (P10), paladín
(P11), oscuro mago (P12).

Cada tema usa variables CSS semánticas con los HEX originales sin modificar.
El texto es blanco/negro según la luminancia para garantizar **WCAG AA
(4.5:1)** en todos los pares de interfaz (texto/fondo, texto/superficie,
botones, bordes, focus). Se respeta `prefers-reduced-motion` y no se usa
`transition: all`.

### 7. Autenticación (temporalmente desactivada)

El flujo de autenticación original queda preservado y no se ha eliminado:

- Configuración inicial de usuario y contraseña maestra.
- Inicio de sesión con contraseña maestra (Argon2).
- Cierre de sesión (POST, CSRF).
- Recuperación mediante frase de rescate (un solo uso).
- Cambio de contraseña autenticado.
- Bloqueo tras 5 intentos fallidos (15 minutos) y reinicio tras éxito.
- Auditoría de eventos de acceso.

Mientras `AUTH_DISABLED = True` en `config/settings/base.py`:

- La aplicación abre directamente el panel principal.
- No se muestran pantallas de login, registro, rescate ni cambio de contraseña.
- El botón "Cerrar sesión" no aparece en la navegación.
- Las rutas de autenticación redirigen al panel principal (HTTP 302).
- El progreso se asocia al propietario local creado o reutilizado en el arranque.
- La auditoría registra actor nulo (`usuario=None`).

Para reactivar la autenticación, cambie `AUTH_DISABLED` a `False` únicamente
con autorización expresa del propietario del proyecto. No se requieren migraciones
ni cambios de esquema.

---

## Estado de distribución (QA 21-11-2026)

El AppImage Linux x64 se compiló y verificó con un E2E sobre perfil temporal:
health check, siete rutas HTTP 200 (incluye Biblioteca y Base de conocimiento),
12 temas, responsive a 1024/768 px, formulario real de importación PDF con
CSRF, visor PDF, persistencia de tema al reiniciar y cierre sin procesos
huérfanos ni puertos abiertos. El arranque normal medido fue ~2,8 s con
Electron y ~1,2 s para el servidor empaquetado; el primer arranque ~13–16 s según carga.

El job `windows-package` de CI ejecuta la aceptación automatizada (instalación
NSIS, primer arranque, health, persistencia de tema y progreso, cierre,
desinstalación y portable) y publica `codeguard-windows-x64`. **La aceptación
manual en un equipo Windows físico sigue pendiente**; CI no sustituye hardware
real. No distribuir como versión estable hasta completar esa matriz. Consulta
[docs/INFORME_FINAL_1.0.0.md](docs/INFORME_FINAL_1.0.0.md),
[docs/PROJECT_EXECUTION_STATUS.md](docs/PROJECT_EXECUTION_STATUS.md) y el
informe QA de la rama `documentation`.

## ⚡ Instalación rápida

### Windows

```bat
build_windows.bat
```

Genera el servidor Django (PyInstaller) + instalador Electron (NSIS / portable).

### Linux x64 (entorno de desarrollo; no es instalador de usuario)

```bash
git clone https://github.com/MaverickBms/CodeGuard-Pro.git
cd CodeGuard-Pro
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
npm ci
export CODEGUARD_DATA_DIR="$PWD/.local-data"
npm start
```

`npm start` usa el mismo `server_entry.py` que el paquete: aplica migraciones,
crea el propietario local, instala ASCENSO 3.1 y verifica la integridad en los
arranques posteriores. Para generar el AppImage: `npm run build:linux`.

Usa un directorio de datos aislado. Consulta la guía de instalación en la rama `documentation`. macOS todavía no está configurado ni validado.

Comandos de gestión disponibles:

| Comando | Propósito |
|---|---|
| `cargar_ascenso` | Carga o actualiza las 33 etapas del roadmap ASCENSO 3.1 |
| `verificar_perfil` | Verifica la integridad del roadmap instalado sin modificar el perfil |
| `crear_version_leccion` | Genera un snapshot versionado borrador de una lección |
| `gestionar_version_leccion` | Envía, aprueba, publica o retira una versión de contenido |
| `importar_paquete_contenido` | Importa un lote validado como borradores editoriales |
| `registrar_fuente_conocimiento` | Registra una fuente documental para el flujo editorial |
| `revisar_licencia_fuente` | Registra una decisión editorial auditada sobre la licencia de una fuente |
| `validar_paquete_contenido` | Valida un lote JSON académico sin escribir en la base de datos |
| `publicar_paquete_conocimiento` | Genera localmente un paquete reproducible, manifiesto y firma Ed25519 desde contenido editorial publicado |
| `sincronizar_conocimiento` | Comprueba y descarga actualizaciones firmadas desde un endpoint HTTPS configurado |
| `crear_backup --output RUTA.zip` | Crea una copia ZIP verificada de la base local y `media/` |
| `verificar_backup RUTA.zip` | Verifica estructura, hashes e integridad SQLite de una copia |
| `restaurar_backup RUTA.zip --confirm` | Restaura base y `media/` con validación previa y rollback |

### Copias de seguridad y restauración

La pantalla **Backups** permite crear una copia verificada y volver a verificar
cualquier copia de la carpeta local. Las copias se guardan fuera del perfil de
datos, en `CodeGuard Backups/`, junto al directorio de datos de la aplicación.

La restauración está disponible con la aplicación cerrada:

- **Aplicación empaquetada:** menú **CodeGuard Pro → Restaurar copia de seguridad…**.
  La aplicación se detiene, restaura el ZIP, conserva una copia de reversión del
  perfil anterior y se reinicia.
- **Entorno de desarrollo:** `python manage.py restaurar_backup RUTA.zip --confirm`.

Desde la raíz del proyecto también puedes crear copias por CLI:

```bash
python manage.py crear_backup --output "$HOME/CodeGuard-backup.zip"
python manage.py verificar_backup "$HOME/CodeGuard-backup.zip"
```

El destino debe estar fuera de `CODEGUARD_DATA_DIR` y no existir previamente.
El formato incluye `db.sqlite3` como snapshot consistente y `media/`; excluye
`.secret_key` y logs. La restauración valida formato, hashes, integridad SQLite
y compatibilidad de esquema, rechaza versiones futuras y restaura en staging
antes de sustituir el perfil. Consulta
[el contrato y las pruebas pendientes de plataforma](https://github.com/MaverickBms/CodeGuard-Pro/blob/documentation/docs/BACKUPS_Y_RESTAURACION.md).

---

## 🌐 Funcionamiento offline y actualizaciones de conocimiento

- El servidor de la aplicación escucha únicamente en `127.0.0.1`.
- El contenido instalado y los datos del estudiante se conservan localmente.
- La conexión no es requisito para estudiar con los recursos descargados.
- El registro local de paquetes (`PaqueteConocimientoInstalado`) y el estado de sincronización por canal (`EstadoSincronizacion`) ya están implementados y verificados: transiciones controladas (`descargado → verificado → activo → rechazado → sustituido`), identidad inmutable (package_id, hashes, versión), un solo paquete activo por canal y restricción de secuencia única por canal.
- La Fase 2 contempla un servicio central que distribuirá paquetes académicos revisados y versionados mediante HTTPS.
- La sincronización será iniciada por el cliente, de solo descarga y no bloqueará el uso offline.
- Las actualizaciones deberán validar firma, integridad y compatibilidad antes de instalarse, con conservación de la versión anterior.
- El diseño no contempla enviar intentos, código, calificaciones, progreso ni datos personales al servidor central.
- **Estado actual:** registro local, verificador Ed25519, publicador local, instalador transaccional, rollback y cliente HTTP están implementados. Electron programa comprobaciones periódicas. La sincronización remota permanece inactiva hasta configurar endpoint, allowlist y claves públicas confiables; el hosting y la publicación remota de producción no están implementados.

## 🔒 Privacidad

- Servidor local en `127.0.0.1` (nunca `0.0.0.0`).
- CSP estricta, cabeceras de seguridad, `DEBUG=False`.
- Contraseñas y frases con Argon2, un solo uso.
- Recursos estáticos locales, sin CDN ni telemetría.
- Cualquier futura conexión de actualización se limitará a descargar conocimiento publicado y no habilitará acceso remoto a la aplicación local.

## 🗄️ Dónde están tus datos

```
<CODEGUARD_DATA_DIR>/
├── db.sqlite3
├── logs/
├── media/
│   └── biblioteca/
├── knowledge-packages/
├── ui-preferences.json
└── .secret_key
```

## 🧠 Stack técnico

Electron + Django 5.2 LTS + SQLite + Argon2 + Waitress + WhiteNoise + Bootstrap/HTMX/SweetAlert2/FontAwesome locales. Dependencias adicionales: `cryptography` (verificación Ed25519 de manifiestos de conocimiento), `pyinstaller` + `pyinstaller-hooks-contrib` (empaquetado del servidor local). La biblioteca PDF usa el visor integrado de Chromium y no añade librerías de parsing/OCR; su licencia y superficie de ataque quedan fuera de la distribución.

## 🧪 Verificación

```bash
python manage.py check --settings=config.settings.development
python manage.py makemigrations --check --dry-run --settings=config.settings.development
python manage.py test apps.core apps.accounts apps.audit apps.roadmaps apps.tutoring apps.gamification apps.challenges apps.library --settings=config.settings.development
python scripts/benchmark-startup.py
```

Resultado verificado en este repositorio (21-11-2026): **331 pruebas OK** en
`apps.core`, `apps.accounts`, `apps.audit`, `apps.roadmaps`, `apps.tutoring`,
`apps.gamification`, `apps.challenges` y `apps.library`, con
`--settings=config.settings.development` (system check 0 incidencias y
migraciones al día). Las pruebas incluyen restauración de backups, biblioteca
PDF, cabeceras CSP, contraste WCAG de los 12 temas e índices de
evaluaciones/evidencias. `npm run test:electron` ejecuta 24 pruebas de IPC,
arranque, restauración y persistencia de tema.

Rendimiento medido: primer arranque empaquetado ~12,6 s; segundo ~1,2 s en el
servidor y ~2,8 s con Electron. El segundo arranque verifica 1.946 lecciones sin
reconstruirlas. Detalle y metodología en
[docs/RENDIMIENTO_ARRANQUE.md](docs/RENDIMIENTO_ARRANQUE.md). El inventario
académico y los hallazgos editoriales están en
[docs/ROADMAP_ASCENSO_INVENTARIO.md](docs/ROADMAP_ASCENSO_INVENTARIO.md).

## ❓ Solución de problemas

- El panel se abre directamente sin solicitar credenciales (autenticación desactivada).
- Si el roadmap no aparece, ejecute `python manage.py verificar_perfil` y después
  `python manage.py cargar_ascenso`; el arranque normal también lo repara.
- Un PDF es rechazado → compruebe que termina en `.pdf`, que es un PDF real
  (firma `%PDF-`) y que no supera 50 MB. Los duplicados por SHA-256 se rechazan.
- El tutor muestra «no disponible» → Ollama no está en marcha o falta el modelo
  configurado. La aplicación usa pistas deterministas y sigue funcionando.
- La importación o un formulario devuelve 403 → no use `Referrer-Policy:
  no-referrer`; esta versión usa `same-origin` para que Chromium envíe un
  `Origin` válido en los POST locales.
- El AppImage se queda bloqueado al montar FUSE → ejecute
  `CODEGUARD_APPIMAGE_EXTRACT=1 ./run.sh`.
- Si usabas `./codeguard` antes de esta versión, `run.sh` detecta el perfil
  heredado en `Code Guard Pro/data` y lo conserva automáticamente.
- Para reactivar el inicio de sesión, cambie `AUTH_DISABLED` a `False` en
  `config/settings/base.py` (requiere autorización expresa). El propietario
  local creado sin credenciales necesitará un restablecimiento autorizado.

## 🤝 Contribuir · 🛡️ Seguridad · 📄 Licencia

- [Guía para contribuir](CONTRIBUTING.md)
- [Instalación y uso en Windows](README_WINDOWS.md)
- [Licencia](LICENSE)

La documentación técnica extendida (índice, arquitectura, estructura del repositorio, seguridad, modelo de datos, planes, pruebas y manual extendido) se encuentra en la rama [`documentation`](https://github.com/MaverickBms/CodeGuard-Pro/tree/documentation).

---

*CodeGuard Pro — con cimientos técnicos sólidos, funcionales, seguros, comprobables y preparados para evolucionar.*
