# Etapa 2 · Módulo 2.4 — Matemáticas

**Estado:** borrador académico desarrollado (pendiente validación editorial externa).  
**Alineación:** ASCENSO 3.1, Etapa 2, Módulo 2.4.  
**Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 2 — Pensamiento computacional, lógica y matemáticas.
- **Módulo:** 2.4 — Matemáticas.
- **Lecciones oficiales:** 9 (2.4.1 a 2.4.9).

## Propósito
Proporcionar bases matemáticas prácticas para programación, análisis de problemas y razonamiento técnico.

## Resultados de aprendizaje
1. Aplicar aritmética, álgebra, ecuaciones, funciones y conjuntos.
2. Interpretar proporciones, porcentajes y probabilidad básica.
3. Traducir problemas a expresiones matemáticas simples.

---

## Lección 2.4.1 — Aritmética

### Identificación
- **Lección oficial:** 2.4.1 — Aritmética. **Secuencia:** 1/9.

### Propósito de aprendizaje
Aplicar operaciones aritméticas básicas con precisión.

### Conocimientos previos
- Matemáticas básicas escolares.

### Resultados de aprendizaje
- Realizar suma, resta, multiplicación, división y módulo.
- Aplicar orden de operaciones.
- Interpretar división entera y residuo.
- Evitar errores comunes en cálculos.

### Desarrollo conceptual
La aritmética es la base de muchos cálculos en programación: totales, promedios, índices, tiempos, tamaños y conversiones. Operaciones clave: `+`, `-`, `*`, `/`, división entera, módulo (`%`).

El **orden de operaciones** (paréntesis, exponentes, multiplicación/división, suma/resta) evita ambigüedad. En programación, también importa el tipo de dato: división entera vs flotante.

El operador módulo devuelve el residuo: `7 % 3 = 1`. Es útil para paridad, ciclos, hashes y distribución.

### Ejemplo técnico desarrollado
**Cálculo:** `total = (3 + 5) * 2 = 16`.  
Sin paréntesis: `3 + 5 * 2 = 13`.

**Módulo:** `10 % 2 = 0` (par), `11 % 2 = 1` (impar).

### Práctica guiada
- Calcula: `8 + 2 * 5`, `(8 + 2) * 5`, `17 % 5`, `17 // 5`.

### Actividad independiente
Escribe 5 problemas de programación que requieran aritmética y resuélvelos.

### Criterios de aceptación
- Aplica orden correcto.
- Usa módulo correctamente.
- Explica resultados.

### Errores frecuentes y recomendaciones
- **Error:** ignorar paréntesis. **Recomendación:** explicitar precedencia.
- **Error:** confundir `/` y `//` en lenguajes como Python. **Recomendación:** probar con ejemplos.

### Evaluación de comprensión
1. ¿Cuál es el resultado de `2 + 3 * 4`?
2. ¿Para qué sirve el módulo?
3. ¿Por qué importa el tipo de división?

### Referencias
- OpenStax. *Prealgebra*. https://openstax.org/details/books/prealgebra. Consultado: 2026-11-24.

---

## Lección 2.4.2 — Álgebra básica

### Identificación
- **Lección oficial:** 2.4.2 — Álgebra básica. **Secuencia:** 2/9.

### Propósito de aprendizaje
Usar variables y expresiones algebraicas para modelar problemas.

### Conocimientos previos
- Lección 2.4.1.

### Resultados de aprendizaje
- Manipular expresiones algebraicas simples.
- Sustituir valores en fórmulas.
- Traducir enunciados a expresiones.
- Comprender variables como incógnitas o parámetros.

### Desarrollo conceptual
El álgebra usa símbolos para representar valores desconocidos o variables. En programación, esto se relaciona directamente con variables, fórmulas y funciones.

Expresiones como `2x + 3` o `a*b - c` permiten generalizar cálculos. La sustitución consiste en reemplazar variables por valores concretos.

Simplificar expresiones reduce errores y mejora claridad. Por ejemplo, `2x + 3x = 5x`.

