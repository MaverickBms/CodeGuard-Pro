# Etapa 0 · Módulo 0.2 — Investigación técnica

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · referencia operativa vigente de la lección 0.2. No implica publicación ni aprobación editorial.  
**Alineación curricular:** ASCENSO 3.1, Etapa 0, apartado 0.2.  
**Objetivo:** desarrollar un método sostenible para investigar problemas técnicos.

Este módulo cubre exactamente los siete temas del roadmap: buscar documentación; buscar soluciones a errores; leer Stack Overflow; consultar GitHub; investigar repositorios; diferenciar información verificada de opiniones; formular preguntas técnicas.

## Resultados de aprendizaje

Al terminar, podrás:
1. Convertir una duda vaga en una pregunta técnica delimitada.
2. Buscar primero en documentación primaria y después ampliar a fuentes secundarias.
3. Evaluar resultados según versión, contexto y evidencia.
4. Leer respuestas de Stack Overflow de forma crítica.
5. Investigar un repositorio sin ejecutar código desconocido a ciegas.
6. Separar hechos, hipótesis, opiniones y experiencias.
7. Registrar una investigación reproducible.

## Apéndice didáctico — Formular preguntas técnicas (comunicación reproducible)

Una búsqueda eficaz comienza describiendo el problema, no adivinando una solución.

**Plantilla**
- Objetivo: ¿qué intentabas conseguir?
- Contexto: sistema operativo, lenguaje, framework, versión y entorno.
- Acción: ¿qué comando, código o secuencia ejecutaste?
- Resultado real y resultado esperado.
- Evidencia: mensaje completo, stack trace o fragmento mínimo.
- Cambios recientes: dependencias, configuración, código o entorno.

**Ejemplo deficiente:** «No funciona Django».

**Ejemplo investigable:** «En Python [versión] y Django [versión], al ejecutar [comando] en [sistema operativo], aparece [mensaje]. Espero [resultado]. El error comenzó después de [cambio]. ¿Qué documentación describe este comportamiento y cómo puedo reproducirlo en un caso mínimo?»

Nunca publiques contraseñas, tokens, claves privadas, datos personales ni archivos de configuración con secretos. Sustituye valores sensibles por marcadores ficticios.

**Ejercicio:** transforma tres dudas vagas en reportes con contexto, resultado esperado, resultado real y evidencia.

## Apéndice didáctico — Buscar y leer documentación

La documentación oficial del proyecto o mantenedor suele ser el punto de partida para conocer comportamiento soportado, opciones, sintaxis, compatibilidad y cambios entre versiones.

**Orden recomendado**
1. Documentación oficial de la versión utilizada.
2. Guías de migración, notas de versión y changelog.
3. Repositorio oficial: README, ejemplos, issues y código.
4. Estándares o especificaciones aplicables.
5. Preguntas comunitarias y artículos de terceros como pistas que deben contrastarse.

**Lectura dirigida**
- Identifica producto y versión.
- Localiza la sección del concepto, API o error.
- Comprueba requisitos y prerrequisitos.
- Lee ejemplos completos y advertencias.
- Revisa cambios incompatibles o deprecaciones.
- Prueba el ejemplo en un entorno aislado y registra el resultado.

**Ejemplo:** si una función no existe en tu versión instalada, no copies sin comprobar una solución de la documentación más reciente. Compara versión instalada, documentación y notas de versión.

**Ejercicio:** elige una biblioteca. Localiza documentación oficial, identifica la versión y encuentra instalación, tutorial y referencia API. Resume qué responde tu pregunta y qué no.

## Apéndice didáctico — Buscar soluciones a errores

Un mensaje de error contiene pistas. Antes de buscarlo, elimina datos sensibles y conserva el texto técnico distintivo.

**Procedimiento**
1. Lee el error y el contexto relevante del stack trace.
2. Identifica el componente que falla y la línea propia implicada.
3. Extrae una frase distintiva.
4. Busca la frase junto al nombre y versión del componente.
5. Repite con el identificador del error y sin datos específicos del proyecto.
6. Compara explicaciones, priorizando documentación oficial e issues del proyecto.
7. Formula una hipótesis comprobable.
8. Cambia una variable a la vez y repite el caso.
9. Registra qué cambio resolvió el problema y qué evidencia lo demuestra.

