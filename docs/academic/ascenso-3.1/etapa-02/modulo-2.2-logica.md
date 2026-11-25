# Etapa 2 · Módulo 2.2 — Lógica

**Estado:** borrador académico desarrollado (pendiente validación editorial externa).  
**Alineación:** ASCENSO 3.1, Etapa 2, Módulo 2.2.  
**Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 2 — Pensamiento computacional, lógica y matemáticas.
- **Módulo:** 2.2 — Lógica.
- **Lecciones oficiales:** 7 (2.2.1 a 2.2.7).

## Propósito
Desarrollar la base lógica para razonar, modelar condiciones y comprender estructuras de decisión en programación.

## Resultados de aprendizaje
1. Identificar proposiciones y operadores lógicos.
2. Construir y leer tablas de verdad.
3. Comprender implicaciones, equivalencias y álgebra booleana.
4. Introducir predicados como base de condiciones más expresivas.

---

## Lección 2.2.1 — Proposiciones

### Identificación
- **Lección oficial:** 2.2.1 — Proposiciones. **Secuencia:** 1/7.

### Propósito de aprendizaje
Distinguir proposiciones de otras expresiones lingüísticas.

### Conocimientos previos
- Módulo 2.1.

### Resultados de aprendizaje
- Definir proposición.
- Identificar si un enunciado es proposición.
- Asignar valor de verdad cuando corresponde.
- Reconocer proposiciones simples y compuestas.

### Desarrollo conceptual
Una **proposición** es un enunciado que puede ser verdadero o falso, pero no ambos al mismo tiempo en el mismo contexto. Ejemplos: “2 + 2 = 4” (verdadera), “El disco está lleno” (puede ser verdadera o falsa según el estado).

No son proposiciones: preguntas (“¿Está encendido?”), órdenes (“Cierra la puerta”), exclamaciones ambiguas, o expresiones con variables sin definir (“x > 5” sin indicar x). Estas últimas se acercan a predicados.

En programación, las condiciones de `if`, `while` y filtros se basan en expresiones booleanas que derivan de la lógica proposicional.

### Ejemplo técnico desarrollado
| Enunciado | ¿Proposición? | Motivo |
|---|---:|---|
| 5 es impar | Sí | Verdadera |
| Abre el archivo | No | Es orden |
| ¿Hay conexión? | No | Es pregunta |
| La RAM es volátil | Sí | Verdadera en contexto técnico normal |
| x es mayor que 10 | Depende | Falta definir x |

### Práctica guiada
- Clasifica 10 enunciados propios como proposición/no proposición.

### Actividad independiente
Escribe 5 proposiciones relacionadas con ciberseguridad o programación y determina su valor de verdad.

### Criterios de aceptación
- Clasificación correcta.
- Justificación clara.
- Identifica casos ambiguos.

### Errores frecuentes y recomendaciones
- **Error:** confundir opinión con proposición verificable. **Recomendación:** pedir criterio de verdad.
- **Error:** aceptar enunciados con variables libres. **Recomendación:** identificar variables no definidas.

### Evaluación de comprensión
1. ¿Qué hace que un enunciado sea proposición?
2. ¿“Actualiza el sistema” es proposición?
3. Da un ejemplo ambiguo y explica por qué.

### Referencias
- Hurley, P. J. *A Concise Introduction to Logic*. Cengage.
- Stanford Encyclopedia of Philosophy. *Propositional Logic*. https://plato.stanford.edu/entries/logic-propositional/. Consultado: 2026-11-24.

---

## Lección 2.2.2 — Operadores AND, OR, NOT

### Identificación
- **Lección oficial:** 2.2.2 — Operadores AND, OR, NOT. **Secuencia:** 2/7.

### Propósito de aprendizaje
Usar operadores lógicos básicos para combinar proposiciones.

### Conocimientos previos
- Lección 2.2.1.

### Resultados de aprendizaje
- Aplicar AND, OR y NOT.
- Interpretar expresiones booleanas.
- Traducir condiciones de lenguaje natural a lógica.
- Reconocer diferencias entre OR inclusivo y exclusivo.

### Desarrollo conceptual
- **AND (∧):** verdadero solo si ambas proposiciones son verdaderas.
- **OR (∨):** verdadero si al menos una es verdadera (OR inclusivo).
- **NOT (¬):** invierte el valor de verdad.

