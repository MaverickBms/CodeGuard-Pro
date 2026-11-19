# Etapa 0 · Módulo 0.1 — Aprender a aprender

**Roadmap:** ASCENSO 3.1 · Etapa 0 «Preparación y método de aprendizaje»  
**Prioridad:** P1 · Obligatoria  
**Estado editorial:** borrador académico piloto; no publicado en CodeGuard Pro  
**Versión:** 0.1.0 · **Fecha:** 2026-11-19  
**Público:** principiante sin experiencia técnica previa  
**Prerrequisitos:** ninguno  
**Carga estimada:** 8–12 horas, distribuibles en 2–3 semanas. Es una estimación didáctica, no una duración garantizada.

## Propósito del módulo

Aprender programación y tecnología exige más que leer explicaciones o mirar videos. El estudiante debe recuperar conocimientos, explicarlos, aplicarlos a problemas nuevos, detectar errores y revisar su desempeño. Este módulo enseña ocho estrategias que ayudarán a estudiar las siguientes etapas de ASCENSO.

La evidencia educativa respalda especialmente la práctica de recuperación, la distribución del estudio en el tiempo, la elaboración y el uso de ejemplos concretos. Ninguna técnica garantiza por sí sola el éxito: el resultado depende de la tarea, los conocimientos previos, la calidad de la retroalimentación y la constancia. Las estrategias de este módulo son herramientas para experimentar y ajustar, no recetas universales.

---

## Lección 0.1.1 — Aprendizaje activo

### Objetivos de aprendizaje
Al terminar, podrás:
- distinguir estudiar pasivamente de realizar actividades que exigen procesar o recuperar información;
- transformar una lectura o video en preguntas, explicaciones y ejercicios;
- comprobar qué recuerdas sin mirar el material;
- seleccionar una actividad activa adecuada para un tema técnico.

### 1. ¿Qué significa aprender activamente?

Aprender activamente significa realizar operaciones mentales observables con la información: formular preguntas, explicar relaciones, resolver un problema, comparar alternativas, recuperar una idea de memoria o aplicar un procedimiento. No significa simplemente estar ocupado, subrayar mucho, copiar páginas o pulsar botones.

Leer y escuchar pueden ser útiles para una primera exposición. El problema aparece cuando se confunde familiaridad con dominio: reconocer una explicación al verla no demuestra que puedas reconstruirla o utilizarla sin ayuda.

Una secuencia sencilla para estudiar un concepto:
1. **Antes:** escribe qué sabes y qué pregunta intentas responder.
2. **Durante:** detente y predice el siguiente paso; anota dudas concretas.
3. **Después:** cierra la fuente y explica la idea con tus palabras.
4. **Aplicación:** resuelve una tarea nueva sin copiar el ejemplo.
5. **Comprobación:** compara tu respuesta con una referencia fiable y corrige errores.

La práctica de recuperación (intentar recordar sin consultar) y la práctica espaciada cuentan con respaldo empírico. Un repaso no debe limitarse a releer: primero intenta responder; después consulta y corrige.

### 2. Ejemplo guiado: aprender qué es una variable

**Actividad pasiva:** leer tres veces «una variable es un espacio donde se almacena un dato».

**Actividad activa:**
- Sin mirar, responde: ¿qué problema resuelve un nombre asociado a un valor?
- Predice qué imprimirá este pseudocódigo: `nombre ← "Ada"; mostrar(nombre)`.
- Cambia el valor y explica qué resultado esperas.
- Inventa un caso en el que guardar un dato con nombre sea útil.
- Consulta la explicación y corrige cualquier imprecisión.

La analogía de «caja» puede ayudar al principio, pero no es una descripción exacta de todos los lenguajes: algunos nombres se vinculan a objetos o valores mediante reglas específicas. Esa precisión se estudiará cuando corresponda.

### 3. Ejercicios

**Básico.** Después de estudiar durante diez minutos un concepto que ya conozcas, cierra el material y escribe cinco ideas que recuerdes. Reabre la fuente y marca: correcto, incompleto o incorrecto.

