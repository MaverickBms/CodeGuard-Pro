# Etapa 17 — Testing, aseguramiento y calidad del software

**Prioridad:** P1 · Obligatoria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** aprender a demostrar que el software funciona, cumple requisitos y tiene una calidad verificable.  
**Proyecto oficial:** diseñar un plan de pruebas completo y automatizar las pruebas de una aplicación construida en etapas anteriores.

## Resultados de aprendizaje
Distinguir QA y QC, verificación y validación; diseñar casos y criterios de aceptación; seleccionar niveles de prueba; medir rendimiento; utilizar dobles de prueba; aplicar TDD/BDD; usar herramientas del stack; interpretar análisis estático y modelos de calidad sin confundir métricas con calidad real.

## 17.1 — Fundamentos
Quality Assurance (QA) comprende actividades planificadas para dar confianza en que los procesos pueden producir calidad. Quality Control (QC) evalúa productos y resultados para detectar incumplimientos. Verificación pregunta si el producto cumple especificaciones; validación pregunta si satisface necesidades y uso previsto.

Un defecto es una condición del producto que puede provocar un resultado incorrecto. Un bug es una expresión informal frecuente. Un caso de prueba define condiciones, datos, pasos y resultado esperado. Los criterios de aceptación expresan condiciones verificables para considerar una funcionalidad aceptable.

Aprende severidad frente a prioridad, precondiciones, postcondiciones, datos de prueba, reproducibilidad y trazabilidad requisito-prueba-defecto. No uses “cero bugs” como criterio absoluto: documenta riesgos residuales.

**Ejercicio:** escribe criterios de aceptación para registrar una venta, incluidos inventario insuficiente, duplicidad de solicitud y fallo de persistencia.

## 17.2 — Testing funcional
- **Unit testing:** prueba una unidad aislada, con dependencias controladas.
- **Integration testing:** verifica interacción entre componentes reales, por ejemplo servicio y base de datos.
- **End-to-end:** comprueba un flujo completo desde la perspectiva del usuario/sistema.
- **Regression:** detecta reaparición de defectos tras cambios.
- **Smoke:** verifica funciones críticas básicas de una build.
- **Sanity:** comprobación acotada de una modificación o área concreta; su definición varía entre equipos.
- **API testing:** valida contrato, estados, autorización, datos, errores y límites de API.

No todos los tests deben ser unitarios ni toda prueba de integración requiere un entorno de producción. Aísla los datos y evita que los tests dependan de orden o estado residual.

**Ejercicio:** diseña pruebas para crear producto, vender unidades, rechazar stock insuficiente y consultar inventario actualizado.

## 17.3 — Testing de usuario
Usability testing observa si las personas pueden completar tareas y dónde encuentran fricción. Accessibility testing comprueba uso con teclado, lectores de pantalla, contraste y otros requisitos aplicables. Exploratory testing utiliza aprendizaje y experimentación estructurada para descubrir escenarios no anticipados. UAT verifica con usuarios o representantes que el producto cumple necesidades y criterios acordados.

No confundas pruebas de usabilidad con encuesta de satisfacción, ni UAT con una aprobación informal sin criterios. Define tareas, perfiles, entorno, consentimiento y registro de hallazgos.

## 17.4 — Rendimiento
- Load testing evalúa comportamiento bajo carga esperada.
- Stress testing lleva el sistema más allá de condiciones previstas para identificar límites y recuperación.
- Spike testing aplica cambios abruptos de carga.
- Endurance testing mantiene carga durante tiempo prolongado.
- Response time mide duración percibida de una operación; latency puede referirse al retraso de una interacción; throughput mide operaciones por unidad de tiempo.
- Bottleneck es un recurso o etapa que limita el rendimiento global.

Define hipótesis, carga, mezcla de operaciones, datos, duración, percentiles, errores y límites. No publiques cifras sin registrar entorno, configuración y metodología. No ejecutes pruebas de carga contra servicios ajenos sin autorización.

## 17.5 — Testing técnico
Test cases contienen pasos y resultados esperados. Assertions verifican condiciones. Mocking sustituye una dependencia para controlar interacción; fixtures preparan datos; test doubles incluyen mocks, stubs, fakes y spies según propósito. Test coverage mide qué parte del código fue ejecutada por tests, no si las pruebas son correctas. Test isolation evita que un caso contamine otro.

Usa mocks para controlar fronteras, pero no simules tanto que las pruebas dejen de representar el comportamiento real. Añade pruebas de integración para validar contratos entre componentes.

