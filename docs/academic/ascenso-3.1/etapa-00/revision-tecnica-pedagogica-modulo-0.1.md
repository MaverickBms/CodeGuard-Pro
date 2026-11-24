# Revisión de escritorio — Módulo 0.1 «Aprender a aprender»

**Fecha:** 2026-11-24  
**Rama:** `content/ascenso-stage-0-learning-method`  
**Documento revisado:** `modulo-0.1-aprender-a-aprender.md`  
**Tipo de revisión:** inspección editorial y de alineación interna; no equivale a revisión independiente ni a validación experimental.  
**Estado:** hallazgos preliminares; módulo BORRADOR.

## Alcance y método

Se contrastaron los ocho títulos y el orden de las lecciones con `apps/roadmaps/data/ascenso_3_1.json`. Para cada lección se inspeccionó la presencia y coherencia visible de objetivos, explicación, ejemplo, actividad, criterios de evaluación, autoevaluación/solución y referencias. También se buscó que la evidencia propuesta permita observar el verbo del objetivo.

No se evaluó a estudiantes, no se midió retención, no se verificaron experimentalmente las afirmaciones educativas y no se ejecutaron actividades. Los resultados describen el documento, no el aprendizaje real.

## Resultado ejecutivo

- Correspondencia de títulos y orden: **8/8**.
- Lecciones con objetivos explícitos: **8/8**.
- Lecciones con alguna actividad o tarea identificable: **8/8**.
- Lecciones con criterios de evaluación visibles: **8/8**.
- Lecciones con ejemplos resueltos, fichas o guías de retroalimentación adicionales incorporadas en esta iteración: **0.1.2–0.1.7**.
- Proyecto 0.1.8 con criterios de aceptación por hito: **incorporados**.
- Referencias educativas del módulo: presentes en una bibliografía común; su correspondencia afirmación por afirmación y vigencia requieren revisión especializada.
- Validación independiente o empírica: **0/8**.

La existencia de objetivos, actividades y criterios es una condición estructural, no prueba suficiente de validez pedagógica. No se asigna estado APROBADO a ninguna lección.

## Matriz individual

| Lección oficial | Evidencia de desempeño que debe producir el estudiante | Hallazgo de escritorio | Ajuste necesario antes de revisión independiente |
|---|---|---|---|
| 0.1.1 Aprendizaje activo | Transformar un recurso en preguntas, predicciones, recuperación sin apuntes y una aplicación nueva; corregir la respuesta al contrastarla. | La secuencia antes/durante/después y el ejemplo de variable alinean bien con los objetivos. Incluye ejercicios y respuestas orientativas. | Pendiente: consolidar una rúbrica de niveles y asociar fuentes educativas a afirmaciones específicas. |
| 0.1.2 Pensamiento crítico | Entregar una ficha de verificación de una afirmación técnica: formulación, fuente primaria, versión/contexto, evidencia, límites y grado de confianza. | Explica la diferencia entre crítica y desconfianza y modela una afirmación falsable. Hay criterios, pero la tarea y la retroalimentación deben quedar más explícitas. | Se incorporó una ficha resuelta sobre `git status` con fuente primaria, límite y conclusión calibrada. Pendiente: añadir contraste con fuente secundaria y caso de evidencia insuficiente. |
| 0.1.3 Método Feynman | Presentar una explicación inicial, marcar vacíos, consultar una fuente y entregar una versión corregida con ejemplo propio. | La rutina de cuatro pasos y el ejemplo de función son adecuados como autoexplicación; se evita atribuirle eficacia mágica al nombre. | Se añadió producto mínimo y ejemplo resuelto sobre IPv4, con límite explícito de la analogía y rúbrica breve. Pendiente: revisar la fuente técnica primaria que el estudiante debe consultar. |
| 0.1.4 Repetición espaciada | Diseñar un calendario de dos semanas con intentos de recuperación, resultados, errores y ajuste de intervalos. | Se aclara que el calendario es ilustrativo y no universal; el ejercicio propone comandos de terminal. | Se incorporó una plantilla de registro con tres sesiones y decisiones de ajuste. Pendiente: revisión independiente de las referencias educativas. |
| 0.1.5 Práctica deliberada y enfocada | Definir una habilidad acotada, tarea con dificultad apropiada, criterio, retroalimentación, error y siguiente iteración. | El texto evita afirmar que la práctica explique por sí sola el rendimiento experto. El ejemplo de depuración hace concreta la meta. | Se añadió un ejemplo de tres sesiones, evidencia observable y una advertencia explícita de que el tiempo no demuestra dominio. Pendiente: validar la calidad de los mecanismos de feedback. |
| 0.1.6 Resolución de problemas | Entregar especificación de entradas/salidas/restricciones, pseudocódigo, casos normal/límite/inválido y comparación esperado/obtenido. | El proceso y el ejemplo de compra introducen supuestos y casos límite. | Se añadió pseudocódigo de referencia, supuesto explícito de escala 0–100 y cinco casos de prueba, incluidos límites y entradas inválidas. Pendiente: revisión técnica independiente. |
| 0.1.7 Descomposición de problemas complejos | Presentar árbol o diagrama de subproblemas, responsabilidades, entradas/salidas, errores y dependencias; justificar cobertura. | El ejemplo de inventario propone responsabilidades razonables y no anticipa decisiones tecnológicas fuera de alcance. | Se añadió una tabla de responsabilidades, entradas, salidas, errores y dependencias, con recorrido de cobertura y nota de que no es la única descomposición válida. Pendiente: revisión independiente. |
| 0.1.8 Aprendizaje basado en proyectos | Entregar una versión incremental de ASCENSO-Knowledge-Base, decisiones justificadas, registro de cambios, autoevaluación y reflexión final. | Contiene mini proyecto, rúbrica y material de curación audiovisual. La sección es considerablemente más extensa y mezcla contenido de lecciones previas, recursos y matrices. | Se añadieron criterios de aceptación por hito y evidencias revisables. Pendiente: revisión de consistencia entre esta rúbrica y la rúbrica general del proyecto; curación audiovisual sigue pendiente. |

