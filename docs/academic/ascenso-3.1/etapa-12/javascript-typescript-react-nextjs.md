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

Las variables enlazan identificadores con valores. `let` permite reasignación, `const` impide reasignar el enlace y `var` tiene alcance de función y hoisting histórico. Prefiere const por defecto y let cuando el flujo requiere reasignación.

**Ejemplo técnico:** `const limite = 10; let intentos = 0;`

**Práctica guiada:** Declara valores, intenta reasignar const y observa el error en modo estricto.

**Actividad independiente:** Refactoriza variables para minimizar mutabilidad.

**Criterios de aceptación:** Cada variable tiene alcance y mutabilidad justificados.

**Errores frecuentes:** Usar var sin razón o pensar que const vuelve inmutable un objeto.

**Comprobación:** ¿Qué impide const y qué no impide?

#### 12.1.02 — Tipos

JavaScript es dinámico y los valores tienen tipos como string, number, bigint, boolean, undefined, symbol y object; null es un valor primitivo especial pese a typeof histórico.

**Ejemplo técnico:** typeof null devuelve 'object' por una peculiaridad histórica.

**Práctica guiada:** Prueba typeof en valores primitivos y objetos.

**Actividad independiente:** Clasifica entradas y define validación antes de operar.

**Criterios de aceptación:** No se confunden tipos ni coerciones implícitas.

**Errores frecuentes:** Asumir que typeof null devuelve null.

**Comprobación:** ¿Qué diferencia hay entre tipo de variable y tipo del valor actual?

#### 12.1.03 — Operadores

Los operadores realizan operaciones aritméticas, comparación, lógica, asignación y coalescencia. `===` evita coerción en comparación de igualdad; `??` usa fallback solo ante null/undefined, a diferencia de `||`.

**Ejemplo técnico:** `valor ?? 'sin dato'` conserva 0 y cadena vacía.

**Práctica guiada:** Prueba ==/===, ||/?? y precedencia con valores límite.

**Actividad independiente:** Construye expresiones de validación sin coerciones ambiguas.

**Criterios de aceptación:** Resultados previstos para null, 0, false y ''.

**Errores frecuentes:** Usar == sin comprender coerción o confundir || con ??.

**Comprobación:** ¿Qué valor de entrada distingue ?? de ||?

#### 12.1.04 — Condicionales

if/else, switch y operador ternario controlan ramificación. La comparación debe ser explícita y las ramas exhaustivas cuando el dominio lo exige.

**Ejemplo técnico:** switch sobre estado con default que maneja valor desconocido.

**Práctica guiada:** Prueba ramas verdadera/falsa y estados no contemplados.

**Actividad independiente:** Implementa validación de estados de pedido.

**Criterios de aceptación:** Cada estado posible tiene comportamiento definido.

**Errores frecuentes:** Olvidar default o anidar ternarios ilegibles.

**Comprobación:** ¿Por qué conviene manejar el caso desconocido?

#### 12.1.05 — Bucles

for, while, do...while, for...of y for...in recorren estructuras con semánticas diferentes. for...of itera valores iterables; for...in enumera claves enumerables, por lo que no es sustituto general para arrays.

**Ejemplo técnico:** for...of sobre array devuelve elementos; for...in devuelve índices como cadenas.

**Práctica guiada:** Compara iteraciones sobre array y objeto.

**Actividad independiente:** Procesa colección con salida temprana y condición de terminación.

**Criterios de aceptación:** No se omiten ni duplican elementos.

**Errores frecuentes:** Usar for...in para arrays sin controlar propiedades heredadas.

**Comprobación:** ¿Qué diferencia hay entre for...of y for...in?

#### 12.1.06 — Funciones

Las funciones encapsulan comportamiento y pueden declararse, asignarse o expresarse como arrow functions. Parámetros, retorno, efectos secundarios y contrato deben ser claros.

**Ejemplo técnico:** Una función pura recibe número y devuelve doble sin modificar estado externo.

**Práctica guiada:** Implementa funciones con parámetros, retorno y casos límite.

**Actividad independiente:** Divide un cálculo en funciones pequeñas y comprobables.

**Criterios de aceptación:** Entradas/salidas definidas y sin efectos inesperados.

**Errores frecuentes:** Funciones largas que mezclan entrada, cálculo y DOM.

**Comprobación:** ¿Qué característica hace que una función sea pura?

#### 12.1.07 — Objetos

Los objetos agrupan propiedades y métodos. Las propiedades pueden ser propias o heredadas; la mutación afecta referencias compartidas. Object.keys/entries y destructuring facilitan inspección.

**Ejemplo técnico:** Dos variables que apuntan al mismo objeto observan la misma mutación.

**Práctica guiada:** Crea objeto y compara copia por referencia con copia superficial.

**Actividad independiente:** Modela objeto de pedido con propiedades validadas.

**Criterios de aceptación:** Se explica identidad y mutabilidad de referencias.

**Errores frecuentes:** Creer que asignar objeto a otra variable lo clona.

**Comprobación:** ¿Qué sucede al modificar un objeto desde una segunda referencia?

#### 12.1.08 — Arrays

Los arrays son objetos indexados y ordenados; métodos como map, filter, reduce, find y some expresan transformaciones. Algunos mutan (sort, splice, push) y otros devuelven nuevos arrays.

**Ejemplo técnico:** filter selecciona; map transforma; reduce acumula.

**Práctica guiada:** Aplica map/filter/reduce a datos sintéticos y compara original.

**Actividad independiente:** Construye pipeline de transformación sin mutar entrada.

**Criterios de aceptación:** Resultado y mutación están documentados.

**Errores frecuentes:** Confundir métodos mutables e inmutables o mutar estado React directamente.

**Comprobación:** ¿Qué diferencia hay entre map y forEach?

#### 12.1.09 — Strings

Las cadenas son inmutables y ofrecen métodos de búsqueda, extracción, normalización y reemplazo. Template literals interpolan expresiones; Unicode puede requerir cuidado con unidades UTF-16 y grafemas.

**Ejemplo técnico:** `texto.trim().toLowerCase()` normaliza espacios y mayúsculas simples.

**Práctica guiada:** Prueba slice, includes, replace y trim con entradas acentuadas.

**Actividad independiente:** Normaliza y valida una etiqueta sin perder caracteres Unicode.

