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

**Laboratorio de profundización — Alcance y mutabilidad de variables.**

1. Compara `let`, `const` y `var` en bloques y funciones. 2. Prueba reasignación y redeclaración. 3. Identifica errores de referencia temporal. 4. Define qué bindings deben ser constantes en un módulo.

**Evidencia esperada.** El ejemplo demuestra alcance léxico y distingue mutabilidad del binding y mutabilidad del objeto.

**Seguridad y límites.** No utilizar `var` en código nuevo sin razón de compatibilidad ni depender de variables globales.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.02 — Tipos

JavaScript es dinámico y los valores tienen tipos como string, number, bigint, boolean, undefined, symbol y object; null es un valor primitivo especial pese a typeof histórico.

**Ejemplo técnico:** typeof null devuelve 'object' por una peculiaridad histórica.

**Práctica guiada:** Prueba typeof en valores primitivos y objetos.

**Actividad independiente:** Clasifica entradas y define validación antes de operar.

**Criterios de aceptación:** No se confunden tipos ni coerciones implícitas.

**Errores frecuentes:** Asumir que typeof null devuelve null.

**Comprobación:** ¿Qué diferencia hay entre tipo de variable y tipo del valor actual?

**Laboratorio de profundización — Conversión y coerción de tipos.**

1. Compara string, number, bigint, boolean, null, undefined y symbol. 2. Prueba `typeof` y `Number.isNaN`. 3. Evalúa coerciones explícitas e implícitas. 4. Diseña validación de entrada de formulario.

**Evidencia esperada.** Se identifica tipo real y conversión y se manejan NaN y valores ausentes correctamente.

**Seguridad y límites.** No confiar en coerción implícita para validar datos externos.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.03 — Operadores

Los operadores realizan operaciones aritméticas, comparación, lógica, asignación y coalescencia. `===` evita coerción en comparación de igualdad; `??` usa fallback solo ante null/undefined, a diferencia de `||`.

**Ejemplo técnico:** `valor ?? 'sin dato'` conserva 0 y cadena vacía.

**Práctica guiada:** Prueba ==/===, ||/?? y precedencia con valores límite.

**Actividad independiente:** Construye expresiones de validación sin coerciones ambiguas.

**Criterios de aceptación:** Resultados previstos para null, 0, false y ''.

**Errores frecuentes:** Usar == sin comprender coerción o confundir || con ??.

**Comprobación:** ¿Qué valor de entrada distingue ?? de ||?

**Laboratorio de profundización — Precedencia y evaluación corta.**

1. Evalúa expresiones con operadores aritméticos, comparación, igualdad estricta y lógica. 2. Compara `==` con `===`. 3. Prueba `&&`, `||` y `??`. 4. Añade paréntesis para expresar intención.

**Evidencia esperada.** El resultado se explica por precedencia y short-circuit y se prefiere igualdad estricta cuando corresponde.

**Seguridad y límites.** No utilizar eval para ejecutar expresiones recibidas de usuarios.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.04 — Condicionales

if/else, switch y operador ternario controlan ramificación. La comparación debe ser explícita y las ramas exhaustivas cuando el dominio lo exige.

**Ejemplo técnico:** switch sobre estado con default que maneja valor desconocido.

**Práctica guiada:** Prueba ramas verdadera/falsa y estados no contemplados.

**Actividad independiente:** Implementa validación de estados de pedido.

**Criterios de aceptación:** Cada estado posible tiene comportamiento definido.

**Errores frecuentes:** Olvidar default o anidar ternarios ilegibles.

**Comprobación:** ¿Por qué conviene manejar el caso desconocido?

**Laboratorio de profundización — Ramas exhaustivas y casos límite.**

1. Implementa una clasificación de estados mediante if/else y switch. 2. Incluye null, undefined y valores inesperados. 3. Compara switch con objeto mapa. 4. Prueba cada rama.

**Evidencia esperada.** Todas las ramas están cubiertas y el caso por defecto es explícito.

**Seguridad y límites.** No asumir que una entrada externa pertenece a un conjunto válido sin comprobarla.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.05 — Bucles

for, while, do...while, for...of y for...in recorren estructuras con semánticas diferentes. for...of itera valores iterables; for...in enumera claves enumerables, por lo que no es sustituto general para arrays.

**Ejemplo técnico:** for...of sobre array devuelve elementos; for...in devuelve índices como cadenas.

**Práctica guiada:** Compara iteraciones sobre array y objeto.

**Actividad independiente:** Procesa colección con salida temprana y condición de terminación.

**Criterios de aceptación:** No se omiten ni duplican elementos.

**Errores frecuentes:** Usar for...in para arrays sin controlar propiedades heredadas.

**Comprobación:** ¿Qué diferencia hay entre for...of y for...in?

**Laboratorio de profundización — Iteración segura de colecciones.**

1. Compara for, while, for...of y for...in. 2. Recorre array y objeto. 3. Explica diferencia entre valores e índices/propiedades. 4. Evita mutar colección durante iteración sin diseño.

**Evidencia esperada.** Se elige el iterador adecuado y se evita recorrer propiedades heredadas accidentalmente.

**Seguridad y límites.** No utilizar for...in para arrays cuando se requieren valores en orden.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.06 — Funciones

Las funciones encapsulan comportamiento y pueden declararse, asignarse o expresarse como arrow functions. Parámetros, retorno, efectos secundarios y contrato deben ser claros.

**Ejemplo técnico:** Una función pura recibe número y devuelve doble sin modificar estado externo.

**Práctica guiada:** Implementa funciones con parámetros, retorno y casos límite.

**Actividad independiente:** Divide un cálculo en funciones pequeñas y comprobables.

**Criterios de aceptación:** Entradas/salidas definidas y sin efectos inesperados.

**Errores frecuentes:** Funciones largas que mezclan entrada, cálculo y DOM.

**Comprobación:** ¿Qué característica hace que una función sea pura?

**Laboratorio de profundización — Parámetros, retorno y funciones puras.**

1. Implementa función con parámetros por defecto. 2. Compara declaración, expresión y arrow function. 3. Identifica efectos secundarios. 4. Escribe pruebas para entradas límite.

**Evidencia esperada.** La función tiene contrato claro, retorno predecible y efectos secundarios controlados.

**Seguridad y límites.** No asumir que arrow function tiene this propio.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.07 — Objetos

Los objetos agrupan propiedades y métodos. Las propiedades pueden ser propias o heredadas; la mutación afecta referencias compartidas. Object.keys/entries y destructuring facilitan inspección.

**Ejemplo técnico:** Dos variables que apuntan al mismo objeto observan la misma mutación.

**Práctica guiada:** Crea objeto y compara copia por referencia con copia superficial.

**Actividad independiente:** Modela objeto de pedido con propiedades validadas.

**Criterios de aceptación:** Se explica identidad y mutabilidad de referencias.

**Errores frecuentes:** Creer que asignar objeto a otra variable lo clona.

**Comprobación:** ¿Qué sucede al modificar un objeto desde una segunda referencia?

**Laboratorio de profundización — Propiedades, referencias y copia.**

1. Crea objeto con propiedades y métodos. 2. Compara asignación por referencia con copia superficial. 3. Modifica objeto anidado y observa aliasing. 4. Diseña actualización inmutable.

**Evidencia esperada.** Se explica referencia compartida y límites de spread/Object.assign para objetos anidados.

**Seguridad y límites.** No utilizar JSON stringify/parse como clonación universal de objetos.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.08 — Arrays

Los arrays son objetos indexados y ordenados; métodos como map, filter, reduce, find y some expresan transformaciones. Algunos mutan (sort, splice, push) y otros devuelven nuevos arrays.

**Ejemplo técnico:** filter selecciona; map transforma; reduce acumula.

**Práctica guiada:** Aplica map/filter/reduce a datos sintéticos y compara original.

**Actividad independiente:** Construye pipeline de transformación sin mutar entrada.

**Criterios de aceptación:** Resultado y mutación están documentados.

**Errores frecuentes:** Confundir métodos mutables e inmutables o mutar estado React directamente.

**Comprobación:** ¿Qué diferencia hay entre map y forEach?

**Laboratorio de profundización — Transformación funcional de arrays.**

1. Usa map, filter, reduce, find y some con dataset sintético. 2. Compara métodos mutables e inmutables. 3. Encadena transformaciones. 4. Prueba array vacío y valores faltantes.

**Evidencia esperada.** Cada operación devuelve el resultado esperado y se justifica si modifica o no el array original.

**Seguridad y límites.** No usar reduce para todo cuando map/filter expresan mejor la intención.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.09 — Strings

Las cadenas son inmutables y ofrecen métodos de búsqueda, extracción, normalización y reemplazo. Template literals interpolan expresiones; Unicode puede requerir cuidado con unidades UTF-16 y grafemas.

**Ejemplo técnico:** `texto.trim().toLowerCase()` normaliza espacios y mayúsculas simples.

**Práctica guiada:** Prueba slice, includes, replace y trim con entradas acentuadas.

**Actividad independiente:** Normaliza y valida una etiqueta sin perder caracteres Unicode.

**Criterios de aceptación:** Se documenta tratamiento de espacios y caracteres.

**Errores frecuentes:** Asumir que length equivale siempre a cantidad de caracteres percibidos.

**Comprobación:** ¿Por qué una cadena Unicode puede tener length distinto al número de símbolos visibles?

**Laboratorio de profundización — Unicode, búsqueda y plantillas.**

1. Construye strings con template literals. 2. Prueba includes, startsWith, slice y replace. 3. Compara longitud UTF-16 con cantidad de grafemas. 4. Normaliza y valida entradas según dominio.

**Evidencia esperada.** La solución distingue unidades de código y caracteres percibidos y maneja espacios y Unicode.

**Seguridad y límites.** No asumir que length representa siempre caracteres visibles ni insertar texto no confiable como HTML.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.10 — Destructuring

Destructuring extrae valores de arrays y propiedades de objetos en variables, con valores por defecto y renombrado. En objetos, el nombre de propiedad y variable puede diferir.

**Ejemplo técnico:** `const {nombre: etiqueta = 'Invitado'} = usuario;`

**Práctica guiada:** Extrae campos presentes, ausentes y anidados.

**Actividad independiente:** Refactoriza acceso repetido a propiedades con destructuring legible.

**Criterios de aceptación:** Defaults solo aplican a undefined y el origen está claro.

**Errores frecuentes:** Confundir default de destructuring con fallback ante null.

**Comprobación:** ¿Qué ocurre si la propiedad existe con valor null?

**Laboratorio de profundización — Extracción de estructuras.**

1. Extrae propiedades y elementos con destructuring. 2. Define valores por defecto. 3. Renombra propiedades. 4. Maneja propiedades ausentes y valores null con seguridad.

**Evidencia esperada.** La extracción es legible y los valores opcionales se manejan sin errores inesperados.

**Seguridad y límites.** No destructurar profundamente datos externos sin validar forma y nulabilidad.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.11 — Spread

Spread expande elementos iterables o propiedades enumerables en nuevos contextos. La copia de arrays/objetos suele ser superficial; objetos anidados conservan referencias.

**Ejemplo técnico:** `const copia = {...original}` crea objeto distinto, pero conserva referencia a subobjetos.

**Práctica guiada:** Compara identidad y mutación en copia superficial.

**Actividad independiente:** Actualiza una propiedad anidada sin mutar el estado original.

**Criterios de aceptación:** Se identifica qué niveles fueron copiados.

**Errores frecuentes:** Creer que spread realiza clonación profunda.

**Comprobación:** ¿Qué limitación tiene la copia superficial?

**Laboratorio de profundización — Composición y copia superficial.**

