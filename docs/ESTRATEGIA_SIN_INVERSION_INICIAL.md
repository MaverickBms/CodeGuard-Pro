# Estrategia de desarrollo sin inversión inicial

- **Estado:** Aprobada como estrategia de ejecución inicial
- **Fecha:** 15 de noviembre de 2026
- **Decisor:** Propietario del proyecto
- **Producto:** CodeGuard Pro
- **Relacionado:** `docs/PLAN_MAESTRO_CODEGUARD.md`, `docs/ADR/ADR-004-sincronizacion-hibrida-conocimiento.md`, `docs/DECISIONES_PENDIENTES.md`

## 1. Decisión

CodeGuard Pro se continuará desarrollando inicialmente **sin inversión económica y sin contratar infraestructura externa**. La prioridad es terminar y validar una versión útil, estable y autónoma que funcione localmente.

La expansión mediante hosting, servicios remotos o infraestructura de pago se evaluará más adelante, cuando el producto tenga una base funcional sólida y exista una necesidad real que justifique el gasto. La decisión de invertir será explícita y corresponderá al propietario del proyecto. No se asume ningún compromiso de contratación ni una fecha automática para comenzar a pagar.

Esta estrategia no elimina la arquitectura híbrida aprobada en ADR-004: **pospone su despliegue remoto**, no su posibilidad futura.

## 2. Alcance de la etapa inicial: costo operativo externo $0

Mientras esté vigente esta decisión:

- No contratar VPS, hosting, servidores administrados ni bases de datos alojadas.
- No comprar dominio ni certificados/servicios adicionales de pago. Para desarrollo local no se necesita un dominio público.
- No depender de APIs de IA de pago, servicios de terceros con cobro por uso ni suscripciones para que el núcleo educativo funcione.
- No hacer obligatoria una conexión a Internet para iniciar la aplicación, estudiar, practicar o consultar el progreso ya guardado.
- No trasladar los datos personales o académicos del estudiante a una infraestructura remota.
- Evitar incorporar dependencias que generen costos recurrentes inevitables.

El objetivo es mantener el **costo de infraestructura externa en cero** durante esta etapa. Esto no significa que desarrollar software no tenga ningún costo indirecto: equipo, electricidad, conexión a Internet, tiempo y eventuales herramientas personales siguen siendo responsabilidad del propietario.

## 3. Arquitectura y funcionamiento durante esta etapa

### 3.1 Aplicación local

- Electron y Django se ejecutan en el equipo del usuario.
- SQLite es la base de datos local del producto.
- El progreso, intentos, configuraciones, historial y evidencias permanecen en el almacenamiento local.
- El contenido académico necesario para estudiar debe estar disponible localmente.
- La aplicación debe conservar sus funciones esenciales sin conexión después de instalarla.

**No se necesita una base de datos central alojada para terminar la versión local.** SQLite no se sustituye por PostgreSQL ni por otro servicio remoto en esta etapa.

### 3.2 Conocimiento y actualizaciones

El catálogo de conocimiento también podrá mantenerse y utilizarse localmente. El desarrollo debe priorizar:

1. Contenido académico original, revisado y versionado.
2. Paquetes de conocimiento que puedan generarse localmente.
3. Importación manual de paquetes cuando exista una nueva versión.
4. Validación de estructura, compatibilidad, integridad y firma antes de instalar.
5. Conservación de la versión anterior y posibilidad de rollback.
6. Registro visible de la versión instalada y de su fecha de actualización.

El publicador local, el formato de manifiestos, el verificador y el instalador transaccional son piezas reutilizables para esta estrategia. Sin embargo, **no se debe afirmar que el flujo manual completo está listo para distribución a usuarios hasta ejecutar y documentar una prueba integral**. Si algún paso aún no está validado, se mantendrá como tarea pendiente.

La sincronización automática remota permanecerá desactivada mientras no existan endpoint HTTPS, allowlist, claves públicas confiables y pruebas de aceptación de producción.

### 3.3 Tutor y funciones de IA

El núcleo de aprendizaje no debe depender de una API comercial. Se priorizarán explicaciones, pistas, evaluadores y herramientas deterministas que funcionen localmente. Un modelo de IA local podrá evaluarse como opción posterior, teniendo en cuenta los requisitos de memoria, CPU/GPU y experiencia real en los equipos objetivo. No se promete que cualquier equipo pueda ejecutar modelos locales con buen rendimiento.

