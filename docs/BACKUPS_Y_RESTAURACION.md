# CodeGuard Pro — Backups y restauración

**Producto:** CodeGuard Pro  
**Versión:** 1.0  
**SRS de referencia:** `IEEE830(1).md` v2.0 — RF-100 a RF-109, RS-007, RS-008

---

## 1. Formato de backup

El formato previsto es **tar.gz** que empaqueta:
- Base de datos SQLite (`data/db.sqlite3`; la tabla del usuario único local es
  `accounts_usuario` tras el modelo custom `AUTH_USER_MODEL = "accounts.Usuario"`).
- Archivos de usuario (`media/`).
- Archivo de metadatos del backup (fecha, versión, hash SHA-256).

---

## 2. Creación de backup (manual, RF-100)

1. Usuario solicita "Crear backup" desde la administración.
2. El sistema empaqueta SQLite + archivos en un `tar.gz`.
3. Se calcula el hash SHA-256 del paquete.
4. Se guarda en la ruta especificada por el usuario.
5. Se registra la operación en auditoría (`backup_creado`).

---

## 3. Validación de integridad (RF-102)

- Hash SHA-256 pre y post creación.
- Validación de contenido del archivo tar.gz antes de considerar el backup válido.

---

## 4. Restauración segura (RF-103, RF-104)

La restauración **debe validar el contenido antes de extraerlo** y no sobrescribir los datos
actuales hasta haber validado la copia y preparado una estrategia de recuperación.

Protecciones implementadas/planificadas:
- **Rutas de archivo maliciosas:** rechazar rutas absolutas o con `..` dentro del tar.
- **Path traversal:** validar que todas las rutas del tar estén dentro del directorio destino.
- **Archivos inesperados:** permitir solo tipos esperados (SQLite, archivos de media, metadatos).
- **Archivos excesivamente grandes:** limitar tamaño del tar y de cada archivo interno.
- **Archivos corruptos:** detectar tar.gz dañado y abortar.
- **Restauraciones incompletas:** verificar checksum de todos los miembros del tar.

Estrategia de recuperación:
1. Antes de restaurar, hacer un backup de seguridad del estado actual.
2. Validar el backup a restaurar (hash, contenido, tamaño).
3. Extraer en ubicación temporal.
4. Si todo es válido, reemplazar los datos actuales.
5. Si falla en cualquier paso, restaurar desde el backup de seguridad y abortar.

---

## 5. Cifrado de backup (RF-105 / RS-008 — PROPUESTO)

El cifrado de backup está **propuesto, no aprobado** como requisito funcional.

**Recomendación:** ofrecer cifrado para backups que se trasladen a otro dispositivo, ya que
LUKS solo protege el disco en reposo (dispositivo apagado) y no protege backups copiados fuera
del equipo.

**Riesgos:**
- Pérdida de la contraseña de cifrado = pérdida irreversible del backup.
- Complejidad adicional en el flujo de restauración.
- No es requisito del MVP; se deja para una fase posterior si el propietario lo aprueba.

---

## 6. Registro de operaciones (RF-108)

Todas las operaciones de backup y restauración se registran en `AuditLog` con evento
`backup_creado` / `backup_restaurado`, usuario, IP y fecha.

---

## 7. Limpieza de temporales (RF-109)

Los archivos temporales generados durante backups y restauraciones se limpian tras la
operación, incluso en caso de error (bloques `try/finally`).
