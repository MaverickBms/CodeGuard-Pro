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


---

## Seguimiento de producción — 2026-11-24

**Rama:** `content/ascenso-stage-0-learning-method`  
**Alcance de esta actualización:** profundización documental y alineación de los módulos 0.2, 0.3 y 0.4. No se modificó el JSON maestro ni la aplicación.

### 1. Resultado curricular comprobado

El archivo `apps/roadmaps/data/ascenso_3_1.json` fue parseado en esta revisión. Resultado: **33 etapas, 212 módulos y 1.946 lecciones nominales**. La etapa 0 conserva cuatro módulos y 30 lecciones nominales. El JSON declara como fuente el DOCX maestro y su SHA-256 ya registrado en el inventario. La estructura y sus títulos no fueron modificados.

Los siete prerrequisitos se conservan según el inventario contrastado con el DOCX: el JSON no serializa las relaciones de prerrequisito, por lo que no se reconstruyen a partir de él.

### 2. Cambios documentales realizados

| Archivo | Cambio comprobable | Estado |
|---|---|---|
| `etapa-00/modulo-0.2-investigacion-tecnica.md` | Se añadieron siete talleres canónicos con ejemplos, tareas, evidencia, criterios, retroalimentación, evaluación analítica y referencias; se separó el material heredado como apéndice para preservar el orden oficial. | BASE DE TRABAJO ACTIVA |
| `etapa-00/modulo-0.3-herramientas.md` | Se añadieron procedimientos y ejercicios para VS Code, terminal, Git, GitHub, DevTools, Markdown y Draw.io; se separó explícitamente 0.3.8 «Herramientas de diagramación». | BORRADOR |
| `etapa-00/modulo-0.4-depuracion.md` | Se añadieron casos de debugging, breakpoints, stack traces, logs, hipótesis, reproducción y análisis de causas en el orden oficial; se diseñó un laboratorio con defecto de frontera, pruebas y solución razonada. | BORRADOR |
| `etapa-00/modulo-0.1-aprender-a-aprender.md` | Se conserva el documento previo con ocho lecciones desarrolladas como base de trabajo activa; no se ha declarado superada su auditoría individual. | BORRADOR |

La ampliación de los cuatro módulos no convierte automáticamente una lección en «desarrollada» ni un laboratorio en «ejecutado». Los ejemplos de código y comandos incorporados son propuestas didácticas no ejecutadas en este entorno.

### 3. Matriz de estado editorial y evidencias

| Indicador | Estado real al 2026-11-24 |
|---|---:|
| Etapas con documento de desarrollo | 33/33 |
| Módulos de la etapa 0 con documento | 4/4 |
| Lecciones nominales de etapa 0 cubiertas por los cuatro documentos | 30/30 |
| Lecciones de etapa 0 con auditoría técnica, pedagógica, práctica y editorial independiente completada | 0/30 |
| Módulos de etapa 0 como base de trabajo activa | 4/4 |
| Lecciones aprobadas | 0 |
| Lecciones publicadas en la aplicación | 0 |
| Laboratorios escritos en los documentos 0.2–0.4 | 3 (más actividades del módulo 0.1) |
| Laboratorios ejecutados y verificados en esta sesión | 0 |
| Videos verificados mediante escucha/revisión del contenido | 0 |
| Videos candidatos aún pendientes de verificación | 6 |
| Manifiesto de UUID exportado desde una base real | No disponible |
| Paquetes JSON v1 validados | 0 |
| Importaciones, aprobaciones o publicaciones realizadas | 0 |

**Interpretación:** 30/30 significa que los títulos oficiales tienen cobertura documental inicial en los cuatro módulos. No significa que las 30 lecciones estén completas ni aprobadas. No se contabilizan títulos como lecciones desarrolladas.

### 4. Verificación técnica y pedagógica pendiente

- **0.1:** auditar las ocho lecciones individualmente, especialmente la correspondencia entre evidencia pedagógica, ejercicios, soluciones y rúbricas; la ampliación de recuperación no equivale a revisión independiente.
- **0.2:** comprobar en un entorno controlado los pasos y ejemplos que se decida ejecutar; revisar que las páginas de documentación sigan vigentes al preparar una versión publicable.
- **0.3:** ejecutar por separado los recorridos de Bash/Zsh, PowerShell o CMD que correspondan; validar el laboratorio de Git en un repositorio descartable y la inspección DevTools en una página propia.
- **0.4:** ejecutar el laboratorio Python, comprobar que las pruebas fallan antes y pasan después, y verificar el procedimiento de breakpoint en un runtime real.
- **Fuentes:** se añadieron referencias oficiales o primarias pertinentes para los temas tratados. La revisión de enlaces realizada no equivale a una revisión exhaustiva de cada afirmación de los cuatro módulos.
- **Videos:** se mantienen como candidatos. No se ha escuchado el audio real de ninguno ni se han verificado duración y segmentos; no deben mostrarse como recomendados.

