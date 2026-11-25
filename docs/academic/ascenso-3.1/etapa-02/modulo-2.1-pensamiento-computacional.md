# Etapa 2 · Módulo 2.1 — Pensamiento computacional

**Estado:** borrador académico desarrollado (pendiente validación editorial externa).  
**Alineación:** ASCENSO 3.1, Etapa 2, Módulo 2.1.  
**Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 2 — Pensamiento computacional, lógica y matemáticas.
- **Objetivo oficial de etapa:** desarrollar la capacidad de solucionar problemas antes de escribir código.
- **Módulo:** 2.1 — Pensamiento computacional.
- **Lecciones oficiales:** 6 (2.1.1 a 2.1.6).

## Propósito del módulo
Desarrollar habilidades para analizar problemas, abstraer lo relevante, reconocer patrones, generalizar soluciones y modelar casos límite antes de programar.

## Resultados de aprendizaje
1. Descomponer problemas complejos en partes manejables.
2. Abstraer detalles irrelevantes y conservar los esenciales.
3. Reconocer patrones y generalizar soluciones.
4. Modelar problemas y anticipar casos límite.

---

## Lección 2.1.1 — Descomposición

### Identificación
- **Lección oficial:** 2.1.1 — Descomposición. **Secuencia:** 1/6.

### Propósito de aprendizaje
Aprender a dividir problemas grandes en subproblemas más pequeños y resolubles.

### Conocimientos previos
- Etapa 0: resolución de problemas y documentación.
- Etapa 1: noción de sistema y componentes.

### Resultados de aprendizaje
- Definir descomposición.
- Dividir un problema en partes con responsabilidades claras.
- Identificar dependencias entre subproblemas.
- Verificar que las partes cubren el problema original.

### Desarrollo conceptual
La descomposición es la técnica de dividir un problema complejo en partes más pequeñas, comprensibles y manejables. Cada parte debe tener un propósito claro y, idealmente, poder resolverse o verificarse de forma independiente.

No se trata solo de “hacer una lista”. Una buena descomposición define límites: qué hace cada parte, qué entradas necesita, qué salida produce y cómo se relaciona con las demás. En software, esto se relaciona con funciones, módulos, servicios y equipos.

Criterios prácticos:
- **Cobertura:** las partes juntas resuelven el problema completo.
- **No solapamiento excesivo:** evitar duplicar responsabilidades.
- **Tamaño adecuado:** ni demasiado grande ni demasiado granular.
- **Verificabilidad:** cada parte puede probarse.

### Ejemplo técnico desarrollado
**Problema:** construir un sistema de registro de asistencia.

Descomposición:
1. **Entrada de datos:** capturar nombre/ID, fecha, hora.
2. **Validación:** verificar formato, duplicados, usuario existente.
3. **Almacenamiento:** guardar registro en base de datos.
4. **Consulta:** listar asistencia por fecha/usuario.
5. **Reporte:** generar resumen semanal/mensual.
6. **Seguridad:** controlar quién puede registrar y consultar.

**Interpretación:** cada subproblema puede desarrollarse y probarse por separado, pero deben integrarse mediante interfaces claras.

### Práctica guiada
- Descompón el problema “organizar una biblioteca digital personal” en al menos 5 subproblemas.

### Actividad independiente
Descompón un problema de tu vida diaria (planificar un viaje, organizar estudios) y presenta un diagrama de árbol con 3 niveles.

### Criterios de aceptación
- Al menos 5 subproblemas coherentes.
- Cada uno tiene nombre y responsabilidad.
- No hay partes obvias faltantes.

### Errores frecuentes y recomendaciones
- **Error:** descomponer demasiado pronto en código. **Recomendación:** primero entender el problema.
- **Error:** crear partes ambiguas. **Recomendación:** describir entrada/salida de cada parte.
- **Error:** olvidar integración. **Recomendación:** indicar dependencias.

### Evaluación de comprensión
1. ¿Qué hace buena una descomposición?
2. ¿Cómo verificas que no faltan partes?
3. Da un ejemplo de subproblema mal definido y mejóralo.

### Referencias
- Wing, J. M. *Computational Thinking*. Communications of the ACM, 2006. https://doi.org/10.1145/1118178.1118215. Consultado: 2026-11-24.
- BBC Bitesize. *Decomposition*. https://www.bbc.co.uk/bitesize/guides/zqqfyrd/revision/1. Consultado: 2026-11-24.