En programación aparecen como `&&`, `||`, `!` o `and`, `or`, `not`. El OR cotidiano a veces es exclusivo (“café o té”), pero en lógica formal el OR estándar suele ser inclusivo.

### Ejemplo técnico desarrollado
**Condición de acceso:** “Puede entrar si es empleado AND tiene credencial activa”.

| Empleado | Credencial activa | Acceso |
|---|---:|---:|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

### Práctica guiada
- Traduce: “Puedo instalar si tengo permisos y hay espacio, o si soy administrador”.

### Actividad independiente
Crea 5 reglas de acceso usando AND/OR/NOT y evalúalas con 3 casos cada una.

### Criterios de aceptación
- Usa operadores correctamente.
- Traduce lenguaje natural con precisión.
- Evalúa casos correctamente.

### Errores frecuentes y recomendaciones
- **Error:** confundir OR inclusivo con exclusivo. **Recomendación:** aclarar “uno o ambos”.
- **Error:** negar mal una condición compuesta. **Recomendación:** estudiar De Morgan más adelante.

### Evaluación de comprensión
1. ¿Cuándo es verdadero AND?
2. ¿Cuál es la diferencia entre OR inclusivo y exclusivo?
3. Evalúa: NOT (V AND F).

### Referencias
- Stanford Encyclopedia of Philosophy. *Propositional Logic*. https://plato.stanford.edu/entries/logic-propositional/. Consultado: 2026-11-24.

---

## Lección 2.2.3 — Tablas de verdad

### Identificación
- **Lección oficial:** 2.2.3 — Tablas de verdad. **Secuencia:** 3/7.

### Propósito de aprendizaje
Usar tablas de verdad para evaluar expresiones lógicas.

### Conocimientos previos
- Lección 2.2.2.

### Resultados de aprendizaje
- Construir tablas de verdad.
- Evaluar expresiones compuestas.
- Detectar contradicciones y tautologías a nivel básico.
- Verificar equivalencias simples.

### Desarrollo conceptual
Una tabla de verdad enumera todas las combinaciones posibles de valores de verdad de las proposiciones y muestra el resultado de una expresión. Para *n* proposiciones, hay `2^n` filas.

Es una herramienta sistemática para evitar errores de intuición. En programación, ayuda a validar condiciones complejas antes de implementarlas.

### Ejemplo técnico desarrollado
**Expresión:** `(A AND B) OR NOT A`

| A | B | A AND B | NOT A | Resultado |
|---|---|---:|---:|---:|
| V | V | V | F | V |
| V | F | F | F | F |
| F | V | F | V | V |
| F | F | F | V | V |

### Práctica guiada
- Construye la tabla de verdad de `A OR (NOT B)`.

### Actividad independiente
Evalúa `(A AND NOT B) OR (B AND NOT A)` e interpreta qué significa (XOR).

### Criterios de aceptación
- Tabla completa.
- Cálculos correctos.
- Interpretación correcta.

### Errores frecuentes y recomendaciones
- **Error:** omitir filas. **Recomendación:** calcular `2^n`.
- **Error:** evaluar en orden incorrecto. **Recomendación:** usar paréntesis y precedencia.

### Evaluación de comprensión
1. ¿Cuántas filas tiene una tabla con 3 proposiciones?
2. ¿Qué es una tautología?
3. Construye la tabla de `NOT (A OR B)`.

### Referencias
- Hurley, P. J. *A Concise Introduction to Logic*. Cengage.

---

## Lección 2.2.4 — Implicaciones

### Identificación
- **Lección oficial:** 2.2.4 — Implicaciones. **Secuencia:** 4/7.

### Propósito de aprendizaje
Comprender la implicación lógica y sus formas relacionadas.

### Conocimientos previos
- Lecciones 2.2.1 a 2.2.3.

### Resultados de aprendizaje
- Definir implicación `p -> q`.
- Identificar antecedente y consecuente.
- Distinguir implicación, conversa, inversa y contraposición.
- Evitar falacias comunes.

### Desarrollo conceptual
La implicación `p -> q` se lee “si p, entonces q”. Es falsa solo cuando p es verdadera y q es falsa. En los demás casos, es verdadera. Esto puede resultar contraintuitivo, pero evita ambigüedad formal.

Formas relacionadas:
- **Conversa:** `q -> p`
- **Inversa:** `¬p -> ¬q`
- **Contraposición:** `¬q -> ¬p` (equivalente a la original)

