# Etapa 4 — Programación Orientada a Objetos y paradigmas

**Estado:** borrador didáctico v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 4.  
**Prioridad:** P1 · Obligatoria.  
**Objetivo oficial:** comprender cómo diseñar programas organizados y mantenibles.

## Temario oficial

- **4.1 POO:** clases, objetos, instancias, atributos, métodos, constructores, encapsulamiento, abstracción, herencia, polimorfismo, interfaces y clases abstractas.
- **4.2 Relaciones:** asociación, agregación, composición, dependencia y delegación.
- **4.3 Conceptos de diseño:** acoplamiento, cohesión, separación de responsabilidades, inyección de dependencias y responsabilidad única.
- **4.4 Paradigmas:** programación imperativa, estructurada, orientada a objetos, funcional y declarativa.
- **4.5 UML:** diagramas de clases, objetos, relaciones, herencia, interfaces y diagramas de secuencia.

**Proyecto oficial:** sistema de biblioteca utilizando POO y diagramas UML.

## Resultados de aprendizaje

Podrás modelar entidades mediante clases y objetos; proteger invariantes con encapsulamiento; usar herencia, composición e interfaces con criterio; explicar las relaciones entre objetos; reconocer problemas de acoplamiento y baja cohesión; comparar paradigmas y representar diseños mediante UML.

## 4.1 — Programación Orientada a Objetos

### Clases, objetos e instancias

Una clase define una estructura y comportamiento común. Un objeto es una entidad creada a partir de una clase; cada objeto tiene identidad y estado propio.

Ejemplo conceptual: `Libro` es una clase; el libro con ISBN concreto y título específico es un objeto/instancia.

No confundas clase con objeto ni instancia con variable. Una variable de referencia puede apuntar a un objeto; varias referencias pueden apuntar al mismo objeto.

### Atributos y métodos

Los atributos representan estado; los métodos representan comportamiento. El diseño debe procurar que los métodos mantengan las reglas de la entidad en lugar de exponer datos sin control.

### Constructores

Un constructor inicializa una instancia y establece su estado inicial válido. Puede haber varios constructores mediante sobrecarga. Si una clase debe impedir estados inválidos, valida los datos al construir y no dependas únicamente de que el llamador «se porte bien».

### Encapsulamiento

Consiste en proteger el estado interno y ofrecer operaciones controladas. No significa simplemente declarar todos los atributos privados y generar getters/setters automáticos.

Ejemplo Java:

```java
public class Libro {
    private final String isbn;
    private String titulo;
    private boolean disponible;

    public Libro(String isbn, String titulo) {
        if (isbn == null || isbn.isBlank()) {
            throw new IllegalArgumentException("ISBN obligatorio");
        }
        if (titulo == null || titulo.isBlank()) {
            throw new IllegalArgumentException("Título obligatorio");
        }
        this.isbn = isbn;
        this.titulo = titulo;
        this.disponible = true;
    }

    public String getIsbn() { return isbn; }
    public String getTitulo() { return titulo; }
    public boolean estaDisponible() { return disponible; }

    public void prestar() {
        if (!disponible) {
            throw new IllegalStateException("El libro ya está prestado");
        }
        disponible = false;
    }

    public void devolver() {
        if (disponible) {
            throw new IllegalStateException("El libro ya estaba disponible");
        }
        disponible = true;
    }
}
```

El ejemplo protege la transición de disponibilidad. En un sistema real se necesitarían reglas adicionales, como identidad de préstamo, fechas y concurrencia.

### Abstracción

La abstracción presenta las operaciones relevantes y oculta detalles que no necesitan conocer los consumidores. Una clase `Catalogo` puede ofrecer `buscarPorIsbn` sin revelar cómo almacena o indexa internamente los libros.

Una abstracción útil tiene un contrato claro. No es una capa creada solo para aumentar el número de archivos.

### Herencia

La herencia permite definir una clase especializada a partir de otra. La subclase hereda miembros permitidos y puede añadir o redefinir comportamiento.

Debe existir una relación «es un» coherente con el comportamiento esperado. Si una subclase no puede respetar el contrato de la clase base, la herencia puede ser una mala elección.