El primer resultado, una respuesta votada o una respuesta de IA no es garantía de corrección.

**Ejercicio:** toma un error no sensible de un proyecto propio o ejemplo preparado. Registra búsqueda, fuentes, hipótesis, prueba y conclusión.

## Apéndice didáctico — Leer Stack Overflow críticamente

Stack Overflow es un repositorio comunitario, no documentación normativa del lenguaje o framework.

Evalúa cada respuesta:
- ¿Responde exactamente a la pregunta?
- ¿Coinciden lenguaje, framework y versión?
- ¿La respuesta aceptada o votada tiene explicación y evidencia? El voto es una señal comunitaria, no una garantía.
- ¿La fecha importa porque la API pudo cambiar?
- ¿Hay comentarios que advierten errores o cambios?
- ¿Puede contrastarse con documentación oficial o código fuente?
- ¿Introduce riesgos o dependencias innecesarias?

**Práctica:** toma una respuesta antigua y busca la documentación actual del método. Anota qué sigue vigente, qué cambió y qué no puedes confirmar.

## Apéndice didáctico — Consultar GitHub e investigar repositorios

Antes de usar un repositorio:
1. Confirma propietario, nombre y URL.
2. Lee README, licencia, documentación y política de contribución.
3. Comprueba actividad, releases, tags, ramas y compatibilidad.
4. Revisa manifiestos de dependencias para entender qué instala el proyecto.
5. Inspecciona estructura, pruebas, CI y ejemplos.
6. Busca el símbolo, archivo o error dentro del código.
7. Lee issues y pull requests, diferenciando propuestas de cambios integrados.
8. No ejecutes scripts, binarios, contenedores ni workflows desconocidos en tu equipo habitual. Usa un entorno aislado y revisa permisos.

Una estrella o muchas descargas no demuestran seguridad, calidad ni mantenimiento. Revisa la licencia antes de reutilizar o distribuir código.

**Ejercicio:** investiga un repositorio pequeño. Entrega mapa de carpetas, propósito, lenguaje, licencia, instrucciones de prueba, mantenimiento observado y tres límites de lo que no pudiste confirmar.

## Apéndice didáctico — Diferenciar información verificada de opiniones

Clasifica las afirmaciones:
- **Hecho comprobado:** respaldado por fuente primaria o prueba reproducible.
- **Resultado experimental:** observado en un entorno concreto; no implica universalidad.
- **Interpretación:** conclusión razonada a partir de hechos.
- **Opinión:** preferencia o valoración.
- **Hipótesis:** explicación provisional pendiente de prueba.
- **No verificado:** evidencia insuficiente.

Registra procedencia, autor/mantenedor, fecha, versión, contexto y limitaciones. Dos fuentes que se copian mutuamente no son necesariamente evidencias independientes.

**Ejemplo:** «En mi equipo, con versión X, el comando Y produjo Z» es un resultado observado. «Y siempre falla en todos los sistemas» es una generalización que ese experimento no demuestra.

**Ejercicio:** toma cinco afirmaciones de un tutorial, clasifícalas y busca evidencia primaria para las que sean comprobables.

## Apéndice didáctico — Comunicar una investigación

Una buena respuesta permite que otra persona entienda y reproduzca el diagnóstico.

**Estructura del informe**
1. Resumen del problema.
2. Entorno y versiones.
3. Pasos mínimos para reproducir.
4. Resultado esperado y real.
5. Evidencias y fuentes con URL y fecha.
6. Hipótesis descartadas y motivo.
7. Solución aplicada o estado pendiente.
8. Pruebas realizadas y límites.
9. Riesgos, efectos secundarios y alternativa de reversión.

No afirmes «solucionado» si solo desapareció el mensaje sin comprobar el comportamiento esperado.

## Proyecto — Bitácora de investigación ASCENSO

