# Auditoría de continuidad académica ASCENSO 3.1

**Fecha:** 2026-11-19  
**Rama examinada:** `content/ascenso-stage-0-learning-method`  
**Base técnica:** `release/1.0.0`  
**Estado:** diagnóstico documental; no equivale a aprobación editorial ni a pruebas de runtime.

## 1. Alcance y precisión del estado

La rama contiene 33 documentos de etapa (0–32), además de cuatro documentos de módulos de la etapa 0, cinco documentos de módulos de la etapa 1 y dos estándares editoriales. Esto representa una **primera cobertura documental de las 33 etapas**, no 1.946 lecciones terminadas. El roadmap oficial contiene 33 etapas, 212 módulos y 1.946 títulos de lección. Los documentos son guías de desarrollo de etapa/módulo. Se incorporó granularidad de encabezados por lección para las etapas 1–32 y se ampliaron sus guías, pero el nivel de desarrollo de cada lección es variable: todavía se requiere completar teoría, ejemplos, ejercicios, referencias trazables y evidencia de verificación según el estándar editorial. La existencia de un encabezado no equivale a una lección completa.

No se deben comunicar las 33 etapas como «curso completo», «lecciones completas» ni «contenido listo para publicar».

## 2. Hallazgos confirmados

### 2.1 Contrato real de importación

La inspección de `apps/roadmaps/content_import.py` en `release/1.0.0` confirma que el importador no acepta Markdown directamente. Acepta documentos JSON v1 con estas claves:

- Documento: `schema_version`, `resumen_cambios`, `snapshot`, `fuentes`.
- Snapshot: `esquema_version`, `leccion`, `contenido`, `ejemplos`, `ejercicios`.
- Identidad de lección: UUID canónico, título, descripción y tipo que deben coincidir exactamente con una lección ya existente.
- Ejemplos y ejercicios: cada elemento requiere sus propios UUID canónicos y debe pertenecer a la lección indicada.
- Fuentes: entre 1 y 20 referencias registradas, activas y asociadas a la versión.

El importador valida el UUID contra la base de datos, verifica identidad curricular, comprueba pertenencia de ejemplos/ejercicios y valida las fuentes. No crea ni inventa lecciones, UUID curriculares, ejemplos o ejercicios.

### 2.2 Flujo editorial real

Los comandos existentes establecen un flujo explícito:

1. Registrar fuente con `registrar_fuente_conocimiento`.
2. Revisar licencia y alcance con `revisar_licencia_fuente`.
3. Validar un lote JSON sin escrituras con `validar_paquete_contenido`.
4. Crear borradores con `importar_paquete_contenido --confirmar --usuario EDITOR`.
5. Enviar, aprobar y publicar mediante `gestionar_version_leccion` y sus transiciones.

La importación crea borradores, no publicaciones. La aprobación y publicación son transiciones separadas con actor editorial. No se debe saltar este flujo.

### 2.3 Límite de la inspección

La revisión se hizo leyendo código de la rama base a través de GitHub. No se ejecutó Django, no se consultó la SQLite real de una instalación de CodeGuard Pro y no se crearon registros. Por ello, todavía no se dispone de un inventario operativo de UUID de las 1.946 lecciones ni de las fuentes ya registradas en la base de datos del usuario.

### 2.4 Excepción curricular documentada

La etapa 25 del documento maestro no contiene un objetivo formal en el campo `objetivo`. El inventario `docs/ROADMAP_ASCENSO_INVENTARIO.md` ya registra esta ausencia. No se debe inventar un objetivo ni escribirlo en el JSON curricular como si fuera oficial. La guía académica puede explicar el propósito a partir de sus módulos, dejando claro que es una interpretación didáctica propuesta y pendiente de aprobación.

### 2.5 Regla audiovisual

La política se corrigió en los documentos editoriales: el audio hablado debe ser español y la relación temática debe ser directa. Un video hablado en inglés no se acepta aunque tenga subtítulos o doblaje automático. Cuando no se haya comprobado el audio, el recurso es candidato, no aprobado.

## 3. Riesgos y trabajo pendiente

| Riesgo | Acción requerida antes de publicación |
|---|---|
| Las guías y encabezados granulares no equivalen a 1.946 lecciones desarrolladas | Completar cada lección con teoría, ejemplos, ejercicios, referencias trazables y evidencia según la plantilla editorial. |
| No se dispone del UUID de cada lección en este entorno | Exportar un manifiesto de UUID desde la instalación/DB de destino; cotejar título, etapa y módulo. |
| Los ejemplos/ejercicios también requieren claves estables existentes | Inventariar sus UUID reales o acordar, mediante el flujo de ingeniería correspondiente, cómo se crean antes de importar. |
| Fuentes no registradas/licencia sin revisar | Registrar fuentes reales, verificar edición/licencia/alcance y asociar IDs existentes. |
| Los Markdown no son el formato del importador | Crear un conversor Markdown/autoría → JSON v1 con pruebas de contrato; nunca inferir UUID. |
| Videos no reproducidos | No aprobar hasta verificar audio español, tema, enlace y actividad asociada. |
| Código/laboratorios no ejecutados | Mantener estado «no verificado» hasta probar entorno, instrucciones y resultado. |
| Etapa 25 sin objetivo oficial | Mantenerlo como vacío/propuesta, sin alterar el documento maestro ni el JSON. |

## 4. Próxima secuencia técnica segura

1. Crear un manifiesto de solo lectura desde la base de datos destino con UUID, etapa, módulo, título, tipo y claves de ejemplos/ejercicios.
2. Compararlo con el JSON oficial y detectar faltantes, duplicados y diferencias exactas de título.
3. Completar lecciones individuales con teoría, explicación sencilla, ejemplos, ejercicios, referencias y evidencia de verificación.
4. Registrar y revisar fuentes mediante los comandos editoriales existentes.
5. Convertir un lote piloto pequeño a JSON v1, usando exclusivamente UUID reales y fuentes registradas.
6. Ejecutar primero `validar_paquete_contenido`; no usar `--confirmar` hasta que el reporte sea limpio y el editor responsable esté identificado.
7. Importar solo borradores. Revisión, aprobación y publicación deben permanecer como actos editoriales separados.
8. Añadir pruebas de conversión, fidelidad curricular, trazabilidad y regresión.

## 5. Estado de esta auditoría

- Cobertura documental de etapas: 33/33.
- Lecciones curriculares redactadas y listas para importar: no determinado; no afirmar que sean 1.946.
- UUIDs de destino inventariados desde una base SQLite real: pendiente.
- Paquete JSON v1 generado y validado: pendiente.
- Contenido importado a SQLite: no.
- Contenido aprobado/publicado: no.
- Documento maestro y JSON curricular modificados por esta rama: no.

La prioridad siguiente es obtener un manifiesto curricular real y desarrollar contenido a nivel de lección, no declarar completado el roadmap por la mera existencia de 33 archivos.

## 6. Exportador de manifiesto de solo lectura añadido

Se añadió `apps.roadmaps.management.commands.exportar_manifiesto_academico` junto con pruebas Django en `apps/roadmaps/tests/test_exportar_manifiesto_academico.py`.

El comando:
- Selecciona el roadmap por nombre y edición exactos.
- Exporta jerarquía de etapas, módulos y lecciones.
- Incluye los UUID estables existentes de lecciones, ejemplos y ejercicios.
- Puede incluir el catálogo de fuentes registradas y su estado de licencia.
- No exporta progreso, cuentas, contraseñas ni datos de usuarios.
- No crea ni actualiza registros de la base de datos.
- Por defecto imprime JSON en stdout; con `--salida` crea un archivo nuevo y se niega a sobrescribir uno existente.

Ejemplo de ejecución en una instalación de desarrollo o una copia controlada de la base de datos:

```bash
python manage.py exportar_manifiesto_academico \
  --nombre "NOMBRE EXACTO DEL ROADMAP EN LA INSTALACIÓN" \
  --edicion "3.1" \
  --salida ./var/ascenso-manifest.json \
  --incluir-fuentes
```

El directorio `./var` debe existir y el archivo de salida no debe existir. Se recomienda ejecutar primero en una copia de la base de datos y almacenar el manifiesto en una ubicación privada, pues contiene identificadores internos de contenido. No subir ese manifiesto con UUID de una instalación real a un repositorio público.

**Verificación automatizada:** el workflow de GitHub Actions `CodeGuard Pro CI` terminó correctamente para el commit `510d0f8bbcaf560ce8027c8298da74fcd22baa03`: validación de sintaxis Python, `manage.py check`, comprobación de migraciones, suite Django, pruebas IPC de Electron y compilación/smoke test del servidor PyInstaller. El paquete Windows fue omitido por las condiciones del workflow. Los commits posteriores en esta rama modificaron únicamente documentación. **Pendiente de entorno real:** todavía no se ha ejecutado el exportador contra la base de datos local del usuario ni se ha generado el manifiesto real; esa comprobación requiere acceso a la instalación y su base de datos.


## Continuidad de las etapas 1–32 — 2026-11-24

Se consolidó la clasificación documental de las etapas 1–32 como **BASE DE TRABAJO ACTIVA**. Se actualizaron sus metadatos de estado para que la documentación sea la referencia operativa del desarrollo, sin presentarla como aprobada, revisada independientemente, validada en laboratorios ni publicada.

Se añadió [la guía de continuidad académica de las etapas 1–32](ASCENSO_3_1_GUIA_CONTINUIDAD_ETAPAS_01_32.md), construida a partir del inventario curricular existente. La guía resume la progresión por bloques, enumera los módulos oficiales y sus cantidades nominales de lecciones, conserva los proyectos del roadmap y explica cómo conectar los proyectos a lo largo del recorrido.

### Inventario confirmado

- Etapas 1–32: 32 etapas, 208 módulos y 1.916 lecciones nominales.
- Etapa 0: 4 módulos y 30 lecciones nominales.
- Total ASCENSO 3.1: 33 etapas, 212 módulos y 1.946 lecciones nominales.
- La etapa 25 conserva su objetivo oficial vacío; no se infirió ni se completó.
- No se modificó `apps/roadmaps/data/ascenso_3_1.json`, no se crearon UUID y no se importó contenido.

### Alcance de la actualización

La clasificación como base activa establece qué documentación debe utilizarse para continuar el trabajo. No significa que las 1.916 lecciones nominales de las etapas 1–32 estén desarrolladas individualmente con el mismo nivel de detalle, ni que todos los ejemplos, laboratorios, videos o proyectos se hayan ejecutado. El desarrollo granular por lección continúa como trabajo pendiente y se realizará sin alterar el inventario oficial.

La secuencia de bloques de la guía es una organización didáctica para facilitar continuidad; no introduce prerrequisitos curriculares obligatorios nuevos ni modifica los siete prerrequisitos registrados.


### Primera expansión granular — etapa 1

Se alinearon los módulos 1.1 y 1.2 con la granularidad exacta de sus lecciones en el roadmap, separando temas que antes aparecían combinados bajo un mismo encabezado:

- **Módulo 1.1 — Hardware:** 16 encabezados de lección, desde CPU y ALU hasta fuente de alimentación y periféricos.
- **Módulo 1.2 — Representación de información:** 9 encabezados de lección, separando sistemas binario, decimal y hexadecimal, y ASCII, Unicode y UTF-8.

La separación conserva las explicaciones y ejemplos existentes y mejora la correspondencia entre identificador curricular y contenido. No se afirma ejecución del laboratorio de hardware ni del codificador. Los módulos 1.3, 1.4 y 1.5 ya presentan 8, 7 y 6 encabezados temáticos respectivamente, en correspondencia con las cantidades nominales del roadmap.


### Expansión granular — etapa 2

El documento de la etapa 2 se reorganizó para que cada uno de sus 39 temas nominales tenga un encabezado con identificador curricular exacto (2.1.1–2.5.7). Se separaron las entradas, el procesamiento y las salidas; pseudocódigo y diagramas; contadores y acumuladores; proporciones y porcentajes; relaciones y grafos; y los conceptos lógicos que antes compartían un encabezado. El orden de las lecciones de algoritmos se ajustó al roadmap.

Se conservaron las explicaciones, ejemplos, proyecto y ejercicios existentes. Esta alineación mejora la navegación y trazabilidad; no representa una evaluación formal ni ejecución del proyecto.


### Expansión granular — etapa 3

El documento de programación inicial con Java quedó alineado con las 48 lecciones nominales del roadmap mediante encabezados curriculares individuales: 13 de fundamentos, 9 de control de flujo, 7 de métodos, 7 de manejo de información, 6 de manejo de errores y 6 de archivos. Se separaron conceptos que antes compartían encabezado (JDK/JVM/JRE, compilación/ejecución, sintaxis/semántica, variables/constantes, ramas de control, parámetros/argumentos, entrada/Scanner, throw/throws y lectura/escritura/directorios/rutas).

Se conservaron los ejemplos y el proyecto de inventario, y se mantuvo explícito que los comandos y ejemplos no se han compilado ni ejecutado en esta sesión.


### Expansión granular — etapa 4

El documento de POO y paradigmas quedó alineado con sus 33 lecciones nominales: 12 de POO, 5 de relaciones, 5 de conceptos de diseño, 5 de paradigmas y 6 de UML. Se separaron clases, objetos e instancias; atributos y métodos; y los elementos de UML para clases, objetos, relaciones, herencia, interfaces y secuencia. Se conservaron el ejemplo de dominio de biblioteca, el proyecto y sus entregables.


### Expansión granular — etapa 5

El documento de Git, GitHub, terminal y modularidad quedó alineado con sus 42 lecciones nominales: 17 de Git, 9 de GitHub, 7 de terminal y 9 de modularidad. Se separaron las áreas de Git (repositorio, working directory, staging, operaciones de sincronización e historial), comandos de terminal, redirecciones/pipes y módulos/imports/exports/namespaces/paquetes. El orden de las operaciones Git se ajustó al roadmap. Se mantuvieron las advertencias para operaciones destructivas, secretos y publicación de repositorios.


### Expansión granular — etapa 6

La etapa 6 quedó alineada con las 57 lecciones del roadmap: 9 de estructuras lineales, 7 asociativas, 7 de árboles, 7 de grafos, 12 de algoritmos, 7 técnicas y 8 de complejidad. Se separaron estructuras antes agrupadas (listas simples/dobles/circulares, colas/deques, mapas/conjuntos), tipos de grafos, algoritmos de búsqueda/ordenamiento/caminos mínimos/árboles de expansión, técnicas y notaciones de complejidad. Se mantuvo el proyecto de biblioteca de estructuras en Java y se precisaron supuestos de complejidad y aplicabilidad de algoritmos. No se afirma compilación ni ejecución de implementaciones.


### Expansión granular — etapa 7

La etapa 7 quedó alineada con 84 lecciones oficiales: 14 de fundamentos de sistemas operativos, 17 de Linux, 20 comandos de administración Linux, 12 de Bash, 12 de Windows y 9 de virtualización. Se separaron conceptos de kernel/espacios de ejecución, procesos/hilos/planificador, llamadas al sistema/drivers, elementos de administración Linux, comandos individuales, componentes de Bash, administración de Windows y modos de virtualización/red. Se conservaron el proyecto de servidores virtuales Ubuntu y Windows Server y las advertencias de seguridad para comandos destructivos, privilegios y redes expuestas. Las prácticas siguen siendo propuestas; no se declara ejecución en VMs reales.


### Expansión granular — etapa 8

La etapa 8 quedó alineada con 81 lecciones oficiales: 13 de fundamentos de redes, 9 de modelos de comunicación, 13 de direccionamiento, 16 protocolos, 10 de routing/switching, 9 de seguridad y 11 herramientas. Se separaron los tipos de redes y equipos, capas y unidades de datos, elementos de direccionamiento, protocolos individuales, conceptos de rutas/VLAN/subredes, controles de seguridad y herramientas de diagnóstico. Se mantuvieron las restricciones para capturas y escaneos: únicamente laboratorios propios o sistemas con autorización expresa. El proyecto de red virtual continúa como práctica propuesta, no como laboratorio ejecutado.


### Expansión granular — etapa 9

La etapa 9 quedó alineada con 81 lecciones oficiales: 10 de fundamentos, 11 de modelado, 9 de MySQL, 19 de SQL, 9 de diseño y normalización, 15 de bases de datos avanzadas y 8 de PostgreSQL. Se separaron entidades, atributos, relaciones, cardinalidades, claves, restricciones y los modelos conceptual/lógico/físico; también se identificaron individualmente los comandos SQL y los temas de índices, transacciones, concurrencia y optimización. Se conservaron el proyecto de base de datos de ventas, los ejemplos y las advertencias sobre credenciales, operaciones destructivas y diferencias entre motores. Los scripts y el proyecto no se ejecutaron contra instancias reales de MySQL o PostgreSQL en esta sesión.


### Expansión granular — etapa 10

La etapa 10 quedó alineada con 38 lecciones oficiales: 8 de fundamentos NoSQL, 14 de MongoDB, 11 de Redis y 5 de otras arquitecturas de almacenamiento. Se individualizaron CAP, consistencia, disponibilidad, escalabilidad, CRUD, filtros, índices, aggregation pipeline, embedding/referencing, replicación, sharding, estructuras Redis, TTL, caché, sesiones, Pub/Sub y rate limiting. Se conservó el proyecto híbrido MySQL/MongoDB/Redis y se reforzó la distinción entre fuente de verdad, caché y replicación. Los comandos y laboratorios no se ejecutaron contra instancias reales en esta sesión.


### Expansión granular — etapas 11 a 13

Se incorporó un desglose por encabezado para las lecciones oficiales de las etapas 11–13, conservando el orden y los títulos del JSON curricular:

- **Etapa 11 — HTML y CSS:** 60 lecciones (21 HTML, 8 accesibilidad, 17 CSS, 8 diseño de interfaces y 6 SEO).
- **Etapa 12 — JavaScript, TypeScript y frameworks frontend:** 89 lecciones (19 JavaScript, 9 DOM, 10 asincronía, 7 Web APIs, 11 TypeScript, 16 React, 10 Next.js y 7 herramientas).
- **Etapa 13 — Internet, HTTP, APIs y comunicación entre sistemas:** 63 lecciones (13 arquitectura web, 11 HTTP, 14 APIs, 10 consumo, 5 estilos de comunicación, 6 seguridad y 4 documentación).

Los documentos conservan explicaciones temáticas, proyectos, autoevaluaciones y referencias técnicas; el desglose facilita navegación y correspondencia curricular. Las frases de propósito asociadas a cada encabezado son guías de estudio, no resultados de evaluación. No se ejecutaron navegadores de prueba, compilaciones frontend, servidores, APIs ni laboratorios de seguridad en esta sesión. Las tres etapas permanecen como base de trabajo activa, sin aprobación ni publicación.


### Expansión granular — etapas 14 a 16

Se incorporó el desglose individual de las lecciones oficiales de las etapas 14–16:

- **Etapa 14 — Backend I: Java y Spring Boot:** 58 lecciones distribuidas en arquitectura backend, Spring Framework, Spring Boot, persistencia, seguridad, backend avanzado y construcción/dependencias.
- **Etapa 15 — Backend II: Node.js y NestJS:** 53 lecciones distribuidas en Node.js, Express.js, NestJS, persistencia, seguridad y temas avanzados.
- **Etapa 16 — Backend III: PHP, Laravel y .NET:** 46 lecciones distribuidas en PHP, Laravel, C#/.NET y ASP.NET Core.

Los encabezados siguen los títulos y el orden del roadmap oficial y se apoyan en las guías técnicas y proyectos existentes. Las frases de propósito son orientaciones de estudio, no evidencias de dominio. No se ejecutaron servidores, migraciones, pruebas automatizadas ni laboratorios de autenticación en esta sesión. Las etapas permanecen como base de trabajo activa, sin aprobación ni publicación.


### Expansión granular — etapas 17 a 19

Se incorporó el desglose individual de las lecciones oficiales de las etapas 17–19:

- **Etapa 17 — Testing, aseguramiento y calidad del software:** 61 lecciones en fundamentos, testing funcional y de usuario, rendimiento, técnicas, metodologías, herramientas, análisis y modelos de calidad.
- **Etapa 18 — Arquitectura, diseño y planeación de software:** 100 lecciones en requerimientos, metodologías ágiles, documentación, diagramas, principios, patrones GoF, arquitecturas, diseño de sistemas y modelado de dominios.
- **Etapa 19 — DevOps, Docker, CI/CD y servidores:** 67 lecciones en fundamentos DevOps, Docker, servidores, Nginx, CI/CD, cloud, proveedores, Kubernetes y Terraform.

Los títulos y su secuencia corresponden al roadmap oficial. En la etapa 18 se preservan como entradas curriculares los rótulos de familias de patrones (creacionales, estructurales y de comportamiento) presentes en el JSON. No se ejecutaron suites de pruebas, pipelines, despliegues, clústeres ni infraestructura cloud en esta sesión. Las etapas permanecen como base de trabajo activa, sin aprobación ni publicación.


### Expansión granular — etapas 20 a 22

Se incorporó el desglose de las entradas curriculares de las etapas 20–22:

- **Etapa 20 — Desarrollo seguro de software (AppSec):** 57 entradas en fundamentos, seguridad web, OWASP Top 10, autenticación/autorización, seguridad de APIs e infraestructura.
- **Etapa 21 — Fundamentos de ciberseguridad, gestión de riesgos y ética:** 82 entradas en panorama de seguridad, principios, conceptos, gestión de riesgos, amenazas, marcos, ética/legislación e IAM.
- **Etapa 22 — Laboratorio de ciberseguridad, hardening y administración segura:** 58 entradas en virtualización, Linux, hardening Linux/Windows, redes y entornos de laboratorio.