1. Combina arrays y objetos con spread. 2. Demuestra que la copia es superficial. 3. Actualiza propiedad anidada sin mutar original. 4. Compara con structuredClone cuando esté disponible y sea apropiado.

**Evidencia esperada.** La operación conserva inmutabilidad del nivel actualizado y explica referencias anidadas.

**Seguridad y límites.** No confundir spread con clonación profunda ni usarlo para copiar objetos con comportamiento especial sin evaluar.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.12 — Rest

Rest recoge elementos restantes en parámetros, destructuring o arrays/objetos. En parámetros debe aparecer al final y permite funciones de aridad variable.

**Ejemplo técnico:** `function sumar(...valores)` recibe argumentos en un array.

**Práctica guiada:** Implementa función con cantidad variable de argumentos.

**Actividad independiente:** Combina primer parámetro y resto para un reporte.

**Criterios de aceptación:** El resto captura exactamente argumentos no asignados.

**Errores frecuentes:** Confundir rest con spread pese a sintaxis parecida.

**Comprobación:** ¿En qué contexto `...` recoge valores en vez de expandirlos?

**Laboratorio de profundización — Parámetros variables y recolección.**

1. Define función que reciba primer argumento y rest de elementos. 2. Combina rest con destructuring. 3. Compara rest parameters con objeto arguments. 4. Valida cantidad de argumentos.

**Evidencia esperada.** La función recoge argumentos restantes como array y mantiene firma comprensible.

**Seguridad y límites.** Rest debe ser el último parámetro; no aceptar listas ilimitadas sin validar tamaño.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.13 — Scope

El scope determina dónde es accesible un identificador: global, función y bloque. let/const tienen alcance de bloque; var de función. Shadowing puede ocultar variables externas y dificultar lectura.

**Ejemplo técnico:** Una let declarada dentro de if no existe fuera del bloque.

**Práctica guiada:** Prueba acceso antes/después de bloque y función.

**Actividad independiente:** Refactoriza variables globales a alcance mínimo.

**Criterios de aceptación:** Cada identificador tiene alcance intencional.

**Errores frecuentes:** Crear globals accidentales o reutilizar nombres que ocultan valores externos.

**Comprobación:** ¿Qué diferencia el scope de bloque del scope de función?

**Laboratorio de profundización — Ámbito léxico y cadena de entornos.**

1. Compara global, función y bloque. 2. Prueba shadowing con nombres repetidos. 3. Identifica dónde resuelve una referencia. 4. Reestructura variables para minimizar alcance.

**Evidencia esperada.** El resultado se explica mediante cadena léxica y se evitan variables globales innecesarias.

**Seguridad y límites.** No depender de variables globales mutables para comunicar estado entre módulos.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.14 — Closures

Una closure conserva acceso al entorno léxico donde se creó la función, incluso después de que la función externa termina. Se utiliza para encapsular estado, callbacks y factories; también puede retener memoria si mantiene referencias innecesarias.

**Ejemplo técnico:** Una función contador puede cerrar sobre una variable privada y exponer incremento/lectura.

**Práctica guiada:** Crea contador y dos instancias independientes.

**Actividad independiente:** Diseña factory que encapsule configuración sin exponer mutación directa.

**Criterios de aceptación:** Instancias mantienen estados separados.

**Errores frecuentes:** Asumir que closure copia valores en vez de conservar entorno léxico.

**Comprobación:** ¿Por qué dos closures creadas por llamadas distintas pueden mantener estados independientes?

**Laboratorio de profundización — Cierre sobre estado privado.**

1. Implementa una función creadora de contador. 2. Devuelve funciones que leen y modifican el estado capturado. 3. Crea dos instancias y comprueba aislamiento. 4. Explica ciclo de vida de referencias.

**Evidencia esperada.** Cada closure mantiene estado independiente y se identifica qué variables conserva.

**Seguridad y límites.** No capturar accidentalmente objetos grandes o datos sensibles por tiempo indefinido.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.15 — Hoisting

Hoisting describe cómo declaraciones se procesan antes de ejecutar código. function declarations pueden invocarse antes de su ubicación; var se inicializa como undefined; let/const permanecen en temporal dead zone hasta inicialización.

**Ejemplo técnico:** Acceder a let antes de declararla produce ReferenceError.

**Práctica guiada:** Compara function, var, let y const en ejemplos aislados.

**Actividad independiente:** Refactoriza código para declarar dependencias antes de uso.

**Criterios de aceptación:** No se depende de comportamiento confuso de hoisting.

**Errores frecuentes:** Decir que let/const no se elevan; se elevan pero quedan en TDZ.

**Comprobación:** ¿Qué es la temporal dead zone?

**Laboratorio de profundización — Inicialización y zona temporal muerta.**

1. Compara declaración function, var, let y const antes de su línea textual. 2. Observa errores de TDZ. 3. Explica qué se eleva y qué no. 4. Refactoriza para declarar antes de usar.

**Evidencia esperada.** Se predice comportamiento y se distingue hoisting de inicialización.

**Seguridad y límites.** No depender de hoisting como estilo; ordenar declaraciones para claridad.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.16 — Prototypes

La herencia de JavaScript se basa en cadena de prototipos. Los objetos pueden delegar búsqueda de propiedades a su prototype; class es sintaxis sobre este mecanismo. Object.create y Object.getPrototypeOf permiten inspección.

**Ejemplo técnico:** Una instancia puede heredar método desde prototype sin copiarlo como propiedad propia.

**Práctica guiada:** Compara Object.hasOwn y búsqueda heredada.

**Actividad independiente:** Modela comportamiento compartido y explica cuándo preferir composición.

**Criterios de aceptación:** Se distingue propiedad propia de heredada.

**Errores frecuentes:** Confundir prototype de función con [[Prototype]] de instancia.

**Comprobación:** ¿Qué sucede cuando una propiedad no existe como propia?

**Laboratorio de profundización — Cadena de prototipos.**

1. Crea objeto con Object.create. 2. Consulta Object.getPrototypeOf y hasOwn. 3. Compara propiedad propia y heredada. 4. Explica método compartido frente a método duplicado.

**Evidencia esperada.** Se identifica resolución por cadena y diferencia entre propiedad propia y heredada.

**Seguridad y límites.** No modificar prototipos globales de objetos nativos.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.17 — This

El valor de this depende del modo de invocación, no solo del lugar donde se define la función. Arrow functions capturan this léxico; métodos tradicionales reciben this según receptor y bind/call/apply pueden fijarlo.

**Ejemplo técnico:** obj.metodo() vincula this a obj; extraer método puede perder ese receptor.

**Práctica guiada:** Prueba método, función extraída, bind y arrow function.

**Actividad independiente:** Corrige callback que pierde contexto de this.

**Criterios de aceptación:** Contexto de this explicado por invocación.

**Errores frecuentes:** Asumir que this siempre apunta al objeto que contiene la definición.

**Comprobación:** ¿Por qué una arrow function no crea su propio this?

**Laboratorio de profundización — Binding de this según invocación.**

1. Compara método, llamada independiente, bind, call y apply. 2. Prueba arrow function dentro de objeto. 3. Explica this léxico. 4. Corrige callback que pierde contexto.

**Evidencia esperada.** El valor de this se predice según forma de invocación y se corrige explícitamente.

**Seguridad y límites.** No asumir que this apunta siempre al objeto donde se definió la función.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.18 — ES6+

ECMAScript moderno incorpora módulos, let/const, arrow functions, clases, promesas, destructuring, spread, iteradores y otras mejoras. La compatibilidad depende del runtime y objetivo de compilación.

**Ejemplo técnico:** Una aplicación puede usar async/await en runtime moderno o transpilar para navegadores antiguos.

**Práctica guiada:** Identifica características modernas en código y comprueba soporte del target.

**Actividad independiente:** Actualiza un fragmento legacy conservando comportamiento y compatibilidad.

**Criterios de aceptación:** La característica se usa según soporte y necesidad.

**Errores frecuentes:** Confundir versión del lenguaje con versión de Node/navegador.

**Comprobación:** ¿Qué papel cumple un target de compilación?

**Laboratorio de profundización — Uso de características modernas del lenguaje.**

1. Reescribe código con let/const, template literals, destructuring, spread, módulos y async/await. 2. Comprueba compatibilidad del runtime objetivo. 3. Evita transformaciones innecesarias. 4. Documenta soporte de navegadores o Node.

**Evidencia esperada.** El código utiliza sintaxis moderna con compatibilidad definida y sin cambiar semántica accidentalmente.

**Seguridad y límites.** No asumir soporte uniforme de toda característica por todos los navegadores y runtimes.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 12.1.19 — Modules

Los módulos ES utilizan export e import, tienen scope propio y se evalúan una vez por módulo en un grafo de dependencias. Los imports estáticos deben estar en nivel superior; la resolución depende del entorno y configuración.

**Ejemplo técnico:** Export nombrado y default tienen sintaxis y consumo distintos.

**Práctica guiada:** Separa función y constantes en dos módulos y prueba importaciones.

**Actividad independiente:** Organiza utilidades con API pública mínima.

**Criterios de aceptación:** Dependencias explícitas y sin ciclos innecesarios.

**Errores frecuentes:** Confundir CommonJS require con import ESM o exportar internals innecesarios.

**Comprobación:** ¿Qué diferencia existe entre export nombrado y default?


**Laboratorio de profundización — Diseño de módulos y límites de dependencias.**

1. Separa funciones en módulos ES. 2. Compara export nombrado y default. 3. Construye import relativo. 4. Identifica ciclo de dependencias y define API pública pequeña.

**Evidencia esperada.** Los módulos tienen responsabilidades claras y dependencias explícitas.

**Seguridad y límites.** No exponer secretos en módulos frontend ni asumir que ocultar una variable en bundle la protege.

**Registro sugerido.** Conserva runtime y versión, código mínimo, entradas de prueba, salida y observaciones sobre compatibilidad. No marques la práctica como ejecutada sin evidencia real.
#### 12.2.01 — Document Object Model

El DOM representa el documento como árbol de nodos y permite consultar/modificar estructura, atributos y texto. El DOM vivo refleja cambios; no es lo mismo que el HTML fuente inicial.

**Ejemplo técnico:** document.querySelector('main') obtiene el primer main del documento.

**Práctica guiada:** Inspecciona árbol DOM y relación padre/hijo.

**Actividad independiente:** Construye estructura simple y localiza nodos por selector.

**Criterios de aceptación:** Se distingue fuente, DOM y renderizado.

**Errores frecuentes:** Asumir que DOM y HTML fuente siempre son idénticos.

**Comprobación:** ¿Qué ocurre con el DOM después de modificar un nodo?

**Laboratorio de profundización — Inspección del árbol DOM.**

1. Abre una página propia y examina document, html, head y body. 2. Identifica nodos elemento, texto y atributo. 3. Compara DOM con código fuente recibido. 4. Explica cómo JavaScript puede cambiar el árbol en ejecución.

**Evidencia esperada.** El estudiante identifica nodos y diferencia DOM actual de fuente HTML inicial.

**Seguridad y límites.** No asumir que el DOM refleja fielmente el servidor ni insertar HTML no confiable.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.2.02 — Selección de elementos

querySelector/querySelectorAll usan selectores CSS y devuelven elemento o NodeList; getElementById busca por id. La selección debe ser específica y manejar ausencia de resultados.

**Ejemplo técnico:** querySelectorAll('.item') devuelve colección estática de coincidencias.

**Práctica guiada:** Selecciona por id, clase y atributo; prueba cero coincidencias.

**Actividad independiente:** Implementa función que valida si un elemento existe antes de usarlo.

**Criterios de aceptación:** No hay referencias nulas no controladas.

