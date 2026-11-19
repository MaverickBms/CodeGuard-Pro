# Etapa 0 · Módulo 0.4 — Depuración

**Estado:** borrador didáctico v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 0, apartado 0.4.  
**Temas exactos:** debugging, breakpoints, stack traces, logs, hipótesis, reproducción de errores y análisis de causas.

## Objetivo

Aprender un proceso sistemático para localizar, comprender y corregir defectos sin cambiar código al azar.

## Resultados de aprendizaje

Podrás reproducir un defecto, leer un stack trace, utilizar breakpoints, diseñar logs seguros, formular hipótesis y verificar que una corrección no introduce regresiones.

## 0.4.1 — Debugging

Depurar es investigar un comportamiento que no cumple lo esperado; no consiste en editar líneas hasta que el error desaparezca.

**Ciclo**
1. Describe resultado esperado y real.
2. Reproduce el problema.
3. Reduce el caso a un ejemplo mínimo.
4. Formula hipótesis.
5. Diseña una prueba que distinga hipótesis.
6. Observa variables, flujo y estado.
7. Corrige la causa identificada.
8. Ejecuta pruebas de regresión.
9. Documenta causa y cambio.

## 0.4.2 — Reproducción de errores

Registra versiones, sistema operativo, entorno, datos de entrada no sensibles, pasos exactos, frecuencia, resultado esperado y real, condiciones previas y cambios recientes.

No alteres muchas variables simultáneamente. Si el error desaparece al cambiar cinco cosas, no sabrás cuál cambio fue relevante.

**Ejercicio:** prepara un programa de práctica con un defecto lógico. Escribe pasos que permitan a otra persona reproducir el resultado incorrecto.

## 0.4.3 — Stack traces

Un stack trace muestra la secuencia de llamadas que condujo a una excepción. Ayuda a localizar dónde se manifestó el fallo, pero la primera línea visible no siempre es la causa raíz.

- Identifica tipo y mensaje de excepción.
- Busca el primer frame de tu propio código.
- Lee el contexto de llamadas.
- Identifica entradas y estado relevantes.
- Comprueba si intervienen dependencias o datos inválidos.
- Contrasta con documentación de la versión exacta.

**Ejercicio:** analiza un stack trace ficticio o de un proyecto propio sin datos sensibles. Señala excepción, archivo, función, línea y qué falta para confirmar la causa.

## 0.4.4 — Breakpoints

Un breakpoint pausa la ejecución para inspeccionar el estado.

- Colócalo antes de la operación sospechosa.
- Ejecuta el caso mínimo.
- Inspecciona variables y argumentos.
- Avanza paso a paso.
- Observa cuándo cambia el estado.
- Retira breakpoints temporales al terminar.

No compartas capturas si muestran tokens, datos personales o secretos.

**Ejercicio:** coloca un breakpoint en una función que calcula un total e inspecciona argumentos y variables intermedias.

## 0.4.5 — Logs

Los logs registran eventos durante la ejecución. Deben ayudar a reconstruir qué ocurrió sin inundar la salida ni exponer información privada.

- Usa niveles coherentes.
- Incluye contexto útil y, cuando corresponda, identificadores de correlación no sensibles.
- No registres contraseñas, tokens, cookies ni cuerpos completos de solicitudes.
- Evita mensajes ambiguos como «algo falló».
- Define retención y acceso apropiados.
- Distingue logs temporales de depuración de registros operativos.

**Ejercicio:** diseña cinco mensajes de log para un flujo de autenticación ficticio sin registrar credenciales ni tokens.

## 0.4.6 — Hipótesis

Una hipótesis debe ser concreta y comprobable.

- Observación: qué sucede.
- Hipótesis: qué condición podría explicarlo.
- Predicción: qué debería observarse si es cierta.
- Prueba: qué medición o cambio permite distinguirla.
- Resultado: evidencia obtenida.
- Conclusión: confirmada, descartada o pendiente.

Que un error aparezca después de una actualización no demuestra por sí solo que la actualización sea la causa.

## 0.4.7 — Causa raíz y regresión

- Reproduce el defecto antes del cambio.
- Añade una prueba que falle antes y pase después, cuando sea viable.
- Aplica la corrección mínima coherente.
- Ejecuta pruebas relacionadas y de regresión.
- Comprueba escenarios límite.
- Documenta efectos secundarios y limitaciones.

## Laboratorio — Depurar un sistema de cálculo

Construye un programa local que reciba cantidades y calcule subtotal, descuento e impuesto. Introduce defectos controlados: condición de borde, variable mal inicializada y fórmula incorrecta.

Entrega:
1. especificación de resultados esperados;
2. tres casos reproducibles;
3. stack trace o logs cuando corresponda;
4. hipótesis y pruebas;
5. corrección;
6. pruebas de regresión;
7. informe de causa raíz.

No uses datos reales ni ejecutes código de terceros.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Reproducción clara | 15 |
| Lectura de stack trace | 15 |
| Uso de breakpoints | 15 |
| Logs seguros y útiles | 15 |
| Hipótesis y pruebas | 20 |
| Corrección y regresión | 20 |

## Video candidato — investigar bugs (audio pendiente de verificación)

**[Tips para enfrentar BUGS y BLOQUEOS como programador — Programación en español](https://www.youtube.com/watch?v=21_f6fglZ_A)**  
Idioma hablado: pendiente de verificación mediante escucha. Pertinencia prevista: trata contexto del problema, búsqueda de soluciones, Stack Overflow, GitHub Issues, trazabilidad y aproximaciones para resolver bloqueos. No aprobar ni recomendar hasta confirmar audio real en español y correspondencia con el contenido.  
Actividad: aplicar el enfoque de investigación a uno de los defectos del laboratorio. El video complementa la investigación, pero no sustituye la práctica específica con breakpoints, stack traces y logs.

No se agregan videos genéricos de programación ni recursos en inglés. Si no se encuentra una pieza en español directamente alineada con un subtema, se mantiene la explicación y el laboratorio sin forzar un enlace.

## Autoevaluación

1. ¿Por qué un stack trace no siempre muestra directamente la causa raíz?
2. ¿Qué diferencia existe entre síntoma e hipótesis?
3. ¿Qué ventaja aporta reproducir un error con un caso mínimo?
4. ¿Qué información nunca debería aparecer en logs?
5. ¿Cómo compruebas que una corrección no introdujo regresiones?

## Referencias

- Python pdb: https://docs.python.org/3/library/pdb.html
- VS Code, depuración: https://code.visualstudio.com/docs/editor/debugging
- OpenTelemetry, logs: https://opentelemetry.io/docs/specs/otel/logs/
- Video: https://www.youtube.com/watch?v=21_f6fglZ_A

**Fecha de consulta:** 19-11-2026. Revisar enlaces y contenido antes de aprobar o publicar.