Se conservaron las entradas textuales del roadmap, incluidas las notas que figuran dentro de algunas listas de lecciones; no se alteró su fuente curricular. Toda práctica ofensiva o de validación se mantiene limitada a entornos propios, aislados y autorizados. No se desplegaron máquinas virtuales, no se ejecutaron herramientas ni se realizaron pruebas contra sistemas externos. Las etapas permanecen como base de trabajo activa, sin aprobación ni publicación.


### Expansión granular — etapas 23 a 25

Se incorporó el desglose de las entradas oficiales de las etapas 23–25:

- **Etapa 23 — Reconocimiento, OSINT y gestión de vulnerabilidades:** 58 entradas en reconocimiento, OSINT, herramientas, identificación de activos, escaneo/enumeración y gestión de vulnerabilidades.
- **Etapa 24 — Pentesting de redes y sistemas:** 47 entradas en fundamentos, evaluación de sistemas, Metasploit, seguridad de credenciales y post-explotación.
- **Etapa 25 — Seguridad de aplicaciones web y APIs:** 50 entradas en arquitectura web, vulnerabilidades, OWASP, Burp Suite, seguridad de APIs y herramientas.

Se mantuvieron las restricciones de autorización, alcance, aislamiento y cierre responsable para cualquier práctica de reconocimiento o pentesting. El campo oficial `objetivo` de la etapa 25 sigue vacío: no se completó ni se sustituyó por una formulación inventada. No se escanearon activos, no se ejecutaron herramientas de explotación y no se probaron sistemas externos. Las etapas permanecen como base de trabajo activa, sin aprobación ni publicación.


### Expansión granular — etapas 26 a 28

Se incorporó el desglose individual de las entradas oficiales de las etapas 26–28:

- **Etapa 26 — Active Directory y seguridad empresarial Windows:** 39 entradas en Active Directory, protocolos, administración, seguridad, herramientas y hardening.
- **Etapa 27 — Blue Team, SOC, SIEM e ingeniería de detección:** 58 entradas en defensa, SOC, logs, indicadores, IDS/IPS, herramientas, SIEM e ingeniería de detección.
- **Etapa 28 — Threat Hunting, respuesta a incidentes y forense digital:** 46 entradas en hunting, inteligencia de amenazas, respuesta, DFIR, herramientas y estándares.

Se mantuvo el enfoque defensivo y la necesidad de preservar evidencia, controlar accesos y trabajar con autorización. No se conectó a dominios Active Directory, no se instalaron SIEM/IDS, no se procesaron imágenes forenses ni se ejecutaron investigaciones reales. Las etapas permanecen como base de trabajo activa, sin aprobación ni publicación.


### Expansión granular — etapas 29 a 32

Se incorporó el desglose individual de las entradas oficiales de las etapas 29–32:

- **Etapa 29 — Cloud Security, DevSecOps y Supply Chain Security:** 71 entradas en seguridad cloud, AWS, Azure, Google Cloud, Docker, Kubernetes, supply chain y DevSecOps.
- **Etapa 30 — Inteligencia artificial, automatización y seguridad avanzada:** 75 entradas en IA para seguridad, LLM Security, AI Red Teaming, automatización Python, automatización de seguridad, threat intelligence, criptografía y criptografía poscuántica.
- **Etapa 31 — Ciberseguridad de bajo nivel, análisis de malware e ingeniería inversa:** 75 entradas en C, C++, arquitectura de bajo nivel, seguridad de memoria, Assembly, ingeniería inversa, malware y herramientas.
- **Etapa 32 — Proyecto profesional, portafolio y preparación laboral:** 54 entradas en portafolio, proyectos full stack, infraestructura, seguridad, colaboración y preparación laboral.

Las prácticas de cloud y DevSecOps se limitan a cuentas y entornos autorizados; las pruebas de IA se limitan a sistemas propios/autorizados y sin exponer secretos; el análisis de malware se limita a muestras controladas y entornos aislados. Los proyectos profesionales deben reflejar contribuciones y resultados reales. No se desplegó infraestructura cloud, no se ejecutaron pruebas de IA, no se analizaron muestras de malware y no se realizaron evaluaciones laborales. Las etapas permanecen como base de trabajo activa, sin aprobación ni publicación.


## 7. Cierre de la expansión granular de etapas 1–32 — 2026-11-24

Se completó la pasada de organización granular de las 32 etapas posteriores a la etapa 0. Las etapas 11–32 cuentan con encabezados individuales para cada entrada de lección del roadmap; se verificó que los conteos por etapa coinciden con las listas oficiales de sus módulos. Las etapas 1–10 ya habían recibido desarrollo y expansión en la continuidad previa.

Esta finalización se refiere a la cobertura documental y a la correspondencia de encabezados, no a la redacción exhaustiva de 1.916 lecciones completas. El contenido de los encabezados agregados en esta pasada incluye orientaciones breves de estudio; aún debe ampliarse con explicaciones completas, ejemplos, ejercicios, fuentes verificadas y evidencia práctica antes de importación, aprobación o publicación.

- Etapas documentadas: 33/33 (0–32).
- Etapas posteriores a la etapa 0 con trabajo de continuidad: 32/32.
- Roadmap oficial: 33 etapas, 212 módulos y 1.946 lecciones nominales.
- Conteos de encabezados de etapas 11–32: coinciden con el número de entradas del roadmap para cada etapa.
- JSON curricular: sin cambios; SHA del archivo en la rama y en `release/1.0.0`: `43b6350dd911350c2b5f68c3d3de3dea4696f878`.
- Objetivo de etapa 25: permanece vacío.
- Importación a SQLite, aprobación editorial y publicación: no realizadas.
- Laboratorios de programación, bases de datos, redes, seguridad, cloud y forense: no ejecutados en esta pasada.

La siguiente fase académica es desarrollar las lecciones individuales a profundidad y reunir evidencias verificables, conservando el flujo editorial y el manifiesto real de UUID como condiciones previas a cualquier importación.


## Desarrollo profundo y revisión editorial interna — etapas 1 a 10 — 2026-11-24

Se realizó una pasada de revisión editorial documental sobre las etapas 1–10 y se registraron hallazgos en los documentos de cada módulo. La correspondencia de encabezados individuales con el roadmap se cotejó por módulo: **549/549 entradas** de lección coinciden con los conteos oficiales de estas diez etapas.

### Ajustes editoriales aplicados

- **Etapa 1:** desarrollo documental por lección completado en esta sesión para los 5 módulos (46/46 lecciones) con estructura didáctica por lección (identificación, propósito, prerrequisitos, resultados, desarrollo, ejemplo, práctica guiada, actividad independiente, criterios, errores, evaluación y referencias). Estado: **DESARROLLADO**; pendiente validación editorial externa, verificación técnica y ejecución de ejemplos.
- **Etapa 2:** desarrollo documental por lección completado en esta sesión para los 5 módulos (39/39 lecciones) con la misma estructura por lección; el documento monolítico fue reemplazado por índice y módulos 2.1-2.5. Estado: **DESARROLLADO**; pendiente validación editorial externa, verificación técnica y ejecución de ejemplos.
- **Etapa 3:** revisión de las 48 entradas; se declaró JDK 21 como línea base para reproducibilidad y se documentaron las APIs que requieren Java 11 o posterior.
- **Etapa 4:** revisión de POO, relaciones, diseño, paradigmas y UML; se alineó la compatibilidad de ejemplos con JDK 21.
- **Etapa 5:** se ordenó la secuencia de Git según el roadmap, se corrigió puntuación y se reforzaron las precauciones para comandos destructivos, ramas y secretos.
- **Etapa 6:** se eliminó la repetición no numerada de Tries y se revisaron algoritmos y estructuras.
- **Etapa 7:** se ordenaron los temas de fundamentos/Linux y se precisó la definición de root, separándola de permisos y sudo.
- **Etapa 8:** se ordenó el módulo de seguridad de redes según la secuencia oficial.
- **Etapas 9 y 10:** revisión de cobertura de SQL relacional y NoSQL; se documentaron las pruebas prácticas pendientes y el solapamiento de síntesis en etapa 10.

### Estado de validación

La revisión realizada es **interna y documental**: confirma correspondencia curricular, consistencia de estructura y aplicación de correcciones editoriales concretas. No constituye aprobación académica externa ni validación funcional. No se ejecutaron compilaciones Java, ejercicios algorítmicos, comandos Git/terminal, máquinas virtuales, capturas de red, ni instancias MySQL, PostgreSQL, MongoDB o Redis. Las referencias deben recibir cotejo bibliográfico final y los ejemplos/laboratorios requieren ejecución reproducible antes de aprobar módulos.

Los módulos de etapas 1–10 siguen en **BASE DE TRABAJO ACTIVA**. No se modificó el roadmap ni se declara aprobación o publicación.


## Desarrollo profundo individual — etapas 11 a 13 — 2026-11-24

Se reemplazaron las 212 descripciones genéricas agregadas durante la pasada de granularización por explicaciones individualizadas y específicas para cada lección oficial:

- **Etapa 11:** 60/60 lecciones, HTML, accesibilidad, CSS, diseño de interfaces y SEO.
- **Etapa 12:** 89/89 lecciones, JavaScript, DOM, asincronía, Web APIs, TypeScript, React, Next.js y herramientas.
- **Etapa 13:** 63/63 lecciones, arquitectura web, HTTP, APIs, consumo, estilos de comunicación, seguridad y documentación.

Cada apartado incluye explicación técnica y límites/decisiones de uso; los contenidos se articulan con las guías principales, ejemplos, proyectos y ejercicios ya presentes. Se reforzaron riesgos de XSS y almacenamiento del navegador, reglas de Hooks, exposición de variables de cliente, seguridad de tokens, CORS, XML/XXE, serialización, autorización y protección de secretos.

**Validación interna:** se cotejaron los encabezados contra el roadmap y se comprobó que no permanecieran los textos genéricos de relleno en las 212 entradas. Pendiente: fijar versiones concretas de runtime/frameworks, ejecutar pruebas de frontend, accesibilidad y APIs en entornos controlados y obtener segunda revisión académica. No se declara despliegue, certificación WCAG ni aprobación externa.


## Desarrollo profundo individual — etapas 14 a 16 — 2026-11-24

Se desarrollaron individualmente las 157 entradas oficiales de las etapas 14–16:

- **Etapa 14 — Java y Spring Boot:** 58/58 lecciones.
- **Etapa 15 — Node.js y NestJS:** 53/53 lecciones.
- **Etapa 16 — PHP, Laravel y .NET:** 46/46 lecciones.

Se sustituyeron las orientaciones genéricas por explicaciones específicas con función, decisiones de arquitectura, límites, riesgos y aplicación técnica. Se reforzaron inyección de dependencias, DTOs, validación, persistencia, migraciones, autorización por recurso, secretos, OAuth/OIDC/JWT, procesamiento asíncrono, idempotencia, dependencias y pruebas.

**Validación interna:** se cotejaron encabezados y cantidad de entradas con el JSON curricular y se comprobó que no quedaran placeholders genéricos en los documentos de las tres etapas. Pendiente: fijar versiones exactas de runtimes/frameworks/ORMs, compilar, ejecutar pruebas, migraciones e integración de seguridad en laboratorios aislados. La revisión es documental y no equivale a aprobación externa.


