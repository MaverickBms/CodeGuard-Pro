# ASCENSO 3.1 — estado documental, estado de aplicación y continuidad

**Fecha de corte:** 2026-11-24  
**Rama de trabajo:** `content/ascenso-stage-0-learning-method`  
**Roadmap de referencia:** `apps/roadmaps/data/ascenso_3_1.json`  
**Edición:** 3.1

## 1. Inventario curricular inmutable

El roadmap maestro registra 33 etapas (0–32), 212 módulos y 1.946 títulos de lección. Este inventario es la fuente de verdad para identificadores, orden, títulos, dependencias y objetivos. La documentación académica no debe modificarlo ni reconstruirlo por inferencia.

La etapa 25 conserva su objetivo oficial vacío. Se mantienen los módulos y títulos que sí existen; no se crea un objetivo sustituto.

## 2. Tres estados que no deben confundirse

| Capa | Estado registrado | Qué significa |
|---|---|---|
| Roadmap | 33 etapas, 212 módulos, 1.946 títulos | Estructura curricular oficial; no equivale a contenido desarrollado. |
| Documentación académica | El índice de continuidad registra desarrollo documental para las etapas 0–32 y cobertura nominal de 1.916 lecciones en el bloque de etapas 1–32, además del desarrollo inicial de etapa 0. | Material de trabajo en Markdown. La cifra del índice es un registro documental y requiere auditoría estructural/semántica independiente antes de considerarse cobertura aceptada. |
| Aplicación | El estado consignado en el PR #17 reporta 8 lecciones con cuerpo en borrador, 0 aprobadas y 0 publicadas; 1.938 pendientes de desarrollo. | Estado de contenido en la instalación/entorno de aplicación descrito por ese PR. No se debe inferir que los documentos Markdown ya fueron importados. |

Los videos con metadatos o enlaces técnicamente verificados tampoco se consideran recomendados hasta completar su revisión pedagógica y confirmar idioma, cobertura y pertinencia.

## 3. Contrato de importación y publicación

Según el contrato editorial documentado en el PR #14:

- El importador consume JSON v1 estricto.
- Los UUID deben ser los UUID curriculares reales, exportados desde la instalación correspondiente. Nunca se generan ni se deducen.
- Las fuentes deben existir en el catálogo y estar activas, con su estado de licencia registrado.
- La validación completa ocurre antes de cualquier escritura.
- La importación crea borradores. Revisión, aprobación y publicación son transiciones separadas.
- No se inserta Markdown directamente en SQLite ni se sobrescriben contenidos existentes.
- Un manifiesto que contenga UUID de una instalación real no debe publicarse en un repositorio público.

## 4. Prioridades de continuidad

### P0 — Obtener una línea base real de la aplicación
1. Ejecutar `exportar_manifiesto_academico` únicamente en el entorno de desarrollo autorizado.
2. Guardar el manifiesto fuera del repositorio público si contiene UUID reales.
3. Comparar el inventario exportado con el JSON maestro: etapas, módulos, lecciones, ejemplos, ejercicios, UUID y dependencias.
4. Identificar las 8 lecciones con cuerpo, sus estados y cualquier diferencia entre roadmap y base de datos.
5. No importar hasta resolver diferencias, fuentes, licencias y protección contra sobrescritura.

### P1 — Auditar la documentación por lección
1. Cotejar cada encabezado con el título y orden exactos del roadmap.
2. Detectar títulos duplicados, lecciones omitidas, numeración no canónica y contenido asignado al módulo equivocado.
3. Revisar que cada lección tenga explicación suficiente, objetivos observables, prerrequisitos, ejemplo, práctica, evidencia y comprobación cuando corresponda.
4. Distinguir contenido original, paráfrasis, citas, material de terceros y recursos audiovisuales.
5. Revisar vigencia de comandos, versiones, APIs, referencias, licencias y seguridad.
6. Registrar hallazgos concretos por archivo y sección; no marcar como corregido lo que no se haya verificado.

### P2 — Preparar lotes de importación pequeños y reversibles
1. Priorizar un módulo completo y representativo para probar el flujo.
2. Construir el JSON v1 usando exclusivamente UUID y fuentes exportados.
3. Validar el lote en modo de solo lectura antes de escribir.
4. Importar como borrador en entorno de desarrollo.
5. Comprobar conteos, asociaciones, renderizado, ejemplos, ejercicios y ausencia de sobrescrituras.
6. Repetir por lotes; conservar trazabilidad de archivo, commit, lote, resultado y responsable.

### P3 — Revisión y aprobación
1. Ejecutar laboratorios en versiones y entornos declarados.
2. Conservar comandos, datos sintéticos, resultados y limitaciones.
3. Solicitar revisión técnica y pedagógica independiente.
4. Aprobar solo cuando exista evidencia suficiente.
5. Publicar únicamente mediante el flujo editorial de la aplicación y con la autorización correspondiente.

## 5. Criterios de aceptación

- 100 % de correspondencia de la estructura contra el roadmap oficial.
- Ningún UUID inventado, duplicado o reasignado.
- Ninguna escritura antes de validación completa del lote.
- Ningún contenido existente sobrescrito silenciosamente.
- Cada lección importada queda asociada al módulo y etapa correctos.
- Los estados borrador, revisión, aprobado y publicado se mantienen diferenciados.
- Ningún laboratorio, prueba, video o referencia se declara verificado sin evidencia.
- La etapa 25 mantiene intacta la ausencia de objetivo oficial.
- El PR #14 permanece como propuesta documental; el PR #17 y su rama de release no se modifican en esta fase.

## 6. Próxima acción concreta

La siguiente acción de mayor valor no es redactar otras explicaciones sin conocer los identificadores reales: es obtener y auditar el manifiesto de la instalación de desarrollo. Esto permitirá convertir el trabajo documental en lotes importables sin inventar UUID ni comprometer datos existentes.

**Estado de este documento:** guía operativa de continuidad; no constituye aprobación curricular, ejecución de laboratorios, importación ni publicación.
