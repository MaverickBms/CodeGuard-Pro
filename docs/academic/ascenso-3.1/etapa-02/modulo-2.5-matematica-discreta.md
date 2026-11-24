# Etapa 2 · Módulo 2.5 — Matemática discreta (introducción)

**Estado:** borrador académico desarrollado (pendiente validación editorial externa).  
**Alineación:** ASCENSO 3.1, Etapa 2, Módulo 2.5.  
**Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 2 — Pensamiento computacional, lógica y matemáticas.
- **Módulo:** 2.5 — Matemática discreta (introducción).
- **Lecciones oficiales:** 7 (2.5.1 a 2.5.7).

## Propósito
Introducir estructuras discretas fundamentales para algoritmos, datos, criptografía básica y razonamiento computacional.

## Resultados de aprendizaje
1. Aplicar lógica matemática, combinatoria y conteo.
2. Comprender permutaciones, combinaciones, relaciones y grafos básicos.
3. Usar aritmética modular en problemas simples.

---

## Lección 2.5.1 — Lógica matemática

### Identificación
- **Lección oficial:** 2.5.1 — Lógica matemática. **Secuencia:** 1/7.

### Propósito de aprendizaje
Consolidar la lógica formal como herramienta para razonamiento y demostración básica.

### Conocimientos previos
- Módulo 2.2.

### Resultados de aprendizaje
- Aplicar lógica proposicional y predicados en contextos matemáticos.
- Distinguir condición necesaria y suficiente.
- Construir argumentos simples válidos.
- Detectar falacias básicas.

### Desarrollo conceptual
La lógica matemática formaliza el razonamiento: proposiciones, conectores, cuantificadores, reglas de inferencia y demostraciones. Permite validar si una conclusión se sigue de unas premisas.

Condición suficiente: si p entonces q. Condición necesaria: q es necesaria para p. Condición necesaria y suficiente: p si y solo si q.

En informática, sustenta verificación, especificaciones, consultas, reglas de negocio y pruebas.

### Ejemplo técnico desarrollado
Premisas: “Si hay error 500, hay fallo del servidor”. “Hay error 500”. Conclusión: “Hay fallo del servidor”. (Modus ponens, válido).

### Práctica guiada
- Identifica premisa, conclusión y validez en 3 argumentos.

### Actividad independiente
Escribe un argumento inválido que parezca plausible y explica la falacia.

### Criterios de aceptación
- Distingue validez y verdad.
- Identifica condición necesaria/suficiente.
- Detecta falacia.

### Errores frecuentes y recomendaciones
- **Error:** confundir argumento válido con conclusión verdadera. **Recomendación:** validez depende de la forma.
- **Error:** invertir implicaciones. **Recomendación:** revisar contraposición.

### Evaluación de comprensión
1. ¿Qué es modus ponens?
2. ¿Diferencia entre necesario y suficiente?
3. Da una falacia común.

### Referencias
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.

---

## Lección 2.5.2 — Combinatoria

### Identificación
- **Lección oficial:** 2.5.2 — Combinatoria. **Secuencia:** 2/7.

### Propósito de aprendizaje
Contar posibilidades de forma sistemática.

### Conocimientos previos
- Lección 2.4.1.

### Resultados de aprendizaje
- Aplicar regla de la suma y del producto.
- Contar configuraciones simples.
- Evitar doble conteo.
- Modelar problemas de conteo.

### Desarrollo conceptual
La **combinatoria** estudia cómo contar arreglos y selecciones. Reglas básicas:
- **Producto:** si una tarea tiene m opciones y otra n, juntas tienen m*n.
- **Suma:** si opciones mutuamente excluyentes, se suman.

El doble conteo ocurre cuando se cuenta el mismo caso más de una vez. Definir claramente qué cuenta como caso distinto es esencial.

### Ejemplo técnico desarrollado
PIN de 4 dígitos (0-9, se permiten repetidos): `10^4 = 10.000`.

Si no se permiten repetidos: `10*9*8*7 = 5040`.

### Práctica guiada
- ¿Cuántas contraseñas de 3 letras mayúsculas hay si se permiten repeticiones?

### Actividad independiente
Modela cuántas combinaciones de menú hay con 3 entradas, 4 platos y 2 postres.

### Criterios de aceptación
- Aplica regla correcta.
- Justifica supuestos.
- No doble cuenta.

### Errores frecuentes y recomendaciones
- **Error:** confundir suma y producto. **Recomendación:** producto para pasos secuenciales, suma para alternativas excluyentes.
- **Error:** olvidar si hay repetición. **Recomendación:** explicitarlo.

