# Etapa 16 — Backend III: PHP, Laravel y .NET

**Prioridad:** P2 · Complementaria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** conocer otros ecosistemas empresariales y poder adaptarte a proyectos que utilicen diferentes tecnologías.  
**Proyecto oficial:** crear una API pequeña en Laravel y otra en ASP.NET Core, comparando su arquitectura con Spring Boot y NestJS.

## Enfoque de profundidad
ASCENSO mantiene Java/Spring Boot como especialización backend principal y NestJS como segunda implementación completa. PHP/Laravel y C#/.NET son ecosistemas complementarios: se busca comprender su arquitectura y poder incorporarse a proyectos existentes, no dominar cuatro frameworks al mismo nivel.

## 16.1 — PHP
PHP es un lenguaje de propósito general especialmente utilizado en desarrollo web del lado servidor. Estudia sintaxis, variables, tipos, operadores, funciones, arrays, objetos, POO, namespaces y excepciones. Comprende diferencias entre comparación flexible y estricta, coerción, manejo de errores y configuración del runtime.

Composer administra dependencias y autoloading. Aprende composer.json, composer.lock, restricciones de versiones, paquetes y autoload PSR-4. No edites dependencias instaladas manualmente ni subas credenciales. La versión de PHP debe declararse y ser compatible con el framework y paquetes seleccionados.

**Ejercicio:** implementa una CLI pequeña de catálogo con tipos, clases, excepciones y pruebas; añade autoloading mediante Composer.

## 16.2 — Laravel
Laravel organiza aplicaciones mediante rutas, controllers, models y servicios. Eloquent ORM mapea modelos a tablas; entiende relaciones, consultas, carga de relaciones y riesgo N+1. Las migrations versionan el esquema; seeders cargan datos iniciales de prueba y no deben contener datos personales reales.

Middleware procesa solicitudes de forma transversal. Validation verifica entradas, pero las reglas de negocio deben comprobarse también en el dominio. Authentication identifica usuarios; authorization aplica policies/gates y permisos por recurso. Queues y jobs procesan trabajo diferido; events y listeners desacoplan reacciones; notifications entregan avisos por canales configurados; API Resources controlan la representación JSON.

No devuelvas modelos completos si exponen campos internos. Configura CSRF, cookies, sesiones, rate limiting, almacenamiento de secretos y logs según el despliegue.

**Ejercicio:** crea una API Laravel de productos con migración, seeder de datos ficticios, validación, policy, paginación y API Resource.

## 16.3 — C# y .NET
C# es un lenguaje tipado con clases, interfaces, propiedades, excepciones y genéricos. Estudia LINQ para consultar colecciones y fuentes de datos; comprende evaluación diferida cuando aplique. Async/Await permite coordinar operaciones asíncronas; no bloquees innecesariamente con llamadas síncronas ni confundas concurrencia con paralelismo.

Comprende manejo de excepciones, nullable reference types, interfaces, inyección de dependencias y estructura de proyectos .NET. Distingue compilación, runtime y paquetes NuGet. No suprimas advertencias de nulabilidad sin analizar su causa.

**Ejercicio:** implementa una biblioteca de dominio de inventario en C#, con interfaces, LINQ, validación y pruebas unitarias.

## 16.4 — ASP.NET Core
ASP.NET Core permite construir aplicaciones web y APIs. Comprende arquitectura, routing, controllers y Minimal APIs. Dependency Injection registra servicios con ciclos de vida adecuados: transient, scoped y singleton; no inyectes dependencias scoped en singleton sin un patrón correcto.

Middleware forma una pipeline ordenada. Entity Framework Core ofrece ORM y migraciones; entiende tracking, consultas, relaciones, transacciones y problemas N+1. REST requiere contratos coherentes. Authentication y Authorization deben proteger rutas y recursos; JWT requiere validación de firma, issuer, audience y expiración. No confundas autenticación con autorización.

**Ejercicio:** crea una API mínima de inventario con EF Core, migraciones, validación, manejo uniforme de errores y autorización por recurso.

## Proyecto oficial — Comparación Laravel y ASP.NET Core
Construye una API pequeña equivalente en ambos ecosistemas y compara sus decisiones con las de Spring Boot y NestJS.

### Requisitos
1. Mismo dominio y casos de uso en las dos implementaciones.
2. CRUD, validación y errores consistentes.
3. Persistencia relacional y migraciones.
4. Separación entre transporte, lógica y persistencia.
5. Autenticación/autorización demostrable o declarar explícitamente su alcance.
6. Pruebas unitarias e integración.
7. Documentación de endpoints.
8. Comparación de DI, middleware, ORM, validación, seguridad y testing.
9. Versiones y dependencias fijadas.
10. No afirmar equivalencia de seguridad por compartir rutas o nombres de métodos.

### Trayecto complementario — CMS y comercio electrónico
Este trayecto se aborda después de comprender frontend, backend, bases de datos y seguridad.