Evita jerarquías profundas creadas para reutilizar unas pocas líneas. La composición suele ofrecer más flexibilidad.

### Polimorfismo

El polimorfismo permite utilizar objetos de distintos tipos mediante un contrato común, ejecutando el comportamiento correspondiente al tipo real.

Ejemplo: una interfaz `Notificable` puede ser implementada por `NotificacionEmail` y `NotificacionConsola`. El consumidor invoca el método del contrato sin depender de la clase concreta.

### Interfaces

Una interfaz define un contrato de operaciones que las clases pueden implementar. Una clase puede implementar varias interfaces. Las interfaces ayudan a separar el «qué» del «cómo».

No conviertas cada clase en una interfaz automáticamente. Introduce contratos cuando haya una frontera real, variantes de implementación o una necesidad clara de desacoplamiento.

### Clases abstractas

Una clase abstracta no se instancia directamente y puede combinar estado, implementación compartida y métodos abstractos. Es útil cuando existe una base común con comportamiento y restricciones compartidas.

**Comparación:** una interfaz expresa un contrato; una clase abstracta puede aportar estado e implementación común. La elección depende de la relación y del diseño.

## 4.2 — Relaciones entre objetos

### Asociación

Una asociación indica que dos clases mantienen una relación estructural o colaboran. Ejemplo: un `Socio` realiza un `Prestamo`.

La asociación puede tener multiplicidad: un socio puede tener cero o muchos préstamos; cada préstamo pertenece a un socio según las reglas del modelo.

### Agregación

La agregación representa una relación todo-parte débil: las partes pueden existir independientemente del contenedor. La semántica exacta debe documentarse; UML usa un rombo blanco para esta relación.

Ejemplo didáctico: una biblioteca puede agrupar colecciones que también pueden gestionarse de forma independiente.

### Composición

La composición representa una relación todo-parte fuerte, donde el ciclo de vida de la parte depende del todo en el modelo. UML la representa con rombo negro.

Ejemplo: un detalle de préstamo podría no tener sentido fuera del préstamo que lo contiene. No fuerces composición si la parte debe persistir o reutilizarse independientemente.

### Dependencia

Una dependencia indica que un elemento utiliza a otro temporalmente o en su implementación. Un método que recibe un servicio como parámetro depende de su contrato.

### Delegación

Delegar significa que un objeto deriva una tarea a otro objeto especializado. Por ejemplo, `ServicioPrestamo` delega el envío de avisos a `Notificador`. Esto evita que una clase acumule responsabilidades ajenas.

## 4.3 — Conceptos de diseño

### Acoplamiento

El acoplamiento mide cuánto depende un módulo de otros. Un acoplamiento alto hace que los cambios se propaguen y dificulta pruebas y mantenimiento.

Reducir acoplamiento no significa eliminar todas las dependencias: significa controlar cuáles existen y depender de contratos estables cuando sea útil.

### Cohesión

La cohesión describe qué tan relacionadas están las responsabilidades dentro de un módulo. Una clase con una finalidad clara suele ser más fácil de comprender y probar que otra que mezcla persistencia, reglas de negocio, interfaz y notificaciones.

### Separación de responsabilidades

Divide el sistema según motivos de cambio y responsabilidades. En un sistema de biblioteca, por ejemplo:
- entidades y reglas del dominio;
- casos de uso/servicios de aplicación;
- persistencia;
- interfaz de usuario.

No es obligatorio crear una arquitectura compleja para un ejercicio pequeño. La separación debe resolver un problema real de comprensión o cambio.

### Inyección de dependencias

Consiste en proporcionar a un objeto las dependencias que necesita, en lugar de crearlas rígidamente dentro de él.

```java
interface RepositorioLibros {
    Libro buscarPorIsbn(String isbn);
}

class ServicioCatalogo {
    private final RepositorioLibros repositorio;

    ServicioCatalogo(RepositorioLibros repositorio) {
        this.repositorio = repositorio;
    }

    Libro consultar(String isbn) {
        return repositorio.buscarPorIsbn(isbn);
    }
}
```

