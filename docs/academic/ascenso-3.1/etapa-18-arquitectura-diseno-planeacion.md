# Etapa 18 — Arquitectura, diseño y planeación de software

**Prioridad:** P1 · Obligatoria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** aprender a planear y diseñar sistemas antes de comenzar a programar.  
**Proyecto oficial:** recibir un problema empresarial, analizarlo, documentarlo, modelarlo, diseñar su arquitectura y elaborar un plan de trabajo antes de escribir código.

## Resultados de aprendizaje
Convertir necesidades en requisitos verificables; organizar trabajo ágil; documentar decisiones; modelar estructura y comportamiento; aplicar principios y patrones con criterio; comparar arquitecturas; razonar sobre sistemas distribuidos; modelar dominios; y trabajar mediante especificaciones proporcionales al riesgo.

## 18.1 — Análisis de requerimientos
Los requisitos funcionales describen capacidades o comportamientos. Los no funcionales expresan cualidades, restricciones o condiciones medibles, por ejemplo latencia, disponibilidad, seguridad, accesibilidad o mantenibilidad. Evita requisitos vagos como “rápido”, “seguro” o “fácil”: define escenario, métrica, umbral y contexto.

Historias de usuario expresan necesidad desde una perspectiva; casos de uso describen actores, condiciones y flujos. Criterios de aceptación hacen verificable el resultado. Reglas de negocio definen políticas del dominio; restricciones limitan diseño o implementación. Stakeholders son personas o grupos afectados o con interés legítimo. Define alcance, exclusiones, supuestos, dependencias y riesgos.

**Ejercicio:** transforma una petición ambigua de inventario en requisitos funcionales y no funcionales, historias, casos de uso y criterios comprobables.

## 18.2 — Metodologías ágiles
El Manifiesto Ágil expresa valores y principios; no prescribe una herramienta ni elimina planificación. Scrum organiza trabajo mediante responsabilidades, eventos y artefactos definidos. Kanban visualiza flujo, limita trabajo en progreso (WIP) y busca mejorar entrega continua.

Comprende Product Backlog, Sprint Backlog, Planning, Daily Scrum, Review, Retrospective y Definition of Done. Story Points son una técnica relativa de estimación, no horas universales ni medida individual de productividad. WIP limita tareas simultáneas y ayuda a detectar cuellos de botella.

**Ejercicio:** crea un backlog priorizado, divide una historia en tareas, define DoD y simula un flujo Kanban con límite WIP.

## 18.3 — Documentación
README explica propósito, requisitos, instalación, configuración, ejecución, pruebas y limitaciones. La especificación de requisitos conserva alcance y trazabilidad. Documentación técnica explica arquitectura y operación; funcional describe capacidades y reglas. API Documentation debe reflejar el contrato real. ADR registra una decisión, contexto, opciones, decisión y consecuencias. Changelog documenta cambios relevantes.

Incluye manual de instalación, usuario, pruebas y despliegue cuando el producto lo requiera. La documentación debe actualizarse junto al código y diferenciar lo implementado, probado y planificado.

**Ejercicio:** escribe un ADR que compare monolito modular y microservicios para una aplicación pequeña; registra consecuencias y condiciones que podrían hacer revisar la decisión.

## 18.4 — Diagramas
Usa diagramas de flujo para procesos; UML para estructura y comportamiento; clases para tipos y relaciones; secuencia para mensajes en el tiempo; actividades para flujos; componentes para módulos y dependencias; despliegue para nodos y artefactos; ER para datos. C4 modela contexto, contenedores, componentes y código con niveles distintos de detalle.

Un diagrama debe responder una pregunta y declarar límites. Evita diagramas ornamentales sin relación con decisiones. Mantén coherencia entre diagramas y sistema real.

**Ejercicio:** modela el sistema de ventas con contexto C4, contenedores, secuencia de venta y ER.

## 18.5 — Principios de diseño
- **SOLID:** cinco principios para organizar responsabilidades, extensibilidad y dependencias; no son reglas mecánicas.
- **DRY:** evita duplicación de conocimiento que debería tener una única fuente; no abstraigas coincidencias accidentales.
- **KISS:** favorece soluciones simples que satisfagan requisitos.
- **YAGNI:** no construyas capacidades especulativas sin necesidad demostrable.
- **Separation of Concerns:** separa aspectos con motivos de cambio distintos.
- **High Cohesion / Low Coupling:** agrupa responsabilidades relacionadas y reduce dependencias innecesarias.
- **Dependency Inversion:** políticas de alto nivel no deben depender directamente de detalles; ambos deben depender de abstracciones apropiadas.

Evalúa coste de abstracción, testabilidad y complejidad. Una interfaz para cada clase no garantiza buen diseño.

## 18.6 — Patrones GoF
Los patrones describen soluciones recurrentes en contextos específicos; no son recetas obligatorias.

**Creacionales:** Factory, Abstract Factory, Builder, Singleton y Prototype. Estudia qué problema de creación resuelven, cómo afectan acoplamiento y pruebas y qué alternativas ofrece el lenguaje/framework.

**Estructurales:** Adapter, Decorator, Facade, Proxy, Composite, Bridge y Flyweight. Compara adaptación de interfaces, composición, acceso indirecto, simplificación y uso compartido.

**Comportamiento:** Strategy, Observer, Command, State, Iterator, Mediator, Template Method y Chain of Responsibility. Identifica cómo distribuyen decisiones, mensajes y responsabilidades.

**Ejercicio:** elige tres patrones para escenarios distintos, implementa ejemplos pequeños y documenta cuándo sería mejor no utilizarlos.

## 18.7 — Arquitecturas
- Monolítica: una unidad principal de despliegue; puede ser modular internamente.
- Monolito modular: módulos con límites y dependencias controlados en un despliegue coordinado.
- Layered: separa presentación, aplicación, dominio y persistencia según diseño.
- MVC: separa modelo, vista y controlador en contextos apropiados.
- Clean Architecture: centra reglas de negocio y controla dirección de dependencias.
- Hexagonal: organiza puertos y adaptadores alrededor del núcleo.
- Onion: capas concéntricas con dominio en el centro.
- Event-Driven: componentes reaccionan a eventos; exige contratos, idempotencia y observabilidad.
- Microservices: servicios autónomos con despliegue y datos/contratos distribuidos; añade complejidad operacional.

No confundas patrones de arquitectura con frameworks. Selecciona según equipo, escala, dominio, operación y requisitos; un monolito bien modularizado puede ser la decisión más adecuada.

## 18.8 — Diseño de sistemas
Razonar sobre scalability, availability, reliability, consistency y fault tolerance exige escenarios y métricas. CAP se refiere al compromiso bajo particiones en sistemas distribuidos; no es una clasificación simplista de bases de datos. Load balancing distribuye carga; caching reduce trabajo a cambio de invalidación y frescura; message queues desacoplan procesos; distributed systems deben gestionar fallos parciales, latencia y duplicados. API Gateway concentra políticas de entrada; service discovery permite localizar servicios.

