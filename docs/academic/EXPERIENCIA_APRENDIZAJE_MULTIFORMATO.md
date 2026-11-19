# Curación audiovisual y experiencia de aprendizaje ASCENSO 3.1

**Estado:** propuesta editorial/funcional v0.1.0.  
**Fecha:** 2026-11-19.  
**Alcance inicial:** Etapa 0; ampliable a las etapas 1–32.

## Propósito

Complementar el material escrito con recursos audiovisuales útiles, preferiblemente en español, y convertir su consumo en una actividad de aprendizaje activo. El objetivo no es llenar las lecciones de videos: es seleccionar pocos recursos de calidad que expliquen conceptos desde otra perspectiva y conduzcan a una práctica verificable.

## Principios

1. Primero se define el objetivo de aprendizaje; después se busca el video.
2. Español como idioma preferente.
3. En inglés: comprobar subtítulos en español dentro de YouTube o proporcionar alternativa equivalente en español.
4. Enlazar siempre al video original y respetar derechos de autor.
5. No asumir duración, subtítulos, idioma o vigencia sin verificarlos.
6. La calidad didáctica y exactitud prevalecen sobre la fama del canal.
7. Ver un video no completa una lección ni una etapa.

## Canales candidatos

Los siguientes nombres proceden de la lista sugerida por el estudiante. Son candidatos para buscar piezas concretas; su inclusión aquí no implica que cada canal tenga un video aprobado para cada etapa.

- MoureDev
- midudev
- Fireship
- Mosh Hamedani
- HolaMundo
- The Net Ninja
- DotCSV
- Héctor de León
- Ania Kubów
- The Cherno
- Alex Profe
- Daniel Carreon
- Julio Profe

Se podrán incorporar otros canales, universidades, instituciones y mantenedores oficiales si la pieza concreta mejora el aprendizaje.

## Metadatos mínimos de un recurso

| Campo | Regla |
|---|---|
| Título y creador | Exactos, contrastados con la página original. |
| URL | Enlace canónico al recurso original. |
| Idioma hablado | Español, inglés u otro. |
| Subtítulos | Idioma, tipo y estado de verificación. |
| Duración | Solo si la página/reproductor la confirma. |
| Nivel | Inicial, intermedio o avanzado, justificado por prerrequisitos. |
| Temas | Conceptos que realmente aborda. |
| Relación curricular | Etapa, módulo y objetivo al que aporta. |
| Actividad | Pregunta, ejercicio o práctica posterior. |
| Verificación | Fecha, estado del enlace y observaciones editoriales. |

## Funciones de experiencia de aprendizaje

### 1. Secuencia multimodal

La lección organiza teoría, video, ejemplo, práctica, evaluación y proyecto. El estudiante puede consultar el video cuando quiera, pero el avance se calcula mediante competencias y evidencias, no por tiempo de reproducción.

### 2. Video con guía de observación

Antes de reproducir: mostrar una pregunta que active conocimientos previos.  
Durante: permitir notas y marcas de tiempo.  
Después: pedir explicación propia, contraste con documentación y ejercicio independiente.

### 3. Subtítulos y accesibilidad

Priorizar audio en español. Para material inglés, ofrecer subtítulos españoles verificados y una alternativa en español. Indicar que la disponibilidad puede variar por dispositivo/cuenta y no garantizar la precisión de subtítulos automáticos.

### 4. Repaso y recuperación

Crear preguntas cortas de recuperación, tarjetas de conceptos y sesiones espaciadas configurables. La agenda debe adaptarse al desempeño y permitir que el estudiante entienda por qué se programa cada repaso.

### 5. Laboratorios y evidencias

Cada laboratorio debe indicar objetivo, prerrequisitos, entorno, pasos, resultado esperado, solución orientativa, riesgos y evidencia de finalización. Un laboratorio no se etiqueta como probado si no se ejecutó en el entorno declarado.

### 6. Seguimiento por competencias

Mostrar progreso por objetivos: pendiente, en práctica y demostrado. La finalización requiere una evaluación o evidencia que respalde el dominio. No convertir el porcentaje de videos vistos en un indicador de competencia.

### 7. Biblioteca audiovisual

Filtros por etapa, módulo, idioma, nivel, canal, tema y estado de vigencia. Los recursos con enlace o subtítulos no comprobados se mantienen como candidatos editoriales, no como material recomendado.

## Flujo editorial de recursos

Candidato → comprobación de enlace y metadatos → revisión de pertinencia y calidad → actividad de aprendizaje asociada → revisión editorial → aprobación → publicación → mantenimiento o retirada.

## Primera curación: Etapa 0 / Módulo 0.1

