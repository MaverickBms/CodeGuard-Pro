# Etapa 3 · Módulo 3.3 — Métodos

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 3, Módulo 3.3. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 3.3 — Métodos. **Lecciones oficiales:** 7 (3.3.1 a 3.3.7).
- **Prerrequisitos:** Módulos 3.1, 3.2.

## Propósito
Encapsular lógica en métodos reutilizables, con parámetros, retorno, sobrecarga, alcance y recursividad.

---

## Lección 3.3.1 — Declaración
- **Lección oficial:** 3.3.1 — Declaración. **Secuencia:** 1/7.
- **Propósito:** definir métodos con firma clara.
- **Prerrequisitos:** sintaxis Java, variables.
- **Resultados:** declarar método con modificador, tipo de retorno, nombre y cuerpo.
- **Desarrollo:** un método encapsula un comportamiento. Firma: `modificador tipoRetorno nombre(params)`. Convención: camelCase, verbo descriptivo.
```java
public static int sumar(int a, int b) {
    return a + b;
}
```
- **Práctica guiada:** crea método `saludar(String nombre)` que imprima saludo.
- **Actividad independiente:** crea 3 métodos: sumar, restar, multiplicar.
- **Criterios:** firma correcta, nombre descriptivo, compila.
- **Errores:** nombre ambiguo; método que hace demasiadas cosas.
- **Evaluación:** ¿Qué partes tiene la firma de un método?
- **Ref:** Oracle. *Defining Methods*. https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html (2026-11-24).

## Lección 3.3.2 — Parámetros
- **Lección oficial:** 3.3.2 — Parámetros. **Secuencia:** 2/7.
- **Propósito:** recibir datos de entrada en un método.
- **Prerrequisitos:** 3.3.1.
- **Resultados:** definir parámetros con tipo, entender paso por valor en Java.
- **Desarrollo:** parámetros son variables declaradas en la firma. Java pasa por valor: para primitivos copia el valor; para objetos copia la referencia.
```java
static void cambiar(int x) { x = 99; }
int n = 5; cambiar(n); // n sigue siendo 5
```
- **Práctica guiada:** método que reciba precio y descuento y calcule total.
- **Actividad independiente:** demuestra con código que modificar un primitivo en método no afecta al original.
- **Criterios:** parámetros tipados, comportamiento correcto.
- **Errores:** confundir parámetro con variable global; asumir paso por referencia.
- **Evaluación:** ¿Java pasa por valor o por referencia?
- **Ref:** Oracle. *Passing Information to a Method*. https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html (2026-11-24).

## Lección 3.3.3 — Argumentos
- **Lección oficial:** 3.3.3 — Argumentos. **Secuencia:** 3/7.
- **Propósito:** pasar valores reales al invocar métodos.
- **Prerrequisitos:** 3.3.2.
- **Resultados:** distinguir parámetro/argumento, pasar argumentos correctos.
- **Desarrollo:** parámetro es la variable en la declaración; argumento es el valor pasado en la llamada. Deben coincidir en número, tipo y orden (salvo sobrecarga/varargs).
```java
static int doble(int n) { return n * 2; }
int r = doble(7); // 7 es el argumento
```
- **Práctica guiada:** invoca método con diferentes argumentos y observa resultados.
- **Actividad independiente:** crea método con 3 parámetros y llámalo con argumentos válidos e inválidos (analiza error).
- **Criterios:** distinción correcta, llamadas válidas.
- **Errores:** invertir orden de argumentos de mismo tipo.
- **Evaluación:** ¿Cuál es la diferencia entre parámetro y argumento?
- **Ref:** Oracle Java Tutorials. https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html (2026-11-24).

