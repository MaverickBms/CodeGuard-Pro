# Etapa 0 · Módulo 0.2 — Investigación técnica

**Estado:** borrador didáctico v0.1.0.  
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

## 0.2.1 — Formular preguntas técnicas

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

## 0.2.2 — Buscar y leer documentación

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

## 0.2.3 — Buscar soluciones a errores

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

## 0.2.4 — Leer Stack Overflow críticamente

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

## 0.2.5 — Consultar GitHub e investigar repositorios

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

## 0.2.6 — Diferenciar información verificada de opiniones

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

## 0.2.7 — Comunicar una investigación

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
