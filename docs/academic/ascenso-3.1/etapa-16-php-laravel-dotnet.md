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
