# Etapa 2 · Módulo 2.3 — Algoritmos iniciales

**Estado:** borrador académico desarrollado (pendiente validación editorial externa).  
**Alineación:** ASCENSO 3.1, Etapa 2, Módulo 2.3.  
**Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 2 — Pensamiento computacional, lógica y matemáticas.
- **Módulo:** 2.3 — Algoritmos iniciales.
- **Lecciones oficiales:** 10 (2.3.1 a 2.3.10).

## Propósito
Aprender a diseñar soluciones paso a paso mediante algoritmos, pseudocódigo y estructuras básicas.

## Resultados de aprendizaje
1. Identificar entrada, procesamiento y salida.
2. Representar algoritmos con pseudocódigo y diagramas de flujo.
3. Usar variables, contadores, acumuladores, condiciones e iteraciones.
4. Trazar algoritmos y detectar errores lógicos.

---

## Lección 2.3.1 — Entrada

### Identificación
- **Lección oficial:** 2.3.1 — Entrada. **Secuencia:** 1/10.

### Propósito de aprendizaje
Identificar los datos que un algoritmo necesita para comenzar.

### Conocimientos previos
- Módulos 2.1 y 2.2.

### Resultados de aprendizaje
- Definir entrada de un algoritmo.
- Identificar entradas explícitas e implícitas.
- Validar entradas mínimas.
- Documentar entradas con tipo y restricción.

### Desarrollo conceptual
La **entrada** es el conjunto de datos que el algoritmo recibe para resolver un problema. Puede venir del usuario, un archivo, una base de datos, un sensor, una API u otro proceso.

Una entrada bien definida especifica: nombre, tipo, rango, formato, obligatoriedad y qué ocurre si falta o es inválida. No definir entradas conduce a ambigüedad y errores.

Entradas implícitas son datos que el algoritmo usa pero no se pasan explícitamente (configuración, hora del sistema, estado global). Conviene hacerlas visibles para evitar sorpresas.

### Ejemplo técnico desarrollado
**Algoritmo:** calcular precio final.
- Entradas: `precio` (número > 0), `descuento` (0-100).
- Inválidas: precio negativo, descuento 150.

### Práctica guiada
- Define entradas para un algoritmo que calcula la edad a partir de fecha de nacimiento.

### Actividad independiente
Documenta entradas para un sistema de login, incluyendo entradas inválidas.

### Criterios de aceptación
- Entradas nombradas y tipadas.
- Restricciones claras.
- Casos inválidos considerados.

### Errores frecuentes y recomendaciones
- **Error:** asumir entrada siempre válida. **Recomendación:** validar.
- **Error:** olvidar unidades/formato. **Recomendación:** especificar.

### Evaluación de comprensión
1. ¿Qué es una entrada?
2. Da un ejemplo de entrada implícita.
3. ¿Por qué importa el rango de una entrada?

### Referencias
- Cormen, T. H., et al. *Introduction to Algorithms*. MIT Press.

---

## Lección 2.3.2 — Procesamiento

### Identificación
- **Lección oficial:** 2.3.2 — Procesamiento. **Secuencia:** 2/10.

### Propósito de aprendizaje
Definir los pasos que transforman entradas en resultados.

### Conocimientos previos
- Lección 2.3.1.

### Resultados de aprendizaje
- Definir procesamiento.
- Descomponer procesamiento en pasos ordenados.
- Identificar operaciones y decisiones.
- Verificar que el procesamiento es determinista cuando corresponde.

### Desarrollo conceptual
El **procesamiento** es la parte del algoritmo que transforma entradas en salidas. Incluye cálculos, comparaciones, asignaciones, llamadas a otros procesos y control de flujo.

Un buen procesamiento es claro, ordenado y verificable. Cada paso debe tener un propósito. Si un paso depende de una condición, debe indicarse.

El procesamiento puede ser determinista (misma entrada, misma salida) o no determinista (aleatoriedad, tiempo, estado externo). En aprendizaje inicial conviene priorizar algoritmos deterministas.

### Ejemplo técnico desarrollado
**Entrada:** precio=100, descuento=15.
**Procesamiento:** `monto_descuento = precio * descuento / 100`; `total = precio - monto_descuento`.
**Salida:** total=85.

### Práctica guiada
- Describe el procesamiento para convertir Celsius a Fahrenheit.

### Actividad independiente
Escribe el procesamiento para determinar si un número es par o impar.

