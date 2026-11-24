# Etapa 3 · Módulo 3.4 — Manejo de información

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 3, Módulo 3.4. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 3.4 — Manejo de información. **Lecciones oficiales:** 7 (3.4.1 a 3.4.7).
- **Prerrequisitos:** Módulos 3.1-3.3.

## Propósito
Manipular datos comunes en Java: strings, arrays, matrices, enums, E/S, Scanner y formateo.

---

## Lección 3.4.1 — Strings
- **Lección oficial:** 3.4.1 — Strings. **Secuencia:** 1/7.
- **Propósito:** manipular texto de forma segura y eficiente.
- **Prerrequisitos:** 3.1.11.
- **Resultados:** crear Strings, usar métodos comunes, entender inmutabilidad.
- **Desarrollo:** `String` es inmutable en Java. Métodos: `length()`, `charAt()`, `substring()`, `toLowerCase()`, `contains()`, `split()`, `trim()`, `equals()`. Concatenar muchas veces en bucle es ineficiente; usar `StringBuilder`.
```java
String s = "CodeGuard";
System.out.println(s.length()); // 9
System.out.println(s.substring(0,4)); // Code
System.out.println(s.toLowerCase().contains("guard")); // true
```
- **Práctica guiada:** validar si un email contiene `@` y `.`.
- **Actividad independiente:** crear método que cuente vocales en una cadena.
- **Criterios:** usa `equals`, maneja null/empty, resultado correcto.
- **Errores:** comparar con `==`; no considerar null.
- **Evaluación:** ¿Por qué String es inmutable? ¿Cuándo usar StringBuilder?
- **Ref:** Oracle. *Strings*. https://docs.oracle.com/javase/tutorial/java/data/strings.html (2026-11-24).

## Lección 3.4.2 — Arrays
- **Lección oficial:** 3.4.2 — Arrays. **Secuencia:** 2/7.
- **Propósito:** almacenar colecciones de tamaño fijo del mismo tipo.
- **Prerrequisitos:** 3.1.10, 3.2.5.
- **Resultados:** declarar, inicializar, recorrer y acceder arrays.
- **Desarrollo:** array tiene tamaño fijo, índices desde 0. Acceso fuera de rango lanza `ArrayIndexOutOfBoundsException`.
```java
int[] nums = {10, 20, 30};
for (int i = 0; i < nums.length; i++) {
    System.out.println(nums[i]);
}
for (int n : nums) { System.out.println(n); }
```
- **Práctica guiada:** calcular máximo y mínimo de un array.
- **Actividad independiente:** invertir un array sin crear otro.
- **Criterios:** sin acceso fuera de rango, recorrido correcto.
- **Errores:** off-by-one; confundir length con último índice.
- **Evaluación:** ¿Qué pasa si accedes a `nums[nums.length]`?
- **Ref:** Oracle. *Arrays*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html (2026-11-24).

## Lección 3.4.3 — Matrices
- **Lección oficial:** 3.4.3 — Matrices. **Secuencia:** 3/7.
- **Propósito:** representar datos bidimensionales.
- **Prerrequisitos:** 3.4.2.
- **Resultados:** declarar, recorrer y operar matrices.
- **Desarrollo:** matriz en Java es array de arrays. Acceso `m[fila][columna]`. Recorrido con bucles anidados.
```java
int[][] m = {{1,2},{3,4}};
for (int i = 0; i < m.length; i++) {
    for (int j = 0; j < m[i].length; j++) {
        System.out.print(m[i][j] + " ");
    }
}
```
- **Práctica guiada:** sumar todos los elementos de una matriz.
- **Actividad independiente:** imprimir transpuesta de una matriz 3x3.
- **Criterios:** índices correctos, bucles anidados claros.
- **Errores:** confundir filas/columnas; índices invertidos.
- **Evaluación:** ¿Cómo obtienes el número de filas y columnas?
- **Ref:** Oracle Java Tutorials. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html (2026-11-24).

