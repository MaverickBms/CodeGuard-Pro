# Etapa 4 · Módulo 4.1 — POO

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 4, Módulo 4.1. **Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 4 — Programación Orientada a Objetos y paradigmas.
- **Objetivo oficial:** dominar la programación orientada a objetos y los principales paradigmas.
- **Módulo:** 4.1 — POO. **Lecciones oficiales:** 12 (4.1.1 a 4.1.12).

## Propósito
Comprender clases, objetos, encapsulación, herencia, polimorfismo, abstracción y mecanismos clave de Java OOP.

---

## Lección 4.1.1 — Clases
- **Oficial:** 4.1.1 — Clases. **Sec:** 1/12.
- **Propósito:** modelar tipos con atributos y comportamiento.
- **Prerrequisitos:** Etapa 3.
- **Resultados:** definir clase, campos, métodos, instanciación.
- **Desarrollo:** una clase es un molde/definición. Define estado (campos) y comportamiento (métodos). En Java: `public class Producto { ... }`.
```java
public class Producto {
    String nombre;
    double precio;
    void mostrar() { System.out.println(nombre + ": " + precio); }
}
```
- **Práctica:** crea clase `Libro` con título, autor y `mostrar()`.
- **Independiente:** modela `CuentaBancaria` con saldo y métodos básicos.
- **Criterios:** clase compila, campos/métodos coherentes.
- **Errores:** clase Dios; campos públicos sin control.
- **Eval:** ¿Diferencia entre clase y objeto?
- **Ref:** Oracle. *Classes*. https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html (2026-11-24).

## Lección 4.1.2 — Objetos
- **Oficial:** 4.1.2 — Objetos. **Sec:** 2/12.
- **Propósito:** instanciar y usar objetos.
- **Resultados:** crear objetos con `new`, acceder campos/métodos, entender identidad.
- **Desarrollo:** un objeto es una instancia de una clase. Cada objeto tiene su propio estado. Dos objetos pueden tener mismos valores pero distinta identidad.
```java
Producto p1 = new Producto(); p1.nombre = "Teclado";
Producto p2 = new Producto(); p2.nombre = "Mouse";
```
- **Práctica:** crea 3 objetos Producto y muéstralos.
- **Independiente:** compara identidad (`==`) y contenido (`equals` definido).
- **Criterios:** instanciación correcta, estado independiente.
- **Errores:** confundir clase con objeto.
- **Eval:** ¿Dos objetos con mismos datos son el mismo objeto?
- **Ref:** Oracle. *Objects*. https://docs.oracle.com/javase/tutorial/java/javaOO/objects.html (2026-11-24).

## Lección 4.1.3 — Constructores
- **Oficial:** 4.1.3 — Constructores. **Sec:** 3/12.
- **Propósito:** inicializar objetos correctamente.
- **Resultados:** definir constructor, usar `this`, sobrecargar constructores.
- **Desarrollo:** constructor tiene el nombre de la clase y no retorna tipo. Inicializa estado válido. Si no se define, Java provee uno por defecto.
```java
public class Producto {
    String nombre; double precio;
    public Producto(String nombre, double precio) {
        this.nombre = nombre; this.precio = precio;
    }
}
```
- **Práctica:** añade constructor a Libro.
- **Independiente:** crea constructor con validación (precio no negativo).
- **Criterios:** objeto queda en estado válido.
- **Errores:** dejar objeto en estado inválido; lógica pesada en constructor.
- **Eval:** ¿Qué pasa si no defines constructor?
- **Ref:** Oracle. *Constructors*. https://docs.oracle.com/javase/tutorial/java/javaOO/constructors.html (2026-11-24).

## Lección 4.1.4 — Encapsulación
- **Oficial:** 4.1.4 — Encapsulación. **Sec:** 4/12.
- **Propósito:** proteger el estado interno y exponer comportamiento controlado.
- **Resultados:** usar `private`, getters/setters con criterio, validar invariantes.
- **Desarrollo:** encapsular significa ocultar detalles internos y controlar acceso. No todo campo necesita getter/setter; exponer comportamiento es mejor que exponer datos crudos.
```java
public class Cuenta {
    private double saldo;
    public void depositar(double monto) {
        if (monto <= 0) throw new IllegalArgumentException("Monto inválido");
        saldo += monto;
    }
    public double getSaldo() { return saldo; }
}
```
- **Práctica:** encapsula Producto con validación de precio.
- **Independiente:** diseña clase con invariante (saldo nunca negativo).
- **Criterios:** campos privados, validaciones, invariantes preservadas.
- **Errores:** getters/setters para todo sin lógica; campos públicos.
- **Eval:** ¿Encapsular es solo poner getters/setters?
- **Ref:** Oracle. *Access Control*. https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html (2026-11-24).