### Criterios de aceptación
- Pasos ordenados.
- Usa entradas definidas.
- Produce salida lógica.

### Errores frecuentes y recomendaciones
- **Error:** saltos implícitos. **Recomendación:** escribir cada paso.
- **Error:** usar variables no definidas. **Recomendación:** definir antes de usar.

### Evaluación de comprensión
1. ¿Qué es procesamiento?
2. ¿Qué hace determinista a un algoritmo?
3. Identifica un paso ambiguo en un algoritmo mal escrito.

### Referencias
- Cormen, T. H., et al. *Introduction to Algorithms*. MIT Press.

---

## Lección 2.3.3 — Salida

### Identificación
- **Lección oficial:** 2.3.3 — Salida. **Secuencia:** 3/10.

### Propósito de aprendizaje
Definir claramente el resultado que produce un algoritmo.

### Conocimientos previos
- Lecciones 2.3.1 y 2.3.2.

### Resultados de aprendizaje
- Definir salida.
- Especificar formato y significado de la salida.
- Distinguir salida correcta de salida esperada.
- Considerar salidas de error.

### Desarrollo conceptual
La **salida** es el resultado entregado por el algoritmo: un valor, mensaje, archivo, registro, acción o cambio de estado. Debe ser clara, completa y útil para quien la consume.

También hay que definir salidas de error: ¿qué pasa si la entrada es inválida? ¿se devuelve error, valor nulo, excepción o mensaje? No definir esto genera comportamientos ambiguos.

La salida debe corresponder al problema. Si el problema pide el mayor de tres números, devolver la suma es una salida incorrecta aunque esté bien calculada.

### Ejemplo técnico desarrollado
**Algoritmo:** login.
- Salida éxito: `{"ok": true, "usuario": "ana"}`.
- Salida error: `{"ok": false, "error": "credenciales inválidas"}`.

### Práctica guiada
- Define salidas para un algoritmo que busca un producto por ID.

### Actividad independiente
Diseña salidas de éxito y error para un conversor de moneda.

### Criterios de aceptación
- Salida definida con formato.
- Incluye caso de error.
- Responde al problema.

### Errores frecuentes y recomendaciones
- **Error:** no definir salida de error. **Recomendación:** incluir caminos alternativos.
- **Error:** salida ambigua. **Recomendación:** especificar tipo y significado.

### Evaluación de comprensión
1. ¿Qué es una salida?
2. ¿Por qué definir salidas de error?
3. Da un ejemplo de salida correcta en formato incorrecto.

### Referencias
- Cormen, T. H., et al. *Introduction to Algorithms*. MIT Press.

---

## Lección 2.3.4 — Pseudocódigo

### Identificación
- **Lección oficial:** 2.3.4 — Pseudocódigo. **Secuencia:** 4/10.

### Propósito de aprendizaje
Representar algoritmos con pseudocódigo claro e independiente del lenguaje.

### Conocimientos previos
- Lecciones 2.3.1 a 2.3.3.

### Resultados de aprendizaje
- Escribir pseudocódigo legible.
- Usar estructuras básicas: asignación, condición, iteración.
- Trazar un pseudocódigo.
- Convertir pseudocódigo simple a código.

### Desarrollo conceptual
El **pseudocódigo** es una descripción estructurada de un algoritmo usando lenguaje natural y convenciones de programación, sin depender de la sintaxis de un lenguaje específico. Su objetivo es comunicar la lógica.

Buenas prácticas:
- Usar nombres claros.
- Indentar bloques.
- Usar `SI/ENTONCES/SINO`, `MIENTRAS`, `PARA`, `RETORNAR`.
- Ser consistente.

El pseudocódigo no se ejecuta directamente, pero debe ser suficientemente preciso para implementarse.

### Ejemplo técnico desarrollado
```text
INICIO
  LEER nota
  SI nota >= 60 ENTONCES
    ESCRIBIR "Aprobado"
  SINO
    ESCRIBIR "Reprobado"
  FIN SI
FIN
```

### Práctica guiada
- Escribe pseudocódigo para determinar el mayor de dos números.

### Actividad independiente
Escribe pseudocódigo para calcular el promedio de N notas.

### Criterios de aceptación
- Lógica correcta.
- Estructura clara.
- Incluye entrada, procesamiento y salida.

### Errores frecuentes y recomendaciones
- **Error:** pseudocódigo demasiado vago. **Recomendación:** incluir condiciones y pasos concretos.
- **Error:** mezclar sintaxis de muchos lenguajes. **Recomendación:** mantener consistencia.