## Desarrollo profundo individual — etapas 17 a 19 — 2026-11-24

Se desarrollaron individualmente las 228 entradas oficiales de las etapas 17–19:

- **Etapa 17 — Testing, aseguramiento y calidad:** 61/61 lecciones.
- **Etapa 18 — Arquitectura, diseño y planeación:** 100/100 lecciones.
- **Etapa 19 — DevOps, Docker, CI/CD y servidores:** 67/67 lecciones.

Se sustituyeron las orientaciones genéricas por explicaciones específicas y se añadieron límites de uso, criterios técnicos y riesgos. En 18.6 se preservan «Creacionales», «Estructurales» y «Comportamiento» porque son entradas explícitas del roadmap, explicadas como rótulos de familia y no como patrones individuales.

**Validación interna:** conteos cotejados con el JSON y ausencia de placeholders genéricos comprobada. Pendiente: ejecutar suites de testing, pruebas de carga, diagramas/revisión con stakeholders, builds, pipelines, despliegues y laboratorios cloud/Kubernetes/Terraform aislados. No se declara ejecución ni aprobación académica externa.


## Desarrollo profundo individual — etapas 20 a 22 — 2026-11-24

Se desarrollaron individualmente las 197 entradas oficiales de las etapas 20–22:

- **Etapa 20 — AppSec:** 57/57 lecciones.
- **Etapa 21 — Fundamentos de ciberseguridad, riesgos y ética:** 82/82 lecciones.
- **Etapa 22 — Laboratorio y hardening:** 58/58 lecciones.

Se sustituyeron las orientaciones genéricas por explicaciones específicas y se reforzaron límites de autorización, controles de aplicación, gestión de riesgos, protección de datos, IAM y aislamiento de laboratorios. La referencia a OWASP Top 10:2025 se verificó en el sitio oficial, que identifica 2025 como la versión publicada más reciente al momento de esta revisión. Se añadieron referencias oficiales de Colombia para Ley 1273/2009 y Ley 1581/2012, con advertencia de verificación jurídica vigente.

**Validación interna:** conteos cotejados con el JSON y ausencia de placeholders genéricos comprobada. Pendiente: verificar legislación consolidada y normativa sectorial, ejecutar análisis AppSec/DAST y laboratorios de hardening en entornos aislados autorizados, y obtener segunda revisión especializada. No se ejecutaron pruebas ni se declara aprobación externa.


## Desarrollo profundo individual — etapas 23 a 25 — 2026-11-24

Se desarrollaron individualmente las 155 entradas oficiales de las etapas 23–25:

- **Etapa 23 — Reconocimiento, OSINT y vulnerabilidades:** 58/58 lecciones.
- **Etapa 24 — Pentesting de redes y sistemas:** 47/47 lecciones.
- **Etapa 25 — Seguridad web y APIs:** 50/50 lecciones.

Se sustituyeron las orientaciones genéricas por explicaciones específicas y se reforzaron autorización, alcance, límites de escaneo, protección de evidencias, validación de hallazgos y pruebas no destructivas. Las herramientas de reconocimiento, pentesting y seguridad web se restringen a activos propios o expresamente autorizados, en laboratorios aislados.

**Nota curricular:** el campo oficial `objetivo` de la etapa 25 sigue vacío. No se añadió ni propuso un objetivo alternativo.

**Validación interna:** conteos cotejados con el JSON y ausencia de placeholders genéricos comprobada. Pendiente: verificar versiones/licencias de herramientas y ejecutar prácticas únicamente en laboratorios autorizados con segunda revisión. No se escanearon activos ni se declara aprobación externa.


## Desarrollo profundo individual — etapas 26 a 28 — 2026-11-24

Se desarrollaron individualmente las 143 entradas oficiales de las etapas 26–28:

- **Etapa 26 — Active Directory y seguridad empresarial Windows:** 39/39 lecciones.
- **Etapa 27 — Blue Team, SOC, SIEM e ingeniería de detección:** 58/58 lecciones.
- **Etapa 28 — Threat Hunting, respuesta a incidentes y DFIR:** 46/46 lecciones.

Se sustituyeron las orientaciones genéricas por explicaciones específicas y se reforzaron mínimo privilegio, protección de credenciales, telemetría, triage, validación de detecciones, privacidad, preservación de evidencia y cadena de custodia. La entrada «Herramientas» de 27.7 se explica como rótulo curricular; CSRC se identifica como repositorio NIST, no como estándar único.

**Validación interna:** conteos cotejados con el JSON y ausencia de placeholders genéricos comprobada. Pendiente: validar en dominio ficticio y laboratorios SIEM/DFIR aislados, comprobar versiones de herramientas y obtener segunda revisión especializada. No se conectaron dominios empresariales ni se analizaron incidentes reales.


## Desarrollo profundo individual — etapas 29 a 32 — 2026-11-24

Se desarrollaron individualmente las 275 entradas oficiales de las etapas 29–32:

- **Etapa 29 — Cloud Security, DevSecOps y Supply Chain:** 71/71 lecciones.
- **Etapa 30 — IA, automatización y criptografía avanzada/poscuántica:** 75/75 lecciones.
- **Etapa 31 — Bajo nivel, análisis de malware e ingeniería inversa:** 75/75 lecciones.
- **Etapa 32 — Proyecto profesional, portafolio y preparación laboral:** 54/54 lecciones.

Se sustituyeron orientaciones genéricas por explicaciones específicas. Se reforzaron IAM, responsabilidad compartida, SBOM/procedencia, seguridad de agentes y LLM, gestión de claves y transición poscuántica, seguridad de memoria, análisis aislado de malware y evidencia profesional verificable. Se añadieron fuentes NIST para ML-KEM (FIPS 203), ML-DSA (FIPS 204) y SLH-DSA (FIPS 205).

**Validación interna:** conteos cotejados con el JSON y ausencia de placeholders genéricos comprobada. Pendiente: validar versiones de proveedores/herramientas, ejecutar laboratorios cloud/IA/criptografía/malware solo en entornos autorizados, completar proyectos y recibir segunda revisión técnica/editorial. No se desplegó infraestructura, no se ejecutó malware ni se declara aprobación externa.


## Estado consolidado de desarrollo individual — 2026-11-24

Se completó la primera pasada de desarrollo individual de las **1.916 entradas nominales** correspondientes a las etapas 1–32. El trabajo se distribuye así:

- Etapas 1–10: 549 entradas con desarrollo técnico previo en guías de módulo, revisión documental y correcciones editoriales.
- Etapas 11–32: 1.367 entradas con explicación técnica individualizada, sustituyendo las orientaciones genéricas de la granularización.
- Total: 1.916 entradas de las etapas 1–32, alineadas con el roadmap de 33 etapas/212 módulos/1.946 lecciones.

Se añadieron registros de revisión editorial interna por bloque y se corrigieron duplicaciones, orden de temas, referencias impropias, compatibilidad de entornos, advertencias de seguridad y referencias oficiales seleccionadas. Se comprobó por bloques que los conteos de encabezados de lección coinciden con el currículo y que los textos genéricos de relleno fueron sustituidos.

### Estado real y criterios pendientes

Esta pasada completa la **redacción individual inicial y la revisión editorial documental**, pero no debe confundirse con aprobación académica final. Las lecciones de etapas 11–32 se integran con guías principales, ejemplos/proyectos y explicaciones específicas; aún pueden requerir ampliación adicional de casos resueltos, ejercicios graduados, soluciones comentadas y referencias específicas por lección. La aprobación final exige, como mínimo:

1. cotejo bibliográfico actualizado de todas las fuentes y versiones;
2. ejecución reproducible de ejemplos, proyectos, pruebas y laboratorios;
3. verificación de accesibilidad, seguridad y compatibilidad donde aplique;
4. revisión independiente técnica y pedagógica con criterios de aceptación;
5. evidencias trazables y resolución de hallazgos antes de cualquier importación.

No se ejecutaron pruebas ni laboratorios en esta pasada; no se aprobaron, importaron ni publicaron lecciones. El objetivo oficial de la etapa 25 continúa vacío. El JSON curricular permanece intacto.

## Addendum de sesión — 2026-11-24 (worktree local, agente)

### Contexto

- Trabajo realizado en `content/ascenso-stage-0-learning-method` (worktree separado), después de detectar que la rama remota tenía commits adicionales respecto a la base local inicial. Se hizo rebase sobre `origin/content/ascenso-stage-0-learning-method` y se resolvieron conflictos conservando el contenido más detallado para etapas 1-2.

### Desarrollo realizado en esta sesión

- **Etapa 1 (46 lecciones, módulos 1.1-1.5):** reescritura a nivel lección con estructura didáctica completa por lección: identificación, propósito, conocimientos previos, resultados observables, desarrollo conceptual, ejemplo técnico, práctica guiada, actividad independiente, criterios de aceptación, errores frecuentes, evaluación de comprensión y referencias.
- **Etapa 2 (39 lecciones, módulos 2.1-2.5):** creación de módulos por lección con la misma estructura; el documento monolítico quedó como índice.

### Cobertura honesta de esta sesión

- Lecciones desarrolladas documentalmente por lección en esta sesión: **85** (Etapa 1: 46, Etapa 2: 39).
- Lecciones validadas técnicamente: **0**.
- Lecciones con ejecución de ejemplos: **0**.
- Referencias: incluidas como fuentes candidatas; **no verificadas una por una** por web/fetch en esta sesión.

### Pendientes críticos

- Verificar referencias/URLs y vigencia de todas las lecciones desarrolladas.
- Ejecutar ejemplos de código/labs en entorno controlado y registrar evidencia.
- Revisar coherencia técnica con revisión humana experta.
- Continuar desarrollo por lección de etapas 3-32 según prioridad y estado real de sus documentos.
- Obtener manifiesto UUID real antes de cualquier conversión/importación.

## Addendum final de sesión — 2026-11-24 (continuación)

### Lotes completados en esta sesión

| Etapa | Módulos | Lecciones | Artefactos | Estado |
|---:|---:|---:|---|---|
| 1 | 5 | 46 | módulos 1.1-1.5 reescritos por lección | DESARROLLADO (doc) |
| 2 | 5 | 39 | módulos 2.1-2.5 + índice | DESARROLLADO (doc) |
| 3 | 6 | 48 | módulos 3.1-3.6 + índice | DESARROLLADO (doc) |
| 4 | 5 | 33 | módulos 4.1-4.5 + índice | DESARROLLADO (doc) |
| 5 | 4 | 42 | módulos 5.1-5.4 + índice | DESARROLLADO (doc) |
| 6 | 7 | 57 | módulos 6.1-6.7 + índice | DESARROLLADO (doc) |

**Total desarrollado documentalmente por lección en esta sesión:** 265 lecciones (etapas 1-6).

### Validación

