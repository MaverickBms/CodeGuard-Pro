# Copias de seguridad y restauración — CodeGuard Pro

> **Estado: creación, verificación y restauración implementadas y probadas en Linux.**
>
> La restauración sustituye la base y `media/` con staging, validación de
> esquema, copia de reversión y rollback. En la aplicación empaquetada se
> invoca desde el menú de Electron; la aceptación en Windows sigue pendiente.

## Estado real de implementación

El módulo `apps/core/backup.py` proporciona `create_backup()` e
`inspect_backup()`. Crea un snapshot SQLite mediante la API de backup, incluye
`media/`, genera manifiesto SHA-256, verifica CRC e integridad SQLite y publica
el ZIP sin sobrescribir un destino existente. Rechaza rutas inseguras, enlaces
simbólicos, duplicados y tamaños fuera de los límites configurados. No incluye
`.secret_key` ni logs.

El módulo `apps/core/restore.py` implementa `restore_backup()`:

- valida el ZIP con `inspect_backup` antes de tocar el perfil;
- extrae únicamente `database.sqlite3` y `media/**` a un directorio de staging
  en el mismo volumen;
- rechaza migraciones desconocidas (esquema futuro) y acepta migraciones
  pendientes, que se aplican en el siguiente arranque;
- cierra las conexiones Django, elimina WAL/SHM obsoletos y sustituye base y
  media mediante renombrados;
- conserva una copia de reversión del perfil anterior y revierte si falla la
  verificación final;
- preserva `.secret_key`, logs y cualquier otro archivo del perfil.

Interfaces disponibles:

- `python manage.py crear_backup --output RUTA.zip`
- `python manage.py verificar_backup RUTA.zip`
- `python manage.py restaurar_backup RUTA.zip --confirm` (con la aplicación cerrada)
- Pantalla **Backups** para crear y verificar copias.
- Menú **CodeGuard Pro → Restaurar copia de seguridad…** en Electron, que
  detiene Django, ejecuta el modo `--restore-backup` del servidor empaquetado y
  reinicia la aplicación.

Pruebas automatizadas: `apps/core/tests/test_backups.py`,
`test_backup_commands.py`, `test_restore.py` y `test_backup_views.py`.
Verificación manual ejecutada el 19-11-2026 en Linux: backup real, restauración
en perfil vacío, arranque del servidor empaquetado sobre el perfil restaurado y
health check con los cuatro estados `ok`.

## 1. Alcance de los datos

El perfil escribible se determina exclusivamente por `CODEGUARD_DATA_DIR` (en escritorio, Electron lo establece en su carpeta `userData`). La configuración actual define:

- Base de datos: `db.sqlite3`.
- Archivos del usuario: `media/`.
- Clave local Django: `.secret_key`.
- Registros: `logs/`.

Una copia de seguridad debe preservar como mínimo la base de datos y `media/`. La clave `.secret_key` no puede copiarse en claro: si se decide conservarla para mantener continuidad criptográfica, debe ir cifrada dentro del archivo con una clave derivada de una frase de paso que nunca se almacene junto al backup. Los logs no se incluyen por defecto porque pueden contener rutas y datos operativos. Los archivos temporales SQLite `-wal` y `-shm` no se copian directamente.

## 2. Formato propuesto

Archivo ZIP versionado, con estructura lógica:

- `manifest.json`: formato, versión de CodeGuard, versión del esquema, fecha UTC, lista de archivos, tamaños y SHA-256.
- `database.sqlite3`: snapshot consistente de la base.
- `media/**`: árbol de archivos multimedia, conservando rutas relativas.
- `secrets/secret-key.enc`: opcional y cifrado con AES-256-GCM; clave derivada mediante Scrypt. La frase de paso no se escribe en el archivo, base de datos ni logs.

El manifest no debe incluir credenciales, tokens, variables de entorno ni rutas absolutas del equipo. El ZIP debe ser determinista en sus rutas y rechazar nombres absolutos, segmentos `..`, enlaces simbólicos, entradas duplicadas y tamaños descomprimidos excesivos.

## 3. Creación segura

1. Verificar que la aplicación se ejecuta sobre un perfil local escribible y que el destino de backup no está dentro del propio `CODEGUARD_DATA_DIR`.
2. Obtener snapshot de SQLite mediante la API de backup de SQLite (conexión origen y destino independientes), no copiando `db.sqlite3` mientras está abierto en modo WAL.
3. Comprobar `PRAGMA integrity_check` sobre el snapshot; exigir resultado `ok`.
4. Copiar `media/` a un área temporal, sin seguir enlaces simbólicos ni salir de la raíz.
5. Calcular SHA-256 y tamaño de cada archivo; escribir el manifest.
6. Crear primero un archivo temporal en el directorio destino, cerrar el ZIP, reabrirlo y verificar CRC, manifest y hashes.
7. Publicar el archivo final mediante rename atómico en el mismo volumen. Si algo falla, eliminar solo temporales creados por la operación y conservar backups anteriores.
8. Registrar `backup_creado` sin incluir la frase de paso, claves ni contenido sensible.

