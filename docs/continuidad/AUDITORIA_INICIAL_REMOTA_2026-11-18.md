# Auditoría inicial remota — CodeGuard Pro

**Fecha:** 2026-11-18 (Colombia)  
**Repositorio:** https://github.com/MaverickBms/CodeGuard-Pro  
**Rama inspeccionada:** `main`  
**HEAD remoto observado:** `59d08848726550fde442be1eb1e1be5522637f0b`  
**Rama de continuidad:** `docs/continuidad-beta-2026-11-18`  
**Alcance:** auditoría remota de estructura, documentación y archivos de configuración/código seleccionados. No equivale a una auditoría local ejecutada ni a aceptación beta.

> Esta revisión se realizó mediante acceso remoto a GitHub. Este entorno no dispone de un checkout local del propietario ni de su terminal, por lo que no puede observar `git status`, el diff local completo, las bases de datos locales, los artefactos empaquetados ni ejecutar comandos del proyecto. No se afirma que se hayan ejecutado pruebas o builds.

## 1. Identidad y propósito

CodeGuard Pro es una plataforma educativa personal, monousuario, local y offline-first para organizar el aprendizaje técnico. El flujo central previsto es roadmap ASCENSO, consulta de lecciones y documentación, ejercicios, evaluaciones, registro de intentos/evidencias, progreso y tutoría local opcional.

No debe convertirse en una plataforma web multiusuario ni reconstruirse con otra arquitectura por conveniencia.

## 2. Arquitectura activa

La documentación y los archivos de configuración actuales describen:

- Electron como aplicación de escritorio (`electron/main.js`, `electron/preload.js`).
- Django 5.2 como backend local.
- Waitress como servidor WSGI empaquetado.
- SQLite para persistencia local.
- PyInstaller para generar `CodeGuardServer`.
- electron-builder para generar paquetes de escritorio.
- Templates HTML, CSS y JavaScript locales; Bootstrap, HTMX, SweetAlert2 y FontAwesome.
- WhiteNoise para estáticos.
- Ollama opcional para tutoría local.
- Ed25519 y SHA-256 para la verificación de paquetes de conocimiento.

La aplicación debe enlazar el servidor solo a `127.0.0.1`. PySide6/desktop es legado y se conserva bajo `legacy/desktop-pyside6`; no es la arquitectura activa.

## 3. Módulos observados en el árbol de main

| Módulo | Estado de estructura |
|---|---|
| `apps.core` | Dashboard y health check |
| `apps.accounts` | Identidad y autenticación |
| `apps.audit` | Registro de auditoría |
| `apps.roadmaps` | ASCENSO, contenido, intentos, evaluaciones, importación, distribución y sincronización |
| `apps.tutoring` | Tutoría local |
| `apps.gamification` | Progreso gamificado, misiones, rachas y avatar |
| `apps.challenges` | Desafíos y evidencias |

La presencia de archivos y pruebas no acredita por sí sola la aceptación funcional de cada módulo.

## 4. Estado documental y hallazgos