## 17.6 — Metodologías
TDD propone ciclo red-green-refactor: escribir una prueba que falla, implementar lo mínimo para hacerla pasar y refactorizar manteniendo pruebas. BDD expresa comportamiento mediante ejemplos compartidos y lenguaje del dominio. AAA organiza pruebas en Arrange, Act, Assert. La pirámide de testing orienta una mayor cantidad de pruebas rápidas y focalizadas y menos pruebas end-to-end costosas; no es una regla matemática universal.

## 17.7 — Herramientas
JUnit y Mockito para Java; Jest y Vitest para ecosistemas JavaScript/TypeScript; Playwright y Cypress para automatización de navegador; Postman para pruebas de API; JMeter para carga. Selecciona herramienta por stack y caso de uso, revisa compatibilidad y fija versiones.

## 17.8 — Análisis de calidad
Static analysis inspecciona código sin ejecutarlo. Linters detectan patrones y problemas configurados; formatters normalizan estilo. SonarQube agrega análisis y reportes según configuración y edición. Code coverage cuantifica ejecución de líneas/rutas según herramienta. Code smells señalan patrones que pueden dificultar mantenimiento, pero no todos son defectos automáticamente.

Revisa falsos positivos, reglas, alcance, exclusiones y calidad de configuración. No conviertas un porcentaje de cobertura en único indicador de calidad.

## 17.9 — Normas y modelos de calidad
ISO/IEC 25010:2023 es referencia para modelo de calidad de producto; verifica la edición y el alcance al citar características. ISO/IEC/IEEE 12207:2026 es la edición indicada en el roadmap para procesos del ciclo de vida; consulta el catálogo oficial y la licencia antes de reproducir contenido normativo. CMMI es un modelo de capacidad y mejora de procesos, no una norma ISO.

Relaciona mantenibilidad, fiabilidad, seguridad, rendimiento y usabilidad con indicadores verificables. Define cada métrica, fuente, periodo y umbral; una métrica aislada puede incentivar comportamientos no deseados.

## Proyecto oficial — Plan de pruebas automatizado
Selecciona una aplicación previa y entrega:
1. Inventario de requisitos y riesgos.
2. Matriz requisito-criterio-caso de prueba.
3. Casos positivos, negativos, límites y permisos.
4. Pruebas unitarias, integración, API y end-to-end proporcionadas al riesgo.
5. Pruebas de accesibilidad y usabilidad.
6. Prueba de rendimiento con entorno autorizado y metodología documentada.
7. Reporte de defectos con pasos de reproducción.
8. Pipeline que ejecute pruebas y análisis estático.
9. Cobertura interpretada, no presentada como calidad absoluta.
10. Informe de resultados, limitaciones y riesgos residuales.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Fundamentos, QA/QC y criterios | 10 |
| Diseño y cobertura de pruebas funcionales | 20 |
| Pruebas de usuario y accesibilidad | 10 |
| Rendimiento y metodología | 10 |
| Dobles, fixtures y aislamiento | 10 |
| TDD/BDD y estrategia | 10 |
| Herramientas y automatización | 10 |
| Análisis estático y métricas | 10 |
| Trazabilidad y reporte | 10 |

Criterio orientativo: 80/100 y evidencia reproducible. Un test no ejecutado no se reporta como aprobado.

## Autoevaluación
1. Diferencia QA y QC.
2. Diferencia verificación y validación.
3. ¿Qué nivel de prueba utilizarías para una consulta SQL real?
4. ¿Qué distingue smoke de regression testing?
5. ¿Por qué coverage no demuestra calidad?
6. ¿Cuándo usarías mock y cuándo fake?
7. Explica red-green-refactor.
8. ¿Qué diferencia hay entre load y stress testing?
9. ¿Qué riesgos tiene medir solo cantidad de bugs?
10. ¿Por qué debes registrar el entorno de rendimiento?

## Recursos audiovisuales
No se incluyen videos aprobados. Se incorporarán solo tras confirmar audio en español y relación directa con la práctica concreta (JUnit, Playwright, TDD, pruebas de carga o accesibilidad).