**Ejercicio:** diseña un servicio de pedidos para carga creciente. Identifica cuellos de botella, puntos únicos de fallo, estrategia de caché, cola y comportamiento ante indisponibilidad de un servicio.

## 18.9 — Modelado de dominios
Domain-Driven Design (DDD) centra el diseño en el dominio y su lenguaje. Entity posee identidad; Value Object se define por sus valores; Aggregate agrupa invariantes y establece una raíz; Repository abstrae persistencia de agregados; Bounded Context define límites donde un modelo y lenguaje tienen significado coherente; Ubiquitous Language alinea vocabulario entre especialistas y equipo técnico.

No conviertas cada tabla en agregado ni cada entidad en microservicio. Modela invariantes, transacciones y límites del contexto antes de decidir estructura de código.

## Ampliación metodológica — SDD (Spec-Driven Development)
El desarrollo guiado por especificaciones comienza por definir problema, usuarios, alcance y reglas. Escribe requisitos funcionales/no funcionales, historias y criterios verificables; modela datos, módulos, responsabilidades, interfaces y decisiones; divide la especificación en tareas y dependencias; implementa respetándola y registra cambios; crea pruebas para criterios de aceptación; mantiene trazabilidad requisito-código-prueba.

La especificación debe ser proporcional al tamaño y riesgo: breve para una práctica pequeña, más rigurosa para un sistema empresarial. SDD no significa producir documentos extensos antes de cada ejercicio ni reemplaza el juicio de ingeniería.

## Proyecto oficial — Diseño de un sistema empresarial
Antes de programar, entrega:
1. Problema, usuarios, stakeholders y alcance.
2. Requisitos funcionales y no funcionales verificables.
3. Historias, casos de uso y criterios de aceptación.
4. Reglas de negocio, restricciones y riesgos.
5. Modelo de dominio y lenguaje ubicuo.
6. Modelo ER y diagramas UML/C4 pertinentes.
7. Comparación de al menos dos arquitecturas con ADR.
8. Patrones justificados por necesidad concreta.
9. Backlog priorizado, tareas, dependencias y Definition of Done.
10. Plan de pruebas vinculado a requisitos.
11. Especificación técnica y plan de implementación.
12. Revisión de consistencia entre documentos.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Requisitos, alcance y criterios | 15 |
| Método ágil y planificación | 10 |
| Documentación y ADR | 10 |
| Diagramas y modelado | 15 |
| Principios y patrones | 15 |
| Selección de arquitectura | 15 |
| Diseño de sistemas y resiliencia | 10 |
| DDD y SDD | 10 |

Criterio orientativo: 80/100 y trazabilidad entre problema, requisitos, diseño y pruebas.

## Autoevaluación
1. ¿Cómo conviertes un requisito no funcional en verificable?
2. Diferencia historia de usuario y caso de uso.
3. ¿Qué limita WIP?
4. ¿Qué debe contener un ADR?
5. ¿Qué pregunta responde un diagrama de secuencia?
6. ¿Por qué DRY no significa eliminar toda repetición?
7. ¿Cuándo un monolito modular es preferible a microservicios?
8. ¿Qué problema resuelve un Aggregate?
9. ¿Qué significa bounded context?
10. ¿Cómo se relacionan especificación, implementación y pruebas en SDD?

## Recursos audiovisuales
No se incluyen videos aprobados. Se incorporarán únicamente con audio hablado en español y correspondencia directa con el subtema: requisitos, Scrum/Kanban, UML/C4, patrones, arquitectura o DDD. No se usarán charlas generales como sustituto de explicación técnica.

## Referencias oficiales y técnicas
- Agile Manifesto: https://agilemanifesto.org/
- Scrum Guide: https://scrumguides.org/
- Kanban Guide: https://kanbanguides.org/
- OMG UML: https://www.omg.org/spec/UML/
- C4 Model: https://c4model.com/
- ISO Systems and software engineering standards: https://www.iso.org/committee/45086.html
- Martin Fowler — Architecture: https://martinfowler.com/architecture/
- Microsoft Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/
- Domain-Driven Design Community: https://www.domainlanguage.com/
- ADR GitHub: https://adr.github.io/

**Consulta documental:** 2026-11-19. **Verificación práctica:** proyecto de diseño no implementado ni validado en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 18

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados orientan el estudio de los conceptos dentro de la guía y el proyecto de la etapa; no constituyen resultados de pruebas ni evidencias de implementación.

### Módulo 18.1 — Análisis de requerimientos

#### 18.1.01 — Requerimientos funcionales
Los requerimientos funcionales describen capacidades y comportamientos que el sistema debe ofrecer. Redáctalos con actor, acción, condición y resultado observable; cada requisito debe poder relacionarse con criterios de aceptación y pruebas.


**Práctica y evidencia:** Redacta requisitos funcionales para crear y consultar pedidos con actores y resultados observables. **Evidencia:** cada requisito puede verificarse mediante un escenario.

#### 18.1.02 — No funcionales
Los requerimientos no funcionales expresan atributos y restricciones como rendimiento, seguridad, disponibilidad, accesibilidad y mantenibilidad. Cuantifícalos con umbrales, contexto y método de medición; «rápido» o «seguro» no son criterios verificables por sí solos.


**Práctica y evidencia:** Define requisitos no funcionales medibles de rendimiento, seguridad, disponibilidad y accesibilidad. **Evidencia:** sustituye adjetivos vagos por umbrales, condiciones y método de medición.

#### 18.1.03 — Historias de usuario
Una historia de usuario comunica una necesidad desde la perspectiva de un actor y el valor esperado. Acompáñala con criterios de aceptación, reglas y dependencias; la plantilla «Como/quiero/para» no reemplaza el análisis.


**Práctica y evidencia:** Escribe historias de usuario con actor, necesidad y valor y añade criterios de aceptación. **Evidencia:** demuestra que una historia puede dividirse en tareas sin perder el resultado del usuario.

#### 18.1.04 — Casos de uso
Un caso de uso describe interacciones entre actores y sistema para alcanzar un objetivo, incluyendo flujo principal y alternativas. Registra precondiciones, postcondiciones y excepciones para descubrir comportamientos que una historia breve podría omitir.


**Práctica y evidencia:** Modela un caso de uso de compra con flujo principal, alternos y excepciones. **Evidencia:** identifica actor, precondición, postcondición y límites del sistema.

#### 18.1.05 — Reglas de negocio
Las reglas de negocio expresan políticas, cálculos, permisos y restricciones propias del dominio. Distingue reglas del negocio de decisiones técnicas y define fuente de autoridad, prioridad y tratamiento de excepciones.


**Práctica y evidencia:** Extrae reglas de negocio para inventario y descuentos y exprésalas sin depender de una interfaz. **Evidencia:** prueba casos válidos, inválidos y fronteras.