**Criterios de aceptación:** Se documenta tratamiento de espacios y caracteres.

**Errores frecuentes:** Asumir que length equivale siempre a cantidad de caracteres percibidos.

**Comprobación:** ¿Por qué una cadena Unicode puede tener length distinto al número de símbolos visibles?

#### 12.1.10 — Destructuring

Destructuring extrae valores de arrays y propiedades de objetos en variables, con valores por defecto y renombrado. En objetos, el nombre de propiedad y variable puede diferir.

**Ejemplo técnico:** `const {nombre: etiqueta = 'Invitado'} = usuario;`

**Práctica guiada:** Extrae campos presentes, ausentes y anidados.

**Actividad independiente:** Refactoriza acceso repetido a propiedades con destructuring legible.

**Criterios de aceptación:** Defaults solo aplican a undefined y el origen está claro.

**Errores frecuentes:** Confundir default de destructuring con fallback ante null.

**Comprobación:** ¿Qué ocurre si la propiedad existe con valor null?

#### 12.1.11 — Spread

Spread expande elementos iterables o propiedades enumerables en nuevos contextos. La copia de arrays/objetos suele ser superficial; objetos anidados conservan referencias.

**Ejemplo técnico:** `const copia = {...original}` crea objeto distinto, pero conserva referencia a subobjetos.

**Práctica guiada:** Compara identidad y mutación en copia superficial.

**Actividad independiente:** Actualiza una propiedad anidada sin mutar el estado original.

**Criterios de aceptación:** Se identifica qué niveles fueron copiados.

**Errores frecuentes:** Creer que spread realiza clonación profunda.

**Comprobación:** ¿Qué limitación tiene la copia superficial?

#### 12.1.12 — Rest

Rest recoge elementos restantes en parámetros, destructuring o arrays/objetos. En parámetros debe aparecer al final y permite funciones de aridad variable.

**Ejemplo técnico:** `function sumar(...valores)` recibe argumentos en un array.

**Práctica guiada:** Implementa función con cantidad variable de argumentos.

**Actividad independiente:** Combina primer parámetro y resto para un reporte.

**Criterios de aceptación:** El resto captura exactamente argumentos no asignados.

**Errores frecuentes:** Confundir rest con spread pese a sintaxis parecida.

**Comprobación:** ¿En qué contexto `...` recoge valores en vez de expandirlos?

#### 12.1.13 — Scope

El scope determina dónde es accesible un identificador: global, función y bloque. let/const tienen alcance de bloque; var de función. Shadowing puede ocultar variables externas y dificultar lectura.

**Ejemplo técnico:** Una let declarada dentro de if no existe fuera del bloque.

**Práctica guiada:** Prueba acceso antes/después de bloque y función.

**Actividad independiente:** Refactoriza variables globales a alcance mínimo.

**Criterios de aceptación:** Cada identificador tiene alcance intencional.

**Errores frecuentes:** Crear globals accidentales o reutilizar nombres que ocultan valores externos.

**Comprobación:** ¿Qué diferencia el scope de bloque del scope de función?

#### 12.1.14 — Closures

Una closure conserva acceso al entorno léxico donde se creó la función, incluso después de que la función externa termina. Se utiliza para encapsular estado, callbacks y factories; también puede retener memoria si mantiene referencias innecesarias.

**Ejemplo técnico:** Una función contador puede cerrar sobre una variable privada y exponer incremento/lectura.

**Práctica guiada:** Crea contador y dos instancias independientes.

**Actividad independiente:** Diseña factory que encapsule configuración sin exponer mutación directa.

**Criterios de aceptación:** Instancias mantienen estados separados.

**Errores frecuentes:** Asumir que closure copia valores en vez de conservar entorno léxico.

**Comprobación:** ¿Por qué dos closures creadas por llamadas distintas pueden mantener estados independientes?

#### 12.1.15 — Hoisting

Hoisting describe cómo declaraciones se procesan antes de ejecutar código. function declarations pueden invocarse antes de su ubicación; var se inicializa como undefined; let/const permanecen en temporal dead zone hasta inicialización.

**Ejemplo técnico:** Acceder a let antes de declararla produce ReferenceError.

**Práctica guiada:** Compara function, var, let y const en ejemplos aislados.

**Actividad independiente:** Refactoriza código para declarar dependencias antes de uso.

**Criterios de aceptación:** No se depende de comportamiento confuso de hoisting.

**Errores frecuentes:** Decir que let/const no se elevan; se elevan pero quedan en TDZ.

**Comprobación:** ¿Qué es la temporal dead zone?

#### 12.1.16 — Prototypes

La herencia de JavaScript se basa en cadena de prototipos. Los objetos pueden delegar búsqueda de propiedades a su prototype; class es sintaxis sobre este mecanismo. Object.create y Object.getPrototypeOf permiten inspección.

**Ejemplo técnico:** Una instancia puede heredar método desde prototype sin copiarlo como propiedad propia.

**Práctica guiada:** Compara Object.hasOwn y búsqueda heredada.

**Actividad independiente:** Modela comportamiento compartido y explica cuándo preferir composición.

**Criterios de aceptación:** Se distingue propiedad propia de heredada.

**Errores frecuentes:** Confundir prototype de función con [[Prototype]] de instancia.

**Comprobación:** ¿Qué sucede cuando una propiedad no existe como propia?

#### 12.1.17 — This

El valor de this depende del modo de invocación, no solo del lugar donde se define la función. Arrow functions capturan this léxico; métodos tradicionales reciben this según receptor y bind/call/apply pueden fijarlo.

**Ejemplo técnico:** obj.metodo() vincula this a obj; extraer método puede perder ese receptor.

**Práctica guiada:** Prueba método, función extraída, bind y arrow function.

**Actividad independiente:** Corrige callback que pierde contexto de this.

**Criterios de aceptación:** Contexto de this explicado por invocación.

**Errores frecuentes:** Asumir que this siempre apunta al objeto que contiene la definición.

**Comprobación:** ¿Por qué una arrow function no crea su propio this?

#### 12.1.18 — ES6+

ECMAScript moderno incorpora módulos, let/const, arrow functions, clases, promesas, destructuring, spread, iteradores y otras mejoras. La compatibilidad depende del runtime y objetivo de compilación.

