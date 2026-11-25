# Etapa 3 · Módulo 3.1 — Fundamentos

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 3 «Programación desde cero con Java», Módulo 3.1.  
**Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 3 — Programación desde cero con Java.
- **Objetivo oficial de etapa:** aprender la lógica de la programación mediante Java, comprendiendo su sintaxis, estructura, tipos y control de flujo.
- **Módulo:** 3.1 — Fundamentos.
- **Lecciones oficiales:** 13 (3.1.1 a 3.1.13).

## Propósito
Establecer las bases de Java: plataforma, ejecución, sintaxis, variables, tipos, casting y operadores.

---

## Lección 3.1.1 — JDK

### Identificación
- **Lección oficial:** 3.1.1 — JDK. **Secuencia:** 1/13.

### Propósito de aprendizaje
Comprender qué es el JDK y qué herramientas proporciona para desarrollar en Java.

### Conocimientos previos
- Etapa 1: CPU, memoria, archivos.
- Etapa 2: algoritmos básicos.

### Resultados de aprendizaje
- Definir JDK.
- Identificar componentes principales (javac, java, jar, javadoc, etc.).
- Instalar/verificar una versión LTS.
- Compilar y ejecutar un programa simple.

### Desarrollo conceptual
El **JDK (Java Development Kit)** es el kit de desarrollo para Java. Incluye herramientas para compilar, ejecutar, depurar, empaquetar y documentar programas Java. Normalmente incluye un JRE/runtime y el compilador `javac`.

Componentes comunes: `javac` (compilador), `java` (lanzador), `jar` (empaquetado), `javadoc` (documentación), `jshell` (REPL), herramientas de diagnóstico.

Para aprendizaje reproducible, conviene usar una versión LTS soportada (por ejemplo Java 21 LTS, según contexto del proyecto). La versión afecta APIs disponibles.

### Ejemplo técnico desarrollado
```bash
java -version
javac -version
```
```java
// Hola.java
public class Hola {
    public static void main(String[] args) {
        System.out.println("Hola, ASCENSO");
    }
}
```
```bash
javac Hola.java
java Hola
```
**Resultado esperado:** imprime `Hola, ASCENSO`.

### Práctica guiada
- Instala/verifica JDK. Compila y ejecuta `Hola.java`. Registra versión y salida.

### Actividad independiente
Crea un programa que imprima tu nombre, etapa actual y objetivo de estudio.

### Criterios de aceptación
- JDK verificado.
- Programa compila y ejecuta.
- Salida correcta.

### Errores frecuentes y recomendaciones
- **Error:** confundir JDK con IDE. **Recomendación:** el IDE usa el JDK; no lo reemplaza.
- **Error:** versión incompatible. **Recomendación:** usar LTS y documentar versión.

### Evaluación de comprensión
1. ¿Qué incluye el JDK?
2. ¿Qué hace `javac`?
3. ¿Por qué importa la versión?

### Referencias
- Oracle. *JDK Documentation*. https://docs.oracle.com/en/java/javase/. Consultado: 2026-11-24.
- OpenJDK. *JDK Project*. https://openjdk.org/. Consultado: 2026-11-24.

---

## Lección 3.1.2 — JVM

### Identificación
- **Lección oficial:** 3.1.2 — JVM. **Secuencia:** 2/13.

### Propósito de aprendizaje
Comprender el rol de la JVM en la ejecución de Java.

### Conocimientos previos
- Lección 3.1.1.

### Resultados de aprendizaje
- Definir JVM.
- Explicar bytecode y ejecución.
- Comprender “write once, run anywhere” con matices.
- Identificar responsabilidades básicas: carga, verificación, ejecución, GC.

### Desarrollo conceptual
La **JVM (Java Virtual Machine)** es la máquina virtual que ejecuta bytecode Java. El compilador genera archivos `.class` con bytecode; la JVM los carga, verifica y ejecuta, usando interpretación y/o compilación JIT según la implementación.