### Evaluación de comprensión
1. ¿Para qué sirve el pseudocódigo?
2. ¿Por qué no depende de un lenguaje?
3. Convierte un pseudocódigo simple a Python.

### Referencias
- Cormen, T. H., et al. *Introduction to Algorithms*. MIT Press.

---

## Lección 2.3.5 — Diagramas de flujo

### Identificación
- **Lección oficial:** 2.3.5 — Diagramas de flujo. **Secuencia:** 5/10.

### Propósito de aprendizaje
Representar algoritmos visualmente con diagramas de flujo.

### Conocimientos previos
- Lección 2.3.4.

### Resultados de aprendizaje
- Identificar símbolos básicos de diagramas de flujo.
- Crear un diagrama de flujo simple.
- Trazar el flujo de ejecución.
- Comparar diagrama de flujo y pseudocódigo.

### Desarrollo conceptual
Un **diagrama de flujo** representa un algoritmo mediante símbolos conectados por flechas. Símbolos comunes:
- Óvalo: inicio/fin.
- Paralelogramo: entrada/salida.
- Rectángulo: proceso.
- Rombo: decisión.
- Flechas: flujo.

Los diagramas son útiles para visualizar decisiones y ciclos, pero pueden volverse difíciles de mantener en algoritmos grandes. Por eso se usan más en enseñanza, documentación inicial o procesos simples.

### Ejemplo técnico desarrollado
**Aprobar/reprobar:**
Inicio -> Leer nota -> ¿nota >= 60? -> Sí: "Aprobado" -> Fin; No: "Reprobado" -> Fin.

### Práctica guiada
- Dibuja un diagrama de flujo para verificar si un número es positivo, negativo o cero.

### Actividad independiente
Crea un diagrama de flujo para un cajero que valida PIN (máximo 3 intentos).

### Criterios de aceptación
- Símbolos adecuados.
- Flujo completo.
- Decisiones con salidas Sí/No.

### Errores frecuentes y recomendaciones
- **Error:** decisiones sin dos salidas. **Recomendación:** todo rombo debe tener caminos claros.
- **Error:** flechas ambiguas. **Recomendación:** etiquetar Sí/No.

### Evaluación de comprensión
1. ¿Qué símbolo representa una decisión?
2. ¿Cuándo prefieres pseudocódigo sobre diagrama de flujo?
3. Traza un diagrama con un ciclo.

### Referencias
- ISO 5807. *Information processing — Documentation symbols and conventions for data, program and system flowcharts*. (Referencia normativa; verificar edición aplicable).

---

## Lección 2.3.6 — Variables

### Identificación
- **Lección oficial:** 2.3.6 — Variables. **Secuencia:** 6/10.

### Propósito de aprendizaje
Comprender el uso de variables para almacenar y manipular datos.

### Conocimientos previos
- Lecciones 2.3.1 a 2.3.4.

### Resultados de aprendizaje
- Definir variable.
- Distinguir nombre, valor y tipo.
- Usar variables en pseudocódigo/algoritmos.
- Identificar errores de variable no inicializada.

### Desarrollo conceptual
Una **variable** es un nombre asociado a un valor que puede cambiar durante la ejecución. En un nivel conceptual, permite almacenar datos para usarlos después.

Una variable tiene: nombre, valor, tipo (en lenguajes tipados o en tiempo de ejecución), ámbito y tiempo de vida. La asignación cambia el valor asociado.

Nombrar bien importa: `edad`, `total`, `contador` comunican intención; `x1`, `tmp2` pueden ser ambiguos.

### Ejemplo técnico desarrollado
```text
precio = 100
descuento = 10
total = precio - descuento
ESCRIBIR total
```
`total` cambia según entradas. Si no se inicializa, el resultado es impredecible.

### Práctica guiada
- Crea variables para representar un estudiante: nombre, edad, notaFinal.

### Actividad independiente
Escribe un algoritmo que intercambie dos variables e indica si necesitas una variable temporal.

### Criterios de aceptación
- Nombres claros.
- Asignaciones correctas.
- No usa variables sin definir.

### Errores frecuentes y recomendaciones
- **Error:** usar variable antes de asignarla. **Recomendación:** inicializar.
- **Error:** nombres crípticos. **Recomendación:** nombres descriptivos.