Crea una carpeta investigaciones/ en ASCENSO-Knowledge-Base y documenta tres casos:
- una consulta respondida con documentación oficial;
- un error investigado con una fuente comunitaria contrastada;
- un repositorio analizado sin ejecutar código no confiable.

Cada caso incluirá pregunta, entorno, evidencias, fuentes, hipótesis, pruebas, resultado y limitaciones. No incluyas secretos ni datos privados.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Delimitación del problema | 15 |
| Calidad y trazabilidad de fuentes | 20 |
| Lectura crítica y versiones | 15 |
| Método experimental | 20 |
| Seguridad | 10 |
| Comunicación reproducible | 20 |

Aprobación sugerida: 80/100 y ningún fallo crítico de seguridad. Esta rúbrica es propuesta pedagógica y no sustituye los criterios de aprobación de la aplicación.

## Videos candidatos — coincidencia temática y audio pendientes de verificación

Los siguientes enlaces son candidatos editoriales por sus títulos y descripciones; no se consideran recomendados ni aprobados hasta escuchar el audio real, confirmar que está hablado en español y comprobar que cubre directamente los objetivos del módulo. No se infiere el idioma del audio a partir de metadatos. No se añaden videos de productividad, Git o herramientas generales porque no enseñan específicamente investigación técnica.