---

## Lección 2.1.2 — Abstracción

### Identificación
- **Lección oficial:** 2.1.2 — Abstracción. **Secuencia:** 2/6.

### Propósito de aprendizaje
Aprender a enfocarse en los detalles relevantes e ignorar los irrelevantes para el problema.

### Conocimientos previos
- Lección 2.1.1.

### Resultados de aprendizaje
- Definir abstracción.
- Distinguir detalles esenciales y accidentales.
- Crear un modelo simplificado de un problema.
- Reconocer cuándo una abstracción pierde información crítica.

### Desarrollo conceptual
La abstracción consiste en representar lo esencial de un problema ocultando detalles innecesarios. Permite manejar complejidad: no necesitas saber cómo funciona el motor de combustión para conducir, pero sí necesitas volante, pedales y reglas.

En informática, la abstracción aparece en mapas, modelos, interfaces, funciones, clases y APIs. Una buena abstracción reduce carga cognitiva sin ocultar lo que afecta la solución.

El riesgo es abstraer demasiado: omitir un detalle crítico. Por ejemplo, en un sistema de pagos, abstraer “moneda” como simple número puede ignorar decimales, redondeo o tipo de moneda.

### Ejemplo técnico desarrollado
**Problema:** app de transporte urbano.

| Esencial | No esencial (para el modelo inicial) |
|---|---|
| origen, destino, tiempo, tarifa | color del auto, marca de llantas |
| conductor disponible | música favorita del conductor |
| estado del viaje | historial de lavado del vehículo |

**Interpretación:** lo esencial depende del objetivo. Para mantenimiento del vehículo, el historial de lavado podría ser relevante.

### Práctica guiada
- Para un sistema de turnos médicos, lista 5 datos esenciales y 5 no esenciales.

### Actividad independiente
Crea dos abstracciones diferentes del mismo objeto “estudiante”: una para biblioteca y otra para plataforma de cursos.

### Criterios de aceptación
- Distingue esencial/no esencial según contexto.
- Justifica sus decisiones.
- Reconoce que la abstracción depende del objetivo.

### Errores frecuentes y recomendaciones
- **Error:** abstraer detalles críticos. **Recomendación:** preguntar “¿afecta el resultado o la decisión?”.
- **Error:** creer que hay una sola abstracción correcta. **Recomendación:** depende del contexto.

### Evaluación de comprensión
1. ¿Qué es abstraer?
2. Da un ejemplo de detalle crítico que no debe abstraerse.
3. ¿Por qué la abstracción depende del objetivo?

### Referencias
- Wing, J. M. *Computational Thinking*. CACM, 2006. https://doi.org/10.1145/1118178.1118215. Consultado: 2026-11-24.
- MIT OpenCourseWare. *Introduction to Computer Science and Programming*. https://ocw.mit.edu/. Consultado: 2026-11-24.

---

## Lección 2.1.3 — Reconocimiento de patrones

### Identificación
- **Lección oficial:** 2.1.3 — Reconocimiento de patrones. **Secuencia:** 3/6.

### Propósito de aprendizaje
Identificar similitudes y regularidades para reutilizar soluciones.

### Conocimientos previos
- Lecciones 2.1.1 y 2.1.2.

### Resultados de aprendizaje
- Definir patrón en resolución de problemas.
- Identificar similitudes entre problemas distintos.
- Reutilizar una estrategia conocida con adaptación.
- Evitar aplicar patrones de forma ciega.

### Desarrollo conceptual
El reconocimiento de patrones consiste en observar similitudes entre problemas, datos o procesos. Permite reutilizar soluciones, predecir comportamientos y reducir esfuerzo.

En programación, se ve en bucles, validaciones repetidas, plantillas de algoritmos, estructuras de datos y patrones de diseño. En análisis de datos, en tendencias y regularidades.

El peligro es la falsa analogía: dos problemas parecen iguales pero difieren en una restricción clave. Por eso, tras identificar un patrón, hay que validar si realmente aplica.

### Ejemplo técnico desarrollado
**Patrón:** validar entrada de usuario.
- Registro: email no vacío, formato válido.
- Login: usuario no vacío, contraseña no vacía.
- Formulario de pago: monto positivo, tarjeta con formato.

