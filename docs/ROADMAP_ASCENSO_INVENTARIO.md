# Inventario académico ASCENSO 3.1

**Fecha:** 2026-11-19
**Estado:** inventario y diagnóstico; **no** sustituye ni modifica el documento maestro.
**Fuente oficial localizada:** `PROYECTO_ASCENSO_Roadmap_Maestro_Consolidado_3_1_2026.docx`
en `/home/mvxbms/Descargas/` (102 KB).
**SHA-256 de la fuente:** `15a9ef38c7284de79eedd1ba10ef33cc50b324c9706836740205778eea4704d3`.
**Copia en el repositorio:** no existe. El JSON `apps/roadmaps/data/ascenso_3_1.json`
declara el mismo SHA-256; se verificó que ambos coinciden.

> El DOCX no se ha publicado en el repositorio por contener material académico del
> propietario. Cualquier incorporación al repositorio requiere autorización expresa.
>
> **Nota de lectura:** las secciones 1–4 conservan el inventario inicial del
> 2026-11-19, cuando no había cuerpos de lección. La sección 13 registra la
> iteración académica posterior (8 lecciones, 16 ejercicios y 13 fuentes), por lo
> que las cifras de «0 contenido» deben leerse como estado histórico, no actual.

## 1. Método de verificación

1. Se calculó el SHA-256 del DOCX local y se comparó con `metadata.sha256_fuente`
   del JSON oficial.
2. Se parseó `word/document.xml` del DOCX y se contrastaron títulos de etapa,
   prioridades, módulos, lecciones y proyectos con el JSON.
3. Se cargó el JSON en un perfil SQLite aislado (`/tmp/cg-inv`) con
   `migrate` + `cargar_ascenso`.
4. Se consultaron los modelos `Roadmap`, `Etapa`, `Modulo`, `Leccion`,
   `Prerrequisito`, `ContenidoLeccion`, `EjercicioLeccion`, `Quiz` y
   `CriterioFinalizacion`.

## 2. Correspondencia estructural verificada

| Comprobación | Resultado |
|---|---|
| Etapas | 33 (0–32) |
| Módulos | 212 |
| Lecciones (títulos) | 1.946 |
| Prerrequisitos explícitos | 7 (etapas 10, 15 y 31) |
| Prioridades | 24 P1, 6 P2, 3 P3 |
| Objetivos de etapa | 32 con texto; **etapa 25 sin objetivo formal en el DOCX** |
| Proyectos de etapa | 33; etapa 10 corregida de 4.739 a 136 caracteres |
| Contenido de lección desarrollado | **0** (`ContenidoLeccion`) |
| Ejemplos | **0** (`EjemploLeccion`) |
| Ejercicios | **0** (`EjercicioLeccion`) |
| Quizzes/exámenes publicados | **0** |
| Etapas marcadas `desarrollada_en_mvp` | 0 |

**Conclusión:** la estructura curricular oficial está completa y es consistente,
pero el contenido pedagógico desarrollado está vacío. Navegar por 1.946 títulos
no equivale a disponer de 1.946 lecciones redactadas y evaluables.

## 3. Inventario de las 33 etapas