### Evaluación de comprensión
1. ¿Cuándo usas regla del producto?
2. ¿Qué es doble conteo?
3. Calcula casos con y sin repetición.

### Referencias
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.

---

## Lección 2.5.3 — Permutaciones

### Identificación
- **Lección oficial:** 2.5.3 — Permutaciones. **Secuencia:** 3/7.

### Propósito de aprendizaje
Contar arreglos donde el orden importa.

### Conocimientos previos
- Lección 2.5.2.

### Resultados de aprendizaje
- Definir permutación.
- Calcular permutaciones sin y con restricciones simples.
- Distinguir permutación de combinación.
- Aplicar factorial.

### Desarrollo conceptual
Una **permutación** es un arreglo ordenado de elementos. El orden importa: ABC es distinto de BAC.

Permutaciones de n elementos: `n!`. Permutaciones de r elementos tomados de n: `P(n,r)=n!/(n-r)!`.

El factorial crece rápidamente, lo cual es relevante en algoritmos (complejidad).

### Ejemplo técnico desarrollado
3 personas para 3 puestos: `3!=6`.  
5 candidatos para 2 puestos ordenados: `P(5,2)=5*4=20`.

### Práctica guiada
- Calcula `P(6,3)`.

### Actividad independiente
¿Cuántas formas hay de ordenar 4 libros distintos en una estantería?

### Criterios de aceptación
- Usa fórmula correcta.
- Identifica que el orden importa.
- Calcula factorial correctamente.

### Errores frecuentes y recomendaciones
- **Error:** usar permutación cuando el orden no importa. **Recomendación:** preguntar si ABC = BAC.
- **Error:** error de factorial. **Recomendación:** simplificar antes de multiplicar.

### Evaluación de comprensión
1. ¿Qué es una permutación?
2. ¿Cuándo importa el orden?
3. Calcula `P(4,2)`.

### Referencias
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.

---

## Lección 2.5.4 — Combinaciones

### Identificación
- **Lección oficial:** 2.5.4 — Combinaciones. **Secuencia:** 4/7.

### Propósito de aprendizaje
Contar selecciones donde el orden no importa.

### Conocimientos previos
- Lección 2.5.3.

### Resultados de aprendizaje
- Definir combinación.
- Calcular `C(n,r)`.
- Distinguir combinación y permutación.
- Aplicar a problemas de selección.

### Desarrollo conceptual
Una **combinación** es una selección de elementos donde el orden no importa. ABC es la misma combinación que BAC.

Fórmula: `C(n,r)=n!/(r!(n-r)!)`.

Se usa en selección de equipos, subconjuntos, loterías y muestreo.

### Ejemplo técnico desarrollado
Elegir 2 personas de 5: `C(5,2)=10`.

### Práctica guiada
- Calcula `C(6,2)` y `C(6,4)`. Observa la simetría.

### Actividad independiente
De 8 candidatos, ¿cuántos comités de 3 se pueden formar?

### Criterios de aceptación
- Usa fórmula correcta.
- Distingue de permutación.
- Interpreta resultado.

### Errores frecuentes y recomendaciones
- **Error:** confundir con permutación. **Recomendación:** preguntar si el orden cambia el caso.
- **Error:** calcular factoriales grandes innecesariamente. **Recomendación:** simplificar.

### Evaluación de comprensión
1. ¿Qué diferencia hay entre combinación y permutación?
2. Calcula `C(5,3)`.
3. Da un caso donde el orden no importa.

### Referencias
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.

---

## Lección 2.5.5 — Relaciones

### Identificación
- **Lección oficial:** 2.5.5 — Relaciones. **Secuencia:** 5/7.

### Propósito de aprendizaje
Profundizar en relaciones discretas y sus propiedades.

### Conocimientos previos
- Lección 2.4.6.

### Resultados de aprendizaje
- Representar relaciones discretas.
- Analizar reflexividad, simetría, antisimetría y transitividad.
- Identificar relaciones de equivalencia y orden a nivel introductorio.
- Aplicar a modelos de datos.

### Desarrollo conceptual
En matemática discreta, las relaciones modelan conexiones entre elementos: grafos, dependencias, equivalencias, jerarquías.

Una relación de equivalencia es reflexiva, simétrica y transitiva. Una relación de orden parcial suele ser reflexiva, antisimétrica y transitiva.

Estas propiedades importan en bases de datos, dependencias de paquetes, control de acceso y modelado.

### Ejemplo técnico desarrollado
Relación “misma versión mayor” en paquetes: puede formar clases de equivalencia si se define bien.  
Relación “depende de” en paquetes: dirigida, puede ser transitiva en análisis, pero debe evitar ciclos.

### Práctica guiada
- Determina propiedades de la relación “<=” en enteros.

