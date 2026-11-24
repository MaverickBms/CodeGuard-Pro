# Progreso de producción académica — ASCENSO 3.1

**Actualizado:** 2026-11-24  
**Rama:** `release/1.0.0-final`  
**Estado:** trabajo editorial en curso; este documento no aprueba ni publica contenido.

## Línea base

La estructura curricular de referencia permanece intacta: 33 etapas, 212 módulos, 1.946 lecciones nominales y 7 prerrequisitos. La fuente maestra sigue siendo el DOCX del propietario identificado en `docs/ROADMAP_ASCENSO_INVENTARIO.md`; no se modifica ni se sustituye.

## Trabajo incorporado en esta iteración

| Entregable | Resultado | Estado editorial |
|---|---|---|
| Plan maestro de producción | `docs/PLAN_DESARROLLO_ACADEMICO_ASCENSO_3.1.md` | Plan, no contenido aprobado |
| Módulo 0.1 — Aprender a aprender | 8 lecciones existentes en `contenido_academico_0_1.json` | Borrador previo; requiere revisión individual |
| Módulo 0.2 — Investigación técnica | 7 lecciones nuevas en `contenido_academico_0_2.json` | Borrador de repositorio; falta dry-run/importación y revisión editorial |

El lote 0.2 conserva exactamente los siete títulos del manifiesto oficial e incluye 7 ejemplos, 14 ejercicios, 16 referencias y ningún video. Se omiten videos deliberadamente hasta verificar idioma, correspondencia temática y revisión pedagógica completa.

La validación realizada sobre el archivo 0.2 comprobó:
- JSON parseable.
- Siete títulos coincidentes con el manifiesto ASCENSO 3.1.
- Campos obligatorios y longitudes mínimas del contrato académico.
- Presencia de ejemplo, ejercicios y fuentes en cada lección.
- Tipos de evaluador admitidos por el importador.
- URLs de referencia en formato HTTPS.

Esta comprobación estructural no equivale a ejecutar `manage.py cargar_contenido_academico --dry-run`, importar el lote en SQLite ni aprobar su exactitud pedagógica. Esas verificaciones quedan pendientes en el entorno de la aplicación.

## Conteos que no deben mezclarse

- **8 lecciones:** borradores existentes del módulo 0.1, según la cobertura documentada anteriormente.
- **7 lecciones:** nuevo lote 0.2 redactado en el repositorio, todavía no confirmado como importado en la base de datos.
- **15 lecciones:** cuerpos de contenido disponibles en archivos de lote del repositorio (8 + 7), antes de deduplicación y revisión.
- **1.931 títulos:** saldo aritmético sin lote de contenido redactado en estos dos archivos; no es una lectura de cobertura de la base de datos.
- **0 lecciones aprobadas/publicadas:** se mantiene la política de no aprobar ni publicar automáticamente.

## Hallazgos de revisión que se deben resolver

1. Revisar individualmente las ocho lecciones 0.1, incluidos sus ejemplos, ejercicios, soluciones, referencias y videos.
2. Comprobar que los ejercicios automáticos no confundan coincidencia de palabras con evaluación semántica. Las respuestas abiertas requieren rúbrica o revisión humana; el evaluador por fragmentos solo debe usarse como comprobación limitada.
3. Ejecutar el dry-run del importador para el archivo 0.2 y resolver cualquier incompatibilidad antes de importarlo.
4. Verificar las URLs y la vigencia de cada referencia; registrar fecha y alcance real de consulta.
5. Revisar videos por separado. Los metadatos técnicos no demuestran pertinencia didáctica.
6. Diseñar rúbrica y entregables para el proyecto integrador de la etapa 0.
7. No crear objetivo oficial para la etapa 25: falta en el documento maestro y cualquier propuesta continúa sujeta a decisión editorial.

## Siguiente secuencia

1. Auditoría de contenido 0.1 y correcciones justificadas.
2. Dry-run y revisión del lote 0.2.
3. Módulo 0.3 — Herramientas (8 lecciones).
4. Módulo 0.4 — Depuración (7 lecciones).
5. Proyecto integrador de etapa 0.
6. Revisión de la etapa completa antes de pasar a la siguiente etapa P1.

Cada lote se conserva como borrador hasta superar revisión técnica, pedagógica, práctica, editorial, de fuentes y de licencias. El importador no debe ser tratado como aprobación.
