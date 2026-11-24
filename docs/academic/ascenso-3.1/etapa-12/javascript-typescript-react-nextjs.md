# Etapa 12 — JavaScript, TypeScript y frameworks frontend

**Prioridad:** P1 · Obligatoria  
**Estado editorial:** en desarrollo; no aprobado ni publicado.  
**Objetivo oficial:** convertirte en un desarrollador frontend capaz de construir aplicaciones interactivas.  
**Proyecto oficial:** dashboard administrativo con autenticación visual, formularios, paneles, tablas, filtros y consumo de APIs.

## Resultados de aprendizaje
Al terminar, el estudiante podrá escribir JavaScript moderno, manipular el DOM, coordinar operaciones asíncronas, utilizar Web APIs con criterio de seguridad, modelar datos con TypeScript estricto, construir interfaces React y Next.js y preparar un flujo de trabajo frontend reproducible.

## 12.1 — JavaScript

### Variables, tipos y operadores
JavaScript es dinámico. Usa const cuando no necesites reasignar el identificador y let cuando sí; const no vuelve inmutable el objeto apuntado. Evita var en código nuevo por su alcance de función y sus reglas de hoisting. Tipos primitivos: string, number, bigint, boolean, undefined, symbol y null. Objetos, arrays y funciones son referencias.

Comprende operadores aritméticos, comparación, lógicos, asignación, ternario, optional chaining y nullish coalescing. Prefiere igualdad estricta y conversiones explícitas. || opera mediante truthiness; ?? solo sustituye null y undefined. Number usa representación IEEE 754, por lo que algunos decimales no son exactos.

### Control de flujo y funciones
Practica if/else, switch, for, while, for...of y for...in. Elige for...of para recorrer valores iterables; for...in enumera claves y no suele ser la opción correcta para arrays. Estudia declaración de función, expresión, arrow function, parámetros, argumentos, retorno, parámetros por defecto y funciones de orden superior. Las arrow functions heredan this léxicamente; las funciones tradicionales tienen this dependiente de invocación.

### Objetos, arrays y strings
Aprende propiedades, métodos, iteración, map, filter, reduce, find, some y every. Los strings son inmutables. Destructuring extrae valores; spread expande; rest agrupa elementos restantes. La copia mediante spread es superficial: objetos anidados conservan referencias compartidas.

### Scope, closures y hoisting
El scope determina dónde se resuelven identificadores. Estudia alcance global, de función y de bloque, shadowing y zona temporal muerta de let/const. Hoisting describe el procesamiento de declaraciones antes de ejecutar; no implica que toda variable pueda usarse antes de inicializarse. Una closure conserva el entorno léxico donde se creó y permite encapsular estado.

### Prototypes, this, ES6+ y módulos
JavaScript delega propiedades mediante cadenas de prototipos. La sintaxis class se apoya en ese modelo. Comprende this según contexto de invocación y el comportamiento léxico de arrow functions. ES6+ reúne mejoras como let/const, módulos, destructuring, template literals, clases y Promises. Usa import/export para dependencias explícitas; distingue módulos ES y CommonJS.

**Ejercicio:** crea un módulo de inventario con funciones puras para agregar, filtrar y calcular valor de productos. Prueba arrays vacíos, duplicados y entradas inválidas.

## 12.2 — DOM
El Document Object Model representa el documento como un árbol de nodos. Selecciona con querySelector/querySelectorAll y modifica nodos de forma controlada. Prefiere textContent para texto no confiable; innerHTML interpreta marcado y puede introducir XSS. Para contenido dinámico, crea nodos y asigna propiedades seguras.

Registra eventos con addEventListener. Comprende bubbling, capturing, event.target, currentTarget, preventDefault y stopPropagation. La delegación coloca un manejador en un ancestro y determina el elemento mediante closest. No detengas propagación sin una razón clara.

Los formularios deben tener labels, validación accesible y mensajes asociados a campos. La validación del cliente mejora experiencia, pero el servidor debe volver a validar porque el navegador puede manipularse.

**Ejercicio:** crea una lista de tareas accesible con alta, edición, eliminación y filtros; utiliza delegación y evita insertar HTML no confiable.

## 12.3 — Asincronía
Distingue ejecución síncrona y asíncrona. Los callbacks permiten ejecutar lógica posteriormente, pero su anidamiento excesivo dificulta control de errores. Una Promise representa una operación futura con estados pendiente, cumplida o rechazada. Usa then/catch/finally o async/await con try/catch/finally.

Fetch normalmente no rechaza por estados HTTP 404 o 500; verifica response.ok. Comprende Event Loop, microtasks y tareas del host; las continuaciones de Promise se procesan como microtasks. No memorices una simplificación que ignore las reglas del navegador o Node.