**Intermedio.** Convierte una explicación de cinco párrafos sobre un tema técnico en: tres preguntas, una predicción y un ejercicio práctico.

**Aplicación.** Estudia un concepto nuevo de ASCENSO. Produce una explicación propia, un ejemplo distinto al de la fuente y una pregunta que todavía no puedas responder.

### 4. Criterios de evaluación
- Diferencia una actividad de reconocimiento de una de recuperación.
- Formula preguntas que exigen explicar o aplicar, no solo copiar.
- Contrasta sus respuestas con una fuente y corrige errores.
- Identifica qué no comprendió todavía.

### Autoevaluación
1. ¿Por qué releer varias veces no demuestra necesariamente que dominas un tema?
2. ¿Qué haces antes de consultar la solución de un ejercicio?
3. ¿Qué diferencia hay entre reconocer una respuesta y recuperarla de memoria?

**Respuestas orientativas:** 1) porque la familiaridad puede confundirse con capacidad de recordar o transferir; 2) intentas resolver, explicar o predecir por cuenta propia; 3) reconocer ocurre al ver una opción, recuperar exige producir la información sin verla.

---

## Lección 0.1.2 — Pensamiento crítico

### Objetivos de aprendizaje
- separar afirmaciones, evidencias, inferencias y opiniones;
- evaluar la autoridad, actualidad y pertinencia de una fuente;
- comprobar una afirmación técnica con documentación primaria;
- expresar incertidumbre cuando la evidencia no alcanza.

### 1. Pensar críticamente no es desconfiar de todo

El pensamiento crítico es evaluar razones y evidencias antes de aceptar una conclusión. No consiste en rechazar automáticamente una afirmación ni en creerla porque aparece en un sitio conocido.

Ante una afirmación técnica, pregunta:
1. ¿Qué se afirma exactamente?
2. ¿Qué evidencia la respalda?
3. ¿La fuente tiene competencia directa sobre el tema?
4. ¿La información corresponde a la versión o contexto que estoy estudiando?
5. ¿Hay condiciones, excepciones o limitaciones?
6. ¿Otra fuente independiente confirma el punto?

Una documentación oficial es normalmente la fuente primaria adecuada para saber cómo funciona una API de un producto. No necesariamente demuestra que ese producto sea el mejor para todos los proyectos. Para comparar resultados educativos o de rendimiento, pueden ser más apropiadas investigaciones empíricas y revisiones científicas.

### 2. Ejemplo guiado: «Este comando siempre borra los archivos temporales»

No aceptes la palabra «siempre» sin comprobar:
- qué comando y versión se utilizan;
- qué ruta afecta;
- qué permisos necesita;
- si hay opciones que cambian su comportamiento;
- qué dice la documentación del mantenedor;
- si el ejemplo puede probarse de forma segura en un directorio temporal.

Reformula la afirmación de manera verificable: «En la versión X, ejecutado con las opciones Y sobre el directorio Z, el comando elimina los archivos que cumplen la condición W». Si no has comprobado todas las condiciones, declara el límite.

### 3. Ejercicio de evaluación de fuentes

Busca una explicación sobre una función de un lenguaje o herramienta. Compara:
- documentación del mantenedor;
- un tutorial de terceros;
- una respuesta de foro.

Registra quién publica cada recurso, cuándo se actualizó, qué versión cubre y qué afirmación concreta respalda. No copies una respuesta de foro como si fuera especificación oficial.

### 4. Errores frecuentes
- usar el primer resultado del buscador como autoridad;
- confundir popularidad con exactitud;
- ignorar fecha y versión;
- citar una fuente que no respalda la frase;
- presentar una hipótesis como hecho;
- buscar solo fuentes que confirmen la opinión inicial.

### Criterios de evaluación
Entrega una ficha de verificación con afirmación, evidencia, fuente, fecha/versión, limitaciones y conclusión calibrada. Se aprueba si otra persona puede reproducir el razonamiento y localizar la evidencia.

