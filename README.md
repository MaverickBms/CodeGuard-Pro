# 🛡️ CodeGuard Pro

> **Tu formación técnica, siempre offline y siempre tuya.**

**CodeGuard Pro** es una plataforma educativa personal, local y **offline-first** que organiza tu roadmap de aprendizaje, gestiona etapas y lecciones, registra tu progreso verificado y documenta tus evidencias.

El núcleo corre en tu propio equipo: un servidor **Django** local + una aplicación de escritorio **Electron**, con **SQLite**. CodeGuard es **offline-first**: no requiere Internet para abrir la aplicación, estudiar con el contenido disponible ni consultar el progreso local.

El roadmap ASCENSO 3.1 (33 etapas) ya está implementado y cargable mediante `python manage.py cargar_ascenso`. El proyecto también incorpora bases funcionales de tutoría IA local (Ollama), evaluaciones, gamificación, mundo/avatar y desafíos; consulta el plan maestro en la rama `documentation` para distinguir lo implementado de lo que sigue en progreso. El flujo editorial de conocimiento versionado (fuentes, snapshots, referencias, envío a revisión, aprobación, publicación, sustitución y retirada) está implementado mediante comandos de gestión (`crear_version_leccion`, `gestionar_version_leccion`, `registrar_fuente_conocimiento`, `revisar_licencia_fuente`). El registro local de paquetes de conocimiento y el verificador de distribución firmada (Ed25519) están implementados (`PaqueteConocimientoInstalado`, `EstadoSincronizacion`, `validate_package_archive`, `verify_signed_manifest`).

La auditoría QA integral del 16-11-2026 mantiene pendientes la instalación limpia, la portabilidad y la aceptación E2E de escritorio (ver informe QA en la rama `documentation`). La recuperación de datos ya está implementada con creación, verificación, restauración transaccional y rollback.

El cliente de sincronización pull-only por HTTPS, el comando `sincronizar_conocimiento`, el publicador local y la integración de comprobaciones periódicas con Electron están implementados. **La distribución remota de producción sigue pendiente**: no hay hosting/endpoint público, allowlist ni claves públicas de producción configuradas. Sin esa configuración, el cliente falla cerrado y no realiza conexiones. No se contempla subir progreso, intentos, código ni datos personales del estudiante.

