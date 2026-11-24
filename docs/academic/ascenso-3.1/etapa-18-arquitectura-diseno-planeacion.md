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

#### 18.1.02 — No funcionales
Los requerimientos no funcionales expresan atributos y restricciones como rendimiento, seguridad, disponibilidad, accesibilidad y mantenibilidad. Cuantifícalos con umbrales, contexto y método de medición; «rápido» o «seguro» no son criterios verificables por sí solos.

#### 18.1.03 — Historias de usuario
Una historia de usuario comunica una necesidad desde la perspectiva de un actor y el valor esperado. Acompáñala con criterios de aceptación, reglas y dependencias; la plantilla «Como/quiero/para» no reemplaza el análisis.

#### 18.1.04 — Casos de uso
Un caso de uso describe interacciones entre actores y sistema para alcanzar un objetivo, incluyendo flujo principal y alternativas. Registra precondiciones, postcondiciones y excepciones para descubrir comportamientos que una historia breve podría omitir.

#### 18.1.05 — Reglas de negocio
Las reglas de negocio expresan políticas, cálculos, permisos y restricciones propias del dominio. Distingue reglas del negocio de decisiones técnicas y define fuente de autoridad, prioridad y tratamiento de excepciones.

#### 18.1.06 — Restricciones
Las restricciones limitan soluciones posibles por tecnología, presupuesto, normativa, plazo, infraestructura o compatibilidad. Registra su origen y si son obligatorias o negociables; una restricción no documentada puede convertirse en riesgo de diseño.

#### 18.1.07 — Stakeholders
Stakeholders son personas u organizaciones que influyen en el sistema o reciben sus efectos. Identifica necesidades, autoridad, conflictos y canales de decisión; no asumas que una sola persona representa a todos los usuarios.

#### 18.1.08 — Alcance del proyecto
El alcance define qué incluye y excluye el proyecto, sus entregables y límites. Documenta supuestos, exclusiones y criterios de cambio para prevenir expansión no controlada y desacuerdos sobre el resultado esperado.

### Módulo 18.2 — Metodologías ágiles

#### 18.2.01 — Manifiesto Ágil
El Manifiesto Ágil expresa valores y principios para desarrollar software de forma adaptativa y colaborativa. Interprétalo como orientación para decisiones y aprendizaje, no como ausencia de planificación, documentación o control.

#### 18.2.02 — Scrum
Scrum es un marco de trabajo con responsabilidades, eventos y artefactos definidos. Comprende Product Owner, Scrum Master y Developers, y adapta el marco con transparencia; no conviertas los eventos en reuniones sin propósito ni inspección.

#### 18.2.03 — Kanban
Kanban visualiza el flujo de trabajo y limita trabajo en progreso para mejorar entrega y detectar cuellos de botella. Define políticas explícitas y mide tiempo de ciclo y throughput, no solo cantidad de tareas en columnas.

#### 18.2.04 — Sprints
Un Sprint es un periodo fijo en Scrum para crear un incremento de valor utilizable. Define objetivo y duración consistente, y ajusta alcance mediante colaboración sin comprometer el objetivo del Sprint.

#### 18.2.05 — Product Backlog
Product Backlog es una lista ordenada y evolutiva del trabajo necesario para mejorar el producto. Refina elementos con criterios y valor, manteniendo transparencia sobre prioridad, incertidumbre y dependencias.

#### 18.2.06 — Sprint Backlog
Sprint Backlog reúne el objetivo del Sprint, elementos seleccionados y plan de trabajo de Developers. Se actualiza conforme se aprende y no debe convertirse en una lista rígida de tareas impuesta externamente.

#### 18.2.07 — Planning
Planning establece por qué el Sprint es valioso, qué puede completarse y cómo se realizará el trabajo. Participan quienes corresponda según Scrum; el resultado debe ser un objetivo claro y un plan adaptativo.

#### 18.2.08 — Daily
Daily Scrum es una oportunidad breve para inspeccionar progreso hacia el objetivo y adaptar el plan. No es un reporte de estatus al gerente ni una obligación de responder siempre tres preguntas idénticas.

#### 18.2.09 — Review
Review inspecciona el incremento y obtiene retroalimentación de stakeholders para adaptar el Product Backlog. Presenta software funcional y resultados reales; no la conviertas en una demostración preparada que oculte limitaciones.