- Conteos de lecciones cotejados contra `apps/roadmaps/data/ascenso_3_1.json`.
- Estructura por lección aplicada (identificación, propósito, prerrequisitos, resultados, desarrollo, ejemplo, práctica, actividad independiente, criterios, errores, evaluación, referencias).
- **No realizado:** ejecución de ejemplos, verificación web exhaustiva de referencias, revisión técnica/ editorial externa, importación JSON v1, aprobación/publicación.

### Limitación de alcance

No fue posible completar en esta sesión el desarrollo profundo y validado de las 1916 lecciones de etapas 1-32. Quedan pendientes 1651 lecciones de etapas 7-32 para desarrollo/revisión por lección con la misma profundidad y evidencia. Los documentos existentes en etapas 7-32 no fueron revalidados uno por uno en esta sesión; el estado consolidado previo del repositorio se conserva, pero no se declara validación final.

### Recomendación de continuación

Continuar por lotes: 7-10 (sistemas/datos), 11-16 (full stack), 17-20 (ingeniería/infra/AppSec), 21-25 (ciberseguridad), 26-32 (especialización/proyecto), con auditoría por lote, verificación de referencias y ejecución de ejemplos en entorno controlado.


## Addendum de profundización didáctica — 2026-11-24 (continuación)

### Lote trabajado: etapas 7–10

Se amplió el desarrollo individual de las lecciones de las etapas 7–10, conservando los títulos, numeración y secuencia del roadmap oficial:

| Etapa | Lecciones | Desarrollo incorporado |
|---:|---:|---|
| 7 — Sistemas operativos | 84 | Explicaciones específicas de kernel, Linux, administración de comandos, Bash, Windows y virtualización; prácticas de laboratorio y evidencias de comprensión. |
| 8 — Redes y protocolos | 81 | Desarrollo específico de redes, modelos, direccionamiento, protocolos, routing/switching, seguridad y herramientas; actividades restringidas a redes propias o autorizadas. |
| 9 — Bases de datos relacionales y SQL | 81 | Desarrollo de fundamentos, modelado, MySQL, categorías y sentencias SQL, normalización, transacciones, índices y PostgreSQL; prácticas de consulta y diseño. |
| 10 — NoSQL y almacenamiento moderno | 38 | Desarrollo de modelos NoSQL, MongoDB, Redis y familias de almacenamiento; actividades de selección, modelado y operaciones de laboratorio. |
| **Total** | **284** | **84 + 81 + 81 + 38** |

### Criterio aplicado

Cada unidad fue ampliada con explicación vinculada al título oficial, una aplicación o práctica pertinente y una evidencia que permite comprobar comprensión. Se corrigieron las secciones vacías o de orientación genérica detectadas en estas etapas. No se modificaron títulos ni la estructura curricular oficial.

### Comprobación documental realizada

- Se volvieron a leer los cuatro archivos desde la rama remota después de los cambios.
- Se contabilizaron 84, 81, 81 y 38 encabezados de lección, respectivamente.
- En los cuatro documentos no se detectaron encabezados de lección vacíos.
- En las etapas 9 y 10 no permaneció la frase de relleno genérica identificada en la revisión inicial.
- No se ejecutaron los comandos, scripts, configuraciones de red, consultas SQL, operaciones MongoDB ni comandos Redis descritos.
- No se verificaron una por una las referencias ni las versiones de herramientas.
- Esta intervención es desarrollo documental y comprobación estructural; no constituye validación técnica por ejecución, revisión independiente ni aprobación editorial final.

### Estado acumulado de profundización

- Etapas 1–6: 265 lecciones desarrolladas documentalmente por OpenCode con estructura didáctica ampliada, según el informe de esa sesión.
- Etapas 7–10: 284 lecciones ampliadas en esta continuación.
- Etapas 1–10: 549 lecciones con desarrollo documental ampliado.
- Etapas 11–32: 1.367 lecciones conservan la primera pasada individual previa; requieren la misma profundización didáctica y revisión de evidencia aplicada a este lote.

Se mantiene pendiente la validación mediante ejecución, la comprobación bibliográfica individual, la revisión técnica experta y la revisión pedagógica independiente. No se importó ni publicó contenido. El objetivo oficial de la etapa 25 permanece vacío y el archivo JSON del roadmap no se modificó.


## Addendum de profundización didáctica — etapas 11–12 — 2026-11-24

### Lote trabajado

Se añadieron prácticas y evidencias de comprensión a las unidades individuales de las etapas 11 y 12, conservando el desarrollo conceptual preexistente:

| Etapa | Lecciones | Ampliación |
|---:|---:|---|
| 11 — HTML y CSS | 60 | Prácticas específicas para estructura HTML, semántica, formularios, multimedia, accesibilidad, CSS, diseño responsivo y fundamentos de SEO. |
| 12 — JavaScript, TypeScript, React y Next.js | 89 | Prácticas para lenguaje, DOM, asincronía, APIs del navegador, tipado, componentes, Hooks, App Router y herramientas de desarrollo. |
| **Total** | **149** | **60 + 89** |

### Comprobación documental

- Se releen los dos archivos desde la rama después de la actualización.
- Se comprueban 60 y 89 encabezados de lección, respectivamente.
- Las 149 lecciones contienen un apartado específico de práctica y evidencia.
- No se detectan encabezados de lección vacíos.
- No se ejecutaron los ejemplos en navegadores, compiladores, proyectos React/Next.js ni pruebas de accesibilidad automatizadas o manuales.
- No se verificaron referencias o versiones de cada herramienta una por una.
- La comprobación es estructural/documental; no equivale a validación técnica de ejecución ni a revisión externa.

### Estado acumulado de esta continuación

- Etapas 7–10: 284 lecciones con desarrollo didáctico ampliado.
- Etapas 11–12: 149 lecciones con prácticas y evidencias incorporadas.
- **Etapas 7–12: 433 lecciones ampliadas.**
- Etapas 1–6: 265 lecciones desarrolladas documentalmente por OpenCode según su informe.
- **Etapas 1–12: 698 lecciones con desarrollo documental ampliado registrado.**
- Etapas 13–32: 1.248 lecciones conservan la primera pasada individual previa y requieren profundización equivalente en prácticas, evidencias y validación.

La redacción ampliada no constituye aprobación. Siguen pendientes ejecución reproducible, verificación bibliográfica individual, revisión técnica experta y revisión pedagógica independiente. No se importó ni publicó contenido.


## Addendum de profundización adicional — módulo 7.1 (2026-11-24)

### Alcance realizado

Se profundizaron las 14 lecciones oficiales del módulo 7.1, «Fundamentos de sistemas operativos», dentro del documento `docs/academic/ascenso-3.1/etapa-07/sistemas-operativos-linux-windows-administracion.md`.

Cada lección incorpora ahora, con contenido específico de su materia:

- propósito y modelo conceptual;
- ejemplo explicado;
- práctica guiada;
- actividad independiente;
- criterios de aceptación;
- errores frecuentes;
- pregunta de comprobación.

También se corrigió el orden y la numeración de los encabezados para que coincidan exactamente con el orden del módulo 7.1 en el roadmap: Kernel, User Space, Kernel Space, Procesos, Hilos, Scheduler, Context Switching, Memoria virtual, Sistema de archivos, Drivers, System Calls, IPC, Concurrencia y Paralelismo.

### Comprobaciones documentales

- Se cotejaron los 14 títulos y su secuencia con `apps/roadmaps/data/ascenso_3_1.json`.
- Se verificó que el documento contiene 14 encabezados de lección del módulo 7.1 y que ninguno está vacío.
- El contenido fue escrito para este módulo; no se aplicó una plantilla genérica intercambiando nombres.
- Se preservaron los apartados posteriores del documento (módulos 7.2–7.6, proyecto, evaluación y referencias).

### Límites de validación

- No se ejecutaron comandos ni prácticas en una máquina Linux real o VM.
- No se ejecutaron pruebas de concurrencia, código, scripts ni mediciones de rendimiento.
- No se hizo verificación web individual de las referencias durante este lote.
- La revisión es documental interna; no equivale a validación técnica por ejecución ni revisión independiente.

### Estado y conteo

Este trabajo profundiza 14 lecciones que ya pertenecían al inventario oficial de la etapa 7; no añade lecciones ni altera el total curricular. Es un sublote del desarrollo de la etapa 7 y no permite marcar la etapa completa como validada. Las etapas 7–32 siguen requiriendo revisión y profundización progresiva conforme al alcance general.

El roadmap JSON no fue modificado. El objetivo oficial de la etapa 25 permanece vacío. No se importó, aprobó ni publicó contenido.


## Addendum de profundización didáctica — etapa 13 — 2026-11-24

Se añadieron prácticas y evidencias específicas a las **63 lecciones** de Internet, HTTP, APIs, herramientas de consumo, protocolos alternativos, seguridad y documentación de APIs.

**Comprobación documental:** el archivo se releyó desde la rama después del cambio; se contaron 63 encabezados de lección, 63 apartados de práctica/evidencia y ningún encabezado vacío. Las prácticas se limitan a servicios propios o autorizados, y los ejemplos de credenciales/tokens utilizan datos ficticios.

**Límites:** no se ejecutaron solicitudes, servidores, pruebas de CORS, JWT, OAuth/tokens, webhooks, gRPC, GraphQL ni herramientas Postman/Insomnia. No se verificaron todas las referencias ni versiones. El resultado es ampliación documental y comprobación estructural, no validación técnica por ejecución ni aprobación externa.

**Acumulado registrado:** etapas 1–6: 265 lecciones según el informe de OpenCode; etapas 7–10: 284; etapas 11–12: 149; etapa 13: 63. Total de etapas 1–13 con desarrollo documental ampliado: **761 lecciones**. Etapas 14–32: 1.155 lecciones requieren profundización equivalente. Se mantienen pendientes la ejecución reproducible, revisión bibliográfica individual y revisión técnica/pedagógica independiente. No se importó ni publicó contenido.


## Addendum de profundización didáctica — etapa 14 — 2026-11-24

Se añadieron prácticas y evidencias a las **58 lecciones** de Java y Spring Boot: arquitectura por capas, IoC/DI, configuración, REST, validación, persistencia, seguridad, transacciones, caché, mensajería y herramientas de build.

**Comprobación documental:** se releyó el archivo actualizado y se verificó el número de unidades con el desglose del roadmap. La práctica asociada a cada lección plantea una aplicación o comprobación y una evidencia observable.

**Límites:** no se ejecutaron compilaciones Java, pruebas Spring, conexiones a MySQL/PostgreSQL, flujos OAuth/OIDC, JWT, colas, WebSockets ni despliegues. No se verificaron versiones ni bibliografía de forma individual. La ampliación no constituye validación técnica por ejecución ni aprobación externa.

**Acumulado:** etapas 1–6: 265 lecciones según el informe de OpenCode; etapas 7–10: 284; etapas 11–12: 149; etapa 13: 63; etapa 14: 58. Total de etapas 1–14 con desarrollo documental ampliado: **819 lecciones**. Etapas 15–32: 1.097 lecciones requieren profundización equivalente. Permanecen pendientes la ejecución reproducible, verificación bibliográfica individual y revisión técnica/pedagógica independiente. No se importó ni publicó contenido.