Una race condition ocurre cuando el resultado depende del orden temporal de operaciones. Mitiga con AbortController, identificadores de solicitud, invalidación de resultados o coordinación explícita.

**Ejercicio:** implementa búsqueda con debounce, cancelación de solicitudes anteriores, estados de carga y error, y pruebas con respuestas simuladas fuera de orden.

## 12.4 — Web APIs
- Fetch API: solicitudes HTTP, cancelación, validación de estado y parseo.
- LocalStorage: persistencia de cadenas por origen; no almacenar secretos ni tokens sensibles por defecto.
- SessionStorage: almacenamiento de sesión por origen y contexto de pestaña; tampoco es un almacén seguro.
- Cookies: atributos Secure, HttpOnly y SameSite según el diseño. Una cookie HttpOnly no es accesible desde JavaScript.
- Geolocation: requiere permiso y contexto seguro en navegadores modernos; solicita solo lo necesario.
- Clipboard: puede requerir permiso o activación del usuario; gestiona rechazo.
- File API: trabaja con archivos seleccionados por el usuario; accept no es una barrera de seguridad y el servidor debe validar.

**Ejercicio:** importa un JSON elegido por el usuario, valida su estructura, presenta una vista previa y permite descargar un reporte sin subir el archivo a terceros.

## 12.5 — TypeScript
TypeScript añade análisis estático y se transforma a JavaScript. Los tipos se eliminan en compilación: no validan datos externos en runtime. Estudia inferencia, anotaciones, tipos primitivos, arrays, tuplas, objetos, funciones, propiedades opcionales y readonly.

Compara interface y type: interfaces describen contratos de objetos y admiten extensión; type permite uniones, intersecciones, tuplas y aliases. Union types expresan alternativas; intersection types combinan requisitos. Aprende narrowing con typeof, in, discriminantes y type guards.

Los genéricos conservan relaciones entre tipos; añade restricciones con extends cuando corresponda. Utility types habituales: Partial, Required, Pick, Omit, Record, Readonly y ReturnType. Comprende enums y cuándo una unión literal es más simple. Activa strict y evita any; usa unknown en fronteras no confiables.

La tipificación no sustituye validación runtime. Valida JSON, formularios y respuestas de API con esquemas o validadores explícitos.

**Ejercicio:** modela productos, usuarios, filtros, respuestas paginadas y errores de API; valida en runtime un JSON externo y documenta por qué el tipo estático no basta.

## 12.6 — React
React construye interfaces mediante componentes. JSX es sintaxis transformada, no HTML literal. Props transmiten datos y deben tratarse como inmutables. State representa información que afecta renderizado; actualiza objetos y arrays creando nuevas referencias. Usa actualizaciones funcionales cuando el nuevo estado depende del anterior.

Los Hooks se llaman en el nivel superior de componentes o Hooks propios. useState conserva estado; useEffect sincroniza con sistemas externos y debe incluir dependencias correctas y limpieza; useContext comparte valores; useRef conserva una referencia mutable sin provocar renderizado. No uses useEffect para derivar datos que pueden calcularse durante render.

Estudia formularios controlados y no controlados, routing, elevación de estado, Context API, custom Hooks y Error Boundaries. Estos últimos aíslan ciertos errores de renderizado, pero no capturan automáticamente todos los errores asíncronos o de eventos. Diseña estados loading, empty, success y error.

**Ejercicio:** implementa Dashboard, SummaryCard, ProductTable, SearchFilters, ProductForm y ErrorPanel, separando presentación, estado y acceso a API.

## 12.7 — Next.js
App Router organiza rutas mediante el sistema de archivos y convenciones como page, layout, loading, error y not-found. Comprende rutas dinámicas y layouts anidados.

En App Router, los Server Components son el modelo predeterminado para componentes compatibles. Los Client Components se utilizan cuando hacen falta estado, efectos, eventos o APIs del navegador. Marca la frontera cliente-servidor deliberadamente; no conviertas toda la aplicación en cliente por comodidad. No expongas secretos en módulos enviados al navegador.

Distingue renderizado en servidor, generación estática y renderizado dinámico según la versión y configuración. Aprende data fetching, caché y revalidación de la versión objetivo. La autenticación y autorización deben validarse en servidor: ocultar botones no protege datos. Configura metadata, variables privadas/públicas, build reproducible, headers y registros.

**Ejercicio:** migra una vista del dashboard a App Router, manteniendo datos privados en servidor y tabla interactiva en cliente. Justifica cada frontera.

## 12.8 — Herramientas
- npm y pnpm: gestores de paquetes, scripts, lockfiles y dependencias transitivas. No mezcles gestores sin política explícita.
- Vite: servidor de desarrollo y herramienta de build; distingue desarrollo de producción.
- ESLint: análisis estático; no desactives reglas sin justificación.
- Prettier: formato consistente; no sustituye revisión ni lint.
- Tailwind CSS: utilidades de estilo y tokens coherentes; sigue la guía de la versión elegida.
- React DevTools: inspecciona árbol, props, estado y renderizados; no expongas datos sensibles.