| # | Etapa | Prioridad | Módulos | Lecciones | Objetivo | Proyecto (chars) | Observaciones |
|---:|---|---:|---:|---:|---|---:|---|
| 0 | Preparación y método de aprendizaje | P1 | 4 | 30 | Sí | 81 | etapa de apertura/cierre |
| 1 | Fundamentos de computación y arquitectura del computador | P1 | 5 | 46 | Sí | 125 | — |
| 2 | Pensamiento computacional, lógica y matemáticas | P1 | 5 | 39 | Sí | 87 | — |
| 3 | Programación desde cero con Java | P1 | 6 | 48 | Sí | 104 | — |
| 4 | Programación Orientada a Objetos y paradigmas | P1 | 5 | 33 | Sí | 53 | — |
| 5 | Git, GitHub, terminal y modularidad | P1 | 4 | 42 | Sí | 94 | — |
| 6 | Estructuras de datos y algoritmos | P1 | 7 | 57 | Sí | 68 | — |
| 7 | Sistemas operativos: Linux, Windows y administración | P1 | 6 | 84 | Sí | 159 | — |
| 8 | Redes informáticas y protocolos de comunicación | P1 | 7 | 81 | Sí | 124 | — |
| 9 | Bases de datos relacionales y SQL | P1 | 7 | 81 | Sí | 119 | — |
| 10 | Bases de datos NoSQL y almacenamiento moderno | P1 | 4 | 38 | Sí | 136 | proyecto corregido a 136 chars; prerrequisitos: 9 |
| 11 | HTML y CSS: fundamentos profesionales del frontend | P1 | 5 | 60 | Sí | 73 | — |
| 12 | JavaScript, TypeScript y frameworks frontend | P1 | 8 | 89 | Sí | 107 | — |
| 13 | Internet, HTTP, APIs y comunicación entre sistemas | P1 | 7 | 63 | Sí | 79 | — |
| 14 | Backend I: Java y Spring Boot | P1 | 7 | 58 | Sí | 89 | — |
| 15 | Backend II: Node.js y NestJS | P2 | 6 | 53 | Sí | 92 | prerrequisitos: 13 |
| 16 | Backend III: PHP, Laravel y .NET | P2 | 4 | 46 | Sí | 109 | — |
| 17 | Testing, aseguramiento y calidad del software | P1 | 9 | 61 | Sí | 112 | — |
| 18 | Arquitectura, diseño y planeación de software | P1 | 9 | 100 | Sí | 149 | — |
| 19 | DevOps, Docker, CI/CD y servidores | P1 | 9 | 67 | Sí | 109 | — |
| 20 | Desarrollo seguro de software (AppSec) | P1 | 6 | 57 | Sí | 168 | — |
| 21 | Fundamentos de ciberseguridad, gestión de riesgos y ética | P1 | 8 | 82 | Sí | 134 | — |
| 22 | Laboratorio de ciberseguridad, hardening y administración segura | P1 | 6 | 58 | Sí | 193 | — |
| 23 | Reconocimiento, OSINT y gestión de vulnerabilidades | P1 | 7 | 58 | Sí | 155 | — |
| 24 | Pentesting de redes y sistemas | P2 | 5 | 47 | Sí | 138 | — |
| 25 | Seguridad de aplicaciones web y APIs | P1 | 6 | 50 | **No** | 140 | DOCX sin objetivo formal |
| 26 | Active Directory y seguridad empresarial Windows | P2 | 6 | 39 | Sí | 132 | — |
| 27 | Blue Team, SOC, SIEM e ingeniería de detección | P2 | 8 | 58 | Sí | 150 | — |
| 28 | Threat Hunting, respuesta a incidentes y forense digital | P3 | 6 | 46 | Sí | 138 | — |
| 29 | Cloud Security, DevSecOps y Supply Chain Security | P2 | 8 | 71 | Sí | 145 | — |
| 30 | Inteligencia artificial, automatización y seguridad avanzada | P3 | 8 | 75 | Sí | 159 | — |
| 31 | Ciberseguridad de bajo nivel, análisis de malware e ingeniería inversa | P3 | 8 | 75 | Sí | 315 | prerrequisitos: 3, 4, 7, 8, 21 |
| 32 | Proyecto profesional, portafolio y preparación laboral | P1 | 6 | 54 | Sí | 228 | etapa de apertura/cierre |

## 4. Hallazgos editoriales

### 4.1 Etapa 25 — objetivo ausente

El DOCX no contiene una línea `Objetivo:` para la etapa 25. El texto inmediatamente
posterior al título dice:

> «Esta etapa será especialmente importante porque combina tus dos grandes intereses:
> Desarrollo de software + Ciberseguridad.»

No se ha inventado ni publicado un objetivo nuevo. Propuesta sujeta a aprobación:

> «Comprender la arquitectura de seguridad de aplicaciones web y APIs, identificar
> vulnerabilidades frecuentes y aplicar prácticas de desarrollo seguro y pruebas
> de seguridad en entornos locales autorizados.»

La propuesta se deriva del título, los módulos 25.1–25.6 y la introducción textual
del DOCX. Debe revisarse y aprobarse antes de modificar el contenido oficial.

### 4.2 Etapa 10 — proyecto desproporcionado (corregido)

El DOCX define el proyecto de la etapa 10 en una sola frase:

> «Diseñar un sistema que utilice MySQL para datos transaccionales, MongoDB para
> documentos y Redis para caché, justificando cada decisión.»

El JSON anterior contenía 4.739 caracteres porque el extractor no cerraba el
marcador `Proyecto` al entrar en la sección `Ampliación de profundidad`. Se
corrigió el extractor y el JSON conserva ahora la frase oficial (136 caracteres).
**No se cambió el contenido académico: se restauró la fidelidad al DOCX.**

### 4.3 Lecciones repetidas

Hay 333 títulos repetidos en el conjunto global (por ejemplo, conceptos que
aparecen en varias etapas). No se encontraron duplicados dentro de un mismo
módulo. No se consideran un defecto por sí mismos; deben revisarse al desarrollar
contenido para evitar repetición innecesaria.

### 4.4 Profundidad y evaluaciones

No existen cuerpos de lección, ejemplos, ejercicios ni quizzes publicados en el
perfil limpio. Por tanto, el recorrido académico completo no es cursable todavía;
la aplicación muestra estados vacíos honestos en las lecciones.

## 5. Fuentes externas propuestas para enriquecimiento

No se ha copiado texto de estas fuentes. Se registran como referencias candidatas
para una futura revisión editorial, con fecha de consulta y justificación.