**Ejemplo técnico:** Una aplicación puede usar async/await en runtime moderno o transpilar para navegadores antiguos.

**Práctica guiada:** Identifica características modernas en código y comprueba soporte del target.

**Actividad independiente:** Actualiza un fragmento legacy conservando comportamiento y compatibilidad.

**Criterios de aceptación:** La característica se usa según soporte y necesidad.

**Errores frecuentes:** Confundir versión del lenguaje con versión de Node/navegador.

**Comprobación:** ¿Qué papel cumple un target de compilación?

#### 12.1.19 — Modules

Los módulos ES utilizan export e import, tienen scope propio y se evalúan una vez por módulo en un grafo de dependencias. Los imports estáticos deben estar en nivel superior; la resolución depende del entorno y configuración.

**Ejemplo técnico:** Export nombrado y default tienen sintaxis y consumo distintos.

**Práctica guiada:** Separa función y constantes en dos módulos y prueba importaciones.

**Actividad independiente:** Organiza utilidades con API pública mínima.

**Criterios de aceptación:** Dependencias explícitas y sin ciclos innecesarios.

**Errores frecuentes:** Confundir CommonJS require con import ESM o exportar internals innecesarios.

**Comprobación:** ¿Qué diferencia existe entre export nombrado y default?

#### 12.2.01 — Document Object Model

El DOM representa el documento como árbol de nodos y permite consultar/modificar estructura, atributos y texto. El DOM vivo refleja cambios; no es lo mismo que el HTML fuente inicial.

**Ejemplo técnico:** document.querySelector('main') obtiene el primer main del documento.

**Práctica guiada:** Inspecciona árbol DOM y relación padre/hijo.

**Actividad independiente:** Construye estructura simple y localiza nodos por selector.

**Criterios de aceptación:** Se distingue fuente, DOM y renderizado.

**Errores frecuentes:** Asumir que DOM y HTML fuente siempre son idénticos.

**Comprobación:** ¿Qué ocurre con el DOM después de modificar un nodo?

#### 12.2.02 — Selección de elementos

querySelector/querySelectorAll usan selectores CSS y devuelven elemento o NodeList; getElementById busca por id. La selección debe ser específica y manejar ausencia de resultados.

**Ejemplo técnico:** querySelectorAll('.item') devuelve colección estática de coincidencias.

**Práctica guiada:** Selecciona por id, clase y atributo; prueba cero coincidencias.

**Actividad independiente:** Implementa función que valida si un elemento existe antes de usarlo.

**Criterios de aceptación:** No hay referencias nulas no controladas.

**Errores frecuentes:** Asumir que querySelectorAll devuelve array o que siempre encuentra nodo.

**Comprobación:** ¿Qué diferencia hay entre querySelector y querySelectorAll?

#### 12.2.03 — Manipulación del DOM

Se pueden crear, insertar, reemplazar y eliminar nodos. textContent trata contenido como texto; innerHTML interpreta marcado y requiere sanitización estricta ante datos no confiables.

**Ejemplo técnico:** createElement + textContent evita interpretar texto de usuario como HTML.

**Práctica guiada:** Crea lista dinámica con createElement y append.

**Actividad independiente:** Renderiza datos sintéticos sin concatenar HTML no confiable.

**Criterios de aceptación:** Datos se presentan sin ejecutar marcado no previsto.

**Errores frecuentes:** Insertar entradas de usuario con innerHTML sin sanitizar.

**Comprobación:** ¿Por qué textContent es más seguro para mostrar texto no confiable?

#### 12.2.04 — Eventos

Los eventos notifican acciones o cambios; el objeto Event contiene tipo, target, currentTarget y otros datos. La propagación incluye fases de captura, target y burbujeo.

**Ejemplo técnico:** click se propaga desde el elemento objetivo hacia ancestros durante bubbling.

**Práctica guiada:** Registra target/currentTarget y observa propagación.

**Actividad independiente:** Implementa acción con evento y estado accesible.

**Criterios de aceptación:** El manejador responde al evento correcto sin efectos duplicados.

**Errores frecuentes:** Usar eventos inline en HTML y mezclar responsabilidades.

**Comprobación:** ¿Qué diferencia target de currentTarget?

#### 12.2.05 — Event listeners

addEventListener registra manejadores con opciones como capture, once, passive y signal. removeEventListener requiere referencia compatible; AbortController permite cancelar grupos de listeners.

**Ejemplo técnico:** {once:true} ejecuta manejador una vez; signal permite limpiar listeners al abortar.

**Práctica guiada:** Registra y retira listener con referencia estable.

**Actividad independiente:** Implementa componente que limpia listeners al desmontarse.

**Criterios de aceptación:** No quedan listeners duplicados tras recrear componente.

**Errores frecuentes:** Crear listeners repetidos sin cleanup o pasar función distinta al retirar.

**Comprobación:** ¿Por qué guardar referencia al callback facilita removeEventListener?

#### 12.2.06 — Event bubbling

En bubbling el evento asciende desde target por ancestros; stopPropagation detiene propagación y preventDefault cancela acción predeterminada cuando es cancelable. No deben usarse indiscriminadamente.

**Ejemplo técnico:** Un click en botón puede activar listener del contenedor padre.

**Práctica guiada:** Compara bubbling y capture con árbol simple.

**Actividad independiente:** Evita detener propagación salvo que exista razón de interacción.

**Criterios de aceptación:** Comportamiento predecible y sin handlers duplicados.

**Errores frecuentes:** Confundir stopPropagation con preventDefault.

**Comprobación:** ¿Qué cancela preventDefault y qué detiene stopPropagation?

#### 12.2.07 — Event delegation

La delegación coloca un listener en un ancestro para manejar eventos de descendientes mediante target/closest. Reduce listeners en listas dinámicas, pero requiere validar que el target pertenezca al contenedor.

**Ejemplo técnico:** Un ul gestiona clicks de sus li mediante closest('li').

**Práctica guiada:** Añade y elimina elementos y comprueba que listener delegado sigue funcionando.

**Actividad independiente:** Implementa lista dinámica con acciones por item.

**Criterios de aceptación:** Acciones se limitan al contenedor y reconocen elementos correctos.

**Errores frecuentes:** Confiar en target exacto cuando el clic ocurre en un icono hijo.