> **Documentación extendida:** la documentación técnica detallada (arquitectura, ADRs, planes, seguridad, modelo de datos, informes QA, etc.) se mantiene en la rama [`documentation`](https://github.com/MaverickBms/CodeGuard-Pro/tree/documentation). La rama `main` se centra en el código y la operación del proyecto.

---

## 📖 Manual de uso

### 1. Primer arranque y apertura de la aplicación

Al abrir la aplicación se inicia directamente en el **panel principal**.
No se solicita usuario ni contraseña. El sistema de autenticación está
**temporal y opcionalmente desactivado** para uso local directo (ver detalles en la rama `documentation`).

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
- Marcado de lecciones y de etapas completas con **recalculo automático de porcentaje**.
- Bloqueo de etapas cuyos prerrequisitos no estén completados.

### 4. Evaluaciones y evidencias

- **Evaluaciones:** índice de quizzes y exámenes publicados de la ruta activa,
  con etapa, módulo, umbral, número de preguntas y estado del último intento.
- **Evidencias:** portafolio local de criterios de finalización registrados y
  lista de criterios obligatorios pendientes, con enlace a la etapa.
- Las evidencias de proyecto/manual son declaraciones del estudiante; las
  evaluaciones automáticas se califican por separado.

### 5. Temas visuales

12 temas con las 12 paletas oficiales (P01–P12): claro (P01), oscuro (P02),
alto contraste (P04), retro-pixel (P05), cyberpunk (P03), fantasía (P07),
ciencia ficción (P08), guerrero (P06), mago (P09), pícaro (P10), paladín
(P11), oscuro mago (P12).

Cada tema usa variables CSS semánticas con los HEX originales sin modificar.
El texto es blanco/negro según la luminancia para garantizar **WCAG AA
(4.5:1)** en todos los pares de interfaz (texto/fondo, texto/superficie,
botones, bordes, focus). Se respeta `prefers-reduced-motion` y no se usa
`transition: all`.

### 6. Autenticación (temporalmente desactivada)

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
- El progreso se asocia al propietario local existente de la base de datos.
- La auditoría registra actor nulo (`usuario=None`).

Para reactivar la autenticación, cambie `AUTH_DISABLED` a `False` únicamente
con autorización expresa del propietario del proyecto. No se requieren migraciones
ni cambios de esquema.

---

## Estado de distribución (QA 16-11-2026)

El AppImage Linux x64 se compiló y verificó con un E2E sobre perfil temporal:
health check, cinco rutas HTTP 200, 12 temas, responsive, persistencia de tema
tras reiniciar y cierre sin procesos huérfanos. El job `windows-package` de CI
ejecutó la aceptación automatizada completa (instalación NSIS, primer arranque,
health, persistencia de tema y progreso, cierre, desinstalación y portable) y
publicó el artefacto `codeguard-windows-x64`. **La aceptación manual en un
equipo Windows físico sigue pendiente**; CI no sustituye hardware real. No
distribuir como versión estable hasta completar esa matriz. Consulta
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
python manage.py migrate --settings=config.settings.development
python manage.py cargar_ascenso --settings=config.settings.development
npm start
```

Usa un directorio de datos aislado. Consulta la guía de instalación en la rama `documentation`. macOS todavía no está configurado ni validado.

Comandos de gestión disponibles:

| Comando | Propósito |
|---|---|
| `cargar_ascenso` | Carga o actualiza las 33 etapas del roadmap ASCENSO 3.1 |
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
└── .secret_key
```

## 🧠 Stack técnico

Electron + Django 5.2 LTS + SQLite + Argon2 + Waitress + WhiteNoise + Bootstrap/HTMX/SweetAlert2/FontAwesome locales. Dependencias adicionales: `cryptography` (verificación Ed25519 de manifiestos de conocimiento), `pyinstaller` + `pyinstaller-hooks-contrib` (empaquetado del servidor local). El procesamiento de PDF todavía no tiene una biblioteca activa en `requirements.txt`; se incorporará cuando exista un módulo funcional y se aprueben la licencia y el impacto en el tamaño de distribución.

## 🧪 Verificación

```bash
python manage.py check --settings=config.settings.development
python manage.py makemigrations --check --dry-run --settings=config.settings.development
python manage.py test apps.core apps.accounts apps.audit apps.roadmaps apps.tutoring apps.gamification apps.challenges --settings=config.settings.development
```

Resultado verificado en este repositorio (19-11-2026): **292 pruebas OK** en
`apps.core`, `apps.accounts`, `apps.audit`, `apps.roadmaps`, `apps.tutoring`,
`apps.gamification` y `apps.challenges`, con
`--settings=config.settings.development` (system check 0 incidencias y
migraciones al día). Las pruebas incluyen restauración de backups, cabeceras
CSP, contraste WCAG de los 12 temas e índices de evaluaciones/evidencias.
`npm run test:electron` ejecuta las 20 pruebas de IPC, restauración y
persistencia de tema de escritorio. Las cifras históricas de 245/197/138 quedan sustituidas por esta
línea base reproducible. El inventario académico y los hallazgos editoriales
están en [docs/ROADMAP_ASCENSO_INVENTARIO.md](docs/ROADMAP_ASCENSO_INVENTARIO.md).

## ❓ Solución de problemas

- El panel se abre directamente sin solicitar credenciales (autenticación desactivada).
- El roadmap muestra "El roadmap todavía no está cargado" → ejecute `python manage.py cargar_ascenso`.
- Para reactivar el inicio de sesión, cambie `AUTH_DISABLED` a `False` en `config/settings/base.py` (requiere autorización expresa).

## 🤝 Contribuir · 🛡️ Seguridad · 📄 Licencia

- [Guía para contribuir](CONTRIBUTING.md)
- [Instalación y uso en Windows](README_WINDOWS.md)
- [Licencia](LICENSE)

La documentación técnica extendida (índice, arquitectura, estructura del repositorio, seguridad, modelo de datos, planes, pruebas y manual extendido) se encuentra en la rama [`documentation`](https://github.com/MaverickBms/CodeGuard-Pro/tree/documentation).

---

*CodeGuard Pro — con cimientos técnicos sólidos, funcionales, seguros, comprobables y preparados para evolucionar.*


### Continuidad ASCENSO 3.1 — etapa 9

La documentación de la etapa 9 (Bases de datos relacionales y SQL) quedó desglosada en 81 encabezados de lección, distribuidos en sus siete módulos según el roadmap oficial. Incluye fundamentos, modelado, MySQL, SQL, normalización, temas avanzados y PostgreSQL. Es una base de trabajo activa: los ejemplos y laboratorios no se consideran ejecutados ni aprobados por este cambio.


### Continuidad ASCENSO 3.1 — etapa 10

La documentación de la etapa 10 (Bases de datos NoSQL y almacenamiento moderno) quedó desglosada en 38 encabezados de lección, distribuidos en sus cuatro módulos según el roadmap oficial. Se mantienen las distinciones entre modelos, consistencia, MongoDB, Redis y otras arquitecturas, junto con el proyecto híbrido. Es base de trabajo activa; los laboratorios no se declaran ejecutados ni aprobados.


### Continuidad ASCENSO 3.1 — etapas 11 a 13

Se añadieron encabezados individuales para las 212 lecciones oficiales de las etapas 11–13: etapa 11 (60), etapa 12 (89) y etapa 13 (63). El desglose conserva la secuencia y los títulos del roadmap, y se apoya en las explicaciones, proyectos, autoevaluaciones y referencias presentes en cada documento. Es base de trabajo activa; no equivale a evaluación formal, ejecución de laboratorios, aprobación editorial ni publicación.


### Continuidad ASCENSO 3.1 — etapas 14 a 16

Se incorporaron encabezados individuales para las 157 lecciones oficiales de las etapas 14–16: etapa 14 (58), etapa 15 (53) y etapa 16 (46). El desglose organiza los contenidos de Java/Spring Boot, Node.js/NestJS, PHP/Laravel y .NET según el roadmap. Es base de trabajo activa; no equivale a ejecución de laboratorios, aprobación editorial ni publicación.


### Continuidad ASCENSO 3.1 — etapas 17 a 19

Se incorporaron encabezados individuales para las 228 lecciones oficiales de las etapas 17–19: etapa 17 (61), etapa 18 (100) y etapa 19 (67). El desglose cubre calidad y testing, arquitectura y diseño, y DevOps/infraestructura según el roadmap. Es base de trabajo activa; no se declara ejecución de pruebas, pipelines ni despliegues.


### Continuidad ASCENSO 3.1 — etapas 20 a 22

Se incorporaron encabezados individuales para las 197 entradas oficiales de las etapas 20–22: etapa 20 (57), etapa 21 (82) y etapa 22 (58). Se mantuvieron las restricciones de laboratorio propio, aislado y autorizado. Es base de trabajo activa; no se declara ejecución de máquinas virtuales, pruebas ofensivas ni laboratorios.


### Continuidad ASCENSO 3.1 — etapas 23 a 25

Se incorporaron encabezados individuales para las 155 entradas curriculares de las etapas 23–25: etapa 23 (58), etapa 24 (47) y etapa 25 (50). Se mantienen las condiciones de autorización y alcance para laboratorios; el objetivo oficial vacío de la etapa 25 no fue alterado ni completado. Es base de trabajo activa, sin ejecución de herramientas ni aprobación editorial.


### Continuidad ASCENSO 3.1 — etapas 26 a 28

Se incorporaron encabezados individuales para las 143 entradas oficiales de las etapas 26–28: etapa 26 (39), etapa 27 (58) y etapa 28 (46). El desarrollo mantiene el enfoque defensivo, de monitoreo, respuesta y preservación de evidencia. Es base de trabajo activa; no se declara conexión a entornos empresariales ni ejecución de herramientas forenses o SIEM.


### Continuidad ASCENSO 3.1 — etapas 29 a 32

Se incorporaron encabezados individuales para las 275 entradas oficiales de las etapas 29–32: etapa 29 (71), etapa 30 (75), etapa 31 (75) y etapa 32 (54). Se preservaron las restricciones de seguridad cloud, pruebas autorizadas de IA y análisis aislado de malware. Es base de trabajo activa; no se declaran despliegues, análisis prácticos ni resultados laborales no realizados.


## Cierre de continuidad ASCENSO 3.1 — 24-11-2026

Se completó la pasada de continuidad documental de las 32 etapas posteriores a la etapa 0. Las etapas 11–32 cuentan con encabezados granulares por cada entrada oficial del roadmap y sus conteos se cotejaron por etapa. Esto completa la organización documental de las etapas, no la redacción profunda de las 1.916 lecciones nominales de las etapas 1–32: aún deben ampliarse teoría, ejemplos, ejercicios, referencias y evidencias prácticas. El JSON curricular permanece intacto; la etapa 25 conserva su objetivo vacío. No se importó, aprobó ni publicó contenido.


### Desarrollo profundo y revisión editorial — etapas 1 a 10

Se revisaron editorialmente los documentos de las etapas 1–10 y se cotejaron sus encabezados con el roadmap: 549/549 entradas curriculares coinciden por módulo. Se corrigieron duplicaciones, referencias impropias, orden de lecciones, compatibilidad JDK 21 y advertencias operativas. La revisión es documental interna; los ejemplos y laboratorios siguen pendientes de ejecución reproducible y segunda revisión académica. Los contenidos permanecen como base de trabajo activa, sin aprobación ni publicación.


### Desarrollo profundo individual — etapas 11 a 13

Se desarrollaron individualmente las 212 lecciones oficiales de las etapas 11–13 (60, 89 y 63 respectivamente), sustituyendo textos genéricos por explicaciones técnicas específicas, límites y criterios de aplicación. Se cotejó la cobertura con el roadmap y se comprobó que no quedaran los placeholders de granularización. Las pruebas frontend, accesibilidad, APIs y despliegue siguen pendientes; revisión interna documental, no aprobación externa.


### Desarrollo profundo individual — etapas 14 a 16

Se desarrollaron individualmente las 157 lecciones oficiales de Java/Spring Boot, Node.js/NestJS y PHP/Laravel/.NET (58, 53 y 46). Se cotejó su cobertura con el roadmap y se eliminaron las orientaciones genéricas. Compilaciones, pruebas, migraciones y laboratorios de seguridad siguen pendientes; revisión documental interna, no aprobación externa.


### Desarrollo profundo individual — etapas 17 a 19

Se desarrollaron individualmente las 228 lecciones oficiales de testing/calidad, arquitectura/diseño y DevOps/infraestructura (61, 100 y 67). Se cotejaron los encabezados con el roadmap y se eliminaron orientaciones genéricas. Pruebas, pipelines, despliegues y laboratorios siguen pendientes; revisión documental interna, no aprobación externa.


### Desarrollo profundo individual — etapas 20 a 22

Se desarrollaron individualmente las 197 lecciones oficiales de AppSec, fundamentos de ciberseguridad/riesgos/ética y laboratorio/hardening (57, 82 y 58). Se verificó OWASP Top 10:2025 en su fuente oficial y se añadieron fuentes normativas colombianas con advertencia de vigencia. Las pruebas AppSec y laboratorios siguen pendientes; revisión documental interna, no aprobación externa.


### Desarrollo profundo individual — etapas 23 a 25

Se desarrollaron individualmente las 155 lecciones oficiales de OSINT/reconocimiento, pentesting y seguridad web/APIs (58, 47 y 50). Se cotejaron conteos con el roadmap y se eliminaron textos genéricos. Las prácticas se limitan a entornos propios/autorizados; el objetivo oficial vacío de etapa 25 permanece intacto. No se ejecutaron escaneos ni se declara aprobación externa.


### Desarrollo profundo individual — etapas 26 a 28

Se desarrollaron individualmente las 143 lecciones oficiales de Active Directory, Blue Team/SOC/SIEM y Threat Hunting/DFIR (39, 58 y 46). Se cotejaron conteos con el roadmap y se eliminaron textos genéricos. Las validaciones prácticas en dominios y laboratorios aislados siguen pendientes; revisión documental interna, no aprobación externa.


### Desarrollo profundo individual — etapas 29 a 32

Se desarrollaron individualmente las 275 lecciones oficiales de cloud/DevSecOps, IA/automatización/criptografía, bajo nivel/malware y portafolio profesional (71, 75, 75 y 54). Se cotejaron los conteos con el roadmap y se eliminaron textos genéricos. Laboratorios, despliegues y proyectos verificables siguen pendientes; revisión documental interna, no aprobación externa.


### Estado consolidado de desarrollo individual — 24-11-2026

Se completó la primera pasada de desarrollo individual de las 1.916 entradas nominales de las etapas 1–32 (549 en etapas 1–10 y 1.367 en etapas 11–32). Se registraron revisiones editoriales internas por bloque y se cotejó la correspondencia curricular. Esta fase cubre redacción individual inicial y revisión documental; no equivale a aprobación final. Siguen pendientes el cotejo bibliográfico completo, la ejecución reproducible de ejemplos/laboratorios, las pruebas de accesibilidad/seguridad y la revisión técnica-pedagógica independiente. El JSON curricular no se modificó y el objetivo de etapa 25 permanece vacío. No se importó ni publicó contenido.


### Profundización didáctica por lección — etapa 7 (24-11-2026)

Se completó una profundización documental de las 84 lecciones de la etapa 7: fundamentos de sistemas operativos (14), Linux (17), administración Linux (20), Bash (12), Windows (12) y virtualización (9). Cada lección contiene explicación específica, práctica guiada, actividad independiente, criterios de aceptación y comprobación; además se incorporan ejemplos, escenarios y precauciones operativas según el tema.

Este resultado es una revisión y profundización documental interna. No significa que las prácticas se hayan ejecutado en máquinas virtuales ni que las lecciones estén validadas técnicamente por terceros. Permanecen pendientes la ejecución con evidencia, verificación bibliográfica completa y revisión experta independiente. La auditoría de continuidad contiene el alcance y las limitaciones detalladas. No se modificó el JSON oficial, no se importó ni publicó contenido.