| Fuente | URL | Fecha de consulta | Uso previsto |
|---|---|---|---|
| MDN Web Docs | https://developer.mozilla.org/ | 2026-11-19 | HTTP, HTML, CSS, JavaScript y APIs web (etapas 13–16) |
| Python Documentation | https://docs.python.org/3/ | 2026-11-19 | Fundamentos, tipado, pruebas y empaquetado (etapas 3–6, 12) |
| Java SE Documentation | https://docs.oracle.com/en/java/ | 2026-11-19 | Java, POO y concurrencia (etapas 3–4, 20) |
| OWASP Top 10 | https://owasp.org/Top10/ | 2026-11-19 | Seguridad web y APIs (etapas 25–31) |
| OWASP ASVS | https://owasp.org/www-project-application-security-verification-standard/ | 2026-11-19 | Verificación de seguridad de aplicaciones (etapas 25–29) |
| NIST Cybersecurity Framework 2.0 | https://www.nist.gov/cyberframework | 2026-11-19 | Gobernanza y respuesta (etapas 27–28) |
| MITRE ATT&CK | https://attack.mitre.org/ | 2026-11-19 | Detección, threat hunting y respuesta (etapas 27–28) |
| CIS Benchmarks | https://www.cisecurity.org/cis-benchmarks | 2026-11-19 | Hardening de sistemas y cloud (etapas 26, 29) |
| Microsoft Learn | https://learn.microsoft.com/ | 2026-11-19 | Windows, Active Directory y Azure (etapas 26, 29) |
| AWS Documentation | https://docs.aws.amazon.com/ | 2026-11-19 | Cloud y seguridad (etapa 29) |
| Kubernetes Documentation | https://kubernetes.io/docs/ | 2026-11-19 | Contenedores y orquestación (etapas 18–19, 29) |
| Docker Documentation | https://docs.docker.com/ | 2026-11-19 | Contenedores (etapas 18–19) |
| PostgreSQL Documentation | https://www.postgresql.org/docs/ | 2026-11-19 | Bases relacionales (etapas 9–10) |
| MongoDB Documentation | https://www.mongodb.com/docs/ | 2026-11-19 | Bases documentales (etapa 10) |
| Redis Documentation | https://redis.io/docs/latest/ | 2026-11-19 | Caché y estructuras clave-valor (etapa 10) |
| W3C WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | 2026-11-19 | Accesibilidad de la interfaz (transversal) |
| Git Documentation | https://git-scm.com/doc | 2026-11-19 | Control de versiones (etapa 5) |

## 6. Reglas para la siguiente fase académica

- No modificar el DOCX maestro ni el contenido publicado sin revisión y aprobación.
- Toda lección nueva debe incluir objetivo, teoría, ejemplo, ejercicio, criterio
  de evaluación y referencias con URL/fecha.
- Mantener la correspondencia 33/212/1946 y los 7 prerrequisitos, salvo decisión
  editorial documentada.
- No presentar una lección como desarrollada si solo existe su título.
- Las propuestas de objetivo (etapa 25) y cualquier enriquecimiento externo deben
  quedar en un documento de revisión antes de tocar `ascenso_3_1.json`.

## 7. Reproducción

```bash
# Verificar la fuente local (si está disponible)
sha256sum "$HOME/Descargas/PROYECTO_ASCENSO_Roadmap_Maestro_Consolidado_3_1_2026.docx"

# Cargar en un perfil aislado
CODEGUARD_DATA_DIR=/tmp/cg-inv \
DJANGO_SETTINGS_MODULE=config.settings.development \
python manage.py migrate --noinput
CODEGUARD_DATA_DIR=/tmp/cg-inv \
DJANGO_SETTINGS_MODULE=config.settings.development \
python manage.py cargar_ascenso
```

## 13. Actualización de contenido (2026-11-21)

| Comprobación | Resultado |
|---|---|
| Lecciones con cuerpo estructurado | 8 (módulo 0.1) |
| Lecciones con versión borrador | 8 |
| Lecciones aprobadas | 0 |
| Lecciones publicadas | 0 |
| Lecciones pendientes | 1.938 |
| Videos con enlace/metadatos verificados | 8 |
| Videos con revisión pedagógica aprobada | 0 |
| Fuentes únicas registradas para el lote | 13 |
| Referencias de fuente | 16 |

El contenido del módulo 0.1 se entrega como borrador editorial. No se alteró la
estructura oficial de 33 etapas, 212 módulos ni 1.946 lecciones. La etapa 25
sigue sin objetivo formal en la fuente maestra. Los videos tienen enlace y
metadatos verificados, pero **0 tienen revisión pedagógica aprobada**; esta se
registra por separado. El detalle y el flujo de publicación están en
[`CONTENIDO_ACADEMICO.md`](CONTENIDO_ACADEMICO.md).
