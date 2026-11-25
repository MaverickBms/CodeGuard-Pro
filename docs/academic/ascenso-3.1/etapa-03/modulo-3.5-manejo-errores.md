# Etapa 3 · Módulo 3.5 — Manejo de errores

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 3, Módulo 3.5. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 3.5 — Manejo de errores. **Lecciones oficiales:** 6 (3.5.1 a 3.5.6).
- **Prerrequisitos:** Módulos 3.1-3.4.

## Propósito
Manejar errores y excepciones en Java de forma controlada y segura.

---

## Lección 3.5.1 — Excepciones
- **Lección oficial:** 3.5.1 — Excepciones. **Secuencia:** 1/6.
- **Propósito:** comprender qué es una excepción y por qué ocurre.
- **Prerrequisitos:** 3.3, 3.4.
- **Resultados:** definir excepción, distinguir error de excepción, identificar flujo de excepción.
- **Desarrollo:** una excepción es un evento que interrumpe el flujo normal por una condición anómala. Java usa objetos de tipo `Throwable`. `Exception` representa condiciones que el programa puede manejar; `Error` representa problemas graves del entorno (p. ej. OutOfMemoryError), normalmente no manejables.
- **Ejemplo:**
```java
int[] a = {1,2,3};
System.out.println(a[5]); // ArrayIndexOutOfBoundsException
```
- **Práctica guiada:** provoca 3 excepciones comunes y observa mensajes.
- **Actividad independiente:** clasifica 5 fallos como excepción recuperable o error grave.
- **Criterios:** identifica tipo y causa, no confunde error/exception.
- **Errores:** capturar todo sin entender; ignorar excepciones.
- **Evaluación:** ¿Diferencia entre Exception y Error?
- **Ref:** Oracle. *Exceptions*. https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html (2026-11-24).

## Lección 3.5.2 — try/catch/finally
- **Lección oficial:** 3.5.2 — try/catch/finally. **Secuencia:** 2/6.
- **Propósito:** manejar excepciones sin terminar abruptamente el programa.
- **Prerrequisitos:** 3.5.1.
- **Resultados:** usar try/catch/finally, capturar excepciones específicas.
- **Desarrollo:** `try` contiene código riesgoso; `catch` maneja una excepción específica; `finally` se ejecuta siempre (salvo casos extremos de JVM). Capturar primero las más específicas.
```java
try {
    int n = Integer.parseInt("abc");
} catch (NumberFormatException e) {
    System.out.println("Entrada inválida");
} finally {
    System.out.println("Fin");
}
```
- **Práctica guiada:** leer entero del usuario y manejar entrada inválida.
- **Actividad independiente:** envolver división por cero con manejo adecuado.
- **Criterios:** captura específica, finally justificado, mensaje útil.
- **Errores:** `catch (Exception e) {}` vacío; capturar demasiado amplio.
- **Evaluación:** ¿Cuándo se ejecuta finally?
- **Ref:** Oracle. *Catching and Handling Exceptions*. https://docs.oracle.com/javase/tutorial/essential/exceptions/handling.html (2026-11-24).

## Lección 3.5.3 — throw
- **Lección oficial:** 3.5.3 — throw. **Secuencia:** 3/6.
- **Propósito:** lanzar excepciones explícitamente.
- **Prerrequisitos:** 3.5.1, 3.5.2.
- **Resultados:** usar `throw`, elegir tipo de excepción adecuado.
- **Desarrollo:** `throw` lanza una excepción. Se usa para señalar condiciones inválidas. Elegir excepción semántica (`IllegalArgumentException`, `IllegalStateException`, etc.) mejora diagnóstico.
```java
static void setEdad(int edad) {
    if (edad < 0) throw new IllegalArgumentException("Edad inválida");
}
```
- **Práctica guiada:** validar parámetro y lanzar excepción si es inválido.
- **Actividad independiente:** implementar validación de stock no negativo.
- **Criterios:** excepción apropiada, mensaje claro, validación temprana.
- **Errores:** lanzar Exception genérica; mensajes vagos.
- **Evaluación:** ¿Cuándo usar throw?
- **Ref:** Oracle. *How to Throw Exceptions*. https://docs.oracle.com/javase/tutorial/essential/exceptions/throwing.html (2026-11-24).