El servicio depende del contrato, no de una implementación concreta. En pruebas puede inyectarse una implementación en memoria. La inyección no requiere necesariamente un framework.

### Responsabilidad única

El principio de responsabilidad única recomienda que un módulo tenga una razón principal de cambio. No significa que una clase solo pueda tener un método.

Si una clase calcula multas, imprime recibos, accede a archivos y envía correos, tiene motivos de cambio diferentes. Separar responsabilidades puede hacerla más cohesionada y comprobable.

## 4.4 — Paradigmas

Un paradigma es una forma de organizar y expresar soluciones. Los lenguajes modernos suelen combinar varios paradigmas.

### Programación imperativa

Describe pasos y cambios de estado: asignar valores, ejecutar instrucciones y controlar el flujo.

### Programación estructurada

Organiza el flujo con secuencias, decisiones y ciclos, evitando saltos arbitrarios. Facilita seguir el algoritmo.

### Programación orientada a objetos

Organiza el programa alrededor de objetos que encapsulan estado y comportamiento, colaborando mediante contratos.

### Programación funcional

Da protagonismo a funciones, composición, expresiones y, cuando es posible, datos inmutables y ausencia de efectos secundarios. Java incluye expresiones lambda y APIs funcionales, aunque no es un lenguaje puramente funcional.

### Programación declarativa

Describe qué resultado o propiedad se desea, dejando que el sistema determine cómo obtenerlo. Las consultas SQL son un ejemplo conocido: se declara qué datos se quieren recuperar sin especificar cada paso físico de ejecución.

**Comparación aplicada:** calcular el total de un préstamo puede expresarse imperativamente mediante pasos, encapsularse en un método de dominio, componerse con funciones o consultarse mediante una expresión declarativa según el problema.

No existe un paradigma universalmente superior. Elige el estilo que facilite expresar y mantener la solución.

## 4.5 — UML

UML (Unified Modeling Language) es un lenguaje de modelado visual estandarizado. No es un lenguaje de programación ni exige generar código automáticamente.

### Diagrama de clases