## Lección 4.1.5 — Herencia
- **Oficial:** 4.1.5 — Herencia. **Sec:** 5/12.
- **Propósito:** reutilizar y especializar comportamiento mediante jerarquías.
- **Resultados:** usar `extends`, `super`, entender relación "es-un".
- **Desarrollo:** herencia permite que una subclase herede de una superclase. Usar solo cuando hay verdadera relación "es-un". Prefiere composición cuando la relación es débil.
```java
class Animal { void sonido() { System.out.println("..."); } }
class Perro extends Animal { @Override void sonido() { System.out.println("Guau"); } }
```
- **Práctica:** crea `Empleado` y `EmpleadoTemporal` con atributo extra.
- **Independiente:** identifica un caso donde herencia sea mala idea y propón composición.
- **Criterios:** usa extends correctamente, respeta "es-un".
- **Errores:** herencia por reutilización de código sin relación semántica.
- **Eval:** ¿Cuándo preferir composición sobre herencia?
- **Ref:** Oracle. *Inheritance*. https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html (2026-11-24).

## Lección 4.1.6 — Polimorfismo
- **Oficial:** 4.1.6 — Polimorfismo. **Sec:** 6/12.
- **Propósito:** tratar objetos de distintas clases por una interfaz común.
- **Resultados:** usar polimorfismo en tiempo de ejecución, override.
- **Desarrollo:** polimorfismo permite que una referencia de tipo base apunte a objetos de subclases y ejecute el método sobrescrito correspondiente.
```java
Animal a = new Perro();
a.sonido(); // Guau
```
- **Práctica:** lista de `Animal` con distintos tipos y llama `sonido()`.
- **Independiente:** diseña sistema de notificaciones (Email, SMS) con método `enviar()`.
- **Criterios:** usa tipo base, comportamiento dinámico correcto.
- **Errores:** usar instanceof en exceso en vez de polimorfismo.
- **Eval:** ¿Qué método se ejecuta en tiempo de ejecución?
- **Ref:** Oracle. *Polymorphism*. https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html (2026-11-24).

## Lección 4.1.7 — Abstracción
- **Oficial:** 4.1.7 — Abstracción. **Sec:** 7/12.
- **Propósito:** modelar lo esencial ocultando detalles de implementación.
- **Resultados:** usar clases abstractas y métodos abstractos.
- **Desarrollo:** una clase abstracta no se instancia y puede definir métodos abstractos que las subclases deben implementar. Útil cuando hay comportamiento común pero implementación variable.
```java
abstract class Figura {
    abstract double area();
}
class Circulo extends Figura {
    double r; Circulo(double r){this.r=r;}
    double area(){ return Math.PI*r*r; }
}
```
- **Práctica:** crea jerarquía Figura con Circulo y Rectangulo.
- **Independiente:** decide cuándo usar clase abstracta vs interfaz.
- **Criterios:** no instancia abstracta, implementa métodos requeridos.
- **Errores:** usar clase abstracta cuando solo se necesita interfaz.
- **Eval:** ¿Se puede instanciar una clase abstracta?
- **Ref:** Oracle. *Abstract Classes*. https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html (2026-11-24).

## Lección 4.1.8 — Interfaces
- **Oficial:** 4.1.8 — Interfaces. **Sec:** 8/12.
- **Propósito:** definir contratos de comportamiento.
- **Resultados:** declarar e implementar interfaces, entender múltiples interfaces.
- **Desarrollo:** una interfaz define un contrato. Una clase puede implementar múltiples interfaces. Desde Java 8, interfaces pueden tener métodos default/static, pero deben usarse con cuidado.
```java
interface Exportable { String exportar(); }
class Reporte implements Exportable {
    public String exportar() { return "csv..."; }
}
```
- **Práctica:** crea interfaz `Pagable` e impleméntala en dos clases.
- **Independiente:** diseña 2 interfaces y una clase que implemente ambas.
- **Criterios:** contrato claro, implementación correcta.
- **Errores:** interfaces infladas; usar default methods para herencia múltiple compleja.
- **Eval:** ¿Diferencia entre interfaz y clase abstracta?
- **Ref:** Oracle. *Interfaces*. https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html (2026-11-24).