La implicación no significa causalidad. “Si llueve, la calle se moja” no implica que toda calle mojada sea por lluvia.

### Ejemplo técnico desarrollado
**Regla:** “Si el usuario es admin, puede eliminar registros”.

- Admin y puede eliminar: cumple.
- Admin y no puede eliminar: rompe la regla.
- No admin y puede eliminar: no contradice esta implicación sola.
- No admin y no puede eliminar: no contradice.

### Práctica guiada
- Escribe la conversa, inversa y contraposición de: “Si hay autenticación, entonces hay registro de acceso”.

### Actividad independiente
Identifica una falacia de afirmar la consecuente en un contexto de ciberseguridad.

### Criterios de aceptación
- Identifica antecedente/consecuente.
- Genera las 4 formas.
- Reconoce la contraposición equivalente.

### Errores frecuentes y recomendaciones
- **Error:** asumir que `p -> q` implica `q -> p`. **Recomendación:** probar con contraejemplo.
- **Error:** confundir implicación con causalidad. **Recomendación:** usar ejemplos de reglas.

### Evaluación de comprensión
1. ¿Cuándo es falsa `p -> q`?
2. ¿Cuál forma es equivalente a la implicación original?
3. Da un ejemplo de afirmar la consecuente.

### Referencias
- Stanford Encyclopedia of Philosophy. *Classical Logic*. https://plato.stanford.edu/entries/logic-classical/. Consultado: 2026-11-24.

---

## Lección 2.2.5 — Equivalencias

### Identificación
- **Lección oficial:** 2.2.5 — Equivalencias. **Secuencia:** 5/7.

### Propósito de aprendizaje
Reconocer expresiones lógicas equivalentes.

### Conocimientos previos
- Lecciones 2.2.3 y 2.2.4.

### Resultados de aprendizaje
- Definir equivalencia lógica.
- Verificar equivalencias con tablas de verdad.
- Aplicar equivalencias básicas para simplificar condiciones.
- Usar equivalencias en refactorización de condiciones.

### Desarrollo conceptual
Dos expresiones son lógicamente equivalentes si tienen el mismo valor de verdad en todas las combinaciones posibles. Se denota con `≡` o `<->`.

Equivalencias útiles:
- Doble negación: `¬(¬p) ≡ p`
- De Morgan: `¬(p AND q) ≡ ¬p OR ¬q`; `¬(p OR q) ≡ ¬p AND ¬q`
- Conmutativa: `p AND q ≡ q AND p`
- Distributiva: `p AND (q OR r) ≡ (p AND q) OR (p AND r)`

En programación, simplificar condiciones mejora legibilidad y reduce errores.

### Ejemplo técnico desarrollado
**Condición:** `NOT (isAdmin OR isOwner)`
Por De Morgan: `NOT isAdmin AND NOT isOwner`.

Ambas expresiones son equivalentes. La segunda puede ser más clara según contexto.

### Práctica guiada
- Verifica con tabla de verdad la ley de De Morgan para `NOT (A AND B)`.

### Actividad independiente
Simplifica 3 condiciones de código usando equivalencias lógicas.

### Criterios de aceptación
- Verifica equivalencia correctamente.
- Aplica De Morgan.
- Mantiene el significado.

### Errores frecuentes y recomendaciones
- **Error:** aplicar De Morgan mal (olvidar negar ambos términos). **Recomendación:** negar cada parte y cambiar operador.
- **Error:** simplificar cambiando el significado. **Recomendación:** probar con tabla de verdad.

### Evaluación de comprensión
1. ¿Qué significa que dos expresiones sean equivalentes?
2. Aplica De Morgan a `NOT (A OR B)`.
3. ¿Por qué las equivalencias son útiles en programación?

### Referencias
- Hurley, P. J. *A Concise Introduction to Logic*. Cengage.

---

## Lección 2.2.6 — Álgebra booleana

### Identificación
- **Lección oficial:** 2.2.6 — Álgebra booleana. **Secuencia:** 6/7.

### Propósito de aprendizaje
Aplicar reglas del álgebra booleana para manipular expresiones lógicas.

### Conocimientos previos
- Lecciones 2.2.2 a 2.2.5.

### Resultados de aprendizaje
- Identificar leyes básicas del álgebra booleana.
- Simplificar expresiones booleanas.
- Relacionar álgebra booleana con circuitos y condiciones.
- Verificar simplificaciones.