#### 18.1.06 — Restricciones
Las restricciones limitan soluciones posibles por tecnología, presupuesto, normativa, plazo, infraestructura o compatibilidad. Registra su origen y si son obligatorias o negociables; una restricción no documentada puede convertirse en riesgo de diseño.


**Práctica y evidencia:** Registra restricciones técnicas, legales, presupuestales y de operación. **Evidencia:** clasifica cuáles son obligatorias y cuáles son decisiones negociables.

#### 18.1.07 — Stakeholders
Stakeholders son personas u organizaciones que influyen en el sistema o reciben sus efectos. Identifica necesidades, autoridad, conflictos y canales de decisión; no asumas que una sola persona representa a todos los usuarios.


**Práctica y evidencia:** Identifica stakeholders, intereses, influencia y necesidades de información. **Evidencia:** construye una matriz y define cómo gestionar conflictos.

#### 18.1.08 — Alcance del proyecto
El alcance define qué incluye y excluye el proyecto, sus entregables y límites. Documenta supuestos, exclusiones y criterios de cambio para prevenir expansión no controlada y desacuerdos sobre el resultado esperado.


**Práctica y evidencia:** Define alcance incluido/excluido, entregables y supuestos del proyecto. **Evidencia:** redacta una declaración de alcance que permita rechazar solicitudes fuera de objetivo.

### Módulo 18.2 — Metodologías ágiles

#### 18.2.01 — Manifiesto Ágil
El Manifiesto Ágil expresa valores y principios para desarrollar software de forma adaptativa y colaborativa. Interprétalo como orientación para decisiones y aprendizaje, no como ausencia de planificación, documentación o control.


**Práctica y evidencia:** Compara los valores y principios del Manifiesto Ágil con un proceso de trabajo concreto. **Evidencia:** explica qué significa responder al cambio sin abandonar planificación.

#### 18.2.02 — Scrum
Scrum es un marco de trabajo con responsabilidades, eventos y artefactos definidos. Comprende Product Owner, Scrum Master y Developers, y adapta el marco con transparencia; no conviertas los eventos en reuniones sin propósito ni inspección.


**Práctica y evidencia:** Simula un Sprint Scrum con objetivo, backlog, eventos y revisión. **Evidencia:** distingue responsabilidades y no convierte Daily en reporte al jefe.

#### 18.2.03 — Kanban
Kanban visualiza el flujo de trabajo y limita trabajo en progreso para mejorar entrega y detectar cuellos de botella. Define políticas explícitas y mide tiempo de ciclo y throughput, no solo cantidad de tareas en columnas.


**Práctica y evidencia:** Diseña un tablero Kanban con estados, políticas explícitas y límites WIP. **Evidencia:** identifica bloqueos y mide tiempo de ciclo.

#### 18.2.04 — Sprints
Un Sprint es un periodo fijo en Scrum para crear un incremento de valor utilizable. Define objetivo y duración consistente, y ajusta alcance mediante colaboración sin comprometer el objetivo del Sprint.


**Práctica y evidencia:** Formula un Sprint Goal y selecciona trabajo que pueda terminarse dentro del Sprint. **Evidencia:** demuestra coherencia entre objetivo y elementos seleccionados.

#### 18.2.05 — Product Backlog
Product Backlog es una lista ordenada y evolutiva del trabajo necesario para mejorar el producto. Refina elementos con criterios y valor, manteniendo transparencia sobre prioridad, incertidumbre y dependencias.


**Práctica y evidencia:** Ordena un Product Backlog por valor, riesgo y dependencias. **Evidencia:** justifica prioridad y criterios de refinamiento.

#### 18.2.06 — Sprint Backlog
Sprint Backlog reúne el objetivo del Sprint, elementos seleccionados y plan de trabajo de Developers. Se actualiza conforme se aprende y no debe convertirse en una lista rígida de tareas impuesta externamente.


**Práctica y evidencia:** Descompón el objetivo de Sprint en tareas y plan de entrega. **Evidencia:** cada elemento tiene resultado observable y estimación razonada.

#### 18.2.07 — Planning
Planning establece por qué el Sprint es valioso, qué puede completarse y cómo se realizará el trabajo. Participan quienes corresponda según Scrum; el resultado debe ser un objetivo claro y un plan adaptativo.


**Práctica y evidencia:** Realiza una Planning con capacidad real, objetivo y selección de backlog. **Evidencia:** documenta supuestos y evita compromiso basado solo en velocidad histórica.

#### 18.2.08 — Daily
Daily Scrum es una oportunidad breve para inspeccionar progreso hacia el objetivo y adaptar el plan. No es un reporte de estatus al gerente ni una obligación de responder siempre tres preguntas idénticas.


**Práctica y evidencia:** Simula una Daily breve enfocada en progreso hacia objetivo y adaptación del plan. **Evidencia:** identifica impedimento y acción concreta.

#### 18.2.09 — Review
Review inspecciona el incremento y obtiene retroalimentación de stakeholders para adaptar el Product Backlog. Presenta software funcional y resultados reales; no la conviertas en una demostración preparada que oculte limitaciones.


**Práctica y evidencia:** Prepara una Review con incremento funcional y feedback de stakeholders. **Evidencia:** separa inspección del producto de aprobación formal del Sprint.

#### 18.2.10 — Retrospective
Retrospective analiza cómo mejorar calidad y efectividad del equipo, procesos y herramientas. Acuerda acciones pequeñas con responsable y seguimiento; evita buscar culpables o producir listas que nunca se implementan.


**Práctica y evidencia:** Conduce una retrospectiva basada en datos y selecciona una mejora pequeña. **Evidencia:** define responsable y señal para comprobar impacto en el siguiente ciclo.

#### 18.2.11 — Definition of Done
Definition of Done establece criterios compartidos para considerar un incremento terminado y con calidad suficiente. Incluye pruebas, revisión, documentación y controles aplicables; no debe confundirse con criterios de aceptación de una historia específica.


**Práctica y evidencia:** Define una Definition of Done con calidad, pruebas, seguridad y documentación. **Evidencia:** verifica un incremento contra cada criterio antes de considerarlo terminado.

#### 18.2.12 — Story Points
Story Points son una técnica relativa de estimación de esfuerzo/complexidad/incertidumbre, no horas ni productividad individual. Úsalos solo si ayudan a planificar y nunca para comparar personas o convertir velocidad en objetivo.


**Práctica y evidencia:** Estima esfuerzo relativo con story points mediante comparación y discusión de incertidumbre. **Evidencia:** explica por qué puntos no equivalen a horas ni sirven para comparar equipos.

#### 18.2.13 — Gestión del trabajo en progreso (WIP)
WIP limita cuántos elementos pueden estar en progreso simultáneamente. Establece límites según capacidad y observa bloqueos; reducir multitarea puede mejorar flujo, pero el límite debe revisarse con datos y contexto.


**Práctica y evidencia:** Limita trabajo en progreso y observa efecto sobre flujo y bloqueos. **Evidencia:** compara lead time/cycle time antes y después de una política WIP.

### Módulo 18.3 — Documentación