### Autoevaluación
1. ¿Una fuente oficial demuestra que una herramienta sea la mejor? No: describe con autoridad su propio producto, pero una comparación exige criterios y evidencia adecuados.
2. ¿Qué haces si dos fuentes discrepan? Compruebas alcance, fecha, versión, contexto y autoridad; documentas la discrepancia si no puede resolverse.
3. ¿Qué significa «no tengo evidencia suficiente»? Que la conclusión debe permanecer abierta, no que la afirmación sea falsa.

---

## Lección 0.1.3 — Método Feynman como ejercicio de explicación

### Objetivos de aprendizaje
- explicar un concepto con lenguaje propio;
- detectar vacíos de comprensión mediante una explicación;
- usar ejemplos y analogías sin confundirlos con la definición formal;
- revisar la explicación a partir de fuentes y preguntas.

### 1. Qué haremos en ASCENSO

El llamado «método Feynman» se utiliza popularmente para describir un ciclo de explicación sencilla, detección de vacíos y revisión. En este curso lo trataremos como una **rutina didáctica de autoexplicación**, no como una fórmula científica única ni como una técnica con eficacia garantizada por llevar ese nombre.

La autoexplicación y la elaboración aparecen entre las estrategias estudiadas en la literatura del aprendizaje. El beneficio depende de que la explicación sea correcta, se contraste y se conecte con ejemplos.

### 2. Procedimiento de cuatro pasos
1. Elige una idea delimitada: por ejemplo, «qué hace una función».
2. Explícala como si hablaras con alguien que conoce las palabras comunes, pero no el concepto.
3. Señala frases vagas, saltos lógicos y términos que no puedes definir.
4. Consulta una fuente fiable, corrige y crea un ejemplo nuevo.

No elimines los términos técnicos necesarios: defínelos. Una explicación sencilla debe ser accesible, no incorrecta.

### 3. Ejemplo: función

**Primera explicación incompleta:** «Una función es algo que hace una cosa».

**Revisión:** «En programación, una función es una unidad identificable de código que puede recibir datos de entrada mediante parámetros, ejecutar instrucciones y, si está definida para ello, devolver un resultado. Permite organizar y reutilizar operaciones».

**Ejemplo conceptual:** una función `calcular_total(precio, cantidad)` recibe dos valores y devuelve su producto. La sintaxis real depende del lenguaje; todavía no estamos afirmando una implementación Java o Python concreta.

**Límite de la analogía:** comparar una función con una máquina que recibe ingredientes y entrega un producto ayuda a visualizar entradas y salidas, pero no todas las funciones son puras ni devuelven un valor; algunas producen efectos.

### 4. Ejercicio
Explica «dirección IP» en 120–180 palabras para una persona principiante. Incluye:
- definición precisa;
- ejemplo cotidiano;
- una analogía;
- una limitación de esa analogía;
- una pregunta que la explicación todavía no resuelva.

Después contrasta la definición con una fuente técnica pertinente y corrige cualquier error.

### Criterios de evaluación
La explicación define el concepto, utiliza correctamente sus términos, distingue analogía y realidad, ofrece un ejemplo coherente y reconoce sus límites.

---

## Lección 0.1.4 — Repetición espaciada

### Objetivos de aprendizaje
- explicar qué es distribuir sesiones de estudio en el tiempo;
- diferenciar práctica espaciada de estudio concentrado;
- planificar repasos que incluyan recuperación y retroalimentación;
- ajustar intervalos según dificultad y desempeño.

### 1. Concepto

La práctica espaciada consiste en volver a trabajar un contenido en sesiones separadas por intervalos, en lugar de concentrar todas las repeticiones en una sola sesión. Revisiones de investigación y guías educativas respaldan su utilidad para la retención a largo plazo en muchas tareas de aprendizaje.

No existe un calendario universal óptimo para todos los temas y estudiantes. El intervalo depende de la dificultad, el tiempo disponible, el conocimiento previo y el objetivo de retención.

### 2. Ejemplo de planificación