## Hallazgos transversales

### 1. Alineación constructiva

La mayoría de las lecciones presentan verbos observables, pero la evidencia final no siempre está empaquetada en un entregable fácil de revisar. Cada lección debería terminar con: (a) producto, (b) criterio de aceptación, (c) ejemplo o clave, (d) reflexión sobre error y (e) fuente de contraste cuando corresponda.

### 2. Evaluación y retroalimentación

Los criterios redactados como listas de comprobación son útiles para principiantes, pero todavía no forman una escala consistente. Para revisión independiente, utilizar una rúbrica común de cuatro niveles: **0 — ausente**, **1 — parcial**, **2 — correcto con ayuda**, **3 — correcto y justificado de forma autónoma**. No convertir la puntuación en aprobación automática: los criterios críticos de exactitud y seguridad deben cumplirse.

### 3. Fuentes y afirmaciones

Deben distinguirse:
- afirmaciones sobre aprendizaje humano, que requieren literatura educativa o revisiones pertinentes;
- afirmaciones sobre herramientas o lenguajes, que deben apuntar a documentación primaria y versión/contexto;
- ejemplos creados para el curso, que deben marcarse como ejemplos didácticos y no como resultados empíricos.

La presencia de una URL no acredita que la fuente respalde una afirmación concreta. Se debe registrar autor/organización, título, fecha o versión, afirmación respaldada y fecha de consulta.

### 4. Recursos audiovisuales

Los enlaces audiovisuales siguen siendo candidatos. No se recomienda asignarlos hasta escuchar el audio, verificar idioma, revisar el contenido completo y mapear segmentos a objetivos. Un título o descripción del canal no basta.

### 5. Accesibilidad y carga cognitiva

Usar instrucciones numeradas, glosario de términos nuevos, ejemplos de entrada/salida y alternativas textuales a diagramas o capturas. Mantener las tareas pequeñas y no introducir configuración de herramientas cuando el objetivo sea una estrategia de aprendizaje.

## Criterios de salida para cada lección

Una lección solo podrá pasar a revisión independiente cuando tenga:
1. objetivo observable y acotado;
2. explicación conceptualmente correcta y delimitada;
3. ejemplo resuelto paso a paso;
4. actividad individual con instrucciones y datos suficientes;
5. producto/evidencia identificable;
6. criterios de aceptación alineados con el objetivo;
7. solución razonada o guía de retroalimentación;
8. referencias trazables para afirmaciones externas;
9. nota de seguridad/privacidad cuando la actividad maneje datos, código o cuentas;
10. versión y fecha de revisión.

La revisión independiente debe registrar nombre/rol del revisor, fecha, hallazgo, severidad, corrección y resultado de re-verificación. No se inventan revisores ni firmas en este documento.

## Decisiones y límites

- Se conserva intacto el currículo maestro y el orden oficial de ocho lecciones.
- No se declara ninguna lección APROBADA, REVISADA ni PUBLICADA.
- No se atribuye evidencia de eficacia a resultados no medidos.
- No se verificaron videos ni se ejecutaron laboratorios en esta revisión.
- El objetivo de esta entrega es hacer explícitos los vacíos que debe cerrar la siguiente iteración, no inflar el porcentaje de completitud.

## Seguimiento de la segunda iteración — 2026-11-24

Se incorporaron a las secciones de las lecciones 0.1.2–0.1.7 una ficha de contraste de fuentes, un ejemplo de autoexplicación, una plantilla de repasos, un registro de práctica enfocada, un algoritmo con casos de prueba y una descomposición de referencia. En 0.1.8 se añadieron criterios de aceptación por hito. La colocación de estos materiales se comprobó contra los encabezados oficiales para evitar que una solución quedara asociada a la lección equivocada.

Esta iteración mejora la verificabilidad documental, pero no convierte el módulo en validado: no se ejecutaron las actividades con estudiantes, no se probó una implementación de software, no se escucharon los videos y no hubo revisor externo.

## Próximo trabajo recomendado

1. Revisión de exactitud y trazabilidad de referencias educativas y técnicas por un especialista independiente.
2. Revisar la coherencia entre rúbrica de la lección 0.1.8 y rúbrica del proyecto integrador.
3. Completar las claves y criterios pendientes de 0.1.1 y 0.1.2; normalizar la ubicación de las autoevaluaciones complementarias.
4. Verificar audiovisual y accesibilidad de los recursos candidatos antes de asignarlos.
5. Ejecutar las actividades con un grupo piloto y registrar observaciones, sin convertir una muestra pequeña en prueba general de eficacia.
