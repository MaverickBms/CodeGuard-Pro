# ADR-005 — Activar WAL mode en SQLite

**Estado:** Propuesto  
**Fecha:** 16 de noviembre de 2026  
**Decisor:** Subagente 1 — Arquitectura y Backend  
**Fase:** Fase 1 (estabilización pre-Fase 2)  
**Relacionado:** `docs/ARQUITECTURA.md` (sección 6 Base de datos), `config/settings/base.py`

## Contexto

CodeGuard Pro usa SQLite como base de datos principal (`config/settings/base.py`, `DATABASES.default`), sin configurar `journal_mode`. El motor opera por defecto en modo `delete` (rollback journal), donde una escritura bloquea la base de datos para lecturas concurrentes y viceversa.

La aplicación es local, monousuario y offline-first (`AUTH_DISABLED = True`), ejecutada en un equipo con recursos limitados (HP 240 G10, i3-N305, ~1.3 GB RAM libre). Hoy la contención de escrituras es inexistente por un solo usuario, pero la hoja de ruta contempla:

- Sincronización de conocimiento en segundo plano (proceso hijo `--sync-knowledge`).
- Posible evolución a multiusuario en futuras fases.
- Escrituras de progreso del estudiante (`Progreso`, `IntentoEjercicio`) mientras se lee el roadmap en el panel.

## Problema

Sin WAL, cada operación de escritura en SQLite adquiere un bloqueo exclusivo que impide lecturas concurrentes. En el monolito actual esto se manifiesta como:

1. El panel de roadmap lee `Etapa`, `Modulo`, `Leccion`, `Progreso` mientras procesos en segundo plano pueden escribir `EstadoSincronizacion`, `PaqueteConocimientoInstalado` o `Progreso`.
2. Futuras escrituras concurrentes (multiusuario + sincronización) pueden producir `database is locked` bajo carga ligera.
3. No hay configuración explícita de modo de diario, por lo que el comportamiento depende del valor por defecto de la compilación de SQLite.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Decisión |
|---|---|---|---|
| 1. Mantener modo `delete` (estado actual) | Sin cambios, comportamiento por defecto. | Bloqueo exclusivo en escritura; riesgos de contención futura. | Rechazada para el horizonte de estabilización. |
| 2. Cambiar a PostgreSQL / MySQL | Soporte nativo a concurrencia masiva. | Requiere servidor adicional, rompe el requisito de equipo personal sin servicios extra (RNF-001). | Descartada (ver ADR-002). |
| 3. Activar WAL mode en SQLite | Lecturas concurrentes durante escritura, menor contención, mismo fichero único, sin servidor adicional. | Genera ficheros auxiliares `-wal` y `-shm`; backup debe considerar ambos; no funciona sobre sistemas de archivo de red (NAS), pero v1 es local. | **Adoptada**. |

## Decisión adoptada

Activar el modo WAL (Write-Ahead Logging) en SQLite mediante la opción de Django:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATA_DIR / "db.sqlite3",
        "OPTIONS": {
            "init_command": "PRAGMA journal_mode=WAL;",
        },
    }
}
```

en `config/settings/base.py`. El cambio es aplicable tanto al modo desarrollo (`development.py`) como al modo escritorio empaquetado (`desktop.py`), ya que ambos heredan de `base.py`.

## Justificación

- Mantiene SQLite como motor único (sin servidor adicional, cumple RNF-001).
- Mejora la concurrencia lecturas/escrituras sin cambiar el modelo de datos ni el código de aplicación.
- Compatible con `AUTH_DISABLED = True` y con la v1 local: no altera el comportamiento funcional, solo el modo de diario interno.
- Bajo consumo de RAM/CPU, coherente con el equipo objetivo.
- Django gestiona la conexión persistente; `PRAGMA journal_mode=WAL` se ejecuta al abrir cada conexión.

## Consecuencias

Positivas:

- Lecturas del panel y del roadmap no se bloquean mientras hay escrituras de sincronización o progreso.
- Menor probabilidad de `database is locked` en futuros escenarios de multiusuario ligero.
- Checkpoints automáticos de WAL mantienen el fichero principal con tamaño acotado.

Negativas / costes aceptados:

- Aparecen ficheros auxiliares `db.sqlite3-wal` y `db.sqlite3-shm` junto a la base de datos; los procedimientos de backup y restauración (`docs/BACKUPS_Y_RESTAURACION.md`) deben copiar los tres ficheros o forzar un checkpoint antes de copiar.
- WAL no es compatible con sistemas de archivo de red (NFS/SMB); la aplicación asume almacenamiento local, que ya es el caso de v1.
- En sistemas de archivos sin soporte para memoria compartida (`shm`), SQLite cae de regreso al modo `delete` de forma transparente.

## Implicaciones futuras

- Prepara la base para la sincronización de conocimiento en segundo plano y una posible evolución a multiusuario sin cambiar de motor.
- Los scripts de backup deben incluir `PRAGMA wal_checkpoint(TRUNCATE)` o copiar los ficheros `-wal`/`-shm`.
- No afecta a las migraciones de Django ni al esquema de datos.

## Verificación pendiente

- Ejecutar `python manage.py test` tras el cambio para confirmar 0 issues y 197 pruebas OK.
- Comprobar que `server_entry.py` (Waitress) y `--sync-knowledge` funcionan con WAL activado.
- Validar que el backup/restauración de `data/db.sqlite3` incluya los ficheros auxiliares.

---
*ADR registrado sin modificar código Python. La aplicación al código requiere cambios en `config/settings/base.py`.*