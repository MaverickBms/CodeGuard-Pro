# Etapa 3 — Programación desde cero con Java

**Estado:** borrador didáctico v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 3.  
**Prioridad:** P1 · Obligatoria.  
**Objetivo oficial:** aprender programación de verdad utilizando Java como primer lenguaje principal.

## Temario oficial

- **3.1 Fundamentos:** JDK, JVM, JRE, compilación, interpretación, sintaxis, semántica, variables, constantes, tipos primitivos, tipos de referencia, casting y operadores.
- **3.2 Control de flujo:** if, else, else if, switch, for, while, do-while, break y continue.
- **3.3 Métodos:** declaración, parámetros, argumentos, retorno, sobrecarga, scope y recursividad.
- **3.4 Manejo de información:** Strings, arrays, matrices, enums, entrada/salida, Scanner y formateo de datos.
- **3.5 Manejo de errores:** excepciones, try/catch/finally, throw, throws, checked exceptions y unchecked exceptions.
- **3.6 Archivos:** lectura, escritura, directorios, paths, archivos de texto y serialización básica.

**Proyecto oficial:** sistema de inventario mediante consola, con registro, consulta, modificación y eliminación de productos.

## Resultados de aprendizaje

Al finalizar podrás escribir programas Java pequeños, compilar y ejecutar código, seleccionar tipos de datos, controlar decisiones y ciclos, organizar lógica en métodos, procesar cadenas y colecciones básicas, validar entradas, manejar excepciones y trabajar con archivos de forma controlada.

## 3.1 — Fundamentos

### JDK, JVM y JRE

- **JVM (Java Virtual Machine):** entorno de ejecución que carga y ejecuta bytecode Java y proporciona servicios como gestión de memoria y recolección de basura.
- **JRE (Java Runtime Environment):** concepto de entorno necesario para ejecutar aplicaciones Java: JVM y bibliotecas/runtime correspondientes. La distribución moderna puede empaquetar estos componentes de otra forma.
- **JDK (Java Development Kit):** herramientas para desarrollar, compilar, depurar y empaquetar aplicaciones Java; incluye el compilador `javac` y herramientas relacionadas.

En distribuciones modernas, no siempre existe una descarga separada denominada JRE. No memorices nombres de paquetes como si fueran universales: revisa la distribución y versión que utilizas.

### Compilación e interpretación

El compilador Java transforma archivos fuente `.java` en bytecode `.class`. La JVM carga y ejecuta ese bytecode; las implementaciones modernas pueden interpretar inicialmente y compilar partes a código máquina mediante JIT.

Flujo habitual:
1. escribir `Hola.java`;
2. compilar con `javac Hola.java`;
3. ejecutar con `java Hola`.

Ejemplo:

```java
public class Hola {
    public static void main(String[] args) {
        System.out.println("Hola, ASCENSO");
    }
}
```

Comandos (requieren JDK instalado y disponible en PATH):

```bash
javac Hola.java
java Hola
```

No se afirma que estos comandos se hayan ejecutado en tu equipo; son el procedimiento esperado para un entorno JDK compatible.

### Sintaxis y semántica

La sintaxis establece cómo se escriben construcciones válidas: llaves, paréntesis, punto y coma, palabras reservadas y reglas gramaticales. La semántica describe qué significa el programa.

Un programa puede tener sintaxis válida y aun así producir un resultado incorrecto por una regla mal formulada. Compilar no demuestra que el algoritmo sea correcto.

### Variables y constantes

Una variable representa un dato asociado a un nombre y un tipo. Una variable local debe inicializarse antes de leerse.

```java
int cantidad = 3;
double precioUnitario = 12500.0;
double subtotal = cantidad * precioUnitario;
final int MAX_INTENTOS = 3;
```

`final` impide reasignar esa variable después de inicializarla. Si contiene una referencia a un objeto, no significa que el objeto sea inmutable.

Usa nombres que describan el propósito y evita abreviaturas opacas.

