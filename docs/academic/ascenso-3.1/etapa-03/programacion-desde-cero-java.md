# Etapa 3 — Programación desde cero con Java

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
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

### 3.1.1 — JDK

El **JDK (Java Development Kit)** proporciona las herramientas para desarrollar, compilar, depurar y empaquetar aplicaciones Java. Incluye el compilador `javac` y herramientas relacionadas.

### 3.1.2 — JVM

La **JVM (Java Virtual Machine)** carga y ejecuta bytecode Java y proporciona servicios como gestión de memoria y recolección de basura.

### 3.1.3 — JRE

El **JRE (Java Runtime Environment)** representa el entorno necesario para ejecutar aplicaciones Java: JVM y bibliotecas/runtime correspondientes. Las distribuciones modernas pueden empaquetar estos componentes de otra forma, y no siempre existe una descarga separada denominada JRE.

No memorices nombres de paquetes como si fueran universales: revisa la distribución y versión que utilizas.

### 3.1.4 — Compilación

El compilador Java transforma archivos fuente `.java` en bytecode `.class`.

Flujo habitual:
1. escribir `Hola.java`;
2. compilar con `javac Hola.java`.

Ejemplo:

```java
public class Hola {
    public static void main(String[] args) {
        System.out.println("Hola, ASCENSO");
    }
}
```

Comando (requiere JDK instalado y disponible en PATH):

```bash
javac Hola.java
```

### 3.1.5 — Interpretación y ejecución

La JVM carga y ejecuta el bytecode. Las implementaciones modernas pueden interpretar inicialmente y compilar partes a código máquina mediante JIT.

Después de compilar, ejecuta la clase con:

```bash
java Hola
```

No se afirma que estos comandos se hayan ejecutado en tu equipo; son el procedimiento esperado para un entorno JDK compatible.

### 3.1.6 — Sintaxis

La sintaxis establece cómo se escriben construcciones válidas: llaves, paréntesis, punto y coma, palabras reservadas y reglas gramaticales.

### 3.1.7 — Semántica

La semántica describe qué significa el programa. Un programa puede tener sintaxis válida y aun así producir un resultado incorrecto por una regla mal formulada. Compilar no demuestra que el algoritmo sea correcto.

### 3.1.8 — Variables

Una variable representa un dato asociado a un nombre y un tipo. Una variable local debe inicializarse antes de leerse.

```java
int cantidad = 3;
double precioUnitario = 12500.0;
double subtotal = cantidad * precioUnitario;
```

Usa nombres que describan el propósito y evita abreviaturas opacas.

### 3.1.9 — Constantes

Una constante expresa un valor que no debe reasignarse después de inicializarse. En Java se declara habitualmente con `final`.

```java
final int MAX_INTENTOS = 3;
```

Si una constante contiene una referencia a un objeto, `final` impide reasignar la referencia, pero no vuelve inmutable al objeto.

### 3.1.10 — Tipos primitivos

Java define ocho tipos primitivos:
- enteros: `byte`, `short`, `int`, `long`;
- punto flotante: `float`, `double`;
- carácter: `char`;
- lógico: `boolean`.

Los rangos y precisiones dependen del tipo. Para cálculos monetarios no uses `float` o `double` sin analizar redondeos; en aplicaciones reales suele ser preferible `BigDecimal` o unidades enteras mínimas, según requisitos.

### 3.1.11 — Tipos de referencia

Los tipos de referencia identifican objetos, arreglos, interfaces, clases y cadenas. Una variable de referencia puede contener `null`, que indica ausencia de una referencia a objeto.

`String` es una clase y sus instancias son inmutables: operaciones como concatenar producen otra cadena, no modifican la instancia original.

### 3.1.12 — Casting

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

### 3.1.13 — Operadores