**WordPress, Drupal y Joomla:** instalación, configuración, actualizaciones, backups, mantenimiento, temas, plantillas, plugins/módulos, usuarios, roles, permisos, contenidos, medios y hardening. Evalúa extensiones, procedencia, mantenimiento y permisos antes de instalarlas.

**Magento, WooCommerce y PrestaShop:** arquitectura, catálogos, productos, variantes, inventario, precios, carrito, pedidos, clientes, pagos, envíos, integración con pasarelas y pruebas en sandbox. No utilices datos de tarjetas reales ni hagas pruebas de pagos en producción sin autorización.

**Proyecto de salida complementario:** sitio gestionable o tienda de demostración con catálogo, roles, inventario, flujo de compra simulado y procedimientos de respaldo/actualización.

### Entregables
Dos repositorios o dos aplicaciones claramente separadas; modelo de dominio común; pruebas; documentación API; tabla comparativa; guía de ejecución; informe de seguridad y limitaciones.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Fundamentos PHP y Composer | 15 |
| Laravel y Eloquent | 20 |
| C# y .NET | 15 |
| ASP.NET Core y EF Core | 20 |
| Comparación arquitectónica | 15 |
| Pruebas y documentación | 10 |
| Seguridad y mantenimiento | 5 |

Criterio orientativo: 80/100. La evaluación debe distinguir dominio complementario de especialización avanzada.

## Autoevaluación
1. ¿Qué aporta Composer y para qué sirve composer.lock?
2. ¿Qué diferencia hay entre autoloading y cargar archivos manualmente?
3. ¿Qué problema resuelve una migration?
4. ¿Qué diferencia hay entre authentication y authorization en Laravel?
5. ¿Qué es el problema N+1 en un ORM?
6. ¿Qué aporta LINQ?
7. ¿Qué diferencia hay entre transient, scoped y singleton?
8. ¿Por qué el orden del middleware importa?
9. ¿Qué diferencia hay entre EF Core y una base de datos?
10. ¿Qué aspectos compararías para elegir un stack backend?