Flujo recomendado: instalar desde lockfile, ejecutar lint, comprobación de tipos, pruebas y build; revisar consola/red; probar teclado, formularios, estados vacíos y errores; documentar versiones y comandos.

## Proyecto oficial — Dashboard administrativo
Construye un dashboard para un negocio ficticio con autenticación visual, formularios, paneles, tablas, filtros y consumo de APIs.

Requisitos:
1. Indicadores calculados desde datos trazables.
2. Tabla de productos con búsqueda, filtros, orden y paginación.
3. Alta y edición con validación.
4. Detalle con estados loading, empty y error.
5. Consumo de API documentada.
6. Manejo de errores HTTP, cancelación y respuestas inesperadas.
7. Navegación y rutas inexistentes.
8. Diseño responsive y accesible por teclado.
9. Separación entre tipos, componentes, servicios y estado.
10. Si la autenticación es simulada, declararlo; no afirmar que protege recursos.
11. Una vista React y una vista Next.js que documente frontera servidor/cliente.
12. Pruebas de lógica, componentes y flujos críticos.

Entregables: repositorio y README; diagrama de componentes y flujo; modelos TypeScript y validadores runtime; evidencia de pruebas/build; matriz de estados; informe de accesibilidad y seguridad; capturas sin secretos; decisiones y limitaciones.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| JavaScript y DOM | 15 |
| Asincronía y errores | 15 |
| TypeScript y validación runtime | 15 |
| React: componentes, estado y Hooks | 20 |
| Next.js y frontera servidor/cliente | 10 |
| Herramientas y reproducibilidad | 10 |
| Accesibilidad, seguridad y UX | 10 |
| Pruebas y documentación | 5 |

Criterio orientativo: 80/100 y ningún fallo crítico de seguridad, pérdida de datos o bloqueo de flujo principal.

## Autoevaluación
1. ¿Por qué const no hace inmutable un objeto?
2. ¿Qué diferencia existe entre ?? y ||?
3. ¿Qué problema resuelve una closure?
4. ¿Por qué innerHTML con datos no confiables es peligroso?
5. ¿Qué diferencia hay entre target y currentTarget?
6. ¿Por qué fetch puede resolver ante HTTP 404?
7. ¿Qué es una race condition y cómo cancelarías una solicitud obsoleta?
8. ¿Por qué TypeScript no valida una respuesta JSON en runtime?
9. ¿Cuándo usarías useEffect?
10. ¿Qué información debe permanecer en el servidor en Next.js?

## Recursos audiovisuales
No se aprueban videos en esta versión. Se incorporarán solo tras confirmar audio hablado en español y relación directa con el subtema (closures, Event Loop, TypeScript generics, React Hooks, etc.). Un curso general no se asignará indiscriminadamente a todos los apartados.

## Referencias oficiales
- ECMAScript: https://tc39.es/ecma262/
- MDN JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- MDN DOM: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
- MDN Fetch: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- MDN Web APIs: https://developer.mozilla.org/en-US/docs/Web/API
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- React: https://react.dev/learn
- Next.js: https://nextjs.org/docs
- Vite: https://vite.dev/guide/
- npm: https://docs.npmjs.com/
- pnpm: https://pnpm.io/
- ESLint: https://eslint.org/docs/latest/
- Prettier: https://prettier.io/docs/
- Tailwind CSS: https://tailwindcss.com/docs

**Consulta documental:** 2026-11-19. **Verificación práctica:** ejemplos y proyecto no ejecutados en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 12

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados desarrollan las lecciones a partir del contenido conceptual de esta guía; no representan evaluación, aprobación ni ejecución práctica.

### Módulo 12.1 — JavaScript

#### 12.1.01 — Variables
`let`, `const` y `var` declaran enlaces con reglas distintas de ámbito y reasignación. Prefiere `const` cuando no reasignas, `let` cuando sí y evita `var` en código moderno; recuerda que `const` no vuelve inmutable un objeto.

#### 12.1.02 — Tipos
JavaScript es dinámicamente tipado: un valor tiene tipo en tiempo de ejecución y una variable puede referirse a valores de tipos distintos. Distingue `undefined`, `null`, boolean, number, bigint, string, symbol y object; usa comprobaciones explícitas al validar entradas externas.

#### 12.1.03 — Operadores
Los operadores realizan operaciones aritméticas, comparación, asignación, lógica y acceso. Comprende precedencia, coerción y diferencia entre `===` y `==`; usa comparación estricta por defecto y agrupa expresiones complejas para hacer visible la intención.