#### 18.3.01 — README
README explica propósito, requisitos, instalación, configuración, ejecución y contribución de un repositorio. Mantén instrucciones probadas y coherentes con el estado real; nunca incluyas secretos ni instrucciones que requieran permisos no documentados.


**Práctica y evidencia:** Escribe un README con propósito, requisitos, instalación, ejecución y contribución. **Evidencia:** otra persona puede iniciar el proyecto siguiendo solo el documento.

#### 18.3.02 — Especificación de requisitos
La especificación de requisitos documenta funciones, calidad, interfaces, restricciones y criterios de aceptación. Mantén identificadores, versiones y trazabilidad hacia diseño y pruebas para gestionar cambios sin perder contexto.


**Práctica y evidencia:** Crea una especificación de requisitos trazable a historias, reglas y pruebas. **Evidencia:** detecta requisitos ambiguos y conflictos.

#### 18.3.03 — Documentación técnica
La documentación técnica explica arquitectura, componentes, contratos, decisiones y operación para desarrolladores y operadores. Debe responder cómo funciona el sistema y qué límites tiene, no duplicar comentarios obvios del código.


**Práctica y evidencia:** Documenta arquitectura, dependencias, decisiones y operación técnica. **Evidencia:** un desarrollador nuevo puede ubicar componentes y puntos de extensión.

#### 18.3.04 — Documentación funcional
La documentación funcional describe capacidades desde el punto de vista del usuario y las reglas del negocio. Usa lenguaje del dominio, flujos y excepciones verificables para que negocio, QA y desarrollo compartan interpretación.


**Práctica y evidencia:** Describe flujos funcionales, roles y reglas de negocio para usuarios y analistas. **Evidencia:** cada flujo enlaza con un requisito y criterio de aceptación.

#### 18.3.05 — API Documentation
API Documentation describe endpoints, esquemas, autenticación, errores, límites y ejemplos. Genera o valida documentación desde contratos versionados y evita publicar credenciales o datos reales en ejemplos.


**Práctica y evidencia:** Documenta endpoints con esquema, autenticación, ejemplos, errores y límites. **Evidencia:** un consumidor puede reproducir una solicitud sin consultar el código.

#### 18.3.06 — Architecture Decision Records (ADR)
Architecture Decision Records (ADR) registran contexto, decisión, alternativas y consecuencias de una decisión arquitectónica. Mantén cada ADR breve, fechado y con estado; no reescribas la historia para ocultar decisiones reemplazadas.


**Práctica y evidencia:** Redacta un ADR con contexto, decisión, alternativas y consecuencias. **Evidencia:** distingue hechos de supuestos y explica cuándo revisar la decisión.

#### 18.3.07 — Changelog
Changelog comunica cambios relevantes entre versiones, incluyendo funcionalidades, correcciones y cambios incompatibles. Sigue una convención estable y redacta entradas para consumidores, no como copia indiscriminada de commits.


**Práctica y evidencia:** Mantén un changelog por versión con cambios añadidos, corregidos y retirados. **Evidencia:** cada entrada se vincula a un cambio verificable y no incluye secretos.

#### 18.3.08 — Manual de instalación
El manual de instalación especifica requisitos, pasos, configuración, permisos y verificación posterior. Incluye recuperación y desinstalación cuando aplique y prueba los pasos desde un entorno limpio.


**Práctica y evidencia:** Escribe un manual de instalación con versiones, variables y pasos de verificación. **Evidencia:** instala desde un entorno limpio siguiendo el documento.

#### 18.3.09 — Manual de usuario
El manual de usuario explica tareas y resultados con lenguaje comprensible, capturas pertinentes y resolución de problemas. Organiza por objetivos del usuario y mantén imágenes alineadas con la versión real del producto.


**Práctica y evidencia:** Crea un manual de usuario con tareas frecuentes, errores y recuperación. **Evidencia:** una persona no técnica completa una tarea sin asistencia.

#### 18.3.10 — Plan de pruebas
El plan de pruebas define alcance, estrategia, entornos, datos, responsabilidades, riesgos y criterios de entrada/salida. Relaciónalo con requisitos y riesgos; no prometas cobertura o resultados antes de ejecutar las pruebas.


**Práctica y evidencia:** Diseña un plan de pruebas con alcance, entornos, riesgos, datos y criterios de salida. **Evidencia:** relaciona pruebas con requisitos y responsables.

#### 18.3.11 — Documentación de despliegue
La documentación de despliegue describe artefactos, configuración, secretos, migraciones, observabilidad y recuperación. Diferencia entornos y permisos, y proporciona pasos verificables para rollback y respuesta a fallos.


**Práctica y evidencia:** Documenta despliegue, configuración, observabilidad, rollback y recuperación. **Evidencia:** simula un despliegue en staging y una reversión documentada.

### Módulo 18.4 — Diagramas

#### 18.4.01 — Diagramas de flujo
Los diagramas de flujo representan pasos y decisiones de un proceso mediante símbolos y conexiones. Mantén un nivel de detalle consistente, etiqueta condiciones y verifica que cada ruta tenga inicio, fin y tratamiento de errores.


**Práctica y evidencia:** Dibuja un flujo de proceso con decisiones, excepciones y puntos de inicio/fin. **Evidencia:** valida que no existan ramas sin salida o pasos ambiguos.

#### 18.4.02 — UML
UML ofrece notaciones estandarizadas para modelar estructura y comportamiento de sistemas. Selecciona el diagrama según la pregunta que buscas responder; no es necesario producir todos los tipos para cada proyecto.


**Práctica y evidencia:** Selecciona diagramas UML adecuados al problema y usa notación consistente. **Evidencia:** explica qué aspecto del sistema representa cada diagrama.

#### 18.4.03 — Diagrama de clases
Un diagrama de clases representa clases, atributos, operaciones y relaciones estáticas. Muestra solo el detalle útil para la decisión y mantiene consistencia con el modelo de dominio o código que describe.


**Práctica y evidencia:** Modela clases, atributos, operaciones y asociaciones de un dominio pequeño. **Evidencia:** distingue asociación, composición y herencia con justificación.

#### 18.4.04 — Diagrama de secuencia
Un diagrama de secuencia muestra participantes y mensajes ordenados en el tiempo para un escenario. Incluye alternativas, errores y límites de sistema relevantes; evita convertirlo en una transcripción de cada línea de código.


**Práctica y evidencia:** Dibuja una secuencia de solicitud entre UI, API, servicio y repositorio. **Evidencia:** muestra mensajes, retornos y escenarios de error.

#### 18.4.05 — Diagrama de actividades
Un diagrama de actividades representa flujo de trabajo, decisiones, concurrencia y responsabilidades. Úsalo para procesos complejos y valida que las guardas de decisión y caminos alternativos sean explícitos.


**Práctica y evidencia:** Representa un flujo de aprobación con decisiones y estados. **Evidencia:** cubre camino exitoso, rechazo y cancelación.