### Evaluación de comprensión
1. ¿Qué es una variable?
2. ¿Qué significa inicializar?
3. ¿Por qué el nombre importa?

### Referencias
- Python Documentation. *Variables and assignment*. https://docs.python.org/3/reference/simple_stmts.html#assignment-statements. Consultado: 2026-11-24.

---

## Lección 2.3.7 — Contadores

### Identificación
- **Lección oficial:** 2.3.7 — Contadores. **Secuencia:** 7/10.

### Propósito de aprendizaje
Usar contadores para controlar repeticiones y conteos.

### Conocimientos previos
- Lección 2.3.6.

### Resultados de aprendizaje
- Definir contador.
- Inicializar e incrementar correctamente.
- Usar contadores en ciclos.
- Evitar errores de off-by-one.

### Desarrollo conceptual
Un **contador** es una variable que se incrementa (o decrementa) para llevar la cuenta de ocurrencias o iteraciones. Ejemplo típico: contar cuántos elementos cumplen una condición.

Reglas: inicializar antes del ciclo, actualizar en el lugar correcto, y usar condición de parada adecuada. Errores comunes: empezar en 1 cuando debía ser 0, o usar `<` en vez de `<=`.

### Ejemplo técnico desarrollado
```text
contador = 0
PARA i DESDE 1 HASTA 10 HACER
  SI i ES PAR ENTONCES
    contador = contador + 1
  FIN SI
FIN PARA
ESCRIBIR contador
```
Resultado: 5.

### Práctica guiada
- Escribe un algoritmo que cuente cuántos números negativos hay en una lista.

### Actividad independiente
Cuenta cuántas vocales hay en una palabra dada.

### Criterios de aceptación
- Inicialización correcta.
- Incremento en el lugar correcto.
- Resultado correcto.

### Errores frecuentes y recomendaciones
- **Error:** no inicializar. **Recomendación:** siempre inicializar.
- **Error:** incrementar fuera de condición cuando no corresponde. **Recomendación:** trazar el algoritmo.

### Evaluación de comprensión
1. ¿Qué es un contador?
2. ¿Qué es un error off-by-one?
3. Da un ejemplo de contador decreciente.

### Referencias
- Cormen, T. H., et al. *Introduction to Algorithms*. MIT Press.

---

## Lección 2.3.8 — Acumuladores

### Identificación
- **Lección oficial:** 2.3.8 — Acumuladores. **Secuencia:** 8/10.

### Propósito de aprendizaje
Usar acumuladores para sumar o agregar valores progresivamente.

### Conocimientos previos
- Lecciones 2.3.6 y 2.3.7.

### Resultados de aprendizaje
- Definir acumulador.
- Distinguir contador y acumulador.
- Usar acumuladores para sumas/promedios.
- Inicializar correctamente según operación.

### Desarrollo conceptual
Un **acumulador** es una variable que almacena un resultado parcial que se actualiza repetidamente. A diferencia del contador, que suele sumar 1, el acumulador suma valores variables (totales, productos, concatenaciones, etc.).

Ejemplos: suma de ventas, total de puntos, promedio (acumulador + contador).

La inicialización depende de la operación: suma suele iniciar en 0, producto en 1. Una inicialización incorrecta altera todo el resultado.

### Ejemplo técnico desarrollado
```text
suma = 0
PARA cada nota EN notas HACER
  suma = suma + nota
FIN PARA
promedio = suma / cantidad
```

### Práctica guiada
- Calcula el total de una lista de precios.

### Actividad independiente
Escribe un algoritmo que calcule el factorial de N usando un acumulador.

### Criterios de aceptación
- Inicialización correcta.
- Distingue contador/acumulador.
- Resultado correcto.

### Errores frecuentes y recomendaciones
- **Error:** inicializar acumulador de producto en 0. **Recomendación:** usar elemento neutro.
- **Error:** confundir contador con acumulador. **Recomendación:** contador cuenta, acumulador agrega valor.

### Evaluación de comprensión
1. ¿Qué diferencia hay entre contador y acumulador?
2. ¿En qué valor inicializas un acumulador de suma?
3. ¿Y uno de producto?

### Referencias
- Cormen, T. H., et al. *Introduction to Algorithms*. MIT Press.

---

## Lección 2.3.9 — Condiciones

### Identificación
- **Lección oficial:** 2.3.9 — Condiciones. **Secuencia:** 9/10.