**Errores frecuentes:** Asumir que querySelectorAll devuelve array o que siempre encuentra nodo.

**Comprobación:** ¿Qué diferencia hay entre querySelector y querySelectorAll?

**Laboratorio de profundización — Selección precisa y alcance.**

1. Usa getElementById, querySelector y querySelectorAll. 2. Compara NodeList y elemento único. 3. Maneja selector sin coincidencias. 4. Limita búsqueda a un contenedor cuando sea posible.

**Evidencia esperada.** La selección es específica y el código contempla ausencia de elementos.

**Seguridad y límites.** No construir selectores con entrada no validada ni asumir que querySelector devuelve siempre un nodo.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.2.03 — Manipulación del DOM

Se pueden crear, insertar, reemplazar y eliminar nodos. textContent trata contenido como texto; innerHTML interpreta marcado y requiere sanitización estricta ante datos no confiables.

**Ejemplo técnico:** createElement + textContent evita interpretar texto de usuario como HTML.

**Práctica guiada:** Crea lista dinámica con createElement y append.

**Actividad independiente:** Renderiza datos sintéticos sin concatenar HTML no confiable.

**Criterios de aceptación:** Datos se presentan sin ejecutar marcado no previsto.

**Errores frecuentes:** Insertar entradas de usuario con innerHTML sin sanitizar.

**Comprobación:** ¿Por qué textContent es más seguro para mostrar texto no confiable?

**Laboratorio de profundización — Actualización segura de contenido.**

1. Cambia texto con textContent. 2. Crea elementos con createElement y append. 3. Compara textContent con innerHTML. 4. Elimina un nodo de prueba.

**Evidencia esperada.** La actualización conserva estructura y no interpreta texto de usuario como HTML.

**Seguridad y límites.** Evitar innerHTML con datos no confiables; considerar sanitización cuando el caso requiere HTML.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.2.04 — Eventos

Los eventos notifican acciones o cambios; el objeto Event contiene tipo, target, currentTarget y otros datos. La propagación incluye fases de captura, target y burbujeo.

**Ejemplo técnico:** click se propaga desde el elemento objetivo hacia ancestros durante bubbling.

**Práctica guiada:** Registra target/currentTarget y observa propagación.

**Actividad independiente:** Implementa acción con evento y estado accesible.

**Criterios de aceptación:** El manejador responde al evento correcto sin efectos duplicados.

**Errores frecuentes:** Usar eventos inline en HTML y mezclar responsabilidades.

**Comprobación:** ¿Qué diferencia target de currentTarget?

**Laboratorio de profundización — Modelo de eventos del navegador.**

1. Añade evento click a botón semántico. 2. Inspecciona event.target y currentTarget. 3. Cancela comportamiento por defecto solo cuando sea necesario. 4. Comprueba interacción con teclado.

**Evidencia esperada.** El evento se gestiona en el elemento apropiado y el control funciona con entrada estándar.

**Seguridad y límites.** No reemplazar enlaces y botones nativos por divs con click sin soporte completo.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.2.05 — Event listeners

addEventListener registra manejadores con opciones como capture, once, passive y signal. removeEventListener requiere referencia compatible; AbortController permite cancelar grupos de listeners.

**Ejemplo técnico:** {once:true} ejecuta manejador una vez; signal permite limpiar listeners al abortar.

**Práctica guiada:** Registra y retira listener con referencia estable.

**Actividad independiente:** Implementa componente que limpia listeners al desmontarse.

**Criterios de aceptación:** No quedan listeners duplicados tras recrear componente.

**Errores frecuentes:** Crear listeners repetidos sin cleanup o pasar función distinta al retirar.

**Comprobación:** ¿Por qué guardar referencia al callback facilita removeEventListener?

**Laboratorio de profundización — Registro y limpieza de listeners.**

1. Añade listener con addEventListener. 2. Define función nombrada para poder retirar listener. 3. Usa opciones once/passive/capture en escenarios pertinentes. 4. Comprueba que no se duplique el registro.

**Evidencia esperada.** El listener se registra una vez y se retira cuando el componente deja de necesitarlo.

**Seguridad y límites.** No crear listeners globales sin limpiar ni usar passive cuando se requiere preventDefault.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.2.06 — Event bubbling

En bubbling el evento asciende desde target por ancestros; stopPropagation detiene propagación y preventDefault cancela acción predeterminada cuando es cancelable. No deben usarse indiscriminadamente.

**Ejemplo técnico:** Un click en botón puede activar listener del contenedor padre.

**Práctica guiada:** Compara bubbling y capture con árbol simple.

**Actividad independiente:** Evita detener propagación salvo que exista razón de interacción.

**Criterios de aceptación:** Comportamiento predecible y sin handlers duplicados.

**Errores frecuentes:** Confundir stopPropagation con preventDefault.

**Comprobación:** ¿Qué cancela preventDefault y qué detiene stopPropagation?

**Laboratorio de profundización — Propagación y control de eventos.**

1. Crea elementos anidados con listeners. 2. Observa bubbling y capture. 3. Compara stopPropagation y stopImmediatePropagation. 4. Explica cuándo no conviene detener propagación.

**Evidencia esperada.** Se identifica fase de captura, target y bubbling y se evita bloquear componentes superiores sin razón.

**Seguridad y límites.** No detener propagación como solución general a conflictos de eventos.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.2.07 — Event delegation

La delegación coloca un listener en un ancestro para manejar eventos de descendientes mediante target/closest. Reduce listeners en listas dinámicas, pero requiere validar que el target pertenezca al contenedor.

**Ejemplo técnico:** Un ul gestiona clicks de sus li mediante closest('li').

**Práctica guiada:** Añade y elimina elementos y comprueba que listener delegado sigue funcionando.

**Actividad independiente:** Implementa lista dinámica con acciones por item.

**Criterios de aceptación:** Acciones se limitan al contenedor y reconocen elementos correctos.

**Errores frecuentes:** Confiar en target exacto cuando el clic ocurre en un icono hijo.

**Comprobación:** ¿Qué ventaja ofrece closest al delegar eventos?

**Laboratorio de profundización — Delegación para listas dinámicas.**

1. Coloca listener en contenedor. 2. Detecta elemento objetivo mediante closest. 3. Añade y elimina filas dinámicamente. 4. Comprueba que nuevos elementos hereden comportamiento.

**Evidencia esperada.** Un listener maneja elementos actuales y futuros y valida que el target pertenezca al contenedor.

**Seguridad y límites.** No confiar en atributos data-* como autorización o validar selectores de forma insegura.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.2.08 — Formularios

Los formularios generan submit y exponen valores mediante FormData. Deben manejar submit, validar entradas, informar errores y prevenir navegación solo cuando la aplicación controla el flujo. Validación servidor sigue siendo obligatoria.

**Ejemplo técnico:** new FormData(form) recoge controles con atributo name.

**Práctica guiada:** Captura submit, inspecciona FormData y evita enviar datos reales.

**Actividad independiente:** Implementa formulario de laboratorio con estados y mensajes accesibles.

**Criterios de aceptación:** Datos y errores se procesan sin pérdida y sin confiar solo en cliente.

**Errores frecuentes:** Leer inputs por selector frágil o validar únicamente en navegador.

**Comprobación:** ¿Por qué los controles necesitan name para incluirse en FormData?

**Laboratorio de profundización — Procesamiento de submit.**

1. Captura submit del formulario. 2. Usa FormData para recopilar campos. 3. Evita recarga solo cuando corresponda. 4. Presenta estado de envío y errores.

**Evidencia esperada.** El formulario procesa datos con nombres y valores correctos y mantiene feedback accesible.

**Seguridad y límites.** La validación cliente no sustituye servidor, CSRF ni autorización.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.2.09 — Validaciones

La validación combina restricciones HTML, lógica cliente y reglas autoritativas del servidor. Constraint Validation API expone validity, checkValidity y setCustomValidity. Errores deben ser específicos, accesibles y no filtrar información sensible.

**Ejemplo técnico:** input type=email valida formato básico, no existencia del buzón ni permiso de uso.

**Práctica guiada:** Prueba required, minlength y setCustomValidity con datos sintéticos.

**Actividad independiente:** Diseña validación con resumen y mensaje asociado al campo.

**Criterios de aceptación:** Casos válidos/invalidos cubiertos y mensajes claros.

**Errores frecuentes:** Confiar en HTML como barrera de seguridad o usar mensajes genéricos que no permiten corregir.

**Comprobación:** ¿Qué validaciones deben repetirse en servidor?

**Laboratorio de profundización — Validación cliente y servidor.**

1. Define reglas para email, longitud y campos requeridos. 2. Combina restricciones HTML y JavaScript. 3. Prueba entradas límite y caracteres Unicode. 4. Documenta validaciones equivalentes en backend.

**Evidencia esperada.** La validación produce mensajes útiles y se reconoce que el servidor es la autoridad final.

**Seguridad y límites.** No confiar en JavaScript para impedir datos maliciosos ni filtrar solo por regex simplista.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.01 — Synchronous programming

En ejecución síncrona, las instrucciones se procesan en orden y una operación bloqueante impide continuar en ese hilo hasta completarse. JavaScript en navegador ejecuta código de cada contexto principal en un hilo de ejecución, aunque el runtime use otros hilos internamente.

**Ejemplo técnico:** Un bucle costoso en el hilo principal bloquea interacción y renderizado.

**Práctica guiada:** Mide duración de una operación sintética y observa bloqueo de UI.

**Actividad independiente:** Refactoriza trabajo pesado para no congelar interacción.

**Criterios de aceptación:** Se identifica qué operación bloquea y cómo medirla.

**Errores frecuentes:** Confundir síncrono con «rápido» o asumir que todo JavaScript es monohilo en todos los contextos.

**Comprobación:** ¿Qué experiencia percibe el usuario cuando el hilo principal queda bloqueado?

**Laboratorio de profundización — Orden secuencial y bloqueo.**

1. Ejecuta una secuencia de funciones síncronas. 2. Mide tiempo de una operación intensiva en UI. 3. Identifica bloqueo del hilo principal. 4. Propón dividir trabajo o delegar a Web Worker cuando proceda.

**Evidencia esperada.** El análisis identifica qué tarea bloquea y propone una solución adecuada al entorno.

**Seguridad y límites.** No ejecutar bucles intensivos en el hilo principal de la interfaz.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.02 — Asynchronous programming

La programación asíncrona permite iniciar operaciones y continuar mientras se espera resultado. En JavaScript se expresa con callbacks, Promises y async/await; no implica que todo trabajo se ejecute en paralelo.

**Ejemplo técnico:** Una petición fetch devuelve Promise y la interfaz puede seguir respondiendo mientras espera.

**Práctica guiada:** Compara una espera bloqueante simulada con una Promise.

**Actividad independiente:** Diseña carga de datos con estado loading/error/success.

**Criterios de aceptación:** La interfaz mantiene respuesta y gestiona todos los estados.

**Errores frecuentes:** Confundir asíncrono con paralelo o no manejar rechazo.

**Comprobación:** ¿Qué diferencia existe entre concurrencia asíncrona y paralelismo?

**Laboratorio de profundización — Modelo de operaciones no bloqueantes.**

1. Compara setTimeout, fetch y lectura asíncrona. 2. Dibuja hilo principal y tarea pendiente. 3. Identifica cuándo continúa el programa. 4. Maneja estado de carga y error.

**Evidencia esperada.** El flujo distingue inicio de operación y finalización y la interfaz permanece utilizable.

**Seguridad y límites.** No asumir que asincronía significa paralelismo ni ignorar cancelación y errores.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.03 — Callbacks

Un callback es una función pasada para ejecutarse después o durante otra operación. Puede expresar eventos y resultados asíncronos, pero anidamiento excesivo complica flujo y errores; Promises suelen mejorar composición.