#### 18.2.10 — Retrospective
Retrospective analiza cómo mejorar calidad y efectividad del equipo, procesos y herramientas. Acuerda acciones pequeñas con responsable y seguimiento; evita buscar culpables o producir listas que nunca se implementan.

#### 18.2.11 — Definition of Done
Definition of Done establece criterios compartidos para considerar un incremento terminado y con calidad suficiente. Incluye pruebas, revisión, documentación y controles aplicables; no debe confundirse con criterios de aceptación de una historia específica.

#### 18.2.12 — Story Points
Story Points son una técnica relativa de estimación de esfuerzo/complexidad/incertidumbre, no horas ni productividad individual. Úsalos solo si ayudan a planificar y nunca para comparar personas o convertir velocidad en objetivo.

#### 18.2.13 — Gestión del trabajo en progreso (WIP)
WIP limita cuántos elementos pueden estar en progreso simultáneamente. Establece límites según capacidad y observa bloqueos; reducir multitarea puede mejorar flujo, pero el límite debe revisarse con datos y contexto.

### Módulo 18.3 — Documentación

#### 18.3.01 — README
README explica propósito, requisitos, instalación, configuración, ejecución y contribución de un repositorio. Mantén instrucciones probadas y coherentes con el estado real; nunca incluyas secretos ni instrucciones que requieran permisos no documentados.

#### 18.3.02 — Especificación de requisitos
La especificación de requisitos documenta funciones, calidad, interfaces, restricciones y criterios de aceptación. Mantén identificadores, versiones y trazabilidad hacia diseño y pruebas para gestionar cambios sin perder contexto.

#### 18.3.03 — Documentación técnica
La documentación técnica explica arquitectura, componentes, contratos, decisiones y operación para desarrolladores y operadores. Debe responder cómo funciona el sistema y qué límites tiene, no duplicar comentarios obvios del código.

#### 18.3.04 — Documentación funcional
La documentación funcional describe capacidades desde el punto de vista del usuario y las reglas del negocio. Usa lenguaje del dominio, flujos y excepciones verificables para que negocio, QA y desarrollo compartan interpretación.

#### 18.3.05 — API Documentation
API Documentation describe endpoints, esquemas, autenticación, errores, límites y ejemplos. Genera o valida documentación desde contratos versionados y evita publicar credenciales o datos reales en ejemplos.

#### 18.3.06 — Architecture Decision Records (ADR)
Architecture Decision Records (ADR) registran contexto, decisión, alternativas y consecuencias de una decisión arquitectónica. Mantén cada ADR breve, fechado y con estado; no reescribas la historia para ocultar decisiones reemplazadas.

#### 18.3.07 — Changelog
Changelog comunica cambios relevantes entre versiones, incluyendo funcionalidades, correcciones y cambios incompatibles. Sigue una convención estable y redacta entradas para consumidores, no como copia indiscriminada de commits.

#### 18.3.08 — Manual de instalación
El manual de instalación especifica requisitos, pasos, configuración, permisos y verificación posterior. Incluye recuperación y desinstalación cuando aplique y prueba los pasos desde un entorno limpio.

#### 18.3.09 — Manual de usuario
El manual de usuario explica tareas y resultados con lenguaje comprensible, capturas pertinentes y resolución de problemas. Organiza por objetivos del usuario y mantén imágenes alineadas con la versión real del producto.

#### 18.3.10 — Plan de pruebas
El plan de pruebas define alcance, estrategia, entornos, datos, responsabilidades, riesgos y criterios de entrada/salida. Relaciónalo con requisitos y riesgos; no prometas cobertura o resultados antes de ejecutar las pruebas.

#### 18.3.11 — Documentación de despliegue
La documentación de despliegue describe artefactos, configuración, secretos, migraciones, observabilidad y recuperación. Diferencia entornos y permisos, y proporciona pasos verificables para rollback y respuesta a fallos.

### Módulo 18.4 — Diagramas

#### 18.4.01 — Diagramas de flujo
Los diagramas de flujo representan pasos y decisiones de un proceso mediante símbolos y conexiones. Mantén un nivel de detalle consistente, etiqueta condiciones y verifica que cada ruta tenga inicio, fin y tratamiento de errores.

#### 18.4.02 — UML
UML ofrece notaciones estandarizadas para modelar estructura y comportamiento de sistemas. Selecciona el diagrama según la pregunta que buscas responder; no es necesario producir todos los tipos para cada proyecto.