### Tipos primitivos

Java define ocho tipos primitivos:
- enteros: `byte`, `short`, `int`, `long`;
- punto flotante: `float`, `double`;
- carácter: `char`;
- lógico: `boolean`.

Los rangos y precisiones dependen del tipo. Para cálculos monetarios no uses `float` o `double` sin analizar redondeos; en aplicaciones reales suele ser preferible `BigDecimal` o unidades enteras mínimas, según requisitos.

### Tipos de referencia

Los tipos de referencia identifican objetos, arreglos, interfaces, clases y cadenas. Una variable de referencia puede contener `null`, que indica ausencia de una referencia a objeto.

`String` es una clase y sus instancias son inmutables: operaciones como concatenar producen otra cadena, no modifican la instancia original.

### Casting

El casting convierte o interpreta un valor en otro tipo:
- conversión implícita permitida por las reglas del lenguaje;
- conversión explícita mediante cast, que puede perder información;
- conversión de referencia entre tipos compatibles, sujeta a comprobaciones.

Ejemplo:

```java
int unidades = 7;
double unidadesExactas = unidades; // ampliación
double promedio = 8.9;
int promedioEntero = (int) promedio; // trunca la parte decimal
```

No confundas truncamiento con redondeo. Para redondear usa una operación explícita apropiada.

### Operadores

Categorías principales:
- aritméticos: `+`, `-`, `*`, `/`, `%`;
- comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`;
- lógicos: `&&`, `||`, `!`;
- asignación: `=`, `+=`, `-=`, etc.;
- incremento/decremento: `++`, `--`;
- condicional ternario: `condicion ? a : b`.

Para comparar objetos por contenido, utiliza el método adecuado como `equals`, no asumas que `==` compara el contenido.

## 3.2 — Control de flujo

### if, else y else if

Permiten ejecutar bloques según condiciones booleanas.

```java
if (stock >= cantidadSolicitada && cantidadSolicitada > 0) {
    System.out.println("Venta permitida");
} else if (cantidadSolicitada <= 0) {
    System.out.println("La cantidad debe ser positiva");
} else {
    System.out.println("Stock insuficiente");
}
```

Ordena las condiciones para que cada caso tenga una respuesta inequívoca. Evita condiciones duplicadas o ramas inalcanzables.

### switch

Selecciona una rama entre alternativas. La sintaxis disponible depende de la versión de Java. En la forma tradicional, `break` evita continuar accidentalmente a la siguiente etiqueta; las expresiones `switch` modernas tienen reglas distintas.

```java
switch (opcion) {
    case 1:
        System.out.println("Registrar");
        break;
    case 2:
        System.out.println("Consultar");
        break;
    default:
        System.out.println("Opción no válida");
}
```

### for, while y do-while

- `for`: útil cuando la estructura de repetición tiene inicialización, condición y actualización explícitas.
- `while`: repite mientras una condición sea verdadera; puede ejecutarse cero veces.
- `do-while`: evalúa la condición al final; se ejecuta al menos una vez.

```java
for (int i = 0; i < 3; i++) {
    System.out.println(i);
}

int intentos = 0;
while (intentos < 3) {
    intentos++;
}