**Ejemplo técnico:** setTimeout(callback, 0) agenda callback en una tarea posterior, no ejecuta inmediatamente.

**Práctica guiada:** Crea callback de éxito/error para operación simulada.

**Actividad independiente:** Refactoriza callbacks anidados a funciones pequeñas o Promise.

**Criterios de aceptación:** Orden de ejecución y errores documentados.

**Errores frecuentes:** No pasar función sino resultado de ejecutarla o perder contexto this.

**Comprobación:** ¿Por qué el callback de setTimeout no se ejecuta en la misma línea?

**Laboratorio de profundización — Callbacks y control de flujo.**

1. Implementa callback de éxito y error. 2. Compara callback síncrono y asíncrono. 3. Refactoriza anidamiento profundo. 4. Documenta contrato y orden de invocación.

**Evidencia esperada.** El callback tiene contrato claro y se evita invocarlo más de una vez accidentalmente.

**Seguridad y límites.** No ejecutar callbacks de terceros sin controlar errores y no confiar en callbacks para garantizar orden no documentado.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.04 — Promises

Una Promise representa resultado futuro: pending, fulfilled o rejected. then/catch/finally componen flujo; cada then devuelve otra Promise y los errores se propagan por la cadena hasta manejarse.

**Ejemplo técnico:** Promise.resolve(valor).then(transformar).catch(manejar).

**Práctica guiada:** Encadena dos transformaciones y fuerza rechazo controlado.

**Actividad independiente:** Implementa carga de datos con propagación y manejo central de errores.

**Criterios de aceptación:** Cada rama termina en resultado o error manejado.

**Errores frecuentes:** Olvidar return dentro de then o crear promesas que nunca se resuelven.

**Comprobación:** ¿Qué valor devuelve un then y cómo afecta a la cadena?

**Laboratorio de profundización — Estados y composición de promesas.**

1. Crea Promise resuelta y rechazada. 2. Encadena then/catch/finally. 3. Compara Promise.all, allSettled, race y any. 4. Maneja rechazo no capturado.

**Evidencia esperada.** El flujo maneja fulfillment y rejection y explica el resultado de cada combinador.

**Seguridad y límites.** No dejar promesas rechazadas sin manejo ni asumir que Promise.all cancela tareas restantes.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.05 — Async/Await

async declara una función que devuelve Promise; await pausa la continuación de esa función hasta que la Promise se resuelve o rechaza, sin bloquear el hilo principal. try/catch maneja rechazos y la secuencia debe paralelizarse conscientemente.

**Ejemplo técnico:** await Promise.all([cargarA(), cargarB()]) espera operaciones concurrentes.

**Práctica guiada:** Convierte cadena then/catch a async/await y compara manejo de error.

**Actividad independiente:** Implementa dos cargas independientes en paralelo y una dependiente en secuencia.

**Criterios de aceptación:** Errores capturados y paralelismo usado solo cuando es seguro.

**Errores frecuentes:** Esperar secuencialmente tareas independientes o olvidar await en operaciones críticas.

**Comprobación:** ¿Cuándo conviene Promise.all en lugar de varios await secuenciales?

**Laboratorio de profundización — Manejo secuencial de tareas asíncronas.**

1. Convierte cadena de promesas a async/await. 2. Añade try/catch/finally. 3. Compara await secuencial con Promise.all. 4. Propaga errores al llamador.

**Evidencia esperada.** El código mantiene semántica y ejecuta en paralelo solo tareas independientes.

**Seguridad y límites.** No usar await secuencialmente cuando las operaciones pueden ejecutarse concurrentemente ni olvidar manejo de cancelación.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.06 — Event Loop

El event loop coordina ejecución de stack, tareas y microtareas. El código síncrono actual termina antes de que se procese la cola; las microtareas suelen drenarse antes de la siguiente tarea de temporizador o interacción.

**Ejemplo técnico:** Promise.then se ejecuta como microtarea; setTimeout callback como tarea.

**Práctica guiada:** Predice orden de logs mezclando código síncrono, Promise y timer.

**Actividad independiente:** Explica una traza y cómo evitar bloquear el event loop.

**Criterios de aceptación:** Orden predicho coincide con reglas de cola.

**Errores frecuentes:** Afirmar que setTimeout(0) se ejecuta inmediatamente.

**Comprobación:** ¿Por qué una microtarea puede ejecutarse antes que un timer?

**Laboratorio de profundización — Orden de ejecución y colas.**

1. Combina código síncrono, setTimeout y Promise.resolve. 2. Predice orden de logs. 3. Distingue call stack, task queue y microtask queue. 4. Verifica salida en runtime objetivo.

**Evidencia esperada.** La predicción explica vaciado de microtasks y ejecución de tareas.

**Seguridad y límites.** No asumir tiempos exactos de timers ni usar temporizadores como reloj de precisión.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.07 — Microtasks

Microtasks incluyen callbacks de Promise y queueMicrotask. Se procesan en puntos definidos del event loop, habitualmente tras vaciar la pila actual y antes de la siguiente tarea; crear microtareas infinitamente puede retrasar renderizado.

**Ejemplo técnico:** queueMicrotask(() => ...) agenda microtarea después del código síncrono actual.

**Práctica guiada:** Compara Promise.then, queueMicrotask y setTimeout.

**Actividad independiente:** Diagnostica una secuencia que posterga renderizado por exceso de microtareas.

**Criterios de aceptación:** Se explica cola y orden sin confundirlo con ejecución paralela.

**Errores frecuentes:** Crear cadena infinita de microtareas o pensar que toda callback es microtarea.

**Comprobación:** ¿Qué riesgo produce programar microtareas continuamente?

**Laboratorio de profundización — Prioridad de microtasks.**

1. Compara queueMicrotask y callbacks de Promise con setTimeout. 2. Registra orden de ejecución. 3. Explica cuándo se vacía la cola. 4. Identifica riesgo de encadenamiento infinito.

**Evidencia esperada.** El orden se explica por el modelo de event loop y se evita starvation.

**Seguridad y límites.** No generar cadenas infinitas de microtasks que bloqueen renderizado.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.08 — Macrotasks

Macrotask o task describe tareas del event loop como timers, eventos y ciertos callbacks de I/O; la terminología exacta depende del modelo del runtime. Entre tareas pueden procesarse microtareas y renderizado.

**Ejemplo técnico:** setTimeout y evento click se procesan como tareas en el navegador.

**Práctica guiada:** Ordena logs de click, timer y Promise en un ejemplo.

**Actividad independiente:** Construye demostración visual de cola de tareas y microtareas.

**Criterios de aceptación:** Diferencia task de microtask y reconoce puntos de renderizado.

**Errores frecuentes:** Usar macrotask y microtask como categorías idénticas en todos los runtimes.

**Comprobación:** ¿Qué suele ocurrir con microtareas antes de iniciar la siguiente task?

**Laboratorio de profundización — Tareas y renderizado.**

1. Compara setTimeout, eventos y tareas del navegador. 2. Observa renderizado con tareas largas. 3. Divide trabajo usando requestAnimationFrame o scheduler cuando proceda. 4. Explica límites de timers.

**Evidencia esperada.** El estudiante identifica tareas que bloquean frames y selecciona mecanismo apropiado.

**Seguridad y límites.** No depender de delay exacto de setTimeout para sincronización crítica.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.09 — Error handling

El manejo de errores asíncronos requiere capturar excepciones, rechazos y fallos de red, distinguir errores recuperables y presentar mensajes útiles. AbortController permite cancelar fetch; los errores no deben revelar tokens ni detalles internos.

**Ejemplo técnico:** try/catch alrededor de await fetch y comprobación de response.ok.

**Práctica guiada:** Simula rechazo, HTTP 404 y cancelación con AbortController.

**Actividad independiente:** Diseña política de reintento limitado y feedback de error.

**Criterios de aceptación:** Cada fallo se distingue y la interfaz permite recuperación segura.

**Errores frecuentes:** Asumir que fetch rechaza por 404 o reintentar indefinidamente.

**Comprobación:** ¿Por qué fetch no rechaza automáticamente ante una respuesta HTTP 404?

**Laboratorio de profundización — Errores síncronos y asíncronos.**

1. Maneja throw/catch en función síncrona. 2. Maneja rechazo de promesa y excepción en async. 3. Añade contexto sin filtrar secretos. 4. Define errores recuperables y no recuperables.

**Evidencia esperada.** Los errores se capturan en el límite adecuado y se conserva causa/contexto útil.

**Seguridad y límites.** No exponer stack traces o datos sensibles al usuario final.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.

#### 12.3.10 — Race conditions

Una race condition aparece cuando el resultado depende del orden temporal de operaciones concurrentes. En UI, una respuesta antigua puede llegar después de una nueva y sobrescribir estado; se controla con cancelación, identificadores de petición o comparación de versión.

**Ejemplo técnico:** Dos búsquedas con distinto texto terminan fuera de orden y la primera pisa el resultado más reciente.

**Práctica guiada:** Simula respuestas con retrasos diferentes y observa orden de llegada.

**Actividad independiente:** Implementa búsqueda que ignore respuestas obsoletas o aborte petición previa.

**Criterios de aceptación:** Solo la respuesta correspondiente al estado actual modifica UI.

**Errores frecuentes:** Asumir que las respuestas llegan en el mismo orden que las solicitudes.

**Comprobación:** ¿Cómo evitas que una respuesta antigua sobrescriba resultados recientes?


**Laboratorio de profundización — Control de concurrencia lógica.**

1. Simula dos solicitudes que actualizan el mismo estado con distinta latencia. 2. Observa resultado fuera de orden. 3. Aplica AbortController, identificador de solicitud o actualización funcional. 4. Prueba orden rápido/lento.

**Evidencia esperada.** La solución evita que una respuesta obsoleta sobrescriba el estado más reciente.

**Seguridad y límites.** No asumir que el orden de finalización coincide con el de inicio; cancelar o ignorar respuestas obsoletas.

**Registro sugerido.** Conserva ejemplo mínimo, navegador/runtime y versión, orden observado, casos de error y resultado. No marques la práctica como ejecutada sin evidencia real.
#### 12.4.01 — Fetch API

Fetch API realiza solicitudes HTTP y devuelve Promise de Response. Debe comprobarse response.ok, parsear cuerpo según formato y manejar abortos, errores de red y políticas CORS. Un HTTP 4xx/5xx no rechaza automáticamente la Promise.

**Ejemplo técnico:** fetch(url).then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })

**Práctica guiada:** Consulta endpoint público de prueba y registra status y tipo de contenido.

**Actividad independiente:** Implementa cliente API con timeout/cancelación y errores tipados.

**Criterios de aceptación:** Estados HTTP y errores de red se distinguen.

**Errores frecuentes:** Asumir que 404 provoca rechazo o desactivar CORS como solución.

**Comprobación:** ¿Qué comprueba response.ok?

**Laboratorio de profundización — Consumo HTTP con fetch.**

1. Consulta un endpoint de prueba autorizado. 2. Comprueba response.ok y status. 3. Maneja JSON inválido, timeout y error de red. 4. Usa AbortController para cancelar una solicitud.

**Evidencia esperada.** El código diferencia error de red de respuesta HTTP no exitosa y valida el contenido antes de usarlo.

**Seguridad y límites.** No incluir tokens en URL ni desactivar controles CORS; CORS no sustituye autorización del servidor.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.4.02 — LocalStorage

localStorage conserva pares clave-valor de texto por origen y persiste entre sesiones. No es almacén seguro para tokens sensibles; puede ser leído por JavaScript del mismo origen y queda expuesto ante XSS. El acceso puede fallar por políticas del navegador.