## Recursos audiovisuales
No se incluyen videos aprobados. Se añadirán solo cuando el audio hablado sea español y cada video cubra el subtema concreto (PHP/Composer, Laravel Eloquent, C# async/await, ASP.NET Core DI/EF Core o administración segura de CMS). No se recomienda un curso genérico para cubrir toda la etapa.

## Referencias oficiales
- PHP Manual: https://www.php.net/manual/en/
- Composer: https://getcomposer.org/doc/
- Laravel Documentation: https://laravel.com/docs
- C# Documentation: https://learn.microsoft.com/en-us/dotnet/csharp/
- .NET Documentation: https://learn.microsoft.com/en-us/dotnet/
- ASP.NET Core: https://learn.microsoft.com/en-us/aspnet/core/
- Entity Framework Core: https://learn.microsoft.com/en-us/ef/core/
- WordPress Developer Resources: https://developer.wordpress.org/
- Drupal Documentation: https://www.drupal.org/docs
- Joomla Documentation: https://docs.joomla.org/
- Magento DevDocs: https://developer.adobe.com/commerce/docs/
- PrestaShop Developer Documentation: https://devdocs.prestashop-project.org/

**Consulta documental:** 2026-11-19. **Verificación práctica:** implementaciones no ejecutadas en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 16

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados organizan el estudio de los conceptos y los relacionan con la guía técnica y el proyecto de la etapa; no representan evaluación, aprobación ni ejecución práctica.

### Módulo 16.1 — PHP

#### 16.1.01 — Sintaxis
La sintaxis PHP define cómo declarar instrucciones, bloques, funciones y etiquetas dentro de archivos PHP. Comprende apertura/cierre de código, punto y coma, namespaces y modos de ejecución; evita mezclar lógica de presentación y dominio en scripts monolíticos.


**Escenario aplicado.** Un archivo PHP se ejecuta desde CLI y desde servidor web con contextos distintos. La aplicación documenta punto de entrada y evita mezclar salida de depuración con respuestas HTTP.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia puede existir entre ejecutar un script por CLI y mediante el servidor web?

**Práctica y evidencia:** Escribe un script PHP pequeño y ejecútalo desde CLI, comprobando salida y código de retorno. **Evidencia:** explica etiquetas PHP, punto y coma y modo de ejecución.

#### 16.1.02 — Variables
Las variables PHP comienzan con `# Etapa 16 — Backend III: PHP, Laravel y .NET

**Prioridad:** P2 · Complementaria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** conocer otros ecosistemas empresariales y poder adaptarte a proyectos que utilicen diferentes tecnologías.  
**Proyecto oficial:** crear una API pequeña en Laravel y otra en ASP.NET Core, comparando su arquitectura con Spring Boot y NestJS.

#### 16.1.03 — Tipos
PHP maneja tipos escalares, compuestos y especiales con coerciones que dependen del contexto y la versión. Utiliza declaraciones de tipos y comparaciones estrictas cuando sea posible, y valida datos provenientes de formularios, JSON o bases de datos.


**Escenario aplicado.** Un JSON contiene un valor numérico representado como cadena. La aplicación valida el tipo esperado en runtime y evita depender de coerciones implícitas.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué riesgo introducen las conversiones implícitas al validar datos externos?

**Escenario aplicado.** Una variable procedente de un formulario se valida antes de incorporarse a una consulta o salida HTML. El nombre y alcance se mantienen explícitos para evitar estado global accidental.

**Criterio de análisis.** La respuesta debe identificar fuente, validación y contexto de uso. **Pregunta de comprensión:** ¿Por qué no debe confiarse en una variable solo porque llega desde un formulario?

**Práctica y evidencia:** Compara tipos escalares, arrays, objetos, null y conversiones. **Evidencia:** demuestra validación explícita de datos recibidos desde una petición.

#### 16.1.04 — Operadores
Los operadores realizan operaciones aritméticas, lógicas, comparación, asignación y manejo de tipos. Distingue `==` de `===`, comprende precedencia y evita coerciones implícitas ambiguas en reglas de negocio.


**Escenario aplicado.** Una comparación estricta evita que una cadena vacía se interprete como cero en una regla de autorización o negocio.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué las comparaciones estrictas son preferibles en validaciones sensibles?

**Práctica y evidencia:** Prueba operadores de comparación estricta y lógica con valores de tipos distintos. **Evidencia:** explica diferencias entre `==` y `===` mediante casos reproducibles.

#### 16.1.05 — Funciones
Las funciones encapsulan lógica reutilizable y pueden declarar parámetros, valores predeterminados, tipos y retorno. Mantén funciones pequeñas, evita efectos colaterales innecesarios y documenta excepciones y precondiciones.


**Escenario aplicado.** Una función valida y normaliza una dirección de correo y comunica error de forma explícita. No realiza consultas ni efectos secundarios inesperados.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué características hacen que una función sea fácil de probar y reutilizar?

**Práctica y evidencia:** Define una función con parámetros tipados, valor por defecto y retorno declarado. **Evidencia:** prueba entradas válidas y tipos no compatibles.

#### 16.1.06 — Arrays
Los arrays PHP funcionan como mapas ordenados que pueden utilizar claves numéricas o cadenas. Distingue arrays indexados y asociativos, valida la existencia de claves y evita asumir que una estructura recibida tiene la forma esperada.


**Escenario aplicado.** Un array asociativo representa campos de una solicitud. La aplicación verifica claves requeridas y tipos antes de utilizar valores opcionales.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia existe entre una clave ausente y una clave cuyo valor es null?

**Práctica y evidencia:** Transforma un conjunto de pedidos con funciones de arrays y evita modificar la fuente accidentalmente. **Evidencia:** presenta entrada, salida y criterio de transformación.

#### 16.1.07 — Objetos
Los objetos agrupan estado y comportamiento mediante clases, propiedades y métodos. Controla visibilidad, invariantes y construcción; no expongas propiedades sensibles ni permitas que cualquier consumidor modifique el estado sin validación.


**Escenario aplicado.** Un objeto de dominio protege sus invariantes mediante métodos, en lugar de permitir que cualquier consumidor modifique propiedades internas directamente.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué ventaja aporta encapsular el estado de un objeto?

**Práctica y evidencia:** Crea un objeto de dominio con propiedades y métodos y controla su visibilidad. **Evidencia:** explica encapsulación y acceso permitido.

#### 16.1.08 — POO
La POO en PHP utiliza encapsulamiento, herencia, interfaces, traits y polimorfismo. Prefiere composición cuando reduce acoplamiento y diseña contratos que permitan sustituir implementaciones sin romper el comportamiento esperado.


**Escenario aplicado.** Una clase de pedido valida transiciones de estado y evita que un pedido cancelado vuelva a procesarse como nuevo sin una operación explícita.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué las reglas de transición pertenecen al dominio y no solo al controlador?

**Práctica y evidencia:** Modela una jerarquía pequeña o composición para un dominio de ventas. **Evidencia:** justifica cuándo usar composición en lugar de herencia.

#### 16.1.09 — Namespaces
Namespaces organizan símbolos y evitan colisiones de nombres entre clases, interfaces y funciones. Declara namespaces coherentes con la estructura del proyecto y utiliza imports explícitos para que dependencias y nombres sean legibles.


**Escenario aplicado.** Namespaces separan clases con nombres similares y Composer resuelve autoloading según reglas PSR-4. El mapa debe corresponder con la estructura real del proyecto.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué error puede causar una discrepancia entre namespace y autoload mapping?

**Práctica y evidencia:** Organiza clases en namespaces y resuelve importaciones con `use`. **Evidencia:** explica cómo se evita colisión de nombres.

#### 16.1.10 — Excepciones
Las excepciones representan condiciones anómalas que pueden propagarse y capturarse. Captura tipos específicos en el límite donde puedas recuperarte, registra contexto sin secretos y no silencies fallos con bloques catch vacíos.


**Escenario aplicado.** Una excepción de base de datos se registra con correlación, pero la respuesta pública no revela consulta, ruta local ni stack trace.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué información se debe registrar para depurar sin filtrar detalles al usuario?

**Práctica y evidencia:** Lanza y captura excepciones específicas y evita ocultar fallos con catch vacío. **Evidencia:** registra contexto seguro y diferencia error recuperable de fallo inesperado.

#### 16.1.11 — Composer
Composer administra dependencias PHP, autoloading y metadatos del proyecto mediante `composer.json`. Revisa paquetes y scripts, fija restricciones de versión razonables y conserva `composer.lock` en aplicaciones para reproducir instalaciones.


**Escenario aplicado.** Composer instala dependencias y genera lockfile. El equipo revisa paquetes transitivos, scripts de instalación y advisories antes de actualizar.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué composer.lock debe conservarse en una aplicación?

**Práctica y evidencia:** Añade una dependencia con Composer y examina composer.json y composer.lock. **Evidencia:** explica restricciones de versión y reproducibilidad de instalación.

#### 16.1.12 — Autoloading
Autoloading carga clases según reglas configuradas, habitualmente PSR-4 en proyectos modernos. Mantén correspondencia entre namespace y rutas, regenera el autoloader cuando cambie la configuración y evita incluir archivos manualmente sin necesidad.


**Escenario aplicado.** El autoloader carga clases conforme a namespaces y mapeos configurados. Una clase no encontrada requiere revisar ruta, namespace y dump-autoload, no incluir archivos al azar.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué relación existe entre PSR-4, namespace y ruta del archivo?

**Práctica y evidencia:** Configura autoloading PSR-4 para un namespace de aplicación. **Evidencia:** demuestra carga automática y explica por qué no se incluyen manualmente todos los archivos.

### Módulo 16.2 — Laravel

#### 16.2.01 — Routing
Routing de Laravel asocia métodos HTTP y URI con controladores o closures. Define rutas nombradas y agrupadas, valida parámetros y protege rutas sensibles mediante middleware; no confundas ocultar una ruta en frontend con protegerla.


**Escenario aplicado.** Una ruta Laravel declara método y middleware. Las rutas públicas y protegidas se agrupan explícitamente y se comprueba que no existan endpoints administrativos expuestos.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué las rutas deben revisarse junto con sus middlewares?

**Práctica y evidencia:** Define rutas Laravel con métodos HTTP y parámetros y verifica rutas registradas. **Evidencia:** prueba ruta válida, parámetro y 404.

#### 16.2.02 — Controllers
Controllers coordinan solicitudes y respuestas y delegan reglas a servicios o modelos. Mantén controladores delgados, valida entradas mediante Form Requests y devuelve recursos/redirects consistentes.


**Escenario aplicado.** El controller recibe una petición validada y delega a servicios o modelos. Las reglas de negocio no se repiten entre varios controladores.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué problema causa duplicar lógica de negocio en controladores distintos?

**Práctica y evidencia:** Implementa un controller delgado que delegue reglas de negocio a una clase de servicio. **Evidencia:** prueba respuesta y evita lógica de dominio dentro de la vista.

#### 16.2.03 — Models
Models de Eloquent representan entidades persistentes y facilitan consultas y relaciones. Define atributos asignables y ocultos cuidadosamente, controla mass assignment y evita exponer columnas sensibles en serialización.


**Escenario aplicado.** Un modelo Eloquent representa una entidad persistente y define relaciones y casts. No debe serializarse automáticamente si contiene atributos sensibles.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué controles evitan exponer campos ocultos o relaciones privadas en JSON?

**Práctica y evidencia:** Define un modelo Eloquent y sus atributos permitidos, casts y relaciones. **Evidencia:** demuestra protección frente a asignación masiva.

#### 16.2.04 — Eloquent ORM
Eloquent ORM permite consultar y relacionar modelos mediante una abstracción orientada a objetos. Comprende lazy/eager loading y consultas N+1; inspecciona SQL generado y aplica scopes cuando expresen reglas reutilizables.


**Escenario aplicado.** Una relación Eloquent lazy puede generar N+1 consultas. El equipo usa eager loading de forma deliberada y verifica el número de consultas.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Cómo detectas que una consulta está provocando N+1?

**Práctica y evidencia:** Ejecuta una consulta Eloquent y analiza SQL generado y carga de relaciones. **Evidencia:** detecta N+1 y compara eager loading.

#### 16.2.05 — Migrations
Migrations versionan cambios de esquema y permiten recrear la estructura de base de datos. Escribe migraciones reversibles cuando sea posible, revisa impacto sobre datos existentes y no ejecutes cambios destructivos en producción sin respaldo y plan.


**Escenario aplicado.** Una migración añade primero una columna compatible y luego el código empieza a depender de ella. La estrategia permite despliegues graduales y rollback planificado.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué una migración de producción no debe evaluarse solo por su sintaxis?

**Práctica y evidencia:** Crea una migración para añadir una tabla y aplica rollback en base descartable. **Evidencia:** registra estado antes/después y conserva migración versionada.

#### 16.2.06 — Seeders
Seeders cargan datos iniciales o de demostración de forma repetible. Separa fixtures de prueba de datos reales, evita credenciales predeterminadas y asegúrate de que repetir el seeder no corrompa el estado.


**Escenario aplicado.** Un seeder crea datos sintéticos reproducibles para pruebas. No debe insertar usuarios reales, contraseñas por defecto ni datos personales en producción.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia existe entre seed de desarrollo y carga de datos de producción?

**Práctica y evidencia:** Crea un seeder con datos sintéticos repetibles. **Evidencia:** demuestra que puede ejecutarse varias veces sin duplicar registros indebidamente.

#### 16.2.07 — Middleware
Middleware procesa solicitudes antes o después de llegar al controlador, por ejemplo para autenticación, throttling o headers. Ordena el middleware y aplica la protección adecuada a cada grupo de rutas.


**Escenario aplicado.** Un middleware autentica sesión o verifica una condición transversal. La autorización por recurso sigue siendo responsabilidad de una política o capa específica.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué middleware de autenticación no garantiza acceso autorizado al objeto?

**Práctica y evidencia:** Añade middleware que compruebe una condición transversal y pase o rechace la solicitud. **Evidencia:** documenta orden y respuesta ante rechazo.

#### 16.2.08 — Validation
Validation verifica que los datos cumplan reglas de formato, presencia, rango y relación. Utiliza reglas del framework y mensajes claros, pero valida también invariantes en el dominio y constraints en la base de datos.


**Escenario aplicado.** Una solicitud con campo fuera de rango se rechaza mediante reglas de validación. Las invariantes que dependen de datos actuales se comprueban también en la capa de dominio.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia existe entre validar forma de entrada y validar reglas de negocio?

**Práctica y evidencia:** Valida datos con reglas explícitas y mensajes útiles antes de persistir. **Evidencia:** prueba campos faltantes, límites y tipos inválidos.

#### 16.2.09 — Authentication
Authentication en Laravel identifica usuarios mediante guards y providers configurados. Selecciona el mecanismo adecuado para sesión o API, protege cookies y credenciales y aplica expiración, rotación y revocación.


**Escenario aplicado.** El sistema limita intentos, protege sesión y evita enumeración. La autenticación se prueba con credenciales correctas, incorrectas, expiradas y revocadas.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué escenarios deben probarse además del login exitoso?

**Práctica y evidencia:** Configura autenticación mediante el mecanismo apropiado para aplicación web o API. **Evidencia:** prueba sesión, cierre de sesión y protección CSRF donde corresponda.

#### 16.2.10 — Authorization
Authorization determina qué acciones puede realizar un usuario mediante gates, policies y permisos. Comprueba autorización por recurso y operación, incluyendo identificadores manipulados, y no confíes en botones ocultos como control de acceso.


**Escenario aplicado.** Un usuario autenticado intenta editar el recurso de otro tenant. Una policy comprueba propiedad y contexto, aunque la ruta y el token sean válidos.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué ocultar un enlace en la interfaz no protege una acción de API?

**Práctica y evidencia:** Aplica Policies o Gates para autorizar acciones sobre recursos concretos. **Evidencia:** demuestra que un usuario no puede modificar recursos de otro.

#### 16.2.11 — Queues
Queues ejecuta tareas diferidas en workers para desacoplar solicitudes lentas. Configura backend, reintentos, timeout y failed jobs; diseña tareas idempotentes y monitorea workers detenidos.


**Escenario aplicado.** Una cola permite procesar tareas fuera de la solicitud web. El job maneja reintentos y evita duplicar efectos si se entrega más de una vez.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué un job debe ser idempotente cuando se utilizan reintentos?

**Práctica y evidencia:** Despacha un mensaje a una cola de laboratorio y configura un worker. **Evidencia:** registra entrega, reintento y comportamiento ante fallo.

#### 16.2.12 — Jobs
Jobs encapsulan trabajo que puede ejecutarse de manera inmediata o en cola. Mantén payloads serializables y pequeños, maneja reintentos y evita depender de estado temporal que desaparezca entre procesos.


**Escenario aplicado.** Un job de exportación se ejecuta en segundo plano y guarda estado de progreso. Se definen timeout, backoff y manejo de fallo permanente.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué información necesita soporte para investigar un job fallido?

**Práctica y evidencia:** Implementa un Job idempotente con timeout y política de reintentos. **Evidencia:** demuestra que una ejecución repetida no duplica efectos.

#### 16.2.13 — Events
Events y listeners separan la emisión de un hecho de las acciones que reaccionan a él. Define si el listener es síncrono o en cola, considera duplicados y orden, y evita ciclos de eventos difíciles de rastrear.


**Escenario aplicado.** Un evento de dominio notifica que un pedido fue pagado. Los listeners no deben asumir entrega exactamente una vez y registran su procesamiento.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia existe entre emitir un evento y ejecutar directamente una función?

**Práctica y evidencia:** Emite un evento de dominio y conecta un listener. **Evidencia:** explica sincronía/asincronía y consistencia si el evento se publica antes del commit.

#### 16.2.14 — Notifications
Notifications envía avisos mediante canales como correo, base de datos o servicios integrados. Controla preferencias, frecuencia y datos personales, y no incluyas tokens de acceso o información sensible en notificaciones sin protección.


**Escenario aplicado.** Una notificación se envía después de confirmar la operación principal o mediante outbox/cola. Un fallo de correo no debe revertir silenciosamente una compra ya confirmada.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué conviene desacoplar el envío de notificaciones de la transacción principal?

**Práctica y evidencia:** Envía una notificación a un canal de prueba y evita incluir datos sensibles. **Evidencia:** documenta destinatario, canal y resultado de envío.

#### 16.2.15 — API Resources
API Resources transforman modelos y colecciones a representaciones JSON controladas. Expón solo campos autorizados, define relaciones y paginación explícitas y evita serializar automáticamente el modelo completo.


**Escenario aplicado.** Un API Resource transforma un modelo en una representación pública controlada. La respuesta expone solo campos autorizados y evita ciclos de relaciones.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué ventaja aporta un recurso API frente a devolver el modelo directamente?

**Práctica y evidencia:** Define API Resources para controlar la forma de respuesta y relaciones expuestas. **Evidencia:** demuestra que campos internos o sensibles no aparecen en JSON.

### Módulo 16.3 — C# y .NET

#### 16.3.01 — Sintaxis de C#
La sintaxis de C# define declaraciones, expresiones, bloques, patrones y construcciones del lenguaje. Mantén estilo coherente y conoce las características disponibles en la versión de lenguaje configurada en el proyecto.


**Escenario aplicado.** Un método C# recibe parámetros tipados y devuelve un resultado definido. Las convenciones de nullability y análisis estático se usan para detectar errores antes de ejecutar.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué problemas puede detectar el compilador que no detecta una prueba manual?

**Práctica y evidencia:** Escribe un programa C# con tipos, métodos y control de flujo y compílalo con SDK elegido. **Evidencia:** registra versión de SDK y resultado.

#### 16.3.02 — Tipos
C# es estáticamente tipado y ofrece tipos por valor, referencia, nullable y genéricos. Comprende conversiones y nullability, activa nullable reference types cuando sea posible y valida datos externos en runtime.


**Escenario aplicado.** Un API recibe una cadena que representa un entero. La conversión se realiza con TryParse y se valida rango antes de usar el dato.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué TryParse es más apropiado que asumir que toda conversión tendrá éxito?

**Práctica y evidencia:** Compara value types y reference types con asignación y copia. **Evidencia:** explica mutabilidad y comportamiento al pasar valores a métodos.

#### 16.3.03 — Clases
Las clases definen tipos de referencia con estado, métodos, constructores y propiedades. Diseña invariantes y visibilidad explícita, y evita clases que acumulen responsabilidades no relacionadas.


**Escenario aplicado.** Una clase encapsula estado y comportamiento de una entidad. El constructor protege invariantes y no expone setters públicos innecesarios.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué ventaja ofrece un constructor que valida el estado inicial?

**Práctica y evidencia:** Define una clase con constructor, propiedades y métodos con invariantes. **Evidencia:** prueba estado válido y transición inválida.

#### 16.3.04 — Interfaces
Las interfaces definen contratos que pueden implementar múltiples clases o structs. Programa contra abstracciones cuando facilite sustitución y pruebas, pero evita interfaces innecesarias que solo duplican una implementación sin aportar límite útil.


**Escenario aplicado.** Una interfaz define contrato y permite sustituir una implementación en pruebas. No se debe crear una interfaz por cada clase si no aporta abstracción útil.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Cuándo una interfaz mejora diseño y cuándo solo añade complejidad?

**Práctica y evidencia:** Implementa una interfaz y dos clases que la satisfagan. **Evidencia:** consume ambas mediante el contrato sin depender de implementación concreta.

#### 16.3.05 — POO
La POO en C# combina encapsulamiento, herencia, polimorfismo, interfaces y composición. Elige herencia para relaciones de sustitución válidas y utiliza composición para combinar capacidades con menor acoplamiento.


**Escenario aplicado.** Una jerarquía de clases evita duplicación, pero composición puede ser más adecuada cuando los tipos no comparten una relación real de sustitución.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué principio ayuda a decidir si conviene herencia o composición?

**Práctica y evidencia:** Modela un dominio usando encapsulación, composición e interfaces. **Evidencia:** justifica relaciones y evita herencia innecesaria.

#### 16.3.06 — LINQ
LINQ permite consultar secuencias y colecciones mediante operadores como `Where`, `Select`, `OrderBy` y `GroupBy`. Distingue ejecución diferida de materialización, evita enumerar varias veces consultas costosas y revisa la traducción cuando el proveedor es una base de datos.


**Escenario aplicado.** Una consulta LINQ filtra y proyecta datos antes de materializarlos. Con EF Core, la expresión puede traducirse a SQL; una operación no traducible puede ejecutarse en memoria o fallar según contexto.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué debe inspeccionarse el SQL generado por una consulta LINQ?

**Práctica y evidencia:** Consulta una colección con LINQ usando Where, Select, OrderBy y GroupBy. **Evidencia:** explica ejecución diferida y cuándo materializar.

#### 16.3.07 — Generics
Generics permiten escribir clases y métodos reutilizables con parámetros de tipo y restricciones. Conservan seguridad estática y evitan casts; define constraints solo cuando una operación necesita capacidades específicas.


**Escenario aplicado.** Un método genérico opera sobre varios tipos con restricciones explícitas. La restricción expresa capacidades necesarias y evita casts inseguros.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué ventaja ofrecen las restricciones genéricas frente a usar object?

**Práctica y evidencia:** Crea un método genérico con restricción de tipo y úsalo con dos tipos. **Evidencia:** explica qué errores evita el compilador.

#### 16.3.08 — Async/Await
Async/Await simplifica operaciones asíncronas mediante `Task` y `Task<T>`. Evita bloquear con `.Result` o `.Wait()` en rutas asíncronas, propaga cancellation tokens y maneja excepciones de tareas.


**Escenario aplicado.** Un método async espera I/O sin bloquear el hilo mientras se completa. No se debe usar async void salvo manejadores de eventos y se propagan cancelación y excepciones.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué async no significa que el código siempre se ejecute en paralelo?

**Práctica y evidencia:** Implementa una operación asíncrona con Task y cancellation token. **Evidencia:** distingue await de bloqueo y maneja cancelación.

#### 16.3.09 — Exception handling
Exception handling utiliza `try`, `catch`, `finally` y `throw` para gestionar fallos. Captura excepciones específicas, preserva stack trace al relanzar y no utiliza excepciones como flujo normal de negocio.


**Escenario aplicado.** Una excepción de infraestructura se traduce a error de aplicación sin perder correlación. No se captura y descarta una excepción para continuar como si nada hubiera ocurrido.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué riesgo introduce un catch vacío?

**Práctica y evidencia:** Captura excepciones específicas y conserva contexto con inner exception cuando se relanza. **Evidencia:** evita capturar Exception sin propósito y documenta error seguro.

### Módulo 16.4 — ASP.NET Core

#### 16.4.01 — Arquitectura
ASP.NET Core organiza aplicaciones web mediante middleware, routing, servicios y hosting. Comprende el pipeline de solicitudes y el entorno de ejecución, y configura logging, errores y headers seguros desde el inicio.


**Escenario aplicado.** Una API ASP.NET Core separa presentación, aplicación, dominio e infraestructura según la complejidad real. Los límites evitan que el controlador concentre persistencia y reglas.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué problema causa acoplar el dominio directamente al framework web?

**Práctica y evidencia:** Dibuja el pipeline de una solicitud ASP.NET Core desde servidor hasta endpoint. **Evidencia:** identifica configuración, middleware, routing y ejecución.

#### 16.4.02 — Controllers
Controllers en ASP.NET Core agrupan endpoints MVC y coordinan model binding, validación y respuestas. Mantén acciones delgadas, utiliza DTOs y devuelve resultados HTTP coherentes.


**Escenario aplicado.** Un controller usa binding y validación de entrada, y devuelve resultados HTTP adecuados. Las políticas de autorización se aplican también a los recursos.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué controles deben aplicarse además del model binding?

**Práctica y evidencia:** Implementa un controller con binding, validación y respuestas tipadas. **Evidencia:** prueba entrada válida y error de modelo.

#### 16.4.03 — Minimal APIs
Minimal APIs permiten definir endpoints con menos estructura de controladores, adecuadas para servicios pequeños o límites concretos. Mantén agrupación, validación, filtros y documentación claras para que la concisión no convierta el archivo en un monolito.


**Escenario aplicado.** Minimal API define endpoints de forma concisa, pero debe conservar validación, autorización, observabilidad y organización modular.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Cuándo una Minimal API deja de ser mantenible si toda la lógica se concentra en Program.cs?

**Práctica y evidencia:** Crea una Minimal API para un recurso pequeño y compara con controller. **Evidencia:** justifica la opción por tamaño, organización y necesidades del servicio.

#### 16.4.04 — Dependency Injection
Dependency Injection es parte del host de ASP.NET Core y registra servicios con ciclos de vida transient, scoped y singleton. Selecciona el ciclo correcto y no inyectes servicios scoped en singletons sin un patrón seguro.


**Escenario aplicado.** La DI registra servicios con lifetimes singleton, scoped y transient. Un singleton no debe capturar directamente una dependencia scoped que vive por solicitud.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué problema produce un lifetime incompatible entre dependencias?

**Práctica y evidencia:** Registra un servicio en el contenedor y prueba ciclos Transient, Scoped y Singleton. **Evidencia:** explica el alcance y evita inyectar Scoped en Singleton.

#### 16.4.05 — Middleware
Middleware compone el pipeline HTTP y puede inspeccionar, modificar o terminar solicitudes. El orden afecta autenticación, autorización, routing y manejo de errores; prueba el pipeline completo y evita registrar cuerpos sensibles.


**Escenario aplicado.** El middleware se ejecuta en orden y puede terminar una solicitud antes de llegar al endpoint. Autenticación, autorización y manejo de errores deben ordenarse correctamente.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué cambiar el orden del pipeline middleware puede alterar el control de acceso?

**Práctica y evidencia:** Ordena middleware de autenticación, autorización y endpoints y observa el efecto del orden. **Evidencia:** documenta pipeline y prueba acceso permitido/denegado.

#### 16.4.06 — Entity Framework Core
Entity Framework Core es un ORM para mapear entidades y consultar bases relacionales mediante LINQ. Controla tracking, carga, transacciones y migraciones; inspecciona consultas SQL y evita operaciones N+1 o actualizaciones masivas accidentales.


**Escenario aplicado.** EF Core traduce consultas LINQ y administra tracking. Se revisan consultas N+1, tracking innecesario, concurrencia y migraciones antes de desplegar.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Cuándo conviene usar AsNoTracking y qué efecto tiene?

**Práctica y evidencia:** Mapea entidades con EF Core y ejecuta una migración en base de prueba. **Evidencia:** revisa SQL y verifica relaciones y restricciones.

#### 16.4.07 — REST
REST en ASP.NET Core expone recursos mediante rutas, métodos HTTP, status codes y representaciones. Define contratos versionados, valida entradas, pagina resultados y protege cada operación por recurso.


**Escenario aplicado.** Un recurso REST mantiene rutas y métodos coherentes y aplica autorización por objeto. El contrato documenta paginación, errores e idempotencia.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué la semántica HTTP importa aunque el backend esté implementado en .NET?

**Práctica y evidencia:** Diseña una API REST con recursos, métodos y códigos HTTP coherentes. **Evidencia:** prueba idempotencia, validación y paginación.

#### 16.4.08 — Authentication
Authentication en ASP.NET Core identifica usuarios mediante esquemas como cookies o Bearer. Configura issuer, audience, firma y expiración para tokens y protege claves; no confundas autenticación con permisos.


**Escenario aplicado.** La autenticación ASP.NET Core valida identidad mediante esquema configurado. La aplicación distingue cookies, bearer tokens y proveedores externos según tipo de cliente.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Por qué el esquema de autenticación debe elegirse según el cliente y el flujo?

**Práctica y evidencia:** Configura autenticación para una API y valida identidad en servidor. **Evidencia:** demuestra rechazo de credenciales inválidas y protección de endpoints.

#### 16.4.09 — Authorization
Authorization aplica políticas, roles y requisitos sobre endpoints o recursos. Usa políticas explícitas y comprobaciones por objeto cuando corresponda; un rol genérico no basta para proteger recursos de otros usuarios.


**Escenario aplicado.** La autorización combina roles, policies y comprobaciones por recurso. Un endpoint administrativo no queda protegido solo porque el menú lo oculte.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia existe entre autorización basada en roles y basada en recursos?

**Práctica y evidencia:** Aplica autorización basada en policy o claims a una operación. **Evidencia:** prueba un usuario autenticado sin permiso y otro autorizado.

#### 16.4.10 — JWT
JWT permite transportar claims firmados para verificar integridad y contexto de identidad. Valida firma, algoritmo, issuer, audience y expiración, limita duración y diseña rotación/revocación; el contenido firmado suele ser legible.



**Escenario aplicado.** La validación JWT comprueba firma, algoritmo, issuer, audience y expiración con configuración explícita. No se deshabilita la validación TLS para resolver errores de conexión.

**Criterio de análisis.** La respuesta debe justificar el control o decisión, identificar el fallo que previene y proponer evidencia verificable. **Pregunta de comprensión:** ¿Qué riesgo aparece al aceptar cualquier issuer o audience?

**Práctica y evidencia:** Valida JWT con firma, emisor, audiencia, expiración y algoritmo permitido. **Evidencia:** rechaza tokens manipulados y explica que el payload no está cifrado por defecto.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 46 orientaciones genéricas por explicaciones específicas para PHP, Laravel, C#/.NET y ASP.NET Core. Se desarrollaron lenguaje y tipos, POO, namespaces, Composer/autoloading, routing, Eloquent, migraciones, middleware, validación, autorización, queues/jobs/events, LINQ, async/await, DI y EF Core.

**Revisión interna:** 46/46 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron mass assignment, validación en runtime, manejo de secretos, acceso por recurso, ciclos de vida DI y riesgos de consultas ORM. Pendiente: fijar versiones de PHP/Laravel/.NET, ejecutar suites de pruebas, migraciones y flujos de autenticación/autorización en entornos aislados. No se declara ejecución ni aprobación externa.