#### 18.4.03 — Diagrama de clases
Un diagrama de clases representa clases, atributos, operaciones y relaciones estáticas. Muestra solo el detalle útil para la decisión y mantiene consistencia con el modelo de dominio o código que describe.

#### 18.4.04 — Diagrama de secuencia
Un diagrama de secuencia muestra participantes y mensajes ordenados en el tiempo para un escenario. Incluye alternativas, errores y límites de sistema relevantes; evita convertirlo en una transcripción de cada línea de código.

#### 18.4.05 — Diagrama de actividades
Un diagrama de actividades representa flujo de trabajo, decisiones, concurrencia y responsabilidades. Úsalo para procesos complejos y valida que las guardas de decisión y caminos alternativos sean explícitos.

#### 18.4.06 — Diagrama de componentes
Un diagrama de componentes muestra unidades modulares y sus interfaces/dependencias. Permite revisar acoplamiento y límites de despliegue; evita confundir componentes lógicos con procesos o máquinas físicas.

#### 18.4.07 — Diagrama de despliegue
Un diagrama de despliegue representa nodos de ejecución, artefactos y conexiones entre entornos. Identifica zonas de confianza, puertos y dependencias externas sin publicar secretos ni detalles que comprometan infraestructura real.

#### 18.4.08 — Diagramas ER
Los diagramas entidad-relación modelan entidades, atributos, claves y cardinalidades de datos. Comprueba que las relaciones reflejen reglas del dominio y que el modelo pueda traducirse a restricciones e índices.

#### 18.4.09 — C4 Model
C4 Model describe arquitectura mediante niveles de contexto, contenedores, componentes y código. Mantén cada vista orientada a una audiencia y un propósito, y evita mezclar niveles de abstracción en un mismo diagrama.

### Módulo 18.5 — Principios de diseño

#### 18.5.01 — SOLID
SOLID reúne cinco principios de diseño orientado a objetos que buscan reducir rigidez y mejorar extensibilidad. Aplícalos como heurísticas según el contexto, no como reglas mecánicas que obliguen a crear abstracciones innecesarias.

#### 18.5.02 — DRY
DRY recomienda evitar duplicación de conocimiento que debe cambiar de manera coordinada. No significa eliminar toda repetición textual: abstraer demasiado pronto puede crear acoplamiento y hacer el sistema más difícil de modificar.

#### 18.5.03 — KISS
KISS favorece soluciones simples que satisfacen el problema real y pueden mantenerse. La simplicidad se evalúa frente a requisitos, riesgos y evolución, no por la menor cantidad de líneas de código.

#### 18.5.04 — YAGNI
YAGNI aconseja no implementar capacidades especulativas que todavía no se necesitan. Conserva puntos de extensión razonables, pero prioriza requisitos presentes y evita complejidad prematura.

#### 18.5.05 — Separation of Concerns
Separation of Concerns divide el sistema en partes con responsabilidades y razones de cambio diferenciadas. Define límites que permitan evolucionar presentación, dominio e infraestructura sin propagar modificaciones innecesarias.

#### 18.5.06 — High Cohesion
High Cohesion significa que los elementos de un módulo colaboran alrededor de una responsabilidad relacionada. Evalúa si funciones y datos cambian por razones similares; agrupar por conveniencia técnica puede producir módulos poco cohesivos.

#### 18.5.07 — Low Coupling
Low Coupling reduce dependencias fuertes entre módulos y limita el conocimiento que cada uno necesita de otros. Utiliza contratos y límites claros, pero no elimines toda dependencia: la colaboración debe seguir siendo explícita y comprensible.

#### 18.5.08 — Dependency Inversion
Dependency Inversion propone que políticas de alto nivel no dependan de detalles concretos, sino de abstracciones estables. Define interfaces en el límite correcto y evita crear abstracciones que solo replican una implementación sin necesidad.

### Módulo 18.6 — Patrones GoF

#### 18.6.01 — Creacionales
La familia creacional agrupa patrones que abstraen o controlan la creación de objetos. La elección depende de variaciones de construcción, dependencias y ciclo de vida; el patrón no justifica ocultar una creación sencilla.

#### 18.6.02 — Factory
Factory encapsula la selección o creación de un producto detrás de una operación. Resulta útil cuando el tipo concreto depende de configuración o contexto; evita una fábrica si un constructor directo es suficiente.