## Addendum de profundización didáctica — etapas 15–16 — 2026-11-24

Se añadieron prácticas y evidencias a **99 lecciones**:

- **Etapa 15 — Node.js y NestJS: 53 lecciones.** Prácticas sobre runtime, módulos, Event Loop, streams, APIs, middleware, inyección de dependencias, persistencia, autenticación, colas y pruebas.
- **Etapa 16 — PHP, Laravel y .NET: 46 lecciones.** Prácticas sobre lenguaje, Composer, MVC, Eloquent, migraciones, validación, autorización, colas, C#, LINQ y ASP.NET Core.

**Comprobación documental:** ambos archivos fueron releídos desde la rama después de los cambios; se contaron 53 y 46 unidades, cada una con apartado de práctica/evidencia y sin encabezados vacíos.

**Límites:** no se ejecutaron scripts Node/PHP, builds .NET, pruebas de frameworks, migraciones de bases de datos, colas, autenticación ni despliegues. No se verificaron referencias/versiones una por una. El estado es ampliación documental y estructural, no validación técnica por ejecución ni aprobación externa.

**Acumulado:** etapas 1–6: 265; etapas 7–10: 284; etapas 11–12: 149; etapa 13: 63; etapa 14: 58; etapas 15–16: 99. Total de etapas 1–16 con desarrollo documental ampliado: **918 lecciones**. Etapas 17–32: 998 lecciones requieren profundización equivalente. No se importó ni publicó contenido.


## Addendum de profundización — módulos 7.2 y 7.3 (2026-11-24)

### Alcance realizado

Se profundizaron 17 lecciones del módulo 7.2 «Linux» y 20 lecciones del módulo 7.3 «Administración Linux» en el documento de la etapa 7.

- Módulo 7.2: distribuciones, kernel Linux, Ubuntu, Debian, jerarquía del sistema de archivos, directorios FHS, usuarios, grupos, permisos, propietarios, root, sudo, procesos, servicios, paquetes, logs y variables de entorno.
- Módulo 7.3: pwd, ls, cd, mkdir, touch, cp, mv, rm, find, grep, chmod, chown, ps, top, kill, systemctl, journalctl, df, du y mount.

Las lecciones se desarrollaron con explicaciones específicas, ejemplos, prácticas guiadas, actividades independientes, criterios de aceptación, errores frecuentes y preguntas de comprobación. Las actividades administrativas destructivas o privilegiadas se limitaron a entornos de laboratorio y se documentaron precauciones explícitas.

### Conteo acumulado de la etapa 7

| Módulo | Lecciones oficiales | Lecciones profundizadas en estos lotes |
|---|---:|---:|
| 7.1 — Fundamentos de sistemas operativos | 14 | 14 |
| 7.2 — Linux | 17 | 17 |
| 7.3 — Administración Linux | 20 | 20 |
| 7.4 — Bash | 12 | 0 |
| 7.5 — Windows | 12 | 0 |
| 7.6 — Virtualización | 9 | 0 |
| **Total** | **84** | **51** |

### Comprobaciones y límites

- Se cotejaron los títulos y cantidades de los módulos 7.1–7.3 contra el roadmap oficial.
- Se verificó que el documento conserve los módulos 7.4–7.6, el proyecto, la evaluación y las referencias existentes.
- Se corrigió la secuencia de encabezados del módulo 7.1 para hacerla coincidir con el orden oficial del JSON.
- No se ejecutaron comandos en una VM Linux real ni se probaron cambios de permisos, servicios, montajes o procesos en un host.
- No se ejecutaron scripts ni pruebas de automatización; los comandos incluidos son propuestas documentadas, no evidencia de ejecución.
- No se verificaron individualmente las referencias mediante consulta web en estos lotes.
- No se declara la etapa 7 terminada: los 33 temas de Bash, Windows y virtualización aún requieren esta profundización.

### Estado acumulado de trabajo

En esta sesión se profundizaron 51 de las 84 lecciones de la etapa 7. Esto no añade lecciones al roadmap ni altera su identidad curricular. Las etapas 8–32 permanecen sujetas a revisión y profundización progresiva; no se declara completado el objetivo global de 1.916 lecciones.

El roadmap JSON permanece sin cambios (SHA del archivo en la rama: `43b6350dd911350c2b5f68c3d3de3dea4696f878`). El objetivo oficial de la etapa 25 continúa vacío. No se importó, aprobó ni publicó contenido.


## Addendum de profundización didáctica — etapa 17 — 2026-11-24

Se añadieron prácticas y evidencias a las **61 lecciones** de testing y calidad: QA/QC, niveles de prueba, pruebas de API, usabilidad y accesibilidad, rendimiento, diseño de casos, dobles de prueba, TDD/BDD, herramientas, análisis estático y modelos de calidad.

**Comprobación documental:** se releyó el archivo desde la rama; se contaron 61 encabezados, 61 apartados de práctica/evidencia y ningún encabezado vacío.

**Límites:** no se ejecutaron JUnit, Mockito, Jest, Vitest, Playwright, Cypress, Postman, JMeter ni análisis SonarQube. Tampoco se realizaron pruebas de carga. No se verificaron referencias o versiones una por una. La ampliación es documental y estructural, no validación por ejecución ni aprobación externa.

**Acumulado:** etapas 1–6: 265; etapas 7–10: 284; etapas 11–12: 149; etapa 13: 63; etapa 14: 58; etapas 15–16: 99; etapa 17: 61. Total de etapas 1–17 con desarrollo documental ampliado: **979 lecciones**. Etapas 18–32: 937 lecciones requieren profundización equivalente. No se importó ni publicó contenido.


## Addendum de profundización didáctica — etapas 18–19 — 2026-11-24

Se añadieron prácticas y evidencias a **167 lecciones**:

- **Etapa 18 — Arquitectura, diseño y planeación: 100 lecciones.** Requisitos, agilidad, documentación, diagramas, principios de diseño, patrones, arquitecturas, sistemas distribuidos y DDD.
- **Etapa 19 — DevOps, Docker, Cloud y Kubernetes: 67 lecciones.** Cultura DevOps, contenedores, administración de servidores, reverse proxy, CI/CD, nube, Kubernetes e infraestructura como código.

**Comprobación documental:** ambos archivos se releen desde la rama; se cuentan 100 y 67 encabezados y el mismo número de apartados de práctica/evidencia. No se detectan encabezados vacíos.

**Límites:** no se ejecutaron pruebas de infraestructura, imágenes/containers, pipelines, servicios cloud, clústeres Kubernetes, Terraform ni despliegues. No se crearon recursos cloud facturables. No se verificaron todas las referencias y versiones. El resultado es ampliación documental y estructural, no validación técnica por ejecución ni aprobación externa.

**Acumulado:** etapas 1–6: 265; etapas 7–10: 284; etapas 11–12: 149; etapa 13: 63; etapa 14: 58; etapas 15–16: 99; etapa 17: 61; etapas 18–19: 167. Total de etapas 1–19 con desarrollo documental ampliado: **1.146 lecciones**. Etapas 20–32: 770 lecciones requieren profundización equivalente. No se importó ni publicó contenido.


## Addendum de profundización didáctica — etapas 20–22 — 2026-11-24

Se añadieron prácticas y evidencias a **197 lecciones**:

- **Etapa 20 — Desarrollo seguro/AppSec: 57 lecciones.** Secure coding, modelado de amenazas, vulnerabilidades web/API, OWASP, identidad, sesiones, criptografía aplicada, cabeceras y validación.
- **Etapa 21 — Fundamentos de ciberseguridad, riesgos y ética: 82 lecciones.** Activos, amenazas, riesgo, controles, malware desde enfoque defensivo, marcos de referencia, ética, autorización, privacidad e IAM.
- **Etapa 22 — Laboratorio y hardening: 58 lecciones.** Virtualización aislada, Linux/Windows, SSH, firewall, auditoría, segmentación y plataformas vulnerables de entrenamiento.

**Comprobación documental:** se releyeron los tres archivos desde la rama; se contaron 57, 82 y 58 encabezados y el mismo número de apartados de práctica/evidencia. No se detectaron encabezados vacíos.

**Límites:** no se ejecutaron laboratorios, pruebas de penetración, escaneos, servicios, configuraciones de hardening ni máquinas virtuales. Las prácticas ofensivas se limitan explícitamente a activos propios o autorizados y entornos aislados. No se verificaron individualmente todas las referencias ni versiones. La ampliación es documental y estructural, no validación por ejecución ni aprobación externa.

**Acumulado:** etapas 1–6: 265; etapas 7–10: 284; etapas 11–12: 149; etapa 13: 63; etapa 14: 58; etapas 15–16: 99; etapa 17: 61; etapas 18–19: 167; etapas 20–22: 197. Total de etapas 1–22 con desarrollo documental ampliado: **1.343 lecciones**. Etapas 23–32: 573 lecciones requieren profundización equivalente. No se importó ni publicó contenido.


## Addendum de cierre de desarrollo documental por lección — etapas 23–32 — 2026-11-24

Se añadieron prácticas y evidencias específicas a las **573 lecciones** de las etapas 23–32:

| Etapa | Lecciones | Área |
|---:|---:|---|
| 23 | 58 | OSINT, reconocimiento y evaluación de vulnerabilidades |
| 24 | 47 | Pentesting autorizado y documentación de hallazgos |
| 25 | 50 | Seguridad web y APIs |
| 26 | 39 | Active Directory y seguridad Windows |
| 27 | 58 | Blue Team, SOC, SIEM y detección |
| 28 | 46 | Threat Hunting y DFIR |
| 29 | 71 | Cloud Security, DevSecOps y cadena de suministro |
| 30 | 75 | IA, automatización y criptografía |
| 31 | 75 | Bajo nivel, análisis de memoria, ingeniería inversa y análisis defensivo de malware |
| 32 | 54 | Proyecto profesional, portafolio y preparación laboral |
| **Total** | **573** | |

### Comprobación documental y curricular

- Se cotejaron los conteos de encabezados por etapa contra el JSON oficial para las etapas 7–32.
- En las etapas 7–32 no se detectaron encabezados de lección vacíos.
- Las etapas 11–32 cuentan con un apartado de práctica/evidencia por lección; las etapas 7–10 contienen desarrollo específico, actividades y comprobaciones según su estructura documental.
- Se verificó nuevamente que el roadmap contiene 33 etapas, 212 módulos y 1.946 títulos nominales.
- La etapa 25 conserva su objetivo oficial vacío. No se creó ni modificó un objetivo.
- `apps/roadmaps/data/ascenso_3_1.json` permanece sin cambios.

### Cobertura documental acumulada

| Bloque | Lecciones |
|---|---:|
| Etapas 1–6 — informe de OpenCode | 265 |
| Etapas 7–10 — desarrollo ampliado | 284 |
| Etapas 11–12 — prácticas/evidencias | 149 |
| Etapa 13 | 63 |
| Etapa 14 | 58 |
| Etapas 15–16 | 99 |
| Etapa 17 | 61 |
| Etapas 18–19 | 167 |
| Etapas 20–22 | 197 |
| Etapas 23–32 | 573 |
| **Etapas 1–32** | **1.916** |