## Referencias oficiales
- ISTQB Glossary: https://glossary.istqb.org/
- JUnit 5: https://junit.org/junit5/docs/current/user-guide/
- Mockito: https://site.mockito.org/
- Jest: https://jestjs.io/docs/getting-started
- Vitest: https://vitest.dev/guide/
- Playwright: https://playwright.dev/docs/intro
- Cypress: https://docs.cypress.io/
- Postman Learning Center: https://learning.postman.com/
- Apache JMeter: https://jmeter.apache.org/usermanual/
- SonarQube: https://docs.sonarsource.com/sonarqube/
- W3C WCAG: https://www.w3.org/TR/WCAG22/
- ISO catalogue: https://www.iso.org/standards.html
- CMMI: https://cmmiinstitute.com/

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se ejecutaron suites ni pruebas de carga en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 17

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados orientan el estudio de los conceptos dentro de la guía y el proyecto de la etapa; no constituyen resultados de pruebas ni evidencias de implementación.

### Módulo 17.1 — Fundamentos

#### 17.1.01 — Quality Assurance (QA)
Quality Assurance (QA) agrupa actividades preventivas y de proceso destinadas a reducir defectos y mejorar cómo se construye el software. Incluye estándares, revisiones, automatización y mejora continua; no es sinónimo de ejecutar pruebas al final.

#### 17.1.02 — Quality Control (QC)
Quality Control (QC) evalúa entregables para detectar desviaciones respecto de requisitos y criterios. Puede incluir inspecciones y pruebas; registra evidencia, severidad y trazabilidad en vez de limitarse a declarar que algo funciona.

#### 17.1.03 — Verificación
Verificación pregunta si el producto se construye conforme a especificaciones y diseño. Utiliza revisiones, análisis estático y pruebas sobre requisitos definidos; puede descubrir defectos sin demostrar que el producto resuelve la necesidad real del usuario.

#### 17.1.04 — Validación
Validación comprueba si el producto satisface necesidades y uso previsto de sus usuarios. Requiere escenarios representativos y criterios de aceptación; una implementación técnicamente conforme puede fallar la validación si el requisito estaba equivocado.

#### 17.1.05 — Defectos
Un defecto es una condición en un artefacto que puede provocar un resultado incorrecto o incumplimiento. Documenta pasos de reproducción, entorno, resultado esperado/obtenido, impacto y evidencia para permitir diagnóstico.

#### 17.1.06 — Bugs
Bug es el término habitual para un defecto observado en software, aunque el vocabulario puede variar entre equipos. Prioriza según impacto, probabilidad, exposición y consecuencias; no confundas cantidad de bugs reportados con calidad global.

#### 17.1.07 — Casos de prueba
Un caso de prueba define precondiciones, datos, acciones y resultados esperados para comprobar un comportamiento. Incluye escenarios positivos, negativos, límites y permisos; cada expectativa debe ser observable y trazable a un requisito.

### Módulo 17.2 — Testing funcional

#### 17.2.01 — Unit Testing
Unit Testing comprueba una unidad pequeña de comportamiento con dependencias controladas. Debe ser rápida y determinista, y verificar resultados y efectos relevantes sin probar detalles internos que puedan cambiar sin alterar el contrato.

#### 17.2.02 — Integration Testing
Integration Testing verifica interacción entre componentes reales, por ejemplo servicio y base de datos. Controla entorno, datos y limpieza; una prueba de integración detecta fallos de configuración, consultas, serialización y límites entre módulos.

#### 17.2.03 — End-to-End Testing
End-to-End Testing recorre un flujo representativo desde la interfaz o entrada externa hasta el resultado final. Mantén pocos escenarios críticos, datos aislados y observabilidad; las suites E2E suelen ser más lentas y frágiles que pruebas unitarias.

#### 17.2.04 — Regression Testing
Regression Testing vuelve a ejecutar pruebas para comprobar que cambios no rompan comportamientos existentes. Selecciona casos según riesgo e impacto y conserva pruebas para defectos corregidos, evitando una suite extensa sin mantenimiento.

#### 17.2.05 — Smoke Testing
Smoke Testing ejecuta un conjunto pequeño de comprobaciones esenciales para saber si un build o entorno merece pruebas más profundas. Verifica arranque, rutas críticas y dependencias básicas; no equivale a validar todas las funciones.

#### 17.2.06 — Sanity Testing
Sanity Testing realiza una comprobación acotada de una modificación o área concreta después de un cambio. Define alcance y criterio de aprobación, y no lo confundas con una prueba exhaustiva de regresión.

#### 17.2.07 — API Testing
API Testing comprueba contratos, autenticación, validación, errores, límites y comportamiento de endpoints. Incluye entradas inválidas, autorización por recurso, paginación y concurrencia; no te limites a verificar que la respuesta sea HTTP 200.