#### 12.1.04 — Condicionales
Las condicionales ejecutan rutas según una expresión booleana mediante `if`, `else` o `switch`. Convierte las reglas del negocio en condiciones mutuamente comprensibles y prueba valores ausentes, límites y tipos inesperados.

#### 12.1.05 — Bucles
Los bucles `for`, `while`, `do...while` y `for...of` repiten operaciones bajo distintos criterios. Selecciona el bucle según si recorres una colección o esperas una condición, y evita mutar la colección mientras la iteras sin comprender el efecto.

#### 12.1.06 — Funciones
Una función encapsula comportamiento y puede recibir parámetros y devolver un valor. JavaScript admite declaraciones, expresiones y funciones flecha; elige nombres descriptivos, define contratos de entrada/salida y evita mezclar cálculo, acceso a red y manipulación visual en una sola función.

#### 12.1.07 — Objetos
Los objetos agrupan propiedades y métodos y pueden crearse con literales, constructores o clases. Accede de forma segura a propiedades opcionales, evita asumir que datos JSON externos tienen la forma esperada y valida el contrato antes de utilizarlos.

#### 12.1.08 — Arrays
Los arrays son colecciones ordenadas con métodos de iteración, transformación y búsqueda. Practica `map`, `filter`, `reduce`, `find` y `some`; distingue métodos que mutan el array de los que producen uno nuevo y no uses índices como identificadores persistentes.

#### 12.1.09 — Strings
Las cadenas son secuencias UTF-16 y ofrecen métodos de búsqueda, extracción y transformación. Ten presente que longitud e índices no siempre equivalen a caracteres visuales Unicode; valida y normaliza texto según el requisito de la aplicación.

#### 12.1.10 — Destructuring
Destructuring extrae valores de arrays u objetos en variables mediante patrones. Permite asignar valores predeterminados y renombrar propiedades; úsalo para hacer explícita la forma de los datos, sin ocultar estructuras complejas en una sola línea.

#### 12.1.11 — Spread
Spread (`...`) expande elementos iterables o propiedades enumerables en un nuevo array u objeto. Es una copia superficial: los objetos anidados siguen compartiendo referencias, por lo que no garantiza inmutabilidad profunda.

#### 12.1.12 — Rest
Rest (`...`) agrupa los argumentos restantes o propiedades no extraídas en una nueva colección. En parámetros de función debe ser el último parámetro; úsalo para APIs flexibles sin perder claridad sobre qué argumentos son obligatorios.

#### 12.1.13 — Scope
Scope determina dónde puede resolverse un identificador: global, de función o de bloque. `let` y `const` tienen ámbito de bloque y zona temporal muerta; limita variables al menor ámbito útil para reducir efectos colaterales.

#### 12.1.14 — Closures
Una closure conserva acceso al entorno léxico donde se creó una función, incluso después de terminar la función externa. Es útil para encapsular estado y crear funciones especializadas; controla referencias retenidas para no mantener memoria innecesaria.

#### 12.1.15 — Hoisting
Hoisting describe cómo el motor procesa declaraciones antes de ejecutar el código, pero no significa que todas las variables puedan usarse antes de declararse. Las declaraciones `var`, `let`, `const` y `function` tienen reglas distintas; escribe declaraciones antes de su uso.

#### 12.1.16 — Prototypes
Los prototypes permiten delegar la búsqueda de propiedades a otros objetos y forman la base de la herencia basada en prototipos. Comprende `Object.getPrototypeOf` y la cadena de prototipos; evita modificar prototipos globales de objetos nativos.

#### 12.1.17 — This
`this` se determina principalmente por cómo se invoca una función, no por dónde se declara; las funciones flecha capturan `this` léxico. Analiza llamadas como método, función independiente, constructor y `bind` para evitar referencias inesperadas.

#### 12.1.18 — ES6+
ES6+ agrupa mejoras del lenguaje como `let`/`const`, funciones flecha, clases, módulos, destructuring, iteradores y promesas. No trates la etiqueta como una versión única: verifica compatibilidad del runtime y del navegador objetivo antes de utilizar una API.

#### 12.1.19 — Modules
Los módulos separan código mediante `export` e `import`, con ámbitos propios y dependencias explícitas. Define una interfaz pública pequeña, evita ciclos innecesarios y distingue módulos ECMAScript de formatos históricos como CommonJS.

### Módulo 12.2 — DOM

#### 12.2.01 — Document Object Model
El DOM representa el documento como un árbol de nodos que scripts pueden consultar y modificar. Comprende la diferencia entre HTML fuente y DOM vivo, y evita asumir que la estructura permanece igual después de scripts, componentes o interacciones.

#### 12.2.02 — Selección de elementos
La selección de elementos utiliza APIs como `getElementById`, `querySelector` y `querySelectorAll`. Prefiere selectores específicos y comprueba si la búsqueda devuelve `null` o una colección vacía antes de modificar nodos.

