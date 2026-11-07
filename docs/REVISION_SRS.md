# CodeGuard Pro — Auditoría del SRS (REVISION_SRS.md)

**Producto:** CodeGuard Pro  
**Versión del SRS auditado:** `IEEE830(1).md` v2.0  
**Fecha:** 5 de noviembre de 2026  
**Estado:** Borrador de auditoría técnica

---

## 1. Documentos de referencia encontrados

| Documento | Ruta | Estado |
|---|---|---|
| SRS v2.0 (Markdown) | `CodeGuard/IEEE830.md` | ✅ Leído íntegro (531 líneas) |
| SRS v2.0 (PDF) | `CodeGuard/IEEE830 (1).pdf` | ✅ Presente |
| Roadmap ASCENSO Maestro Consolidado 3.1 (PDF) | `Descargas/PROYECTO_ASCENSO_Roadmap_Maestro_Consolidado_3_1_2026.pdf` | ✅ Extraído texto (3661 líneas) |
| Roadmap ASCENSO 3.1 (DOCX) | `Descargas/PROYECTO_ASCENSO_Roadmap_Maestro_Consolidado_3_1_2026.docx` | ✅ Presente |
| Documentación de arquitectura (docs/) | `CodeGuard/docs/` | ❌ No existía — se crea en este proyecto |

No se encontraron diagramas de arquitectura, diseños de interfaz ni ADRs previos en el directorio
de trabajo. Se crean desde cero.

---

## 2. Consistencia de requisitos

El SRS v2.0 distingue claramente:
- **APROBADOS:** línea base del MVP (RF-001, RF-002, RF-003, RF-004, RF-005, RF-010 a RF-017,
  RF-020 a RF-027, RF-030 a RF-044, RF-050 a RF-054, RF-056, RF-060 a RF-070, RF-080 a RF-088,
  RF-090 a RF-094, RF-097, RF-100, RF-102 a RF-104, RF-108, RF-109, RF-110, RF-111, RF-113, RF-114,
  RF-120 a RF-123, y RNF/RS correspondientes).
- **PENDIENTES:** RF-006 / RS-017 (bloqueo tras N intentos — N sin definir).
- **PROPUESTOS:** no obligatorios hasta aprobación (cifrado de backup, panel de competencias,
  OCR, backup automático, etc.).
- **FUT:** etapas posteriores.

No se detectaron contradicciones técnicas graves entre requisitos aprobados.

---

## 3. Intervención de auditoría y consolidación (2026-11-07)

Durante la auditoría de arquitectura y seguridad se aplicaron las correcciones técnicas
identificadas en el plan maestro (CG-001 a CG-010):

- **CG-007** — `DEBUG=False` por defecto (desarrollo con `DEBUG=True` en `config/settings/development.py`).
- **CG-008** — CSP estricta (sin `unsafe-inline` en scripts) + script inline externalizado a `static/js/codeguard.js`.
- **CG-009** — Servidor WSGI local con Waitress + WhiteNoise en `127.0.0.1`.
- **CG-010** — Limpieza de `run.sh`.
- **CG-003** — Eliminación de la creación implícita de usuario.
- **CG-004** — Middlewares de sesión/autenticación.
- **CG-005** — Middleware de inactividad.
- **CG-006** — Rutas protegidas con `@login_required`.
- **CG-001** — Vistas y URLs de autenticación implementadas.
- **CG-002** — Modelo de usuario custom `accounts.Usuario` activado (`AUTH_USER_MODEL`) con
  migración de datos que preservó al usuario existente.

Con estas correcciones, el núcleo local (autenticación, sesión, seguridad, servidor) quedó
implementado y verificado (31 tests OK).

---

## 4. Decisiones pendientes (requieren definición del propietario)

| ID | Decisión pendiente | Por qué es necesaria | Recomendación |
|---|---|---|---|
| RF-006 / RS-017 | Valor de N (intentos fallidos antes de bloqueo) | Sin N no se puede implementar el bloqueo | Preparar arquitectura configurable; N pendiente de propietario |
| Versión exacta de Django LTS | Fijar en `requirements.txt` | Compatibilidad con Python 3.14 | Django 5.2 LTS (seleccionado) |
| Selección de etapas iniciales del MVP | 0, 1, 2, 3, 8, 17, 21 (propuesta del SRS) | No es requisito obligatorio | Las 33 etapas deben estar representadas (RF-010) |

---

## 4. Riesgos identificados

| Riesgo | Impacto | Mitigación |
|---|---|---|
| RAM limitada (~1.3 GB libre) | Ralentización | Django ligero, 1 worker, sin DEBUG, batch en PDFs |
| Backups sin cifrado al trasladarse | Exposición de datos | Opción de cifrado (propuesta); documentar límites LUKS |
| Contenido ASCENSO inventado | Desviación académica | Fuente de verdad: roadmap 3.1; no inventar etapas |
| Versiones abiertas del stack | Incompatibilidad | Versiones fijadas en `requirements.txt` |
| Archivos subidos ejecutables | Ejecución maliciosa | Validación MIME/extensión, fuera de web root (futuro) |

---

## 5. Trazabilidad

La matriz del SRS referencia pruebas T-xxx cuya existencia no implica implementación. Se creará
`docs/MATRIZ_TRAZABILIDAD.md` como complemento (sin modificar el SRS original).

No se modifica `IEEE830(1).md` sin autorización del propietario.
