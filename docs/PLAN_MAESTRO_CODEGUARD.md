# CodeGuard Pro — Plan maestro de desarrollo

> **Documento rector del proyecto.** Define el objetivo del producto, las fases de implementación, sus entregables, criterios de aceptación y las reglas que cualquier persona o agente de IA debe respetar al continuar el desarrollo.
>
> **Estado general:** Fase 1 completada. Fase 2 iniciada y parcialmente implementada.  
> **Repositorio:** `MaverickBms/CodeGuard-Pro`  
> **Directorio local habitual:** `~/Documentos/CodeGuard`  
> **Última actualización:** 11 de noviembre de 2026.

---

## 1. Propósito de este documento

Este archivo es la referencia central para continuar CodeGuard Pro de forma ordenada. Su objetivo es evitar que futuras intervenciones:

- Pierdan de vista el propósito educativo del producto.
- Repitan trabajo ya realizado o declaren terminadas funciones que solo tienen una estructura inicial.
- Introduzcan cambios que rompan funcionalidades, datos, estilos o temas existentes.
- Implementen sistemas de gamificación antes de consolidar el aprendizaje.
- Confundan una prueba técnica satisfactoria con la validación completa de una experiencia.
- Sobrescriban cambios locales del usuario.

**Regla principal:** antes de implementar una tarea, la IA o desarrollador debe leer este documento, inspeccionar el estado real del repositorio y actualizar el estado de la fase correspondiente. Este plan orienta el trabajo, pero no sustituye la inspección del código.

## 2. Visión del producto

CodeGuard Pro es una plataforma educativa de programación, gamificada y orientada al aprendizaje progresivo. Debe permitir que una persona aprenda fundamentos y tecnologías de programación mediante:

1. Rutas formativas organizadas por etapas, módulos y lecciones.
2. Contenido académico riguroso, explicado también en lenguaje sencillo.
3. Ejemplos de código comentados y progresivos.
4. Ejercicios y talleres que permitan demostrar el dominio.
5. Evaluaciones que midan conocimientos y competencias.
6. Un tutor de IA local que acompañe sin resolver los ejercicios por el estudiante.
7. Un sistema de progreso verificable.
8. Elementos de juego que motiven, pero que nunca sustituyan ni falseen el aprendizaje.

La experiencia debe sentirse como un producto de software educativo profesional, no como una colección de páginas independientes.

### 2.1 Principios no negociables

- **Aprendizaje primero:** el contenido, la práctica y la evaluación son el núcleo del producto.
- **Dominio demostrado:** completar una actividad exige cumplir sus criterios; abrir una lección no equivale a dominarla.
- **Progreso verificable:** el sistema determina las finalizaciones académicas a partir de resultados válidos.
- **IA como tutor:** orientar, diagnosticar y explicar; no entregar directamente las respuestas de los ejercicios.
- **Gamificación subordinada:** monedas, logros y objetos no pueden otorgar aprobaciones académicas.
- **Personalización conservada:** mantener los 12 temas visuales y permitir que cada usuario elija su apariencia.
- **Offline-first con sincronización opcional:** el núcleo académico y el progreso residen localmente. La conexión se utiliza para consultar y descargar paquetes de conocimiento aprobados; nunca debe ser requisito para estudiar ni para abrir el historial local.
- **Conocimiento trazable y vigente:** cada contenido publicado debe identificar fuentes, versión, fecha de revisión, licencia/condiciones de uso y estado de vigencia. Los cambios detectados en fuentes externas no se publican automáticamente sin revisión editorial.
- **Seguridad por diseño:** no ejecutar código arbitrario de usuarios directamente en el proceso principal del servidor o de escritorio.
- **Accesibilidad y claridad:** interfaz legible, navegación por teclado, estados comprensibles y movimiento reducido cuando se solicite.
- **Cambios incrementales:** modificar el menor alcance posible y validar antes de avanzar.

## 3. Contexto técnico y reglas de desarrollo

### 3.1 Stack conocido

- Backend: Django 5.2.19.
- Lenguaje: Python 3.14.10 en el entorno virtual del proyecto.
- Frontend: HTML, CSS y JavaScript vanilla.
- Aplicación de escritorio: Electron.
- Persistencia actual: SQLite.
- Estilos: hojas CSS propias y sistema de 12 temas.
- Ejecución local habitual: `./run.sh`.

No introducir React, Vue, Angular, Vite u otro framework frontend sin una decisión arquitectónica explícita y justificada.

### 3.2 Comandos habituales

Desde el directorio del proyecto:

```bash
cd ~/Documentos/CodeGuard
```

Activar el entorno de datos de desarrollo cuando corresponda:

```bash
export CODEGUARD_DATA_DIR="$PWD/data"
```

Ejecutar pruebas de la aplicación de rutas:

```bash
./.venv/bin/python manage.py test apps.roadmaps --settings=config.settings.development
```

Iniciar la aplicación:

```bash
./run.sh
```

**Importante:** utilizar `./.venv/bin/python` para ejecutar Django. El Python global del sistema no necesariamente contiene las dependencias del proyecto.

### 3.3 Protocolo obligatorio antes de editar

1. Leer este plan y la documentación específica de la fase.
2. Comprobar rama, estado y cambios locales:
   ```bash
   git status --short
   git branch --show-current
   git log -5 --oneline
   ```
3. Inspeccionar los archivos reales que se van a modificar y sus dependencias.
4. Identificar pruebas existentes y comportamiento esperado.
5. Proteger todos los cambios locales del usuario. No usar `git reset --hard`, `git clean -fd`, `git checkout -- .` ni `git restore` indiscriminadamente.
6. Definir alcance, archivos previstos, riesgos y criterios de aceptación.
7. Implementar en cambios pequeños y coherentes.
8. Ejecutar las pruebas pertinentes y revisar el diff.
9. Informar con precisión qué se modificó, qué se probó y qué queda pendiente.

No hacer commit, push, merge ni despliegue salvo autorización explícita del usuario. Trabajar en ramas para cambios de alcance relevante. No asumir que una rama experimental ya fue integrada.

### 3.4 Compatibilidad visual

- Los 12 temas son una característica existente y deben conservarse.
- Los componentes nuevos deben consumir tokens/variables semánticas del tema activo.
- Evitar colores fijos que anulen la personalización, salvo colores funcionales justificados (por ejemplo, estados de éxito/error con alternativas accesibles).
- Probar contraste, estados hover/focus/disabled, escritorio, tablet y móvil.
- No resolver problemas de contraste únicamente cambiando el tema o imponiendo un fondo fijo.

---

## 4. Estado actual del proyecto

### Resumen ejecutivo

| Fase | Nombre | Estado |
|---|---|---|
| 1 | Fundamentos UX/UI y experiencia base | **Completada** |
| 2 | Motor de aprendizaje y contenido interactivo | **En progreso — parcial** |
| 3 | Tutor inteligente local | Pendiente |
| 4 | Evaluaciones y progresión académica | Pendiente |
| 5 | Gamificación y economía de recompensas | Pendiente |
| 6 | Mundo, avatar, personajes e inventario | Pendiente |
| 7 | Minijuegos, desafíos y jefes | Pendiente |
| 8 | Integración, calidad, seguridad y optimización | Pendiente |

### 4.1 Fase 1 — completada

La primera fase se considera completada funcionalmente. Su objetivo fue consolidar la experiencia base de la aplicación y su sistema visual.

Alcance realizado:

- Refinamiento de la experiencia general y navegación.
- Ajustes de filtros y presentación de lecciones.
- Correcciones de sidebar, pie de página y acceso a Ajustes.
- Mejoras de adaptación responsive.
- Ajustes de contraste y coherencia para los 12 temas.
- Conservación de la personalización visual del usuario.

**Criterio de estado:** Fase 1 no debe reabrirse para rediseñar toda la aplicación sin una necesidad concreta, un defecto reproducible o una decisión acordada. Se permiten correcciones puntuales que no rompan lo ya validado.

La finalización funcional no significa que todas las combinaciones de dispositivos y temas hayan pasado una auditoría exhaustiva; las regresiones detectadas deben corregirse sin deshacer la fase.

### 4.2 Fase 2 — en progreso, implementación parcial

La Fase 2 comenzó con el primer incremento del flujo de aprendizaje.

Implementado en la base de la Fase 2 y ampliado en ramas de trabajo:

- Modelo `ContenidoLeccion` con campos para objetivos, teoría técnica, explicación sencilla, notas y publicación.
- Modelos `EjemploLeccion` y `EjercicioLeccion`.
- Página de estudio independiente por lección.
- Registro de estado **En progreso** al iniciar una lección; el inicio no completa la actividad.
- Restricción de los servicios y endpoints heredados para impedir finalizaciones manuales no demostradas.
- Presentación de contenido publicado y estados de contenido pendiente.
- Editor de texto básico para entregar respuestas/código, sin resaltado de sintaxis.
- Modelos de configuración de evaluación e intentos persistidos, con historial reciente por ejercicio.
- Evaluadores deterministas iniciales: respuesta exacta y comprobación estática de fragmentos. La coincidencia estática se distingue de la aprobación académica y no ejecuta código.
- Versiones de evaluadores conservadas y vinculadas a cada intento.
- Finalización automática condicionada a evidencia aprobada para todos los ejercicios obligatorios y a una autorización explícita del evaluador; dicha autorización está desactivada por defecto.
- Registro de auditoría de entregas y finalizaciones por evidencia.

Validación registrada:

- La suite `apps.roadmaps` pasó **29 pruebas** en la rama `phase-2/progress-domain-rules` antes de este incremento.
- Las nuevas pruebas de intentos y evaluación están añadidas en `apps/roadmaps/tests/test_attempts.py`, pero todavía requieren ejecución local.
- Último commit de referencia conocido en `main`: `dee0da9b4444ecabc5fc4dd4263296eef8361a99`.

Pendiente de la Fase 2:

- Cargar y revisar contenido académico real para las lecciones.
- Crear el catálogo de fuentes, metadatos de versión, licencia, fecha de revisión y estado de vigencia.
- Diseñar e implementar el flujo editorial de importación, validación, revisión y publicación de contenido versionado.
- Implementar el servicio central de distribución, manifiesto firmado y paquetes académicos inmutables.
- Implementar el cliente de sincronización pull-only, verificación criptográfica, instalación atómica, historial y rollback. **Este sistema está documentado y aprobado, pero todavía no está implementado.**
- Validar navegación y presentación de todos los tipos de lección.
- Incorporar resaltado de sintaxis y mejorar la experiencia del editor.
- Crear un flujo editorial versionado para configurar y publicar ejercicios/evaluadores.
- Ampliar la evaluación con pruebas funcionales seguras. No ejecutar código hasta disponer de un sandbox independiente y auditado.
- Incorporar pistas progresivas y diagnóstico en la Fase 3, no en este incremento.
- Completar la validación visual y funcional con los 12 temas y distintos tamaños de pantalla.

**No declarar Fase 2 completada** hasta cubrir los criterios académicos, técnicos, de seguridad y de validación definidos en este plan.

---

## 5. Plan detallado por fases

## Fase 1 — Fundamentos UX/UI y experiencia base

**Estado: COMPLETADA.**

### Objetivo
Establecer una base visual y de navegación coherente, adaptable y personalizable para toda la aplicación.

### Alcance
- Estructura general del dashboard y navegación.
- Sidebar, encabezados, pie de página y Ajustes.
- Vistas principales y filtros.
- Sistema de temas y contraste.
- Responsive y consistencia de componentes.

### Criterios de aceptación
- La navegación principal funciona.
- Los controles visibles llevan a acciones reales.
- Los 12 temas siguen disponibles y no presentan regresiones graves.
- La interfaz se adapta a escritorio, tablet y móvil.
- Los cambios de estilo no alteran la lógica del producto.

### Regla de cierre
No reconstruir esta fase desde cero. Las mejoras futuras se gestionan como correcciones acotadas o como parte del sistema visual de la pantalla que se esté desarrollando.

## Fase 2 — Motor de aprendizaje y contenido interactivo

**Estado: EN PROGRESO. Es la prioridad inmediata.**

### Objetivo
Convertir la ruta académica en una experiencia de estudio y práctica real, donde cada lección permita aprender, observar ejemplos y demostrar conocimientos.

### 2.1 Estructura académica

Cada ruta debe organizarse en:

- Etapas.
- Módulos dentro de cada etapa.
- Lecciones dentro de cada módulo.
- Objetivos de aprendizaje por lección.
- Contenido, ejemplos y ejercicios asociados.

La navegación debe permitir identificar dónde está el estudiante, qué requisitos tiene cada actividad y cuál es su estado.

### 2.2 Contenido de cada lección

Cuando corresponda, una lección debe contener:

1. **Objetivos:** resultados concretos que se espera alcanzar.
2. **Teoría técnica:** conceptos, terminología, sintaxis, reglas y fundamentos precisos.
3. **Explicación sencilla:** explicación pedagógica del mismo contenido, sin sacrificar exactitud.
4. **Ejemplos guiados:** código ejecutable o verificable, explicación por partes y salida esperada cuando aplique.
5. **Ejercicios y talleres:** tareas progresivas con instrucciones y criterios de evaluación.
6. **Notas y recursos:** advertencias, buenas prácticas y referencias útiles.

El contenido debe revisarse técnicamente. No rellenar lecciones con texto genérico para aparentar que están completas. Si falta contenido, indicarlo de forma honesta.

### 2.3 Editor y práctica de código

- Editor integrado con resaltado de sintaxis.
- Lenguaje y versión claramente identificados.
- Código inicial cuando el ejercicio lo requiera.
- Posibilidad de editar, ejecutar o enviar el intento según el tipo de actividad.
- Resultados comprensibles: salida, errores y pruebas superadas/fallidas.
- Historial de intentos y estado de resolución.
- Diseño adaptable y accesible.

**Seguridad:** nunca ejecutar código arbitrario directamente dentro del proceso principal de Django ni con permisos del usuario del sistema. Diseñar un entorno aislado con límites de tiempo, memoria, CPU, acceso a archivos y red. Si no existe un sandbox seguro disponible, comenzar con validadores controlados y no simular una ejecución real.