Para un concepto introductorio:
- Día 1: estudiar y resolver un ejemplo.
- Día 2: intentar explicar y resolver sin consultar.
- Día 4: responder preguntas mezcladas con el tema anterior.
- Día 7: resolver un problema nuevo.
- Día 14: comprobar si aún puedes aplicarlo.

Este calendario es una **propuesta inicial de organización**, no una regla científica fija. Si fallas, consulta la explicación, corrige y programa otra oportunidad de recuperación.

### 3. Cómo hacer un buen repaso
1. Intenta recordar primero.
2. Responde una pregunta o resuelve un ejercicio.
3. Comprueba con una solución fiable.
4. Anota el error específico.
5. Decide cuándo volver a practicar.

No conviertas la repetición espaciada en releer mecánicamente el mismo texto.

### 4. Ejercicio
Diseña un calendario de dos semanas para aprender diez comandos de terminal. Incluye al menos tres sesiones de recuperación sin mirar apuntes y una tarea que combine comandos. Registra aciertos, errores y cambios al calendario.

### Criterios de evaluación
El calendario distribuye sesiones, exige recuperar o aplicar conocimientos, incluye retroalimentación y justifica los ajustes. No se evalúa que el estudiante use exactamente los días del ejemplo.

---

## Lección 0.1.5 — Práctica deliberada y práctica enfocada

### Objetivos de aprendizaje
- distinguir repetir una tarea de practicar una habilidad concreta;
- establecer una meta pequeña y observable;
- utilizar retroalimentación para corregir errores;
- reconocer que la práctica no es el único factor que explica el rendimiento experto.

### 1. Una práctica con propósito

En este módulo usaremos «práctica enfocada» para describir una actividad con objetivo concreto, dificultad adecuada, atención, retroalimentación y oportunidad de corregir. La investigación sobre práctica deliberada es influyente, pero no justifica afirmar que las horas de práctica explican por sí solas toda diferencia de rendimiento o garantizan convertirse en experto. Influyen conocimientos previos, oportunidades, características individuales, calidad de la instrucción y dominio.

### 2. Ejemplo: depurar un error

Meta vaga: «practicar programación una hora».

Meta concreta: «durante 25 minutos, reproducir un error de índice, identificar la línea y condición que lo causa, formular una hipótesis, corregirlo y escribir una prueba que evite la regresión».

Ciclo:
1. Define qué habilidad entrenas.
2. Elige una tarea apenas por encima de lo que ya puedes resolver.
3. Intenta resolverla sin saltarte pasos.
4. Compara con criterios o retroalimentación.
5. Identifica un error y su causa.
6. Repite con una variante para comprobar que aprendiste el principio.

### 3. Ejercicio
Selecciona una habilidad que ya hayas practicado. Diseña tres sesiones de 20–30 minutos. Cada sesión debe tener una meta observable, un resultado, un error detectado y una decisión para la siguiente sesión.

### Criterios de evaluación
La meta es medible; la tarea corresponde a la habilidad; existe retroalimentación; el estudiante registra correcciones y no confunde tiempo invertido con dominio.

---

## Lección 0.1.6 — Resolución de problemas

### Objetivos de aprendizaje
- describir un problema antes de intentar resolverlo;
- identificar entradas, salidas, restricciones y casos límite;
- proponer y comparar alternativas;
- comprobar una solución con casos de prueba.

### 1. Un proceso reproducible

1. **Comprender:** ¿qué se solicita y qué no se solicita?
2. **Precisar:** define entradas, salidas, restricciones y supuestos.
3. **Dividir:** separa el problema en partes manejables.
4. **Proponer:** escribe una solución posible en lenguaje natural o pseudocódigo.
5. **Probar mentalmente:** usa un caso normal, uno mínimo, uno máximo y uno inválido cuando corresponda.
6. **Implementar:** traduce el procedimiento al lenguaje o herramienta adecuada.
7. **Verificar:** compara el resultado real con el esperado.
8. **Revisar:** analiza errores, complejidad y claridad.