#### 18.6.03 — Abstract Factory
Abstract Factory crea familias de objetos relacionados sin acoplar al cliente con clases concretas. Úsalo cuando deban variar conjuntos compatibles de productos y mantén consistencia entre los miembros de la familia.

#### 18.6.04 — Builder
Builder separa la construcción paso a paso de la representación final de un objeto complejo. Es útil cuando hay muchas opciones o invariantes; evita convertir objetos simples en una cadena de builders innecesaria.

#### 18.6.05 — Singleton
Singleton restringe una clase a una única instancia accesible globalmente en el contexto definido. Puede introducir estado global y dificultar pruebas; considera inyección de dependencias y ciclo de vida del contenedor antes de aplicarlo.

#### 18.6.06 — Prototype
Prototype crea objetos nuevos a partir de una instancia existente mediante clonación. Define si la copia es superficial o profunda y cómo se copian recursos compartidos; no asumas que clonar preserva invariantes automáticamente.

#### 18.6.07 — Estructurales
La familia estructural organiza cómo se componen objetos y clases para formar estructuras mayores. Sus patrones ayudan a adaptar interfaces, añadir responsabilidades y representar jerarquías sin acoplar consumidores a detalles.

#### 18.6.08 — Adapter
Adapter convierte la interfaz de un componente en otra que el consumidor espera. Es útil para integrar legado o proveedores distintos; mantén explícitas conversiones, errores y pérdidas de información.

#### 18.6.09 — Decorator
Decorator añade responsabilidades a un objeto envolviéndolo sin modificar su clase original. Permite combinar comportamientos, pero muchas capas pueden dificultar diagnóstico; conserva contratos y orden de aplicación.

#### 18.6.10 — Facade
Facade ofrece una interfaz simplificada sobre un subsistema complejo. Reduce conocimiento requerido por el cliente, pero no debe convertirse en un objeto que concentre toda la lógica del sistema.

#### 18.6.11 — Proxy
Proxy controla el acceso a otro objeto para aplicar políticas como carga diferida, autorización o acceso remoto. La interfaz debe conservar expectativas del sujeto real y documentar latencia y fallos adicionales.

#### 18.6.12 — Composite
Composite organiza objetos en estructuras de árbol donde hojas y contenedores comparten una interfaz. Es apropiado para jerarquías parte-todo; define qué operaciones son válidas para hojas y cómo se propagan cambios.

#### 18.6.13 — Bridge
Bridge separa una abstracción de su implementación para que ambas evolucionen independientemente. Úsalo cuando existan dos dimensiones de variación que generarían una explosión de subclases.

#### 18.6.14 — Flyweight
Flyweight comparte estado intrínseco entre muchos objetos para reducir consumo de memoria. Separa estado compartido e independiente y garantiza que el objeto compartido no sea modificado accidentalmente por un consumidor.

#### 18.6.15 — Comportamiento
La familia de comportamiento organiza comunicación, responsabilidades y algoritmos entre objetos. Ayuda a cambiar flujos sin concentrar condicionales, pero añade tipos y relaciones que deben justificarse por variación real.

#### 18.6.16 — Strategy
Strategy encapsula algoritmos intercambiables detrás de un contrato común. Permite elegir comportamiento por configuración o contexto y facilita pruebas; evita crear una estrategia por cada variación trivial.

#### 18.6.17 — Observer
Observer establece una relación de suscripción para notificar cambios a observadores. Define alta/baja de suscriptores, orden, errores y concurrencia; evita fugas por listeners que permanecen registrados.

#### 18.6.18 — Command
Command encapsula una acción como objeto con datos y operación de ejecución. Facilita colas, auditoría y deshacer cuando el diseño lo soporta; define idempotencia y manejo de fallos antes de ejecutar comandos diferidos.

#### 18.6.19 — State
State permite que un objeto cambie comportamiento según su estado interno representado por objetos o transiciones explícitas. Define estados válidos y transiciones permitidas para evitar combinaciones inconsistentes de booleanos.

#### 18.6.20 — Iterator
Iterator permite recorrer una colección sin exponer su representación interna. Define orden y comportamiento ante modificaciones concurrentes; utiliza iteradores estándar cuando satisfacen el contrato requerido.

#### 18.6.21 — Mediator
Mediator centraliza coordinación entre componentes que de otro modo se comunicarían directamente. Reduce dependencias cruzadas, pero el mediador puede convertirse en un punto de concentración excesiva; divide responsabilidades cuando crezca.