**Comprobación:** ¿Qué ventaja ofrece closest al delegar eventos?

#### 12.2.08 — Formularios

Los formularios generan submit y exponen valores mediante FormData. Deben manejar submit, validar entradas, informar errores y prevenir navegación solo cuando la aplicación controla el flujo. Validación servidor sigue siendo obligatoria.

**Ejemplo técnico:** new FormData(form) recoge controles con atributo name.

**Práctica guiada:** Captura submit, inspecciona FormData y evita enviar datos reales.

**Actividad independiente:** Implementa formulario de laboratorio con estados y mensajes accesibles.

**Criterios de aceptación:** Datos y errores se procesan sin pérdida y sin confiar solo en cliente.

**Errores frecuentes:** Leer inputs por selector frágil o validar únicamente en navegador.

**Comprobación:** ¿Por qué los controles necesitan name para incluirse en FormData?

#### 12.2.09 — Validaciones

La validación combina restricciones HTML, lógica cliente y reglas autoritativas del servidor. Constraint Validation API expone validity, checkValidity y setCustomValidity. Errores deben ser específicos, accesibles y no filtrar información sensible.

**Ejemplo técnico:** input type=email valida formato básico, no existencia del buzón ni permiso de uso.

**Práctica guiada:** Prueba required, minlength y setCustomValidity con datos sintéticos.

**Actividad independiente:** Diseña validación con resumen y mensaje asociado al campo.

**Criterios de aceptación:** Casos válidos/invalidos cubiertos y mensajes claros.

**Errores frecuentes:** Confiar en HTML como barrera de seguridad o usar mensajes genéricos que no permiten corregir.

**Comprobación:** ¿Qué validaciones deben repetirse en servidor?

#### 12.3.01 — Synchronous programming
La programación síncrona ejecuta operaciones en secuencia y una operación bloqueante impide avanzar en ese hilo. Es sencilla de razonar, pero una operación lenta de I/O puede congelar la interfaz o retrasar otras tareas.


**Práctica y evidencia:** Identifica operaciones síncronas que bloquean el hilo principal y mide el efecto de una tarea de prueba. **Evidencia:** explica por qué la interfaz deja de responder durante trabajo prolongado.

#### 12.3.02 — Asynchronous programming
La programación asíncrona permite iniciar una operación y continuar mientras se espera su resultado. No significa necesariamente ejecución paralela; distingue concurrencia, asincronía y paralelismo al explicar cómo se programan las tareas.


**Práctica y evidencia:** Compara una operación síncrona con una asíncrona basada en temporizador o red. **Evidencia:** dibuja la secuencia temporal y explica qué trabajo puede continuar mientras se espera.

#### 12.3.03 — Callbacks
Un callback es una función entregada a otra operación para invocarse posteriormente o durante un proceso. Es común en eventos y APIs, pero anidar muchos callbacks dificulta el manejo de errores y la lectura; promesas suelen expresar mejor cadenas asíncronas.


**Práctica y evidencia:** Convierte una operación basada en callback en una función que notifique éxito o error. **Evidencia:** explica convención error-first y cómo evitar llamadas duplicadas.

#### 12.3.04 — Promises
Una Promise representa un resultado futuro con estados pending, fulfilled o rejected. Encadena con `then`, `catch` y `finally`, devuelve siempre una nueva promesa desde callbacks y maneja rechazos para evitar errores no observados.


**Práctica y evidencia:** Encadena Promises con `then`, `catch` y `finally`, incluyendo una promesa rechazada. **Evidencia:** identifica dónde se propaga el error y cómo se recupera el flujo.

#### 12.3.05 — Async/Await
`async` declara una función que devuelve una promesa y `await` pausa su continuación hasta que la promesa se resuelve o rechaza. Usa `try/catch` para errores y evita esperar en serie tareas independientes que podrían ejecutarse concurrentemente.


**Práctica y evidencia:** Reescribe una cadena de promesas con `async`/`await` y captura errores con `try/catch`. **Evidencia:** explica que `await` pausa la función async, no bloquea el hilo principal.

#### 12.3.06 — Event Loop
El Event Loop coordina la pila de ejecución, colas de tareas y trabajos de microtareas del entorno. Comprende que JavaScript ejecuta código de usuario en un hilo principal en muchos entornos, mientras ciertas operaciones las realiza el runtime o el navegador.


**Práctica y evidencia:** Dibuja la pila de llamadas, cola de tareas y trabajo de temporizadores en el Event Loop. **Evidencia:** predice el orden de varios `console.log` con temporizadores y promesas.

#### 12.3.07 — Microtasks
Las microtasks incluyen continuaciones de promesas y se procesan en puntos específicos del ciclo de eventos antes de continuar con la siguiente tarea. Una cadena interminable de microtasks puede retrasar renderizado y otras tareas.


**Práctica y evidencia:** Programa una Promise resuelta y un temporizador para observar el orden de ejecución. **Evidencia:** identifica las microtasks y explica cuándo se vacía su cola.

#### 12.3.08 — Macrotasks
Las macrotasks (término didáctico habitual para tareas del event loop) incluyen callbacks de temporizadores y eventos según el entorno. Los temporizadores establecen un tiempo mínimo de espera, no garantizan ejecución exacta en ese instante.


**Práctica y evidencia:** Compara temporizadores y eventos de interfaz como tareas del entorno del navegador. **Evidencia:** explica por qué `setTimeout(fn, 0)` no significa ejecución inmediata.

#### 12.3.09 — Error handling
El manejo de errores asíncronos requiere capturar rechazos, propagar contexto y distinguir fallos de red, HTTP y parseo. `fetch` no rechaza automáticamente por respuestas HTTP 4xx/5xx; comprueba `response.ok` y presenta errores sin filtrar secretos.


**Práctica y evidencia:** Maneja fallos de red, errores de parseo y rechazos de promesas diferenciando mensajes para usuario y detalles de diagnóstico. **Evidencia:** registra error controlado sin filtrar secretos.

#### 12.3.10 — Race conditions
Race conditions ocurren cuando el resultado depende del orden de operaciones concurrentes o asíncronas. Cancela solicitudes obsoletas, usa identificadores de petición o controles de versión y evita que una respuesta antigua sobrescriba datos más recientes.