## 4. Qué se construirá antes de invertir

La prioridad de producto será completar y validar, en este orden lógico:

1. Aplicación de escritorio local estable para los sistemas operativos objetivo.
2. Persistencia SQLite, copias de seguridad y recuperación de datos.
3. Roadmap ASCENSO y navegación académica coherentes.
4. Biblioteca de contenido con fuentes, licencias, revisión y versiones.
5. Lecciones, ejemplos, ejercicios y evaluaciones que midan aprendizaje real.
6. Progreso verificable e historial de intentos/evidencias.
7. Herramientas de práctica seguras; no ejecutar código arbitrario sin sandbox aislado y validado.
8. Tutoría local o ayudas pedagógicas que no requieran servicios de pago.
9. Gamificación subordinada al dominio académico.
10. Importación/actualización manual de contenido con integridad y recuperación comprobadas.
11. Instalación, actualización del ejecutable, pruebas de regresión y documentación de usuario.

El orden detallado y los criterios de aceptación siguen definidos por el plan maestro y los documentos de cada fase. Esta estrategia financiera no autoriza a saltarse pruebas ni a declarar terminadas funciones que solo tengan una estructura inicial.

## 5. Expansión futura: inversión solo cuando aporte valor

Cuando el producto local esté suficientemente consolidado, se podrá evaluar una segunda etapa de expansión. No se activa automáticamente por completar una fase.

Posibles componentes a evaluar:

- Hosting o almacenamiento de paquetes de conocimiento.
- Catálogo remoto y endpoint HTTPS para actualizaciones automáticas.
- Base de datos central, únicamente si aparece una necesidad real que no pueda resolverse con el modelo local y los paquetes.
- Dominio propio, observabilidad, copias de seguridad y operación de servicios.
- Servicios de IA externos, solo como función opcional y con costos transparentes.
- Infraestructura para colaboración, múltiples usuarios o distribución a mayor escala.

La expansión debe diseñarse de forma incremental. No se contratará una base de datos remota solo porque exista un servidor de distribución: **un repositorio estático de paquetes puede ser suficiente para una primera distribución remota**, dependiendo de los requisitos que se definan entonces.

Antes de aprobar cualquier gasto se deberá preparar una propuesta que indique:

- Necesidad concreta que resuelve y por qué la solución local ya no basta.
- Opciones gratuitas y de pago vigentes.
- Costos mensuales y anuales, límites de uso, almacenamiento, transferencia e impuestos aplicables.
- Riesgos de dependencia del proveedor, disponibilidad, seguridad y mantenimiento.
- Procedimiento de migración, exportación y recuperación si se deja de pagar.
- Aprobación explícita del propietario.

No se debe introducir un costo recurrente por comodidad técnica si no existe una necesidad de producto demostrable.

## 6. Condiciones para considerar la expansión

La evaluación de inversión podrá comenzar cuando se cumplan las condiciones que el propietario considere necesarias, por ejemplo:

- La versión local tiene un flujo de aprendizaje completo y validado.
- La persistencia, los backups y la recuperación funcionan.
- La distribución manual de paquetes está probada o se ha documentado por qué ya no es suficiente.
- Existe una necesidad concreta de publicar actualizaciones a varios usuarios o instalaciones.
- Se conocen los requisitos de seguridad y operación del servicio remoto.
- Hay una estimación de costos y un presupuesto aceptado.

Cumplir estas condiciones habilita una evaluación; **no obliga a invertir**.

## 7. Reglas para futuras intervenciones de desarrollo

Cualquier persona o agente que continúe el proyecto deberá:

1. Leer este documento y el plan maestro antes de proponer infraestructura.
2. Mantener la aplicación local como producto funcional independiente.
3. No agregar servicios de pago, secretos de proveedor ni dependencias cloud obligatorias sin aprobación explícita.
4. Mantener separadas la base de datos local del estudiante y la distribución remota opcional del conocimiento.
5. No activar sincronización remota con endpoints o claves de prueba en una compilación de producción.
6. Registrar en la documentación cualquier cambio que altere esta estrategia.
7. Informar de forma transparente qué funciones requieren conexión y cuáles siguen disponibles offline.

## 8. Resumen de la decisión

**Primero terminamos CodeGuard Pro como aplicación local, offline-first y sin gastos de infraestructura. Después, si el proyecto crece y existe una razón clara, evaluaremos invertir para expandirlo. Por ahora no se contrata ni se paga ningún servicio externo.**