#### 18.4.06 — Diagrama de componentes
Un diagrama de componentes muestra unidades modulares y sus interfaces/dependencias. Permite revisar acoplamiento y límites de despliegue; evita confundir componentes lógicos con procesos o máquinas físicas.


**Práctica y evidencia:** Dibuja componentes, interfaces y dependencias del sistema. **Evidencia:** identifica acoplamientos y límites de despliegue.

#### 18.4.07 — Diagrama de despliegue
Un diagrama de despliegue representa nodos de ejecución, artefactos y conexiones entre entornos. Identifica zonas de confianza, puertos y dependencias externas sin publicar secretos ni detalles que comprometan infraestructura real.


**Práctica y evidencia:** Representa nodos, artefactos, conexiones y entornos en un diagrama de despliegue. **Evidencia:** señala zonas de confianza y dependencias externas.

#### 18.4.08 — Diagramas ER
Los diagramas entidad-relación modelan entidades, atributos, claves y cardinalidades de datos. Comprueba que las relaciones reflejen reglas del dominio y que el modelo pueda traducirse a restricciones e índices.


**Práctica y evidencia:** Modela entidades, claves, cardinalidades y restricciones en un ERD. **Evidencia:** deriva tablas sin relaciones muchos-a-muchos sin resolver.

#### 18.4.09 — C4 Model
C4 Model describe arquitectura mediante niveles de contexto, contenedores, componentes y código. Mantén cada vista orientada a una audiencia y un propósito, y evita mezclar niveles de abstracción en un mismo diagrama.


**Práctica y evidencia:** Construye vistas C4 de contexto, contenedores y componentes para una aplicación. **Evidencia:** mantiene consistencia de nombres y audiencias entre niveles.

### Módulo 18.5 — Principios de diseño

#### 18.5.01 — SOLID
SOLID reúne cinco principios de diseño orientado a objetos que buscan reducir rigidez y mejorar extensibilidad. Aplícalos como heurísticas según el contexto, no como reglas mecánicas que obliguen a crear abstracciones innecesarias.


**Práctica y evidencia:** Evalúa una clase con cada principio SOLID y propone una refactorización justificada. **Evidencia:** identifica el principio afectado y el coste del cambio.

#### 18.5.02 — DRY
DRY recomienda evitar duplicación de conocimiento que debe cambiar de manera coordinada. No significa eliminar toda repetición textual: abstraer demasiado pronto puede crear acoplamiento y hacer el sistema más difícil de modificar.


**Práctica y evidencia:** Elimina duplicación real mediante abstracción que represente una regla común. **Evidencia:** demuestra que la abstracción no oculta diferencias relevantes.

#### 18.5.03 — KISS
KISS favorece soluciones simples que satisfacen el problema real y pueden mantenerse. La simplicidad se evalúa frente a requisitos, riesgos y evolución, no por la menor cantidad de líneas de código.


**Práctica y evidencia:** Simplifica una solución y compara legibilidad y complejidad antes/después. **Evidencia:** conserva comportamiento con pruebas.

#### 18.5.04 — YAGNI
YAGNI aconseja no implementar capacidades especulativas que todavía no se necesitan. Conserva puntos de extensión razonables, pero prioriza requisitos presentes y evita complejidad prematura.


**Práctica y evidencia:** Evalúa una funcionalidad especulativa y decide no implementarla hasta existir requisito. **Evidencia:** registra coste evitado y señal que justificaría incorporarla.

#### 18.5.05 — Separation of Concerns
Separation of Concerns divide el sistema en partes con responsabilidades y razones de cambio diferenciadas. Define límites que permitan evolucionar presentación, dominio e infraestructura sin propagar modificaciones innecesarias.


**Práctica y evidencia:** Separa persistencia, reglas de dominio y presentación en un caso pequeño. **Evidencia:** demuestra que una capa puede cambiar sin reescribir las demás.

#### 18.5.06 — High Cohesion
High Cohesion significa que los elementos de un módulo colaboran alrededor de una responsabilidad relacionada. Evalúa si funciones y datos cambian por razones similares; agrupar por conveniencia técnica puede producir módulos poco cohesivos.


**Práctica y evidencia:** Aumenta cohesión agrupando responsabilidades relacionadas y separando las ajenas. **Evidencia:** explica por qué cada módulo tiene una razón principal para cambiar.

#### 18.5.07 — Low Coupling
Low Coupling reduce dependencias fuertes entre módulos y limita el conocimiento que cada uno necesita de otros. Utiliza contratos y límites claros, pero no elimines toda dependencia: la colaboración debe seguir siendo explícita y comprensible.


**Práctica y evidencia:** Reduce dependencias concretas entre módulos mediante contratos estables. **Evidencia:** sustituye una implementación sin cambiar consumidores.

#### 18.5.08 — Dependency Inversion
Dependency Inversion propone que políticas de alto nivel no dependan de detalles concretos, sino de abstracciones estables. Define interfaces en el límite correcto y evita crear abstracciones que solo replican una implementación sin necesidad.


**Práctica y evidencia:** Invierte dependencias para que política de alto nivel dependa de abstracciones. **Evidencia:** prueba dominio sin infraestructura real.

### Módulo 18.6 — Patrones GoF

#### 18.6.01 — Creacionales
La familia creacional agrupa patrones que abstraen o controlan la creación de objetos. La elección depende de variaciones de construcción, dependencias y ciclo de vida; el patrón no justifica ocultar una creación sencilla.


**Práctica y evidencia:** Clasifica patrones por problema de creación, estructura o comportamiento. **Evidencia:** justifica la categoría y evita aplicar patrones por moda.

#### 18.6.02 — Factory
Factory encapsula la selección o creación de un producto detrás de una operación. Resulta útil cuando el tipo concreto depende de configuración o contexto; evita una fábrica si un constructor directo es suficiente.


**Práctica y evidencia:** Implementa Factory para seleccionar una implementación según configuración. **Evidencia:** demuestra que el cliente no conoce la clase concreta.

#### 18.6.03 — Abstract Factory
Abstract Factory crea familias de objetos relacionados sin acoplar al cliente con clases concretas. Úsalo cuando deban variar conjuntos compatibles de productos y mantén consistencia entre los miembros de la familia.


**Práctica y evidencia:** Usa Abstract Factory para crear familias de objetos compatibles. **Evidencia:** cambia la familia completa sin mezclar componentes incompatibles.

#### 18.6.04 — Builder
Builder separa la construcción paso a paso de la representación final de un objeto complejo. Es útil cuando hay muchas opciones o invariantes; evita convertir objetos simples en una cadena de builders innecesaria.


**Práctica y evidencia:** Construye un objeto complejo mediante pasos de Builder y valida invariantes al finalizar. **Evidencia:** compara legibilidad con constructor de muchos parámetros.

#### 18.6.05 — Singleton
Singleton restringe una clase a una única instancia accesible globalmente en el contexto definido. Puede introducir estado global y dificultar pruebas; considera inyección de dependencias y ciclo de vida del contenedor antes de aplicarlo.