#### 12.2.03 — Manipulación del DOM
Manipular el DOM incluye crear, insertar, actualizar y eliminar nodos y atributos. Usa `textContent` para texto no confiable, evita insertar HTML sin sanitización y agrupa cambios cuando sea posible para reducir trabajo de renderizado.

#### 12.2.04 — Eventos
Un evento representa una interacción o suceso como clic, teclado, envío o carga. Identifica el objetivo, la fase de propagación y el contexto; no supongas que todos los eventos se comportan igual en ratón, teclado y pantallas táctiles.

#### 12.2.05 — Event listeners
`addEventListener` registra una función para responder a un evento y permite opciones como `once`, `capture` y `signal`. Retira listeners cuando su ciclo de vida termina o usa una señal de aborto para evitar fugas y respuestas duplicadas.

#### 12.2.06 — Event bubbling
Event bubbling describe cómo muchos eventos se propagan desde el objetivo hacia sus ancestros. `event.target` identifica el origen y `currentTarget` el nodo que ejecuta el listener; detén propagación solo cuando exista una razón funcional clara.

#### 12.2.07 — Event delegation
Event delegation coloca un listener en un ancestro para gestionar eventos de varios descendientes. Es útil para listas dinámicas; filtra el objetivo con `closest`, verifica que pertenezca al contenedor y considera eventos que no hacen bubbling.

#### 12.2.08 — Formularios
Los formularios del DOM exponen controles, valores y eventos de envío. Gestiona `submit` en el formulario, permite la interacción por teclado y evita depender únicamente del clic del botón; el servidor debe volver a validar todos los datos.

#### 12.2.09 — Validaciones
La validación de formularios combina restricciones nativas, lógica de interfaz y validación de servidor. Comunica el campo, el motivo y cómo corregirlo; normaliza entradas y nunca uses validación cliente como control de seguridad.

### Módulo 12.3 — Asincronía

#### 12.3.01 — Synchronous programming
La programación síncrona ejecuta operaciones en secuencia y una operación bloqueante impide avanzar en ese hilo. Es sencilla de razonar, pero una operación lenta de I/O puede congelar la interfaz o retrasar otras tareas.

#### 12.3.02 — Asynchronous programming
La programación asíncrona permite iniciar una operación y continuar mientras se espera su resultado. No significa necesariamente ejecución paralela; distingue concurrencia, asincronía y paralelismo al explicar cómo se programan las tareas.

#### 12.3.03 — Callbacks
Un callback es una función entregada a otra operación para invocarse posteriormente o durante un proceso. Es común en eventos y APIs, pero anidar muchos callbacks dificulta el manejo de errores y la lectura; promesas suelen expresar mejor cadenas asíncronas.

#### 12.3.04 — Promises
Una Promise representa un resultado futuro con estados pending, fulfilled o rejected. Encadena con `then`, `catch` y `finally`, devuelve siempre una nueva promesa desde callbacks y maneja rechazos para evitar errores no observados.

#### 12.3.05 — Async/Await
`async` declara una función que devuelve una promesa y `await` pausa su continuación hasta que la promesa se resuelve o rechaza. Usa `try/catch` para errores y evita esperar en serie tareas independientes que podrían ejecutarse concurrentemente.

#### 12.3.06 — Event Loop
El Event Loop coordina la pila de ejecución, colas de tareas y trabajos de microtareas del entorno. Comprende que JavaScript ejecuta código de usuario en un hilo principal en muchos entornos, mientras ciertas operaciones las realiza el runtime o el navegador.

#### 12.3.07 — Microtasks
Las microtasks incluyen continuaciones de promesas y se procesan en puntos específicos del ciclo de eventos antes de continuar con la siguiente tarea. Una cadena interminable de microtasks puede retrasar renderizado y otras tareas.

#### 12.3.08 — Macrotasks
Las macrotasks (término didáctico habitual para tareas del event loop) incluyen callbacks de temporizadores y eventos según el entorno. Los temporizadores establecen un tiempo mínimo de espera, no garantizan ejecución exacta en ese instante.

#### 12.3.09 — Error handling
El manejo de errores asíncronos requiere capturar rechazos, propagar contexto y distinguir fallos de red, HTTP y parseo. `fetch` no rechaza automáticamente por respuestas HTTP 4xx/5xx; comprueba `response.ok` y presenta errores sin filtrar secretos.

#### 12.3.10 — Race conditions
Race conditions ocurren cuando el resultado depende del orden de operaciones concurrentes o asíncronas. Cancela solicitudes obsoletas, usa identificadores de petición o controles de versión y evita que una respuesta antigua sobrescriba datos más recientes.

### Módulo 12.4 — Web APIs