Esto permite portabilidad: el mismo bytecode puede ejecutarse en distintas plataformas si existe una JVM compatible. El matiz: el comportamiento puede depender de versión, librerías nativas, sistema de archivos, codificación, etc.

Responsabilidades: carga de clases, verificación de bytecode, gestión de memoria, garbage collection, ejecución de hilos, seguridad.

### Ejemplo técnico desarrollado
Tras `javac Hola.java` se genera `Hola.class`. `java Hola` invoca la JVM, que carga la clase y ejecuta `main`.

### Práctica guiada
- Compila una clase y lista el archivo `.class`. Usa `javap -c Hola` para ver bytecode (observación básica).

### Actividad independiente
Explica en un párrafo por qué el bytecode no es lo mismo que código máquina nativo.

### Criterios de aceptación
- Define JVM correctamente.
- Distingue bytecode y código fuente.
- Reconoce matices de portabilidad.

### Errores frecuentes y recomendaciones
- **Error:** creer que Java siempre se interpreta lentamente. **Recomendación:** JVM modernas usan JIT.
- **Error:** asumir portabilidad absoluta sin pruebas. **Recomendación:** probar en entornos objetivo.

### Evaluación de comprensión
1. ¿Qué ejecuta la JVM?
2. ¿Qué es bytecode?
3. ¿Qué matiz tiene “write once, run anywhere”?

### Referencias
- Oracle. *Java Virtual Machine Specification*. https://docs.oracle.com/javase/specs/jvms/se21/html/. Consultado: 2026-11-24.

---

## Lección 3.1.3 — JRE

### Identificación
- **Lección oficial:** 3.1.3 — JRE. **Secuencia:** 3/13.

### Propósito de aprendizaje
Distinguir JRE, JDK y JVM.

### Conocimientos previos
- Lecciones 3.1.1, 3.1.2.

### Resultados de aprendizaje
- Definir JRE.
- Comparar JDK, JRE y JVM.
- Entender por qué en versiones modernas el JRE separado es menos común.

### Desarrollo conceptual
El **JRE (Java Runtime Environment)** es el entorno para ejecutar aplicaciones Java. Tradicionalmente incluía JVM + bibliotecas estándar necesarias para ejecución. El JDK incluye lo necesario para desarrollar y también ejecutar.

En distribuciones modernas de Java, el modelo de distribución cambió: muchas veces se instala JDK o se crea un runtime personalizado con `jlink`. Aun así, conceptualmente JRE significa “runtime para ejecutar”.

### Ejemplo técnico desarrollado
| Componente | Para qué sirve | Incluye |
|---|---|---|
| JVM | Ejecuta bytecode | Motor de ejecución |
| JRE | Ejecutar apps | JVM + librerías runtime |
| JDK | Desarrollar apps | JRE/runtime + herramientas dev |

### Práctica guiada
- Crea la tabla anterior con tus propias palabras y un ejemplo de cuándo usarías cada uno.

### Actividad independiente
Investiga qué distribución de Java tienes instalada y si incluye herramientas de desarrollo.

### Criterios de aceptación
- Diferencia clara JDK/JRE/JVM.
- Ejemplo correcto.

### Errores frecuentes y recomendaciones
- **Error:** usar JRE cuando se necesita compilar. **Recomendación:** instalar JDK para desarrollo.

### Evaluación de comprensión
1. ¿Puedes compilar con solo JRE?
2. ¿Qué relación hay entre JVM y JRE?
3. ¿Qué componente usarías para desarrollar?

### Referencias
- Oracle. *Java Platform Overview*. https://docs.oracle.com/en/java/javase/. Consultado: 2026-11-24.

---

## Lección 3.1.4 — Compilación

### Identificación
- **Lección oficial:** 3.1.4 — Compilación. **Secuencia:** 4/13.

### Propósito de aprendizaje
Comprender el proceso de compilación en Java.

### Conocimientos previos
- Lecciones 3.1.1-3.1.3.