- [midudev — ¿Cómo me ORGANIZO? Mi SECRETO para ser más PRODUCTIVO y APRENDER más rápido programación](https://www.youtube.com/watch?v=UZarokfByTs) — español; organización, apuntes y tareas. Actividad: diseñar un sistema de notas propio y justificar qué se adapta y qué no.
- [Academia de Hostinger — Cómo Aprender a Programar | Consejos y Recursos](https://www.youtube.com/watch?v=Zf48b175sKo) — español; objetivos, herramientas y proyectos. Actividad: comparar sus recomendaciones con la secuencia y el foco de ASCENSO.
- [MoureDev Pro — Ruta de estudio](https://mouredev.pro/roadmap) — recurso web oficial complementario, no video individual de YouTube; el sitio presenta un curso para principiantes titulado «Cómo estudiar programación». Actividad: comparar estrategias de estudio, sin sustituir el roadmap ASCENSO.
- [Fireship — How to Learn to Code - 8 Hard Truths](https://www.youtube.com/watch?v=NtfbWkxJTHw) — inglés; candidato para revisión. No se considera aprobado para el estudiante hasta comprobar subtítulos españoles en el reproductor y definir alternativa en español.

## Mantenimiento

Revisar los recursos antes de publicar una etapa y periódicamente. Si un enlace deja de funcionar, cambia de idioma o pierde subtítulos, marcarlo para revisión y sustituirlo con trazabilidad. La curación debe mantenerse como datos editoriales versionados, no como enlaces incrustados sin control dentro del texto.


## Alineación con capacidades existentes de CodeGuard Pro

Inspección estática de `release/1.0.0` (19-11-2026) confirmó que el proyecto ya contiene modelos y vistas para lecciones, contenido didáctico, ejemplos, ejercicios, intentos, quizzes, resultados, progreso por etapa/módulo/lección/actividad, criterios de finalización, fuentes de conocimiento y versiones editoriales. Por tanto, las funciones propuestas deben ampliar y conectar estas capacidades, no duplicarlas.

| Capacidad | Estado observado en el código | Trabajo recomendado |
|---|---|---|
| Lecciones y contenido | Existen `Leccion` y `ContenidoLeccion`; la vista de lección obtiene contenido activo. | Ampliar contenido por plantilla y asociar recursos sin romper el flujo editorial. |
| Ejemplos y ejercicios | Existen modelos y flujo de intentos para ejercicios. | Añadir actividades específicas de observación/reflexión de videos como actividades normales, si el modelo lo permite. |
| Quizzes | Existen `Quiz`, preguntas, resultados, historial y vista de evaluación. | Reutilizar para recuperación activa; enriquecer feedback y preguntas de aplicación si la arquitectura lo permite. |
| Progreso | Existe `Progreso` por distintos niveles y criterios de finalización con evidencias. | Medir objetivos demostrados y no tiempo de reproducción; revisar la semántica actual antes de cambiar porcentajes. |
| Fuentes y versiones | Existen fuentes de conocimiento y versiones de contenido con flujo editorial. | Registrar videos como referencias externas con metadatos; no asumir que el modelo actual tiene campos de subtítulos o caducidad. |
| Notas y marcas de tiempo | No se confirmó un modelo específico de notas audiovisuales. | Evaluar si se puede reutilizar notas/actividades existentes o si justifica una extensión pequeña. |
| Repaso espaciado | No se confirmó un planificador de repetición espaciada. | Diseñar primero reglas, privacidad y persistencia; después decidir implementación. |
| Catálogo audiovisual | No se confirmó un modelo específico para recursos audiovisuales. | Diseñar integración con fuentes editoriales y evitar almacenar copias de videos. |

### Restricciones de implementación

Esta revisión fue de código fuente en GitHub, no una ejecución de la aplicación. Antes de modificar modelos o vistas se debe revisar el flujo completo de versiones, aprobaciones, distribución y permisos; añadir pruebas unitarias, de integración y de interfaz; y ejecutar los checks del proyecto. No se declara implementada ni probada ninguna función nueva por el hecho de documentarla.


## Guía de subtítulos para estudiantes

En YouTube, abrir el video → seleccionar **Configuración** → **Subtítulos/CC** → elegir **Español**. Si no aparece, se puede probar **Traducir automáticamente → Español**, siempre que el video tenga una pista de subtítulos disponible. La opción puede no aparecer si el video no ofrece subtítulos.

La traducción automática puede cometer errores; para conceptos técnicos, nombres de APIs, comandos y terminología, contrastar con la explicación escrita y la documentación oficial. No se marcará un video como «subtítulos españoles verificados» solo porque YouTube tenga la opción general de traducción automática: la ficha debe registrar el estado observado en ese video concreto.

**Ayuda oficial de YouTube:**
- [Administrar la configuración de subtítulos](https://support.google.com/youtube/answer/100078)
- [Subtítulos automáticos y sus limitaciones](https://support.google.com/youtube/answer/6373554)


## Regla reforzada de selección audiovisual (obligatoria)

La condición es doble e indivisible:
1. El audio del video debe estar en español.
2. El contenido debe corresponder directamente al objetivo o subtema de la lección.

Un video en español sobre programación en general no es válido para una lección sobre Stack Overflow, breakpoints o bases de datos si no enseña ese contenido. La popularidad del canal tampoco demuestra pertinencia. Si no se encuentra un video que cumpla ambas condiciones, la lección se publica sin video hasta localizar uno adecuado. Los subtítulos no convierten un video en inglés en un recurso aceptable.