#### 12.4.01 — Fetch API
Fetch API realiza solicitudes de red y devuelve una promesa con un objeto `Response`. Configura método, headers y body según el contrato; comprueba `ok`, tipo de contenido y errores, y no asumas que una respuesta siempre contiene JSON.

#### 12.4.02 — LocalStorage
LocalStorage persiste pares clave/valor de texto en el origen del navegador y sobrevive al cierre de pestaña. No almacenes contraseñas, tokens sensibles ni datos de alto riesgo; los scripts del mismo origen pueden leerlo y una vulnerabilidad XSS expone su contenido.

#### 12.4.03 — SessionStorage
SessionStorage conserva datos por origen y contexto de pestaña durante la sesión de página. Úsalo para estado temporal de interfaz, no como almacén seguro; define qué ocurre al recargar, duplicar o cerrar pestañas.

#### 12.4.04 — Cookies
Las cookies son pequeños datos enviados en solicitudes según dominio, ruta y políticas del navegador. Para sesiones, configura `Secure`, `HttpOnly` y `SameSite` apropiadamente, define expiración y evita guardar información sensible legible por JavaScript.

#### 12.4.05 — Geolocation
Geolocation API solicita permiso para acceder a una ubicación estimada del dispositivo. Explica el propósito, solicita el dato solo cuando sea necesario y minimiza retención; la precisión y disponibilidad dependen del dispositivo, permisos y entorno.

#### 12.4.06 — Clipboard
Clipboard API permite leer o escribir en el portapapeles bajo restricciones de seguridad y permisos del navegador. Ofrece una acción explícita, maneja rechazo de permisos y proporciona alternativa manual para copiar cuando la API no esté disponible.

#### 12.4.07 — File API
File API permite que una página lea archivos que el usuario selecciona o suelta, sin conceder acceso arbitrario al sistema de archivos. Valida tipo, tamaño y contenido en servidor; el nombre o MIME declarado no demuestra que el archivo sea seguro.

### Módulo 12.5 — TypeScript

#### 12.5.01 — Tipos
Los tipos TypeScript describen las formas de valores y permiten detectar incompatibilidades durante el análisis estático. El sistema se elimina en la compilación y no valida datos en runtime; valida entradas externas con esquemas o comprobaciones reales.

#### 12.5.02 — Interfaces
Una `interface` define la forma de objetos y puede extender otras interfaces o participar en declaración abierta. Úsala para contratos de objetos y servicios; recuerda que las interfaces desaparecen al compilar y no son validadores de datos.

#### 12.5.03 — Type aliases
Un `type alias` asigna un nombre a un tipo, que puede ser primitivo, unión, intersección, tupla o forma de objeto. Selecciona `type` o `interface` según la composición y extensibilidad que necesite el contrato.

#### 12.5.04 — Union types
Los union types permiten que un valor pertenezca a uno de varios tipos, por ejemplo `string | number`. Reduce la unión mediante comprobaciones de tipo y maneja todos los casos posibles antes de utilizar operaciones específicas.

#### 12.5.05 — Intersection types
Los intersection types combinan requisitos de varios tipos en uno solo. Son útiles para componer contratos, pero pueden producir propiedades incompatibles; evita combinaciones que generen tipos imposibles o difíciles de interpretar.

#### 12.5.06 — Generics
Los generics parametrizan funciones, interfaces y clases para conservar relaciones entre tipos sin recurrir a `any`. Define restricciones con `extends` cuando una operación necesita propiedades concretas y prueba inferencia con diferentes entradas.

#### 12.5.07 — Type narrowing
Type narrowing reduce una unión a un tipo más específico mediante `typeof`, `in`, igualdad, discriminantes o guards. Modela estados con etiquetas discriminantes y evita asumir que una conversión de tipo modifica el valor en runtime.

#### 12.5.08 — Utility types
Utility types como `Partial`, `Pick`, `Omit`, `Record`, `Readonly` y `ReturnType` derivan nuevos tipos a partir de otros. Úsalos para expresar transformaciones de contrato y evita construir tipos excesivamente complejos solo para ahorrar unas líneas.

#### 12.5.09 — Enums
Los enums representan conjuntos de constantes nombradas, aunque pueden generar código JavaScript dependiendo de su forma. Considera uniones literales o `as const` cuando sea más sencillo y documenta cómo se serializan los valores.

#### 12.5.10 — Type inference
Type inference permite que TypeScript deduzca tipos a partir de valores, parámetros contextuales y expresiones. Añade anotaciones en límites públicos o cuando aclaren intención; no anotes cada variable de forma redundante ni confíes en inferencia para datos no validados.

#### 12.5.11 — Strict mode
Strict mode activa comprobaciones estrictas del compilador, incluida la gestión de nullability y parámetros implícitos. Actívalo progresivamente en proyectos heredados y corrige los contratos reales en vez de silenciar errores con `any` o aserciones indiscriminadas.