**Ejemplo técnico:** setItem/getItem almacenan cadenas; JSON.stringify/parse serializan objetos.

**Práctica guiada:** Guarda preferencia ficticia y verifica persistencia y manejo de JSON inválido.

**Actividad independiente:** Implementa preferencia no sensible con versión de esquema.

**Criterios de aceptación:** Datos no sensibles, validación y manejo de cuota/error.

**Errores frecuentes:** Guardar contraseñas o tokens de sesión en localStorage.

**Comprobación:** ¿Qué amenaza expone tokens guardados en localStorage ante XSS?

**Laboratorio de profundización — Persistencia local y validación.**

1. Guarda preferencia no sensible en localStorage. 2. Lee y parsea el valor con manejo de JSON inválido. 3. Define versión de esquema y migración simple. 4. Elimina el valor al restablecer preferencias.

**Evidencia esperada.** La aplicación maneja ausencia, corrupción y evolución del dato local.

**Seguridad y límites.** No guardar contraseñas, tokens de sesión o datos sensibles en localStorage.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.4.03 — SessionStorage

sessionStorage mantiene datos por origen y contexto de pestaña, normalmente durante la sesión de esa pestaña. No es un mecanismo de seguridad ni un canal de sincronización entre pestañas.

**Ejemplo técnico:** setItem guarda estado temporal que desaparece al cerrar la pestaña/contexto según comportamiento del navegador.

**Práctica guiada:** Compara localStorage y sessionStorage en dos pestañas.

**Actividad independiente:** Guarda un estado temporal de formulario no sensible.

**Criterios de aceptación:** Alcance y ciclo de vida documentados.

**Errores frecuentes:** Asumir que sessionStorage cifra o que sustituye gestión de sesión del servidor.

**Comprobación:** ¿Qué diferencia de ciclo de vida tiene respecto a localStorage?

**Laboratorio de profundización — Alcance de almacenamiento por pestaña.**

1. Guarda estado temporal de un flujo. 2. Abre nueva pestaña y compara comportamiento. 3. Prueba recarga y cierre de pestaña. 4. Define qué datos deben descartarse al terminar.

**Evidencia esperada.** Se explica alcance por contexto de pestaña y diferencia con localStorage.

**Seguridad y límites.** No utilizar sessionStorage como garantía de confidencialidad ni guardar secretos.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.4.04 — Cookies

Las cookies se envían automáticamente según dominio, path, SameSite y Secure. HttpOnly impide lectura desde JavaScript; Secure limita envío a HTTPS; SameSite ayuda frente a CSRF pero requiere diseño. Las cookies no deben almacenar secretos innecesarios y necesitan expiración y protección adecuadas.

**Ejemplo técnico:** Cookie de sesión con Secure, HttpOnly, SameSite y expiración configurada por servidor.

**Práctica guiada:** Inspecciona cookies de un entorno de prueba y explica atributos sin copiar valores.

**Actividad independiente:** Diseña cookie de sesión segura y flujo de rotación/revocación.

**Criterios de aceptación:** Atributos y alcance corresponden al modelo de amenaza.

**Errores frecuentes:** Creer que HttpOnly evita CSRF o guardar JWT sensible sin estrategia.

**Comprobación:** ¿Qué amenaza mitiga HttpOnly y cuál no?

**Laboratorio de profundización — Atributos y ciclo de vida de cookies.**

1. Inspecciona cookies de un sitio de laboratorio propio. 2. Identifica Domain, Path, Expires/Max-Age, Secure, HttpOnly y SameSite. 3. Diseña cookie de sesión segura desde servidor. 4. Explica CSRF y alcance de SameSite.

**Evidencia esperada.** Se identifica qué atributos controla cliente y cuáles deben establecerse desde servidor.

**Seguridad y límites.** No crear cookies de autenticación accesibles a JavaScript ni exponer datos sensibles en valores.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.4.05 — Geolocation

Geolocation API solicita permiso explícito y devuelve ubicación bajo políticas de seguridad del navegador. Es dato sensible; debe pedirse solo cuando sea necesario, explicar finalidad y minimizar precisión/retención. HTTPS suele ser requisito de contexto seguro.

**Ejemplo técnico:** navigator.geolocation.getCurrentPosition requiere permiso y puede fallar por rechazo o timeout.

**Práctica guiada:** Prueba flujo con ubicación simulada, no publiques coordenadas reales.

**Actividad independiente:** Diseña función con permiso, alternativa manual y política de retención.

**Criterios de aceptación:** No se solicita hasta que el usuario inicia acción y existe alternativa.

**Errores frecuentes:** Solicitar ubicación al cargar página o registrar coordenadas sin necesidad.

**Comprobación:** ¿Por qué debe existir una alternativa si el usuario deniega ubicación?

**Laboratorio de profundización — Permisos y uso responsable de ubicación.**

1. Implementa solicitud de geolocalización tras acción explícita del usuario. 2. Maneja permiso denegado, timeout y posición no disponible. 3. Explica precisión y vigencia. 4. Define retención mínima.

**Evidencia esperada.** La función solicita permiso en contexto y maneja fallos sin bloquear la aplicación.

**Seguridad y límites.** No recopilar ubicación sin consentimiento ni almacenar coordenadas más tiempo del necesario.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.4.06 — Clipboard

Clipboard API permite leer/escribir portapapeles bajo contexto seguro y restricciones de permiso/gesto de usuario. Copiar datos sensibles puede exponerlos a otras aplicaciones; la interfaz debe indicar qué se copia y evitar lecturas inesperadas.

**Ejemplo técnico:** navigator.clipboard.writeText requiere condiciones del navegador y suele necesitar interacción del usuario.

**Práctica guiada:** Implementa botón copiar para texto de prueba y maneja rechazo de permiso.

**Actividad independiente:** Añade feedback accesible y evita copiar secretos por defecto.

**Criterios de aceptación:** Acción explícita, feedback y fallback razonable.

**Errores frecuentes:** Leer portapapeles sin contexto o asumir que API siempre está disponible.

**Comprobación:** ¿Por qué la copia al portapapeles debe ser una acción explícita?

**Laboratorio de profundización — Acceso seguro al portapapeles.**

1. Implementa copia de texto tras interacción del usuario. 2. Maneja rechazo de permisos y contexto seguro. 3. Proporciona confirmación accesible. 4. Prueba alternativa manual.

**Evidencia esperada.** La acción tiene fallback y no depende de permiso siempre concedido.

**Seguridad y límites.** No leer portapapeles sin acción clara ni copiar secretos a portapapeles compartido.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.4.07 — File API

File API permite seleccionar, leer y procesar archivos mediante input file, File, Blob y FileReader/streams. El nombre, MIME type y extensión enviados por el cliente no prueban contenido seguro; servidor debe validar tipo real, tamaño, autorización y almacenamiento.

**Ejemplo técnico:** input type=file expone File; el cliente puede leer texto, pero no debe confiar en MIME declarado.

**Práctica guiada:** Selecciona archivo sintético y muestra nombre/tamaño sin subirlo.

**Actividad independiente:** Diseña carga con límite, validación de servidor y almacenamiento fuera de rutas ejecutables.

**Criterios de aceptación:** Tipos, tamaño y errores manejados; el servidor revalida.

**Errores frecuentes:** Confiar en extensión o MIME del cliente o cargar archivos sin límites.

**Comprobación:** ¿Por qué el servidor debe inspeccionar el contenido del archivo y no confiar solo en su extensión?

**Laboratorio de profundización — Lectura segura de archivos del usuario.**

1. Permite seleccionar archivo con input file. 2. Inspecciona name, type y size. 3. Lee texto de un archivo sintético. 4. Valida contenido en servidor si se sube.

**Evidencia esperada.** La aplicación limita tamaño y tipo esperado y no confía solo en extensión o MIME del cliente.

**Seguridad y límites.** No ejecutar archivos seleccionados ni confiar en validación de tipo del navegador como protección suficiente.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.01 — Tipos

TypeScript añade análisis estático de tipos a JavaScript y se transpila/elimina anotaciones para generar JavaScript. Los tipos se verifican en compilación y no validan automáticamente datos externos en runtime.

**Ejemplo técnico:** `let edad: number = 30` restringe asignaciones durante comprobación.

**Práctica guiada:** Declara tipos primitivos y prueba asignaciones incompatibles.

**Actividad independiente:** Tipa un modelo de datos de dominio.

**Criterios de aceptación:** El tipo refleja semántica y el compilador detecta errores previstos.

**Errores frecuentes:** Creer que TypeScript valida JSON recibido en runtime.

**Comprobación:** ¿Qué diferencia existe entre chequeo estático y validación en ejecución?

**Laboratorio de profundización — Tipado estático y tipos primitivos.**

1. Define tipos string, number, boolean, arrays y objetos. 2. Compara any, unknown y never. 3. Activa strict. 4. Corrige errores sin convertir todo a any.

**Evidencia esperada.** El código expresa contratos y utiliza unknown para datos no validados.

**Seguridad y límites.** Los tipos desaparecen en runtime; validar datos externos durante ejecución.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.02 — Interfaces

Una interface describe forma de objetos y contratos estructurales; puede extenderse y fusionarse según reglas del lenguaje. TypeScript utiliza tipado estructural, por lo que compatibilidad depende de miembros y no de nombre de tipo.

**Ejemplo técnico:** interface Usuario { id: string; activo: boolean }

**Práctica guiada:** Define interface y comprueba objeto compatible e incompatible.

**Actividad independiente:** Modela DTO de usuario y respuesta de API.

**Criterios de aceptación:** Campos requeridos/opcionales explícitos.

**Errores frecuentes:** Usar interface como si validara datos externos en runtime.

**Comprobación:** ¿Qué significa que TypeScript tenga tipado estructural?

**Laboratorio de profundización — Contratos estructurales con interfaces.**

1. Define interfaz Usuario y Pedido. 2. Implementa objetos compatibles. 3. Compara propiedades opcionales y readonly. 4. Extiende interfaces con responsabilidad clara.

**Evidencia esperada.** Los contratos describen forma de objetos y detectan incompatibilidades estáticas.

**Seguridad y límites.** No utilizar interfaz como sustituto de validación runtime de JSON externo.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.03 — Type aliases

type crea alias para tipos, uniones, intersecciones, tuplas y tipos utilitarios. No crea una clase ni estructura runtime; es una construcción del sistema de tipos.

**Ejemplo técnico:** type Estado = 'nuevo' | 'activo' | 'cerrado'

**Práctica guiada:** Define alias para estado y unión discriminada.

**Actividad independiente:** Modela resultado de operación como éxito/error.

**Criterios de aceptación:** Casos cubiertos sin valores ambiguos.

**Errores frecuentes:** Esperar que alias exista en JavaScript generado.

**Comprobación:** ¿Qué diferencia un alias de tipo de una clase en runtime?

**Laboratorio de profundización — Alias y uniones discriminadas.**

1. Define alias para identificadores y estados. 2. Construye union discriminada. 3. Compara alias con interface. 4. Usa exhaustividad con never.

**Evidencia esperada.** El alias mejora legibilidad y la unión discriminada permite manejar todos los casos.

**Seguridad y límites.** No crear alias nominales aparentes si TypeScript mantiene compatibilidad estructural.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.04 — Union types

Una unión `A | B` permite que un valor sea uno de varios tipos. El código debe estrechar el tipo antes de acceder a miembros exclusivos; discriminantes literales facilitan exhaustividad.

**Ejemplo técnico:** type Resultado = {ok:true; dato:string} | {ok:false; error:string}

**Práctica guiada:** Construye unión discriminada y usa switch para estrechar.

**Actividad independiente:** Modela estados de carga y error.

