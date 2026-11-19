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


## Extensión didáctica: aprendizaje multimodal y recursos audiovisuales

Cada módulo podrá combinar, cuando aporte valor:
- explicación escrita original;
- video externo curado y enlazado al canal original;
- demostración o animación propia;
- ejemplo resuelto;
- práctica guiada y reto independiente;
- laboratorio reproducible;
- quiz de recuperación con retroalimentación razonada;
- tarjetas de repaso y agenda de repetición espaciada;
- proyecto integrador y rúbrica;
- glosario, mapa conceptual y referencias.

### Ficha obligatoria de video

Registrar título, creador/canal, URL canónica, idioma hablado, subtítulos (idioma y si son manuales, automáticos o no verificados), duración solo si se ha comprobado, nivel, conceptos cubiertos, objetivo curricular, actividad posterior, fecha de verificación y estado del enlace. El español es la primera opción. Un video en inglés solo será recomendado como principal si se ha verificado una opción de subtítulos en español o existe una alternativa equivalente en español claramente enlazada.

No atribuir al creador afirmaciones que no realiza. No usar visualizaciones, suscriptores o popularidad como sustitutos de revisión pedagógica. El video es material complementario: nunca basta con verlo para completar una lección o etapa.

### Criterio de accesibilidad y mantenimiento

- Proporcionar una alternativa textual o en español cuando el recurso principal esté en inglés.
- Indicar cómo activar subtítulos cuando se haya comprobado su disponibilidad.
- No asumir que los subtítulos automáticos son exactos.
- Revisar enlaces, idioma y subtítulos antes de cada publicación y durante mantenimiento.
- Enlazar al original; no descargar, republicar ni incrustar copias no autorizadas.

### Funciones de aprendizaje recomendadas para la experiencia CodeGuard Pro

Estas son especificaciones funcionales propuestas, no afirmaciones de que ya estén implementadas:
1. **Ruta de la lección:** teoría, ejemplo, video, práctica, evaluación y evidencia en una secuencia visible.
2. **Panel de video:** reproductor/enlace externo, idioma, subtítulos, duración verificada, objetivo y notas del estudiante.
3. **Modo activo:** preguntas de predicción antes del video y preguntas de recuperación después; evitar reproducción pasiva como criterio de avance.
4. **Notas vinculadas:** guardar apuntes y marcas de tiempo asociadas a la lección, sin copiar transcripciones protegidas.
5. **Repaso espaciado:** programar revisiones configurables según desempeño; permitir ajustar y pausar la agenda.
6. **Quizzes con explicación:** explicar por qué una respuesta es correcta o incorrecta, registrar intentos y permitir reintentos.
7. **Laboratorios y entregables:** checklist, instrucciones, entorno, resultados esperados y evidencia entregada.
8. **Progreso por competencias:** mostrar objetivos demostrados, pendientes y evidencias; no confundir porcentaje de videos vistos con dominio.
9. **Biblioteca de recursos:** filtrar por etapa, módulo, idioma, nivel, tipo de recurso y estado de vigencia.
10. **Calidad y caducidad:** registrar quién verificó el enlace y cuándo; detectar recursos rotos o desactualizados mediante revisión editorial.

La implementación debe integrarse con los modelos y servicios existentes de CodeGuard Pro tras inspeccionar su arquitectura real. No crear tablas, APIs, estados ni migraciones por suposición.