### Módulo 12.6 — React

#### 12.6.01 — Components
Un componente React encapsula una parte de interfaz y suele expresarse como función que devuelve JSX. Divide por responsabilidad y reutilización, mantén componentes puros cuando sea posible y no llames componentes como funciones ordinarias.

#### 12.6.02 — JSX
JSX es una sintaxis que permite describir estructuras similares a HTML dentro de JavaScript y se transforma durante el build. Usa `className`, expresiones entre llaves y claves estables en listas; JSX no es HTML literal y aplica reglas de JavaScript.

#### 12.6.03 — Props
Props son entradas de solo lectura que el componente recibe de su padre. Define nombres y tipos claros, evita mutarlas y pasa callbacks para comunicar acciones hacia arriba en lugar de modificar directamente el estado de otro componente.

#### 12.6.04 — State
State representa información que puede cambiar y cuya actualización provoca un nuevo render. Trata el estado como inmutable, calcula actualizaciones desde el valor previo cuando dependa de él y evita duplicar datos derivados que puedan calcularse.

#### 12.6.05 — Hooks
Hooks permiten utilizar estado y otras capacidades de React desde componentes funcionales. Llámalos en el nivel superior y en el mismo orden en cada render; no los invoques dentro de condiciones, ciclos o funciones anidadas.

#### 12.6.06 — useState
`useState` añade estado local y devuelve el valor actual y una función de actualización. Si el nuevo valor depende del anterior, utiliza la forma funcional; no modifiques arrays u objetos existentes directamente.

#### 12.6.07 — useEffect
`useEffect` sincroniza un componente con sistemas externos después del render, como suscripciones o temporizadores. Declara dependencias correctas y limpieza; no lo uses para calcular valores derivados que pueden obtenerse durante el render.

#### 12.6.08 — useContext
`useContext` lee el valor del contexto más cercano para compartir datos a través del árbol. Mantén el contexto para información realmente transversal y divide contextos de alta frecuencia de cambio para evitar renders innecesarios.

#### 12.6.09 — useRef
`useRef` conserva un objeto mutable entre renders sin provocar un render al cambiar su propiedad `current`. Sirve para referencias DOM y valores persistentes no visuales; si un cambio debe reflejarse en pantalla, normalmente corresponde a state.

#### 12.6.10 — Forms
Los formularios React pueden ser controlados por estado o utilizar referencias y APIs nativas. Define validación y mensajes accesibles, evita actualizar estado de manera innecesaria por cada pulsación y protege datos sensibles en el flujo de envío.

#### 12.6.11 — Routing
Routing asocia rutas de URL con vistas y navegación de una aplicación. Distingue rutas cliente de navegación de servidor, maneja rutas desconocidas y protege recursos en backend; ocultar un enlace no constituye autorización.

#### 12.6.12 — Context API
Context API distribuye valores compartidos sin pasar props por cada nivel. Es adecuada para temas, idioma o sesión de interfaz, pero no sustituye automáticamente una estrategia de estado compleja ni el almacenamiento seguro de credenciales.

#### 12.6.13 — Component lifecycle
El ciclo de vida describe montaje, actualización y desmontaje de componentes. En componentes funcionales, efectos y su limpieza expresan sincronización con sistemas externos; el modo estricto de desarrollo puede repetir ciclos para revelar efectos no seguros.

#### 12.6.14 — State management
State management define cómo se representa, actualiza y comparte el estado de una aplicación. Separa estado local, estado de servidor, estado de URL y estado global; selecciona la herramienta menos compleja que cubra las necesidades reales.

#### 12.6.15 — Custom Hooks
Custom Hooks encapsulan lógica reutilizable que usa otros hooks y devuelve datos o acciones. Sus nombres comienzan con `use`, respetan las reglas de hooks y abstraen comportamiento, no necesariamente interfaz visual.

#### 12.6.16 — Error Boundaries
Error Boundaries capturan errores de renderizado en partes del árbol React y muestran una interfaz alternativa. No capturan todos los errores asíncronos ni eventos; registra contexto sin exponer datos privados y ofrece recuperación o navegación segura.

### Módulo 12.7 — Next.js

#### 12.7.01 — App Router
App Router organiza rutas y layouts mediante la estructura de archivos de `app` en Next.js. Comprende segmentos, layouts anidados, loading, error y not-found; consulta la documentación de la versión del proyecto porque convenciones pueden evolucionar.

#### 12.7.02 — Routing
El routing de Next.js convierte segmentos de carpetas y archivos especiales en rutas. Diseña rutas legibles, parámetros dinámicos y layouts compartidos; evita asumir que toda navegación se ejecuta exclusivamente en el cliente.