### 2.4 Progreso y dominio

- Abrir una lección puede registrarla como iniciada, pero nunca como completada.
- Guardar intentos y resultados de forma consistente.
- Una lección se completa cuando se satisfacen sus criterios académicos.
- El estudiante no puede marcar manualmente una etapa como aprobada.
- El progreso debe ser recuperable y coherente después de cerrar y volver a abrir la aplicación.
- Cada intento debe conservar la versión del contenido y del evaluador que se utilizó, para que una actualización posterior no reescriba la evidencia histórica.

### 2.5 Sistema de conocimiento académico y fuentes

El contenido de CodeGuard no se debe improvisar ni depender de que el estudiante aporte documentación. El proyecto debe mantener un catálogo editorial propio, construido a partir de fuentes técnicas confiables y de uso permitido.

Cada unidad de conocimiento debe registrar, como mínimo:

- Identificador estable y tipo de recurso (lección, ejemplo, ejercicio, referencia, aviso de obsolescencia).
- Tecnología, lenguaje, versión y nivel al que aplica.
- Fuente primaria: entidad/publicador, título, URL canónica y versión o edición consultada.
- Licencia o condiciones de reutilización; no asumir que consultar una fuente autoriza copiarla.
- Fecha de consulta, fecha de revisión técnica, responsable/revisor y estado editorial.
- Versión del contenido, fecha de publicación y compatibilidad mínima con el esquema de contenido de CodeGuard.
- Relación con objetivos de aprendizaje, lecciones, ejercicios y evaluadores correspondientes.

El contenido para estudiantes debe ser una explicación pedagógica original y revisada, apoyada por referencias. No se copiará íntegramente documentación de terceros ni se completarán lecciones con texto genérico. Las fuentes externas pueden ser consultadas automáticamente para detectar cambios, pero una persona o proceso editorial autorizado debe revisar y aprobar las modificaciones antes de publicarlas.

### 2.6 Sincronización híbrida de conocimiento (decisión aprobada)

**Modelo elegido:** servidor central de distribución de contenido revisado + sincronización automática opcional + almacenamiento local persistente. Esta capacidad forma parte de la Fase 2 y no constituye una fase adicional.

Arquitectura lógica:

1. **Equipo editorial / repositorio maestro:** crea, revisa, versiona y aprueba los paquetes académicos.
2. **Servicio central de publicación:** expone un manifiesto firmado y paquetes inmutables por HTTPS. Distribuye contenido publicado, no el progreso privado del estudiante.
3. **Cliente CodeGuard local:** consulta el manifiesto cuando hay conexión, compara versiones y descarga solo paquetes compatibles.
4. **Validador local:** verifica firma, hash, tamaño, esquema, versión mínima de aplicación y relaciones internas antes de instalar.
5. **Almacén local:** conserva la versión activa y las versiones anteriores necesarias para recuperación; la base de datos académica local y los datos del estudiante permanecen separados del paquete remoto.

Reglas obligatorias:

- La aplicación debe iniciar, estudiar, consultar lecciones descargadas, practicar con los recursos disponibles y consultar el progreso sin conexión.
- La sincronización no bloquea el arranque ni la navegación. Si falla, se conserva la última versión válida y se informa el estado sin interrumpir el estudio.
- La comprobación puede realizarse al iniciar y en momentos oportunos mientras exista conexión, con timeout, backoff y límites de consumo configurables. No se debe mantener una conexión permanente.
- El cliente solo descarga paquetes publicados y compatibles. No ejecuta scripts, migraciones ni código recibido como contenido.
- Cada paquete debe tener identificador, versión, fecha de publicación, hash criptográfico, firma verificable, versión de esquema, tamaño y requisitos de compatibilidad.
- La instalación debe ser atómica: descargar a una zona temporal, validar, activar en una transacción/control de versión y conservar rollback.
- Actualizar contenido no modifica intentos, progreso, preferencias, notas ni datos personales del estudiante.
- La evidencia académica conserva la versión del contenido y del evaluador con la que fue generada. Una actualización no convierte aprobaciones antiguas en nuevas ni elimina el historial.
- Los contenidos retirados por error crítico deben poder marcarse como retirados/sustituidos, sin borrar evidencia histórica.
- No se enviarán al servidor central código del estudiante, intentos, calificaciones, historial, identificadores personales ni telemetría. La sincronización de esta fase es de descarga de conocimiento (pull-only).
- Las credenciales, claves de firma y claves privadas de publicación nunca se distribuyen en el cliente.

La detección automática de cambios en documentación oficial solo genera alertas o propuestas para revisión. No se debe convertir una modificación de una página externa en una modificación automática de la lección publicada.

### 2.7 Flujo editorial y ciclo de vida del contenido