Este es un marco de trabajo didáctico, no un algoritmo que garantice resolver cualquier problema. Algunos problemas requieren investigación, modelado especializado o reformular la pregunta.

### 2. Ejemplo guiado

**Problema:** calcular el total de una compra a partir del precio unitario y la cantidad.

- Entradas: precio unitario y cantidad.
- Salida: total.
- Supuestos: precio no negativo; cantidad entera no negativa; moneda y redondeo definidos por el contexto.
- Regla inicial: total = precio × cantidad.
- Casos: precio 10 y cantidad 3 → 30; cantidad 0 → 0; precio negativo → rechazo si el dominio lo prohíbe.

Observa que la fórmula es sencilla; definir qué entradas son válidas evita errores de interpretación.

### 3. Ejercicio
Diseña un algoritmo en pseudocódigo para calcular el promedio de tres calificaciones. Define si se admiten valores fuera del intervalo permitido y qué debe ocurrir cuando la entrada no sea válida. Incluye al menos cuatro casos de prueba.

### Criterios de evaluación
El problema está delimitado, las entradas y salidas son claras, los supuestos se declaran, el procedimiento es comprensible y los casos de prueba cubren condiciones normales y límite.

---

## Lección 0.1.7 — Descomposición de problemas complejos

### Objetivos de aprendizaje
- dividir un problema grande en subproblemas;
- identificar dependencias entre partes;
- definir entradas, salidas y responsabilidades de cada parte;
- comprobar que las partes resuelven el objetivo global.

### 1. Concepto

La descomposición consiste en dividir un problema complejo en partes más pequeñas que puedan comprenderse, diseñarse y verificarse. En informática se relaciona con el pensamiento computacional, el diseño modular y la separación de responsabilidades.

Una división útil debe reducir la complejidad sin perder la relación entre las partes. Crear muchas tareas pequeñas sin una estructura común puede aumentar la confusión.

### 2. Ejemplo: sistema de inventario

Problema general: crear un sistema de inventario de productos.

Posibles subproblemas:
- registrar producto;
- validar nombre, precio y cantidad;
- consultar productos;
- actualizar existencias;
- retirar productos;
- guardar y recuperar información;
- informar errores.

Define un contrato sencillo para cada operación. Por ejemplo, «actualizar existencias» recibe identificador y cantidad nueva; debe rechazar un identificador inexistente o una cantidad inválida. Todavía no decidimos base de datos ni lenguaje: eso corresponde a etapas posteriores.

### 3. Ejercicio
Descompón un sistema de biblioteca en al menos seis responsabilidades. Para cada una escribe:
- propósito;
- datos que recibe;
- resultado que produce;
- errores previsibles;
- relación con otras partes.

Después dibuja un diagrama de dependencias y explica por qué elegiste esa división.

### Criterios de evaluación
Las partes tienen responsabilidades claras, no duplican innecesariamente la misma tarea, se identifican dependencias y la suma de las partes cubre el objetivo general.

---

## Lección 0.1.8 — Aprendizaje basado en proyectos

### Objetivos de aprendizaje
- explicar cómo un proyecto integra conocimientos y habilidades;
- dividir un proyecto en entregas pequeñas;
- definir un resultado verificable;
- documentar decisiones, pruebas y aprendizajes.

### 1. Qué es aprender mediante proyectos

En el aprendizaje basado en proyectos, los estudiantes trabajan durante un periodo en una pregunta, reto o problema significativo y producen un resultado que requiere investigar, tomar decisiones, aplicar conocimientos y revisar el trabajo. No basta con asignar una tarea larga y llamarla proyecto: se necesitan objetivos claros, acompañamiento, hitos y evaluación alineada.

Un proyecto es especialmente útil para integrar conocimientos, pero no reemplaza toda explicación explícita ni la práctica guiada. El estudiante principiante puede necesitar ejemplos resueltos y enseñanza directa antes de afrontar una tarea abierta.

### 2. Mini proyecto: ASCENSO-Knowledge-Base