Categorías principales:
- aritméticos: `+`, `-`, `*`, `/`, `%`;
- comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`;
- lógicos: `&&`, `||`, `!`;
- asignación: `=`, `+=`, `-=`, etc.;
- incremento/decremento: `++`, `--`;
- condicional ternario: `condicion ? a : b`.

Para comparar objetos por contenido, utiliza el método adecuado como `equals`, no asumas que `==` compara el contenido.

## 3.2 — Control de flujo

### 3.2.1 — if

`if` ejecuta un bloque cuando una condición booleana es verdadera.

```java
if (stock >= cantidadSolicitada && cantidadSolicitada > 0) {
    System.out.println("Venta permitida");
}
```

### 3.2.2 — else

`else` define la alternativa cuando la condición anterior es falsa. No lleva una condición propia.

### 3.2.3 — else if

`else if` permite evaluar condiciones adicionales en orden. La primera rama verdadera se ejecuta y las siguientes se omiten.

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

### 3.2.4 — switch

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

### 3.2.5 — for

`for` es útil cuando la estructura de repetición tiene inicialización, condición y actualización explícitas.

```java
for (int i = 0; i < 3; i++) {
    System.out.println(i);
}
```

### 3.2.6 — while

`while` repite mientras una condición sea verdadera y puede ejecutarse cero veces.

```java
int intentos = 0;
while (intentos < 3) {
    intentos++;
}
```

### 3.2.7 — do-while

`do-while` evalúa la condición al final y se ejecuta al menos una vez.

```java
int opcion;
do {
    opcion = 0; // sustituir por lectura validada
} while (opcion < 0);
```

En el último ejemplo, la asignación solo ilustra la estructura: una aplicación debe leer y validar una opción real.

### 3.2.8 — break

`break` termina el ciclo o estructura `switch` más cercana.

### 3.2.9 — continue

`continue` salta al siguiente ciclo de iteración.

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

### 3.3.1 — Declaración

La declaración define el método mediante modificadores, tipo de retorno, nombre, parámetros y cuerpo.

### 3.3.2 — Parámetros

Los parámetros son las variables declaradas en la firma del método y reciben los valores de una llamada.

### 3.3.3 — Argumentos

Los argumentos son los valores concretos que se pasan al invocar un método. `calcularSubtotal(12500.0, 3)` pasa dos argumentos a los parámetros correspondientes.

### 3.3.4 — Retorno

El tipo de retorno indica qué valor entrega el método. `void` indica que no devuelve un valor. Todo camino de un método con retorno debe cumplir las reglas de retorno del lenguaje.

### 3.3.5 — Sobrecarga

Permite declarar métodos con el mismo nombre y listas de parámetros diferentes (cantidad, tipos u orden). El tipo de retorno por sí solo no distingue una sobrecarga.

### 3.3.6 — Scope (ámbito)

El ámbito determina dónde puede utilizarse un identificador. Variables locales, parámetros y campos tienen reglas diferentes. Mantén variables en el ámbito más pequeño que permita su uso correcto.

### 3.3.7 — Recursividad

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

### 3.4.1 — Strings

`String` representa secuencias de caracteres y es inmutable. Métodos frecuentes: `length()`, `charAt()`, `substring()`, `contains()`, `equals()`, `equalsIgnoreCase()`, `trim()` y `toLowerCase()`.

No compares cadenas con `==` para verificar contenido. Usa `equals` y valida `null` según el contrato del método.

### 3.4.2 — Arrays

Un array almacena una cantidad fija de elementos del mismo tipo y usa índices desde cero.

```java
int[] cantidades = {2, 4, 6};
System.out.println(cantidades[0]); // 2
```

Acceder fuera de sus límites provoca `ArrayIndexOutOfBoundsException`. La longitud se obtiene con `array.length`.

### 3.4.3 — Matrices

Una matriz puede representarse como un array de arrays. En Java, las filas pueden tener longitudes diferentes (array irregular).

```java
int[][] ventas = {
    {2, 3},
    {1, 5}
};
```

Antes de recorrerla, comprueba las longitudes pertinentes.

### 3.4.4 — Enums

Un `enum` define un conjunto fijo de constantes con nombre.

```java
enum EstadoProducto {
    ACTIVO, INACTIVO, AGOTADO
}
```

Es preferible a representar estados cerrados mediante números mágicos o cadenas sin validación.

### 3.4.5 — Entrada y salida

La entrada permite recibir datos desde el usuario u otra fuente; la salida presenta resultados mediante consola u otros destinos. En una aplicación de consola básica, `System.in` representa la entrada estándar y `System.out` la salida estándar.

### 3.4.6 — Scanner

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

### 3.4.7 — Formateo de datos

Utiliza formatos explícitos para mostrar cantidades y decimales. El separador decimal puede depender de la configuración regional; en sistemas que procesan datos, separa el formato de presentación del formato de almacenamiento.

Ejemplo:

```java
System.out.printf("Unidades: %d%n", 3);
System.out.printf(java.util.Locale.US, "Precio: %.2f%n", 12500.0);
```

## 3.5 — Manejo de errores

### 3.5.1 — Excepciones

Una excepción representa una condición anómala que altera el flujo normal. Debe manejarse en el nivel que pueda tomar una decisión útil, no ocultarse indiscriminadamente.

### 3.5.2 — try/catch/finally

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

### 3.5.3 — throw

`throw` lanza una instancia de excepción.

### 3.5.4 — throws

`throws` declara en la firma las excepciones comprobadas que el método puede propagar.

No declares `throws Exception` indiscriminadamente: especifica el contrato de error más preciso posible.

### 3.5.5 — Checked exceptions

Las checked exceptions deben capturarse o declararse según las reglas del compilador.

### 3.5.6 — Unchecked exceptions

Las unchecked (subclases de `RuntimeException`) no requieren esa declaración obligatoria. Ambas categorías pueden indicar fallos que necesitan tratamiento.

No utilices excepciones como sustituto de condiciones normales de control ni captures `Exception` para ignorar el problema. Registra contexto útil sin revelar datos sensibles y conserva la causa cuando vuelvas a lanzar una excepción.

## 3.6 — Archivos

### 3.6.1 — Lectura

La lectura obtiene contenido desde un archivo. Define codificación, tamaño esperado, tratamiento de archivo inexistente y manejo de errores.

### 3.6.2 — Escritura

La escritura crea o modifica contenido. Define si se reemplaza o añade información, verifica la ruta efectiva y evita sobrescribir archivos importantes sin confirmación.

### 3.6.3 — Directorios

Los directorios organizan archivos y pueden crearse o consultarse mediante las APIs del sistema de archivos. Verifica permisos y rutas antes de modificar contenido.

### 3.6.4 — Paths

Usa `Path` y `Files` de `java.nio.file` para trabajar con rutas y archivos. Evita concatenar separadores manualmente: el sistema operativo puede utilizar convenciones distintas.

### 3.6.5 — Archivos de texto

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

El ejemplo escribe dentro de una carpeta relativa al directorio de trabajo. No lo ejecutes en directorios de producción ni sobre archivos importantes. Comprueba siempre la ruta y los permisos.

### 3.6.6 — Serialización básica

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
**Estado editorial:** en desarrollo; no aprobado ni publicado.


## Línea base de entorno y compatibilidad

Para que los ejemplos sean reproducibles, esta guía toma **JDK 21** como línea base de referencia (versión LTS). Los ejemplos que usan `Path.of`, `Files.readString` y `Files.writeString` requieren Java 11 o posterior; por tanto, son compatibles con JDK 21. Las formas modernas de `switch` no se presentan como requisito en esta etapa: cuando se use sintaxis tradicional, se indicará explícitamente. Antes de ejecutar el proyecto, registra la salida de `java -version` y `javac -version`; si el entorno difiere, documenta la diferencia en lugar de asumir compatibilidad.


## Registro de revisión editorial interna — 2026-11-24

**Alcance:** revisión documental de alineación con el módulo 3.1 del roadmap, cobertura de los títulos oficiales, secuencia didáctica, consistencia terminológica, ejemplos, actividad práctica, evaluación, seguridad y referencias.

**Resultado:** revisión interna realizada; no equivale a aprobación académica externa ni a validación práctica. Se identificaron los ajustes anotados en este registro y se mantienen explícitas las actividades pendientes. Los laboratorios y ejemplos no se declaran ejecutados. Antes de cambiar el estado editorial se requiere cotejo bibliográfico final, ejecución reproducible de actividades y revisión por un segundo evaluador.

**Hallazgos y pendientes específicos:** Se revisaron los 48 temas oficiales, ejemplos Java, proyecto CRUD, casos de prueba, manejo de errores y archivos. Se explicitará una línea base JDK para que APIs y sintaxis sean reproducibles. Pendiente: compilar y ejecutar ejemplos y proyecto con la versión declarada, ejecutar pruebas y revisar dependencias.