- `README.md` describe ASCENSO 3.1 con 33 etapas y documenta el stack Electron + Django + SQLite.
- `README_WINDOWS.md` indica que el empaquetado Windows está definido, pero que la instalación limpia y el primer arranque todavía no están aceptados.
- El README informa 245 pruebas OK el 16-11-2026; debe reproducirse el comando completo sobre el HEAD que se vaya a presentar.
- La documentación QA indica que la aceptación de instalación limpia, GUI empaquetada, offline E2E, backup/restore y cierre limpio sigue pendiente.
- El modo de autenticación está temporalmente desactivado (`AUTH_DISABLED = True)); el flujo original permanece en código. No cambiarlo sin evaluar consecuencias y autorización expresa.
- La sincronización remota de conocimiento debe seguir inactiva si faltan endpoint HTTPS, allowlist y claves públicas confiables. No es requisito para el uso offline.
- La ejecución arbitraria de código del estudiante debe permanecer bloqueada mientras no exista un sandbox independiente y auditado.
- El tutor Ollama es opcional: el núcleo debe funcionar sin Ollama ni conexión a Internet.
- El README público menciona metadatos de PySide6 en la descripción del repositorio, pero el código/documentación de Windows identifican Electron + Django como arquitectura vigente. Corregir metadatos solo después de confirmar con el propietario y sin alterar el alcance.

## 5. Priorización para beta

### P0 — Bloqueante
1. Validar primer arranque con un perfil de datos vacío y temporal.
2. Confirmar migraciones, inicialización idempotente de ASCENSO y health check.
3. Confirmar que no se modifica ni reutiliza accidentalmente la base real del usuario.

### P1 — Esencial
1. Aceptar Electron + servidor local en ejecución normal.
2. Demostrar dashboard, ASCENSO, lección, ejercicio y evaluación.
3. Verificar persistencia después de cerrar y volver a abrir.
4. Verificar que el núcleo local funciona sin Internet.
5. Comprobar cierre normal, liberación del puerto y terminación del proceso hijo.

### P2 — Importante
1. Probar backup y restauración en un perfil aislado.
2. Validar tutor y fallback sin Ollama.
3. Revisar coherencia de gamificación y desafíos sin ampliar su alcance.

### P3 — Futuro
1. Hosting y publicación remota de conocimiento.
2. Distribución nativa macOS/ARM64.
3. Expansión editorial completa del contenido.
4. Características avanzadas de tutoría, mundo/avatar y desafíos.

## 6. Pruebas requeridas y evidencia

No se ejecutaron pruebas desde esta auditoría. La siguiente sesión debe disponer de un checkout local y registrar el SHA exacto:

```bash
git status --short --branch
git rev-parse HEAD
git branch --show-current
git log -5 --oneline --decorate
git diff --check

./.venv/bin/python manage.py check --settings=config.settings.development
./.venv/bin/python manage.py makemigrations --check --dry-run --settings=config.settings.development
./.venv/bin/python -m pip check

node --check electron/main.js
node --check electron/preload.js

./.venv/bin/python manage.py test \
  apps.core apps.accounts apps.audit apps.roadmaps \
  apps.tutoring apps.gamification apps.challenges \
  --settings=config.settings.development
```

Después, ejecutar build/aceptación de GUI en un perfil temporal único. No usar la base habitual. No ejecutar `cargar_ascenso --recrear`. Conservar el perfil temporal y los logs como evidencia.

La cifra histórica de 245 pruebas no debe copiarse como resultado nuevo hasta observar el resultado real.

## 7. Protección de trabajo local

El contexto de la conversación anterior indica que había un cambio local sin preparar en `electron/main.js`. El checkout local no está disponible mediante esta auditoría remota, por lo que ese diff no puede inspeccionarse, preservarse ni publicarse desde aquí. No sobrescribirlo ni recrearlo por inferencia. Antes de integrar cualquier trabajo, el agente local debe capturar `git status`, `git diff -- electron/main.js` y respaldar el parche.

## 8. Ramas y publicación

En la consulta inicial se observaron:
- `main`: `59d08848726550fde442be1eb1e1be5522637f0b`
- `documentation`: `11cefff675d502aca24fb4d93668ce77f8c6fd79`
- `test/phase-2-electron-integration`: `98fb56f68de9557445baebc26b14355092e8362a`
- `docs/continuidad-beta-2026-11-18`: `4a7034bb6fe5acbc2c8862943194915ead5c71e0`

La rama `documentation` contiene documentación extensa, pero el handoff existente advierte que está atrasada respecto a `main`. No hacer merge completo. Recuperar documentos selectivamente y revisar cada diff.

Este informe se publica en la rama de continuidad para facilitar el relevo. No se modificó código de aplicación, no se ejecutaron pruebas, no se creó release ni se desplegó.

## 9. Próximo paso obligatorio

La siguiente intervención debe ejecutarse en el entorno local del propietario (o mediante un agente con acceso real a ese checkout): inspeccionar estado Git y parche local, crear un perfil de datos temporal, ejecutar checks y suite completa, construir solo mediante el pipeline documentado y probar el arranque real de Electron/Waitress. Corregir únicamente defectos reproducibles, añadir regresiones y actualizar este informe con comandos, salidas, hashes y archivos concretos.

**Criterio de honestidad:** mientras no se prueben GUI, primer arranque, persistencia, modo offline y cierre limpio, CodeGuard Pro no debe declararse beta aceptada.
