# Auditoría preliminar — Etapa 0 ASCENSO 3.1

**Fecha:** 2026-11-24  
**Rama:** `content/ascenso-stage-0-learning-method`  
**Estado:** diagnóstico preliminar; no es aprobación pedagógica.

## Alcance

Se inspeccionaron los cuatro documentos de módulo existentes en `docs/academic/ascenso-3.1/etapa-00/`, el estándar editorial, la política audiovisual y el contrato de importación de contenido de esta rama.

La etapa 0 contiene 30 lecciones nominales: 8 en 0.1, 7 en 0.2, 8 en 0.3 y 7 en 0.4. Los cuatro documentos existentes cubren los títulos curriculares, pero el nivel de desarrollo no es uniforme.

## Inventario documental

| Módulo | Tamaño aproximado | Encabezados internos | Menciones de ejercicios | Enlaces HTTPS | Candidatos YouTube |
|---|---:|---:|---:|---:|---:|
| 0.1 Aprender a aprender | 31.257 caracteres | 66 | 20 | 13 | 2 |
| 0.2 Investigación técnica | 11.169 caracteres | 13 | 5 | 9 | 2 |
| 0.3 Herramientas | 7.592 caracteres | 14 | 6 | 8 | 1 |
| 0.4 Depuración | 6.459 caracteres | 14 | 4 | 5 | 1 |

Los conteos son métricas de estructura del Markdown, no medidas de calidad ni pruebas de que los ejercicios estén resueltos o ejecutados.

## Hallazgos por módulo

### 0.1 — Aprender a aprender

Fortalezas:
- Es el documento más desarrollado.
- Tiene ocho lecciones, objetivos y explicaciones extensas.
- Integra estrategias de recuperación, espaciado, elaboración y práctica.
- Los dos videos listados permanecen expresamente como candidatos pendientes de escuchar.

Pendientes:
- Revisar cada afirmación de psicología del aprendizaje contra la fuente primaria o revisión citada.
- Verificar que cada ejercicio mida el objetivo anunciado y tenga criterio/solución razonada.
- Comprobar que las técnicas se presenten como estrategias dependientes de tarea y contexto, no como garantías universales.
- Revisar que el proyecto integrador produzca evidencias y una rúbrica aplicable.

### 0.2 — Investigación técnica

Fortalezas:
- Los siete temas oficiales están presentes.
- El módulo propone una bitácora y una rúbrica de investigación.
- Incluye precauciones para secretos, ejecución de código y evaluación de repositorios.

Pendientes:
- Profundizar cada tema como una lección autocontenida: objetivos, pasos, ejemplo resuelto, ejercicio, solución, criterios y referencias.
- Separar investigación de documentación, preguntas, foros y repositorios sin repetir la misma explicación.
- Los dos videos son candidatos; el propio documento deja pendiente escuchar el audio real y revisar la correspondencia completa. No recomendarlos todavía.

### 0.3 — Herramientas

Fortalezas:
- Conserva los ocho temas oficiales: VS Code, terminal, Git, GitHub, navegador/DevTools, Markdown, Draw.io y diagramación.
- Advierte sobre privilegios, secretos y herramientas confiables.

Pendientes:
- Desarrollar laboratorios verificables por herramienta, con comandos y resultados esperados para Linux como entorno prioritario actual.
- Aclarar diferencias entre Bash/Zsh/PowerShell/CMD sin convertir el módulo introductorio en un manual exhaustivo de cada sistema.
- Añadir prácticas de Git con repositorio de prueba, staging, commit, branch, merge y recuperación segura.
- Revisar el video de MoureDev por su cobertura real: el título se centra en Git/GitHub y no demuestra que cubra VS Code, terminal, DevTools, Markdown o diagramación. Como máximo podrá asociarse a las lecciones de Git/GitHub tras escuchar y verificar el contenido.

### 0.4 — Depuración

Fortalezas:
- El ciclo general de depuración es correcto como base: reproducir, reducir, formular hipótesis, observar, corregir y probar regresiones.
- Incluye stack traces, logs y seguridad de información.

Pendientes:
- Añadir ejemplos guiados separados para breakpoints, stack traces y logs.
- Incluir un laboratorio con defectos deliberados, casos de prueba, hipótesis rivales y una corrección comprobada.
- Enseñar a diferenciar ubicación donde se manifiesta un fallo y causa raíz.
- El video candidato de resolución de bugs es general; no asumir que cubre breakpoints, stack traces o logs. Revisar cada subtema antes de asignarlo.

## Hallazgo transversal: videos

Los documentos cumplen la regla editorial de no presentar los enlaces como aprobados. Sin embargo, varios candidatos tienen títulos amplios y podrían no cubrir todos los objetivos del módulo.

Antes de aprobar cualquier video se debe:
1. escuchar el audio real y confirmar español hablado;
2. revisar contenido y segmentos;
3. mapear minutos/segmentos a objetivos concretos;
4. registrar fecha, duración y subtítulos realmente disponibles;
5. decidir si complementa la lección o si es mejor dejarla sin video.

No se aprueba un video por el nombre del canal, por el título ni por subtítulos automáticos.

## Hallazgo transversal: importación y UUID

El importador de PR #14 exige UUID reales de lección, ejemplo, ejercicio y fuente, además de identidad curricular coincidente con la base de datos. Los paquetes deben prepararse a partir del manifiesto de la instalación de desarrollo y validarse primero sin escribir.

No se debe:
- inventar UUID;
- usar el JSON de contenido de otra rama como paquete compatible;
- importar documentos con UUID de ejemplo/ejercicio que no pertenezcan a la lección;
- registrar fuentes ficticias o no activas;
- aprobar o publicar durante la importación.

El manifiesto exportado puede contener identificadores de una instalación; debe mantenerse fuera del repositorio público.

## Prioridades de mejora

1. **0.1:** auditoría técnica y pedagógica individual de sus ocho lecciones.
2. **0.2:** ampliar cada una de las siete lecciones y crear ejercicios con soluciones y rúbricas.
3. **0.3:** crear ocho laboratorios breves y reproducibles; priorizar Linux sin borrar notas multiplataforma.
4. **0.4:** construir laboratorio de depuración con defectos controlados y evidencia de corrección.
5. **Videos:** mantener candidatos pendientes hasta verificación completa.
6. **Importación:** obtener manifiesto privado y mapear UUID antes de preparar paquetes.

## Conclusión

La etapa 0 tiene una base documental real en los cuatro módulos, por lo que no es necesario empezar desde cero. No obstante, el nivel de detalle y evaluabilidad es desigual: 0.1 es más extenso; 0.2–0.4 requieren ampliación práctica y evaluativa. Ninguno debe considerarse aprobado o publicado por el solo hecho de existir en Markdown.

La siguiente entrega debe ser una revisión individual de las ocho lecciones de 0.1 y un lote mejorado de 0.2, conservando los documentos existentes y registrando cambios de forma trazable.