### Desarrollo conceptual
El álgebra booleana opera sobre valores verdadero/falso (1/0) con operaciones como AND, OR y NOT. Es base de la lógica digital, circuitos, condiciones de programación y búsquedas.

Leyes comunes:
- **Identidad:** `A AND 1 = A`, `A OR 0 = A`
- **Nulidad:** `A AND 0 = 0`, `A OR 1 = 1`
- **Idempotencia:** `A AND A = A`, `A OR A = A`
- **Complemento:** `A AND NOT A = 0`, `A OR NOT A = 1`
- **Absorción:** `A OR (A AND B) = A`

Estas leyes permiten simplificar expresiones y reducir complejidad.

### Ejemplo técnico desarrollado
**Simplificar:** `A OR (A AND B)`
Por absorción: `A`.

Verificación rápida:
- Si A=V, resultado V.
- Si A=F, expresión queda `F OR (F AND B)=F`.

### Práctica guiada
- Simplifica: `A AND (A OR B)` y `(A OR NOT A) AND B`.

### Actividad independiente
Simplifica una condición de programa con 3 variables y demuestra que la versión simplificada es equivalente.

### Criterios de aceptación
- Aplica leyes correctamente.
- Verifica resultado.
- Explica la ley usada.

### Errores frecuentes y recomendaciones
- **Error:** aplicar leyes sin verificar. **Recomendación:** usar tabla de verdad en casos dudosos.
- **Error:** confundir álgebra booleana con álgebra aritmética. **Recomendación:** recordar que OR no es suma normal.

### Evaluación de comprensión
1. Simplifica `A AND 1`.
2. ¿Qué dice la ley de complemento?
3. ¿Dónde se usa álgebra booleana fuera de matemáticas?

### Referencias
- Boole, G. *An Investigation of the Laws of Thought* (obra histórica).
- Mano, M. M., & Ciletti, M. D. *Digital Design*. Pearson.

---

## Lección 2.2.7 — Predicados

### Identificación
- **Lección oficial:** 2.2.7 — Predicados. **Secuencia:** 7/7.

### Propósito de aprendizaje
Introducir predicados para expresar propiedades sobre objetos o variables.

### Conocimientos previos
- Lecciones 2.2.1 a 2.2.6.

### Resultados de aprendizaje
- Definir predicado.
- Distinguir proposición y predicado.
- Usar predicados simples con variables.
- Comprender cuantificadores a nivel introductorio.

### Desarrollo conceptual
Un **predicado** es una expresión que se vuelve proposición cuando sus variables toman valores o se cuantifican. Ejemplo: `P(x): x es mayor que 10`. No es verdadera ni falsa hasta definir `x`.

Los predicados permiten expresar reglas generales: “para todo usuario u, si u está autenticado, u tiene sesión”. Los cuantificadores comunes son:
- **Universal (∀):** para todo.
- **Existencial (∃):** existe al menos uno.

En programación, los predicados aparecen como funciones que devuelven booleano: `esPar(n)`, `estaActivo(usuario)`, `tienePermiso(u, recurso)`.

### Ejemplo técnico desarrollado
**Predicado:** `EsMayorDeEdad(x) := x >= 18`

- `EsMayorDeEdad(20)` = verdadero.
- `EsMayorDeEdad(15)` = falso.
- `∀x en grupo, EsMayorDeEdad(x)` = verdadero solo si todos cumplen.

### Práctica guiada
- Define 3 predicados sobre estudiantes (edad, nota, asistencia) y evalúalos con 2 valores.

### Actividad independiente
Traduce a predicados: “Todos los administradores tienen MFA” y “Existe un usuario sin correo verificado”.

### Criterios de aceptación
- Define predicado correctamente.
- Evalúa con valores concretos.
- Usa cuantificadores básicos.

### Errores frecuentes y recomendaciones
- **Error:** tratar predicado con variable libre como proposición. **Recomendación:** especificar valor o cuantificador.
- **Error:** confundir ∀ con ∃. **Recomendación:** usar ejemplos concretos.

### Evaluación de comprensión
1. ¿Qué diferencia hay entre proposición y predicado?
2. ¿Qué significa ∀?
3. Da un ejemplo de predicado en programación.

### Referencias
- Stanford Encyclopedia of Philosophy. *Predicate Logic*. https://plato.stanford.edu/entries/logic-classical/. Consultado: 2026-11-24.