### Módulo 17.3 — Testing de usuario

#### 17.3.01 — Usability Testing
Usability Testing observa si usuarios representativos pueden completar tareas con eficacia, eficiencia y satisfacción. Define tareas y métricas antes de la sesión, registra dificultades sin guiar al participante y protege su información personal.

#### 17.3.02 — Accessibility Testing
Accessibility Testing combina evaluación automatizada, inspección manual, teclado y tecnologías de asistencia. Comprueba criterios WCAG aplicables y documenta evidencia; ningún escáner automático por sí solo demuestra conformidad.

#### 17.3.03 — Exploratory Testing
Exploratory Testing combina aprendizaje, diseño y ejecución de pruebas durante la exploración del producto. Usa charters y notas para mantener foco, registra condiciones de reproducción y complementa las pruebas automatizadas.

#### 17.3.04 — User Acceptance Testing (UAT)
User Acceptance Testing (UAT) valida que los flujos cumplen criterios de aceptación desde la perspectiva del negocio o usuario. Define responsables, datos y condiciones de aprobación antes de ejecutar; UAT no reemplaza pruebas técnicas ni de seguridad.

### Módulo 17.4 — Rendimiento

#### 17.4.01 — Load Testing
Load Testing mide el comportamiento bajo una carga esperada o proyectada. Define usuarios concurrentes, tasa de llegada, duración y mezcla de operaciones; compara latencia, throughput y errores con objetivos de servicio.

#### 17.4.02 — Stress Testing
Stress Testing aumenta la carga más allá del nivel normal para descubrir límites y comportamiento ante saturación. Comprueba degradación controlada, recuperación y protección de dependencias; ejecútalo solo en entornos autorizados y aislados.

#### 17.4.03 — Spike Testing
Spike Testing aplica incrementos bruscos de carga para evaluar escalado, colas y recuperación. Observa capacidad de absorción y tiempo de estabilización, no solo el pico máximo alcanzado.

#### 17.4.04 — Endurance Testing
Endurance Testing mantiene una carga sostenida durante un periodo prolongado para descubrir fugas, degradación y acumulación de recursos. Registra tendencias y condiciones ambientales y evita extrapolar resultados de una ejecución breve.

#### 17.4.05 — Response Time
Response Time mide el intervalo entre solicitud y respuesta desde un punto de observación definido. Distingue tiempo total, tiempo de servidor y tiempo de cliente, y reporta percentiles además del promedio.

#### 17.4.06 — Throughput
Throughput expresa cuántas operaciones o unidades de trabajo se completan por unidad de tiempo. Interprétalo junto con latencia y tasa de error; un throughput alto no es útil si produce respuestas incorrectas.

#### 17.4.07 — Latency
Latency mide el retraso entre una acción y su efecto observable. Identifica componentes de red, cola, procesamiento y almacenamiento; utiliza percentiles como p95/p99 para comprender experiencias de cola larga.

#### 17.4.08 — Bottlenecks
Un bottleneck es un recurso o etapa que limita el rendimiento total del sistema. Formula hipótesis y mide CPU, memoria, I/O, red y locks antes de optimizar; aumentar capacidad en otro componente puede no mejorar el resultado.

### Módulo 17.5 — Testing técnico

#### 17.5.01 — Test Cases
Test Cases son especificaciones ejecutables o manuales de escenarios, entradas y resultados esperados. Mantén cada caso enfocado, repetible y vinculado a un requisito o riesgo.

#### 17.5.02 — Assertions
Assertions comparan el resultado real con una condición esperada y hacen fallar la prueba si no se cumple. Asegúrate de que la aserción compruebe el comportamiento relevante y no solo la existencia de un valor.

#### 17.5.03 — Mocking
Mocking sustituye una dependencia por una implementación controlada para simular respuestas o fallos. Úsalo para aislar límites externos, pero no simules tanto que la prueba deje de detectar errores de integración.

#### 17.5.04 — Fixtures
Fixtures preparan datos y estado necesarios para una prueba y definen su ciclo de vida. Mantén fixtures pequeños y legibles, evita dependencia entre pruebas y limpia recursos aun cuando ocurra un fallo.

#### 17.5.05 — Test Doubles
Test Doubles son sustitutos de dependencias, como mocks, stubs, fakes y spies, con propósitos distintos. Elige el doble según la interacción que deseas controlar y evita acoplar las pruebas a llamadas internas irrelevantes.