1. **[Cómo usar la documentación para aprender lenguajes, librerías y frameworks — Programación en español](https://www.youtube.com/watch?v=y6f3susXT5g)**  
   Idioma hablado: pendiente de verificación. Pertinencia prevista: navegación de documentación; la descripción indica instalación, tutoriales, referencia API, migración y guías de estilo.  
   Actividad: usar documentación oficial y localizar esas secciones.

2. **[Tips para enfrentar BUGS y BLOQUEOS como programador — Programación en español](https://www.youtube.com/watch?v=21_f6fglZ_A)**  
   Idioma hablado: pendiente de verificación. Pertinencia prevista: investigar errores, buscar en Google/Stack Overflow, consultar GitHub Issues y comprender el contexto del problema.  
   Actividad: aplicar su enfoque a un error reproducible y entregar una bitácora.

Los títulos, descripciones y capítulos publicados se contrastaron el 19-11-2026; eso no verifica el idioma del audio ni sustituye la visualización. Mantener ambos enlaces como candidatos hasta escuchar y revisar el contenido. No publicar como recursos recomendados antes de esa comprobación.

## Autoevaluación

1. ¿Por qué la documentación de otra versión puede llevar a una solución incorrecta?
2. ¿Qué diferencia existe entre una respuesta aceptada en Stack Overflow y una especificación oficial?
3. ¿Qué datos necesitas para formular una pregunta reproducible?
4. ¿Por qué no debes ejecutar directamente un repositorio desconocido?
5. ¿Qué evidencia distingue una hipótesis de un resultado comprobado?
6. ¿Qué información debe contener una bitácora técnica?

Responde con tus palabras y justifica cada respuesta con un ejemplo.

## Referencias

- Video: https://www.youtube.com/watch?v=y6f3susXT5g
- Video: https://www.youtube.com/watch?v=21_f6fglZ_A
- GitHub Docs: https://docs.github.com/
- Stack Overflow, búsqueda: https://stackoverflow.com/help/searching
- Stack Overflow, ejemplo mínimo reproducible: https://stackoverflow.com/help/minimal-reproducible-example
- GitHub Docs, repositorios: https://docs.github.com/en/repositories
- GitHub Docs, seguridad: https://docs.github.com/en/code-security

**Fecha de consulta de enlaces:** 19-11-2026. Revisar enlaces, versiones y contenido audiovisual antes de aprobar o publicar.


---


> **Nota de alineación curricular:** las secciones heredadas de la primera versión se conservan como material complementario, pero no establecen la numeración oficial. La secuencia canónica y sus siete títulos se desarrolla en la sección «Profundización didáctica — versión 0.2.0» que sigue, y coincide con el orden del JSON maestro.

## Profundización didáctica — versión 0.2.0 (24-11-2026)

Esta ampliación desarrolla prácticas evaluables para cada uno de los siete temas oficiales. No cambia títulos, orden ni jerarquía del currículo. Los ejemplos son simulados y no se presentan como experimentos ejecutados.

### Ficha de trabajo común: expediente de investigación

Para cada caso conserva un archivo Markdown con:
- identificador local de la actividad (no es UUID curricular ni se importa a la aplicación);
- pregunta original y reformulación investigable;
- producto, versión, sistema operativo y entorno;
- evidencia primaria consultada y fecha;
- fuentes secundarias consultadas y por qué se consideraron;
- hipótesis, predicción y prueba que las distingue;
- resultado observado, separado de la interpretación;
- solución, limitaciones y pasos de reproducción;
- datos que se omitieron por seguridad.

No incluyas secretos, datos personales ni fragmentos de código cuya licencia no permita redistribución.

### Lección 0.2.1 — Buscar documentación: localizar el contrato correcto

**Situación:** una persona encuentra en un tutorial un parámetro que no existe en la versión instalada de una biblioteca.

**Procedimiento guiado**
1. Registra el nombre exacto del paquete y la versión instalada mediante el gestor del entorno.
2. Identifica el sitio oficial del proyecto; evita asumir que el primer resultado del buscador pertenece al mantenedor.
3. Abre la documentación de la versión correspondiente. Si solo existe documentación actual, localiza la guía de migración y las notas de versión.
4. Busca el nombre del parámetro en la referencia API y en los ejemplos oficiales.
5. Contrasta la firma documentada con el error real.
6. Registra si el parámetro fue añadido, renombrado, eliminado o si el tutorial se refiere a otro producto.

**Ejemplo resuelto (razonamiento):** si el tutorial usa una opción ausente en la referencia de la versión instalada, no se concluye inmediatamente que el paquete esté defectuoso. Primero se comprueba si el tutorial corresponde a una versión posterior. La conclusión correcta queda condicionada a la comparación de versiones y a la fuente del mantenedor.

**Ejercicio:** elige una biblioteca que ya utilices. Localiza una función y documenta: versión consultada, firma, parámetros obligatorios, opcionales, tipo de retorno, excepciones o errores documentados y un ejemplo oficial.

**Evidencia esperada:** ficha con enlaces a la página de versión y a la referencia API. Una captura sin URL, versión o contexto no es evidencia suficiente.

### Lección 0.2.2 — Buscar soluciones a errores: construir una consulta discriminante

**Situación simulada:** un proyecto muestra un error de importación de un módulo. La búsqueda inicial «no funciona Python» devuelve resultados demasiado amplios.

**Método**
1. Conserva el mensaje exacto, eliminando rutas privadas y datos sensibles.
2. Anota versión de Python, entorno virtual, comando de ejecución y directorio de trabajo.
3. Comprueba si el módulo está instalado en el mismo intérprete que ejecuta el programa.
4. Formula dos hipótesis distintas: dependencia ausente o intérprete/entorno incorrecto.
5. Predice qué evidencia distinguiría ambas hipótesis.
6. Consulta primero la documentación del entorno y del gestor de paquetes; usa foros como pistas.
7. Cambia una variable cada vez y registra el resultado.

**Ejemplo de consulta útil:** «Python [versión], entorno virtual [tipo], al ejecutar [comando] aparece [mensaje literal sin rutas privadas]. ¿Cómo compruebo qué intérprete ejecuta el proceso y dónde está instalado el paquete?».

**Ejercicio de análisis:** prepara tres consultas para el mismo fallo: una demasiado vaga, una con exceso de datos irrelevantes y una mínima pero suficiente. Explica qué información hace que la tercera sea discriminante.

**Criterio:** la consulta debe permitir distinguir al menos dos hipótesis plausibles, no limitarse a repetir el mensaje de error.

### Lección 0.2.3 — Leer Stack Overflow: validar una respuesta antes de aplicarla

**Caso:** una respuesta antigua recomienda una función que el proyecto ha marcado como obsoleta.

**Lista de comprobación**
- ¿La pregunta coincide con el síntoma y el contexto?
- ¿Coinciden lenguaje, versión y plataforma?
- ¿La respuesta explica el mecanismo o solo entrega una receta?
- ¿Tiene fecha y comentarios posteriores relevantes?
- ¿La API continúa documentada?
- ¿La solución introduce riesgos, permisos excesivos o dependencias?
- ¿Puede reproducirse en un proyecto mínimo y aislado?

Los votos, la aceptación y la reputación son señales de participación comunitaria; no reemplazan la comprobación técnica.

**Ejercicio:** selecciona una respuesta pública no sensible. Registra pregunta, fecha, versión indicada, solución propuesta, estado actual de la API en documentación primaria y veredicto: vigente, parcialmente vigente, obsoleta o no verificable.

**Solución orientativa:** si la respuesta recomienda un método que la documentación actual declara obsoleto, no se copia sin más. Se busca la alternativa oficial y se explican las diferencias. Si no hay evidencia suficiente para determinar compatibilidad, el veredicto debe ser «no verificable».

### Lección 0.2.4 — Consultar GitHub: navegar issues, pull requests y código

**Caso:** una biblioteca presenta un comportamiento inesperado y existe una issue con un título parecido.

**Ruta de investigación**
1. Confirma propietario y repositorio oficial.
2. Comprueba si la issue pertenece al repositorio original o a un fork.
3. Lee la descripción, etiquetas, fecha, comentarios del mantenedor y versión afectada.
4. Comprueba su estado: abierta, cerrada, duplicada o vinculada a una corrección.
5. Si apunta a un pull request, verifica si fue integrado y en qué commit o release.
6. Busca notas de versión que indiquen cuándo llegó el cambio.
7. No confundas una propuesta o una discusión con una corrección publicada.

**Ejercicio:** investiga una issue cerrada de un proyecto de código abierto. Entrega la secuencia issue → pull request (si existe) → commit/release y explica qué evidencia confirma que el cambio llegó a una versión distribuida.

**Límite:** el estado «closed» por sí solo no demuestra que el defecto esté corregido; la issue pudo cerrarse por duplicación, falta de información o decisión de no implementar.

### Lección 0.2.5 — Investigar repositorios: evaluar mantenibilidad y riesgo

**Caso:** debes decidir si utilizar un paquete de terceros en un proyecto académico.

Evalúa al menos:
- licencia y compatibilidad con el uso previsto;
- releases y versiones soportadas;
- actividad reciente, sin asumir que poca actividad equivale a abandono;
- responsables y política de seguridad;
- pruebas automatizadas y CI;
- dependencias directas y transitivas;
- documentación y procedimiento de instalación;
- issues abiertas, vulnerabilidades publicadas y avisos;
- permisos o acciones que ejecutan scripts de instalación.

**Ejemplo resuelto:** un repositorio con muchas estrellas pero sin licencia identificable no queda automáticamente autorizado para reutilización. Popularidad y permiso legal son cuestiones distintas. La decisión prudente es no redistribuir el código hasta aclarar la licencia.

**Ejercicio:** compara dos repositorios que resuelvan una misma necesidad. Crea una matriz con criterios, evidencia enlazada, fecha y limitaciones. No ejecutes sus scripts ni binarios en el equipo principal.

**Criterio:** toda valoración («mantenido», «seguro», «apto») debe acompañarse de observaciones concretas y no de una impresión basada en estrellas.

### Lección 0.2.6 — Diferenciar información verificada de opiniones: calibrar conclusiones

Clasifica cada afirmación con una categoría y una evidencia:
- hecho respaldado por fuente primaria;
- observación reproducida en un entorno delimitado;
- interpretación derivada;
- opinión o preferencia;
- hipótesis pendiente;
- información no verificada.

**Caso guiado:** «La herramienta A es más rápida que B».

Esta frase no es verificable mientras no se especifiquen carga, versiones, hardware, configuración, métrica, método de medición y repetición. Una medición aislada permite afirmar como máximo que, en ese ensayo concreto, se observó determinado resultado.

**Ejercicio:** transforma cinco afirmaciones absolutas en afirmaciones delimitadas. Para cada una indica qué evidencia permitiría confirmarla y qué resultado la refutaría.

**Retroalimentación:** si la evidencia no permite una conclusión, no fuerces un sí/no. Expresa qué se sabe, qué no se sabe y qué prueba falta.

### Lección 0.2.7 — Formular preguntas técnicas: producir un reporte reproducible

**Plantilla de reporte**
1. Título que describa el fallo, no una conclusión.
2. Objetivo que se intentaba alcanzar.
3. Entorno mínimo: sistema, versiones y configuración pertinente.
4. Pasos numerados desde un estado conocido.
5. Entrada mínima no sensible.
6. Resultado esperado.
7. Resultado real y mensaje literal.
8. Frecuencia y condiciones de aparición.
9. Pruebas ya realizadas y sus resultados.
10. Fuentes consultadas y pregunta concreta.

**Ejemplo de mejora**
- Débil: «Mi API falla, ayuda».
- Mejor: «En [entorno/versiones], al enviar [método y ruta ficticia] con [cuerpo mínimo sin secretos], recibo [código y mensaje]. Esperaba [resultado]. Se reproduce siguiendo [pasos]. ¿Qué parte del contrato HTTP o de la validación debería comprobar primero?».

**Ejercicio:** redacta un reporte a partir de un caso preparado por el docente o un proyecto propio. Pide a otra persona que lo reproduzca sin explicaciones adicionales. Registra las preguntas que tuvo que hacer y corrige el reporte.

**Criterio de éxito:** una persona con el mismo entorno puede reproducir el problema o identificar con claridad qué requisito ambiental falta.

## Claves de práctica — casos modelo y comprobación

Los casos de esta sección son **simulados**. Los nombres entre corchetes son datos que el estudiante debe sustituir por evidencia real de su entorno; no describen una incidencia real de CodeGuard Pro ni una prueba ya ejecutada.

### Clave 0.2.1 — Documentación y versiones

**Caso:** un tutorial muestra `bibliotecaX.metodo_nuevo()`, pero la referencia API de la versión instalada no contiene ese método.

**Razonamiento esperado:**
1. No concluir que el tutorial o la biblioteca están necesariamente equivocados.
2. Registrar versión instalada y versión del tutorial.
3. Consultar changelog/notas de versión y referencia API de ambas versiones.
4. Comprobar si el método se añadió después, cambió de nombre o pertenece a otro paquete.
5. Si la evidencia confirma que se añadió en una versión posterior, informar que el ejemplo no es compatible con la versión instalada; proponer actualizar solo después de revisar requisitos y cambios incompatibles.

**Respuesta insuficiente:** «Actualiza todo». No identifica compatibilidad ni evalúa efectos de una actualización.

### Clave 0.2.2 — Error de importación

**Caso simulado:** aparece `ModuleNotFoundError` al importar un paquete en Python.

**Pruebas iniciales de bajo riesgo:**
- `python --version`: identifica la versión invocada por ese comando.
- `python -c "import sys; print(sys.executable)"`: identifica el intérprete que ejecuta esa invocación.
- `python -m pip show nombre-paquete`: consulta si el paquete aparece instalado para ese intérprete/gestor.

Estas consultas informativas no prueban por sí solas que la aplicación use el mismo entorno: el comando de ejecución, IDE, notebook o servicio puede seleccionar otro intérprete. No se debe instalar o actualizar paquetes a ciegas. Primero compara rutas y entorno; después sigue las instrucciones oficiales del proyecto.

**Conclusión modelo:** «La hipótesis de entornos distintos sigue siendo plausible; necesito comprobar el intérprete configurado en el IDE y compararlo con la ruta de `sys.executable`». No se declara resuelto hasta reproducir la importación desde el mismo proceso/entorno.

### Clave 0.2.3 — Respuesta comunitaria

**Veredicto modelo:** una respuesta antigua que recomienda una API obsoleta se clasifica como «parcialmente vigente» u «obsoleta» según la documentación de la versión actual. Se conserva como pista histórica, no como instrucción vigente. La conclusión debe incluir URL de la pregunta, fecha, versión, documentación primaria consultada y alternativa confirmada. Si no se puede comprobar la versión, usar «no verificable».

### Clave 0.2.4 — Issue, pull request y release

**Cadena de evidencia esperada:** issue con síntoma y versión afectada → pull request que referencia la issue → revisión/merge del cambio → commit integrado → release o paquete que incluye el cambio → prueba de la versión distribuida.

Si falta el vínculo entre merge y release, la conclusión debe limitarse: «el cambio se integró en la rama principal», no «la versión publicada ya lo corrige». Una issue cerrada sin PR puede haberse cerrado por duplicado o falta de actividad.

### Clave 0.2.5 — Licencia y adopción

**Caso modelo:** el repositorio tiene README, actividad reciente y pruebas, pero no contiene una licencia identificable.

**Decisión:** no asumir permiso de reutilización, modificación o redistribución. Registrar «licencia no identificada» como bloqueo, solicitar aclaración al titular o elegir una alternativa con licencia compatible. Las estrellas, forks y disponibilidad pública no sustituyen una licencia.

**Riesgo adicional:** una licencia identificada tampoco equivale a una auditoría de seguridad. La evaluación técnica, legal y de seguridad son controles distintos.

### Clave 0.2.6 — Calibrar una comparación

**Afirmación inicial:** «La herramienta A es el doble de rápida que B».

**Reformulación comprobable:** «En el equipo [modelo], con versiones [A/B], configuración [parámetros] y carga [caso], la métrica [unidad] fue [valor] para A y [valor] para B en [n] ejecuciones; se reporta [mediana/rango].»

**Límite:** ese resultado describe el entorno y carga probados. No demuestra que A sea siempre más rápida, ni que sea mejor en consumo, fiabilidad, seguridad o coste.

### Clave 0.2.7 — Reporte reproducible

**Ejemplo de formato completo, con datos ficticios:**

- **Título:** «La importación de `paquete_demo` falla al ejecutar con el intérprete configurado en el IDE».
- **Objetivo:** ejecutar un script de demostración que importa el paquete.
- **Entorno:** sistema [versión], Python [versión], IDE [versión], entorno virtual [ruta anonimizada].
- **Pasos:** activar el entorno; ejecutar [comando]; observar el mensaje.
- **Esperado:** el módulo se importa y el script continúa.
- **Obtenido:** `ModuleNotFoundError`.
- **Pruebas:** consultar intérprete desde terminal e IDE; revisar instalación en ambos entornos.
- **Fuentes:** documentación del IDE y del gestor de paquetes, URL y fecha.
- **Conclusión:** [hipótesis apoyada / descartada / pendiente], con evidencia.
- **Seguridad:** no adjuntar rutas privadas, nombres de usuario, tokens ni archivos de configuración.

El ejemplo solo ilustra la estructura. El estudiante debe completar campos con datos observados y no copiarlo como si fuera una incidencia real.

### Control de calidad de una fuente

Antes de citar, comprueba cinco cosas:
1. **Identidad:** ¿es el sitio del mantenedor, una organización reconocida o una persona identificable?
2. **Alcance:** ¿la página trata exactamente el producto, API o fenómeno de la afirmación?
3. **Versión/fecha:** ¿corresponde al contexto investigado?
4. **Evidencia:** ¿la página contiene la explicación, dato o prueba que se atribuye?
5. **Independencia:** ¿la fuente aporta evidencia propia o repite otra publicación?

Una ficha que no permita a otra persona abrir la fuente y localizar el respaldo no es trazable.

---

## Evaluación de transferencia — expediente completo

Investiga un problema técnico real de un proyecto propio o un repositorio de demostración. Debes:
1. formular la pregunta;
2. localizar documentación primaria;
3. encontrar y evaluar una fuente comunitaria;
4. consultar una issue o pull request cuando exista;
5. inspeccionar el repositorio sin ejecutar código desconocido;
6. separar observaciones, hipótesis y opiniones;
7. producir un informe reproducible y una conclusión calibrada.

### Rúbrica analítica (100 puntos)

| Dimensión | 4 — Sólido | 3 — Adecuado | 2 — Parcial | 1 — Insuficiente | Peso |
|---|---|---|---|---|---:|
| Delimitación | Contexto, versiones y pasos suficientes | Falta un dato menor | Varias ambigüedades | Problema no reproducible | 20 |
| Fuentes | Primaria pertinente y contraste independiente | Fuentes pertinentes con contraste limitado | Predominan fuentes secundarias | Fuentes no identificables | 20 |
| Razonamiento | Hipótesis discriminantes y conclusión calibrada | Razonamiento correcto con alguna laguna | Confunde observación e inferencia | Afirmaciones sin evidencia | 20 |
| Reproducibilidad | Tercero puede repetir el caso | Requiere aclaración menor | Faltan pasos importantes | No se puede repetir | 20 |
| Seguridad y ética | Minimiza datos y evita ejecución no confiable | Riesgos menores identificados | Controles incompletos | Expone secretos o ejecuta código sin control | 10 |
| Comunicación | Informe claro, trazable y conciso | Informe comprensible | Organización irregular | No permite auditar el proceso | 10 |

**Umbral formativo sugerido:** 75/100, sin fallos críticos de seguridad y con nivel mínimo 3 en delimitación, fuentes y razonamiento. Este umbral es una propuesta didáctica del módulo, no una regla oficial de aprobación de la aplicación.

### Soluciones orientativas y retroalimentación

- Si la fuente comunitaria contradice la documentación de la versión utilizada, prioriza la documentación del mantenedor para el contrato actual y registra la discrepancia.
- Si una issue no enlaza una corrección integrada, no afirmes que el defecto fue resuelto.
- Si el repositorio carece de licencia clara, no concluyas que su código puede reutilizarse libremente.
- Si el caso solo se reproduce con datos privados, crea una entrada sintética equivalente; no publiques los datos originales.
- Si no puedes confirmar una hipótesis, registra el resultado como pendiente y propone la siguiente prueba discriminante.

## Referencias ampliadas y alcance

| Fuente | Tipo | Uso en este módulo | Consulta |
|---|---|---|---|
| Stack Overflow Help, *How to create a Minimal, Reproducible Example* — https://stackoverflow.com/help/minimal-reproducible-example | Guía comunitaria oficial del sitio | Reducir, completar y verificar ejemplos de preguntas | 2026-11-24 |
| GitHub Docs, *Using GitHub Code Search* — https://docs.github.com/en/search-github/github-code-search/using-github-code-search | Documentación oficial del servicio | Búsqueda de código y límites de indexación | 2026-11-24 |
| GitHub Docs, *Searching on GitHub* — https://docs.github.com/en/search-github/searching-on-github | Documentación oficial del servicio | Buscar repositorios, issues, pull requests y otros recursos | 2026-11-24 |
| GitHub Docs, *Repositories* — https://docs.github.com/en/repositories | Documentación oficial del servicio | Navegación y gestión de repositorios | 2026-11-24 |

**Nota de alcance:** la documentación de GitHub describe las funciones del servicio, no certifica la calidad o seguridad de un repositorio concreto. Stack Overflow explica cómo preparar preguntas reproducibles, no garantiza que sus respuestas sean correctas. Las decisiones de adopción deben contrastarse con la documentación del proyecto, su licencia y pruebas propias.

## Registro de verificación de esta ampliación

- Revisión documental y curricular: realizada contra el JSON maestro de la rama y el estándar editorial.
- Enlaces de referencia: localizados en sus dominios originales durante la revisión del 24-11-2026.
- Código ejecutado: no aplica; los talleres no incluyen un programa nuevo que se declare probado.
- Laboratorios ejecutados: ninguno.
- Videos verificados: ninguno añadido.
- Estado de trabajo: BASE DE TRABAJO ACTIVA; requiere revisión técnica, pedagógica, práctica y editorial independiente.
