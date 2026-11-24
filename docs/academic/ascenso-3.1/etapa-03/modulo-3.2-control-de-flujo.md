# Etapa 3 · Módulo 3.2 — Control de flujo

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 3, Módulo 3.2.  
**Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 3.2 — Control de flujo. **Lecciones oficiales:** 9 (3.2.1 a 3.2.9).
- **Prerrequisitos:** Módulo 3.1, lógica booleana (2.2).

## Propósito
Controlar la ejecución de programas mediante condiciones y ciclos.

---

## Lección 3.2.1 — if
- **Lección oficial:** 3.2.1 — if. **Secuencia:** 1/9.
- **Propósito:** ejecutar un bloque solo cuando una condición es verdadera.
- **Prerrequisitos:** operadores lógicos y relacionales.
- **Resultados:** escribir `if`, evaluar condición booleana, evitar errores de llaves.
- **Desarrollo:** `if` evalúa una expresión booleana; si es `true`, ejecuta el bloque. La condición debe ser boolean (Java no acepta enteros como booleanos).
```java
if (edad >= 18) {
    System.out.println("Acceso permitido");
}
```
- **Práctica guiada:** programa que indique si un número es positivo.
- **Actividad independiente:** validar si una contraseña tiene al menos 8 caracteres (longitud).
- **Criterios:** condición correcta, bloque bien delimitado, caso falso considerado.
- **Errores:** usar `=` en vez de `==`; omitir llaves en bloques complejos.
- **Evaluación:** ¿Qué ocurre si la condición es false? ¿Por qué Java exige boolean?
- **Ref:** Oracle Java Tutorials - Control Flow. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html (2026-11-24).

## Lección 3.2.2 — else
- **Lección oficial:** 3.2.2 — else. **Secuencia:** 2/9.
- **Propósito:** definir el camino alternativo cuando el `if` no se cumple.
- **Prerrequisitos:** 3.2.1.
- **Resultados:** usar `if-else`, cubrir dos caminos mutuamente excluyentes.
- **Desarrollo:** `else` ejecuta cuando la condición del `if` es falsa. Útil para decisiones binarias.
```java
if (nota >= 60) {
    System.out.println("Aprobado");
} else {
    System.out.println("Reprobado");
}
```
- **Práctica guiada:** par o impar.
- **Actividad independiente:** verificar si usuario puede votar según edad.
- **Criterios:** ambos caminos cubiertos, salida correcta.
- **Errores:** lógica invertida; duplicar condiciones.
- **Evaluación:** ¿Cuándo prefieres `else` frente a otro `if` separado?
- **Ref:** Oracle Java Tutorials. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html (2026-11-24).

## Lección 3.2.3 — else if
- **Lección oficial:** 3.2.3 — else if. **Secuencia:** 3/9.
- **Propósito:** encadenar múltiples condiciones.
- **Prerrequisitos:** 3.2.2.
- **Resultados:** construir cadenas `if-else if-else`, ordenar condiciones correctamente.
- **Desarrollo:** se evalúan en orden; la primera verdadera ejecuta su bloque. El orden importa cuando las condiciones se solapan.
```java
if (nota >= 90) { System.out.println("Excelente"); }
else if (nota >= 70) { System.out.println("Bueno"); }
else if (nota >= 60) { System.out.println("Suficiente"); }
else { System.out.println("Insuficiente"); }
```
- **Práctica guiada:** clasificador de IMC por rangos.
- **Actividad independiente:** conversor de calificación numérica a letra.
- **Criterios:** orden correcto, sin huecos lógicos, caso final.
- **Errores:** solapamiento; no cubrir default.
- **Evaluación:** ¿Qué pasa si pones `nota >= 60` antes de `nota >= 90`?
- **Ref:** Oracle Java Tutorials. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html (2026-11-24).

## Lección 3.2.4 — switch
- **Lección oficial:** 3.2.4 — switch. **Secuencia:** 4/9.
- **Propósito:** seleccionar entre múltiples casos discretos.
- **Prerrequisitos:** 3.2.3.
- **Resultados:** usar `switch` tradicional y comprender `switch` moderno (Java 14+ switch expressions).
- **Desarrollo:** `switch` es útil cuando se compara una variable contra valores constantes. Requiere `break` en forma tradicional para evitar fall-through (salvo que se desee intencionalmente).
```java
switch (dia) {
    case 1 -> System.out.println("Lunes");
    case 2 -> System.out.println("Martes");
    default -> System.out.println("Otro");
}
```
- **Práctica guiada:** menú de opciones 1-4.
- **Actividad independiente:** convertir número de mes a nombre.
- **Criterios:** casos correctos, default, sin fall-through accidental.
- **Errores:** olvidar `break` en switch clásico; no incluir `default`.
- **Evaluación:** ¿Cuándo prefieres `switch` sobre `if-else if`?
- **Ref:** Oracle. *Switch Expressions*. https://docs.oracle.com/en/java/javase/21/language/switch-expressions.html (2026-11-24).