**Patrón común:** recibir entrada → validar reglas → rechazar o continuar.  
**Diferencia:** reglas específicas cambian por contexto.

### Práctica guiada
- Identifica un patrón en estas tareas: lavar platos, lavar ropa, lavar auto. Luego indica qué cambia.

### Actividad independiente
Encuentra 3 procesos en aplicaciones que uses que sigan el patrón “buscar → filtrar → mostrar resultado”.

### Criterios de aceptación
- Identifica patrón y diferencias.
- No aplica el patrón sin adaptación.
- Da ejemplos concretos.

### Errores frecuentes y recomendaciones
- **Error:** ver patrón donde no hay. **Recomendación:** verificar con contraejemplos.
- **Error:** forzar solución por analogía. **Recomendación:** validar restricciones.

### Evaluación de comprensión
1. ¿Para qué sirve reconocer patrones?
2. ¿Qué es una falsa analogía?
3. Da un patrón útil en programación.

### Referencias
- Wing, J. M. *Computational Thinking*. CACM, 2006. https://doi.org/10.1145/1118178.1118215. Consultado: 2026-11-24.
- Polya, G. *How to Solve It*. Princeton University Press. Referencia clásica.

---

## Lección 2.1.4 — Generalización

### Identificación
- **Lección oficial:** 2.1.4 — Generalización. **Secuencia:** 4/6.

### Propósito de aprendizaje
Transformar soluciones específicas en soluciones reutilizables.

### Conocimientos previos
- Lección 2.1.3.

### Resultados de aprendizaje
- Definir generalización.
- Convertir un caso específico en regla o procedimiento general.
- Identificar parámetros y variables de un problema.
- Evaluar límites de una generalización.

### Desarrollo conceptual
La generalización consiste en pasar de casos particulares a una solución aplicable a muchos casos similares. En lugar de resolver solo “sumar 2 y 3”, se crea un procedimiento que suma dos números cualesquiera.

En programación, se generaliza con variables, parámetros, funciones, clases y plantillas. La generalización reduce duplicación, pero puede aumentar complejidad si se hace prematuramente.

Buena práctica: primero resolver un caso concreto, luego identificar qué cambia (parámetros) y qué se mantiene (estructura).

### Ejemplo técnico desarrollado
**Específico:** calcular área de un rectángulo de 5x3 = 15.  
**General:** `area(base, altura) = base * altura`, con `base > 0` y `altura > 0`.

**Interpretación:** se identificaron parámetros (base, altura), regla (multiplicación) y restricciones.

### Práctica guiada
- Generaliza esta solución: “Para calcular el precio final de un producto de $100 con 10% de descuento, hago 100 - 10 = 90”.

### Actividad independiente
Toma 3 problemas similares y escribe una solución general con parámetros y restricciones.

### Criterios de aceptación
- Identifica parámetros.
- Define restricciones.
- La solución general cubre los casos dados.

### Errores frecuentes y recomendaciones
- **Error:** generalizar sin validar casos borde. **Recomendación:** probar con valores extremos.
- **Error:** generalizar demasiado pronto. **Recomendación:** partir de casos concretos.

### Evaluación de comprensión
1. ¿Qué es generalizar?
2. ¿Qué son parámetros en una solución general?
3. ¿Por qué una generalización necesita restricciones?

### Referencias
- Polya, G. *How to Solve It*. Princeton University Press.
- Wing, J. M. *Computational Thinking*. CACM, 2006. https://doi.org/10.1145/1118178.1118215. Consultado: 2026-11-24.

---

## Lección 2.1.5 — Modelado de problemas

### Identificación
- **Lección oficial:** 2.1.5 — Modelado de problemas. **Secuencia:** 5/6.

### Propósito de aprendizaje
Representar problemas del mundo real en modelos que puedan analizarse o resolverse.

### Conocimientos previos
- Lecciones 2.1.1 a 2.1.4.

### Resultados de aprendizaje
- Definir modelo.
- Crear modelos simples (tablas, diagramas, ecuaciones, pseudomodelos).
- Identificar supuestos y limitaciones del modelo.
- Validar si el modelo responde la pregunta.

### Desarrollo conceptual
Un modelo es una representación simplificada de un sistema o problema. Sirve para entender, predecir, comunicar o resolver. Los modelos pueden ser físicos, matemáticos, gráficos, textuales o computacionales.