Representa clases, atributos, operaciones y relaciones. Elementos comunes:
- nombre de clase;
- atributos;
- operaciones;
- visibilidad (+ pública, − privada, # protegida);
- multiplicidades (1, 0..1, *, 1..*);
- asociación, agregación, composición, herencia y dependencia.

Ejemplo textual de un modelo:
- `Socio` 1 — 0..* `Prestamo`;
- `Prestamo` 1 — 1..* `DetallePrestamo`;
- `DetallePrestamo` * — 1 `Libro`.

Estas multiplicidades son decisiones del ejercicio, no reglas universales de bibliotecas.

### Diagrama de objetos

Muestra instancias concretas y enlaces en un momento determinado. Ayuda a explicar cómo se materializa el modelo de clases con datos específicos.

### Herencia e interfaces en UML

La generalización suele representarse con una línea y triángulo hueco hacia la clase base. La realización de una interfaz usa una notación de línea discontinua con triángulo hueco. Mantén la notación consistente y acompaña el diagrama con leyenda si es necesario.

### Diagrama de secuencia

Representa interacciones ordenadas en el tiempo:
- participantes/líneas de vida;
- mensajes;
- activaciones;
- respuestas;
- fragmentos combinados como alt/opt/loop.

Ejemplo de préstamo:
1. usuario solicita préstamo;
2. interfaz envía petición al servicio;
3. servicio consulta disponibilidad del libro;
4. servicio valida reglas del socio;
5. repositorio registra préstamo;
6. servicio devuelve resultado;
7. interfaz muestra confirmación.

El diagrama debe mostrar el orden y las alternativas importantes, no todos los detalles internos de cada método.

## Proyecto oficial — Sistema de biblioteca con POO y UML

Construye el diseño y una primera implementación Java de una biblioteca pequeña.

### Alcance mínimo

- registrar libros;
- registrar socios;
- consultar catálogo;
- prestar libro disponible;
- devolver libro prestado;
- consultar préstamos activos.

### Modelo de dominio inicial

Clases candidatas: `Libro`, `Socio`, `Prestamo`, `Catalogo` y `ServicioPrestamo`. Una interfaz `RepositorioLibros` puede separar la lógica del mecanismo de almacenamiento. Ajusta el modelo con base en responsabilidades y reglas, no añadas clases sin necesidad.

### Reglas de negocio que deben documentarse

- ISBN/identificador único;
- no prestar un libro que ya está prestado;
- no devolver un préstamo inexistente o ya cerrado;
- un préstamo corresponde a un socio y uno o más libros, según alcance;
- fechas y estados deben ser coherentes;
- toda operación inválida devuelve un error comprensible.

Si no se define una política de multas, reservas o límite de préstamos, no la inventes como requisito: regístrala como fuera de alcance.

### Entregables

1. análisis de requisitos y reglas;
2. diagrama de clases UML;
3. diagrama de objetos para un caso;
4. diagramas de secuencia para prestar y devolver;
5. implementación Java;
6. pruebas de los invariantes del dominio;
7. justificación de herencia/composición/interfaces utilizadas;
8. reflexión sobre acoplamiento y cohesión.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Modelo de clases y encapsulamiento | 20 |
| Relaciones entre objetos | 15 |
| Uso razonado de herencia/interfaces | 15 |
| Cohesión, acoplamiento y responsabilidades | 15 |
| Comprensión de paradigmas | 10 |
| UML de clases, objetos y secuencia | 15 |
| Pruebas y reglas de negocio | 10 |

## Errores frecuentes

- usar herencia solo para reutilizar código;
- exponer todos los atributos mediante setters sin proteger invariantes;
- confundir asociación, agregación y composición;
- crear interfaces sin necesidad;
- hacer que una clase coordine todas las tareas;
- diagramas UML que no coinciden con el código;
- confundir UML con un lenguaje de programación;
- afirmar que la inyección de dependencias requiere un framework;
- aplicar patrones por moda en lugar de resolver un problema.

## Autoevaluación

1. ¿Qué diferencia hay entre clase y objeto?
2. ¿Qué protege el encapsulamiento?
3. ¿Cuándo es inadecuada la herencia?
4. ¿Qué diferencia hay entre interfaz y clase abstracta?
5. ¿Cómo distingues asociación, agregación y composición?
6. ¿Qué significa alta cohesión y bajo acoplamiento?
7. ¿Qué ventaja ofrece inyectar una dependencia?
8. ¿Qué información comunica un diagrama de secuencia?
9. ¿Por qué UML no es código ejecutable?
10. ¿Cómo pueden convivir paradigmas en un mismo programa?

**Respuestas orientativas:** la clase define y el objeto instancia; encapsulamiento protege estado e invariantes; herencia es inadecuada cuando la subclase no respeta el contrato; la interfaz define contrato y la clase abstracta puede compartir estado/implementación; las relaciones difieren en dependencia y ciclo de vida; cohesión agrupa responsabilidades relacionadas y acoplamiento controla dependencias; inyección facilita sustituir implementaciones y probar; secuencia muestra mensajes en el tiempo; UML modela, no ejecuta; Java combina imperativo, objetos y características funcionales.

## Recursos audiovisuales

No se incluye video en esta versión. Para aprobar un recurso de POO/UML debe comprobarse audio hablado en español y relación directa con el concepto (por ejemplo, composición vs. herencia o diagramas de secuencia). No se añadirá un curso general sin validar sus lecciones y su versión.

## Referencias

- Oracle, **Java Language Specification**: https://docs.oracle.com/javase/specs/
- Oracle, **Object-Oriented Programming Concepts**: https://docs.oracle.com/javase/tutorial/java/concepts/
- Object Management Group, **UML Specification**: https://www.omg.org/spec/UML/
- Martin Fowler, **UML Distilled** (referencia bibliográfica; no se reproduce contenido protegido).
- Robert C. Martin, **The Single Responsibility Principle** (artículo del autor): https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** ejemplos de código y proyecto propuestos; no ejecutados ni compilados en esta sesión.  
**Estado editorial:** borrador.