1. Registrar la fuente y sus condiciones de uso.
2. Consultar la versión oficial y detectar cambios relevantes.
3. Crear o actualizar la explicación, ejemplos y ejercicios de CodeGuard.
4. Revisar exactitud técnica, claridad pedagógica, vigencia, licencias y enlaces.
5. Validar ejemplos y evaluadores en el entorno de pruebas correspondiente.
6. Aprobar y publicar una nueva versión inmutable.
7. Generar manifiesto, hash y firma del paquete.
8. Distribuirlo al cliente.
9. Descargar, verificar, instalar y registrar el resultado de sincronización.
10. Si falla la validación o instalación, mantener la versión anterior y registrar el error.

La autoría masiva no debe depender de editar manualmente SQLite ni de activar `django.contrib.admin` sin una decisión de diseño. Se debe crear un flujo editorial versionado e importable, con validación previa y trazabilidad.

### 2.8 Experiencia offline y vigencia

La interfaz debe diferenciar, sin alarmismo:

- **Actualizado:** contenido local coincide con la última versión publicada conocida.
- **Actualización disponible:** existe una versión nueva que puede descargarse.
- **Sin conexión:** se usa la última versión válida local.
- **Revisión recomendada:** el contenido superó su fecha objetivo de revisión, pero no se ha confirmado que sea incorrecto.
- **Retirado o sustituido:** existe una advertencia editorial que debe mostrarse al estudiante.
- **Error de sincronización:** la versión local se conserva y el usuario puede reintentar.

La fecha de revisión no debe confundirse con la fecha de publicación ni usarse por sí sola para declarar falso un contenido. La vigencia depende también de la tecnología y versión a la que aplica.

### Criterios de aceptación de la Fase 2
- Se puede navegar desde etapa hasta lección.
- Las lecciones publicadas presentan objetivos, teoría y explicación.
- Los ejemplos y ejercicios se muestran correctamente.
- El estudiante puede realizar una práctica y recibir una evaluación reproducible.
- Los intentos se guardan.
- El sistema diferencia iniciada, pendiente, aprobada y completada según reglas definidas.
- No se otorga finalización por abrir una lección ni por pulsar un botón manual.
- La suite de pruebas cubre el flujo y los casos límite.
- La interfaz funciona con los 12 temas y en tamaños de pantalla habituales.
- Las lecciones publicadas tienen fuentes trazables, versión, fecha de revisión y estado editorial.
- El flujo editorial valida y publica paquetes versionados sin editar directamente la base de datos de producción.
- El cliente consulta un manifiesto central únicamente cuando hay conexión y no depende de él para arrancar o estudiar.
- Los paquetes se validan criptográficamente y por esquema antes de activarse.
- Una descarga incompleta, firma inválida, versión incompatible o error de instalación no reemplaza el contenido local válido.
- La actualización no modifica el progreso, los intentos ni las preferencias del estudiante.
- Los intentos mantienen la versión de contenido/evaluador que los originó.
- Se puede demostrar el flujo de actualización, rollback y continuidad offline mediante pruebas.

## Fase 3 — Tutor inteligente local

**Estado: PENDIENTE. Depende de la estructura de ejercicios y resultados de la Fase 2.**

### Objetivo
Ofrecer acompañamiento pedagógico personalizado sin sustituir el razonamiento del estudiante.

### Capacidades requeridas
- Explicar errores de sintaxis, lógica y enfoque.
- Analizar el intento y relacionarlo con el objetivo del ejercicio.
- Proporcionar orientación gradual.
- Dar un máximo de **tres pistas por ejercicio**.
- Evitar revelar la solución completa o entregar el código final.
- Recomendar conceptos o lecciones para repasar.
- Ajustar la explicación al nivel del estudiante.
- Funcionar localmente siempre que la arquitectura y el modelo disponible lo permitan.

### Comportamiento de las pistas
1. Primera pista: orientar hacia el concepto o zona relevante.
2. Segunda pista: precisar el enfoque o estrategia posible.
3. Tercera pista: dar una orientación más concreta sin escribir la solución completa.

Las pistas deben ser progresivas, estar vinculadas al ejercicio y no reiniciarse para evadir el límite sin una regla explícita.

### Seguridad y privacidad
- No enviar código, datos personales ni historial a servicios externos sin consentimiento.
- No confiar en la IA para decidir por sí sola una aprobación académica.
- La evaluación determinista del ejercicio debe ser la fuente de verdad; el tutor explica el resultado.
- Definir límites de contexto, tiempo y recursos del modelo local.
- Mostrar con claridad cuándo una respuesta procede del tutor y cuándo de un validador automático.

### Criterios de aceptación
- El tutor explica errores reproducibles.
- Respeta el límite de tres pistas.
- No entrega directamente la solución.
- Puede funcionar sin conexión si el modelo local está disponible.
- Sus recomendaciones no alteran directamente las calificaciones ni la progresión.