### Ejemplo técnico desarrollado
**Fórmula:** precio final `P = c - c*d`, donde `c` es costo y `d` descuento en decimal.
Si `c=200`, `d=0.15`, entonces `P = 200 - 30 = 170`.

### Práctica guiada
- Traduce: “el doble de un número más 5” y “el área de un triángulo”.

### Actividad independiente
Crea 3 fórmulas para problemas de programación (IMC, velocidad, conversión).

### Criterios de aceptación
- Traduce enunciados correctamente.
- Sustituye valores sin error.
- Usa variables con significado.

### Errores frecuentes y recomendaciones
- **Error:** confundir variable algebraica con variable de programa en todos los aspectos. **Recomendación:** en álgebra representa valor; en programa también tiene tipo/estado.
- **Error:** errores de signo. **Recomendación:** revisar paso a paso.

### Evaluación de comprensión
1. Evalúa `3x + 2` para `x=4`.
2. Traduce “la mitad de un número menos 1”.
3. ¿Por qué el álgebra es útil en programación?

### Referencias
- OpenStax. *Elementary Algebra*. https://openstax.org/details/books/elementary-algebra-2e. Consultado: 2026-11-24.

---

## Lección 2.4.3 — Ecuaciones

### Identificación
- **Lección oficial:** 2.4.3 — Ecuaciones. **Secuencia:** 3/9.

### Propósito de aprendizaje
Resolver ecuaciones simples y usarlas para modelar problemas.

### Conocimientos previos
- Lección 2.4.2.

### Resultados de aprendizaje
- Resolver ecuaciones lineales simples.
- Verificar soluciones.
- Modelar problemas con ecuaciones.
- Interpretar soluciones en contexto.

### Desarrollo conceptual
Una **ecuación** es una igualdad que contiene una o más incógnitas. Resolverla significa encontrar valores que hacen verdadera la igualdad.

Para ecuaciones lineales simples: despejar la incógnita aplicando operaciones equivalentes en ambos lados.

Verificar es esencial: sustituir la solución en la ecuación original.

### Ejemplo técnico desarrollado
`2x + 4 = 10`
- Restar 4: `2x = 6`
- Dividir por 2: `x = 3`
- Verificar: `2(3)+4=10`.

### Práctica guiada
- Resuelve: `3x - 5 = 16`, `x/2 + 1 = 7`.

### Actividad independiente
Modela con ecuación: “Si un servicio cobra 20€ fijo más 5€ por hora y pagaste 45€, ¿cuántas horas fueron?”

### Criterios de aceptación
- Resuelve correctamente.
- Verifica solución.
- Modela enunciado.

### Errores frecuentes y recomendaciones
- **Error:** aplicar operación en un solo lado. **Recomendación:** mantener equilibrio.
- **Error:** no verificar. **Recomendación:** sustituir siempre.

### Evaluación de comprensión
1. Resuelve `5x + 2 = 17`.
2. ¿Por qué verificar la solución?
3. Modela un problema propio con ecuación lineal.

### Referencias
- OpenStax. *Elementary Algebra*. https://openstax.org/details/books/elementary-algebra-2e. Consultado: 2026-11-24.

---

## Lección 2.4.4 — Funciones

### Identificación
- **Lección oficial:** 2.4.4 — Funciones. **Secuencia:** 4/9.

### Propósito de aprendizaje
Comprender funciones como relación entrada-salida.

### Conocimientos previos
- Lecciones 2.4.2 y 2.4.3.

### Resultados de aprendizaje
- Definir función matemática.
- Identificar dominio, codominio/rango e imagen.
- Evaluar funciones.
- Relacionar funciones matemáticas con funciones en programación.

### Desarrollo conceptual
Una **función** asigna a cada elemento de un dominio exactamente una salida. Se escribe `f(x)=...`. Para un mismo input, no puede haber dos outputs distintos.

Conceptos: dominio (entradas válidas), rango/imagen (salidas posibles/obtenidas), variable independiente/dependiente.