Todo modelo omite detalles. La pregunta clave es: ¿omite detalles irrelevantes o críticos? Un buen modelo hace explícitos sus supuestos.

En informática, modelamos datos, procesos, estados, flujos y relaciones. Por ejemplo, modelar una cola de atención como FIFO.

### Ejemplo técnico desarrollado
**Problema:** gestionar fila de soporte técnico.

Modelo:
- Entidades: ticket, cliente, agente, cola.
- Atributos: id, prioridad, tiempo de llegada, estado.
- Regla: atender por orden de llegada, salvo prioridad alta.
- Supuesto: un agente atiende un ticket a la vez.
- Limitación: no modela pausas, reassignaciones ni SLA complejo.

### Práctica guiada
- Modela un sistema de reservas de sala: entidades, datos, reglas, supuestos.

### Actividad independiente
Crea un modelo simple para el inventario de una tienda pequeña e indica qué dejaste fuera.

### Criterios de aceptación
- Modelo con entidades, datos y reglas.
- Supuestos explícitos.
- Limitaciones identificadas.

### Errores frecuentes y recomendaciones
- **Error:** confundir modelo con realidad completa. **Recomendación:** declarar supuestos.
- **Error:** modelar sin objetivo. **Recomendación:** preguntar qué decisión soporta el modelo.

### Evaluación de comprensión
1. ¿Qué es un modelo?
2. ¿Por qué es importante declarar supuestos?
3. Da un ejemplo de modelo útil pero incompleto.

### Referencias
- Polya, G. *How to Solve It*. Princeton University Press.
- Brooks, F. P. *The Mythical Man-Month*. Addison-Wesley. (Sobre complejidad y modelos, referencia complementaria).

---

## Lección 2.1.6 — Casos límite

### Identificación
- **Lección oficial:** 2.1.6 — Casos límite. **Secuencia:** 6/6.

### Propósito de aprendizaje
Identificar entradas o condiciones extremas que pueden romper una solución.

### Conocimientos previos
- Lecciones 2.1.1 a 2.1.5.

### Resultados de aprendizaje
- Definir caso límite y caso borde.
- Identificar casos límite en problemas comunes.
- Diseñar pruebas para casos límite.
- Prevenir fallos por supuestos no validados.

### Desarrollo conceptual
Los casos límite (edge cases) son condiciones en los extremos o fuera del comportamiento “normal” esperado. Suelen revelar errores de diseño: división por cero, lista vacía, valor nulo, número máximo, texto vacío, fecha inválida, usuario sin permisos.

Pensar en casos límite es parte del pensamiento computacional porque obliga a definir el comportamiento del sistema ante entradas inusuales pero posibles.

No todos los casos límite son errores del usuario; algunos son condiciones reales del dominio. La solución puede ser rechazar, manejar con valor por defecto, pedir confirmación o registrar excepción, según el caso.

### Ejemplo técnico desarrollado
**Función:** calcular promedio de calificaciones.

Casos límite:
- lista vacía: ¿devolver 0, error o `None`?
- calificación negativa: ¿inválida?
- calificación > 100: ¿inválida?
- un solo elemento: debe funcionar.
- valores no numéricos: rechazar.

**Interpretación:** definir el comportamiento esperado evita bugs y ambigüedad.

### Práctica guiada
- Para una función que divide `a/b`, lista 5 casos límite y el comportamiento esperado.

### Actividad independiente
Diseña 10 casos de prueba para un formulario de registro (email, contraseña, edad), incluyendo al menos 5 casos límite.

### Criterios de aceptación
- Identifica casos límite relevantes.
- Define comportamiento esperado.
- Incluye casos normales y extremos.

### Errores frecuentes y recomendaciones
- **Error:** probar solo el “camino feliz”. **Recomendación:** incluir bordes y entradas inválidas.
- **Error:** manejar todos los casos límite igual. **Recomendación:** decidir según dominio.
- **Error:** asumir que el usuario siempre ingresa datos válidos. **Recomendación:** validar entradas.

### Evaluación de comprensión
1. ¿Qué es un caso límite?
2. Da 3 casos límite para una función que busca un elemento en una lista.
3. ¿Por qué los casos límite son importantes en seguridad?

### Referencias
- Myers, G. J., Sandler, C., & Badgett, T. *The Art of Software Testing*. Wiley.
- OWASP. *Input Validation Cheat Sheet*. https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html. Consultado: 2026-11-24.