#### 17.5.06 — Test Coverage
Test Coverage mide qué partes del código o condiciones fueron ejecutadas por una suite. No demuestra calidad ni corrección: complementa la cobertura con aserciones significativas, casos límite y análisis de riesgo.

#### 17.5.07 — Test Isolation
Test Isolation evita que una prueba dependa del orden, estado o efectos de otra. Usa datos únicos, recursos temporales y limpieza fiable; la ejecución paralela debe producir resultados equivalentes a la ejecución aislada.

### Módulo 17.6 — Metodologías

#### 17.6.01 — TDD
TDD desarrolla mediante ciclos pequeños de prueba fallida, implementación mínima y refactorización. La prueba define comportamiento esperado; evita escribir pruebas que solo confirmen la implementación actual y refactoriza manteniendo la suite verde.

#### 17.6.02 — BDD
BDD describe comportamiento mediante ejemplos comprensibles para negocio y equipo técnico. Escenarios Given/When/Then deben expresar reglas observables y evitar convertirse en scripts de interfaz frágiles o en documentación que nadie mantiene.

#### 17.6.03 — AAA (Arrange, Act, Assert)
AAA organiza una prueba en Arrange (preparar), Act (ejecutar) y Assert (verificar). Mantén cada fase clara y una acción principal por prueba para que el fallo revele rápidamente qué comportamiento no se cumple.

#### 17.6.04 — Pirámide de testing
La pirámide de testing propone muchas pruebas unitarias, una cantidad menor de integración y pocas E2E, como heurística de coste y velocidad. Ajusta la distribución al riesgo y arquitectura; no es una proporción universal obligatoria.

### Módulo 17.7 — Herramientas

#### 17.7.01 — JUnit
JUnit es un framework de pruebas para Java con anotaciones, assertions, lifecycle y extensiones. Fija versión, organiza pruebas por comportamiento y evita compartir estado mutable entre casos.

#### 17.7.02 — Mockito
Mockito crea dobles de prueba para dependencias Java y permite verificar interacciones. Mockea límites externos, no cada clase interna; combina mocks con pruebas de integración para comprobar configuración y contratos reales.

#### 17.7.03 — Jest
Jest ejecuta pruebas JavaScript/TypeScript con assertions, mocks y cobertura. Configura entorno y transformaciones de acuerdo con el proyecto y evita mocks globales que oculten efectos secundarios o dependencias no declaradas.

#### 17.7.04 — Vitest
Vitest ofrece un runner integrado con herramientas modernas como Vite y soporte para pruebas unitarias y de componentes. Alinea configuración con el build, aísla módulos y comprueba compatibilidad con el entorno de ejecución elegido.

#### 17.7.05 — Playwright
Playwright automatiza navegadores para pruebas E2E y de interacción. Usa locators accesibles, espera condiciones observables y captura trazas; evita pausas fijas y datos compartidos que vuelvan inestable la suite.

#### 17.7.06 — Cypress
Cypress permite probar aplicaciones web desde el navegador con comandos encadenados y herramientas de depuración. Controla estado y red, separa pruebas de componente y E2E y evita depender de detalles visuales frágiles.

#### 17.7.07 — Postman
Postman permite ejecutar colecciones de solicitudes y assertions sobre APIs. Versiona casos reproducibles, utiliza datos no sensibles y comprueba errores y permisos, no solo respuestas exitosas.

#### 17.7.08 — JMeter
JMeter genera carga y mide comportamiento de aplicaciones y servicios mediante planes de prueba. Diseña perfiles realistas, controla recursos del generador y limita las pruebas a entornos autorizados para no afectar producción.

### Módulo 17.8 — Análisis de calidad

#### 17.8.01 — Static Analysis
Static Analysis examina código sin ejecutar el programa para detectar defectos potenciales, complejidad y patrones riesgosos. Ajusta reglas al lenguaje y contexto, revisa falsos positivos y utiliza hallazgos para priorizar mejoras.

#### 17.8.02 — Linters
Linters detectan patrones problemáticos y aplican convenciones de código. Fija configuración compartida y ejecuta reglas en CI; no conviertas warnings en errores sin acordar el criterio con el equipo.

#### 17.8.03 — Formatters
Formatters aplican formato consistente sin cambiar intencionalmente la lógica del programa. Automatiza el formato y separa su función del linting, análisis estático y revisión de calidad.