### 5. Importación y restricciones

El exportador `exportar_manifiesto_academico` existe en la rama y es de solo lectura. No se ha ejecutado contra una base de datos real en esta sesión; por ello no hay UUID de destino disponibles. No se generó paquete de importación ni se ejecutó un dry-run del importador, porque sin manifiesto real no es posible construir un lote legítimo. No se ha escrito contenido en SQLite, aprobado ni publicado.

La etapa 25 mantiene el campo `objetivo` vacío en el JSON. No se propone ni se registra aquí un objetivo formal alternativo.

### 6. Próxima secuencia de trabajo

1. Completar la auditoría de las ocho lecciones de 0.1 y registrar una matriz objetivo–evidencia–fuente–criterio.
2. Ejecutar los laboratorios de 0.2–0.4 en entornos aislados y adjuntar resultados reproducibles.
3. Realizar revisión técnica y pedagógica independiente de cada lección, corregir y registrar hallazgos.
4. Auditar el proyecto ASCENSO-Knowledge-Base como integrador de la etapa.
5. Obtener el manifiesto privado real desde la instalación de desarrollo, sin subir sus UUID al repositorio público.
6. Solo entonces diseñar y validar en seco un primer paquete JSON v1 con UUID y fuentes existentes.

**Estado general de la etapa 0:** BASE DE TRABAJO ACTIVA. Los cuatro módulos son la referencia operativa vigente. Esta condición no significa que cada lección esté revisada de forma independiente, aprobada o publicada; esas distinciones se mantienen según las evidencias registradas.


### 7. Proyecto integrador ASCENSO-Knowledge-Base

Se añadió `docs/academic/ascenso-3.1/etapa-00/proyecto-integrador-ascenso-knowledge-base.md`, alineado con el proyecto indicado por el JSON maestro. La especificación incluye contexto, resultados observables, requisitos funcionales/no funcionales, estructura de referencia, plantillas, fases conectadas con los cuatro módulos, entregables, criterios de validación, rúbrica analítica, errores frecuentes y registro de ejecución.

**Estado:** BASE DE TRABAJO ACTIVA. Se ha redactado la especificación; el repositorio del estudiante no se ha creado, no se han producido entregables, no se ha ejecutado una revisión por pares y no se ha aprobado ni publicado el proyecto.


### 8. Revisión de escritorio del módulo 0.1

Se creó `etapa-00/revision-tecnica-pedagogica-modulo-0.1.md` con una inspección individual de las ocho lecciones. La revisión contrasta objetivos, ejemplos, actividades, evidencias, criterios, autoevaluación y fuentes, y propone criterios de salida para una revisión independiente.

**Resultado:** los ocho títulos oficiales y su orden están presentes; las ocho lecciones contienen objetivos, actividades y criterios identificables. Esto es una comprobación estructural/editorial, no una validación de aprendizaje ni una aprobación. Se identificaron ajustes específicos: fortalecer la ficha de verificación de fuentes en 0.1.2; añadir producto y rúbrica a 0.1.3; plantilla y ajuste de intervalos en 0.1.4; ejemplo de retroalimentación en 0.1.5; solución de referencia con casos de prueba en 0.1.6; descomposición resuelta en 0.1.7; y separar anexos/material audiovisual de la lección 0.1.8.

**Estado:** 0/8 lecciones aprobadas; 0/8 con revisión independiente completa; 0 actividades ejecutadas en esta revisión. Los seis videos candidatos siguen sin verificación audiovisual. El informe no altera el currículo ni eleva el estado editorial del módulo.


### 9. Segunda iteración del módulo 0.1

Se completaron mejoras documentales específicas en las lecciones 0.1.2–0.1.8: ficha de verificación de fuentes con conclusión calibrada; ejemplo resuelto de autoexplicación; registro de práctica espaciada; ejemplo de tres sesiones con feedback; pseudocódigo del promedio con supuesto de escala declarado y cinco casos de prueba; descomposición de referencia de biblioteca; y criterios de aceptación verificables para los cinco hitos del proyecto de aprendizaje.