### Propósito de aprendizaje
Usar estructuras condicionales para tomar decisiones en algoritmos.

### Conocimientos previos
- Módulo 2.2, Lección 2.3.4.

### Resultados de aprendizaje
- Usar SI/ENTONCES/SINO.
- Combinar condiciones con AND/OR/NOT.
- Cubrir casos mutuamente excluyentes.
- Evitar condiciones ambiguas.

### Desarrollo conceptual
Una **condición** permite que el algoritmo tome caminos diferentes según una expresión booleana. Las estructuras comunes son `if`, `if-else`, `if-elif-else`, `switch/case`.

Es importante cubrir casos: ¿qué pasa si ninguna condición se cumple? ¿las condiciones se solapan? ¿el orden importa?

Las condiciones deben basarse en expresiones claras y comprobables. En código real, también se debe considerar evaluación de cortocircuito y legibilidad.

### Ejemplo técnico desarrollado
```text
SI edad < 0 ENTONCES
  ESCRIBIR "Edad inválida"
SINO SI edad < 18 ENTONCES
  ESCRIBIR "Menor de edad"
SINO
  ESCRIBIR "Mayor de edad"
FIN SI
```

### Práctica guiada
- Escribe condiciones para clasificar una nota: insuficiente, suficiente, notable, sobresaliente.

### Actividad independiente
Diseña un algoritmo que determine si un año es bisiesto (reglas completas).

### Criterios de aceptación
- Condiciones correctas.
- Casos cubiertos.
- Sin solapamientos no deseados.

### Errores frecuentes y recomendaciones
- **Error:** condiciones solapadas mal ordenadas. **Recomendación:** ordenar de más específica a más general.
- **Error:** olvidar caso por defecto. **Recomendación:** incluir `SINO`.

### Evaluación de comprensión
1. ¿Qué es una condición?
2. ¿Por qué importa el orden en `if-elif`?
3. Da un ejemplo de condición compuesta.

### Referencias
- Python Docs. *if statements*. https://docs.python.org/3/tutorial/controlflow.html#if-statements. Consultado: 2026-11-24.

---

## Lección 2.3.10 — Iteraciones

### Identificación
- **Lección oficial:** 2.3.10 — Iteraciones. **Secuencia:** 10/10.

### Propósito de aprendizaje
Usar ciclos para repetir acciones controladamente.

### Conocimientos previos
- Lecciones 2.3.7 a 2.3.9.

### Resultados de aprendizaje
- Definir iteración.
- Usar ciclos PARA/MIENTRAS/REPETIR.
- Evitar ciclos infinitos.
- Elegir el tipo de ciclo adecuado.

### Desarrollo conceptual
Una **iteración** es la repetición de un bloque de instrucciones. Los ciclos permiten procesar colecciones, repetir hasta una condición o ejecutar un número conocido de veces.

- **PARA (for):** cuando se conoce el número de iteraciones o se recorre una colección.
- **MIENTRAS (while):** cuando se repite mientras una condición sea verdadera.
- **REPETIR/HASTA (do-while):** ejecuta al menos una vez.

Todo ciclo necesita: estado inicial, condición/parada y progreso hacia la terminación. Sin progreso, hay ciclo infinito.

### Ejemplo técnico desarrollado
```text
suma = 0
i = 1
MIENTRAS i <= 5 HACER
  suma = suma + i
  i = i + 1
FIN MIENTRAS
ESCRIBIR suma
```
Resultado: 15.

### Práctica guiada
- Convierte el ciclo MIENTRAS anterior a un ciclo PARA.

### Actividad independiente
Escribe un algoritmo que pida números hasta que el usuario ingrese 0 y luego muestre la suma.

### Criterios de aceptación
- Ciclo termina correctamente.
- Tiene inicialización, condición y actualización.
- Produce resultado correcto.

### Errores frecuentes y recomendaciones
- **Error:** ciclo infinito. **Recomendación:** verificar progreso hacia la condición de salida.
- **Error:** off-by-one. **Recomendación:** probar límites.
- **Error:** modificar la variable de control incorrectamente. **Recomendación:** trazar iteraciones.

### Evaluación de comprensión
1. ¿Cuándo usar `for` vs `while`?
2. ¿Qué causa un ciclo infinito?
3. Traza un ciclo que sume 1 a 5.

### Referencias
- Python Docs. *for and while statements*. https://docs.python.org/3/tutorial/controlflow.html. Consultado: 2026-11-24.