int opcion;
do {
    opcion = 0; // sustituir por lectura validada
} while (opcion < 0);
```

En el último ejemplo, la asignación solo ilustra la estructura: una aplicación debe leer y validar una opción real.

### break y continue

- `break` termina el ciclo o estructura `switch` más cercana.
- `continue` salta al siguiente ciclo de iteración.

Úsalos cuando aclaren el flujo; demasiados saltos pueden hacer difícil entender dónde termina cada operación.

## 3.3 — Métodos

Un método agrupa una operación con un nombre, parámetros, cuerpo y, cuando corresponde, tipo de retorno.

```java
static double calcularSubtotal(double precio, int cantidad) {
    if (precio < 0 || cantidad < 0) {
        throw new IllegalArgumentException("Valores negativos");
    }
    return precio * cantidad;
}
```

### Declaración, parámetros y argumentos

La declaración define el método y sus parámetros. Los argumentos son los valores concretos que se pasan al invocarlo.

`calcularSubtotal(12500.0, 3)` pasa dos argumentos. Los parámetros reciben esos valores para ejecutar el cuerpo.

### Retorno

El tipo de retorno indica qué valor entrega el método. `void` indica que no devuelve un valor. Todo camino de un método con retorno debe cumplir las reglas de retorno del lenguaje.

### Sobrecarga

Permite declarar métodos con el mismo nombre y listas de parámetros diferentes (cantidad, tipos u orden). El tipo de retorno por sí solo no distingue una sobrecarga.

### Scope (ámbito)

El ámbito determina dónde puede utilizarse un identificador. Variables locales, parámetros y campos tienen reglas diferentes. Mantén variables en el ámbito más pequeño que permita su uso correcto.

### Recursividad

Un método recursivo se llama a sí mismo directa o indirectamente. Debe tener:
- caso base que detenga la recursión;
- paso recursivo que acerque al caso base.

```java
static int factorial(int n) {
    if (n < 0) {
        throw new IllegalArgumentException("n debe ser >= 0");
    }
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

La recursión no siempre es la mejor opción: puede consumir stack y provocar `StackOverflowError` para entradas grandes.

## 3.4 — Manejo de información

### Strings

`String` representa secuencias de caracteres y es inmutable. Métodos frecuentes: `length()`, `charAt()`, `substring()`, `contains()`, `equals()`, `equalsIgnoreCase()`, `trim()` y `toLowerCase()`.

No compares cadenas con `==` para verificar contenido. Usa `equals` y valida `null` según el contrato del método.

### Arrays

Un array almacena una cantidad fija de elementos del mismo tipo y usa índices desde cero.

```java
int[] cantidades = {2, 4, 6};
System.out.println(cantidades[0]); // 2
```

Acceder fuera de sus límites provoca `ArrayIndexOutOfBoundsException`. La longitud se obtiene con `array.length`.

### Matrices

Una matriz puede representarse como un array de arrays. En Java, las filas pueden tener longitudes diferentes (array irregular).

```java
int[][] ventas = {
    {2, 3},
    {1, 5}
};
```

Antes de recorrerla, comprueba las longitudes pertinentes.

### Enums

Un `enum` define un conjunto fijo de constantes con nombre.

```java
enum EstadoProducto {
    ACTIVO, INACTIVO, AGOTADO
}
```

Es preferible a representar estados cerrados mediante números mágicos o cadenas sin validación.

### Entrada/salida y Scanner

`Scanner` facilita leer tokens y valores desde una fuente como `System.in`. Sus métodos pueden lanzar excepciones de entrada y la mezcla de `nextInt()` con `nextLine()` requiere comprender el salto de línea pendiente.

```java
import java.util.Scanner;

public class LeerCantidad {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Cantidad: ");
            if (scanner.hasNextInt()) {
                int cantidad = scanner.nextInt();
                if (cantidad > 0) {
                    System.out.println("Cantidad válida: " + cantidad);
                } else {
                    System.out.println("Debe ser mayor que cero");
                }
            } else {
                System.out.println("Debe ingresar un entero");
            }
        }
    }
}
```

### Formateo de datos

Utiliza formatos explícitos para mostrar cantidades y decimales. El separador decimal puede depender de la configuración regional; en sistemas que procesan datos, separa el formato de presentación del formato de almacenamiento.

Ejemplo:

```java
System.out.printf("Unidades: %d%n", 3);
System.out.printf(java.util.Locale.US, "Precio: %.2f%n", 12500.0);
```

## 3.5 — Manejo de errores

### Excepciones

Una excepción representa una condición anómala que altera el flujo normal. Debe manejarse en el nivel que pueda tomar una decisión útil, no ocultarse indiscriminadamente.

### try/catch/finally

`try` contiene la operación susceptible de fallar; `catch` maneja tipos de excepción concretos; `finally` ejecuta limpieza en los casos habituales, aunque existen terminaciones abruptas del proceso donde no puede garantizarse.

```java
try {
    int cantidad = Integer.parseInt("12");
    System.out.println(cantidad);
} catch (NumberFormatException ex) {
    System.out.println("La cantidad no es un entero válido");
} finally {
    System.out.println("Fin de la operación");
}
```

### throw y throws

- `throw` lanza una instancia de excepción.
- `throws` declara en la firma las excepciones comprobadas que el método puede propagar.

No declares `throws Exception` indiscriminadamente: especifica el contrato de error más preciso posible.

### Checked y unchecked exceptions

Las checked exceptions deben capturarse o declararse según las reglas del compilador. Las unchecked (subclases de `RuntimeException`) no requieren esa declaración obligatoria. Ambas pueden indicar fallos que necesitan tratamiento.

No utilices excepciones como sustituto de condiciones normales de control ni captures `Exception` para ignorar el problema. Registra contexto útil sin revelar datos sensibles y conserva la causa cuando vuelvas a lanzar una excepción.

## 3.6 — Archivos

### Paths y directorios

Usa `Path` y `Files` de `java.nio.file` para trabajar con rutas y archivos. Evita concatenar separadores manualmente: el sistema operativo puede utilizar convenciones distintas.

### Lectura y escritura de texto

Ejemplo de escritura y lectura UTF-8:

```java
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class ArchivoTexto {
    public static void main(String[] args) throws IOException {
        Path ruta = Path.of("datos", "nota.txt");
        Files.createDirectories(ruta.getParent());
        Files.writeString(ruta, "ASCENSO\n", StandardCharsets.UTF_8);
        String contenido = Files.readString(ruta, StandardCharsets.UTF_8);
        System.out.print(contenido);
    }
}
```

El ejemplo escribe dentro de una carpeta relativa al directorio de trabajo. No lo ejecutes en directorios de producción ni sobre archivos importantes. Comprueba siempre la ruta efectiva y los permisos.

### Serialización básica

La serialización transforma un objeto en una representación que puede almacenarse o transmitirse. La serialización nativa de Java puede implicar riesgos al deserializar datos no confiables y requiere compatibilidad de clases/versiones. No deserialices objetos recibidos de fuentes desconocidas.

Para intercambio de datos, suele ser preferible un formato explícito y validable como JSON, utilizando una biblioteca mantenida y una política de esquema. En este módulo, «serialización básica» significa comprender el propósito y los riesgos; no habilita deserialización insegura.

## Proyecto oficial — Inventario por consola

Construye una aplicación de consola que permita registrar, consultar, modificar y eliminar productos.

### Modelo mínimo

Cada producto debe tener identificador, nombre, precio y cantidad en stock. Define reglas de validación antes de implementar: identificador no vacío y único; nombre no vacío; precio no negativo; cantidad no negativa.

### Requisitos funcionales

1. Registrar un producto.
2. Consultar un producto por identificador.
3. Listar productos.
4. Modificar nombre, precio o stock.
5. Eliminar un producto con confirmación.
6. Guardar y cargar el inventario en un archivo de texto con formato documentado.
7. Informar errores de entrada y operaciones no permitidas.

No añadas autenticación, base de datos o interfaz gráfica en esta etapa: el objetivo es consolidar fundamentos de Java y consola.

### Plan de implementación

- Fase 1: menú y ciclo principal.
- Fase 2: modelo de datos y métodos.
- Fase 3: validación de entradas.
- Fase 4: operaciones CRUD en memoria.
- Fase 5: persistencia de archivo.
- Fase 6: pruebas manuales y documentación.

### Casos de prueba mínimos

| Caso | Entrada/estado | Resultado esperado |
|---|---|---|
| Registro válido | ID nuevo, nombre, precio y stock válidos | Producto guardado |
| ID duplicado | ID ya existente | Rechazo sin sobrescribir |
| Consulta inexistente | ID no registrado | Mensaje claro, sin caída |
| Precio negativo | Precio < 0 | Rechazo |
| Stock negativo | Cantidad < 0 | Rechazo |
| Modificación | ID existente y datos válidos | Solo campos solicitados cambian |
| Eliminación | ID existente y confirmación | Producto eliminado |
| Archivo inexistente | Primera ejecución | Inicio controlado con inventario vacío o aviso documentado |
| Archivo mal formado | Datos inválidos | Error controlado, no pérdida silenciosa |
| Menú inválido | Texto donde se espera número | Solicitar entrada válida sin terminar abruptamente |

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Fundamentos, tipos y operadores | 10 |
| Control de flujo | 15 |
| Métodos y modularidad | 15 |
| Strings, arrays/enums y entrada | 15 |
| Excepciones y validación | 15 |
| Archivos y rutas | 15 |
| Pruebas, documentación y claridad | 15 |

## Errores frecuentes

- usar `==` para comparar contenido de cadenas;
- acceder a un array con un índice fuera de rango;
- no validar entrada del usuario;
- crear ciclos sin condición de salida;
- métodos demasiado largos con múltiples responsabilidades;
- capturar excepciones y no hacer nada;
- confundir compilación exitosa con algoritmo correcto;
- escribir archivos en rutas no controladas;
- asumir que `double` representa exactamente cualquier decimal;
- deserializar datos no confiables.

## Autoevaluación

1. ¿Qué diferencia existe entre JDK, JVM y JRE?
2. ¿Qué produce `javac`?
3. ¿Qué diferencia hay entre tipo primitivo y tipo de referencia?
4. ¿Por qué `==` no es la opción general para comparar el contenido de dos Strings?
5. ¿Cuándo usarías `while` en vez de `for`?
6. ¿Qué es la sobrecarga y qué no puede distinguirla?
7. ¿Qué diferencia hay entre parámetro y argumento?
8. ¿Qué problema resuelve una excepción checked?
9. ¿Qué diferencia existe entre `throw` y `throws`?
10. ¿Por qué hay que validar rutas y evitar deserializar datos desconocidos?

**Respuestas orientativas:** JDK desarrolla, JVM ejecuta bytecode y JRE representa el entorno de ejecución; `javac` genera bytecode; los primitivos almacenan valores y las referencias apuntan a objetos; `==` compara valores primitivos o identidad de referencias; `while` es útil cuando no se conoce de antemano el número de iteraciones; la sobrecarga cambia parámetros, no solo retorno; parámetro aparece en declaración y argumento en llamada; checked obliga a tratar/declarar ciertos fallos; `throw` lanza y `throws` declara propagación; rutas y deserialización pueden introducir pérdida de datos o ejecución/efectos no deseados.

## Recursos audiovisuales

No se incluye video en esta versión: no se ha verificado una serie o pieza en español que cubra con fidelidad todos los subtemas de Java de esta etapa. Se prefiere curar recursos concretos por lección (JDK/JVM, control de flujo, métodos, arrays, excepciones y archivos) en lugar de recomendar un curso extenso sin comprobar idioma hablado, versión de Java y correspondencia de cada capítulo.

## Referencias

- Oracle, **Java Language Specification**: https://docs.oracle.com/javase/specs/
- Oracle, **Java SE Documentation**: https://docs.oracle.com/en/java/
- Dev.java, **Learn Java** (portal oficial de aprendizaje): https://dev.java/learn/
- OpenJDK, **JDK**: https://openjdk.org/
- Java API, **Scanner**: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Scanner.html
- Java API, **Files**: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Files.html
- Java API, **Path**: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html
- OWASP, **Deserialization Cheat Sheet**: https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** los ejemplos son material didáctico no ejecutado en un JDK dentro de esta sesión; deben compilarse y probarse antes de aprobar el módulo.  
**Estado editorial:** borrador.
