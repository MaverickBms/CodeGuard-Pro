# Etapa 4 · Módulo 4.4 — Paradigmas

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 4, Módulo 4.4. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 4.4 — Paradigmas. **Lecciones oficiales:** 5 (4.4.1 a 4.4.5).

## Propósito
Conocer paradigmas de programación y cuándo aplicar cada enfoque.

---

## Lección 4.4.1 — Paradigma imperativo
- **Oficial:** 4.4.1 — Paradigma imperativo. **Sec:** 1/5.
- **Propósito:** comprender programación basada en instrucciones y estado mutable.
- **Resultados:** escribir código imperativo, identificar secuencia/estado/asignación.
- **Desarrollo:** el paradigma imperativo describe cómo hacer algo paso a paso, modificando estado. Es la base de C, Java procedural, etc. Ventaja: control explícito. Riesgo: estado mutable complejo.
```java
int total = 0;
for (int n : nums) { total += n; }
```
- **Práctica:** implementa suma de array en estilo imperativo.
- **Independiente:** compara el mismo problema en imperativo y declarativo.
- **Criterios:** identifica estado y pasos.
- **Errores:** confundir imperativo con “malo”.
- **Eval:** ¿Qué caracteriza al paradigma imperativo?
- **Ref:** Van Roy, P., Haridi, S. *Concepts, Techniques, and Models of Computer Programming*. MIT Press.

## Lección 4.4.2 — Paradigma declarativo
- **Oficial:** 4.4.2 — Paradigma declarativo. **Sec:** 2/5.
- **Propósito:** expresar qué se quiere lograr, no cómo paso a paso.
- **Resultados:** reconocer estilo declarativo (SQL, streams, HTML).
- **Desarrollo:** declarativo describe el resultado deseado. SQL `SELECT * FROM users WHERE active=true` dice qué quiere, no cómo iterar. En Java, Streams permiten estilo más declarativo.
```java
int total = nums.stream().mapToInt(Integer::intValue).sum();
```
- **Práctica:** filtrar lista con streams.
- **Independiente:** escribe la misma consulta en imperativo y declarativo.
- **Criterios:** identifica diferencia de enfoque.
- **Errores:** creer que declarativo no tiene ejecución interna.
- **Eval:** ¿SQL es declarativo o imperativo?
- **Ref:** Oracle. *Streams*. https://docs.oracle.com/javase/tutorial/collections/streams/ (2026-11-24).

## Lección 4.4.3 — Paradigma funcional
- **Oficial:** 4.4.3 — Paradigma funcional. **Sec:** 3/5.
- **Propósito:** usar funciones puras, inmutabilidad y composición.
- **Resultados:** identificar función pura, efectos secundarios, map/filter/reduce.
- **Desarrollo:** funcional enfatiza funciones puras (misma entrada, misma salida, sin efectos secundarios), inmutabilidad y composición. Java soporta elementos funcionales con lambdas y streams, aunque no es puramente funcional.
```java
List<Integer> pares = nums.stream().filter(n -> n % 2 == 0).toList();
```
- **Práctica:** usa map/filter/reduce en una lista.
- **Independiente:** identifica efectos secundarios en una función dada.
- **Criterios:** reconoce pureza e inmutabilidad.
- **Errores:** usar streams con efectos secundarios ocultos.
- **Eval:** ¿Qué es una función pura?
- **Ref:** Oracle. *Lambda Expressions*. https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html (2026-11-24).

## Lección 4.4.4 — Paradigma orientado a objetos
- **Oficial:** 4.4.4 — Paradigma orientado a objetos. **Sec:** 4/5.
- **Propósito:** consolidar el enfoque OO como paradigma.
- **Resultados:** modelar problema con objetos, responsabilidades y colaboración.
- **Desarrollo:** OO organiza el software en objetos que encapsulan estado y comportamiento. Útil para modelar dominios complejos. Riesgos: jerarquías excesivas, sobreabstracción. Java es principalmente OO.
- **Práctica:** modela un pequeño dominio (biblioteca) con 3 clases.
- **Independiente:** compara solución OO vs procedural para el mismo problema.
- **Criterios:** responsabilidades claras, colaboración entre objetos.
- **Errores:** usar clases solo como contenedores de datos sin comportamiento.
- **Eval:** ¿Cuándo OO es una buena opción?
- **Ref:** Gamma et al. *Design Patterns*. Addison-Wesley.

## Lección 4.4.5 — Paradigma basado en eventos
- **Oficial:** 4.4.5 — Paradigma basado en eventos. **Sec:** 5/5.
- **Propósito:** comprender sistemas que reaccionan a eventos.
- **Resultados:** identificar productor, evento, listener/handler.
- **Desarrollo:** en programación basada en eventos, el flujo se dispara por eventos (click, mensaje, señal, timer). Común en UI, Node.js, brokers de mensajes. Requiere gestionar asincronía, errores y orden de eventos.
```java
button.addActionListener(e -> System.out.println("Click"));
```
- **Práctica:** crea un listener simple (o simula con interfaz Java).
- **Independiente:** modela sistema de eventos con productor y 2 suscriptores.
- **Criterios:** identifica emisor/evento/handler.
- **Errores:** acoplar fuertemente productor y consumidor.
- **Eval:** ¿Qué dispara el flujo en este paradigma?
- **Ref:** Fowler, M. *Event-Driven Architecture*. https://martinfowler.com/articles/201701-event-driven.html (2026-11-24).