**Práctica y evidencia:** Simula dos solicitudes concurrentes que actualizan el mismo estado y observa cuál termina primero. **Evidencia:** identifica la condición de carrera y propone cancelación, versionado o coordinación.

### Módulo 12.4 — Web APIs

#### 12.4.01 — Fetch API
Fetch API realiza solicitudes de red y devuelve una promesa con un objeto `Response`. Configura método, headers y body según el contrato; comprueba `ok`, tipo de contenido y errores, y no asumas que una respuesta siempre contiene JSON.


**Práctica y evidencia:** Realiza una solicitud `fetch` a un endpoint de prueba y gestiona estados HTTP, errores de red y parseo. **Evidencia:** distingue respuesta HTTP no exitosa de rechazo de la promesa.

#### 12.4.02 — LocalStorage
LocalStorage persiste pares clave/valor de texto en el origen del navegador y sobrevive al cierre de pestaña. No almacenes contraseñas, tokens sensibles ni datos de alto riesgo; los scripts del mismo origen pueden leerlo y una vulnerabilidad XSS expone su contenido.


**Práctica y evidencia:** Guarda una preferencia no sensible en LocalStorage y comprueba persistencia tras recargar. **Evidencia:** explica alcance por origen, persistencia y riesgo de almacenar tokens o secretos accesibles a JavaScript.

#### 12.4.03 — SessionStorage
SessionStorage conserva datos por origen y contexto de pestaña durante la sesión de página. Úsalo para estado temporal de interfaz, no como almacén seguro; define qué ocurre al recargar, duplicar o cerrar pestañas.


**Práctica y evidencia:** Guarda un dato temporal en SessionStorage y abre otra pestaña para observar su alcance. **Evidencia:** compara ciclo de vida con LocalStorage sin asumir sincronización entre pestañas.

#### 12.4.04 — Cookies
Las cookies son pequeños datos enviados en solicitudes según dominio, ruta y políticas del navegador. Para sesiones, configura `Secure`, `HttpOnly` y `SameSite` apropiadamente, define expiración y evita guardar información sensible legible por JavaScript.


**Práctica y evidencia:** Inspecciona cookies de prueba con atributos Secure, HttpOnly, SameSite, Path y expiración. **Evidencia:** explica cuáles son accesibles desde JavaScript y cómo se reduce exposición CSRF/XSS.

#### 12.4.05 — Geolocation
Geolocation API solicita permiso para acceder a una ubicación estimada del dispositivo. Explica el propósito, solicita el dato solo cuando sea necesario y minimiza retención; la precisión y disponibilidad dependen del dispositivo, permisos y entorno.


**Práctica y evidencia:** Solicita geolocalización solo tras una acción explícita del usuario y gestiona permiso denegado. **Evidencia:** demuestra que la función no debe bloquear la experiencia cuando el usuario no comparte ubicación.

#### 12.4.06 — Clipboard
Clipboard API permite leer o escribir en el portapapeles bajo restricciones de seguridad y permisos del navegador. Ofrece una acción explícita, maneja rechazo de permisos y proporciona alternativa manual para copiar cuando la API no esté disponible.


**Práctica y evidencia:** Copia texto mediante Clipboard API en respuesta a una interacción del usuario y maneja contexto no seguro o permiso denegado. **Evidencia:** muestra alternativa manual y no copia información sensible sin consentimiento.

#### 12.4.07 — File API
File API permite que una página lea archivos que el usuario selecciona o suelta, sin conceder acceso arbitrario al sistema de archivos. Valida tipo, tamaño y contenido en servidor; el nombre o MIME declarado no demuestra que el archivo sea seguro.


**Práctica y evidencia:** Lee un archivo seleccionado por el usuario con File API y valida tipo/tamaño también en servidor. **Evidencia:** demuestra que el atributo accept no constituye una validación de seguridad.

### Módulo 12.5 — TypeScript

#### 12.5.01 — Tipos
Los tipos TypeScript describen las formas de valores y permiten detectar incompatibilidades durante el análisis estático. El sistema se elimina en la compilación y no valida datos en runtime; valida entradas externas con esquemas o comprobaciones reales.


**Práctica y evidencia:** Declara tipos para una entidad de dominio y activa comprobaciones del compilador. **Evidencia:** demuestra un error de asignación detectado antes de ejecutar el programa.

#### 12.5.02 — Interfaces
Una `interface` define la forma de objetos y puede extender otras interfaces o participar en declaración abierta. Úsala para contratos de objetos y servicios; recuerda que las interfaces desaparecen al compilar y no son validadores de datos.


**Práctica y evidencia:** Define una interfaz para un objeto de cliente y úsala en una función que lo recibe. **Evidencia:** comprueba propiedades requeridas y explica tipado estructural.

#### 12.5.03 — Type aliases
Un `type alias` asigna un nombre a un tipo, que puede ser primitivo, unión, intersección, tupla o forma de objeto. Selecciona `type` o `interface` según la composición y extensibilidad que necesite el contrato.


**Práctica y evidencia:** Crea un alias de tipo para una estructura y compáralo con una interfaz ampliable. **Evidencia:** justifica la elección según composición, unión o extensión.

#### 12.5.04 — Union types
Los union types permiten que un valor pertenezca a uno de varios tipos, por ejemplo `string | number`. Reduce la unión mediante comprobaciones de tipo y maneja todos los casos posibles antes de utilizar operaciones específicas.


**Práctica y evidencia:** Modela un estado como unión discriminada, por ejemplo loading, success y error. **Evidencia:** demuestra que cada variante exige los campos correctos.

#### 12.5.05 — Intersection types
Los intersection types combinan requisitos de varios tipos en uno solo. Son útiles para componer contratos, pero pueden producir propiedades incompatibles; evita combinaciones que generen tipos imposibles o difíciles de interpretar.


**Práctica y evidencia:** Combina tipos con intersección para componer capacidades y resuelve un conflicto de propiedades. **Evidencia:** explica por qué una intersección puede producir un tipo imposible.

#### 12.5.06 — Generics
Los generics parametrizan funciones, interfaces y clases para conservar relaciones entre tipos sin recurrir a `any`. Define restricciones con `extends` cuando una operación necesita propiedades concretas y prueba inferencia con diferentes entradas.