## Lección 3.3.4 — Retorno
- **Lección oficial:** 3.3.4 — Retorno. **Secuencia:** 4/7.
- **Propósito:** devolver resultados desde un método.
- **Prerrequisitos:** 3.3.1-3.3.3.
- **Resultados:** usar `return`, tipos de retorno, `void`.
- **Desarrollo:** `return` termina el método y devuelve un valor compatible con el tipo declarado. `void` indica que no devuelve valor. Todos los caminos en método no-void deben retornar.
```java
static boolean esPar(int n) { return n % 2 == 0; }
static void log(String msg) { System.out.println(msg); }
```
- **Práctica guiada:** método que retorne el mayor de dos números.
- **Actividad independiente:** método que retorne si una cadena es vacía o nula (con cuidado).
- **Criterios:** tipo de retorno correcto, todos los caminos cubiertos.
- **Errores:** olvidar return en algún camino; retornar tipo incompatible.
- **Evaluación:** ¿Qué significa `void`?
- **Ref:** Oracle. *Returning a Value from a Method*. https://docs.oracle.com/javase/tutorial/java/javaOO/returnvalue.html (2026-11-24).

## Lección 3.3.5 — Sobrecarga
- **Lección oficial:** 3.3.5 — Sobrecarga. **Secuencia:** 5/7.
- **Propósito:** definir varios métodos con el mismo nombre y distinta firma.
- **Prerrequisitos:** 3.3.2-3.3.4.
- **Resultados:** aplicar sobrecarga, entender resolución por firma.
- **Desarrollo:** la sobrecarga (overloading) permite mismo nombre con diferente número/tipo/orden de parámetros. El compilador elige según argumentos. No basta con cambiar solo el tipo de retorno.
```java
static int sumar(int a, int b) { return a + b; }
static double sumar(double a, double b) { return a + b; }
```
- **Práctica guiada:** sobrecarga `area` para círculo y rectángulo.
- **Actividad independiente:** crea 3 versiones de `imprimir` para int, String y array.
- **Criterios:** firmas distintas, compilación correcta, uso coherente.
- **Errores:** cambiar solo retorno; crear sobrecargas ambiguas.
- **Evaluación:** ¿Qué hace diferente a dos métodos sobrecargados?
- **Ref:** Oracle Java Tutorials. https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html (2026-11-24).

## Lección 3.3.6 — Scope

### Identificación
- **Lección oficial:** 3.3.6 — Scope. **Secuencia:** 6/7.
- **Propósito:** comprender dónde existe y es accesible una variable.
- **Prerrequisitos:** 3.1.8, 3.3.1.
- **Resultados:** distinguir scope local, de bloque, de parámetro y de clase.
- **Desarrollo:** el **scope** define la visibilidad y vida de una variable. Variables locales existen dentro del método/bloque donde se declaran. Parámetros existen durante la ejecución del método. Shadowing ocurre cuando una variable local oculta otra de ámbito mayor; debe evitarse por claridad.
```java
static void demo() {
    int x = 10; // scope de método
    if (x > 5) {
        int y = 20; // scope de bloque
        System.out.println(x + y);
    }
    // y no existe aquí
}
```
- **Práctica guiada:** experimenta con variable dentro de if y accede fuera (observa error).
- **Actividad independiente:** explica un caso de shadowing y cómo evitarlo.
- **Criterios:** identifica scope correctamente, evita shadowing.
- **Errores:** usar variable fuera de scope; shadowing confuso.
- **Evaluación:** ¿Dónde existe una variable declarada dentro de un `for`?
- **Ref:** Oracle. *Variables*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html (2026-11-24).

## Lección 3.3.7 — Recursividad
- **Lección oficial:** 3.3.7 — Recursividad. **Secuencia:** 7/7.
- **Propósito:** resolver problemas donde un método se llama a sí mismo.
- **Prerrequisitos:** 3.3.1-3.3.6.
- **Resultados:** definir caso base y caso recursivo, trazar recursión simple.
- **Desarrollo:** un método recursivo se llama a sí mismo. Necesita **caso base** (terminación) y **caso recursivo** (se acerca al base). Sin caso base o sin progreso, causa `StackOverflowError`.
```java
static int factorial(int n) {
    if (n <= 1) return 1; // base
    return n * factorial(n - 1); // recursivo
}
```
- **Práctica guiada:** traza factorial(4) paso a paso.
- **Actividad independiente:** implementa Fibonacci recursivo y explica por qué es ineficiente para n grande.
- **Criterios:** caso base correcto, progreso, resultado correcto.
- **Errores:** sin caso base; recursión demasiado profunda.
- **Evaluación:** ¿Qué pasa si falta el caso base?
- **Ref:** Oracle Java Tutorials. https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html (2026-11-24).