**Criterios de aceptación:** Todas las variantes se manejan explícitamente.

**Errores frecuentes:** Acceder a propiedad que no existe en todas las variantes.

**Comprobación:** ¿Qué aporta un discriminante literal a una unión?

**Laboratorio de profundización — Narrowing de tipos unidos.**

1. Define función que reciba string | number. 2. Usa typeof para estrechar. 3. Maneja null y undefined. 4. Añade caso no alcanzable.

**Evidencia esperada.** Cada rama utiliza operaciones válidas para el tipo estrechado.

**Seguridad y límites.** No forzar casts para silenciar errores de diseño.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.05 — Intersection types

Una intersección `A & B` combina requisitos de tipos; el valor debe cumplir ambos. Puede expresar composición, pero intersecciones incompatibles pueden producir tipos imposibles o confusos.

**Ejemplo técnico:** type ConAuditoria = Entidad & {creadoEn: Date}

**Práctica guiada:** Combina dos tipos y analiza colisiones de propiedades.

**Actividad independiente:** Compón tipos de dominio sin duplicar contratos.

**Criterios de aceptación:** Propiedades compatibles y semántica clara.

**Errores frecuentes:** Usar intersección para modelar alternativas excluyentes.

**Comprobación:** ¿Por qué A & B no significa lo mismo que A | B?

**Laboratorio de profundización — Composición de capacidades.**

1. Combina tipos Identificable y ConMarcaTemporal. 2. Define objeto que satisfaga ambos. 3. Analiza conflictos de propiedades con tipos incompatibles. 4. Compara intersección con herencia.

**Evidencia esperada.** La intersección representa composición de contratos sin duplicar campos incoherentes.

**Seguridad y límites.** No crear intersecciones imposibles que produzcan never sin detectar conflicto.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.06 — Generics

Los genéricos parametrizan tipos y permiten reutilizar funciones/estructuras preservando relaciones entre entradas y salidas. Las restricciones `extends` limitan operaciones válidas.

**Ejemplo técnico:** function primero<T>(items:T[]):T|undefined conserva tipo del elemento.

**Práctica guiada:** Implementa función genérica y prueba con string/número.

**Actividad independiente:** Diseña wrapper de resultado genérico con manejo de error.

**Criterios de aceptación:** Tipo se infiere sin perder información.

**Errores frecuentes:** Usar any en lugar de genérico o restringir innecesariamente T.

**Comprobación:** ¿Qué información conserva un genérico que any descarta?

**Laboratorio de profundización — Funciones y estructuras genéricas.**

1. Implementa función identity<T>. 2. Crea contenedor genérico con restricciones extends. 3. Preserva tipo de retorno. 4. Compara con any.

**Evidencia esperada.** El tipo genérico conserva información y evita perder seguridad estática.

**Seguridad y límites.** No introducir genéricos sin necesidad ni restringir tipos más de lo que exige el contrato.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.07 — Type narrowing

Narrowing reduce un tipo unión mediante typeof, instanceof, in, discriminantes, guards y control de flujo. La comprobación debe reflejar evidencia real y cubrir null/undefined.

**Ejemplo técnico:** if (typeof valor === 'string') habilita métodos de cadena.

**Práctica guiada:** Implementa guards para unión y valor desconocido.

**Actividad independiente:** Valida entrada unknown antes de transformarla.

**Criterios de aceptación:** No hay casts sin evidencia ni ramas sin cubrir.

**Errores frecuentes:** Usar `as` para silenciar errores sin validar.

**Comprobación:** ¿Por qué unknown es más seguro que any para datos externos?

**Laboratorio de profundización — Guardas y discriminación.**

1. Utiliza typeof, in, instanceof y predicados de tipo. 2. Valida una unión de eventos. 3. Maneja null. 4. Escribe type guard reutilizable.

**Evidencia esperada.** El compilador reconoce el tipo tras cada comprobación y no se usa dato antes de validar.

**Seguridad y límites.** No declarar type guard que afirme condiciones que no comprueba realmente.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.08 — Utility types

Utility types transforman tipos existentes: Partial, Required, Pick, Omit, Readonly, Record, ReturnType y otros. Facilitan derivar DTOs y contratos, pero deben conservar intención semántica.

**Ejemplo técnico:** Pick<Usuario,'id'|'nombre'> crea vista tipada limitada.

**Práctica guiada:** Deriva tipos de actualización y lectura desde una entidad.

**Actividad independiente:** Diseña DTO parcial sin exponer campos internos.

**Criterios de aceptación:** Campos permitidos y mutabilidad explícitos.

**Errores frecuentes:** Aplicar Partial a todo y perder invariantes obligatorias.

**Comprobación:** ¿Por qué un DTO de actualización no debe permitir modificar cualquier campo?

**Laboratorio de profundización — Transformación de contratos existentes.**

1. Aplica Partial, Pick, Omit, Record y Readonly a tipos de dominio. 2. Construye DTO de actualización. 3. Explica diferencia entre Partial y opcionalidad semántica. 4. Comprueba inferencia.

**Evidencia esperada.** El tipo derivado conserva el contrato esperado y reduce duplicación.

**Seguridad y límites.** No permitir actualización masiva de campos sensibles por usar Partial sin lista permitida.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.09 — Enums

enum define un conjunto de constantes con representación runtime en TypeScript; existen enums numéricos, string enums y alternativas con union literals. La elección afecta JavaScript generado y serialización.

**Ejemplo técnico:** type Estado = 'pendiente' | 'aprobado' puede ser suficiente sin enum runtime.

**Práctica guiada:** Compara enum string y unión literal en switch.

**Actividad independiente:** Selecciona representación para valores que viajan por API.

**Criterios de aceptación:** Valores serializados estables y documentados.

**Errores frecuentes:** Asumir que enum y union type se comportan igual en runtime.

**Comprobación:** ¿Qué diferencia existe entre enum y unión de literales en JavaScript generado?

**Laboratorio de profundización — Representación de conjuntos finitos.**

1. Compara enum numérico, string union y const object. 2. Evalúa salida JavaScript generada. 3. Diseña estados de pedido. 4. Comprueba serialización JSON.

**Evidencia esperada.** La representación mantiene valores estables entre frontend y API.

**Seguridad y límites.** No asumir que enum TypeScript existe en runtime como tipo puro ni aceptar valores no validados.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.10 — Type inference

Type inference permite al compilador deducir tipos desde inicializadores, contexto y retornos. Anotaciones son útiles en límites públicos, parámetros complejos y contratos, pero redundancia excesiva reduce legibilidad.

**Ejemplo técnico:** const nombre = 'Ada' infiere string; una variable let puede ampliarse según contexto.

**Práctica guiada:** Inspecciona inferencia de const/let, arrays y retornos.

**Actividad independiente:** Elimina anotaciones redundantes sin perder claridad de API.

**Criterios de aceptación:** El tipo inferido coincide con intención.

**Errores frecuentes:** Anotar cada variable o depender de inferencia demasiado amplia.

**Comprobación:** ¿Cuándo conviene anotar explícitamente un tipo?

**Laboratorio de profundización — Inferencia contextual y explícita.**

1. Observa inferencia en variables, funciones y callbacks. 2. Identifica cuándo la anotación mejora claridad. 3. Evita anotaciones redundantes. 4. Revisa tipo inferido en IDE/compilador.

**Evidencia esperada.** La inferencia reduce ruido sin ocultar contratos importantes.

**Seguridad y límites.** No depender de inferencia amplia cuando el límite público requiere tipo explícito.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.

#### 12.5.11 — Strict mode

El modo strict de TypeScript habilita un conjunto de comprobaciones más rigurosas, como strictNullChecks y noImplicitAny. Configuración exacta depende de tsconfig y versión; activar strict puede revelar defectos que deben corregirse, no silenciarse.

**Ejemplo técnico:** strictNullChecks obliga a tratar null/undefined antes de usar valor.

**Práctica guiada:** Activa strict en proyecto de laboratorio y resuelve errores de nulabilidad.

**Actividad independiente:** Define tsconfig reproducible para aplicación.

**Criterios de aceptación:** Compilación estricta sin any/casts injustificados.

**Errores frecuentes:** Desactivar strict para ocultar errores o añadir non-null assertion indiscriminadamente.

**Comprobación:** ¿Qué clase de errores detecta strictNullChecks?


**Laboratorio de profundización — Configuración estricta del compilador.**

1. Activa strict en tsconfig. 2. Revisa strictNullChecks y noImplicitAny. 3. Corrige errores de entrada y retorno. 4. Define política de migración incremental.

**Evidencia esperada.** La compilación identifica riesgos de nulabilidad y tipos implícitos y el proyecto documenta excepciones.

**Seguridad y límites.** No desactivar strict globalmente para ocultar errores sin registrar deuda técnica.

**Registro sugerido.** Registra versión de navegador/Node y TypeScript, tsconfig, datos sintéticos, pruebas de tipos y comportamiento runtime. No marques la práctica como ejecutada sin evidencia real.
#### 12.6.01 — Components

Los componentes React encapsulan UI reutilizable como funciones que reciben props y devuelven elementos React. Deben ser predecibles, con responsabilidades claras y composición antes que jerarquías profundas.

**Ejemplo técnico:** function Saludo({nombre}) { return <p>Hola, {nombre}</p>; }

**Práctica guiada:** Crea componente funcional y renderízalo con dos props distintas.

**Actividad independiente:** Divide una página en componentes de responsabilidad única.

**Criterios de aceptación:** Props explícitas y salida determinista para mismos datos/estado.

**Errores frecuentes:** Componentes monolíticos o mutar props.

**Comprobación:** ¿Por qué un componente no debe modificar sus props?

#### 12.6.02 — JSX

JSX es una sintaxis que se transforma en llamadas/estructuras React; permite expresiones JavaScript dentro de marcado. Reglas como un solo nodo raíz, className y escape automático aplican; dangerouslySetInnerHTML requiere control estricto.

**Ejemplo técnico:** `<h1>{titulo}</h1>` interpola expresión y escapa texto.

**Práctica guiada:** Convierte fragmento HTML a JSX y resuelve atributos/expresiones.

**Actividad independiente:** Crea vista que muestra datos dinámicos seguros.

**Criterios de aceptación:** JSX válido y datos no confiables renderizados como texto.

**Errores frecuentes:** Insertar HTML no confiable con dangerouslySetInnerHTML.

**Comprobación:** ¿Qué protección ofrece el escape automático de JSX?

#### 12.6.03 — Props

Props son entradas de solo lectura para un componente. Deben tiparse y tener valores por defecto cuando corresponda; callbacks permiten comunicar eventos hacia arriba.

**Ejemplo técnico:** <Tarjeta titulo="Curso" activo={true}/>

**Práctica guiada:** Pasa props de tipos distintos y prueba ausencia/valor por defecto.

**Actividad independiente:** Diseña API de componente sin estado duplicado.

**Criterios de aceptación:** Contrato claro y sin mutación de props.

**Errores frecuentes:** Usar props como almacenamiento mutable interno.

**Comprobación:** ¿Qué patrón permite que un hijo notifique una acción al padre?

#### 12.6.04 — State

State representa datos que cambian con el tiempo y afectan renderizado. En React se actualiza mediante setter; las actualizaciones pueden agruparse y dependen del valor previo. No se mutan objetos/arrays de estado directamente.

**Ejemplo técnico:** setCount(prev => prev + 1) evita depender de cierre obsoleto.

**Práctica guiada:** Crea contador y actualiza usando forma funcional.

**Actividad independiente:** Implementa formulario controlado con estado inmutable.

**Criterios de aceptación:** UI refleja estado actualizado y no hay mutaciones directas.

**Errores frecuentes:** Modificar objeto state directamente o usar valor obsoleto en actualización concurrente.