## Lección 3.2.5 — for
- **Lección oficial:** 3.2.5 — for. **Secuencia:** 5/9.
- **Propósito:** repetir un bloque un número conocido de veces.
- **Prerrequisitos:** 2.3.10, 3.1.13.
- **Resultados:** escribir `for`, controlar inicio/condición/incremento, evitar off-by-one.
- **Desarrollo:** `for (inicialización; condición; actualización)` es ideal para conteos e iteraciones con índice.
```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```
- **Práctica guiada:** tabla de multiplicar de N.
- **Actividad independiente:** sumar números del 1 al 100.
- **Criterios:** termina correctamente, sin off-by-one, variable de control clara.
- **Errores:** bucle infinito por actualización incorrecta; límites incorrectos.
- **Evaluación:** ¿Qué imprime `for (int i=0; i<3; i++)`?
- **Ref:** Oracle. *The for Statement*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html (2026-11-24).

## Lección 3.2.6 — while
- **Lección oficial:** 3.2.6 — while. **Secuencia:** 6/9.
- **Propósito:** repetir mientras una condición sea verdadera.
- **Prerrequisitos:** 3.2.5.
- **Resultados:** usar `while`, asegurar progreso hacia terminación.
- **Desarrollo:** `while` evalúa antes de ejecutar. Útil cuando no se conoce el número exacto de iteraciones.
```java
int intentos = 0;
while (intentos < 3) {
    System.out.println("Intento " + (intentos + 1));
    intentos++;
}
```
- **Práctica guiada:** leer números hasta que el usuario ingrese 0.
- **Actividad independiente:** juego de adivinar número con intentos limitados.
- **Criterios:** condición de salida, progreso, sin bucle infinito.
- **Errores:** no actualizar variable; condición siempre verdadera.
- **Evaluación:** ¿Cuándo prefieres `while` sobre `for`?
- **Ref:** Oracle. *The while Statement*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/while.html (2026-11-24).

## Lección 3.2.7 — do-while
- **Lección oficial:** 3.2.7 — do-while. **Secuencia:** 7/9.
- **Propósito:** ejecutar al menos una vez y luego repetir según condición.
- **Prerrequisitos:** 3.2.6.
- **Resultados:** usar `do-while`, reconocer casos de “al menos una vez”.
- **Desarrollo:** la condición se evalúa al final. Útil para menús o validaciones que deben ejecutarse al menos una vez.
```java
int opcion;
do {
    System.out.println("1. Continuar  2. Salir");
    opcion = leerOpcion();
} while (opcion != 2);
```
- **Práctica guiada:** menú que se repite hasta elegir salir.
- **Actividad independiente:** pedir contraseña hasta que cumpla longitud mínima.
- **Criterios:** ejecuta al menos una vez, termina correctamente.
- **Errores:** usar `while` cuando se necesita al menos una ejecución.
- **Evaluación:** ¿Cuál es la diferencia clave con `while`?
- **Ref:** Oracle Java Tutorials. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/while.html (2026-11-24).

## Lección 3.2.8 — break
- **Lección oficial:** 3.2.8 — break. **Secuencia:** 8/9.
- **Propósito:** salir anticipadamente de un ciclo o switch.
- **Prerrequisitos:** 3.2.4-3.2.7.
- **Resultados:** usar `break` con criterio, evitar abuso.
- **Desarrollo:** `break` termina el ciclo/switch actual. Útil para búsqueda donde ya se encontró el resultado. Su abuso puede hacer el flujo difícil de seguir.
```java
for (int i = 0; i < nums.length; i++) {
    if (nums[i] == objetivo) { System.out.println("Encontrado"); break; }
}
```
- **Práctica guiada:** buscar un número en array y detener al encontrar.
- **Actividad independiente:** validar entrada y salir al recibir valor válido.
- **Criterios:** uso justificado, flujo claro.
- **Errores:** usar `break` para controlar lógica compleja que debería ser una condición.
- **Evaluación:** ¿Cuándo es adecuado usar `break`?
- **Ref:** Oracle. *Branching Statements*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/branch.html (2026-11-24).

## Lección 3.2.9 — continue
- **Lección oficial:** 3.2.9 — continue. **Secuencia:** 9/9.
- **Propósito:** saltar a la siguiente iteración del ciclo.
- **Prerrequisitos:** 3.2.8.
- **Resultados:** usar `continue` correctamente, distinguirlo de `break`.
- **Desarrollo:** `continue` omite el resto del bloque actual y pasa a la siguiente iteración. Útil para ignorar elementos que no cumplen condición.
```java
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) continue;
    System.out.println(i); // impares
}
```
- **Práctica guiada:** imprimir solo números impares de 1 a 20.
- **Actividad independiente:** procesar lista ignorando valores nulos o vacíos.
- **Criterios:** diferencia clara con `break`, resultado correcto.
- **Errores:** confundir `continue` con `break`; crear lógica difícil de leer.
- **Evaluación:** ¿Qué diferencia hay entre `break` y `continue`?
- **Ref:** Oracle. *Branching Statements*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/branch.html (2026-11-24).