#### 12.7.03 — Server Components
Server Components se ejecutan en el servidor y permiten obtener datos y reducir JavaScript enviado al navegador. No acceden a APIs exclusivas del navegador ni manejan estado cliente; evita enviar secretos o datos no autorizados en sus props.

#### 12.7.04 — Client Components
Client Components habilitan estado, eventos y APIs del navegador mediante la directiva `use client` en el límite apropiado. Mantén el límite cliente pequeño y no confundas la ejecución inicial de render con la disponibilidad de APIs del navegador.

#### 12.7.05 — Server-side rendering
Server-side rendering genera HTML en el servidor para una solicitud o estrategia configurada. Considera hidratación, caché, datos personalizados y coste de render; evita que datos de usuario se filtren por cachés compartidas.

#### 12.7.06 — Static site generation
Static site generation produce páginas durante la compilación o regeneración configurada, reduciendo trabajo por solicitud. Es apropiada para contenido que puede servirse estáticamente; define cómo se actualiza y evita publicar datos privados o obsoletos.

#### 12.7.07 — Data fetching
Data fetching obtiene datos desde servicios o bases de datos dentro de los límites de ejecución de Next.js. Define caché, revalidación, timeout, manejo de errores y permisos; el lugar de la solicitud afecta rendimiento y exposición de secretos.

#### 12.7.08 — Authentication
La autenticación identifica al usuario y la autorización determina qué puede hacer. Usa bibliotecas y protocolos mantenidos, valida sesión y permisos en el servidor y no confíes en rutas protegidas solo por controles de interfaz.

#### 12.7.09 — Metadata
Metadata permite definir título, descripción, iconos y otras propiedades de página desde la configuración de Next.js. Genera metadatos coherentes por ruta, evita duplicados y no incluyas datos personales o secretos en valores públicos.

#### 12.7.10 — Deployment
Deployment publica la aplicación y su configuración en un entorno de ejecución. Documenta variables de entorno, build, runtime, migraciones, observabilidad, rollback y dominio; no incluyas secretos en repositorio ni confundas build exitoso con servicio saludable.

### Módulo 12.8 — Herramientas

#### 12.8.01 — npm
npm instala paquetes, ejecuta scripts y administra dependencias mediante `package.json` y un lockfile. Revisa scripts antes de ejecutarlos, fija versiones según política y evita instalar paquetes de nombres parecidos sin verificar el mantenedor.

#### 12.8.02 — pnpm
pnpm gestiona dependencias con un almacén de contenido direccionado y enlaces, optimizando espacio y consistencia. Conserva `pnpm-lock.yaml`, documenta la versión del gestor y no mezcles lockfiles sin una decisión explícita del equipo.

#### 12.8.03 — Vite
Vite ofrece servidor de desarrollo y proceso de build para aplicaciones frontend. Configura plugins y variables con cuidado, recuerda que las variables expuestas al cliente son públicas y valida el artefacto de producción además del servidor local.

#### 12.8.04 — ESLint
ESLint analiza patrones de código y aplica reglas para detectar errores potenciales y mantener convenciones. Configura reglas compatibles con la versión del lenguaje y framework; no desactives globalmente reglas para ocultar advertencias recurrentes.

#### 12.8.05 — Prettier
Prettier formatea código de manera consistente y reduce discusiones de estilo. Fija configuración compartida y ejecútalo en el flujo del proyecto; el formateador no reemplaza linting, revisión ni pruebas.

#### 12.8.06 — Tailwind CSS
Tailwind CSS ofrece utilidades de bajo nivel para expresar estilos directamente en el marcado. Mantén tokens y patrones reutilizables, revisa el tamaño del CSS generado y evita construir nombres de clase dinámicos que el proceso de detección no pueda identificar.

#### 12.8.07 — React DevTools
React DevTools permite inspeccionar árbol de componentes, props, estado y rendimiento en desarrollo. Utilízalo para localizar renders y estructura; evita compartir capturas con datos de usuario o tokens y no lo confundas con una prueba de rendimiento completa.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 89 orientaciones genéricas del desglose por explicaciones específicas de cada entrada oficial. Se añadieron precisiones sobre semántica y coerción de JavaScript, closures/prototypes/this, propagación de eventos, ciclo de eventos y microtasks, almacenamiento del navegador, límites de TypeScript en runtime, reglas de hooks, Server/Client Components, caché, autenticación y seguridad de dependencias.

**Revisión interna:** 89/89 entradas desarrolladas y cotejadas con el roadmap. La guía principal conserva ejemplos, proyecto y evaluación. Pendiente: fijar versiones exactas de Node.js, TypeScript, React y Next.js para ejecución reproducible; compilar, ejecutar pruebas de componentes y accesibilidad, validar APIs y revisar el despliegue. Esta revisión documental no acredita ejecución ni aprobación externa.