**Práctica y evidencia:** Evalúa Singleton frente a inyección de dependencias y estado global. **Evidencia:** identifica impacto en pruebas, concurrencia y ciclo de vida.

#### 18.6.06 — Prototype
Prototype crea objetos nuevos a partir de una instancia existente mediante clonación. Define si la copia es superficial o profunda y cómo se copian recursos compartidos; no asumas que clonar preserva invariantes automáticamente.


**Práctica y evidencia:** Clona un prototipo configurable y distingue copia superficial de profunda. **Evidencia:** demuestra que las partes mutables no quedan compartidas accidentalmente.

#### 18.6.07 — Estructurales
La familia estructural organiza cómo se componen objetos y clases para formar estructuras mayores. Sus patrones ayudan a adaptar interfaces, añadir responsabilidades y representar jerarquías sin acoplar consumidores a detalles.


**Práctica y evidencia:** Clasifica Adapter, Decorator, Facade, Proxy, Composite, Bridge y Flyweight por intención. **Evidencia:** selecciona patrón para un problema y explica alternativa descartada.

#### 18.6.08 — Adapter
Adapter convierte la interfaz de un componente en otra que el consumidor espera. Es útil para integrar legado o proveedores distintos; mantén explícitas conversiones, errores y pérdidas de información.


**Práctica y evidencia:** Implementa Adapter para integrar una interfaz externa incompatible con el contrato interno. **Evidencia:** el consumidor utiliza el contrato sin conocer al proveedor.

#### 18.6.09 — Decorator
Decorator añade responsabilidades a un objeto envolviéndolo sin modificar su clase original. Permite combinar comportamientos, pero muchas capas pueden dificultar diagnóstico; conserva contratos y orden de aplicación.


**Práctica y evidencia:** Añade Decorator para incorporar una capacidad sin modificar la clase base. **Evidencia:** combina decoradores y prueba el orden de composición.

#### 18.6.10 — Facade
Facade ofrece una interfaz simplificada sobre un subsistema complejo. Reduce conocimiento requerido por el cliente, pero no debe convertirse en un objeto que concentre toda la lógica del sistema.


**Práctica y evidencia:** Crea Facade para simplificar una operación que coordina varios subsistemas. **Evidencia:** mantiene ocultos detalles sin convertir la fachada en un objeto dios.

#### 18.6.11 — Proxy
Proxy controla el acceso a otro objeto para aplicar políticas como carga diferida, autorización o acceso remoto. La interfaz debe conservar expectativas del sujeto real y documentar latencia y fallos adicionales.


**Práctica y evidencia:** Aplica Proxy para controlar acceso, caché o carga diferida de un recurso. **Evidencia:** demuestra que conserva el contrato del objeto real.

#### 18.6.12 — Composite
Composite organiza objetos en estructuras de árbol donde hojas y contenedores comparten una interfaz. Es apropiado para jerarquías parte-todo; define qué operaciones son válidas para hojas y cómo se propagan cambios.


**Práctica y evidencia:** Modela elementos simples y compuestos con Composite y una operación común. **Evidencia:** recorre el árbol sin condicionales por tipo en el cliente.

#### 18.6.13 — Bridge
Bridge separa una abstracción de su implementación para que ambas evolucionen independientemente. Úsalo cuando existan dos dimensiones de variación que generarían una explosión de subclases.


**Práctica y evidencia:** Usa Bridge para separar abstracción de implementación que pueden variar independientemente. **Evidencia:** combina dos dimensiones sin crear una jerarquía explosiva.

#### 18.6.14 — Flyweight
Flyweight comparte estado intrínseco entre muchos objetos para reducir consumo de memoria. Separa estado compartido e independiente y garantiza que el objeto compartido no sea modificado accidentalmente por un consumidor.


**Práctica y evidencia:** Evalúa Flyweight para compartir estado intrínseco en muchos objetos similares. **Evidencia:** separa estado compartido y extrínseco y mide si la complejidad compensa.

#### 18.6.15 — Comportamiento
La familia de comportamiento organiza comunicación, responsabilidades y algoritmos entre objetos. Ayuda a cambiar flujos sin concentrar condicionales, pero añade tipos y relaciones que deben justificarse por variación real.


**Práctica y evidencia:** Clasifica patrones de comportamiento según cómo distribuyen responsabilidad y colaboración. **Evidencia:** identifica problema de acoplamiento que resuelve el patrón.

#### 18.6.16 — Strategy
Strategy encapsula algoritmos intercambiables detrás de un contrato común. Permite elegir comportamiento por configuración o contexto y facilita pruebas; evita crear una estrategia por cada variación trivial.


**Práctica y evidencia:** Implementa Strategy para intercambiar un algoritmo sin cambiar el cliente. **Evidencia:** añade una estrategia nueva sin modificar condicionales centrales.

#### 18.6.17 — Observer
Observer establece una relación de suscripción para notificar cambios a observadores. Define alta/baja de suscriptores, orden, errores y concurrencia; evita fugas por listeners que permanecen registrados.


**Práctica y evidencia:** Usa Observer para notificar cambios a suscriptores y gestiona alta/baja. **Evidencia:** evita fugas de listeners y define orden/errores de notificación.

#### 18.6.18 — Command
Command encapsula una acción como objeto con datos y operación de ejecución. Facilita colas, auditoría y deshacer cuando el diseño lo soporta; define idempotencia y manejo de fallos antes de ejecutar comandos diferidos.


**Práctica y evidencia:** Encapsula una operación como Command y permite cola, auditoría o deshacer cuando el dominio lo admite. **Evidencia:** explica qué estado requiere una reversión segura.

#### 18.6.19 — State
State permite que un objeto cambie comportamiento según su estado interno representado por objetos o transiciones explícitas. Define estados válidos y transiciones permitidas para evitar combinaciones inconsistentes de booleanos.


**Práctica y evidencia:** Modela estados de un pedido y transiciones válidas mediante State o una máquina de estados explícita. **Evidencia:** demuestra que una transición inválida se rechaza.

#### 18.6.20 — Iterator
Iterator permite recorrer una colección sin exponer su representación interna. Define orden y comportamiento ante modificaciones concurrentes; utiliza iteradores estándar cuando satisfacen el contrato requerido.


**Práctica y evidencia:** Implementa Iterator para recorrer una colección sin exponer su representación interna. **Evidencia:** demuestra recorrido uniforme y comportamiento ante modificación.

#### 18.6.21 — Mediator
Mediator centraliza coordinación entre componentes que de otro modo se comunicarían directamente. Reduce dependencias cruzadas, pero el mediador puede convertirse en un punto de concentración excesiva; divide responsabilidades cuando crezca.


**Práctica y evidencia:** Usa Mediator para coordinar componentes que no deben conocerse directamente. **Evidencia:** identifica cuándo el mediador se vuelve demasiado complejo.

