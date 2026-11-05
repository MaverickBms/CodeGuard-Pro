# ADR-001 — Arquitectura del sistema

**Estado:** Aprobado (implementado en el incremento 1)  
**Fecha:** 5 de noviembre de 2026

## Contexto

CodeGuard Pro debe ser una aplicación local, monousuario, offline-first, ligera y fácil de
mantener en un equipo con recursos limitados (HP 240 G10, i3-N305, ~1.3 GB RAM libre).

## Decisión

Arquitectura monolito modular basada en Django (patrón MVT), con aplicaciones separadas por
dominio (`core`, `accounts`, `audit`, y por venir `roadmaps`, `competencies`, `library`,
`knowledge`, `assessments`, `evidence`, `labs`, `backups`, `vigencia`, `ethics`). Servidor
local en `127.0.0.1`, sin contenedores, sin servicios adicionales, sin CDN.

## Justificación

- Django provee ORM seguro, autenticación integrada, protección CSRF/XSS/SQLi y admin.
- SQLite elimina la necesidad de un servidor de base de datos separado.
- HTMX + Bootstrap locales permiten interactividad sin SPA pesada ni dependencia de Internet.
- El monolito modular evita la complejidad de microservicios en un equipo personal.

## Consecuencias

Positivas: bajo consumo, arranque rápido, fácil mantenimiento, 100% offline.
Negativas: no escalable a multiusuario sin rearquitectura (no es objetivo del MVP).

## Alternativas consideradas

- Microservicios: descartado (sobreingeniería para un equipo personal).
- Flask/FastAPI: descartado (se pierde el admin y autenticación integrada de Django).
- PostgreSQL: descartado (requiere servidor adicional; SQLite es suficiente para monousuario).
