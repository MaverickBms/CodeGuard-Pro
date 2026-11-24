# Etapa 2 — Pensamiento computacional, lógica y matemáticas

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 2.  
**Prioridad:** P1 · Obligatoria.  
**Objetivo oficial:** desarrollar la capacidad de solucionar problemas antes de escribir código.

## Temario oficial

- **2.1 Pensamiento computacional:** descomposición, abstracción, reconocimiento de patrones, generalización, modelado de problemas y casos límite.
- **2.2 Lógica:** proposiciones, operadores AND/OR/NOT, tablas de verdad, implicaciones, equivalencias, álgebra booleana y predicados.
- **2.3 Algoritmos iniciales:** entrada, procesamiento, salida, pseudocódigo, diagramas de flujo, variables, contadores, acumuladores, condiciones e iteraciones.
- **2.4 Matemáticas:** aritmética, álgebra básica, ecuaciones, funciones, conjuntos, relaciones, proporciones, porcentajes y probabilidad básica.
- **2.5 Matemática discreta (introducción):** lógica matemática, combinatoria, permutaciones, combinaciones, relaciones, grafos y aritmética modular.

**Proyecto oficial:** diseñar algoritmos y diagramas de flujo de un sistema de administración de una empresa.

## Resultados de aprendizaje

Al finalizar podrás analizar un problema antes de programar, separar lo esencial de los detalles, identificar patrones y reglas, representar decisiones mediante lógica, diseñar algoritmos con entradas/procesos/salidas, construir pseudocódigo y diagramas de flujo, y utilizar matemáticas básicas para justificar cálculos y restricciones.

## 2.1 — Pensamiento computacional

El pensamiento computacional es una forma estructurada de formular problemas y diseñar soluciones que puedan ejecutarse, comprobarse o automatizarse. No es sinónimo de programar: se aplica antes y durante la implementación.

### 2.1.1 — Descomposición

Consiste en dividir un problema amplio en subproblemas más pequeños, comprensibles y comprobables.

**Ejemplo:** un sistema de administración de una tienda se puede dividir en:
1. gestión de productos;
2. registro de clientes;
3. ventas;
4. inventario;
5. reportes;
6. usuarios y permisos.

Cada parte puede descomponerse aún más. El módulo de ventas, por ejemplo, requiere seleccionar productos, validar stock, calcular importes, confirmar la operación y actualizar inventario.

Una buena descomposición procura responsabilidades claras y evita que cada parte dependa innecesariamente de todas las demás.

### 2.1.2 — Abstracción

Abstraer es conservar los detalles relevantes para el objetivo y omitir temporalmente los que no afectan la solución.

Para calcular el total de una venta necesitamos precio, cantidad, descuentos e impuestos aplicables. No necesitamos conocer el color de la caja registradora.

La abstracción no significa ignorar detalles importantes. Si una regla fiscal afecta el cálculo, no se puede omitir.

### 2.1.3 — Reconocimiento de patrones

Busca similitudes entre situaciones para reutilizar soluciones o reglas.

Ejemplo: las operaciones de agregar, consultar, modificar y eliminar pueden repetirse en productos, clientes y proveedores. Reconocer el patrón ayuda a diseñar operaciones coherentes, pero no significa que todas las entidades deban compartir exactamente las mismas reglas.

### 2.1.4 — Generalización

Consiste en formular una solución que funcione para una familia de casos, no solo para un ejemplo específico.

Una fórmula para calcular el subtotal de una línea de venta debe funcionar con distintos precios y cantidades válidas. Debe especificar también qué ocurre con cantidades negativas, cero o valores fuera de rango.

### 2.1.5 — Modelado de problemas

Un modelo representa los elementos y relaciones relevantes de una situación. Puede ser textual, matemático, tabular, gráfico o algorítmico.

Para una venta:
- entidades: producto, venta, detalle de venta y cliente;
- datos: identificador, precio, cantidad, fecha;
- reglas: no vender cantidades superiores al stock disponible;
- resultados: total y actualización del inventario.

Un modelo es una simplificación útil, no una copia perfecta de la realidad. Debe declarar sus supuestos.

### 2.1.6 — Casos límite

Son entradas o situaciones extremas que pueden revelar errores:
- lista vacía;
- cantidad cero;
- cantidad negativa;
- precio con muchos decimales;
- producto inexistente;
- stock exactamente igual a la cantidad solicitada;
- valor máximo permitido;
- operación repetida;
- dato faltante o mal formado.

