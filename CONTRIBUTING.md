# Contribuir a CodeGuard Pro

## Principios del repositorio

- `main` es la única rama integrada y la referencia estable de trabajo.
- El producto inicial es personal, local y offline-first. No introducir servicios remotos obligatorios, telemetría ni dependencias CDN.
- No cambiar el comportamiento académico, la persistencia ni la seguridad como parte de una limpieza documental.
- No versionar datos de estudiantes, bases SQLite, secretos, modelos de IA ni artefactos de compilación.
- No eliminar archivos históricos o migraciones para reducir tamaño: preservar trazabilidad.

## Flujo de trabajo

1. Actualizar `main` antes de iniciar una tarea.
2. Para cambios aislados, usar una rama temporal con prefijo `feat/`, `fix/`, `docs/` o `test/`.
3. Mantener el alcance de cada rama pequeño y descriptivo.
4. Ejecutar las comprobaciones aplicables y registrar resultados reproducibles.
5. Integrar mediante fast-forward o pull request después de revisar el diff.
6. No hacer force-push ni borrar ramas con commits exclusivos sin revisar y respaldar su contenido.
7. Eliminar ramas temporales solo después de confirmar que sus cambios están integrados y que no contienen trabajo pendiente.

## Entorno de desarrollo

Consulta `docs/INSTALACION.md`. Utiliza un entorno virtual Python, `npm ci` y un directorio de datos aislado fuera del repositorio. Nunca ejecutes pruebas destructivas sobre la base de datos personal.

## Comprobaciones mínimas

```bash
./.venv/bin/python manage.py check --settings=config.settings.development
./.venv/bin/python manage.py makemigrations --check --dry-run --settings=config.settings.development
./.venv/bin/python -m pip check
./.venv/bin/python manage.py test \
  apps.core apps.accounts apps.audit apps.roadmaps \
  apps.tutoring apps.gamification apps.challenges \
  --settings=config.settings.development
```

Si una tarea afecta Electron, empaquetado, offline o persistencia, añadir las pruebas específicas y documentar la plataforma, arquitectura, pasos y resultado. Una prueba unitaria no sustituye la aceptación de la aplicación empaquetada.

## Django y datos

- Las migraciones existentes son parte del historial y no deben editarse después de publicadas.
- Crear migraciones nuevas y revisar `sqlmigrate` cuando haya cambios de esquema relevantes.
- Mantener ASCENSO y otros JSON académicos versionados como fuentes de contenido; nunca confundirlos con datos runtime.
- No usar `cargar_ascenso --recrear` sobre datos reales.
- Las operaciones de importación, actualización y restauración deben ser idempotentes o disponer de rollback documentado.

## Seguridad y privacidad

- Mantener el servidor local enlazado a loopback.
- No introducir ejecución de código sin sandbox.
- No enviar progreso, código ni datos académicos a servicios externos en el modo privado.
- Nunca incluir claves, tokens, bases de datos personales ni logs sensibles en commits o issues.