#### 17.8.04 — SonarQube
SonarQube centraliza análisis estático, métricas y Quality Gates para proyectos compatibles. Configura perfiles y umbrales adecuados, revisa falsos positivos y no interpretes un gate aprobado como garantía de ausencia de vulnerabilidades.

#### 17.8.05 — Code Coverage
Code Coverage informa qué líneas, ramas o funciones fueron alcanzadas por pruebas. Analiza cobertura de ramas y casos críticos, pero exige aserciones y revisión de escenarios; aumentar el porcentaje sin pruebas significativas no mejora necesariamente calidad.

#### 17.8.06 — Code Smells
Code Smells son señales de diseño que pueden indicar complejidad, duplicación o responsabilidades mal distribuidas. No son defectos automáticos: analiza contexto, coste de cambio y riesgo antes de refactorizar.

### Módulo 17.9 — Normas y modelos de calidad

#### 17.9.01 — ISO/IEC 25010
ISO/IEC 25010 define un modelo de calidad de producto y calidad en uso mediante características y subcaracterísticas. Consulta la edición vigente y utiliza el modelo para especificar atributos medibles, no como una certificación automática del software.

#### 17.9.02 — ISO/IEC/IEEE 12207
ISO/IEC/IEEE 12207 describe procesos del ciclo de vida del software, desde adquisición y desarrollo hasta operación y mantenimiento. Úsala para organizar responsabilidades y evidencias según alcance; no confundas adoptar procesos con certificar un producto.

#### 17.9.03 — CMMI
CMMI es un conjunto de modelos de mejora de capacidades y desempeño organizacional. Interpreta sus prácticas según el modelo y alcance aplicables; no lo presentes como una lista universal de pruebas para un proyecto individual.

#### 17.9.04 — Indicadores de calidad
Los indicadores de calidad convierten objetivos en medidas observables, como defectos escapados, tiempo de recuperación o cobertura de requisitos. Define fórmula, fuente, periodicidad y límites para evitar métricas que incentiven comportamientos contraproducentes.

#### 17.9.05 — Mantenibilidad
Mantenibilidad es la facilidad con que un sistema puede modificarse, corregirse, probarse y comprenderse. Evalúa modularidad, complejidad, documentación y deuda técnica mediante evidencias, no solo por estilo de código.

#### 17.9.06 — Fiabilidad
Fiabilidad es la capacidad de operar sin fallos durante un periodo y contexto definidos. Mide disponibilidad, tasa de fallos, recuperación y comportamiento ante errores; especifica carga y entorno para que el indicador sea interpretable.

#### 17.9.07 — Seguridad
Seguridad como atributo de calidad exige proteger confidencialidad, integridad, disponibilidad y controles de acceso según amenazas. Integra requisitos de seguridad, pruebas y gestión de vulnerabilidades durante todo el ciclo de vida.

#### 17.9.08 — Rendimiento
Rendimiento evalúa tiempos de respuesta, capacidad y uso de recursos bajo condiciones definidas. Establece objetivos por percentiles y perfiles de carga, y relaciona resultados con experiencia del usuario y coste de infraestructura.

#### 17.9.09 — Usabilidad
Usabilidad evalúa si usuarios específicos pueden alcanzar objetivos con eficacia, eficiencia y satisfacción en un contexto. Combina observación, métricas y accesibilidad; no infieras facilidad de uso solo desde la opinión del equipo desarrollador.

#### 17.9.10 — Product quality model
Product quality model organiza características que permiten especificar y evaluar la calidad del producto. Relaciona cada atributo con requisitos y medidas verificables y declara límites de evaluación; el modelo no reemplaza criterios de aceptación propios del sistema.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 61 orientaciones genéricas por explicaciones específicas de cada entrada. Se desarrollaron QA/QC, verificación/validación, pruebas funcionales y de usuario, rendimiento, dobles de prueba, TDD/BDD, herramientas, análisis estático e indicadores/modelos de calidad.

**Revisión interna:** 61/61 entradas desarrolladas y cotejadas con el roadmap. Se aclaró que cobertura no equivale a calidad, que smoke/sanity/regresión tienen alcances distintos y que estándares/modelos no certifican automáticamente un producto. Pendiente: ejecutar suites en proyectos de referencia, validar perfiles de carga en infraestructura aislada, revisar versiones de herramientas y verificar métricas/umbrales con un segundo evaluador. No se declara ejecución ni aprobación externa.
