# ADR-002 — Base de datos

**Estado:** Aprobado (implementado en el incremento 1)  
**Fecha:** 5 de noviembre de 2026

## Contexto

El SRS establece SQLite como base de datos principal con FTS5 para búsqueda. Debe verificarse
en el entorno real y las migraciones deben aplicarse desde una base de datos vacía.

## Decisión

SQLite 3.51.2 con FTS5, gestionado a través del ORM de Django con migraciones. Motor sin
proceso servidor, rápido en SSD NVMe, adecuado para monousuario.

## Justificación

- Verificado FTS5 en el entorno real (SQLite 3.51.2).
- Sin proceso servidor adicional (bajo consumo de RAM/CPU).
- Fichero único, fácil de respaldar y restaurar.
- Django ORM protege contra SQLi (consultas parametrizadas).

## Consecuencias

Positivas: simple, rápido, bajo consumo, backup trivial (copia de fichero).
Negativas: no apto para escrituras concurrentes masivas ni multiusuario (no es objetivo).

## Alternativas consideradas

- PostgreSQL: descartado (servidor adicional, mayor consumo).
- MySQL/MariaDB: descartado (id.).

## Verificación

`python manage.py migrate` aplicó correctamente todas las migraciones desde una base de datos
vacía (contenttypes, auth, accounts, audit, core, admin, sessions).