### Actividad independiente
Modela una relación de prerrequisitos de cursos y analiza si puede tener ciclos.

### Criterios de aceptación
- Identifica propiedades correctamente.
- Usa contraejemplos.
- Aplica a un caso informático.

### Errores frecuentes y recomendaciones
- **Error:** asumir transitividad sin probar. **Recomendación:** buscar contraejemplo.
- **Error:** confundir simétrica con antisimétrica. **Recomendación:** revisar definiciones.

### Evaluación de comprensión
1. ¿Qué es una relación de equivalencia?
2. ¿“Depende de” es simétrica?
3. Da un ejemplo de relación antisimétrica.

### Referencias
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.

---

## Lección 2.5.6 — Grafos

### Identificación
- **Lección oficial:** 2.5.6 — Grafos. **Secuencia:** 6/7.

### Propósito de aprendizaje
Introducir grafos como modelo de relaciones y redes.

### Conocimientos previos
- Lección 2.5.5.

### Resultados de aprendizaje
- Definir grafo, vértice y arista.
- Distinguir grafo dirigido/no dirigido, ponderado/no ponderado.
- Representar grafos simples.
- Identificar aplicaciones en informática.

### Desarrollo conceptual
Un **grafo** es un conjunto de vértices (nodos) y aristas (conexiones). Puede ser dirigido (arcos con dirección) o no dirigido. Puede tener pesos en aristas.

Se usan para modelar redes, rutas, dependencias, redes sociales, estados y más. Representaciones comunes: lista de adyacencia y matriz de adyacencia.

Conceptos básicos: camino, ciclo, grado, conectividad.

### Ejemplo técnico desarrollado
**Red simple:** A-B, A-C, B-D.
- Vértices: {A,B,C,D}
- Aristas: {A-B,A-C,B-D}
- Camino A a D: A-B-D.

### Práctica guiada
- Dibuja un grafo dirigido con 4 nodos y 5 aristas que represente prerrequisitos.

### Actividad independiente
Modela una pequeña red de computadoras como grafo y explica qué representa cada nodo/arista.

### Criterios de aceptación
- Define vértice/arista.
- Representa grafo correctamente.
- Identifica tipo de grafo.

### Errores frecuentes y recomendaciones
- **Error:** confundir grafo con gráfico estadístico. **Recomendación:** especificar graph/network.
- **Error:** olvidar dirección en grafos dirigidos. **Recomendación:** usar flechas.

### Evaluación de comprensión
1. ¿Qué es un grafo dirigido?
2. Da 2 aplicaciones de grafos en informática.
3. ¿Qué es un ciclo?

### Referencias
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.

---

## Lección 2.5.7 — Aritmética modular

### Identificación
- **Lección oficial:** 2.5.7 — Aritmética modular. **Secuencia:** 7/7.

### Propósito de aprendizaje
Comprender la aritmética modular y sus aplicaciones básicas.

### Conocimientos previos
- Lecciones 2.4.1, 2.5.2.

### Resultados de aprendizaje
- Definir congruencia modular.
- Calcular operaciones módulo n.
- Aplicar aritmética modular a problemas simples.
- Reconocer su uso en informática.

### Desarrollo conceptual
La **aritmética modular** trabaja con restos de división. Se dice que `a ≡ b (mod n)` si `a` y `b` dejan el mismo resto al dividir por `n`.

Ejemplo: `17 ≡ 5 (mod 12)` porque ambos dejan resto 5.

Es útil en relojes, hashes, checksums, criptografía, generación de índices y ciclos. Operaciones como suma y multiplicación pueden hacerse módulo n.

### Ejemplo técnico desarrollado
**Reloj 24h:** si son 22:00 y pasan 5 horas, `(22+5) mod 24 = 3`.

**Módulo:** `10 mod 3 = 1`.

### Práctica guiada
- Calcula: `25 mod 7`, `(14+9) mod 12`, `(6*7) mod 5`.

### Actividad independiente
Explica cómo usarías módulo para asignar tareas a 4 workers de forma circular.

### Criterios de aceptación
- Calcula módulos correctamente.
- Explica congruencia.
- Aplica a un caso real.

### Errores frecuentes y recomendaciones
- **Error:** confundir módulo con división. **Recomendación:** módulo devuelve resto.
- **Error:** manejar mal negativos (depende del lenguaje). **Recomendación:** verificar semántica.

### Evaluación de comprensión
1. ¿Qué significa `a ≡ b (mod n)`?
2. Calcula `29 mod 6`.
3. Da una aplicación de aritmética modular en informática.

### Referencias
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.
- Khan Academy. *Modular arithmetic*. https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic. Consultado: 2026-11-24.