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