**Propósito:** crear un repositorio donde el estudiante registre lo aprendido.

**Entregables iniciales:**
1. Un archivo README con propósito y estructura.
2. Una carpeta por etapa.
3. Una nota de aprendizaje con concepto, explicación propia y dudas.
4. Una sección de referencias con URL y fecha de consulta.
5. Un registro de ejercicios realizados y resultados.
6. Un historial de cambios.

**Hitos sugeridos:**
- Hito 1: definir estructura y convenciones.
- Hito 2: documentar tres conceptos.
- Hito 3: añadir ejercicios y evidencias.
- Hito 4: revisar enlaces, claridad y organización.
- Hito 5: presentar el repositorio y explicar decisiones.

No se exige una herramienta específica en esta lección; Git y GitHub se estudiarán con profundidad en la etapa 5. El estudiante puede empezar con archivos locales.

### 3. Rúbrica del mini proyecto

| Criterio | Evidencia |
|---|---|
| Organización | Carpetas y nombres consistentes |
| Comprensión | Explicaciones propias y correctas |
| Trazabilidad | Fuentes con URL y fecha |
| Práctica | Ejercicios con resultado o reflexión |
| Revisión | Errores corregidos y cambios registrados |
| Comunicación | README comprensible para otra persona |

### 4. Ejercicio de reflexión
Al finalizar, responde:
- ¿Qué decisión de organización te ayudó más?
- ¿Qué explicación tuviste que corregir?
- ¿Qué fuente fue más útil y por qué?
- ¿Qué harías distinto en el siguiente proyecto?

### Criterios de evaluación
El repositorio puede ser comprendido por otra persona, contiene evidencia real del proceso, distingue material propio de fuentes externas y muestra al menos una revisión posterior.

---

## Evaluación integradora del módulo 0.1

### Parte A — Comprensión
1. Explica la diferencia entre reconocimiento y recuperación.
2. Describe cómo verificarías una afirmación técnica.
3. Explica por qué una analogía puede ser útil y a la vez limitada.
4. Diseña un calendario de práctica espaciada para un concepto.
5. Formula una meta de práctica enfocada.
6. Enumera las etapas de tu proceso para resolver un problema.
7. Descompón un sistema sencillo en responsabilidades.
8. Explica qué hace que una actividad sea un proyecto de aprendizaje.

### Parte B — Desempeño
Entrega tu ASCENSO-Knowledge-Base inicial con:
- tres notas de aprendizaje;
- una explicación revisada con el método de autoexplicación;
- un calendario de repaso;
- un problema descompuesto;
- un ejercicio resuelto y verificado;
- una lista de fuentes consultadas.

### Rúbrica de dominio
- **Aún no demostrado:** faltan entregables o hay errores conceptuales importantes.
- **En desarrollo:** entrega la mayoría de los elementos, pero requiere ayuda para verificar o explicar.
- **Competente:** explica los conceptos, aplica las estrategias y presenta evidencias coherentes.
- **Sólido:** además compara alternativas, reconoce límites, corrige errores y puede justificar sus decisiones.

La etapa no debe marcarse como completada solo por leer estas lecciones. El dominio se demuestra mediante evidencias y los criterios oficiales de finalización que defina el programa.

---

## Referencias y trazabilidad de fuentes

Fecha de consulta de los recursos web: **2026-11-19**. Las referencias respaldan los principios pedagógicos indicados; no son «certificaciones» del método ASCENSO.

1. **Weinstein, Y., Madan, C. R. y Sumeracki, M. A. (2018).** *Teaching the science of learning*. Cognitive Research: Principles and Implications, 3, 2. Revisión tutorial de estrategias cognitivas: práctica espaciada, intercalado, recuperación, elaboración, ejemplos concretos y codificación dual.  
   https://pmc.ncbi.nlm.nih.gov/articles/PMC5780548/  
   **Uso:** lecciones 0.1.1, 0.1.3 y 0.1.4. Fuente B.