### Resultados de aprendizaje
- Explicar qué hace `javac`.
- Distinguir errores de compilación y de ejecución.
- Compilar clases simples.
- Interpretar mensajes de error básicos.

### Desarrollo conceptual
La **compilación** en Java transforma código fuente `.java` en bytecode `.class`. El compilador verifica sintaxis y reglas del lenguaje a nivel de compilación: tipos, declaraciones, acceso, estructura.

Errores de compilación impiden generar `.class`. Son distintos de errores de ejecución (runtime), que ocurren cuando el programa ya está corriendo.

El compilador también puede emitir warnings. No deben ignorarse sistemáticamente.

### Ejemplo técnico desarrollado
```java
public class Suma {
    public static void main(String[] args) {
        int a = 2;
        int b = 3
        System.out.println(a + b);
    }
}
```
Falta `;` en `int b = 3` -> error de compilación. Se corrige y compila.

### Práctica guiada
- Introduce un error de sintaxis, lee el mensaje, corrígelo y recompila.

### Actividad independiente
Crea 3 ejemplos: uno con error de compilación, uno con error de ejecución, uno correcto. Documenta la diferencia.

### Criterios de aceptación
- Identifica tipo de error.
- Corrige error de compilación.
- Explica diferencia compilación/ejecución.

### Errores frecuentes y recomendaciones
- **Error:** no leer el mensaje del compilador. **Recomendación:** leer línea, tipo y mensaje.
- **Error:** cambiar muchas cosas a la vez. **Recomendación:** corregir incrementalmente.

### Evaluación de comprensión
1. ¿Qué genera `javac`?
2. ¿Un `NullPointerException` es error de compilación?
3. ¿Por qué un programa puede compilar pero fallar al ejecutar?

### Referencias
- Oracle. *javac tool*. https://docs.oracle.com/en/java/javase/21/docs/specs/man/javac.html. Consultado: 2026-11-24.

---

## Lección 3.1.5 — Interpretación

### Identificación
- **Lección oficial:** 3.1.5 — Interpretación. **Secuencia:** 5/13.

### Propósito de aprendizaje
Comprender cómo se ejecuta bytecode en la JVM.

### Conocimientos previos
- Lecciones 3.1.2 y 3.1.4.

### Resultados de aprendizaje
- Explicar interpretación/JIT a nivel básico.
- Describir flujo fuente→bytecode→ejecución.
- Evitar simplificación excesiva “Java es interpretado”.

### Desarrollo conceptual
Java se compila a bytecode y ese bytecode es ejecutado por la JVM. La JVM puede interpretar bytecode y también compilar en caliente a código nativo mediante JIT (Just-In-Time) para mejorar rendimiento.

Por eso, decir solo “Java es interpretado” es incompleto. Es más preciso: código fuente se compila a bytecode; la JVM ejecuta bytecode con técnicas de interpretación y compilación JIT.

### Ejemplo técnico desarrollado
`Hola.java` --javac--> `Hola.class` --java/JVM--> ejecución. Con ejecución prolongada, la JVM puede optimizar métodos calientes.

### Práctica guiada
- Dibuja el flujo de ejecución de Java e indica dónde actúan `javac` y JVM.

### Actividad independiente
Explica a un compañero la diferencia entre compilación a bytecode y compilación a nativo.

### Criterios de aceptación
- Flujo correcto.
- Menciona JIT o matiz de ejecución.
- No usa la simplificación incorrecta.

### Errores frecuentes y recomendaciones
- **Error:** “Java es solo interpretado”. **Recomendación:** explicar bytecode + JVM + JIT.

### Evaluación de comprensión
1. ¿Qué se ejecuta directamente: `.java` o `.class`?
2. ¿Qué es JIT?
3. ¿Dónde interviene la JVM?

### Referencias
- Oracle. *The Java HotSpot Performance Engine Architecture*. https://www.oracle.com/java/technologies/whitepaper.html. Consultado: 2026-11-24.

---

## Lección 3.1.6 — Sintaxis