No basta con probar el «camino feliz». Las reglas deben indicar cómo se manejan entradas inválidas y límites.

### Técnica de análisis antes de programar

1. Escribe el problema en una frase.
2. Identifica quién lo utiliza y qué necesita conseguir.
3. Enumera entradas disponibles.
4. Define salidas esperadas.
5. Establece reglas y restricciones.
6. Divide el problema en tareas.
7. Identifica casos límite.
8. Diseña una solución manual o en pseudocódigo.
9. Prueba el diseño con ejemplos.
10. Solo entonces selecciona lenguaje y estructura de código.

## 2.2 — Lógica

La lógica permite expresar condiciones y razonar sobre ellas. En programación se utiliza para decisiones, validaciones, filtros y control de flujo.

### 2.2.1 — Proposiciones

Una proposición es un enunciado declarativo al que se le puede asignar un valor de verdad: verdadero o falso.

Ejemplos:
- «El stock es mayor que cero» puede ser verdadero o falso para un producto.
- «La cantidad solicitada es positiva» puede evaluarse para una entrada.
- «Cierra la ventana» no es una proposición: es una orden.

### 2.2.2 — Operadores AND, OR y NOT

Sean P y Q proposiciones:

### 2.2.3 — Tablas de verdad

La tabla de verdad enumera las combinaciones posibles de valores y permite comprobar el resultado de un operador o expresión.

| P | Q | P AND Q | P OR Q |
|---|---|---|---|
| F | F | F | F |
| F | V | F | V |
| V | F | F | V |
| V | V | V | V |

- **AND (conjunción):** verdadero solo si todas las condiciones son verdaderas.
- **OR (disyunción inclusiva):** verdadero si al menos una condición es verdadera.
- **NOT (negación):** invierte el valor de verdad.

Tabla de NOT:

| P | NOT P |
|---|---|
| F | V |
| V | F |

**Ejemplo de negocio:** se puede confirmar una venta si el producto existe AND la cantidad solicitada es positiva AND el stock es suficiente.

La prioridad de operadores y el uso de paréntesis importan. Escribe expresiones complejas de forma explícita para evitar interpretaciones erróneas.

### 2.2.4 — Implicaciones

La expresión «si P, entonces Q» se representa (P \rightarrow Q). Solo es falsa cuando P es verdadera y Q es falsa.

Ejemplo: «Si el pago está confirmado, entonces se puede emitir el comprobante». Esta regla no afirma que todo comprobante implica necesariamente un pago confirmado, salvo que se establezca también la relación inversa.

### 2.2.5 — Equivalencias

(P \leftrightarrow Q) es verdadera cuando ambas proposiciones tienen el mismo valor de verdad. Puede leerse «P si y solo si Q».

En diseño de software, una equivalencia expresa que dos condiciones se cumplen exactamente en los mismos casos. No declares equivalencias cuando solo has demostrado una dirección de implicación.

### 2.2.6 — Álgebra booleana

Permite transformar expresiones lógicas manteniendo su valor de verdad. Identidades útiles:

- Identidad: (P \land V = P), (P \lor F = P).
- Dominación: (P \lor V = V), (P \land F = F).
- Idempotencia: (P \land P=P), (P \lor P=P).
- Doble negación: \(\neg(\neg P)=P\).
- Conmutatividad: (P\land Q=Q\land P).
- De Morgan: \(\neg(P\land Q)=\neg P\lor\neg Q\); \(\neg(P\lor Q)=\neg P\land\neg Q\).

Estas leyes ayudan a simplificar condiciones y revisar validaciones.

### 2.2.7 — Predicados

Un predicado es una expresión cuyo valor de verdad depende de una o más variables. Por ejemplo, (StockSuficiente(producto,cantidad)).

Cuando se asignan valores concretos, el predicado puede evaluarse como verdadero o falso. Los predicados permiten expresar reglas generales sin escribir una condición separada para cada producto.

## 2.3 — Algoritmos iniciales

Un algoritmo es una secuencia finita y ordenada de pasos para resolver una tarea. Debe definir qué recibe, qué transforma y qué resultado produce.

### 2.3.1 — Entrada

La entrada son los datos que recibe el algoritmo desde el usuario, un archivo, un dispositivo u otro sistema. Define formato, tipo, rango y reglas de validación.

### 2.3.2 — Procesamiento