2. **Carnegie Mellon University, Eberly Center.** *Retrieval Practice for Improved Learning*. Recurso institucional con ejemplos de recuperación, quizzes de bajo riesgo y explicación entre pares.  
   https://www.cmu.edu/teaching/resources/instructionalstrategies/activelearningstrategies/retrievalpractice/  
   **Uso:** lección 0.1.1 y autoevaluaciones. Fuente D.

3. **Carnegie Mellon University, Eberly Center.** *Spaced Practice*. Explicación institucional de la distribución de sesiones y su contraste con la práctica masiva.  
   https://www.cmu.edu/teaching/resources/instructionalstrategies/activelearningstrategies/spacedopractice/index.html  
   **Uso:** lección 0.1.4. Fuente D.

4. **University of Minnesota, Center for Educational Innovation.** *Leveraging the Learning Sciences*. Síntesis de principios: límites de memoria de trabajo, recuperación, práctica espaciada e intercalada, participación y metacognición.  
   https://cei.umn.edu/teaching-resources/leveraging-learning-sciences  
   **Uso:** diseño general del módulo. Fuente D.

5. **Institute of Education Sciences / What Works Clearinghouse (2007).** *Organizing Instruction and Study to Improve Student Learning*. Guía de práctica con recomendaciones y niveles de evidencia; entre ellas distribuir el aprendizaje en el tiempo e intercalar ejemplos resueltos con ejercicios.  
   https://ies.ed.gov/ncee/WWC/PracticeGuide/1  
   **Uso:** lecciones 0.1.1, 0.1.4 y 0.1.5. Fuente B/D institucional.

6. **Carpenter, S. K., Pan, S. C. y Butler, A. C. (2022).** *The science of effective learning with spacing and retrieval practice*. Nature Reviews Psychology, 1, 496–511. Revisión sobre espaciamiento y práctica de recuperación.  
   https://doi.org/10.1038/s44159-022-00089-1  
   **Uso:** lección 0.1.4. Fuente B.

7. **Ericsson, K. A., Krampe, R. T. y Tesch-Römer, C. (1993).** *The Role of Deliberate Practice in the Acquisition of Expert Performance*. Psychological Review, 100(3), 363–406. Artículo clásico que presenta el marco de práctica deliberada.  
   https://doi.org/10.1037/0033-295X.100.3.363  
   **Uso:** antecedente conceptual de la lección 0.1.5. Fuente C.

8. **Ericsson, K. A. y Harwell, K. W. (2019).** *Deliberate Practice and Proposed Limits on the Effects of Practice on the Acquisition of Expert Performance*. Frontiers in Psychology, 10, 2396. Discute definición y límites del concepto.  
   https://pmc.ncbi.nlm.nih.gov/articles/PMC6824411/  
   **Uso:** evitar afirmaciones simplistas sobre horas de práctica y experticia. Fuente B.

9. **Hambrick, D. Z. et al. (2014).** *Deliberate practice: Is that all it takes to become an expert?* Intelligence, 45, 34–45. Presenta evidencia y argumentos sobre otros factores relacionados con el rendimiento experto.  
   https://doi.org/10.1016/j.intell.2013.04.001  
   **Uso:** limitaciones y matices de la lección 0.1.5. Fuente C.

10. **Institute of Education Sciences / What Works Clearinghouse.** *Practice Guides*. Explica el propósito de las guías y su base en revisiones de investigación, experiencia profesional y paneles de expertos.  
    https://ies.ed.gov/ncee/wwc/PracticeGuides  
    **Uso:** criterio de selección de fuentes pedagógicas. Fuente D institucional.

### Nota de precisión
- «Método Feynman» se presenta aquí como una rutina de autoexplicación; no se afirma que exista un protocolo único validado con ese nombre.
- «Práctica deliberada» no significa simplemente acumular horas; el módulo evita prometer experticia automática.
- El calendario de repasos es un ejemplo adaptable, no una frecuencia universal.
- El aprendizaje basado en proyectos se propone como formato de integración; este módulo no afirma que sea superior a toda enseñanza explícita o práctica guiada.