### Identificación
- **Lección oficial:** 3.1.6 — Sintaxis. **Secuencia:** 6/13.

### Propósito de aprendizaje
Conocer las reglas sintácticas básicas de Java.

### Conocimientos previos
- Lecciones 3.1.1-3.1.5.

### Resultados de aprendizaje
- Identificar estructura básica de una clase Java.
- Usar llaves, punto y coma, identificadores y mayúsculas/minúsculas correctamente.
- Reconocer errores sintácticos comunes.

### Desarrollo conceptual
La **sintaxis** son las reglas de forma del lenguaje: cómo se escriben declaraciones, bloques, clases, métodos y sentencias. Java es sensible a mayúsculas/minúsculas, usa llaves para bloques y punto y coma para terminar muchas sentencias.

Estructura mínima:
```java
public class Main {
    public static void main(String[] args) {
        // código
    }
}
```

Nombres de clase suelen usar PascalCase; variables y métodos, camelCase. Las reglas de estilo no siempre son sintaxis, pero mejoran legibilidad.

### Ejemplo técnico desarrollado
Error: `Public Class main {}` -> fallará por mayúsculas y convenciones/sintaxis. Correcto: `public class Main { ... }`.

### Práctica guiada
- Escribe una clase con `main` que imprima dos líneas. Verifica compilación.

### Actividad independiente
Toma un código con 5 errores sintácticos y corrígelos.

### Criterios de aceptación
- Código compila.
- Usa estructura básica correcta.
- Identifica errores sintácticos.

### Errores frecuentes y recomendaciones
- **Error:** olvidar `;` o `}`. **Recomendación:** indentar y usar IDE/editor con resaltado.
- **Error:** nombre de archivo diferente al de clase pública. **Recomendación:** `Hola.java` para `public class Hola`.

### Evaluación de comprensión
1. ¿Qué es sintaxis?
2. ¿Java distingue mayúsculas/minúsculas?
3. ¿Qué error produce un `;` faltante?

### Referencias
- Oracle. *Java Language Specification*. https://docs.oracle.com/javase/specs/jls/se21/html/index.html. Consultado: 2026-11-24.

---

## Lección 3.1.7 — Semántica

### Identificación
- **Lección oficial:** 3.1.7 — Semántica. **Secuencia:** 7/13.

### Propósito de aprendizaje
Distinguir entre código sintácticamente correcto y código con significado correcto.

### Conocimientos previos
- Lección 3.1.6.

### Resultados de aprendizaje
- Definir semántica.
- Diferenciar sintaxis y semántica.
- Detectar errores lógicos/semánticos simples.
- Probar el comportamiento del programa.

### Desarrollo conceptual
La **semántica** se refiere al significado del código. Un programa puede compilar (sintaxis correcta) pero hacer lo incorrecto (semántica/lógica incorrecta).

Ejemplo: usar `-` en vez de `+` al calcular un total. Compila, pero el resultado es erróneo.

Por eso se necesitan pruebas, revisión y casos de ejemplo. El compilador no puede adivinar tu intención.

### Ejemplo técnico desarrollado
```java
int total = precio - descuento; // intención: sumar impuesto
```
Compila, pero semánticamente incorrecto si la regla de negocio era otra.

### Práctica guiada
- Escribe un programa que calcule promedio de 3 números, introduce un error semántico y detectalo con un caso de prueba.

### Actividad independiente
Crea 3 bugs semánticos y explica cómo los detectarías.

### Criterios de aceptación
- Distingue sintaxis/semántica.
- Identifica bug semántico.
- Propone prueba.

### Errores frecuentes y recomendaciones
- **Error:** “si compila, está bien”. **Recomendación:** probar con casos conocidos.

### Evaluación de comprensión
1. ¿Puede un programa compilar y estar mal?
2. Da un ejemplo de error semántico.
3. ¿Cómo se detectan estos errores?

### Referencias
- Oracle. *Java Tutorials*. https://docs.oracle.com/javase/tutorial/. Consultado: 2026-11-24.