**Práctica y evidencia:** Implementa una función genérica que conserve el tipo de entrada y salida. **Evidencia:** muestra inferencia del parámetro y un caso donde un tipo demasiado amplio pierde información.

#### 12.5.07 — Type narrowing
Type narrowing reduce una unión a un tipo más específico mediante `typeof`, `in`, igualdad, discriminantes o guards. Modela estados con etiquetas discriminantes y evita asumir que una conversión de tipo modifica el valor en runtime.


**Práctica y evidencia:** Utiliza `typeof`, `in`, `instanceof` y discriminantes para estrechar un tipo. **Evidencia:** elimina una aserción insegura mediante control de flujo.

#### 12.5.08 — Utility types
Utility types como `Partial`, `Pick`, `Omit`, `Record`, `Readonly` y `ReturnType` derivan nuevos tipos a partir de otros. Úsalos para expresar transformaciones de contrato y evita construir tipos excesivamente complejos solo para ahorrar unas líneas.


**Práctica y evidencia:** Aplica `Partial`, `Pick`, `Omit`, `Record` y `Readonly` a modelos de dominio. **Evidencia:** explica qué propiedades cambian y por qué los utility types no validan datos externos en runtime.

#### 12.5.09 — Enums
Los enums representan conjuntos de constantes nombradas, aunque pueden generar código JavaScript dependiendo de su forma. Considera uniones literales o `as const` cuando sea más sencillo y documenta cómo se serializan los valores.


**Práctica y evidencia:** Compara enum con unión de literales para representar estados finitos. **Evidencia:** justifica la opción elegida y comprueba el comportamiento del código generado si se usa enum.

#### 12.5.10 — Type inference
Type inference permite que TypeScript deduzca tipos a partir de valores, parámetros contextuales y expresiones. Añade anotaciones en límites públicos o cuando aclaren intención; no anotes cada variable de forma redundante ni confíes en inferencia para datos no validados.


**Práctica y evidencia:** Deja que TypeScript infiera tipos en expresiones simples y declara tipos explícitos en límites públicos. **Evidencia:** identifica una anotación redundante y una frontera donde la anotación mejora claridad.

#### 12.5.11 — Strict mode
Strict mode activa comprobaciones estrictas del compilador, incluida la gestión de nullability y parámetros implícitos. Actívalo progresivamente en proyectos heredados y corrige los contratos reales en vez de silenciar errores con `any` o aserciones indiscriminadas.


**Práctica y evidencia:** Activa `strict` y corrige errores relacionados con null, parámetros implícitos y propiedades opcionales. **Evidencia:** muestra que el proyecto compila sin desactivar reglas para ocultar problemas.

### Módulo 12.6 — React

#### 12.6.01 — Components
Un componente React encapsula una parte de interfaz y suele expresarse como función que devuelve JSX. Divide por responsabilidad y reutilización, mantén componentes puros cuando sea posible y no llames componentes como funciones ordinarias.


**Práctica y evidencia:** Construye un componente React pequeño y reutilizable con una única responsabilidad. **Evidencia:** muestra su uso en dos contextos y explica qué datos recibe.

#### 12.6.02 — JSX
JSX es una sintaxis que permite describir estructuras similares a HTML dentro de JavaScript y se transforma durante el build. Usa `className`, expresiones entre llaves y claves estables en listas; JSX no es HTML literal y aplica reglas de JavaScript.


**Práctica y evidencia:** Escribe JSX con expresiones, listas y atributos correctos. **Evidencia:** identifica diferencias con HTML, incluida `className` y la necesidad de keys estables en listas.

#### 12.6.03 — Props
Props son entradas de solo lectura que el componente recibe de su padre. Define nombres y tipos claros, evita mutarlas y pasa callbacks para comunicar acciones hacia arriba en lugar de modificar directamente el estado de otro componente.


**Práctica y evidencia:** Pasa datos y callbacks mediante props y evita mutarlas dentro del componente. **Evidencia:** demuestra flujo unidireccional y tipa las propiedades.

#### 12.6.04 — State
State representa información que puede cambiar y cuya actualización provoca un nuevo render. Trata el estado como inmutable, calcula actualizaciones desde el valor previo cuando dependa de él y evita duplicar datos derivados que puedan calcularse.


**Práctica y evidencia:** Gestiona estado local con un valor primitivo y un objeto, actualizando de forma inmutable. **Evidencia:** explica por qué mutar directamente no garantiza renderizado.

#### 12.6.05 — Hooks
Hooks permiten utilizar estado y otras capacidades de React desde componentes funcionales. Llámalos en el nivel superior y en el mismo orden en cada render; no los invoques dentro de condiciones, ciclos o funciones anidadas.


**Práctica y evidencia:** Identifica reglas de Hooks y el propósito de estado, efectos y referencias. **Evidencia:** explica por qué los Hooks deben llamarse en el nivel superior de componentes o Hooks personalizados.

#### 12.6.06 — useState
`useState` añade estado local y devuelve el valor actual y una función de actualización. Si el nuevo valor depende del anterior, utiliza la forma funcional; no modifiques arrays u objetos existentes directamente.


**Práctica y evidencia:** Implementa un contador con `useState` y una actualización funcional cuando depende del valor anterior. **Evidencia:** prueba varias actualizaciones seguidas y explica batching.

#### 12.6.07 — useEffect
`useEffect` sincroniza un componente con sistemas externos después del render, como suscripciones o temporizadores. Declara dependencias correctas y limpieza; no lo uses para calcular valores derivados que pueden obtenerse durante el render.


**Práctica y evidencia:** Utiliza `useEffect` para sincronizar con un sistema externo y limpia suscripciones o temporizadores. **Evidencia:** demuestra dependencias correctas y ausencia de efectos repetidos innecesarios.

#### 12.6.08 — useContext
`useContext` lee el valor del contexto más cercano para compartir datos a través del árbol. Mantén el contexto para información realmente transversal y divide contextos de alta frecuencia de cambio para evitar renders innecesarios.


**Práctica y evidencia:** Comparte un dato de tema o sesión mediante Context sin prop drilling excesivo. **Evidencia:** identifica proveedor, consumidor y coste de rerenderizado.