La operación no debe bloquear indefinidamente la UI; el estado y los errores deben ser comunicados al usuario. No borrar backups antiguos automáticamente en la primera versión.

## 4. Restauración segura

La restauración requiere confirmación explícita del usuario y la aplicación completamente cerrada (incluido el servidor Django). El proceso debe:

1. Abrir el ZIP sin extraerlo directamente al perfil.
2. Validar versión de formato, estructura, rutas, límites de tamaño, entradas duplicadas y hashes.
3. Verificar la base restaurada con `PRAGMA integrity_check`.
4. Comprobar compatibilidad del esquema. No ejecutar migraciones destructivas ni downgrade automático.
5. Extraer base y multimedia a un directorio temporal nuevo, dentro del mismo volumen del perfil.
6. Si existe clave cifrada, solicitar frase de paso y verificar AES-GCM antes de modificar el perfil. Una clave incorrecta debe abortar sin cambios.
7. Crear una copia de reversión del perfil actual o renombrar el perfil actual a una ubicación de recuperación.
8. Sustituir el conjunto de datos mediante renombres atómicos controlados. Si falla cualquier paso, restaurar el perfil previo.
9. Arrancar Django y comprobar migraciones/health check antes de marcar la restauración como aceptada.
10. Registrar `backup_restaurado` solo tras el éxito, sin registrar secretos ni rutas sensibles.

No se permite mezclar la base restaurada con el directorio `media/` actual: ambos pertenecen al mismo snapshot lógico.

## 5. Compatibilidad y protección

- Rechazar versiones de formato futuras o no soportadas.
- Para esquemas anteriores, permitir solo una ruta de migración explícita y probada; nunca migrar el único ejemplar del backup.
- Mantener la copia original inmutable.
- No seguir symlinks durante copia o extracción.
- Limitar cantidad de entradas, tamaño individual y tamaño total descomprimido para evitar ZIP bombs.
- No aceptar archivos ZIP cifrados con algoritmos heredados.
- No mostrar ni registrar la frase de paso, clave derivada, contenido de `.secret_key` o hashes de contraseñas.
- El backup contiene datos personales y debe guardarse en una ubicación elegida por el usuario; no subirlo a servicios remotos automáticamente.

## 6. Pruebas de aceptación obligatorias

### Creación
- Perfil vacío y perfil con progreso, documentos y multimedia.
- Escrituras concurrentes durante backup; snapshot íntegro y restaurable.
- SQLite WAL activo; integridad del snapshot y ausencia de dependencia en archivos WAL/SHM externos.
- Destino sin permisos, disco lleno, interrupción y archivo temporal preexistente.
- Destino dentro del perfil: rechazo.
- Destino existente: rechazo sin sobrescribir el backup previo.
- Verificación de SHA-256 y CRC tras crear el ZIP.

### Restauración
- Backup válido en perfil vacío y perfil con datos previos.
- Confirmación cancelada: perfil sin cambios.
- ZIP truncado, manifest ausente, hash incorrecto, rutas `../`, rutas absolutas, symlinks, duplicados y ZIP bomb: rechazo sin tocar el perfil.
- Base corrupta y versión de esquema no compatible: rechazo.
- Frase de paso incorrecta: rechazo sin cambios.
- Fallo simulado durante sustitución: rollback completo.
- Comprobación posterior de documentos, progreso, intentos, evaluaciones, auditoría, roadmap y health check.
- Reinicio posterior y comparación de conteos/checksums de archivos.

### Interfaz
- Mensajes comprensibles, progreso y cancelación segura.
- Confirmación antes de reemplazar el perfil.
- Indicación de fecha, tamaño y versión del backup.
- No presentar la operación como exitosa antes de validar el perfil restaurado.

## 7. Criterio de salida

La implementación y las pruebas automatizadas están completas. La aceptación
en Linux incluye backup real, restauración desde el servidor empaquetado,
arranque posterior y health check. **Pendiente para declarar la función
totalmente aceptada:** repetir la matriz de creación/restauración en una
instalación limpia de Windows y confirmar el cierre/reapertura desde el menú de
Electron en ese sistema. Hasta entonces, Windows debe describirse como
implementado pero no aceptado en esa plataforma.
