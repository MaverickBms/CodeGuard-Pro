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

- **Etapa 1:** revisión de los cinco módulos; se consolidó el segundo bloque de autoevaluación de representación de información como cierre reflexivo para evitar un encabezado duplicado.
- **Etapa 2:** revisión de las 39 entradas; se retiró una referencia que era una nota editorial y no un recurso bibliográfico para estudiantes.
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