#### 18.6.22 — Template Method
Template Method define el esqueleto de un algoritmo y delega pasos variables a subclases o métodos especializados. Úsalo cuando el flujo general sea estable y evita jerarquías rígidas para variaciones que encajan mejor con composición.


**Práctica y evidencia:** Aplica Template Method para fijar el esqueleto de un algoritmo con pasos redefinibles. **Evidencia:** distingue pasos invariantes de puntos de extensión.

#### 18.6.23 — Chain of Responsibility
Chain of Responsibility pasa una solicitud por una secuencia de handlers hasta que alguno la procesa o termina la cadena. Define orden, condición de finalización y comportamiento sin handler para evitar solicitudes perdidas.


**Práctica y evidencia:** Construye Chain of Responsibility para procesar una solicitud a través de handlers. **Evidencia:** prueba orden, terminación y caso sin handler aplicable.

### Módulo 18.7 — Arquitecturas

#### 18.7.01 — Monolithic Architecture
Monolithic Architecture empaqueta gran parte de la aplicación como una unidad desplegable. Puede simplificar desarrollo y operación inicial; controla modularidad interna para evitar que el monolito se convierta en una masa acoplada.


**Práctica y evidencia:** Dibuja un monolito con módulos y límites de despliegue y evalúa sus ventajas operativas. **Evidencia:** identifica qué escala conjuntamente y qué acoplamiento existe.

#### 18.7.02 — Modular Monolith
Modular Monolith mantiene un único despliegue con módulos internos y límites explícitos. Es una alternativa a microservicios cuando se necesita separación de dominio sin asumir complejidad de red y operación distribuida.


**Práctica y evidencia:** Organiza un monolito modular con límites internos y dependencias explícitas. **Evidencia:** prueba que un módulo no accede directamente a datos internos de otro.

#### 18.7.03 — Layered Architecture
Layered Architecture separa responsabilidades en capas como presentación, aplicación, dominio e infraestructura. Define reglas de dependencia y evita que capas superiores accedan directamente a detalles internos de capas inferiores.


**Práctica y evidencia:** Separa presentación, aplicación, dominio e infraestructura en arquitectura por capas. **Evidencia:** documenta dirección permitida de dependencias.

#### 18.7.04 — MVC
MVC organiza interacción entre modelo, vista y controlador. Define qué capa mantiene estado y reglas, y evita convertir controladores en coordinadores gigantes o vistas en lugares de lógica de dominio.


**Práctica y evidencia:** Traza una solicitud en MVC desde vista/controlador hasta modelo y respuesta. **Evidencia:** evita ubicar reglas de negocio críticas en la vista.

#### 18.7.05 — Clean Architecture
Clean Architecture organiza el sistema alrededor de políticas y dominio, haciendo que detalles externos dependan de contratos internos. Evalúa el coste de abstracción y mantén dependencias dirigidas hacia el núcleo.


**Práctica y evidencia:** Aplica Clean Architecture a un caso de uso y define puertos de entrada/salida. **Evidencia:** ejecuta prueba de dominio sin framework ni base de datos.

#### 18.7.06 — Hexagonal Architecture
Hexagonal Architecture separa el núcleo de aplicación de actores externos mediante puertos y adaptadores. Define puertos por necesidad del dominio y adapta bases de datos, interfaces y proveedores sin filtrar sus modelos internos.


**Práctica y evidencia:** Diseña puertos y adaptadores para una aplicación que usa dos proveedores externos. **Evidencia:** sustituye adaptador en pruebas sin cambiar caso de uso.

#### 18.7.07 — Onion Architecture
Onion Architecture organiza capas concéntricas con dependencias hacia el dominio central. Mantén el dominio independiente de frameworks y persistencia; no confundas la representación visual de capas con una regla suficiente de diseño.


**Práctica y evidencia:** Organiza dependencias en anillos de Onion Architecture y mantiene dominio en el centro. **Evidencia:** comprueba que infraestructura depende de abstracciones internas.

#### 18.7.08 — Event-Driven Architecture
Event-Driven Architecture conecta productores y consumidores mediante eventos que representan hechos. Define esquema, entrega, orden, duplicados y observabilidad; evita depender de sincronía o estado compartido entre servicios.


**Práctica y evidencia:** Modela un flujo event-driven con productores, eventos y consumidores desacoplados. **Evidencia:** contempla duplicados, orden, idempotencia y observabilidad.

#### 18.7.09 — Microservices
Microservices divide capacidades de negocio en servicios desplegables y operables independientemente. Exige límites de dominio, automatización, observabilidad y resiliencia; evalúa primero si el beneficio supera la complejidad distribuida.


**Práctica y evidencia:** Compara microservicios con monolito modular según autonomía de despliegue y coste distribuido. **Evidencia:** presenta criterios de descomposición y razones para no dividir prematuramente.

### Módulo 18.8 — Diseño de sistemas

#### 18.8.01 — Scalability
Scalability describe la capacidad de manejar crecimiento de carga mediante ampliación vertical u horizontal. Identifica cuello de botella y perfil de demanda antes de escalar; más instancias pueden aumentar costes y complejidad.


**Práctica y evidencia:** Define una métrica de escalabilidad y prueba cómo responde el sistema al aumentar carga o recursos. **Evidencia:** distingue escalado vertical y horizontal.

#### 18.8.02 — Availability
Availability mide la proporción de tiempo en que un servicio cumple condiciones de disponibilidad definidas. Especifica ventana, dependencias y exclusiones; alta disponibilidad requiere redundancia, detección y recuperación probadas.


**Práctica y evidencia:** Calcula disponibilidad a partir de tiempo de servicio y ventanas de interrupción. **Evidencia:** define SLI/SLO y excluye supuestos no documentados.

#### 18.8.03 — Reliability
Reliability es la capacidad de operar correctamente durante un periodo y condiciones determinados. Diseña tolerancia a fallos, recuperación y consistencia; mide errores y comportamiento real, no solo tiempo de actividad.


**Práctica y evidencia:** Analiza fiabilidad mediante tasa de fallos, recuperación y degradación. **Evidencia:** propone mecanismo de redundancia y prueba de recuperación.

#### 18.8.04 — Consistency
Consistency describe qué garantías reciben los clientes sobre visibilidad y orden de actualizaciones en sistemas distribuidos. Distingue consistencia fuerte, eventual y garantías de lectura/escritura según el modelo de datos.


**Práctica y evidencia:** Define consistencia requerida para una operación de negocio y sus lecturas. **Evidencia:** describe qué estados intermedios puede observar un usuario.

#### 18.8.05 — CAP Theorem
CAP Theorem establece que ante una partición de red un sistema distribuido debe equilibrar disponibilidad y consistencia fuerte bajo el modelo formal. No significa elegir solo dos propiedades en todo momento ni clasifica sistemas sin considerar condiciones.


**Práctica y evidencia:** Analiza una partición de red y decide qué operaciones deben rechazarse o continuar. **Evidencia:** explica el compromiso CAP para ese escenario específico.