En programación, una función tiene una idea similar, pero puede tener efectos secundarios, estado o no ser pura. Conviene distinguir función matemática pura de función de software.

### Ejemplo técnico desarrollado
`f(x)=2x+1`
- `f(3)=7`
- `f(0)=1`
- Dominio: reales (en este caso simple).

### Práctica guiada
- Evalúa `f(x)=x^2 - 2` para x=-2,-1,0,1,2.

### Actividad independiente
Define una función que modele el costo de envío: tarifa base + costo por kg.

### Criterios de aceptación
- Evalúa correctamente.
- Identifica dominio.
- Distingue función matemática y de software.

### Errores frecuentes y recomendaciones
- **Error:** creer que toda relación es función. **Recomendación:** verificar una salida por entrada.
- **Error:** ignorar dominio. **Recomendación:** considerar valores inválidos (división por cero).

### Evaluación de comprensión
1. ¿Qué hace que una relación sea función?
2. Evalúa `f(x)=3x-4` en `x=5`.
3. Da un ejemplo de función en programación que no sea pura.

### Referencias
- OpenStax. *College Algebra*. https://openstax.org/details/books/college-algebra-2e. Consultado: 2026-11-24.

---

## Lección 2.4.5 — Conjuntos

### Identificación
- **Lección oficial:** 2.4.5 — Conjuntos. **Secuencia:** 5/9.

### Propósito de aprendizaje
Usar conjuntos para representar colecciones y relaciones básicas.

### Conocimientos previos
- Lección 2.2.1.

### Resultados de aprendizaje
- Definir conjunto, elemento y pertenencia.
- Realizar unión, intersección y diferencia.
- Usar diagramas de Venn simples.
- Relacionar conjuntos con estructuras de datos.

### Desarrollo conceptual
Un **conjunto** es una colección de elementos distintos. Se denota con llaves: `A = {1,2,3}`. La pertenencia se expresa como `2 ∈ A`.

Operaciones:
- **Unión (A ∪ B):** elementos en A o B.
- **Intersección (A ∩ B):** elementos en ambos.
- **Diferencia (A - B):** elementos en A que no están en B.
- **Complemento:** depende del universo definido.

En programación, los sets implementan ideas similares. Son útiles para eliminar duplicados, membresía y operaciones de conjuntos.

### Ejemplo técnico desarrollado
`A={1,2,3}`, `B={3,4,5}`
- `A∪B={1,2,3,4,5}`
- `A∩B={3}`
- `A-B={1,2}`

### Práctica guiada
- Dados `A={a,b,c}` y `B={b,c,d,e}`, calcula unión, intersección y diferencia.

### Actividad independiente
Modela usuarios con permisos “lectura” y “escritura” como conjuntos y calcula quién tiene ambos.

### Criterios de aceptación
- Operaciones correctas.
- Usa notación básica.
- Aplica a un caso real.

### Errores frecuentes y recomendaciones
- **Error:** duplicar elementos en conjuntos. **Recomendación:** los conjuntos no tienen duplicados.
- **Error:** confundir unión con intersección. **Recomendación:** usar diagramas de Venn.

### Evaluación de comprensión
1. ¿Qué es `A ∩ B`?
2. Si `A={1,2}`, `B={2,3}`, ¿cuál es `A∪B`?
3. ¿Para qué sirve un set en programación?

### Referencias
- OpenStax. *Contemporary Mathematics*. https://openstax.org/details/books/contemporary-mathematics. Consultado: 2026-11-24.

---

## Lección 2.4.6 — Relaciones

### Identificación
- **Lección oficial:** 2.4.6 — Relaciones. **Secuencia:** 6/9.

### Propósito de aprendizaje
Comprender relaciones entre elementos de conjuntos.

### Conocimientos previos
- Lección 2.4.5.

### Resultados de aprendizaje
- Definir relación.
- Representar relaciones con pares ordenados, tablas o grafos.
- Identificar propiedades básicas (reflexiva, simétrica, transitiva) a nivel introductorio.
- Aplicar relaciones a datos.