El procesamiento aplica operaciones y reglas a los datos recibidos. Debe respetar el orden de las operaciones y las restricciones del problema.

### 2.3.3 — Salida

La salida es el resultado que el algoritmo presenta, almacena o envía. Debe indicar formato y comportamiento cuando no exista un resultado válido.

**Ejemplo de total de línea:** entrada: precio unitario y cantidad; procesamiento: validar ambos valores y multiplicarlos; salida: subtotal o mensaje de error.

### 2.3.6 — Variables

Una variable representa un dato que puede cambiar durante el algoritmo. Debe tener un nombre significativo y un dominio válido.

Ejemplos: `precioUnitario`, `cantidad`, `subtotal`. Evita nombres ambiguos como `x` o `dato2` cuando el significado puede expresarse.

### 2.3.7 — Contadores

Un contador registra cuántas veces ocurre un evento; suele incrementarse en una unidad.

### 2.3.8 — Acumuladores

Un acumulador combina valores a medida que se procesan.

Ejemplo:
- contador: número de productos procesados;
- acumulador: suma de los importes de una factura.

Inicializa ambos antes del ciclo. Si el contador empieza en un valor incorrecto, el resultado puede fallar incluso cuando el ciclo esté bien escrito.

### 2.3.9 — Condiciones

Una condición permite seleccionar un camino.

### 2.3.10 — Iteraciones

Una iteración repite un bloque mientras se cumpla una condición o por una cantidad determinada de veces.

Antes de crear un ciclo define:
- condición de inicio;
- condición de continuación;
- actualización de variables;
- condición de terminación;
- comportamiento ante entradas inválidas.

Un ciclo que no cambia la variable que controla su condición puede convertirse en un ciclo infinito.

### 2.3.4 — Pseudocódigo

El pseudocódigo expresa la lógica sin depender de la sintaxis de un lenguaje específico. Debe ser consistente y suficientemente preciso para que otra persona pueda implementarlo.

Ejemplo:

```text
INICIO
  LEER precio
  LEER cantidad

  SI precio < 0 O cantidad <= 0 ENTONCES
    MOSTRAR "Entrada inválida"
  SINO
    subtotal <- precio * cantidad
    MOSTRAR subtotal
  FIN SI
FIN
```

### 2.3.5 — Diagramas de flujo

Representan visualmente el recorrido del algoritmo. Convenciones frecuentes:
- óvalo: inicio/fin;
- paralelogramo: entrada/salida;
- rectángulo: proceso;
- rombo: decisión;
- flechas: dirección del flujo.

Los símbolos son una convención de representación; lo importante es que cada decisión tenga salidas identificadas y que el flujo no quede ambiguo.

## 2.4 — Matemáticas

### 2.4.1 — Aritmética

Operaciones fundamentales: suma, resta, multiplicación, división, potencias y raíces. En programación importa además el tipo numérico, el orden de operaciones y el tratamiento de división por cero.

Ejemplo de importe: (precio \times cantidad). Si se aplican descuentos, documenta si se calculan antes o después de impuestos y qué reglas de redondeo aplican.

### 2.4.2 — Álgebra básica

Las variables representan cantidades desconocidas o cambiantes. Las expresiones permiten modelar relaciones.

Si (p) es el precio unitario y (q) la cantidad, el subtotal es (S=pq).

### 2.4.3 — Ecuaciones

Una ecuación expresa igualdad entre dos expresiones. Resolverla significa encontrar los valores que satisfacen la igualdad.

Ejemplo: si (S=pq), entonces para (p\neq0), (q=S/p). En el modelo real, además deben comprobarse unidades y restricciones del dominio.

### 2.4.4 — Funciones

Una función asigna una salida a cada entrada válida según una regla. Por ejemplo, (f(q)=pq) para precio fijo (p).

En programación, una función puede recibir parámetros, validar datos y devolver un resultado. Debe documentar entradas, salida, efectos secundarios y errores posibles.

### 2.4.5 — Conjuntos

Un conjunto es una colección bien definida de elementos. Se usan operaciones como:
- unión (A\cup B);
- intersección (A\cap B);
- diferencia (A\setminus B);
- pertenencia (x\in A).

Ejemplo: conjunto de productos activos y conjunto de productos con stock. Su intersección contiene productos que cumplen ambas condiciones.

### 2.4.6 — Relaciones