## Fase 4 — Evaluaciones y progresión académica

**Estado: PENDIENTE. Depende de los resultados fiables de las Fases 2 y 3.**

### Objetivo
Medir el aprendizaje de manera consistente y controlar la progresión por dominio demostrado.

### Evaluaciones por módulo
- Cada módulo debe disponer de un quiz de **al menos 15 preguntas**.
- Preguntas vinculadas a objetivos y contenidos del módulo.
- Mezcla razonable de formatos: selección, respuesta, interpretación de código y resolución de problemas, según las capacidades disponibles.
- Corrección automática cuando sea objetiva y revisión controlada cuando sea necesario.
- Resultado, retroalimentación y temas que requieren repaso.

### Evaluaciones por etapa
Cada etapa debe incluir:

- Un examen de conocimientos.
- Un proyecto o desafío práctico que demuestre aplicación.
- Criterio de aprobación de **mínimo 70 %**.
- Registro de intentos y resultados.
- Diagnóstico de debilidades y recomendaciones de recuperación cuando no se apruebe.

No permitir que el usuario se autoconceda la aprobación de una etapa.

### Homologación
El examen de etapa también debe estar disponible desde Evaluaciones para que una persona pueda demostrar conocimientos previos. Si aprueba y cumple los requisitos definidos, el sistema puede homologar la etapa y completar las unidades académicas correspondientes. La homologación debe registrar el origen y resultado de la evaluación.

### Reglas de progresión
- Las lecciones se completan por dominio demostrado.
- Los módulos se completan cuando se cumplen sus requisitos.
- Las etapas se aprueban al satisfacer el examen, proyecto y requisitos establecidos.
- Las recompensas del juego nunca modifican estos resultados.
- Reintentos y recuperación deben ser transparentes y estar documentados.

### Criterios de aceptación
- Hay al menos 15 preguntas por quiz de módulo.
- Los exámenes de etapa aplican el umbral del 70 %.
- El suspenso produce diagnóstico y ruta de repaso.
- La homologación utiliza el mismo estándar de evaluación.
- Las transiciones académicas se realizan automáticamente y quedan auditadas.
- No existen rutas de API o acciones de interfaz que permitan falsear resultados.

## Fase 5 — Gamificación y economía de recompensas

**Estado: PENDIENTE. Implementar después de consolidar aprendizaje y evaluación.**

### Objetivo
Aumentar la motivación, continuidad y reconocimiento del esfuerzo sin convertir las recompensas en sustituto del aprendizaje.

### Sistemas previstos
- Logros y medallas por hitos verificables.
- Misiones diarias, semanales y de progreso.
- Rachas de estudio.
- Moneda virtual ganada mediante actividades.
- Recompensas por constancia, práctica y dominio.
- Inventario de objetos con rangos: cobre, plata, oro, diamante, legendario y arcano.
- Protectores de racha poco frecuentes y obtenidos por mérito.
- Historial de recompensas y transacciones.

### Reglas de economía
- Definir fuentes y usos de cada moneda.
- Evitar inflación, recompensas desproporcionadas y ventajas de pago.
- No vender resultados académicos, aprobaciones ni pistas que resuelvan ejercicios.
- Las recompensas aleatorias, si se implementan, deben ser cosméticas, transparentes y ganadas mediante juego; no usar cajas de botín pagadas.
- No introducir apuestas con dinero real ni mecánicas de casino dirigidas a menores.
- Las recompensas no deben castigar de forma desproporcionada una pausa o una racha perdida.

### Criterios de aceptación
- Cada recompensa tiene una condición verificable.
- El saldo y el inventario son consistentes y auditables.
- No se puede duplicar una recompensa mediante peticiones repetidas.
- La economía no altera el progreso académico.
- Las mecánicas respetan privacidad, edad y bienestar del usuario.

## Fase 6 — Mundo, avatar, personajes e inventario

**Estado: PENDIENTE. Depende de la Fase 5.**

### Objetivo
Dar identidad y continuidad narrativa al recorrido de aprendizaje.

### Sistemas previstos
- Mapa de progreso con una presentación inspirada en rutas de aventura.
- Mundos o zonas asociadas a etapas y competencias.
- Personaje guía por etapa.
- Avatar personalizable.
- Especies, clases y decisiones evolutivas cosméticas o narrativas.
- Inventario y equipamiento visual.
- Objetos con rangos y descripciones claras.
- Desbloqueos asociados a logros y dominio académico.

### Reglas
- El mapa representa el progreso real; no debe mostrar etapas aprobadas sin evaluación.
- El avatar y los objetos no otorgan ventajas injustas en exámenes.
- Las decisiones evolutivas deben explicarse antes de confirmarse y no bloquear el aprendizaje.
- El usuario debe poder revisar su inventario y el origen de los objetos.