### Desarrollo conceptual
Una **relación** es un subconjunto del producto cartesiano entre conjuntos, que indica cómo se relacionan elementos. Por ejemplo, “es amigo de”, “es mayor que”, “pertenece a”.

Las relaciones pueden representarse como pares ordenados `(a,b)`, matrices, tablas o grafos dirigidos.

Propiedades comunes:
- **Reflexiva:** todo elemento se relaciona consigo mismo.
- **Simétrica:** si aRb entonces bRa.
- **Transitiva:** si aRb y bRc entonces aRc.

No toda relación tiene estas propiedades. “Es mayor que” es transitiva, pero no reflexiva ni simétrica.

### Ejemplo técnico desarrollado
Conjunto `A={1,2,3}`, relación “menor que”: {(1,2),(1,3),(2,3)}.

### Práctica guiada
- Determina si la relación “es igual a” en números es reflexiva, simétrica y transitiva.

### Actividad independiente
Modela la relación “prerrequisito de” entre 4 cursos y representa como grafo dirigido.

### Criterios de aceptación
- Representa la relación correctamente.
- Identifica propiedades básicas.
- Aplica a un caso real.

### Errores frecuentes y recomendaciones
- **Error:** asumir que todas las relaciones son simétricas. **Recomendación:** probar contraejemplos.
- **Error:** confundir relación con función. **Recomendación:** función es un tipo especial de relación.

### Evaluación de comprensión
1. ¿Qué es una relación?
2. ¿Es “mayor que” simétrica?
3. Da un ejemplo de relación transitiva.

### Referencias
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.

---

## Lección 2.4.7 — Proporciones

### Identificación
- **Lección oficial:** 2.4.7 — Proporciones. **Secuencia:** 7/9.

### Propósito de aprendizaje
Usar proporciones para comparar cantidades y resolver problemas de escala.

### Conocimientos previos
- Lecciones 2.4.1 y 2.4.2.

### Resultados de aprendizaje
- Definir razón y proporción.
- Resolver proporciones simples.
- Aplicar regla de tres con cuidado.
- Interpretar proporciones en contexto.

### Desarrollo conceptual
Una **razón** compara dos cantidades (a:b o a/b). Una **proporción** es una igualdad entre dos razones: `a/b = c/d`.

Las proporciones se usan en escalas, recetas, conversiones, rendimiento y configuración. La regla de tres funciona cuando la relación es proporcional directa; no debe usarse ciegamente si la relación no es lineal.

### Ejemplo técnico desarrollado
Si 2 servidores procesan 1000 solicitudes/min, ¿cuántas procesan 5 servidores en la misma proporción ideal? `2/1000 = 5/x -> x=2500`.  
**Nota:** en la realidad, puede no escalar linealmente.

### Práctica guiada
- Resuelve: si 3 GB cuestan 12€, ¿cuánto cuestan 7 GB en proporción directa?

### Actividad independiente
Identifica un caso donde la regla de tres no aplique y explica por qué.

### Criterios de aceptación
- Resuelve proporciones.
- Reconoce límite de la proporcionalidad.
- Interpreta contexto.

### Errores frecuentes y recomendaciones
- **Error:** aplicar regla de tres a relaciones no lineales. **Recomendación:** verificar supuesto de proporcionalidad.

### Evaluación de comprensión
1. ¿Qué es una proporción?
2. Resuelve `4/6 = x/9`.
3. Da un ejemplo donde la proporcionalidad no se cumple.

### Referencias
- OpenStax. *Prealgebra*. https://openstax.org/details/books/prealgebra. Consultado: 2026-11-24.

---

## Lección 2.4.8 — Porcentajes

### Identificación
- **Lección oficial:** 2.4.8 — Porcentajes. **Secuencia:** 8/9.

### Propósito de aprendizaje
Calcular e interpretar porcentajes en contextos técnicos y cotidianos.

### Conocimientos previos
- Lección 2.4.7.