Una relación conecta elementos de conjuntos. Puede representar «pertenece a», «es proveedor de» o «es mayor que». Las propiedades (reflexiva, simétrica, transitiva, etc.) dependen de la relación estudiada.

### 2.4.7 — Proporciones

Una proporción compara cantidades.

### 2.4.8 — Porcentajes

Un porcentaje expresa una razón por cada cien.

Si un producto cuesta 80.000 y se aplica un descuento del 10%, el descuento es 8.000 y el precio posterior es 72.000, antes de considerar impuestos u otras reglas.

Evita sumar porcentajes sin revisar la base sobre la que se aplican. Dos descuentos sucesivos del 10% no equivalen a un descuento único del 20%: (0,9\times0,9=0,81), es decir, reducción total del 19%.

### 2.4.9 — Probabilidad básica

La probabilidad cuantifica incertidumbre bajo un modelo. En un espacio muestral finito con resultados equiprobables, (P(A)=\frac{\text{casos favorables}}{\text{casos posibles}}).

No todos los sucesos reales son equiprobables ni independientes. Una probabilidad calculada con un modelo incorrecto produce una respuesta engañosa.

## 2.5 — Matemática discreta (introducción)

### 2.5.1 — Lógica matemática

Formaliza proposiciones, cuantificadores y reglas de inferencia. Es la base para razonar sobre condiciones, algoritmos y propiedades de estructuras.

### 2.5.2 — Combinatoria

Estudia cómo contar selecciones y arreglos sin enumerar todos los casos. Antes de elegir una fórmula, pregunta si el orden importa y si se permite repetir elementos.

### 2.5.3 — Permutaciones

Cuentan ordenamientos donde el orden importa. Para ordenar (n) elementos distintos, hay (n!) permutaciones.

Ejemplo: ordenar tres productos A, B y C produce (3!=6) órdenes.

### 2.5.4 — Combinaciones

Cuentan selecciones donde el orden no importa. El número de formas de elegir (k) elementos de (n) es:

\[
\binom{n}{k}=\frac{n!}{k!(n-k)!}
\]

Ejemplo: elegir dos integrantes de un equipo de cuatro produce \(\binom{4}{2}=6\) pares.

### 2.5.5 — Relaciones

Una relación conecta elementos de conjuntos. Puede representar pertenencia, dependencia, precedencia u otras asociaciones. Sus propiedades dependen de la relación estudiada.

### 2.5.6 — Grafos

Un grafo está formado por vértices y aristas. Puede modelar conexiones entre ciudades, dependencias entre tareas, redes de computadores o relaciones entre entidades.

Conceptos iniciales:
- vértice/nodo;
- arista/enlace;
- grafo dirigido y no dirigido;
- camino;
- ciclo;
- grado de un vértice.

Ejemplo empresarial: productos y proveedores pueden modelarse como nodos conectados por relaciones «suministra». No se debe confundir este modelo conceptual con un diseño de base de datos definitivo.

### 2.5.7 — Aritmética modular

Trabaja con residuos de divisiones. (a\equiv b\pmod n) significa que (a) y (b) dejan el mismo residuo al dividirse por (n).

Ejemplo: (17\equiv5\pmod{12}). Puede utilizarse para representar horas en un reloj de 12 horas o para cálculos cíclicos. En seguridad informática aparece en criptografía, pero esta etapa solo introduce el concepto; no se debe implementar criptografía propia.

## Proyecto oficial — Sistema de administración de una empresa

Diseña los algoritmos y diagramas de flujo de un sistema administrativo. El alcance didáctico mínimo será:

1. registrar productos;
2. consultar un producto;
3. modificar datos de un producto;
4. registrar una venta;
5. validar stock;
6. calcular subtotal y total;
7. actualizar inventario;
8. emitir un resumen;
9. rechazar entradas inválidas.

### Fase A — Análisis

Redacta el problema, identifica usuarios y necesidades, define entradas/salidas, reglas de negocio y supuestos. Separa requisitos confirmados de decisiones que todavía deben consultarse.

### Fase B — Descomposición y modelo

Divide el sistema en módulos. Identifica entidades y relaciones principales. Dibuja el flujo general y los subprocesos de venta e inventario.

### Fase C — Lógica

Escribe las condiciones con AND, OR y NOT. Construye tablas de verdad para reglas críticas, por ejemplo, confirmar una venta solo si el producto existe, la cantidad es positiva y el stock es suficiente.

### Fase D — Algoritmos