---

## Lección 3.1.8 — Variables

### Identificación
- **Lección oficial:** 3.1.8 — Variables. **Secuencia:** 8/13.

### Propósito de aprendizaje
Declarar y usar variables en Java.

### Conocimientos previos
- Lecciones 3.1.6, 3.1.7, 2.3.6.

### Resultados de aprendizaje
- Declarar variables con tipo.
- Asignar y actualizar valores.
- Usar nombres descriptivos.
- Comprender inicialización.

### Desarrollo conceptual
En Java, una variable tiene tipo, nombre y valor. Java es de tipado estático: el tipo se declara y se verifica en compilación.

```java
int edad = 20;
String nombre = "Ana";
edad = 21;
```

Las variables locales deben inicializarse antes de usarse. El ámbito determina dónde existen.

### Ejemplo técnico desarrollado
```java
public class Perfil {
    public static void main(String[] args) {
        String nombre = "Ana";
        int edad = 20;
        edad = edad + 1;
        System.out.println(nombre + " tiene " + edad);
    }
}
```

### Práctica guiada
- Crea variables para producto: nombre, precio, stock. Imprime un resumen.

### Actividad independiente
Escribe un programa que convierta días a horas usando variables.

### Criterios de aceptación
- Tipos correctos.
- Variables inicializadas.
- Salida correcta.

### Errores frecuentes y recomendaciones
- **Error:** usar variable sin inicializar. **Recomendación:** asignar valor antes de leer.
- **Error:** nombres vagos. **Recomendación:** usar nombres con intención.

### Evaluación de comprensión
1. ¿Qué significa tipado estático?
2. ¿Qué pasa si usas una variable local no inicializada?
3. Da un buen nombre de variable.

### Referencias
- Oracle. *Variables*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html. Consultado: 2026-11-24.

---

## Lección 3.1.9 — Constantes

### Identificación
- **Lección oficial:** 3.1.9 — Constantes. **Secuencia:** 9/13.

### Propósito de aprendizaje
Usar constantes para valores que no deben cambiar.

### Conocimientos previos
- Lección 3.1.8.

### Resultados de aprendizaje
- Declarar constantes con `final`.
- Distinguir variable y constante.
- Usar constantes para mejorar claridad y seguridad.

### Desarrollo conceptual
Una constante es un valor que no cambia tras su asignación. En Java se usa `final`.

```java
final double IVA = 0.19;
```

Convención: constantes se nombran en mayúsculas con guiones bajos: `MAX_INTENTOS`. Usar constantes evita “números mágicos” y facilita mantenimiento.

### Ejemplo técnico desarrollado
```java
final double PI = 3.14159;
double radio = 2.0;
double area = PI * radio * radio;
System.out.println(area);
```
Intentar reasignar `PI` causa error de compilación.

### Práctica guiada
- Define constantes para IVA, descuento máximo e intentos máximos.

### Actividad independiente
Refactoriza un código con números mágicos usando constantes.

### Criterios de aceptación
- Usa `final`.
- Nombres claros.
- Elimina números mágicos.

### Errores frecuentes y recomendaciones
- **Error:** usar constante para valor que debe cambiar. **Recomendación:** evaluar si realmente es constante.
- **Error:** abusar de constantes globales. **Recomendación:** limitar alcance.

### Evaluación de comprensión
1. ¿Qué hace `final`?
2. ¿Por qué evitar números mágicos?
3. ¿Cómo se nombran las constantes?

### Referencias
- Oracle. *Variables*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html. Consultado: 2026-11-24.

---

## Lección 3.1.10 — Tipos primitivos

### Identificación
- **Lección oficial:** 3.1.10 — Tipos primitivos. **Secuencia:** 10/13.

### Propósito de aprendizaje
Conocer los tipos primitivos de Java y cuándo usarlos.

### Conocimientos previos
- Lecciones 3.1.8, 1.2.8, 1.2.9.