#### 18.6.22 — Template Method
Template Method define el esqueleto de un algoritmo y delega pasos variables a subclases o métodos especializados. Úsalo cuando el flujo general sea estable y evita jerarquías rígidas para variaciones que encajan mejor con composición.

#### 18.6.23 — Chain of Responsibility
Chain of Responsibility pasa una solicitud por una secuencia de handlers hasta que alguno la procesa o termina la cadena. Define orden, condición de finalización y comportamiento sin handler para evitar solicitudes perdidas.

### Módulo 18.7 — Arquitecturas

#### 18.7.01 — Monolithic Architecture
Monolithic Architecture empaqueta gran parte de la aplicación como una unidad desplegable. Puede simplificar desarrollo y operación inicial; controla modularidad interna para evitar que el monolito se convierta en una masa acoplada.

#### 18.7.02 — Modular Monolith
Modular Monolith mantiene un único despliegue con módulos internos y límites explícitos. Es una alternativa a microservicios cuando se necesita separación de dominio sin asumir complejidad de red y operación distribuida.

#### 18.7.03 — Layered Architecture
Layered Architecture separa responsabilidades en capas como presentación, aplicación, dominio e infraestructura. Define reglas de dependencia y evita que capas superiores accedan directamente a detalles internos de capas inferiores.

#### 18.7.04 — MVC
MVC organiza interacción entre modelo, vista y controlador. Define qué capa mantiene estado y reglas, y evita convertir controladores en coordinadores gigantes o vistas en lugares de lógica de dominio.

#### 18.7.05 — Clean Architecture
Clean Architecture organiza el sistema alrededor de políticas y dominio, haciendo que detalles externos dependan de contratos internos. Evalúa el coste de abstracción y mantén dependencias dirigidas hacia el núcleo.

#### 18.7.06 — Hexagonal Architecture
Hexagonal Architecture separa el núcleo de aplicación de actores externos mediante puertos y adaptadores. Define puertos por necesidad del dominio y adapta bases de datos, interfaces y proveedores sin filtrar sus modelos internos.

#### 18.7.07 — Onion Architecture
Onion Architecture organiza capas concéntricas con dependencias hacia el dominio central. Mantén el dominio independiente de frameworks y persistencia; no confundas la representación visual de capas con una regla suficiente de diseño.

#### 18.7.08 — Event-Driven Architecture
Event-Driven Architecture conecta productores y consumidores mediante eventos que representan hechos. Define esquema, entrega, orden, duplicados y observabilidad; evita depender de sincronía o estado compartido entre servicios.

#### 18.7.09 — Microservices
Microservices divide capacidades de negocio en servicios desplegables y operables independientemente. Exige límites de dominio, automatización, observabilidad y resiliencia; evalúa primero si el beneficio supera la complejidad distribuida.

### Módulo 18.8 — Diseño de sistemas

#### 18.8.01 — Scalability
Scalability describe la capacidad de manejar crecimiento de carga mediante ampliación vertical u horizontal. Identifica cuello de botella y perfil de demanda antes de escalar; más instancias pueden aumentar costes y complejidad.

#### 18.8.02 — Availability
Availability mide la proporción de tiempo en que un servicio cumple condiciones de disponibilidad definidas. Especifica ventana, dependencias y exclusiones; alta disponibilidad requiere redundancia, detección y recuperación probadas.

#### 18.8.03 — Reliability
Reliability es la capacidad de operar correctamente durante un periodo y condiciones determinados. Diseña tolerancia a fallos, recuperación y consistencia; mide errores y comportamiento real, no solo tiempo de actividad.

#### 18.8.04 — Consistency
Consistency describe qué garantías reciben los clientes sobre visibilidad y orden de actualizaciones en sistemas distribuidos. Distingue consistencia fuerte, eventual y garantías de lectura/escritura según el modelo de datos.

#### 18.8.05 — CAP Theorem
CAP Theorem establece que ante una partición de red un sistema distribuido debe equilibrar disponibilidad y consistencia fuerte bajo el modelo formal. No significa elegir solo dos propiedades en todo momento ni clasifica sistemas sin considerar condiciones.

#### 18.8.06 — Load Balancing
Load Balancing distribuye solicitudes entre instancias para mejorar capacidad y disponibilidad. Define health checks, algoritmo, sesiones, afinidad y comportamiento ante fallos; balancear tráfico no corrige un backend saturado o incorrecto.