## Lección 4.1.9 — Paquetes
- **Oficial:** 4.1.9 — Paquetes. **Sec:** 9/12.
- **Propósito:** organizar clases y controlar visibilidad.
- **Resultados:** declarar paquetes, importar, entender estructura de directorios.
- **Desarrollo:** paquetes agrupan clases relacionadas y evitan colisiones de nombres. La declaración `package` debe coincidir con la estructura de directorios. `import` permite usar clases de otros paquetes.
```java
package com.codeguard.model;
public class Usuario { }
```
- **Práctica:** organiza clases en `model`, `service`, `app`.
- **Independiente:** refactoriza un proyecto pequeño en paquetes.
- **Criterios:** estructura coherente, imports correctos.
- **Errores:** todo en paquete default; paquetes sin criterio.
- **Eval:** ¿Para qué sirve un paquete?
- **Ref:** Oracle. *Packages*. https://docs.oracle.com/javase/tutorial/java/package/index.html (2026-11-24).

## Lección 4.1.10 — Modificadores de acceso
- **Oficial:** 4.1.10 — Modificadores de acceso. **Sec:** 10/12.
- **Propósito:** controlar visibilidad de clases, campos y métodos.
- **Resultados:** usar `private`, default, `protected`, `public` adecuadamente.
- **Desarrollo:** 
| Modificador | Clase | Paquete | Subclase | Mundo |
|---|---|---|---|---|
| private | sí | no | no | no |
| default | sí | sí | no | no |
| protected | sí | sí | sí | no |
| public | sí | sí | sí | sí |
Principio: menor visibilidad posible.
- **Práctica:** elige modificadores para una clase Cuenta.
- **Independiente:** revisa un código y reduce visibilidad innecesaria.
- **Criterios:** visibilidad mínima, justificación.
- **Errores:** todo public; usar protected sin necesidad.
- **Eval:** ¿Qué modificador usarías para un campo interno?
- **Ref:** Oracle. *Controlling Access*. https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html (2026-11-24).

## Lección 4.1.11 — this y super
- **Oficial:** 4.1.11 — this y super. **Sec:** 11/12.
- **Propósito:** referenciar la instancia actual y la superclase.
- **Resultados:** usar `this` para campos/constructores, `super` para herencia.
- **Desarrollo:** `this` refiere al objeto actual; útil para desambiguar parámetros. `super` accede a constructor/métodos de la superclase.
```java
class Base { Base(int x){} }
class Sub extends Base {
    int x;
    Sub(int x){ super(x); this.x = x; }
}
```
- **Práctica:** usa `this` en constructor y `super` en subclase.
- **Independiente:** explica error de llamar `super()` después de otra instrucción.
- **Criterios:** uso correcto, sin ambigüedad.
- **Errores:** olvidar super() cuando la superclase no tiene constructor sin args.
- **Eval:** ¿Qué hace `this()`?
- **Ref:** Oracle. *Using the this Keyword*. https://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html (2026-11-24).

## Lección 4.1.12 — static
- **Oficial:** 4.1.12 — static. **Sec:** 12/12.
- **Propósito:** definir miembros asociados a la clase, no a la instancia.
- **Resultados:** usar campos/métodos static, entender limitaciones.
- **Desarrollo:** `static` pertenece a la clase. Útil para constantes, utilidades, contadores compartidos. Los métodos static no pueden acceder a miembros de instancia directamente.
```java
class Contador {
    static int total = 0;
    Contador(){ total++; }
}
```
- **Práctica:** contador de instancias con campo static.
- **Actividad independiente:** crea clase utilitaria con métodos static y explica cuándo no usarla.
- **Criterios:** uso apropiado, no abusa de estado global.
- **Errores:** usar static para todo; estado global mutable.
- **Eval:** ¿Puede un método static acceder a `this`?
- **Ref:** Oracle. *Understanding Class Members*. https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html (2026-11-24).