La revisión se mantuvo dentro de los encabezados de las lecciones oficiales. Se hizo una comprobación estática de los ocho títulos, presencia de objetivos/criterios y balance de bloques de código Markdown. El JSON curricular se volvió a leer y no se modificó.

**Estado actualizado del módulo 0.1:** 8/8 lecciones con ampliación documental de objetivos/actividades; ejemplos y guías adicionales incorporados en 0.1.2–0.1.8; 0/8 revisiones independientes; 0 aprobadas; 0 actividades probadas con estudiantes; 0 videos verificados. Se mantiene como base de trabajo activa. Los chequeos estáticos no son una validación pedagógica ni una ejecución de código.


### 10. Desarrollo y revisión de escritorio del módulo 0.2

Se añadieron claves modelo para los siete temas de investigación técnica: documentación y versiones; diagnóstico de errores; evaluación de respuestas comunitarias; trazabilidad issue/PR/commit/release; licencia y adopción de repositorios; calibración de afirmaciones; y reporte reproducible. Los ejemplos están marcados como simulados. Se creó `etapa-00/revision-tecnica-pedagogica-modulo-0.2.md` con matriz por tema, riesgos y criterios de salida.

**Estado:** 7/7 temas con talleres; 7/7 con claves o retroalimentación modelo añadidas; 0 revisiones independientes; 0 laboratorios ejecutados; 0 videos verificados; 0 aprobaciones. No se ejecutaron comandos ni código ni se clonaron repositorios.


### 11. Revisiones de escritorio de los módulos 0.3 y 0.4

Se crearon informes de revisión de escritorio para los módulos de herramientas y depuración. El primero inspecciona los ocho temas, con énfasis en portabilidad de comandos por shell, operaciones Git potencialmente destructivas, privacidad en DevTools y conservación de fuentes editables de diagramas. El segundo inspecciona los siete temas y la lógica del laboratorio de factura: el contrato y los tres resultados esperados son aritméticamente coherentes por revisión estática, pero ni el código ni las pruebas se ejecutaron.

**Estado común de módulos 0.1–0.4:** existen revisiones de escritorio documentales para los cuatro módulos; ninguna equivale a revisión independiente ni validación práctica. Se mantienen 0 laboratorios ejecutados, 0 videos verificados, 0 módulos aprobados y 0 módulos publicados. Los informes están enlazados desde el README académico.

### 12. Comprobación de consistencia de encabezados — 2026-11-24

Se volvió a contrastar el JSON curricular oficial con los encabezados de los cuatro documentos de la etapa 0. La comprobación es estática y se limita a identificadores y encabezados Markdown; no evalúa la calidad ni la suficiencia didáctica del contenido.

| Módulo | Lecciones nominales en JSON | Encabezados numerados localizados | Resultado estructural |
|---|---:|---:|---|
| 0.1 | 8 | 8 encabezados principales «Lección 0.1.n» | Coincide |
| 0.2 | 7 | 7 encabezados «Lección 0.2.n» en la sección de profundización | Coincide tras normalizar la etiqueta «Taller» a «Lección» |
| 0.3 | 8 | 8 encabezados numerados 0.3.1–0.3.8 en la profundización | Coincide; 0.3.7 y 0.3.8 permanecen diferenciados |
| 0.4 | 7 | 7 encabezados numerados 0.4.1–0.4.7 en la profundización | Coincide |

En 0.2 se normalizó la etiqueta de los siete encabezados canónicos de «Taller» a «Lección», sin cambiar su numeración ni sus títulos, para que la unidad curricular no se confunda con el formato de actividad. Las claves de práctica y los encabezados de apéndices no se cuentan como lecciones adicionales. En 0.3, los seis encabezados introductorios y los apéndices heredados tampoco se suman al conteo: la serie numerada de la profundización es la que cubre las ocho unidades del JSON.

**Límite de esta comprobación:** la coincidencia 8/7/8/7 demuestra trazabilidad estructural de las unidades, no que cada lección haya superado revisión técnica, pedagógica, práctica o de fuentes. Los cuatro módulos se mantienen como BASE DE TRABAJO ACTIVA; no se declara aprobación ni publicación.