#### 18.8.07 — Caching
Caching guarda resultados cercanos al consumidor para reducir latencia y carga. Define TTL, invalidación, consistencia y alcance; las cachés compartidas requieren aislamiento para no mezclar datos de distintos usuarios.

#### 18.8.08 — Message Queues
Message Queues desacopla productores y consumidores y absorbe variaciones de carga. Define confirmaciones, reintentos, orden, expiración y dead-letter; consumidores deben tolerar mensajes duplicados y fallos parciales.

#### 18.8.09 — Distributed Systems
Distributed Systems coordina componentes que se ejecutan en nodos independientes y se comunican por redes falibles. Diseña para latencia, particiones, relojes no sincronizados y fallos parciales; no asumas transacciones locales globales.

#### 18.8.10 — API Gateway
API Gateway ofrece un punto de entrada para enrutamiento, políticas transversales y composición de APIs. Evita concentrar lógica de dominio en el gateway y limita su alcance para que no se convierta en cuello de botella.

#### 18.8.11 — Service Discovery
Service Discovery permite localizar instancias de servicios dinámicamente. Define registro, salud, expiración y autenticación de descubrimiento; protege el catálogo porque revela topología y puntos internos de la plataforma.

#### 18.8.12 — Fault Tolerance
Fault Tolerance permite que el sistema continúe ofreciendo capacidades aceptables ante fallos de componentes. Usa timeouts, retries con backoff, circuit breakers y degradación controlada; reintentos indiscriminados pueden amplificar una caída.

### Módulo 18.9 — Modelado de dominios

#### 18.9.01 — Domain-Driven Design
Domain-Driven Design alinea el diseño de software con el conocimiento del dominio y colaboración entre expertos y desarrolladores. Utiliza lenguaje compartido y límites explícitos; no es una receta de clases ni exige microservicios.

#### 18.9.02 — Entities
Entities tienen identidad persistente que las distingue aunque cambien sus atributos. Define identidad y ciclo de vida según el dominio y evita comparar entidades solo por igualdad de todos sus campos.

#### 18.9.03 — Value Objects
Value Objects representan conceptos definidos por sus valores y suelen ser inmutables. Encapsulan validación y operaciones propias, como dinero o rango de fechas, evitando tipos primitivos sin significado.

#### 18.9.04 — Aggregates
Aggregates agrupan entidades y value objects bajo una raíz que protege invariantes y límites transaccionales. Accede al conjunto a través de su raíz y evita agregados enormes que bloqueen concurrencia.

#### 18.9.05 — Repositories
Repositories ofrecen una abstracción para recuperar y persistir aggregates sin exponer detalles de almacenamiento al dominio. Define operaciones por intención del negocio y evita convertir el repositorio en un CRUD genérico sin límites.

#### 18.9.06 — Bounded Contexts
Bounded Context define un límite dentro del cual un modelo y lenguaje tienen significado consistente. Identifica contextos por capacidades y reglas; no fuerces una única definición de un término que cambia entre áreas.

#### 18.9.07 — Ubiquitous Language
Ubiquitous Language es el vocabulario compartido entre expertos del dominio y equipo técnico dentro de un contexto delimitado. Úsalo en conversaciones, código y documentación y revisa términos ambiguos con ejemplos reales.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 100 orientaciones genéricas por explicaciones específicas de cada entrada oficial. Se desarrollaron requerimientos, Scrum/Kanban, artefactos, documentación y diagramas, principios de diseño, las tres familias GoF, arquitecturas, atributos de sistemas distribuidos y modelado de dominio.

**Nota de fidelidad curricular:** las entradas «Creacionales», «Estructurales» y «Comportamiento» de 18.6 se conservan porque aparecen como elementos del roadmap; se explican como rótulos de clasificación de las familias de patrones, no como patrones individuales.

**Revisión interna:** 100/100 entradas desarrolladas y cotejadas con el roadmap. Se precisaron límites de CAP, disponibilidad/fiabilidad, microservicios, WIP, ADR y patrones; se mantuvo el enfoque de seleccionar patrones por necesidad. Pendiente: revisar diagramas con stakeholders, contrastar arquitectura con requisitos reales, probar decisiones con escenarios de carga/fallo y realizar segunda revisión técnica. No se declara implementación ni aprobación externa.