#### 18.8.06 — Load Balancing
Load Balancing distribuye solicitudes entre instancias para mejorar capacidad y disponibilidad. Define health checks, algoritmo, sesiones, afinidad y comportamiento ante fallos; balancear tráfico no corrige un backend saturado o incorrecto.


**Práctica y evidencia:** Diseña balanceo de carga con health checks y estrategia de distribución. **Evidencia:** prueba comportamiento cuando un nodo deja de responder.

#### 18.8.07 — Caching
Caching guarda resultados cercanos al consumidor para reducir latencia y carga. Define TTL, invalidación, consistencia y alcance; las cachés compartidas requieren aislamiento para no mezclar datos de distintos usuarios.


**Práctica y evidencia:** Define política de caché con TTL e invalidación para datos cambiantes. **Evidencia:** demuestra cómo evita servir indefinidamente una versión obsoleta.

#### 18.8.08 — Message Queues
Message Queues desacopla productores y consumidores y absorbe variaciones de carga. Define confirmaciones, reintentos, orden, expiración y dead-letter; consumidores deben tolerar mensajes duplicados y fallos parciales.


**Práctica y evidencia:** Diseña comunicación asíncrona mediante cola con reintentos y dead-letter queue. **Evidencia:** explica entrega, duplicados y consumidor idempotente.

#### 18.8.09 — Distributed Systems
Distributed Systems coordina componentes que se ejecutan en nodos independientes y se comunican por redes falibles. Diseña para latencia, particiones, relojes no sincronizados y fallos parciales; no asumas transacciones locales globales.


**Práctica y evidencia:** Dibuja componentes de un sistema distribuido y analiza latencia, particiones, fallos parciales y observabilidad. **Evidencia:** identifica una estrategia de correlación entre servicios.

#### 18.8.10 — API Gateway
API Gateway ofrece un punto de entrada para enrutamiento, políticas transversales y composición de APIs. Evita concentrar lógica de dominio en el gateway y limita su alcance para que no se convierta en cuello de botella.


**Práctica y evidencia:** Define responsabilidades de API Gateway para enrutamiento, autenticación y límites. **Evidencia:** evita colocar reglas de dominio complejas en el gateway.

#### 18.8.11 — Service Discovery
Service Discovery permite localizar instancias de servicios dinámicamente. Define registro, salud, expiración y autenticación de descubrimiento; protege el catálogo porque revela topología y puntos internos de la plataforma.


**Práctica y evidencia:** Modela registro y descubrimiento de servicios con health status y expiración. **Evidencia:** explica cómo se retiran instancias no saludables.

#### 18.8.12 — Fault Tolerance
Fault Tolerance permite que el sistema continúe ofreciendo capacidades aceptables ante fallos de componentes. Usa timeouts, retries con backoff, circuit breakers y degradación controlada; reintentos indiscriminados pueden amplificar una caída.


**Práctica y evidencia:** Diseña tolerancia a fallos con timeout, retry con backoff, circuit breaker y fallback. **Evidencia:** evita reintentos ilimitados y tormentas de solicitudes.

### Módulo 18.9 — Modelado de dominios

#### 18.9.01 — Domain-Driven Design
Domain-Driven Design alinea el diseño de software con el conocimiento del dominio y colaboración entre expertos y desarrolladores. Utiliza lenguaje compartido y límites explícitos; no es una receta de clases ni exige microservicios.


**Práctica y evidencia:** Aplica DDD para identificar lenguaje del dominio, subdominios y límites de contexto. **Evidencia:** documenta términos y conflictos de significado entre áreas.

#### 18.9.02 — Entities
Entities tienen identidad persistente que las distingue aunque cambien sus atributos. Define identidad y ciclo de vida según el dominio y evita comparar entidades solo por igualdad de todos sus campos.


**Práctica y evidencia:** Define una Entity con identidad estable y reglas de ciclo de vida. **Evidencia:** explica por qué dos entidades con mismos atributos pueden ser distintas.

#### 18.9.03 — Value Objects
Value Objects representan conceptos definidos por sus valores y suelen ser inmutables. Encapsulan validación y operaciones propias, como dinero o rango de fechas, evitando tipos primitivos sin significado.


**Práctica y evidencia:** Crea un Value Object inmutable para dinero o dirección y define igualdad por valor. **Evidencia:** prueba invariantes y ausencia de identidad propia.

#### 18.9.04 — Aggregates
Aggregates agrupan entidades y value objects bajo una raíz que protege invariantes y límites transaccionales. Accede al conjunto a través de su raíz y evita agregados enormes que bloqueen concurrencia.


**Práctica y evidencia:** Diseña un Aggregate con raíz y reglas transaccionales consistentes. **Evidencia:** demuestra que cambios internos pasan por la raíz y respetan invariantes.

#### 18.9.05 — Repositories
Repositories ofrecen una abstracción para recuperar y persistir aggregates sin exponer detalles de almacenamiento al dominio. Define operaciones por intención del negocio y evita convertir el repositorio en un CRUD genérico sin límites.


**Práctica y evidencia:** Define un Repository para recuperar y persistir agregados sin exponer detalles de almacenamiento. **Evidencia:** prueba el dominio con repositorio en memoria.

#### 18.9.06 — Bounded Contexts
Bounded Context define un límite dentro del cual un modelo y lenguaje tienen significado consistente. Identifica contextos por capacidades y reglas; no fuerces una única definición de un término que cambia entre áreas.


**Práctica y evidencia:** Delimita Bounded Contexts para ventas e inventario y define contratos de integración. **Evidencia:** identifica términos homónimos con significado distinto.

#### 18.9.07 — Ubiquitous Language
Ubiquitous Language es el vocabulario compartido entre expertos del dominio y equipo técnico dentro de un contexto delimitado. Úsalo en conversaciones, código y documentación y revisa términos ambiguos con ejemplos reales.



**Práctica y evidencia:** Construye un glosario de Ubiquitous Language y úsalo en código, pruebas y documentación. **Evidencia:** detecta un término ambiguo y acuerda una definición compartida.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 100 orientaciones genéricas por explicaciones específicas de cada entrada oficial. Se desarrollaron requerimientos, Scrum/Kanban, artefactos, documentación y diagramas, principios de diseño, las tres familias GoF, arquitecturas, atributos de sistemas distribuidos y modelado de dominio.

**Nota de fidelidad curricular:** las entradas «Creacionales», «Estructurales» y «Comportamiento» de 18.6 se conservan porque aparecen como elementos del roadmap; se explican como rótulos de clasificación de las familias de patrones, no como patrones individuales.

**Revisión interna:** 100/100 entradas desarrolladas y cotejadas con el roadmap. Se precisaron límites de CAP, disponibilidad/fiabilidad, microservicios, WIP, ADR y patrones; se mantuvo el enfoque de seleccionar patrones por necesidad. Pendiente: revisar diagramas con stakeholders, contrastar arquitectura con requisitos reales, probar decisiones con escenarios de carga/fallo y realizar segunda revisión técnica. No se declara implementación ni aprobación externa.