### Criterios de aceptación
- El mapa refleja la estructura académica real.
- Desbloqueos y recompensas son consistentes.
- Personalización e inventario persisten correctamente.
- La experiencia es usable con teclado y pantallas pequeñas.

## Fase 7 — Minijuegos, desafíos y jefes

**Estado: PENDIENTE.**

### Objetivo
Reforzar conceptos mediante experiencias breves, interactivas y relacionadas directamente con competencias de programación.

### Sistemas previstos
- Minijuegos de lógica, sintaxis, depuración, algoritmos y lectura de código.
- Desafíos por nivel de dificultad.
- Dificultad adaptativa basada en desempeño real.
- Jefes o retos integradores al cerrar unidades o etapas.
- Recompensas cosméticas y educativas por resultados.
- Registro de intentos, rendimiento y conceptos practicados.

### Reglas pedagógicas
- Cada juego debe declarar qué competencia practica.
- La dificultad adaptativa debe poder explicarse y no penalizar injustamente.
- Un minijuego no sustituye el examen formal de una etapa.
- Evitar que la velocidad sea el único indicador de dominio.
- Ofrecer alternativas accesibles para personas que no puedan usar interacciones basadas en tiempo o movimiento.

### Criterios de aceptación
- Los juegos tienen reglas, objetivos y criterios de resultado claros.
- Las actividades refuerzan competencias del plan académico.
- El sistema registra resultados sin duplicar recompensas.
- La dificultad se adapta de forma verificable.

## Fase 8 — Integración, calidad, seguridad y optimización

**Estado: PENDIENTE. Es una fase transversal de estabilización; también debe acompañar las anteriores.**

### Objetivo
Consolidar el producto completo para que sea estable, seguro, accesible, eficiente y confiable en modo local.

### Áreas de trabajo

**Calidad funcional**
- Pruebas unitarias, de integración y de extremo a extremo.
- Flujos completos de usuario.
- Migraciones y consistencia de datos.
- Manejo de errores y recuperación.
- Pruebas de regresión de las funciones existentes.

**Seguridad**
- Autenticación, autorización y protección de datos.
- Validación de entradas y protección contra XSS, CSRF, inyección y acceso indebido.
- Aislamiento de ejecución de código.
- Protección de secretos y configuración.
- Auditoría de acciones sensibles y transacciones de recompensas.
- Dependencias actualizadas y revisión de vulnerabilidades.

**Accesibilidad**
- Contraste WCAG aplicable.
- Navegación completa por teclado.
- Foco visible.
- Etiquetas accesibles y semántica correcta.
- Compatibilidad con lectores de pantalla.
- Respeto a `prefers-reduced-motion`.

**Rendimiento y experiencia**
- Tiempos de carga y respuesta.
- Optimización de consultas y recursos.
- Gestión eficiente del almacenamiento local.
- Comportamiento responsive.
- Estados de carga, vacío, éxito y error consistentes.

**Offline-first y sincronización de conocimiento**
- Definir y probar qué funciones funcionan sin conexión.
- Persistir progreso, intentos, preferencias y contenido local de forma segura.
- Verificar manifiestos, firmas, hashes, compatibilidad y límites de descarga.
- Probar instalaciones atómicas, interrupciones, reintentos, rollback y recuperación.
- Garantizar que la sincronización de contenido no suba datos personales ni académicos del estudiante.
- Resolver sincronización y conflictos entre dispositivos solo si se aprueba en una decisión futura; no forma parte del sincronizador de contenido de la Fase 2.
- Comunicar claramente las funciones que sí requieren conexión.

**Compatibilidad**
- Aplicación web/local y empaquetado Electron.
- Sistemas operativos soportados.
- Diferentes resoluciones y densidades de pantalla.
- Los 12 temas y sus combinaciones principales.

### Criterios de aceptación
- Flujos críticos cubiertos por pruebas.
- Sin errores críticos conocidos.
- Datos y progreso sobreviven reinicios.
- Ejecución de código aislada o deshabilitada si no se puede garantizar la seguridad.
- Auditoría de accesibilidad y responsive completada.
- Modo offline documentado y probado.
- Documentación de instalación, operación y recuperación actualizada.

---

## 6. Dependencias y orden de ejecución

El orden recomendado es:

```text
FASE 1 — UX/UI base [COMPLETADA]
             |
             v
FASE 2 — Motor de aprendizaje [EN PROGRESO]
             |
             +----------+
             |          |
             v          v
FASE 3 — Tutor IA     FASE 4 — Evaluaciones
             |          |
             +-----+----+
                   |
                   v
          FASE 5 — Gamificación
                   |
                   v
       FASE 6 — Mundo y personalización
                   |
                   v
        FASE 7 — Minijuegos y desafíos
                   |
                   v
        FASE 8 — Integración y calidad
```