**Estado:** las 1.916 lecciones de las etapas 1–32 tienen una base de desarrollo documental individual ampliada y actividades/evidencias en los lotes descritos. Esto no equivale a validación técnica por ejecución ni a aprobación académica final.

### Validaciones que siguen pendientes

1. Ejecutar los ejemplos, scripts, consultas, configuraciones y laboratorios en entornos definidos y seguros.
2. Verificar individualmente URLs, versiones, licencias y pertinencia de las referencias.
3. Revisar accesibilidad, seguridad y compatibilidad según la tecnología.
4. Obtener revisión técnica y pedagógica independiente.
5. Registrar evidencia de ejecución y resolver hallazgos antes de cualquier importación.

No se importó, aprobó ni publicó contenido. No se modificaron UUID ni se inventaron identificadores. No se fusionó el PR.


## Addendum de cierre documental de la etapa 7 — 2026-11-24

### Alcance de la ampliación

Se completó la profundización documental individual de los módulos restantes de la etapa 7:

- **7.4 Bash:** 12 lecciones (variables, operadores, condicionales, bucles, funciones, arrays, pipes, redirecciones, códigos de salida, scripts, cron y automatización).
- **7.5 Windows:** 12 lecciones (arquitectura, NTFS, usuarios y grupos, permisos, procesos, servicios, Registro, Administrador de tareas, Visor de eventos, firewall, PowerShell y administración de servicios).
- **7.6 Virtualización:** 9 lecciones (VirtualBox, VMware, máquinas virtuales, snapshots, recursos, redes virtuales, NAT, host-only y adaptadores virtuales).

Cada lección contiene desarrollo conceptual, ejemplo o escenario razonado, práctica guiada, actividad independiente, criterios de aceptación, errores frecuentes y pregunta de comprobación. Se priorizaron prácticas de consulta y laboratorios aislados; las operaciones privilegiadas, destructivas o de cambio de configuración se excluyeron del host y se señalaron como actividades que requieren entorno autorizado.

### Cobertura documental de la etapa 7

| Módulo | Lecciones oficiales | Lecciones con desarrollo individualizado |
|---|---:|---:|
| 7.1 — Fundamentos de sistemas operativos | 14 | 14 |
| 7.2 — Linux | 17 | 17 |
| 7.3 — Administración Linux | 20 | 20 |
| 7.4 — Bash | 12 | 12 |
| 7.5 — Windows | 12 | 12 |
| 7.6 — Virtualización | 9 | 9 |
| **Total etapa 7** | **84** | **84** |

### Revisión documental y límites

- Se comprobó la correspondencia de los 84 encabezados de lección con los módulos y cantidades del roadmap oficial de etapa 7.
- Se revisó que los módulos conservaran el orden curricular y que el proyecto oficial posterior al módulo 7.6 permaneciera en el documento.
- Las prácticas propuestas incluyen comandos de consulta y actividades de laboratorio; no se ejecutaron en máquinas virtuales reales en esta intervención.
- No se ejecutaron scripts, pruebas de PowerShell, cambios de firewall, modificaciones del Registro, cambios de permisos, tareas cron ni operaciones de snapshots.
- No se realizó validación externa experta ni verificación exhaustiva de cada referencia bibliográfica en esta intervención.
- Por ello, el estado es **desarrollo documental individualizado completo para las 84 lecciones de la etapa 7**, no validación técnica ejecutada ni aprobación académica final.

### Estado global

El roadmap oficial continúa sin cambios. Esta actualización no altera la identidad, cantidad ni orden de lecciones. Las etapas 8–32 continúan pendientes de la misma profundización individualizada sistemática; no se declara completo el total de 1.916 lecciones.

No se importó ni publicó contenido. El objetivo oficial de la etapa 25 permanece vacío y no fue completado por inferencia.


## Addendum de cierre documental de la etapa 7 — 2026-11-24

### Resultado

Se completó el desarrollo documental individual de las 84 lecciones oficiales de la etapa 7, distribuidas en seis módulos:

| Módulo | Lecciones | Cobertura documental |
|---|---:|---|
| 7.1 — Fundamentos de sistemas operativos | 14 | 14/14 |
| 7.2 — Linux | 17 | 17/17 |
| 7.3 — Administración Linux | 20 | 20/20 |
| 7.4 — Bash | 12 | 12/12 |
| 7.5 — Windows | 12 | 12/12 |
| 7.6 — Virtualización | 9 | 9/9 |
| **Total** | **84** | **84/84** |

Las lecciones incluyen desarrollo conceptual específico, ejemplos técnicos o escenarios razonados, prácticas guiadas, actividades independientes, criterios de aceptación, errores frecuentes y preguntas de comprobación. Se añadieron límites de seguridad para prácticas de permisos, procesos, servicios, firewall, Registro, redes virtuales y operaciones administrativas.

### Revisión estructural realizada

- Se verificaron 84 encabezados de lección y su distribución por módulo.
- Se comprobó en las 84 lecciones la presencia de práctica guiada, actividad independiente y criterios de aceptación.
- Se cotejó la distribución de módulos y lecciones con el documento curricular de la etapa 7 en el roadmap oficial.
- Se mantuvieron los títulos y el orden oficial de las lecciones.
- Se mantuvieron el proyecto oficial, la evaluación y las secciones de referencias ya existentes.

### Límites de validación

- El resultado representa desarrollo documental y revisión estructural interna; no equivale a validación técnica independiente ni aprobación académica.
- No se ejecutaron las prácticas en máquinas virtuales Linux o Windows.
- No se ejecutaron scripts, comandos administrativos, cambios de ACL, modificaciones del Registro, reglas de firewall, montajes ni pruebas de redes virtuales.
- No se verificaron de manera exhaustiva las referencias bibliográficas ni la vigencia de cada versión de producto.
- No se ejecutaron pruebas automatizadas ni se obtuvo evidencia CI para esta actualización.
- Las prácticas que modifican el sistema requieren VM desechable, autorización, respaldo y registro de resultados antes de considerarse verificadas.

### Estado curricular global

La etapa 7 queda desarrollada documentalmente en sus 84 lecciones. Este cierre no implica que las etapas 8–32 estén terminadas ni que las 1.916 lecciones de las etapas 1–32 estén validadas. El trabajo debe continuar con la etapa 8 y avanzar en secuencia, conservando el baseline curricular oficial.

No se modificó `apps/roadmaps/data/ascenso_3_1.json`; no se inventaron UUID; no se ejecutó importación, aprobación ni publicación. El objetivo de la etapa 25 permanece vacío y sin cambios.


## Addendum de continuidad — etapa 8, módulos 8.1–8.4 (2026-11-24)

### Desarrollo individualizado realizado

Se desarrollaron 51 lecciones de los primeros cuatro módulos de la etapa 8:

- **8.1 Fundamentos de redes:** 13 lecciones, desde LAN/WAN/MAN hasta dispositivos de interconexión y acceso inalámbrico.
- **8.2 Modelos de comunicación:** 9 lecciones sobre OSI, TCP/IP, encapsulamiento, paquetes, tramas, segmentos y MTU.
- **8.3 Direccionamiento:** 13 lecciones sobre MAC, IPv4/IPv6, rangos públicos/privados, máscaras, subnetting, CIDR, VLSM, gateway, broadcast, ARP y DHCP.
- **8.4 Protocolos:** 16 lecciones sobre TCP, UDP, ICMP, DNS, HTTP(S), SSH, FTP/SFTP, correo, SMB, LDAP, Kerberos y WebSockets.

Cada lección incluye explicación conceptual específica, práctica guiada, actividad independiente, criterios de aceptación, errores frecuentes y pregunta de comprobación. Se limitaron las prácticas a sistemas propios, capturas de laboratorio y consultas autorizadas; no se proponen escaneos ni accesos a redes ajenas.

### Cobertura de etapa 8

| Módulo | Lecciones oficiales | Desarrolladas en esta entrega |
|---|---:|---:|
| 8.1 Fundamentos de redes | 13 | 13 |
| 8.2 Modelos de comunicación | 9 | 9 |
| 8.3 Direccionamiento | 13 | 13 |
| 8.4 Protocolos | 16 | 16 |
| 8.5 Routing y Switching | 10 | 0 |
| 8.6 Seguridad de redes | 9 | 0 |
| 8.7 Herramientas | 11 | 0 |
| **Total** | **81** | **51** |

### Límites de validación

- Se comprobó el número de lecciones de cada uno de los módulos 8.1–8.4 contra los encabezados oficiales del documento.
- No se ejecutaron capturas de paquetes, consultas DNS, trazas, pruebas de conectividad ni configuraciones de red en un laboratorio real durante esta entrega.
- No se verificó de manera exhaustiva cada referencia externa ni se obtuvo revisión técnica independiente.
- La etapa 8 no se declara terminada: faltan 30 lecciones de routing/switching, seguridad y herramientas.

La etapa 7 queda documentada con desarrollo individualizado de sus 84 lecciones. La etapa 8 presenta 51 de 81 lecciones profundizadas. El roadmap oficial y sus identidades curriculares permanecen sin modificación; no se importó ni publicó contenido.


## Desarrollo documental individual — etapa 8 (2026-11-24)

### Resultado

Se desarrollaron individualmente las 81 lecciones oficiales de la etapa 8 «Redes informáticas y protocolos», respetando títulos, numeración y distribución del roadmap:

| Módulo | Lecciones oficiales | Desarrolladas |
|---|---:|---:|
| 8.1 — Fundamentos de redes | 13 | 13 |
| 8.2 — Modelos de comunicación | 9 | 9 |
| 8.3 — Direccionamiento | 13 | 13 |
| 8.4 — Protocolos | 16 | 16 |
| 8.5 — Routing y Switching | 10 | 10 |
| 8.6 — Seguridad de redes | 9 | 9 |
| 8.7 — Herramientas | 11 | 11 |
| **Total** | **81** | **81** |

Cada lección incorpora desarrollo conceptual específico, ejemplo o escenario, práctica guiada, actividad independiente, criterios de aceptación, errores frecuentes y pregunta de comprobación. Se incluyeron restricciones explícitas de autorización para captura de tráfico, Nmap, inspección de servicios, configuración de firewall y otras actividades de red.

### Revisión estructural

- Se verificaron 81 encabezados únicos de lección.
- Se cotejaron los siete módulos y sus conteos con `apps/roadmaps/data/ascenso_3_1.json`.
- Se verificó en las 81 lecciones la presencia de práctica guiada, actividad independiente y criterios de aceptación.
- Se conservaron proyecto oficial, evaluación y referencias preexistentes.

### Límites de validación

- Se trata de desarrollo documental y revisión estructural interna; no equivale a validación técnica independiente ni aprobación académica.
- No se ejecutaron laboratorios de routing, switching, VLAN, VPN, firewall o direccionamiento en infraestructura real.
- No se ejecutaron capturas ni escaneos de red; los comandos de diagnóstico se proponen para equipos propios o expresamente autorizados.
- No se verificaron individualmente todas las referencias ni vigencia de versiones de herramientas.
- No se ejecutaron pruebas automatizadas ni se obtuvo evidencia CI para este lote.