#### 12.6.09 — useRef
`useRef` conserva un objeto mutable entre renders sin provocar un render al cambiar su propiedad `current`. Sirve para referencias DOM y valores persistentes no visuales; si un cambio debe reflejarse en pantalla, normalmente corresponde a state.


**Práctica y evidencia:** Usa `useRef` para conservar una referencia DOM o valor mutable que no debe disparar renderizado. **Evidencia:** compara con state y justifica cuándo corresponde cada uno.

#### 12.6.10 — Forms
Los formularios React pueden ser controlados por estado o utilizar referencias y APIs nativas. Define validación y mensajes accesibles, evita actualizar estado de manera innecesaria por cada pulsación y protege datos sensibles en el flujo de envío.


**Práctica y evidencia:** Implementa un formulario controlado y valida valores con mensajes accesibles. **Evidencia:** prueba envío, error, corrección y conservación de datos.

#### 12.6.11 — Routing
Routing asocia rutas de URL con vistas y navegación de una aplicación. Distingue rutas cliente de navegación de servidor, maneja rutas desconocidas y protege recursos en backend; ocultar un enlace no constituye autorización.


**Práctica y evidencia:** Configura rutas y enlaces con la solución de routing seleccionada para el proyecto. **Evidencia:** prueba navegación directa, parámetros y ruta inexistente.

#### 12.6.12 — Context API
Context API distribuye valores compartidos sin pasar props por cada nivel. Es adecuada para temas, idioma o sesión de interfaz, pero no sustituye automáticamente una estrategia de estado compleja ni el almacenamiento seguro de credenciales.


**Práctica y evidencia:** Diseña Context API para estado transversal de baja o moderada frecuencia de cambio. **Evidencia:** explica cuándo conviene dividir contextos o usar otra solución de estado.

#### 12.6.13 — Component lifecycle
El ciclo de vida describe montaje, actualización y desmontaje de componentes. En componentes funcionales, efectos y su limpieza expresan sincronización con sistemas externos; el modo estricto de desarrollo puede repetir ciclos para revelar efectos no seguros.


**Práctica y evidencia:** Relaciona montaje, actualización y desmontaje con el modelo actual de componentes funcionales y efectos. **Evidencia:** explica qué sincronización se limpia al desmontar sin tratar Hooks como equivalentes literales a todos los lifecycle methods.

#### 12.6.14 — State management
State management define cómo se representa, actualiza y comparte el estado de una aplicación. Separa estado local, estado de servidor, estado de URL y estado global; selecciona la herramienta menos compleja que cubra las necesidades reales.


**Práctica y evidencia:** Compara estado local, estado compartido y estado remoto; elige dónde mantener cada dato. **Evidencia:** presenta un diagrama de flujo y evita duplicar estado derivable.

#### 12.6.15 — Custom Hooks
Custom Hooks encapsulan lógica reutilizable que usa otros hooks y devuelve datos o acciones. Sus nombres comienzan con `use`, respetan las reglas de hooks y abstraen comportamiento, no necesariamente interfaz visual.


**Práctica y evidencia:** Extrae lógica reutilizable en un Hook personalizado con nombre `use...` y dependencias claras. **Evidencia:** úsalo en dos componentes y demuestra que no comparte estado automáticamente entre llamadas.

#### 12.6.16 — Error Boundaries
Error Boundaries capturan errores de renderizado en partes del árbol React y muestran una interfaz alternativa. No capturan todos los errores asíncronos ni eventos; registra contexto sin exponer datos privados y ofrece recuperación o navegación segura.


**Práctica y evidencia:** Implementa una frontera de error para capturar errores de renderizado y ofrece fallback. **Evidencia:** demuestra qué errores captura y cuáles, como ciertos fallos asíncronos o de eventos, requieren manejo separado.

### Módulo 12.7 — Next.js

#### 12.7.01 — App Router
App Router organiza rutas y layouts mediante la estructura de archivos de `app` en Next.js. Comprende segmentos, layouts anidados, loading, error y not-found; consulta la documentación de la versión del proyecto porque convenciones pueden evolucionar.


**Práctica y evidencia:** Organiza rutas del App Router mediante estructura de carpetas y archivos especiales. **Evidencia:** documenta URL resultante, layout heredado y página correspondiente.

#### 12.7.02 — Routing
El routing de Next.js convierte segmentos de carpetas y archivos especiales en rutas. Diseña rutas legibles, parámetros dinámicos y layouts compartidos; evita asumir que toda navegación se ejecuta exclusivamente en el cliente.


**Práctica y evidencia:** Crea rutas dinámicas y navegación entre páginas, contemplando parámetros y estados no encontrados. **Evidencia:** prueba acceso directo a una URL con parámetro y ruta inexistente.

#### 12.7.03 — Server Components
Server Components se ejecutan en el servidor y permiten obtener datos y reducir JavaScript enviado al navegador. No acceden a APIs exclusivas del navegador ni manejan estado cliente; evita enviar secretos o datos no autorizados en sus props.


**Práctica y evidencia:** Identifica Server Components y sus ventajas para renderizado, acceso a datos y reducción de JavaScript enviado al cliente. **Evidencia:** explica por qué un componente servidor no puede usar Hooks de cliente.

#### 12.7.04 — Client Components
Client Components habilitan estado, eventos y APIs del navegador mediante la directiva `use client` en el límite apropiado. Mantén el límite cliente pequeño y no confundas la ejecución inicial de render con la disponibilidad de APIs del navegador.


**Práctica y evidencia:** Marca un Client Component cuando requiere interacción, estado o APIs del navegador. **Evidencia:** minimiza la frontera cliente y justifica cada componente marcado.

#### 12.7.05 — Server-side rendering
Server-side rendering genera HTML en el servidor para una solicitud o estrategia configurada. Considera hidratación, caché, datos personalizados y coste de render; evita que datos de usuario se filtren por cachés compartidas.


**Práctica y evidencia:** Explica SSR como generación de HTML en servidor para una solicitud y considera hidratación y consistencia inicial. **Evidencia:** compara HTML recibido con interfaz después de hidratación.

#### 12.7.06 — Static site generation
Static site generation produce páginas durante la compilación o regeneración configurada, reduciendo trabajo por solicitud. Es apropiada para contenido que puede servirse estáticamente; define cómo se actualiza y evita publicar datos privados o obsoletos.