### Resultados de aprendizaje
- Calcular porcentaje de una cantidad.
- Calcular aumentos y descuentos.
- Interpretar puntos porcentuales vs porcentaje.
- Evitar errores comunes de porcentaje.

### Desarrollo conceptual
Un porcentaje representa una fracción sobre 100. `p% = p/100`. Se usa para descuentos, impuestos, progreso, métricas, tasas de error y rendimiento.

Cálculos comunes:
- `x% de N = N * x/100`
- Aumento: `N * (1 + x/100)`
- Descuento: `N * (1 - x/100)`

Cuidado: subir 10% y bajar 10% no vuelve al valor original. También hay que distinguir porcentaje de puntos porcentuales.

### Ejemplo técnico desarrollado
Precio 200€, descuento 15%: `200 * 0.85 = 170€`.  
Si luego sube 15%: `170 * 1.15 = 195.5€`, no 200€.

### Práctica guiada
- Calcula 25% de 80, un aumento de 20% sobre 50 y un descuento de 30% sobre 120.

### Actividad independiente
Analiza una métrica: “la tasa de error pasó de 2% a 4%”. ¿Cuánto subió en puntos porcentuales y en porcentaje relativo?

### Criterios de aceptación
- Cálculos correctos.
- Distingue puntos porcentuales y porcentaje relativo.
- Interpreta contexto.

### Errores frecuentes y recomendaciones
- **Error:** confundir puntos porcentuales con %. **Recomendación:** explicitar ambos.
- **Error:** asumir reversibilidad. **Recomendación:** calcular paso a paso.

### Evaluación de comprensión
1. ¿Cuánto es 15% de 300?
2. ¿Por qué 10% arriba y 10% abajo no vuelve al original?
3. Diferencia entre 2% a 4%.

### Referencias
- OpenStax. *Prealgebra*. https://openstax.org/details/books/prealgebra. Consultado: 2026-11-24.

---

## Lección 2.4.9 — Probabilidad básica

### Identificación
- **Lección oficial:** 2.4.9 — Probabilidad básica. **Secuencia:** 9/9.

### Propósito de aprendizaje
Comprender probabilidad básica para razonar sobre incertidumbre.

### Conocimientos previos
- Lecciones 2.4.1, 2.4.7, 2.4.8.

### Resultados de aprendizaje
- Definir experimento, espacio muestral y evento.
- Calcular probabilidades simples.
- Distinguir eventos independientes y dependientes a nivel básico.
- Evitar falacias comunes.

### Desarrollo conceptual
La **probabilidad** mide la posibilidad de que ocurra un evento, entre 0 y 1 (o 0% y 100%). En casos equiprobables: `P(E)=casos favorables/casos posibles`.

Conceptos: experimento aleatorio, espacio muestral, evento, complemento. Eventos independientes no se afectan entre sí; dependientes sí.

La probabilidad no garantiza resultados individuales, solo describe tendencias en el largo plazo. Es útil en testing, riesgos, fiabilidad y análisis.

### Ejemplo técnico desarrollado
Lanzar un dado justo: espacio muestral {1..6}.  
`P(par)=3/6=0.5`.  
`P(>4)=2/6=1/3`.

### Práctica guiada
- En una bolsa con 3 bolas rojas y 2 azules, ¿probabilidad de sacar roja?

### Actividad independiente
Modela la probabilidad de acertar una contraseña de 4 dígitos si solo hay 1 intento aleatorio.

### Criterios de aceptación
- Calcula probabilidades simples.
- Define espacio muestral.
- Interpreta resultado.

### Errores frecuentes y recomendaciones
- **Error:** falacia del jugador. **Recomendación:** independencia de eventos.
- **Error:** confundir probabilidad con certeza. **Recomendación:** expresar incertidumbre.

### Evaluación de comprensión
1. ¿Qué es el espacio muestral?
2. ¿Cuál es P(sacar 6) en un dado justo?
3. ¿Qué significa independencia?

### Referencias
- OpenStax. *Introductory Statistics*. https://openstax.org/details/books/introductory-statistics-2e. Consultado: 2026-11-24.