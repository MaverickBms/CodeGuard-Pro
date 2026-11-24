# Etapa 0 · Módulo 0.4 — Depuración

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · referencia operativa vigente de la lección 0.4. No implica publicación ni aprobación editorial.  
**Alineación:** ASCENSO 3.1, Etapa 0, apartado 0.4.  
**Temas exactos:** debugging, breakpoints, stack traces, logs, hipótesis, reproducción de errores y análisis de causas.

## Objetivo

Aprender un proceso sistemático para localizar, comprender y corregir defectos sin cambiar código al azar.

## Resultados de aprendizaje

Podrás reproducir un defecto, leer un stack trace, utilizar breakpoints, diseñar logs seguros, formular hipótesis y verificar que una corrección no introduce regresiones.

## Apéndice didáctico — Debugging

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

## Apéndice didáctico — Reproducción de errores

Registra versiones, sistema operativo, entorno, datos de entrada no sensibles, pasos exactos, frecuencia, resultado esperado y real, condiciones previas y cambios recientes.

No alteres muchas variables simultáneamente. Si el error desaparece al cambiar cinco cosas, no sabrás cuál cambio fue relevante.

**Ejercicio:** prepara un programa de práctica con un defecto lógico. Escribe pasos que permitan a otra persona reproducir el resultado incorrecto.

## Apéndice didáctico — Stack traces

Un stack trace muestra la secuencia de llamadas que condujo a una excepción. Ayuda a localizar dónde se manifestó el fallo, pero la primera línea visible no siempre es la causa raíz.

- Identifica tipo y mensaje de excepción.
- Busca el primer frame de tu propio código.
- Lee el contexto de llamadas.
- Identifica entradas y estado relevantes.
- Comprueba si intervienen dependencias o datos inválidos.
- Contrasta con documentación de la versión exacta.

**Ejercicio:** analiza un stack trace ficticio o de un proyecto propio sin datos sensibles. Señala excepción, archivo, función, línea y qué falta para confirmar la causa.

## Apéndice didáctico — Breakpoints

Un breakpoint pausa la ejecución para inspeccionar el estado.

- Colócalo antes de la operación sospechosa.
- Ejecuta el caso mínimo.
- Inspecciona variables y argumentos.
- Avanza paso a paso.
- Observa cuándo cambia el estado.
- Retira breakpoints temporales al terminar.

No compartas capturas si muestran tokens, datos personales o secretos.

**Ejercicio:** coloca un breakpoint en una función que calcula un total e inspecciona argumentos y variables intermedias.

## Apéndice didáctico — Logs

Los logs registran eventos durante la ejecución. Deben ayudar a reconstruir qué ocurrió sin inundar la salida ni exponer información privada.

- Usa niveles coherentes.
- Incluye contexto útil y, cuando corresponda, identificadores de correlación no sensibles.
- No registres contraseñas, tokens, cookies ni cuerpos completos de solicitudes.
- Evita mensajes ambiguos como «algo falló».
- Define retención y acceso apropiados.
- Distingue logs temporales de depuración de registros operativos.

**Ejercicio:** diseña cinco mensajes de log para un flujo de autenticación ficticio sin registrar credenciales ni tokens.

## Apéndice didáctico — Hipótesis

Una hipótesis debe ser concreta y comprobable.

- Observación: qué sucede.
- Hipótesis: qué condición podría explicarlo.
- Predicción: qué debería observarse si es cierta.
- Prueba: qué medición o cambio permite distinguirla.
- Resultado: evidencia obtenida.
- Conclusión: confirmada, descartada o pendiente.

Que un error aparezca después de una actualización no demuestra por sí solo que la actualización sea la causa.

## Apéndice didáctico — Causa raíz y regresión

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


---


> **Nota de alineación curricular:** los apartados heredados se conservan como apéndice de consulta. La secuencia numerada de la profundización sigue el orden oficial del maestro: debugging, breakpoints, stack traces, logs, hipótesis, reproducción de errores y análisis de causas.

## Profundización didáctica — versión 0.2.0 (24-11-2026)

Esta ampliación conserva los siete temas nominales del módulo. Los fragmentos son material didáctico propuesto; no se declara que hayan sido ejecutados en esta entrega. Las pruebas indicadas permiten que el estudiante los ejecute en su propio entorno local.