**Comprobación:** ¿Por qué la forma funcional es útil cuando el nuevo estado depende del anterior?

#### 12.6.05 — Hooks

Hooks permiten usar estado, efectos y otras capacidades en componentes funcionales. Deben llamarse en nivel superior de componente o custom hook y conservar orden entre renderizados. No deben ejecutarse condicionalmente ni dentro de bucles.

**Ejemplo técnico:** useState al inicio del componente conserva orden de hooks.

**Práctica guiada:** Identifica usos válidos e inválidos en fragmentos.

**Actividad independiente:** Extrae lógica repetida en custom hook.

**Criterios de aceptación:** Reglas de hooks respetadas y dependencias justificadas.

**Errores frecuentes:** Llamar hooks dentro de if, callback o bucle.

**Comprobación:** ¿Por qué React exige el mismo orden de hooks en cada render?

#### 12.6.06 — useState

useState devuelve valor actual y setter. El setter solicita nuevo render; no modifica variable local inmediatamente. Para estado derivado del anterior se usa updater funcional; inicializadores costosos pueden ser funciones.

**Ejemplo técnico:** const [items,setItems]=useState([]); setItems(prev=>[...prev,nuevo]);

**Práctica guiada:** Implementa lista con alta y eliminación inmutable.

**Actividad independiente:** Gestiona estado complejo sin mutar arrays.

**Criterios de aceptación:** Actualizaciones inmutables y UI sincronizada.

**Errores frecuentes:** Esperar cambio inmediato en variable local o mutar array con push.

**Comprobación:** ¿Por qué setState no cambia inmediatamente la variable capturada en el render actual?

#### 12.6.07 — useEffect

useEffect sincroniza componente con sistemas externos: suscripciones, timers o conexiones. Dependencias deben reflejar valores usados; cleanup desuscribe o cancela. No debe usarse para calcular datos derivados que pueden calcularse durante render.

**Ejemplo técnico:** Effect que suscribe evento y retorna cleanup para removerlo.

**Práctica guiada:** Implementa suscripción y comprueba montaje/desmontaje.

**Actividad independiente:** Carga datos con cancelación y manejo de carrera.

**Criterios de aceptación:** Dependencias correctas y cleanup evita fugas/actualizaciones obsoletas.

**Errores frecuentes:** Usar effect para derivar estado o ignorar cleanup.

**Comprobación:** ¿Qué problema resuelve la función cleanup?

#### 12.6.08 — useContext

useContext lee valor del proveedor más cercano y permite compartir datos entre componentes sin pasar props por muchos niveles. Cambios de contexto pueden volver a renderizar consumidores; dividir contextos reduce actualizaciones innecesarias.

**Ejemplo técnico:** Contexto de tema expone theme y toggleTheme.

**Práctica guiada:** Crea Provider y consume valor en componente descendiente.

**Actividad independiente:** Separa contexto de datos y contexto de acciones si sus cambios difieren.

**Criterios de aceptación:** Provider cubre consumidores y valor estable.

**Errores frecuentes:** Usar context para todo el estado global o consumir fuera de Provider sin fallback.

**Comprobación:** ¿Qué sucede si un consumidor no encuentra Provider?

#### 12.6.09 — useRef

useRef conserva objeto mutable entre renders sin provocar nuevo render al cambiar current. Se usa para referencias DOM o valores persistentes no visuales; no sustituye state cuando el valor debe actualizar UI.

**Ejemplo técnico:** ref.current almacena referencia a input y permite focus().

**Práctica guiada:** Enfoca input con ref y compara con estado.

**Actividad independiente:** Guarda ID de timer sin renderizar por cada cambio.

**Criterios de aceptación:** Ref estable y uso coherente con render.

**Errores frecuentes:** Usar ref para datos visuales que deberían ser state.

**Comprobación:** ¿Por qué cambiar ref.current no provoca render?

#### 12.6.10 — Forms

React puede controlar formularios mediante value/onChange o permitir lectura nativa al submit. Los campos controlados deben mantener valor sincronizado y asociar etiquetas/errores; la validación del servidor sigue siendo autoritativa.

**Ejemplo técnico:** value={email} onChange={e=>setEmail(e.target.value)}

**Práctica guiada:** Implementa formulario controlado y evita cambiar entre controlado/no controlado.

**Actividad independiente:** Construye formulario accesible con estado de envío y error.

**Criterios de aceptación:** Valores, etiquetas y errores sincronizados.

**Errores frecuentes:** Input controlado sin onChange o validación solo cliente.

**Comprobación:** ¿Qué diferencia existe entre controlado y no controlado?

#### 12.6.11 — Routing

El routing del cliente asocia rutas URL con vistas y navegación sin recarga completa. Debe gestionar rutas desconocidas, parámetros, query strings, navegación accesible e historial; autenticación y autorización no deben depender solo de ocultar rutas.

**Ejemplo técnico:** Ruta /cursos/:id extrae parámetro id y carga recurso autorizado.

**Práctica guiada:** Define rutas, navegación y fallback 404.

**Actividad independiente:** Protege vistas y valida permisos también en servidor/API.

**Criterios de aceptación:** URL y vista coherentes; rutas desconocidas manejadas.

**Errores frecuentes:** Confiar en guard de frontend como control de acceso.

**Comprobación:** ¿Por qué una ruta oculta no protege el recurso del servidor?

#### 12.6.12 — Context API

Context API permite compartir valores a través del árbol. Provider define el alcance y consumidores acceden al contexto; para estado complejo puede combinarse con reducer y dividir contextos para limitar renders.

**Ejemplo técnico:** Contexto AuthProvider ofrece usuario y acciones de sesión.

**Práctica guiada:** Construye contexto tipado con valor inicial seguro.

**Actividad independiente:** Define límites de contexto y estrategia de test.

**Criterios de aceptación:** API contextual documentada y Provider en raíz apropiada.

**Errores frecuentes:** Crear contexto global monolítico que provoca renders amplios.

**Comprobación:** ¿Cuándo conviene separar un contexto de estado y otro de acciones?

#### 12.6.13 — Component lifecycle

En componentes funcionales, render, commit y efectos describen fases de actualización. Hooks reemplazan muchos patrones de lifecycle de clases; el montaje/desmontaje no debe equipararse a cada ejecución de render. Strict Mode puede repetir ciertas operaciones de desarrollo para detectar efectos no seguros.

**Ejemplo técnico:** Un componente puede renderizar varias veces antes de un commit visible.

**Práctica guiada:** Registra render y cleanup en entorno de desarrollo.

**Actividad independiente:** Asegura que efectos sean idempotentes y limpiables.

**Criterios de aceptación:** No hay dependencia de ejecutar efecto exactamente una vez en desarrollo.

**Errores frecuentes:** Usar efecto como constructor que asume ejecución única.

**Comprobación:** ¿Por qué Strict Mode puede revelar efectos con side effects no seguros?

#### 12.6.14 — State management

La gestión de estado define dónde vive cada dato, quién puede modificarlo y cómo se sincroniza. Estado local, Context, reducers y librerías externas resuelven escalas distintas; estado servidor requiere caché, invalidación y sincronización diferenciadas.

**Ejemplo técnico:** Estado de modal local; usuario autenticado compartido; datos remotos con caché/query layer.

**Práctica guiada:** Clasifica estado UI, dominio y servidor.

**Actividad independiente:** Diseña estrategia de estado para panel con filtros, sesión y datos remotos.

**Criterios de aceptación:** Cada estado tiene propietario y ciclo de vida definidos.

**Errores frecuentes:** Guardar todo en un único contexto o duplicar estado servidor en varios componentes.

**Comprobación:** ¿Por qué estado de servidor y estado de interfaz suelen requerir estrategias distintas?

#### 12.6.15 — Custom Hooks

Un custom hook encapsula lógica reutilizable que usa otros hooks y comparte estado por instancia de llamada, no crea automáticamente estado global. Su nombre comienza por use y respeta reglas de hooks.

**Ejemplo técnico:** useDebounce(value,delay) mantiene valor derivado mediante timer y cleanup.

**Práctica guiada:** Extrae lógica de listener a hook y prueba dos instancias independientes.

**Actividad independiente:** Crea hook de carga con abort/cancelación y estados explícitos.

**Criterios de aceptación:** API pequeña, cleanup y dependencias correctas.

**Errores frecuentes:** Suponer que dos componentes comparten estado solo por llamar el mismo hook.

**Comprobación:** ¿Qué diferencia existe entre reutilizar lógica con custom hook y compartir estado global?

#### 12.6.16 — Error Boundaries

Error Boundaries capturan errores de renderizado en componentes descendientes y muestran fallback; no capturan todos los errores de eventos, async callbacks ni fallos fuera del árbol. La estrategia debe registrar errores sin exponer datos sensibles.

**Ejemplo técnico:** Un boundary alrededor de panel muestra fallback si un componente hijo lanza durante render.

**Práctica guiada:** Implementa fallback de sección y prueba error controlado en desarrollo.

**Actividad independiente:** Diseña recuperación/reintento y reporte de error seguro.

**Criterios de aceptación:** Fallo aislado, mensaje comprensible y registro sin secretos.

**Errores frecuentes:** Asumir que boundary captura errores de fetch o event handlers.

**Comprobación:** ¿Qué tipos de errores no captura un Error Boundary tradicional?

#### 12.7.01 — App Router

App Router organiza rutas mediante estructura de carpetas y archivos especiales. Layouts, pages, loading, error y route handlers cumplen roles distintos; convenciones pueden variar por versión Next.js.

**Ejemplo técnico:** app/cursos/[id]/page.tsx representa ruta dinámica.

**Práctica guiada:** Identifica archivos de una app de laboratorio y dibuja árbol de rutas.

**Actividad independiente:** Crea estructura conceptual con layout y páginas anidadas.

**Criterios de aceptación:** Cada archivo cumple convención documentada para la versión.

**Errores frecuentes:** Confundir App Router con Pages Router o ubicar código client sin necesidad.

**Comprobación:** ¿Qué función cumple layout frente a page?

#### 12.7.02 — Routing

Next.js resuelve rutas estáticas y dinámicas mediante segmentos, grupos, parámetros y navegación. La estructura debe evitar rutas ambiguas y contemplar not-found, redirects y parámetros validados.

**Ejemplo técnico:** `[slug]` captura segmento dinámico; `not-found.tsx` representa ruta no encontrada.

**Práctica guiada:** Diseña árbol de rutas para catálogo y detalle.

**Actividad independiente:** Define rutas, parámetros y estados 404/redirect.

**Criterios de aceptación:** URLs previsibles y parámetros validados.

**Errores frecuentes:** Confiar en parámetros URL sin validarlos en backend.

**Comprobación:** ¿Por qué un segmento dinámico debe validarse antes de consultar datos?

#### 12.7.03 — Server Components

React Server Components permiten renderizar componentes en servidor y reducir JavaScript enviado al cliente. No acceden a APIs de navegador; pueden consultar datos en servidor y pasar props serializables a componentes cliente.

**Ejemplo técnico:** Componente servidor consulta catálogo y entrega datos a una isla interactiva cliente.

**Práctica guiada:** Clasifica componentes según necesidad de interactividad y acceso a datos.

**Actividad independiente:** Refactoriza página para mantener lectura en servidor y dejar interacción mínima en cliente.

**Criterios de aceptación:** Directiva client se limita a fronteras necesarias.

**Errores frecuentes:** Marcar toda la aplicación como client por comodidad.

**Comprobación:** ¿Qué beneficio aporta mantener un componente como Server Component?

#### 12.7.04 — Client Components