### Resultados de aprendizaje
- Identificar los 8 tipos primitivos.
- Elegir el tipo adecuado.
- Comprender rangos y precisión.

### Desarrollo conceptual
Java tiene 8 tipos primitivos: `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`.

| Tipo | Uso típico | Nota |
|---|---|---|
| `int` | enteros comunes | 32 bits |
| `long` | enteros grandes | sufijo `L` |
| `double` | decimales | más usado que float |
| `boolean` | verdadero/falso | lógica |
| `char` | carácter UTF-16 code unit | comillas simples |

No usar `float/double` para dinero exacto. Elegir tipo por rango, precisión y semántica.

### Ejemplo técnico desarrollado
```java
int edad = 25;
long poblacion = 8_000_000_000L;
double precio = 19.99;
boolean activo = true;
char letra = 'A';
```

### Práctica guiada
- Declara variables con los 8 tipos primitivos y muestra sus valores.

### Actividad independiente
Elige el tipo correcto para: edad, precio, activo, inicial, población mundial.

### Criterios de aceptación
- Usa tipos correctos.
- Explica elección.
- Reconoce limitaciones de float/double.

### Errores frecuentes y recomendaciones
- **Error:** usar `double` para dinero. **Recomendación:** usar `BigDecimal` o enteros en centavos.
- **Error:** overflow por tipo pequeño. **Recomendación:** considerar rango.

### Evaluación de comprensión
1. ¿Cuántos primitivos tiene Java?
2. ¿Por qué `long` necesita `L` en literales grandes?
3. ¿Qué tipo usarías para verdadero/falso?

### Referencias
- Oracle. *Primitive Data Types*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html. Consultado: 2026-11-24.

---

## Lección 3.1.11 — Tipos de referencia

### Identificación
- **Lección oficial:** 3.1.11 — Tipos de referencia. **Secuencia:** 11/13.

### Propósito de aprendizaje
Distinguir tipos primitivos y tipos de referencia.

### Conocimientos previos
- Lección 3.1.10.

### Resultados de aprendizaje
- Definir tipo de referencia.
- Entender referencia vs valor.
- Reconocer `null`.
- Usar `String` como ejemplo básico.

### Desarrollo conceptual
Los tipos de referencia almacenan una referencia a un objeto, no el valor primitivo directamente. Ejemplos: `String`, arrays, objetos, colecciones.

Una variable de referencia puede ser `null`, lo que significa que no apunta a ningún objeto. Acceder a un método sobre `null` causa `NullPointerException`.

Comparar referencias con `==` compara identidad/referencia; para contenido en objetos como `String`, usar `equals`.

### Ejemplo técnico desarrollado
```java
String a = new String("hola");
String b = new String("hola");
System.out.println(a == b);      // false (referencias distintas)
System.out.println(a.equals(b)); // true (contenido igual)
```

### Práctica guiada
- Prueba comparación con `==` y `equals` en Strings.

### Actividad independiente
Explica qué es `null` y escribe un caso que produzca `NullPointerException`.

### Criterios de aceptación
- Distingue referencia y valor.
- Usa `equals` correctamente.
- Explica `null`.

### Errores frecuentes y recomendaciones
- **Error:** comparar Strings con `==`. **Recomendación:** usar `equals`.
- **Error:** desreferenciar `null`. **Recomendación:** validar antes de usar.

### Evaluación de comprensión
1. ¿Qué almacena una variable de referencia?
2. ¿Qué significa `null`?
3. ¿Por qué `equals` es importante en Strings?

### Referencias
- Oracle. *Classes and Objects*. https://docs.oracle.com/javase/tutorial/java/javaOO/index.html. Consultado: 2026-11-24.

---

## Lección 3.1.12 — Casting

### Identificación
- **Lección oficial:** 3.1.12 — Casting. **Secuencia:** 12/13.

### Propósito de aprendizaje
Convertir tipos de datos de forma segura y consciente.

### Conocimientos previos
- Lecciones 3.1.10, 3.1.11.