### Modelo mental: síntoma, defecto, causa y corrección

- **Síntoma:** comportamiento observable que no coincide con lo esperado.
- **Defecto:** error en un artefacto (código, configuración, datos o diseño) que puede producir el síntoma.
- **Causa raíz:** condición subyacente que explica el defecto en el contexto investigado.
- **Corrección:** cambio que elimina o controla la causa identificada.
- **Regresión:** fallo nuevo o reaparición de un comportamiento incorrecto después del cambio.

No siempre existe una única causa raíz. En sistemas distribuidos pueden interactuar varias condiciones; documenta el alcance de la conclusión.

### 0.4.1 — Debugging: seguir un procedimiento repetible

**Caso:** una función calcula un descuento incorrecto para un importe límite.

Proceso:
1. Escribe el contrato: entrada, salida esperada y reglas de negocio.
2. Construye un caso que falle y otro cercano que funcione.
3. Reproduce el síntoma sin cambiar el código.
4. Reduce el caso hasta conservar solo los datos y pasos necesarios.
5. Formula hipótesis alternativas.
6. Usa pruebas, logs o depurador para observar el estado.
7. Corrige el defecto más pequeño que explica la evidencia.
8. Ejecuta pruebas del límite, casos normales y regresión.
9. Documenta qué se comprobó y qué queda fuera.

**Ejercicio:** describe el resultado esperado para importes inferiores, iguales y superiores al umbral. Explica por qué probar únicamente un importe alto no detectaría todos los defectos de comparación.

### 0.4.2 — Breakpoints: observar el estado sin adivinar

En Visual Studio Code:
1. Abre la carpeta del proyecto.
2. Confirma que el runtime/SDK del lenguaje está instalado.
3. Coloca un breakpoint en una línea ejecutable antes del cálculo sospechoso.
4. Inicia una sesión de depuración con la configuración adecuada.
5. Inspecciona argumentos y variables.
6. Avanza una línea cada vez y observa dónde diverge el valor esperado.
7. Comprueba el call stack y el contexto.
8. Retira breakpoints temporales y repite la prueba sin depurador.

En Python también se puede utilizar `breakpoint()` o `python -m pdb archivo.py`. La experiencia depende de la versión de Python y de la configuración del entorno.

**Ejercicio:** registra tres valores antes y después de una operación. No entregues solo una captura: explica qué hipótesis confirma o descarta cada observación.

### 0.4.3 — Stack traces: leer desde el error hacia el contexto

Un stack trace de Python puede tener esta forma ilustrativa:

```text
Traceback (most recent call last):
  File "demo.py", line 8, in <module>
    print(calcular_total("10", 2))
  File "demo.py", line 4, in calcular_total
    return precio * cantidad + 1
TypeError: can only concatenate str (not "int") to str
```

**Lectura guiada**
1. La última línea identifica tipo y mensaje de la excepción.
2. Los frames muestran la ruta de llamadas hasta el punto donde se manifestó.
3. La línea indicada en la función muestra la operación que falló.
4. La entrada `"10"` es una cadena, no un número.
5. Antes de corregir, define si la función debe aceptar texto o solo valores numéricos. La validación debe corresponder al contrato.

**Ejercicio:** explica por qué convertir cualquier valor a número sin validar podría ocultar datos mal formados. Propón una validación explícita y un mensaje de error útil.

### 0.4.4 — Logs: observabilidad útil y segura

Un evento de log debería responder, según el caso: qué ocurrió, cuándo, en qué componente, con qué resultado y bajo qué contexto no sensible.

**Ejemplo adecuado (conceptual):**
```text
2026-11-24T10:15:00Z INFO billing.calculation
request_ref=demo-014 outcome=completed currency=COP item_count=2
```

**Ejemplo inadecuado:**
```text
INFO login password=... access_token=... cookie=...
```

No registres contraseñas, tokens, cookies, claves, datos bancarios ni cuerpos completos de solicitudes por defecto. Enmascarar parcialmente un secreto no garantiza que sea imposible reconstruirlo. Define acceso, retención y protección de registros de acuerdo con su sensibilidad.

**Ejercicio:** redacta seis eventos para un flujo de compra ficticio: inicio, validación, cálculo, rechazo, finalización y error inesperado. Cada evento debe aportar contexto sin revelar información sensible.