No se modificó el roadmap JSON, no se inventaron UUID y no se importó, aprobó ni publicó contenido. El objetivo de etapa 25 continúa vacío. Las etapas posteriores aún requieren desarrollo y revisión equivalentes.


## Desarrollo documental individual — etapa 9 (2026-11-24)

### Resultado

Se desarrollaron individualmente las 81 lecciones oficiales de la etapa 9 «Bases de datos relacionales y SQL», conservando módulos, títulos y numeración:

| Módulo | Lecciones oficiales | Desarrolladas |
|---|---:|---:|
| 9.1 — Fundamentos | 10 | 10 |
| 9.2 — Modelado | 11 | 11 |
| 9.3 — MySQL | 9 | 9 |
| 9.4 — SQL | 19 | 19 |
| 9.5 — Diseño y normalización | 9 | 9 |
| 9.6 — Bases de datos avanzadas | 15 | 15 |
| 9.7 — PostgreSQL | 8 | 8 |
| **Total** | **81** | **81** |

Cada lección contiene explicación conceptual específica, ejemplo, práctica guiada, actividad independiente, criterios de aceptación, errores frecuentes y pregunta de comprobación. Se incluyeron prácticas en esquemas desechables, protección de credenciales, prevención de sentencias destructivas y distinción entre sintaxis/semántica de MySQL y PostgreSQL.

### Revisión estructural

- Se verificaron 81 encabezados únicos de lección.
- Se cotejaron los siete módulos y sus conteos con el roadmap JSON oficial.
- Se comprobó en todas las lecciones la presencia de práctica guiada, actividad independiente y criterios de aceptación.
- Se conservaron resultados de aprendizaje, proyecto, evaluación y referencias preexistentes.

### Límites de validación

- Es desarrollo documental y revisión estructural interna, no validación técnica independiente ni aprobación académica.
- No se ejecutaron sentencias SQL, migraciones, transacciones ni pruebas de concurrencia en motores reales.
- No se ejecutaron instalaciones de MySQL/PostgreSQL ni se verificó compatibilidad por versiones en laboratorio.
- No se verificaron exhaustivamente las referencias bibliográficas.
- No se ejecutaron pruebas automatizadas ni se obtuvo evidencia CI para este lote.

No se modificó el roadmap JSON, no se inventaron UUID y no se importó, aprobó ni publicó contenido. Las etapas siguientes permanecen pendientes de desarrollo documental equivalente; la etapa 25 mantiene su objetivo oficial vacío.


## Desarrollo documental individual — etapa 10 (2026-11-24)

### Resultado

Se desarrollaron individualmente las 38 lecciones oficiales de la etapa 10 «NoSQL y almacenamiento moderno», manteniendo títulos, módulos y numeración:

| Módulo | Lecciones oficiales | Desarrolladas |
|---|---:|---:|
| 10.1 — Fundamentos NoSQL | 8 | 8 |
| 10.2 — MongoDB | 14 | 14 |
| 10.3 — Redis | 11 | 11 |
| 10.4 — Otras arquitecturas de almacenamiento | 5 | 5 |
| **Total** | **38** | **38** |

Cada lección contiene explicación específica, ejemplo o escenario, práctica guiada, actividad independiente, criterios de aceptación, errores frecuentes y pregunta de comprobación. Se añadieron precauciones para no utilizar datos reales, proteger sesiones y secretos, limitar comandos destructivos y considerar consistencia, replicación, persistencia y retención.

### Revisión estructural

- Se verificaron 38 encabezados únicos.
- Se cotejaron los cuatro módulos y sus conteos con el roadmap JSON oficial.
- Se comprobó la presencia de práctica guiada, actividad independiente y criterios de aceptación en todas las lecciones.
- Se conservaron resultados de aprendizaje, proyecto, evaluación y referencias preexistentes.

### Límites de validación

- Es desarrollo documental y revisión estructural interna, no validación técnica independiente ni aprobación académica.
- No se desplegaron instancias MongoDB, Redis ni otros motores; no se ejecutaron operaciones CRUD, pipelines, replicación, sharding, TTL ni pruebas de rendimiento.
- No se verificaron exhaustivamente referencias ni compatibilidad por versiones de los productos.
- No se ejecutaron pruebas automatizadas ni se obtuvo evidencia CI para este lote.

No se modificó el roadmap JSON, no se inventaron UUID y no se importó, aprobó ni publicó contenido. Las etapas posteriores permanecen pendientes de desarrollo equivalente; el objetivo oficial vacío de etapa 25 sigue intacto.


## Desarrollo documental individual — etapa 11 (2026-11-24)

### Resultado

Se desarrollaron individualmente las 60 lecciones oficiales de la etapa 11 «HTML, CSS y fundamentos frontend», conservando módulos, títulos y numeración:

| Módulo | Lecciones oficiales | Desarrolladas |
|---|---:|---:|
| 11.1 — HTML | 21 | 21 |
| 11.2 — Accesibilidad | 8 | 8 |
| 11.3 — CSS | 17 | 17 |
| 11.4 — Diseño de interfaces | 8 | 8 |
| 11.5 — SEO | 6 | 6 |
| **Total** | **60** | **60** |

Las lecciones incluyen explicación técnica, ejemplo, práctica guiada, actividad independiente, criterios de aceptación, errores frecuentes y pregunta de comprobación. Se incorporaron consideraciones de HTML semántico, teclado, ARIA, contraste, lectores de pantalla, responsive, reducción de movimiento y uso veraz de metadatos/datos estructurados.

### Revisión estructural

- Se verificaron 60 encabezados únicos.
- Se cotejaron los cinco módulos y sus conteos con el roadmap JSON oficial.
- Se comprobó en todas las lecciones la presencia de práctica guiada, actividad independiente y criterios de aceptación.
- Se conservaron resultados de aprendizaje, proyecto, evaluación y referencias preexistentes.

### Límites de validación

- Desarrollo documental y revisión estructural interna; no constituye validación técnica independiente ni aprobación académica.
- No se ejecutaron pruebas de navegador, validadores HTML/CSS, auditorías WCAG, pruebas con lectores de pantalla ni evaluación de SEO en entornos reales.
- No se verificó exhaustivamente la vigencia de todas las referencias ni la compatibilidad entre navegadores.
- No se ejecutaron pruebas automatizadas ni se obtuvo evidencia CI para este lote.

No se modificó el roadmap JSON, no se inventaron UUID y no se importó, aprobó ni publicó contenido. Las etapas posteriores siguen pendientes de desarrollo equivalente; el objetivo oficial vacío de etapa 25 permanece intacto.


## Profundización documental integral — etapa 7 (2026-11-24)

### Alcance

Se completó la ampliación didáctica documental de las **84 lecciones** oficiales de la etapa 7, distribuidas en seis módulos:

| Módulo | Lecciones | Cobertura documental |
|---|---:|---|
| 7.1 Fundamentos de sistemas operativos | 14 | 14/14 |
| 7.2 Linux | 17 | 17/17 |
| 7.3 Administración Linux | 20 | 20/20 |
| 7.4 Bash | 12 | 12/12 |
| 7.5 Windows | 12 | 12/12 |
| 7.6 Virtualización | 9 | 9/9 |
| **Total** | **84** | **84/84** |

Se añadieron prácticas específicas, evidencias esperadas, criterios de aceptación, límites de seguridad y registros sugeridos a las lecciones de Bash, Windows y virtualización. Se amplió además el trabajo previo de Linux y administración con ejercicios guiados y advertencias operativas. El proyecto oficial de dos servidores virtuales, rúbrica, autoevaluación y referencias se conservaron.

### Control editorial y técnico

- Se cotejaron los seis módulos y sus cantidades de lecciones contra el roadmap oficial.
- Se comprobó estructuralmente la presencia de 84 encabezados de lección en el documento.
- Se conservaron las prácticas en modo de inspección o laboratorio autorizado; no se instruye desactivar controles ni modificar servicios del host.
- No se ejecutaron los comandos Bash/PowerShell en máquinas reales o virtuales durante esta intervención.
- No se ejecutaron instalaciones de Windows Server, Ubuntu Server, VirtualBox o VMware.
- No se verificaron individualmente todas las referencias externas ni se obtuvo revisión experta independiente.

**Estado:** desarrollo documental de la etapa 7 completo en esta pasada; validación técnica por ejecución y aprobación académica siguen pendientes. La cobertura 84/84 no equivale a pruebas ejecutadas ni a aprobación.

El roadmap JSON no fue modificado. Se conserva el objetivo vacío de la etapa 25. No se importó ni publicó contenido.


## Desarrollo documental individual — etapa 12 (2026-11-24)

### Resultado

Se desarrollaron individualmente las 89 lecciones oficiales de la etapa 12 «JavaScript, TypeScript, React y Next.js», respetando títulos, módulos y numeración:

| Módulo | Lecciones oficiales | Desarrolladas |
|---|---:|---:|
| 12.1 — JavaScript | 19 | 19 |
| 12.2 — DOM | 9 | 9 |
| 12.3 — Asincronía | 10 | 10 |
| 12.4 — Web APIs | 7 | 7 |
| 12.5 — TypeScript | 11 | 11 |
| 12.6 — React | 16 | 16 |
| 12.7 — Next.js | 10 | 10 |
| 12.8 — Herramientas | 7 | 7 |
| **Total** | **89** | **89** |

Cada lección incluye explicación técnica, ejemplo, práctica guiada, actividad independiente, criterios de aceptación, errores frecuentes y pregunta de comprobación. Se incluyeron límites de seguridad para almacenamiento del navegador, cookies, geolocalización, portapapeles, carga de archivos, variables de entorno, autenticación, acceso a datos y uso de dependencias.

### Revisión estructural

- Se verificaron 89 encabezados únicos.
- Se cotejaron los ocho módulos y sus conteos con el roadmap JSON oficial.
- Se comprobó en todas las lecciones la presencia de práctica guiada, actividad independiente y criterios de aceptación.
- Se conservaron resultados de aprendizaje, proyecto, evaluación y referencias preexistentes.

### Límites de validación

- Desarrollo documental y revisión estructural interna; no equivale a validación técnica independiente ni aprobación académica.
- No se ejecutaron ejemplos JavaScript/TypeScript, builds, pruebas React/Next.js ni pruebas en navegadores.
- No se probaron versiones concretas de frameworks, dependencias o herramientas; las instrucciones deben cotejarse con versiones fijadas antes de ejecutar.
- No se verificaron exhaustivamente las referencias bibliográficas.
- No se ejecutaron pruebas automatizadas ni se obtuvo evidencia CI para este lote.

No se modificó el roadmap JSON, no se inventaron UUID y no se importó, aprobó ni publicó contenido. Las etapas siguientes permanecen pendientes de desarrollo equivalente; el objetivo oficial vacío de etapa 25 permanece intacto.