## Lección 3.4.4 — Enums
- **Lección oficial:** 3.4.4 — Enums. **Secuencia:** 4/7.
- **Propósito:** representar conjuntos fijos de constantes con tipo seguro.
- **Prerrequisitos:** 3.1.9, 3.1.10.
- **Resultados:** declarar enum, usar en switch, entender ventajas sobre constantes.
- **Desarrollo:** `enum` define un tipo con valores finitos. Mejora legibilidad y seguridad de tipos frente a usar ints/strings sueltos.
```java
enum Estado { PENDIENTE, ACTIVO, BLOQUEADO }
Estado e = Estado.ACTIVO;
if (e == Estado.ACTIVO) { System.out.println("OK"); }
```
- **Práctica guiada:** enum para días de semana y mostrar si es laboral.
- **Actividad independiente:** enum para niveles de prioridad con un método que retorne tiempo SLA.
- **Criterios:** usa enum en lugar de constantes mágicas, switch completo.
- **Errores:** usar strings para valores fijos; no manejar todos los casos.
- **Evaluación:** ¿Qué ventaja tiene enum sobre `public static final int`?
- **Ref:** Oracle. *Enum Types*. https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html (2026-11-24).

## Lección 3.4.5 — Entrada y salida
- **Lección oficial:** 3.4.5 — Entrada y salida. **Secuencia:** 5/7.
- **Propósito:** leer datos y mostrar resultados en consola.
- **Prerrequisitos:** 3.1.6.
- **Resultados:** usar `System.out`, `System.err`, entender entrada básica.
- **Desarrollo:** `System.out.println/print/printf` para salida. `System.in` es flujo de entrada bruto; normalmente se envuelve con `Scanner` o `BufferedReader`. Separar E/S de lógica facilita pruebas.
- **Práctica guiada:** programa que pida nombre y muestre saludo.
- **Actividad independiente:** crear menú simple con salida formateada.
- **Criterios:** salida clara, entrada leída correctamente.
- **Errores:** mezclar lógica y E/S en un solo bloque grande.
- **Evaluación:** ¿Por qué separar E/S de la lógica?
- **Ref:** Oracle. *I/O Streams*. https://docs.oracle.com/javase/tutorial/essential/io/index.html (2026-11-24).

## Lección 3.4.6 — Scanner
- **Lección oficial:** 3.4.6 — Scanner. **Secuencia:** 6/7.
- **Propósito:** leer entrada de usuario desde consola.
- **Prerrequisitos:** 3.4.5.
- **Resultados:** usar `Scanner` para leer strings, ints, doubles; manejar fin de línea.
- **Desarrollo:** `Scanner` parsea tokens y líneas.
```java
Scanner sc = new Scanner(System.in);
System.out.print("Nombre: ");
String nombre = sc.nextLine();
System.out.print("Edad: ");
int edad = sc.nextInt();
sc.close();
```
Cuidado con mezclar `nextInt()` y `nextLine()`: queda salto de línea pendiente.
- **Práctica guiada:** leer nombre y edad y mostrar mensaje.
- **Actividad independiente:** crear formulario de consola que lea 3 campos y valide vacíos.
- **Criterios:** lee correctamente, maneja el problema nextInt/nextLine.
- **Errores:** no consumir salto de línea; cerrar `System.in` prematuramente en apps complejas.
- **Evaluación:** ¿Qué problema ocurre al mezclar `nextInt()` y `nextLine()`?
- **Ref:** Oracle. *Scanner API*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Scanner.html (2026-11-24).

## Lección 3.4.7 — Formateo de datos
- **Lección oficial:** 3.4.7 — Formateo de datos. **Secuencia:** 7/7.
- **Propósito:** presentar datos con formato legible y consistente.
- **Prerrequisitos:** 3.4.1, 3.4.5.
- **Resultados:** usar `printf`, `String.format`, formatos numéricos y de fecha básicos.
- **Desarrollo:** `System.out.printf("%.2f%n", precio)` formatea decimales. `String.format` devuelve string formateado. Para fechas, usar `java.time` y `DateTimeFormatter`.
```java
double total = 1234.5;
System.out.printf("Total: %.2f%n", total);
String f = String.format("%-10s %5d", "Ana", 30);
```
- **Práctica guiada:** imprimir tabla alineada de productos y precios.
- **Actividad independiente:** formatear reporte con fechas usando `LocalDate` y `DateTimeFormatter`.
- **Criterios:** formato legible, decimales correctos, sin concatenación caótica.
- **Errores:** formatear moneda con float sin cuidado; locale incorrecto.
- **Evaluación:** ¿Qué diferencia hay entre `printf` y `println`?
- **Ref:** Oracle. *Formatting Numeric Print Output*. https://docs.oracle.com/javase/tutorial/java/data/numberformat.html (2026-11-24).