### 0.4.5 — Hipótesis: diseñar pruebas que distingan explicaciones

Una hipótesis útil tiene:
- observación verificable;
- mecanismo propuesto;
- predicción observable;
- prueba discriminante;
- resultado;
- conclusión limitada al alcance probado.

**Ejemplo:** «El descuento falla porque la comparación excluye el valor límite». Predicción: el importe exactamente igual al umbral no recibe descuento, mientras que uno apenas superior sí. Prueba: comparar ambos casos con la misma configuración.

No cambies simultáneamente umbral, tasa, formato de entrada y entorno. Si el resultado cambia, no podrás atribuirlo a una sola causa.

**Ejercicio:** escribe dos hipótesis alternativas para un cálculo incorrecto y una prueba que permita distinguirlas sin introducir múltiples cambios.

### 0.4.6 — Reproducción de errores: fijar las condiciones

Un reporte reproducible identifica el estado inicial. Incluye:
- versión de lenguaje/runtime y dependencias;
- sistema operativo y arquitectura cuando sean relevantes;
- comando exacto de ejecución;
- configuración pertinente, sin secretos;
- entrada mínima;
- pasos ordenados;
- resultado esperado y real;
- frecuencia y condiciones de aparición.

**Ejercicio:** entrega un caso que otra persona pueda ejecutar sin tener que adivinar variables de entorno o archivos de entrada. Si no puede reproducirlo, registra qué dato falta; no declares el defecto corregido.

### 0.4.7 — Análisis de causas: corregir y prevenir regresiones

Una corrección queda respaldada cuando:
1. el caso falla antes del cambio;
2. una prueba automatizada o manual captura el comportamiento incorrecto;
3. la modificación elimina la causa identificada;
4. el caso original pasa;
5. los límites y escenarios vecinos pasan;
6. las pruebas relacionadas no muestran regresiones;
7. el cambio y su justificación quedan documentados.

No llames «causa raíz confirmada» a una correlación temporal. Una actualización previa puede ser una pista, no una demostración causal.

## Laboratorio guiado — cálculo de factura con error de límite

**Objetivo:** localizar un defecto de comparación, justificar una hipótesis y demostrar la corrección con pruebas de frontera.

**Requisitos:** Python 3.11 o superior, terminal y editor de texto. No requiere paquetes externos. Comprueba tu versión con `python --version` (en algunos sistemas el comando es `python3 --version`).

### Código inicial con defecto deliberado

Guarda como `factura.py`:

```python
def calcular_total(subtotal: float) -> float:
    if subtotal > 100:
        descuento = 0.10
    else:
        descuento = 0.0

    return subtotal * (1 - descuento)


if __name__ == "__main__":
    for importe in (99.99, 100.00, 100.01):
        print(f"{importe:.2f} -> {calcular_total(importe):.2f}")
```

**Contrato del ejercicio:** se aplica un descuento del 10 % cuando el subtotal es igual o superior a 100 unidades monetarias. Para importes inferiores no hay descuento. El ejemplo no modela impuestos, redondeos fiscales ni reglas comerciales reales.

### Actividades

1. Antes de ejecutar, predice la salida para los tres importes.
2. Ejecuta el archivo y conserva la salida.
3. Compara cada resultado con el contrato.
4. Formula una hipótesis concreta sobre el operador de comparación.
5. Coloca un breakpoint en la condición y observa `subtotal` y `descuento`.
6. Cambia únicamente la condición para incluir el límite.
7. Repite exactamente las tres entradas.
8. Añade pruebas automatizadas para los tres casos.
9. Registra causa, corrección y alcance.

### Pruebas de aceptación

| Entrada | Resultado esperado |
|---:|---:|
| 99.99 | 99.99 |
| 100.00 | 90.00 |
| 100.01 | 90.01 |

**Solución razonada (consultar después del intento):** la condición inicial utiliza `>`, por lo que el valor exactamente igual a 100 sigue la rama sin descuento. El contrato dice «igual o superior»; la corrección es utilizar `>=`. No es necesario cambiar la fórmula ni redondear de otra manera.

### Pruebas automatizadas de referencia

Guarda junto a `factura.py` un archivo `test_factura.py`:

```python
import unittest

from factura import calcular_total


class CalcularTotalTests(unittest.TestCase):
    def test_sin_descuento_bajo_umbral(self):
        self.assertAlmostEqual(calcular_total(99.99), 99.99)

    def test_descuento_en_el_limite(self):
        self.assertAlmostEqual(calcular_total(100.00), 90.00)

    def test_descuento_sobre_el_limite(self):
        self.assertAlmostEqual(calcular_total(100.01), 90.009)


if __name__ == "__main__":
    unittest.main()
```

Ejecuta con `python -m unittest -v`. La prueba del límite debe fallar con el código inicial y pasar después de aplicar la corrección. La tolerancia de `assertAlmostEqual` evita comparar directamente representaciones binarias de números de punto flotante.

**Extensión:** define el comportamiento para subtotal negativo, cero, texto y valores no finitos. No inventes reglas de negocio: documenta primero qué entradas acepta el contrato y luego implementa la validación.

### Entregables

- contrato de la función;
- predicción inicial;
- salida observada antes y después;
- hipótesis y prueba discriminante;
- captura o registro del breakpoint sin información sensible;
- diff de la corrección;
- pruebas y resultados reales;
- informe breve de causa raíz y limitaciones.

### Rúbrica analítica (100 puntos)

| Criterio | Peso | Evidencia |
|---|---:|---|
| Reproducción | 15 | Mismo caso falla antes de corregir |
| Stack trace/observación | 10 | Interpreta correctamente el contexto |
| Breakpoints | 15 | Identifica el valor que cruza el límite |
| Hipótesis | 15 | Predicción distingue la causa propuesta |
| Corrección | 15 | Cambio mínimo alineado con el contrato |
| Regresión | 20 | Casos inferior, igual y superior comprobados |
| Comunicación y seguridad | 10 | Informe reproducible sin datos sensibles |

**Dominio sugerido:** 80/100 y evidencia de que la prueba de frontera falla antes y pasa después. La puntuación no reemplaza la revisión de un docente.

## Autoevaluación con retroalimentación

1. **¿Por qué el último frame de un stack trace no siempre es la causa raíz?**  
   Porque identifica dónde se lanzó o manifestó la excepción; el origen puede estar en una entrada, estado o llamada anterior.

2. **¿Qué diferencia hay entre reproducir y observar?**  
   Reproducir establece de nuevo las condiciones del fallo; observar recoge evidencia durante esa ejecución.

3. **¿Por qué probar 99.99 y 100.01 no basta?**  
   Porque no prueba el valor límite exacto, que es donde se manifiesta el error de comparación.

4. **¿Qué debe ocurrir con un token en un log?**  
   No debe registrarse. Se debe rediseñar el evento para usar una referencia no sensible.

5. **¿Qué demuestra una prueba de regresión?**  
   Que los comportamientos cubiertos siguen cumpliendo el contrato tras el cambio; no demuestra ausencia total de defectos.

## Referencias técnicas y vigencia

- Python, *pdb — The Python Debugger*: https://docs.python.org/3/library/pdb.html — documentación oficial del depurador; describe breakpoints, stepping, stack frames y uso post-mortem. Consultada 2026-11-24.
- Visual Studio Code, *Debug code with Visual Studio Code*: https://code.visualstudio.com/docs/debugtest/debugging — documentación oficial de sesiones, breakpoints, inspección de variables y call stack. Consultada 2026-11-24.
- Visual Studio Code, *Debug your first application*: https://code.visualstudio.com/docs/debugtest/quickstart — recorrido guiado para reproducir y corregir un defecto. Consultada 2026-11-24.
- OpenTelemetry, *Logs*: https://opentelemetry.io/docs/specs/otel/logs/ — especificación y modelo de datos de logs; no sustituye una política de privacidad o retención propia. La página debe revisarse antes de publicación para fijar la versión de la especificación.

## Registro de verificación

- Revisión de contenido: realizada contra los siete temas del JSON maestro.
- Código del laboratorio: escrito como ejemplo didáctico; no ejecutado por el autor en esta entrega.
- Pruebas unitarias: diseñadas; ejecución pendiente.
- Breakpoints y logs: instrucciones revisadas; práctica de estudiante pendiente.
- Laboratorio: no ejecutado.
- Videos: ninguno verificado ni añadido.
- Estado de trabajo: BASE DE TRABAJO ACTIVA; requiere revisión técnica, pedagógica, práctica y editorial independiente.