Client Components se habilitan con 'use client' y pueden usar estado, efectos y APIs del navegador. La directiva crea frontera de cliente y sus dependencias forman parte del bundle; secretos de servidor nunca deben importarse allí.

**Ejemplo técnico:** Componente de filtro interactivo utiliza useState y recibe datos serializables.

**Práctica guiada:** Identifica APIs de navegador y estado que requieren cliente.

**Actividad independiente:** Extrae control interactivo pequeño desde página servidor.

**Criterios de aceptación:** Frontera de cliente mínima y sin secretos.

**Errores frecuentes:** Importar variables privadas de servidor o usar hooks sin directiva.

**Comprobación:** ¿Por qué 'use client' debe colocarse en la frontera y no por defecto en cada archivo?

#### 12.7.05 — Server-side rendering

SSR genera HTML en servidor para cada solicitud o render según estrategia. Puede mejorar contenido inicial y SEO, pero requiere considerar caché, datos personalizados, hydration y costo del servidor.

**Ejemplo técnico:** Una página SSR presenta contenido inicial antes de hidratar interacciones.

**Práctica guiada:** Compara HTML inicial y comportamiento tras hydration en app de prueba.

**Actividad independiente:** Diseña página con datos por usuario y evita caché compartida de contenido privado.

**Criterios de aceptación:** Hydration coherente y caché no mezcla usuarios.

**Errores frecuentes:** Cachear respuesta personalizada públicamente o depender de window en servidor.

**Comprobación:** ¿Qué riesgo introduce cachear SSR personalizado con una clave de caché incorrecta?

#### 12.7.06 — Static site generation

SSG genera HTML en build o prerender para rutas conocidas. Reduce costo de solicitud y mejora distribución, pero el contenido puede quedar desactualizado; revalidación y rutas dinámicas deben planificarse.

**Ejemplo técnico:** Página de documentación estática con revalidación programada.

**Práctica guiada:** Identifica qué contenido puede generarse en build.

**Actividad independiente:** Diseña estrategia SSG para documentación y catálogo parcialmente dinámico.

**Criterios de aceptación:** Datos públicos actualizados según política y sin contenido privado embebido.

**Errores frecuentes:** Generar información sensible en HTML estático o asumir frescura infinita.

**Comprobación:** ¿Qué trade-off introduce SSG entre rendimiento y actualidad?

#### 12.7.07 — Data fetching

Next.js ofrece mecanismos de obtención de datos en servidor y cliente; caché, revalidación, streaming y deduplicación dependen de versión/configuración. Las llamadas deben validar respuesta, controlar errores y evitar filtrar secretos al cliente.

**Ejemplo técnico:** Fetch en servidor puede utilizar credenciales privadas si respuesta se limita a datos permitidos.

**Práctica guiada:** Diseña carga de datos en Server Component y estados de loading/error.

**Actividad independiente:** Implementa política de caché según público, personalización y volatilidad.

**Criterios de aceptación:** Caché coherente con sensibilidad y frescura.

**Errores frecuentes:** Exponer secretos en props serializadas o cachear datos de un usuario para otro.

**Comprobación:** ¿Qué criterio determina si una respuesta puede almacenarse en caché compartida?

#### 12.7.08 — Authentication

La autenticación verifica identidad; autorización decide acceso. Next.js puede integrar proveedores o sesiones, pero la protección real debe aplicarse en servidor/API y en cada recurso. Cookies seguras, rotación, expiración y CSRF forman parte del diseño.

**Ejemplo técnico:** Middleware o layout puede mejorar navegación, pero endpoint vuelve a verificar permisos.

**Práctica guiada:** Dibuja login, sesión, autorización de recurso y cierre de sesión.

**Actividad independiente:** Diseña acceso con cookie HttpOnly/Secure/SameSite y comprobación de rol en servidor.

**Criterios de aceptación:** Rutas y datos protegidos server-side; sesión revocable.

**Errores frecuentes:** Proteger solo rutas cliente o almacenar credenciales en localStorage.

**Comprobación:** ¿Por qué ocultar una página no sustituye autorización en el endpoint?

#### 12.7.09 — Metadata

Metadata API permite definir title, description, Open Graph y metadatos dinámicos. Los valores deben corresponder al contenido; no incluir secretos ni duplicar títulos. El soporte y generación varían por versión y tipo de ruta.

**Ejemplo técnico:** generateMetadata puede derivar title de un registro público validado.

**Práctica guiada:** Define metadata estática y dinámica en rutas de prueba.

**Actividad independiente:** Diseña títulos y descripciones por página con fallback seguro.

**Criterios de aceptación:** Metadatos únicos, coherentes y sin datos privados.

**Errores frecuentes:** Generar metadata desde input no validado o duplicar tags.

**Comprobación:** ¿Qué problema puede causar reutilizar metadata genérica en todas las rutas?

#### 12.7.10 — Deployment

El despliegue Next.js depende de runtime Node, plataforma serverless/edge o export estático, variables de entorno, build y configuración de caché. Secretos deben residir en entorno servidor, y los builds deben ser reproducibles y verificables.

**Ejemplo técnico:** Una variable NEXT_PUBLIC se expone al bundle cliente; una variable privada no debe prefijarse así.

**Práctica guiada:** Distingue variables públicas/privadas y modos de despliegue en configuración de prueba.

**Actividad independiente:** Redacta checklist de build, migraciones, health check, rollback y monitoreo.

**Criterios de aceptación:** Build reproducible y secretos no expuestos.

**Errores frecuentes:** Subir .env al repositorio o asumir que todos los hostings soportan runtime idéntico.

**Comprobación:** ¿Qué implica el prefijo NEXT_PUBLIC para una variable?

#### 12.8.01 — npm

npm es el gestor de paquetes incluido habitualmente con Node.js. package.json declara scripts, dependencias y metadatos; package-lock.json fija árbol resuelto para instalaciones reproducibles. Scripts pueden ejecutar código, por lo que se revisa origen de dependencias.

**Ejemplo técnico:** npm ci instala según lockfile y falla si package/lock no coinciden.

**Práctica guiada:** Inspecciona package.json y lockfile de proyecto de laboratorio.

**Actividad independiente:** Define scripts de build, test y lint.

**Criterios de aceptación:** Versiones y scripts reproducibles.

**Errores frecuentes:** Ejecutar paquetes desconocidos sin revisar o ignorar lockfile.

**Comprobación:** ¿Qué diferencia hay entre npm install y npm ci en un entorno reproducible?

#### 12.8.02 — pnpm

pnpm es gestor de paquetes que utiliza almacenamiento direccionado por contenido y enlaces para ahorrar espacio y mejorar consistencia. Workspace y lockfile administran monorepos; compatibilidad depende de versión y configuración.

**Ejemplo técnico:** pnpm install --frozen-lockfile exige coherencia del lockfile.

**Práctica guiada:** Compara estructura de node_modules y lockfile en proyecto de prueba.

**Actividad independiente:** Diseña workspace con dos paquetes internos.

**Criterios de aceptación:** Instalación reproducible y dependencias explícitas.

**Errores frecuentes:** Mezclar gestores sin política o ignorar versión fijada de pnpm.

**Comprobación:** ¿Por qué conviene fijar versión de gestor en un equipo?

#### 12.8.03 — Vite

Vite proporciona servidor de desarrollo rápido y build basado en herramientas modernas; utiliza módulos ESM en desarrollo y empaqueta para producción. Plugins y configuración dependen del framework y versión.

**Ejemplo técnico:** npm run dev inicia servidor de desarrollo; npm run build genera artefactos.

**Práctica guiada:** Crea app de laboratorio y observa diferencia dev/build.

**Actividad independiente:** Configura variables, alias y build reproducible.

**Criterios de aceptación:** Build generado y rutas verificadas.

**Errores frecuentes:** Confundir servidor dev con despliegue productivo o exponer secretos con prefijos públicos.

**Comprobación:** ¿Por qué el servidor de desarrollo no debe tratarse como servidor de producción?

#### 12.8.04 — ESLint

ESLint analiza patrones de código y aplica reglas configurables. Plugins y configuraciones pueden incluir reglas de framework, accesibilidad y TypeScript. Lint detecta clases de defectos, pero no demuestra corrección funcional.

**Ejemplo técnico:** npm run lint informa variables no usadas y patrones problemáticos.

**Práctica guiada:** Ejecuta lint en proyecto propio y clasifica errores/advertencias.

**Actividad independiente:** Define reglas mínimas y justifica excepciones.

**Criterios de aceptación:** Reglas reproducibles y excepciones documentadas.

**Errores frecuentes:** Desactivar reglas globalmente para silenciar problemas.

**Comprobación:** ¿Qué diferencia hay entre lint y pruebas automatizadas?

#### 12.8.05 — Prettier

Prettier formatea código de forma consistente según configuración. Reduce debates de estilo, pero no valida lógica ni reemplaza ESLint. Integración debe evitar conflictos de reglas y ejecutarse de forma reproducible.

**Ejemplo técnico:** prettier --check informa archivos que no cumplen formato.

**Práctica guiada:** Formatea un archivo de laboratorio y revisa diff.

**Actividad independiente:** Define .prettierrc y script check.

**Criterios de aceptación:** Formato uniforme sin cambios semánticos esperados.

**Errores frecuentes:** Usar formateador como sustituto de revisión o tests.

**Comprobación:** ¿Qué clase de defectos no detecta Prettier?

#### 12.8.06 — Tailwind CSS

Tailwind CSS ofrece clases utilitarias generadas a partir de configuración y contenido detectado. La versión cambia configuración y directivas; seguir documentación de la versión instalada. La composición debe preservar semántica, accesibilidad y consistencia.

**Ejemplo técnico:** Clases de layout y spacing componen UI sin crear selector por componente.

**Práctica guiada:** Inspecciona build y clases de un componente de prueba.

**Actividad independiente:** Define tokens/tema y evita clases arbitrarias repetidas.

**Criterios de aceptación:** CSS generado cubre clases usadas y el HTML sigue accesible.

**Errores frecuentes:** Copiar sintaxis de otra versión o usar clases solo para ocultar controles esenciales.

**Comprobación:** ¿Por qué hay que identificar la versión de Tailwind antes de aplicar una guía?

#### 12.8.07 — React DevTools

React DevTools permite inspeccionar árbol de componentes, props, estado y rendimiento en entorno compatible. Debe utilizarse sin exponer datos sensibles y con diferencias entre build desarrollo/producción.

**Ejemplo técnico:** Profiler identifica componentes que renderizan y tiempos relativos.

**Práctica guiada:** Inspecciona árbol de una app de laboratorio y registra renders.

**Actividad independiente:** Analiza renderizaciones innecesarias y justifica optimización medida.

**Criterios de aceptación:** Hallazgos reproducibles y sin datos privados.

**Errores frecuentes:** Optimizar por intuición o dejar herramientas de depuración con datos sensibles en producción.

**Comprobación:** ¿Qué evidencia aporta Profiler antes de optimizar un componente?

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 89 orientaciones genéricas del desglose por explicaciones específicas de cada entrada oficial. Se añadieron precisiones sobre semántica y coerción de JavaScript, closures/prototypes/this, propagación de eventos, ciclo de eventos y microtasks, almacenamiento del navegador, límites de TypeScript en runtime, reglas de hooks, Server/Client Components, caché, autenticación y seguridad de dependencias.

**Revisión interna:** 89/89 entradas desarrolladas y cotejadas con el roadmap. La guía principal conserva ejemplos, proyecto y evaluación. Pendiente: fijar versiones exactas de Node.js, TypeScript, React y Next.js para ejecución reproducible; compilar, ejecutar pruebas de componentes y accesibilidad, validar APIs y revisar el despliegue. Esta revisión documental no acredita ejecución ni aprobación externa.