Entrega pseudocódigo para:
- registrar producto;
- buscar producto;
- modificar precio;
- registrar venta;
- actualizar stock;
- calcular totales;
- generar resumen.

### Fase E — Pruebas de escritorio

Simula los algoritmos con:
- catálogo vacío;
- producto inexistente;
- cantidad cero;
- cantidad negativa;
- stock exacto;
- stock insuficiente;
- dos ventas consecutivas;
- precio con decimales;
- descuento del 0% y del máximo permitido.

### Entregables

- documento de análisis y supuestos;
- descomposición del problema;
- modelo de entidades/relaciones;
- pseudocódigo de cada proceso;
- diagramas de flujo;
- tablas de verdad de validaciones;
- tabla de pruebas de escritorio con entrada, estado inicial, resultado esperado y resultado obtenido;
- reflexión sobre casos límite.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Análisis y descomposición | 15 |
| Abstracción, patrones y modelo | 15 |
| Lógica y tablas de verdad | 15 |
| Pseudocódigo y control de flujo | 20 |
| Diagramas claros y completos | 15 |
| Matemáticas y reglas de negocio | 10 |
| Casos límite y pruebas de escritorio | 10 |

## Banco de ejercicios con soluciones

1. Descompón «registrar una venta» en al menos cinco tareas.  
   **Solución orientativa:** identificar cliente, seleccionar producto, validar cantidad/stock, calcular importes, confirmar venta, actualizar stock y emitir comprobante.

2. Evalúa (P\land\neg Q) cuando P es verdadero y Q falso.  
   **Respuesta:** verdadero.

3. ¿Cuándo es falsa la implicación (P\rightarrow Q)?  
   **Respuesta:** únicamente cuando P es verdadera y Q es falsa.

4. Escribe pseudocódigo para sumar diez precios válidos.  
   **Solución orientativa:** inicializar acumulador en cero; repetir diez veces lectura y validación; sumar cada precio válido; mostrar el acumulado. Debe especificarse qué hacer con una entrada inválida.

5. ¿Cuánto es el 15% de 200.000?  
   **Respuesta:** 30.000.

6. ¿Cuántas formas hay de ordenar cuatro productos distintos?  
   **Respuesta:** (4!=24).

7. ¿Cuántos pares se pueden formar eligiendo dos personas de cinco, sin importar el orden?  
   **Respuesta:** \(\binom{5}{2}=10\).

8. ¿Cuál es el residuo de 29 módulo 6?  
   **Respuesta:** 5.

## Autoevaluación

- ¿Puedes explicar el problema antes de proponer código?
- ¿Puedes identificar qué datos son relevantes y cuáles no?
- ¿Puedes construir una tabla de verdad y justificarla?
- ¿Puedes transformar una regla escrita en pseudocódigo?
- ¿Puedes distinguir contador de acumulador?
- ¿Puedes probar casos normales y límite?
- ¿Puedes justificar si un cálculo utiliza permutación o combinación?

Si una respuesta depende de una regla de negocio no especificada, regístrala como supuesto pendiente; no inventes la regla.

## Recursos audiovisuales

No se incorpora video en esta versión. La selección audiovisual de esta etapa requiere verificar que el audio esté en español y que cada recurso enseñe directamente el concepto concreto (por ejemplo, tablas de verdad o diagramas de flujo). No se incluyen enlaces genéricos ni videos cuya pertinencia no se haya comprobado.

## Referencias

- OpenStax, **College Algebra** (material educativo abierto para álgebra, funciones y ecuaciones): https://openstax.org/details/books/college-algebra-2e
- OpenStax, **Precalculus 2e** (funciones, conjuntos y probabilidad introductoria según capítulos): https://openstax.org/details/books/precalculus-2e
- MIT OpenCourseWare, **Mathematics for Computer Science** (lógica, pruebas, combinatoria y grafos; recurso académico en inglés, referencia de consulta para autoría, no video recomendado al estudiante): https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/
- NIST, **Discrete Mathematics** no se atribuye como estándar; para conceptos de modularidad se recomienda consultar textos académicos y materiales del curso indicado.
- Khan Academy en Español, biblioteca de matemáticas: https://es.khanacademy.org/math

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** algoritmos y ejercicios propuestos; el proyecto aún no se implementa ni ejecuta como software.  
**Estado editorial:** en desarrollo; referencias y pertinencia audiovisual pendientes de revisión antes de aprobar.