### Resultados de aprendizaje
- Diferenciar widening y narrowing.
- Aplicar casting explícito.
- Reconocer pérdida de datos.
- Evitar conversiones inseguras.

### Desarrollo conceptual
**Widening (implícito):** de tipo más pequeño a más grande compatible (`int` a `double`). Seguro en general.
**Narrowing (explícito):** de tipo más grande a más pequeño (`double` a `int`). Puede perder información.

```java
int i = 10;
double d = i;        // widening
double x = 9.8;
int y = (int) x;     // narrowing, y=9
```

En referencias, casting también existe, pero requiere cuidado con `ClassCastException`.

### Ejemplo técnico desarrollado
```java
double precio = 19.99;
int entero = (int) precio; // 19, pierde decimales
System.out.println(entero);
```

### Práctica guiada
- Prueba conversiones widening y narrowing y documenta resultados.

### Actividad independiente
Escribe un caso donde narrowing cause pérdida de datos y explica cómo prevenirlo.

### Criterios de aceptación
- Distingue widening/narrowing.
- Usa cast explícito correctamente.
- Identifica pérdida de datos.

### Errores frecuentes y recomendaciones
- **Error:** hacer narrowing sin considerar pérdida. **Recomendación:** validar rango/precisión.
- **Error:** asumir que casting redondea. **Recomendación:** en `double` a `int` trunca.

### Evaluación de comprensión
1. ¿Qué es widening?
2. ¿Qué pierde al hacer `(int) 9.8`?
3. ¿Cuándo usarías casting explícito?

### Referencias
- Oracle. *Conversions and Promotions*. https://docs.oracle.com/javase/specs/jls/se21/html/jls-5.html. Consultado: 2026-11-24.

---

## Lección 3.1.13 — Operadores

### Identificación
- **Lección oficial:** 3.1.13 — Operadores. **Secuencia:** 13/13.

### Propósito de aprendizaje
Usar operadores aritméticos, relacionales, lógicos y de asignación en Java.

### Conocimientos previos
- Lecciones 3.1.8-3.1.12, 2.2.

### Resultados de aprendizaje
- Aplicar operadores aritméticos, relacionales y lógicos.
- Usar precedencia y paréntesis.
- Comprender operadores de asignación compuesta.
- Evitar errores de precedencia.

### Desarrollo conceptual
Operadores comunes:
- **Aritméticos:** `+ - * / %`
- **Relacionales:** `== != > < >= <=`
- **Lógicos:** `&& || !`
- **Asignación:** `= += -= *= /=`
- **Incremento/decremento:** `++ --`

La precedencia determina el orden de evaluación. Ante duda, usar paréntesis.

`==` compara primitivos por valor; en referencias compara identidad. `&&` y `||` tienen cortocircuito.

### Ejemplo técnico desarrollado
```java
int a = 10, b = 3;
System.out.println(a / b); // 3 (división entera)
System.out.println(a % b); // 1
boolean ok = (a > b) && (b > 0); // true
a += 2; // 12
```

### Práctica guiada
- Escribe expresiones que usen operadores de cada categoría y predice el resultado antes de ejecutar.

### Actividad independiente
Crea un programa que calcule precio final con descuento e IVA usando operadores y paréntesis claros.

### Criterios de aceptación
- Usa operadores correctamente.
- Explica precedencia.
- Resultado correcto.

### Errores frecuentes y recomendaciones
- **Error:** confundir `=` con `==`. **Recomendación:** asignación vs comparación.
- **Error:** división entera inesperada. **Recomendación:** verificar tipos.
- **Error:** depender de precedencia poco clara. **Recomendación:** usar paréntesis.

### Evaluación de comprensión
1. ¿Cuál es la diferencia entre `=` y `==`?
2. ¿Qué devuelve `7 / 2` en enteros Java?
3. ¿Qué significa cortocircuito en `&&`?

### Referencias
- Oracle. *Operators*. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html. Consultado: 2026-11-24.