**Práctica y evidencia:** Compara generación estática con renderizado dinámico y revalidación según frescura del contenido. **Evidencia:** selecciona estrategia para una página institucional y un panel personalizado.

#### 12.7.07 — Data fetching
Data fetching obtiene datos desde servicios o bases de datos dentro de los límites de ejecución de Next.js. Define caché, revalidación, timeout, manejo de errores y permisos; el lugar de la solicitud afecta rendimiento y exposición de secretos.


**Práctica y evidencia:** Obtén datos en el servidor o cliente según requisitos de caché, autenticación y latencia. **Evidencia:** documenta origen, política de caché, manejo de errores y datos que nunca deben exponerse al navegador.

#### 12.7.08 — Authentication
La autenticación identifica al usuario y la autorización determina qué puede hacer. Usa bibliotecas y protocolos mantenidos, valida sesión y permisos en el servidor y no confíes en rutas protegidas solo por controles de interfaz.


**Práctica y evidencia:** Implementa autenticación usando una biblioteca o proveedor mantenido y protege rutas/acciones en servidor. **Evidencia:** demuestra verificación de sesión y autorización por recurso; ocultar un enlace no basta.

#### 12.7.09 — Metadata
Metadata permite definir título, descripción, iconos y otras propiedades de página desde la configuración de Next.js. Genera metadatos coherentes por ruta, evita duplicados y no incluyas datos personales o secretos en valores públicos.


**Práctica y evidencia:** Define metadata por página con título, descripción y metadatos sociales coherentes. **Evidencia:** inspecciona HTML generado y evita duplicar títulos entre rutas.

#### 12.7.10 — Deployment
Deployment publica la aplicación y su configuración en un entorno de ejecución. Documenta variables de entorno, build, runtime, migraciones, observabilidad, rollback y dominio; no incluyas secretos en repositorio ni confundas build exitoso con servicio saludable.


**Práctica y evidencia:** Prepara despliegue con variables de entorno, build reproducible, revisión de dependencias y configuración de runtime. **Evidencia:** documenta comandos, variables requeridas sin valores secretos y health check.

### Módulo 12.8 — Herramientas

#### 12.8.01 — npm
npm instala paquetes, ejecuta scripts y administra dependencias mediante `package.json` y un lockfile. Revisa scripts antes de ejecutarlos, fija versiones según política y evita instalar paquetes de nombres parecidos sin verificar el mantenedor.


**Práctica y evidencia:** Utiliza npm para instalar dependencias y scripts definidos en package.json. **Evidencia:** explica diferencia entre dependencias de runtime y desarrollo y conserva lockfile.

#### 12.8.02 — pnpm
pnpm gestiona dependencias con un almacén de contenido direccionado y enlaces, optimizando espacio y consistencia. Conserva `pnpm-lock.yaml`, documenta la versión del gestor y no mezcles lockfiles sin una decisión explícita del equipo.


**Práctica y evidencia:** Compara pnpm con npm en almacenamiento, enlaces y workspace; no mezcles gestores en el mismo proyecto sin decisión explícita. **Evidencia:** instala desde lockfile y documenta gestor/versión.

#### 12.8.03 — Vite
Vite ofrece servidor de desarrollo y proceso de build para aplicaciones frontend. Configura plugins y variables con cuidado, recuerda que las variables expuestas al cliente son públicas y valida el artefacto de producción además del servidor local.


**Práctica y evidencia:** Configura Vite para desarrollo y build, distinguiendo servidor de desarrollo y artefactos de producción. **Evidencia:** ejecuta build y verifica rutas de recursos en el resultado.

#### 12.8.04 — ESLint
ESLint analiza patrones de código y aplica reglas para detectar errores potenciales y mantener convenciones. Configura reglas compatibles con la versión del lenguaje y framework; no desactives globalmente reglas para ocultar advertencias recurrentes.


**Práctica y evidencia:** Configura ESLint con reglas del proyecto y corrige problemas reales sin desactivar reglas globalmente. **Evidencia:** presenta salida de lint y justifica excepciones locales.

#### 12.8.05 — Prettier
Prettier formatea código de manera consistente y reduce discusiones de estilo. Fija configuración compartida y ejecútalo en el flujo del proyecto; el formateador no reemplaza linting, revisión ni pruebas.


**Práctica y evidencia:** Configura Prettier para formato consistente y evita que compita con reglas de lint. **Evidencia:** formatea archivos y demuestra que una segunda ejecución no genera cambios adicionales.

#### 12.8.06 — Tailwind CSS
Tailwind CSS ofrece utilidades de bajo nivel para expresar estilos directamente en el marcado. Mantén tokens y patrones reutilizables, revisa el tamaño del CSS generado y evita construir nombres de clase dinámicos que el proceso de detección no pueda identificar.


**Práctica y evidencia:** Aplica utilidades Tailwind para construir componentes y organiza tokens/configuración según la versión utilizada. **Evidencia:** muestra diseño responsivo y documenta versión y mecanismo de configuración.

#### 12.8.07 — React DevTools
React DevTools permite inspeccionar árbol de componentes, props, estado y rendimiento en desarrollo. Utilízalo para localizar renders y estructura; evita compartir capturas con datos de usuario o tokens y no lo confundas con una prueba de rendimiento completa.



**Práctica y evidencia:** Usa React DevTools para inspeccionar árbol de componentes, props, estado y renders. **Evidencia:** identifica un renderizado innecesario y demuestra su causa antes de optimizar.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 89 orientaciones genéricas del desglose por explicaciones específicas de cada entrada oficial. Se añadieron precisiones sobre semántica y coerción de JavaScript, closures/prototypes/this, propagación de eventos, ciclo de eventos y microtasks, almacenamiento del navegador, límites de TypeScript en runtime, reglas de hooks, Server/Client Components, caché, autenticación y seguridad de dependencias.

**Revisión interna:** 89/89 entradas desarrolladas y cotejadas con el roadmap. La guía principal conserva ejemplos, proyecto y evaluación. Pendiente: fijar versiones exactas de Node.js, TypeScript, React y Next.js para ejecución reproducible; compilar, ejecutar pruebas de componentes y accesibilidad, validar APIs y revisar el despliegue. Esta revisión documental no acredita ejecución ni aprobación externa.
