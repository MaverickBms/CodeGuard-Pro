# ADR-003 — Gestión de documentos y evidencias

**Estado:** Propuesto (pendiente de implementar en incrementos 4 y 5)  
**Fecha:** 5 de noviembre de 2026

## Contexto

El SRS requiere importación de PDFs (RF-030 a RF-044), detección de duplicados por hash,
detección de documentos dañados/protegidos, extracción de texto nativo, FTS5, y gestión de
evidencias con hash SHA-256 (RF-080 a RF-088). Los archivos deben almacenarse fuera del web
root y no servirse como contenido activo.

## Decisión propuesta

- Procesamiento de PDFs con PyMuPDF en modo batch (control de memoria, RF-037 / RNF-016).
- Búsqueda textual con SQLite FTS5 (RF-039).
- Detección de duplicados por hash SHA-256 del archivo (RF-034).
- Almacenamiento de archivos en `media/` fuera del web root, servidos mediante vistas
  protegidas con `Content-Disposition: attachment` (RS-005, RS-006, RF-086).
- Evidencias con hash SHA-256 y verificación de integridad (RF-084, RF-085).

## Justificación

PyMuPDF es rápido y de bajo consumo; FTS5 integrada en SQLite evita un motor de búsqueda
separado; almacenar archivos fuera del web root y servirlos como adjunto evita ejecución
accidental.

## Consecuencias

Positivas: seguridad de archivos, búsqueda integrada, bajo consumo.
Negativas: OCR queda fuera del MVP (PDFs escaneados se detectan y notifican, RF-033).

## Alternativas consideradas

- Tesseract OCR: descartado para el MVP (dependencia adicional, fuera de alcance).
- Elasticsearch/Whoosh: descartado (servidor adicional, sobreingeniería).

## Pendiente

Implementar en el incremento 4 (biblioteca) e incremento 5 (evidencias).