La Fase 8 no debe aplazarse por completo hasta el final: seguridad, accesibilidad, pruebas y rendimiento deben revisarse en cada fase. El diagrama representa la secuencia de entregas principales, no una prohibición de trabajo transversal.

## 7. Priorización inmediata

La siguiente tarea no es construir el tutor ni añadir recompensas. Es cerrar correctamente el núcleo de aprendizaje.

Orden inmediato recomendado:

1. Revisar visual y funcionalmente la página de lección existente.
2. Consolidar su diseño para escritorio, tablet y móvil, manteniendo los 12 temas.
3. Definir el modelo editorial, las fuentes y los metadatos de vigencia.
4. Diseñar e implementar la publicación central y la sincronización híbrida de paquetes académicos.
5. Producir contenido real, revisado y trazable para las rutas prioritarias.
6. Definir el contrato de ejecución y evaluación segura de ejercicios.
7. Implementar editor, navegación y flujo de intentos.
8. Crear validadores automáticos y pruebas, incluyendo offline, integridad, rollback y compatibilidad.
9. Conectar resultados con la finalización automática de lecciones.
10. Cerrar Fase 2 mediante criterios de aceptación y documentación.
11. Comenzar Fase 3: tutor local.

### Nota sobre el rediseño visual de la página de lección

Existe una rama de trabajo experimental llamada `ui/redesign-learning-experience`, creada para refinar `templates/roadmaps/leccion.html` y `static/css/lesson-learning.css`. Sus cambios no deben considerarse integrados ni validados hasta revisar el diff, probar la aplicación en navegador, verificar los temas y ejecutar las pruebas. No asumir que esa rama está desplegada o fusionada en `main`.

---

## 8. Definición de terminado para cualquier tarea

Una tarea solo puede marcarse como terminada cuando:

- Cumple el objetivo descrito.
- Respeta el alcance y las restricciones.
- No rompe funcionalidades relacionadas.
- Tiene pruebas adecuadas o una explicación explícita de por qué no son aplicables.
- Se verificó el resultado visual cuando afecta la interfaz.
- Se actualizó la documentación pertinente.
- Se reportaron limitaciones y trabajo pendiente.

Usar estos estados en los informes:

- **Pendiente:** no iniciado.
- **En análisis:** inspección y diseño en curso.
- **En implementación:** cambios en desarrollo.
- **Implementado, sin validar:** existe código, pero falta comprobación.
- **Validado:** pruebas y verificaciones definidas pasaron.
- **Bloqueado:** existe una dependencia o problema que impide continuar.
- **Completado:** criterios de aceptación satisfechos y documentación actualizada.

No confundir “implementado” con “validado” ni “validado” con “desplegado”.

## 9. Protocolo de continuidad para cualquier IA

Toda IA que reciba este repositorio debe seguir este procedimiento:

### Antes de comenzar
1. Leer `docs/PLAN_MAESTRO_CODEGUARD.md`.
2. Leer la documentación de la fase activa, especialmente `docs/FASE_2_APRENDIZAJE.md` para la Fase 2.
3. Inspeccionar rama, commits, cambios locales y estructura real del proyecto.
4. Verificar si el estado descrito aquí sigue vigente.
5. Identificar la tarea más pequeña que aporte valor a la fase activa.

### Durante el trabajo
1. Mantener el foco en la fase activa y sus dependencias.
2. No introducir funciones de fases posteriores como atajos que comprometan la arquitectura.
3. No inventar modelos, campos, rutas, comandos ni resultados: inspeccionar antes.
4. Respetar el stack y los 12 temas.
5. No alterar el progreso académico sin reglas y pruebas.
6. Separar validación determinista de recomendaciones generadas por IA.
7. Mantener los cambios acotados y reversibles.

### Al terminar
Entregar un informe con:

- Fase y tarea trabajada.
- Estado anterior y posterior.
- Archivos modificados.
- Decisiones técnicas y motivos.
- Pruebas ejecutadas y resultado exacto.
- Verificaciones visuales realizadas.
- Riesgos o limitaciones pendientes.
- Siguiente tarea recomendada.

Actualizar este plan cuando cambie el estado real de una fase. No marcar una fase completa por conveniencia ni eliminar requisitos acordados sin autorización del usuario.

---

## 10. Instrucción rectora

**CodeGuard Pro debe convertirse en una plataforma seria para aprender programación, con una experiencia visual atractiva y elementos de juego bien integrados. La gamificación debe reforzar el aprendizaje, nunca reemplazarlo.**

La prioridad actual es completar la **Fase 2** con contenido de calidad, práctica verificable y progreso automático. Las fases posteriores deben construirse sobre ese núcleo, sin perder seguridad, accesibilidad, funcionamiento local ni personalización visual.

Ante cualquier duda o conflicto entre una mejora llamativa y la integridad del aprendizaje, debe prevalecer la integridad del aprendizaje.