## Lección 3.5.4 — throws
- **Lección oficial:** 3.5.4 — throws. **Secuencia:** 4/6.
- **Propósito:** declarar que un método puede propagar una excepción.
- **Prerrequisitos:** 3.5.3.
- **Resultados:** usar `throws`, entender propagación.
- **Desarrollo:** `throws` en la firma declara excepciones checked que el método puede lanzar. Obliga al llamador a manejar o declarar. No silencia el error; lo hace explícito.
```java
static void leer() throws IOException {
    Files.readString(Path.of("datos.txt"));
}
```
- **Práctica guiada:** crea método que declare `IOException` y manéjalo desde main.
- **Actividad independiente:** decide si manejar o propagar en 3 escenarios.
- **Criterios:** declaración correcta, decisión de manejo justificada.
- **Errores:** usar throws en todo sin criterio; tragar excepciones.
- **Evaluación:** ¿Qué diferencia hay entre throw y throws?
- **Ref:** Oracle. *Specifying Exceptions*. https://docs.oracle.com/javase/tutorial/essential/exceptions/declaring.html (2026-11-24).

## Lección 3.5.5 — Checked exceptions
- **Lección oficial:** 3.5.5 — Checked exceptions. **Secuencia:** 5/6.
- **Propósito:** comprender excepciones verificadas en compilación.
- **Prerrequisitos:** 3.5.4.
- **Resultados:** identificar checked exceptions, manejarlas o declararlas.
- **Desarrollo:** las checked exceptions (subclases de `Exception`, no `RuntimeException`) deben ser manejadas o declaradas. Representan condiciones recuperables previsibles: IO, SQL, parsing. Fuerzan al desarrollador a decidir.
- **Ejemplo:** `IOException`, `SQLException`, `FileNotFoundException`.
- **Práctica guiada:** lee archivo con `Files.readString` y maneja `IOException`.
- **Actividad independiente:** explica por qué `IOException` es checked.
- **Criterios:** maneja o declara correctamente, no usa catch vacío.
- **Errores:** catch vacío; convertir todo a RuntimeException sin justificación.
- **Evaluación:** ¿Qué obliga el compilador ante una checked exception?
- **Ref:** Oracle. *Checked vs Unchecked Exceptions*. https://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html (2026-11-24).

## Lección 3.5.6 — Unchecked exceptions
- **Lección oficial:** 3.5.6 — Unchecked exceptions. **Secuencia:** 6/6.
- **Propósito:** comprender excepciones no verificadas y prevenirlas.
- **Prerrequisitos:** 3.5.5.
- **Resultados:** identificar unchecked exceptions, prevenir causas comunes.
- **Desarrollo:** unchecked exceptions son `RuntimeException` y sus subclases. No obligan a declarar/manejar. Suelen indicar errores de programación: `NullPointerException`, `IllegalArgumentException`, `IndexOutOfBoundsException`. Se previenen con validación, null checks, límites y pruebas.
- **Ejemplo:**
```java
String s = null;
s.length(); // NullPointerException
```
- **Práctica guiada:** identifica causa de 3 NPE y corrígelas.
- **Actividad independiente:** diseña validaciones para evitar 5 unchecked exceptions comunes.
- **Criterios:** distingue checked/unchecked, propone prevención.
- **Errores:** capturar RuntimeException genérica para ocultar bugs.
- **Evaluación:** ¿Debes capturar siempre NullPointerException? ¿Cuál es mejor enfoque?
- **Ref:** Oracle. *Unchecked Exceptions*. https://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html (2026-11-24).