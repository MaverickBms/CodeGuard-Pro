# Etapa 12 — JavaScript, TypeScript y frameworks frontend

**Prioridad:** P1 · Obligatoria  
**Estado editorial:** borrador  
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

**Consulta documental:** 2026-11-19. **Verificación práctica:** ejemplos y proyecto no ejecutados en esta sesión. **Estado:** borrador.
