# Estándar editorial académico ASCENSO 3.1

**Estado:** borrador de trabajo; no publicado en la aplicación.  
**Versión del estándar:** 0.1.0  
**Fecha:** 2026-11-19

## Propósito

Convertir cada título del roadmap en una experiencia de aprendizaje clara, rigurosa, práctica y evaluable, sin alterar silenciosamente la estructura curricular oficial.

## Principios no negociables

1. **Fidelidad curricular:** conservar la numeración, los títulos, la prioridad y la secuencia del documento maestro. Toda propuesta de cambio se registra como propuesta, nunca como hecho oficial.
2. **Trazabilidad:** cada afirmación técnica o científica que no sea conocimiento elemental debe tener una fuente identificable y un alcance de uso declarado.
3. **Primacía de fuentes:** priorizar especificaciones, estándares, documentación del mantenedor, organismos públicos y revisiones científicas revisadas por pares. Blogs y foros solo pueden orientar búsquedas o aportar experiencias, nunca ser la única base de una afirmación importante.
4. **Exactitud temporal:** indicar versiones de herramientas, fecha de consulta y fecha de revisión cuando el contenido pueda cambiar.
5. **No inventar autoridad:** distinguir entre estándar oficial, documentación del fabricante, artículo científico, guía institucional y explicación didáctica original.
6. **No copiar material protegido:** redactar explicaciones originales, atribuir ideas y enlazar fuentes. No reproducir extensamente libros, cursos o documentación de terceros.
7. **Práctica verificable:** ejemplos y laboratorios deben producir resultados comprobables. El código se ejecuta en un entorno definido antes de marcarlo como verificado.
8. **Evaluación alineada:** cada ejercicio mide objetivos declarados; proporcionar criterios de evaluación y retroalimentación.
9. **Seguridad y ética:** las prácticas técnicas se realizan en equipos propios, laboratorios locales o entornos con autorización explícita.
10. **Transparencia:** ningún borrador se presenta como contenido aprobado, publicado o validado por un experto humano.

## Plantilla obligatoria de lección

- Identificador curricular exacto (etapa, módulo y título de la lección).
- Estado editorial: borrador, revisión técnica, revisión pedagógica, aprobado o publicado.
- Versión y fecha.
- Prerrequisitos reales.
- Objetivos observables y medibles.
- Contexto y utilidad.
- Explicación técnica gradual.
- Explicación sencilla o analogía, indicando dónde deja de ser válida.
- Ejemplo resuelto paso a paso.
- Ejercicios progresivos y criterios de éxito.
- Práctica o laboratorio cuando corresponda.
- Errores frecuentes y límites del concepto.
- Autoevaluación con respuestas razonadas.
- Referencias precisas: autor/organismo, título, tipo de fuente, URL, fecha de consulta, sección utilizada y afirmaciones respaldadas.
- Registro de verificación: código/experimento ejecutado, versión/entorno, fecha y resultado; o «no aplica».

## Puertas de calidad

Una lección no puede pasar a «aprobado» si:
- contiene afirmaciones factuales importantes sin fuente;
- atribuye a una fuente algo que esta no afirma;
- incluye código o comandos no comprobados presentados como ejecutables;
- no tiene ejercicios alineados con sus objetivos;
- confunde opinión, analogía o recomendación con un hecho establecido;
- usa enlaces rotos o documentación obsoleta para la versión enseñada;
- omite riesgos relevantes o límites de aplicación.

## Niveles de evidencia

- **A — Primaria/normativa:** estándar, especificación, documentación oficial del producto o institución responsable.
- **B — Síntesis científica:** revisión sistemática, metaanálisis o revisión académica revisada por pares.
- **C — Investigación primaria:** estudio empírico revisado por pares, con población y limitaciones identificadas.
- **D — Complementaria:** material educativo institucional o experiencia profesional; útil para ejemplos, no suficiente por sí sola para afirmaciones críticas.

No se debe llamar «oficial» a un artículo académico independiente ni «estándar» a una guía.

## Estado de esta entrega

Esta rama desarrolla únicamente el módulo 0.1 «Aprender a aprender» como piloto editorial. No modifica el JSON curricular, no crea lecciones publicadas en SQLite y no cambia el DOCX maestro. La siguiente integración requiere mapear cada lección a su UUID real de la base de datos y usar el flujo editorial de fuentes, snapshots, revisión y aprobación ya existente en CodeGuard Pro.
