# Especificación de Requisitos de Software (SRS)

**Proyecto:** CodeGuard Pro (El arte de crear código. La ciencia de defenderlo.)
**Versión del Documento:** 2.2 (Revisión Incremento 2 — Electron + Django)
**Estándar de Referencia:** IEEE Std 830-1998 (Adaptado a prácticas modernas)  
**Fecha:** 5 de noviembre de 2026  
**Estado:** Documento base consolidado. Distingue explícitamente requisitos aprobados, decisiones pendientes y propuestas de arquitectura.  
**Cambios respecto a v1.0:** Incorporación de requisitos faltantes de evaluación, competencias, evidencias, laboratorios y vigencia documental. Precisión de decisiones de seguridad. Corrección y fijación del stack. Validación explícita de la integración ASCENSO. Matriz de trazabilidad completa con estados.
**Cambios respecto a v2.0 (primera revisión post-MVP):** Cambio de arquitectura de aplicación web en navegador a aplicación desktop independiente (Electron + Django embebido). Registro de versión .exe para Windows. Mejora de estética y estilado profesional.

**Cambios respecto a v2.1 (revisión Incremento 2):** Sustitución de PySide6/Qt por Electron como contenedor de escritorio. El servidor Django se empaqueta de forma autónoma con PyInstaller y electron-builder genera el instalador NSIS y la versión portable para Windows. Se incorpora el roadmap ASCENSO 3.1 completo (33 etapas, 212 módulos, 1 946 lecciones, 33 proyectos).

---

## 1. Introducción

### 1.1. Propósito
Este documento define formal, estructurada y verificablemente los requisitos funcionales, no funcionales, de datos y de seguridad para la construcción de una plataforma educativa personal monousuario, offline-first. Constituye la línea base técnica para diseño, implementación, pruebas y despliegue del MVP. Se distingue explícitamente entre requisitos aprobados, decisiones pendientes y propuestas de arquitectura.

### 1.2. Alcance del Producto
Aplicación desktop independiente, local, monousuario y offline-first, para gestionar la formación técnica del usuario mediante el Roadmap ASCENSO, biblioteca documental trazable, evaluaciones por competencias, laboratorios y portafolio de evidencias. La aplicación se ejecuta como un programa nativo de escritorio (no requiere navegador web externo) con servidor Django embebido en `127.0.0.1` y ventana nativa de Electron (Chromium).

*   **Incluye (MVP):** Roadmap ASCENSO (33 etapas representadas), importación y lectura de PDFs con detección de errores, base de conocimiento relacional, evaluaciones teórico-prácticas, registro detallado de resultados e intentos, gestión de competencias, registro de laboratorios, evidencias con integridad verificable, progreso, autenticación local, copias de seguridad protegidas.
*   **No incluye (Futuro):** IA integrada, ejecución de VMs/contenedores desde la plataforma, multiusuario, foros, sincronización cloud, OCR, videojuegos, multimedia integrada.

### 1.3. Definiciones, Acrónimos y Abreviaturas
*   **ASCENSO:** Roadmap formativo de 33 etapas (0 a 32).
*   **MVP:** Minimum Viable Product.
*   **Offline-first:** Prioridad de funcionamiento sin Internet.
*   **SRS:** Software Requirements Specification.
*   **FTS5:** Full-Text Search v5 de SQLite.
*   **LUKS:** Cifrado de disco Linux.
*   **HTMX:** Librería JS para interactividad vía atributos HTML.
*   **Argon2:** Algoritmo de hashing de contraseñas.
*   **MVT:** Model-View-Template (patrón de Django).
*   **CSP:** Content Security Policy.
*   **Aplicación desktop:** Programa nativo de escritorio que se ejecuta sin navegador web externo, con interfaz renderizada en ventana nativa de Electron (Chromium) y servidor Django embebido en localhost.

### 1.4. Referencias
*   PROYECTO ASCENSO — ROADMAP MAESTRO CONSOLIDADO 3.1 (fuente de verdad académica).
*   IEEE Std 830-1998.
*   Documentación oficial de Django, SQLite, PyMuPDF, HTMX, Bootstrap, Electron, PyInstaller y electron-builder.
*   OWASP ASVS, OWASP Top 10.
*   Fedora Linux 44 Release Notes.

### 1.5. Visión General del Documento
Sección 2: descripción general. Sección 3: requisitos específicos (RF, RNF, RD, RS). Sección 4: casos de uso. Sección 5: matriz de trazabilidad completa. Sección 6: decisiones, riesgos y evolución, con estados explícitos.

---

## 2. Descripción General

### 2.1. Perspectiva del Producto
Aplicación desktop independiente basada en un monolito modular Django con servidor embebido en `127.0.0.1` y ventana nativa de Electron. Sustituye la dispersión de herramientas (lectores, notas, hojas de cálculo) centralizando el proceso educativo. No depende de servicios en la nube ni de navegador web externo.

### 2.2. Funciones del Producto
1.  Identidad y acceso local con rescate seguro.
2.  Gestión académica (roadmap, etapas, módulos, lecciones, actividades, prerrequisitos).
3.  Gestión de competencias y criterios de finalización configurables.
4.  Gestión documental (importación, detección de errores, extracción, indexación, visor, anotaciones).
5.  Base de conocimiento (conceptos, relaciones, trazabilidad precisa).
6.  Evaluación (teórica, práctica, proyectos, rúbricas, intentos, retroalimentación).
7.  Gestión de evidencias (integridad, asociaciones múltiples).
8.  Laboratorios (guías, resultados, comandos, evidencias).
9.  Administración (backups protegidos, exportación, auditoría).
10. Vigencia y revisión de contenidos.
11. Advertencias éticas/legales.

### 2.3. Características de los Usuarios
Usuario único: estudiante con perfil técnico (ciberseguridad/backend), capaz de ejecutar comandos, gestionar entornos locales y comprender conceptos avanzados.

### 2.4. Restricciones
*   **Hardware:** HP 240 G10, Intel Core i3-N305 (8 núcleos), 8 GB RAM (2.9 GiB disponibles en el entorno actual), SSD NVMe 238.5 GB (108 GB libres).
*   **SO:** Fedora Linux 44 (Workstation Edition).
*   **Cifrado de disco:** LUKS activo en la partición principal.
*   **Entorno:** Entorno de escritorio con Electron (Chromium), Python 3.x y SQLite con FTS5. No requiere navegador web externo.

### 2.5. Suposiciones y Dependencias
*   El usuario posee los PDFs de estudio.
*   El entorno de escritorio incluye Chromium embebido mediante Electron y Node.js para el proceso principal.
*   Python y SQLite están disponibles en el entorno Fedora.
*   Las versiones específicas del stack se fijan en la Sección 6.1.

---

## 3. Requisitos Específicos

**Convenciones:**
*   **Prioridad:** MVP (imprescindible), IMP (importante, posterior cercano), FUT (futuro).
*   **Estado:** APROBADO, PENDIENTE, PROPUESTO.
*   **Módulo:** Identidad, Académico, Competencias, Documental, Conocimiento, Evaluación, Evidencias, Laboratorios, Administración, Vigencia, Ética.

### 3.1. Requisitos de Interfaces Externas

*   **3.1.1. UI:** Ventana desktop nativa de Electron con Chromium embebido. Diseño profesional, responsivo, accesible, Bootstrap 5 y 12 temas CSS con glassmorphism para la capa web interna. Servida localmente sin CDN.
*   **3.1.2. Hardware:** Sistema de archivos local para lectura de PDFs y escritura de evidencias/backups.
*   **3.1.3. Software:** Servidor Django embebido en `127.0.0.1`, SQLite con FTS5, PyMuPDF, Electron, PyInstaller y electron-builder.
*   **3.1.4. Comunicación:** HTTP sobre `127.0.0.1` exclusivamente (servidor embebido, no expuesto a red). No exponer en `0.0.0.0`.

### 3.2. Requisitos Funcionales

#### 3.2.1. Identidad y Acceso (Módulo: Identidad)
*   **RF-001:** Autenticación local mediante contraseña maestra. [MVP · APROBADO]
*   **RF-002:** Cierre de sesión por inactividad configurable (defecto 15 min). [MVP · APROBADO]
*   **RF-003:** Configuración inicial guiada: creación de contraseña, generación de frase de rescate, aceptación de términos. [MVP · APROBADO]
*   **RF-004:** Generación de frase de rescate de alta entropía (≥128 bits), mostrada una sola vez, almacenada como hash Argon2, uso exclusivo para recuperación, invalidada tras uso. [MVP · APROBADO]
*   **RF-005:** Registro de auditoría de inicios/cierres de sesión y fallos. [MVP · APROBADO]
*   **RF-006:** Bloqueo local tras N intentos fallidos (configurable). [MVP · PENDIENTE — definir N]

#### 3.2.2. Gestión Académica (Módulo: Académico)
*   **RF-010:** Cargar y representar las **33 etapas** de ASCENSO desde el documento maestro 3.1. [MVP · APROBADO]
*   **RF-011:** Mostrar todas las etapas; las no desarrolladas se marcan como "No desarrollada en MVP" pero permanecen visibles. [MVP · APROBADO]
*   **RF-012:** Mostrar dependencias entre etapas según el documento maestro. [MVP · APROBADO]
*   **RF-013:** Definir módulos, lecciones y actividades con objetivos y prerrequisitos. [MVP · APROBADO]
*   **RF-014:** Configurar prerrequisitos por elemento. [MVP · APROBADO]
*   **RF-015:** Configurar criterios de finalización por etapa/módulo. [MVP · APROBADO]
*   **RF-016:** Registrar progreso por etapa, módulo, lección y actividad. [MVP · APROBADO]
*   **RF-017:** Bloquear contenido con prerrequisitos incumplidos. [MVP · APROBADO]
*   **RF-018:** Registrar tiempo dedicado por actividad. [MVP · PROPUESTO]
*   **RF-019:** Permitir crear rutas personalizadas adicionales a ASCENSO. [FUT · PROPUESTO]

#### 3.2.3. Competencias y Criterios de Finalización (Módulo: Competencias)
*   **RF-020:** Definir competencias con evidencia observable. [MVP · APROBADO]
*   **RF-021:** Definir niveles de dominio por competencia (ej. básico, intermedio, avanzado). [MVP · APROBADO]
*   **RF-022:** Definir criterios de evaluación por competencia. [MVP · APROBADO]
*   **RF-023:** Definir requisitos de evidencia por competencia. [MVP · APROBADO]
*   **RF-024:** Configurar reglas de finalización combinables (ej. 3 lecciones + 1 examen ≥ 80% + 1 proyecto + 1 evidencia). [MVP · APROBADO]
*   **RF-025:** Validar automáticamente el cumplimiento de criterios. [MVP · APROBADO]
*   **RF-026:** Permitir anulación manual de criterios con justificación registrada. [MVP · PROPUESTO]
*   **RF-027:** Registrar el logro de competencia (fecha, nivel, evidencia). [MVP · APROBADO]
*   **RF-028:** Panel de competencias con estado por nivel. [MVP · PROPUESTO]
*   **RF-029:** Generar informe de competencias. [IMP · PROPUESTO]

#### 3.2.4. Gestión Documental (Módulo: Documental)
*   **RF-030:** Importar PDFs desde el sistema de archivos. [MVP · APROBADO]
*   **RF-031:** Extraer metadatos (título, autor, páginas, TOC). [MVP · APROBADO]
*   **RF-032:** Extraer texto nativo. [MVP · APROBADO]
*   **RF-033:** Detectar PDFs sin texto extraíble (escaneados) y notificar. [MVP · APROBADO]
*   **RF-034:** Detectar duplicados por hash y notificar antes de importar. [MVP · APROBADO]
*   **RF-035:** Manejar PDFs dañados o corruptos con mensaje de error explícito. [MVP · APROBADO]
*   **RF-036:** Manejar PDFs protegidos con contraseña con mensaje explícito. [MVP · APROBADO]
*   **RF-037:** Procesar PDFs grandes por lotes para controlar memoria. [MVP · APROBADO]
*   **RF-038:** Almacenar metadatos, licencia y estado de vigencia. [MVP · APROBADO]
*   **RF-039:** Indexar texto en FTS5. [MVP · APROBADO]
*   **RF-040:** Visor con navegación, zoom y anotaciones. [MVP · APROBADO]
*   **RF-041:** Asociar documento o fragmento (página/capítulo) a etapa/lección. [MVP · APROBADO]
*   **RF-042:** Búsqueda de texto completo. [MVP · APROBADO]
*   **RF-043:** Navegar desde resultado de búsqueda al documento y página exacta. [MVP · APROBADO]
*   **RF-044:** Registrar errores de importación en log con detalle. [MVP · APROBADO]

#### 3.2.5. Base de Conocimiento (Módulo: Conocimiento)
*   **RF-050:** Crear conceptos con definición. [MVP · APROBADO]
*   **RF-051:** Crear relaciones tipadas entre conceptos. [MVP · APROBADO]
*   **RF-052:** Vincular concepto a fragmento documental (documento, capítulo, página, posición). [MVP · APROBADO]
*   **RF-053:** Vincular concepto a actividad/evaluación. [MVP · APROBADO]
*   **RF-054:** Buscar conceptos. [MVP · APROBADO]
*   **RF-055:** Detectar duplicados/conflictos de conceptos (manual o asistido). [MVP · PROPUESTO]
*   **RF-056:** Registrar estado de vigencia del concepto. [MVP · APROBADO]

#### 3.2.6. Evaluación (Módulo: Evaluación)
*   **RF-060:** Crear preguntas de selección múltiple. [MVP · APROBADO]
*   **RF-061:** Crear preguntas abiertas. [MVP · APROBADO]
*   **RF-062:** Crear ejercicios prácticos con rúbrica. [MVP · APROBADO]
*   **RF-063:** Crear proyectos con rúbrica. [MVP · APROBADO]
*   **RF-064:** Crear demostraciones de competencia. [MVP · PROPUESTO]
*   **RF-065:** Configurar instrumentos por actividad. [MVP · APROBADO]
*   **RF-066:** Registrar resultados con timestamp. [MVP · APROBADO]
*   **RF-067:** Registrar múltiples intentos por evaluación. [MVP · APROBADO]
*   **RF-068:** Registrar retroalimentación por evaluación. [MVP · APROBADO]
*   **RF-069:** Calcular puntuación según rúbrica. [MVP · APROBADO]
*   **RF-070:** Historial de evaluaciones por actividad. [MVP · APROBADO]
*   **RF-071:** Informe de evaluación. [MVP · PROPUESTO]

#### 3.2.7. Evidencias (Módulo: Evidencias)
*   **RF-080:** Subir evidencias (imagen, texto, archivo). [MVP · APROBADO]
*   **RF-081:** Asociar evidencia a actividad. [MVP · APROBADO]
*   **RF-082:** Asociar evidencia a competencia. [MVP · APROBADO]
*   **RF-083:** Asociar evidencia a laboratorio. [MVP · APROBADO]
*   **RF-084:** Calcular y almacenar SHA-256. [MVP · APROBADO]
*   **RF-085:** Verificar integridad de evidencias. [MVP · APROBADO]
*   **RF-086:** Impedir ejecución de archivos subidos (validación MIME/extensión, permisos sin ejecución, servido como adjunto). [MVP · APROBADO]
*   **RF-087:** Limitar tamaño y tipo de archivo. [MVP · APROBADO]
*   **RF-088:** Portafolio por etapa/competencia. [MVP · APROBADO]
*   **RF-089:** Exportar portafolio. [FUT · PROPUESTO]

#### 3.2.8. Laboratorios (Módulo: Laboratorios)
*   **RF-090:** Crear guías con pasos secuenciales y resultados esperados. [MVP · APROBADO]
*   **RF-091:** Registrar comandos ejecutados por paso. [MVP · APROBADO]
*   **RF-092:** Registrar resultados/observaciones por paso. [MVP · APROBADO]
*   **RF-093:** Adjuntar capturas por paso. [MVP · APROBADO]
*   **RF-094:** Registrar inicio/fin y duración. [MVP · APROBADO]
*   **RF-095:** Registrar entorno/contexto del laboratorio. [MVP · PROPUESTO]
*   **RF-096:** Generar informe de laboratorio. [MVP · PROPUESTO]
*   **RF-097:** Vincular laboratorio a etapa/competencia. [MVP · APROBADO]

#### 3.2.9. Administración y Backups (Módulo: Administración)
*   **RF-100:** Crear backup manual (tar.gz: SQLite + archivos). [MVP · APROBADO]
*   **RF-101:** Programar backup automático. [MVP · PROPUESTO]
*   **RF-102:** Verificar integridad del backup (hash pre/post, validación de contenido). [MVP · APROBADO]
*   **RF-103:** Restaurar desde backup. [MVP · APROBADO]
*   **RF-104:** Validar contenido del backup antes de restaurar (evitar archivos maliciosos). [MVP · APROBADO]
*   **RF-105:** Ofrecer opción de cifrado del backup. [MVP · PROPUESTO — importante si se traslada a otro dispositivo]
*   **RF-106:** Exportar datos en formato abierto. [MVP · PROPUESTO]
*   **RF-107:** Importar datos desde formato abierto. [FUT · PROPUESTO]
*   **RF-108:** Visor de log de auditoría. [MVP · APROBADO]
*   **RF-109:** Limpieza de archivos temporales. [MVP · APROBADO]

#### 3.2.10. Vigencia y Revisión (Módulo: Vigencia)
*   **RF-110:** Registrar estado de vigencia (vigente, obsoleto, pendiente revisión). [MVP · APROBADO]
*   **RF-111:** Registrar fecha de revisión. [MVP · APROBADO]
*   **RF-112:** Alertar sobre contenido potencialmente obsoleto según reglas configurables. [MVP · PROPUESTO]
*   **RF-113:** Flujo de revisión manual. [MVP · APROBADO]
*   **RF-114:** Registrar decisión de revisión (mantener, actualizar, retirar). [MVP · APROBADO]
*   **RF-115:** Historial de cambios de contenido. [MVP · PROPUESTO]

#### 3.2.11. Ética y Advertencias (Módulo: Ética)
*   **RF-120:** Mostrar advertencia en contenido ofensivo. [MVP · APROBADO]
*   **RF-121:** Requerir aceptación explícita antes de acceder a contenido ofensivo/laboratorios. [MVP · APROBADO]
*   **RF-122:** Registrar aceptación de términos. [MVP · APROBADO]
*   **RF-123:** Proveer guías de uso ético. [MVP · APROBADO]

### 3.3. Requisitos No Funcionales

*   **RNF-001:** 100% de funciones del MVP operan sin Internet. [MVP · APROBADO]
*   **RNF-002:** Servidor local escucha exclusivamente en `127.0.0.1`. [MVP · APROBADO]
*   **RNF-003:** Prueba de rendimiento formal: medir RAM en reposo, tiempo de respuesta y búsqueda; definir entorno de prueba. [MVP · APROBADO — el umbral de 300 MB queda como objetivo a validar, no como garantía]
*   **RNF-004:** Búsqueda FTS5 < 2 s para hasta 50 libros. [MVP · APROBADO]
*   **RNF-005:** Compatibilidad con Fedora 44 y distribuciones con Python 3.10+. [MVP · APROBADO]
*   **RNF-006:** UI responsiva en 1366x768. [MVP · APROBADO]
*   **RNF-007:** Arquitectura MVT con separación de responsabilidades. [MVP · APROBADO]
*   **RNF-008:** Integridad transaccional en SQLite. [MVP · APROBADO]
*   **RNF-009:** Protección CSRF, XSS, SQLi. [MVP · APROBADO]
*   **RNF-010:** Timeout de sesión probado; acceso directo a archivos no debe evadir autenticación. [MVP · APROBADO]
*   **RNF-011:** Integridad de backups verificada. [MVP · APROBADO]
*   **RNF-012:** Python en versión estable compatible con Django. [MVP · APROBADO — fijar en implementación]
*   **RNF-013:** Django en versión con soporte vigente (LTS preferente). [MVP · APROBADO — fijar en implementación]
*   **RNF-014:** SQLite compilado con FTS5 verificado. [MVP · APROBADO]
*   **RNF-015:** HTMX y Bootstrap servidos localmente, sin CDN. [MVP · APROBADO]
*   **RNF-016:** PyMuPDF en modo batch para controlar memoria. [MVP · APROBADO]
*   **RNF-017:** Logging y auditoría. [MVP · APROBADO]
*   **RNF-018:** Sin telemetría. [MVP · APROBADO]
*   **RNF-019:** Documentación de instalación y actualización. [MVP · APROBADO]
*   **RNF-020:** Sesiones con timeout y limpieza de datos sensibles en memoria. [MVP · PROPUESTO]

### 3.4. Requisitos de Datos

*   **RD-001:** Credenciales de usuario (hash Argon2). [APROBADO]
*   **RD-002:** Frase de rescate (hash Argon2, alta entropía, mostrada una vez, invalidada tras uso). [APROBADO]
*   **RD-003:** Sesión server-side con timeout. [APROBADO]
*   **RD-004:** Jerarquía académica (roadmap, etapa, módulo, lección, actividad). [APROBADO]
*   **RD-005:** Prerrequisitos (relaciones). [APROBADO]
*   **RD-006:** Criterios de finalización (reglas configurables). [APROBADO]
*   **RD-007:** Competencias, niveles y criterios. [APROBADO]
*   **RD-008:** Instrumentos de evaluación y rúbricas. [APROBADO]
*   **RD-009:** Resultados, intentos y retroalimentación. [APROBADO]
*   **RD-010:** Metadatos documentales (título, autor, páginas, licencia, hash, estado, errores). [APROBADO]
*   **RD-011:** Fragmentos documentales (página, capítulo, texto, posición). [APROBADO]
*   **RD-012:** Índice FTS5. [APROBADO]
*   **RD-013:** Conceptos y relaciones. [APROBADO]
*   **RD-014:** Vínculos concepto-fragmento-actividad. [APROBADO]
*   **RD-015:** Evidencias (ruta, tipo, tamaño, hash, asociaciones). [APROBADO]
*   **RD-016:** Guías de laboratorio y resultados. [APROBADO]
*   **RD-017:** Progreso. [APROBADO]
*   **RD-018:** Vigencia y revisión. [APROBADO]
*   **RD-019:** Auditoría. [APROBADO]
*   **RD-020:** Metadatos de backup. [APROBADO]
*   **RD-021:** Configuración. [APROBADO]
*   **RD-022:** Log de errores de importación. [APROBADO]

### 3.5. Requisitos de Seguridad

*   **RS-001:** Autenticación local obligatoria. [MVP · APROBADO]
*   **RS-002:** Argon2 para hash de contraseña y frase de rescate. [MVP · APROBADO]
*   **RS-003:** Frase de rescate: ≥128 bits de entropía, mostrada una vez, almacenada como hash, de un solo uso. [MVP · APROBADO]
*   **RS-004:** Servidor bind exclusivo a `127.0.0.1`. [MVP · APROBADO]
*   **RS-005:** Validación de archivos subidos (MIME, extensión, tamaño). [MVP · APROBADO]
*   **RS-006:** Archivos subidos fuera del web root; servidos como `Content-Disposition: attachment`; sin permisos de ejecución. [MVP · APROBADO]
*   **RS-007:** Integridad de backup verificada (hash, validación de contenido). [MVP · APROBADO]
*   **RS-008:** Opción de cifrado de backup para traslado a otros dispositivos. [MVP · PROPUESTO]
*   **RS-009:** Timeout de sesión probado; acceso directo a archivos no evade autenticación. [MVP · APROBADO]
*   **RS-010:** CSRF en todas las peticiones que cambian estado. [MVP · APROBADO]
*   **RS-011:** XSS: escape de salida y CSP. [MVP · APROBADO]
*   **RS-012:** SQLi: ORM con consultas parametrizadas. [MVP · APROBADO]
*   **RS-013:** Cabeceras de seguridad (CSP, X-Frame-Options, etc.). [MVP · APROBADO]
*   **RS-014:** Auditoría de eventos de seguridad. [MVP · APROBADO]
*   **RS-015:** Documentar que LUKS protege en reposo con dispositivo apagado; los backups trasladados a otro dispositivo no quedan automáticamente protegidos. [MVP · APROBADO]
*   **RS-016:** Política de contraseñas (longitud mínima, complejidad). [MVP · APROBADO]
*   **RS-017:** Bloqueo local tras N intentos fallidos. [MVP · PENDIENTE — definir N]
*   **RS-018:** Minimización de datos sensibles. [MVP · APROBADO]
*   **RS-019:** Dependencias actualizadas y documentadas. [MVP · APROBADO]
*   **RS-020:** No exponer errores internos en la UI. [MVP · APROBADO]

---

## 4. Casos de Uso Principales

### CU-001: Configuración Inicial
*   **Actor:** Usuario (primer arranque).
*   **Flujo:** Crear contraseña → Generar y mostrar frase de rescate (una vez) → Aceptar términos → Acceso al panel.

### CU-002: Importación y Procesamiento de un Libro
*   **Actor:** Usuario.
*   **Flujo:** Seleccionar PDF → Validar (dañado, protegido, duplicado, sin texto) → Extraer metadatos y texto → Indexar FTS5 → Asociar a etapa → Disponible en biblioteca.
*   **Flujos alternativos:** PDF dañado → mensaje; PDF protegido → mensaje; duplicado → confirmar; sin texto → advertencia.

### CU-003: Completar una Etapa con Competencia
*   **Actor:** Usuario.
*   **Flujo:** Revisar contenidos → Aprobar evaluación teórica → Entregar proyecto con rúbrica → Subir evidencias → Sistema valida criterios → Marca etapa y competencia como logradas.

### CU-004: Búsqueda en la Base de Conocimiento
*   **Actor:** Usuario.
*   **Flujo:** Ingresar término → Buscar en conceptos y FTS5 → Mostrar definición, fragmentos de documentos y actividades relacionadas → Navegar al documento y página exacta.

### CU-005: Registro de Laboratorio
*   **Actor:** Usuario.
*   **Flujo:** Abrir guía → Ejecutar pasos → Registrar comandos y resultados → Adjuntar capturas → Finalizar → Generar informe (si aplica) → Vincular a etapa/competencia.

### CU-006: Creación y Restauración de Backup
*   **Actor:** Usuario.
*   **Flujo (crear):** Seleccionar "Crear backup" → Empaquetar SQLite + archivos → Calcular hash → Guardar en ruta especificada.
*   **Flujo (restaurar):** Seleccionar backup → Validar contenido → Verificar hash → Restaurar.

### CU-007: Revisión de Vigencia
*   **Actor:** Usuario.
*   **Flujo:** Revisar lista de contenidos marcados como obsoletos o pendientes → Decidir (mantener, actualizar, retirar) → Registrar decisión y fecha.

### CU-008: Gestión de Contenido Ofensivo
*   **Actor:** Usuario.
*   **Flujo:** Acceder a etapa ofensiva → Ver advertencia → Aceptar términos → Registrar aceptación → Acceder al contenido.

---

## 5. Matriz de Trazabilidad Completa

**Columnas:** ID · Descripción breve · Prioridad · Módulo · Criterio de aceptación · Prueba asociada · Estado · Fuente/Referencia.

| ID | Descripción | Prioridad | Módulo | Criterio de aceptación | Prueba | Estado | Fuente |
|:---|:---|:---|:---|:---|:---|:---|:---|
| RF-001 | Autenticación local | MVP | Identidad | Login con credenciales válidas | T-001 | APROBADO | Necesidad de privacidad |
| RF-002 | Cierre por inactividad | MVP | Identidad | Sesión expira tras 15 min | T-002 | APROBADO | Seguridad local |
| RF-003 | Configuración inicial | MVP | Identidad | Wizard completa en primer arranque | T-003 | APROBADO | UX |
| RF-004 | Frase de rescate | MVP | Identidad | Alta entropía, hash, un uso | T-004 | APROBADO | RS-003 |
| RF-005 | Auditoría de acceso | MVP | Identidad | Log con eventos | T-005 | APROBADO | RS-014 |
| RF-006 | Bloqueo tras N fallos | MVP | Identidad | Bloqueo configurable | T-006 | PENDIENTE | RS-017 |
| RF-010 | Cargar 33 etapas | MVP | Académico | 33 etapas representadas | T-010 | APROBADO | ASCENSO 3.1 |
| RF-011 | Etapas no desarrolladas visibles | MVP | Académico | Marcadas como "No desarrollada" | T-011 | APROBADO | Validación E |
| RF-012 | Dependencias de etapas | MVP | Académico | Relaciones del documento maestro | T-012 | APROBADO | ASCENSO 3.1 |
| RF-013 | Módulos/lecciones/actividades | MVP | Académico | Creación y visualización | T-013 | APROBADO | ASCENSO 3.1 |
| RF-014 | Prerrequisitos | MVP | Académico | Bloqueo por prerrequisitos | T-014 | APROBADO | Académico |
| RF-015 | Criterios de finalización | MVP | Académico | Reglas configurables | T-015 | APROBADO | RF-024 |
| RF-016 | Progreso | MVP | Académico | Estado por elemento | T-016 | APROBADO | Académico |
| RF-017 | Bloqueo por prerrequisitos | MVP | Académico | Contenido bloqueado | T-017 | APROBADO | Académico |
| RF-018 | Tiempo por actividad | MVP | Académico | Registro de tiempo | T-018 | PROPUESTO | Analítica |
| RF-019 | Rutas personalizadas | FUT | Académico | Crear ruta propia | T-019 | PROPUESTO | Extensibilidad |
| RF-020 | Competencias | MVP | Competencias | Definir con evidencia | T-020 | APROBADO | Aprendizaje por competencias |
| RF-021 | Niveles de dominio | MVP | Competencias | Básico/intermedio/avanzado | T-021 | APROBADO | Competencias |
| RF-022 | Criterios por competencia | MVP | Competencias | Criterios verificables | T-022 | APROBADO | Competencias |
| RF-023 | Requisitos de evidencia | MVP | Competencias | Evidencia exigida | T-023 | APROBADO | Competencias |
| RF-024 | Reglas combinables | MVP | Competencias | Reglas configurables | T-024 | APROBADO | RF-015 |
| RF-025 | Validación automática | MVP | Competencias | Validación de criterios | T-025 | APROBADO | Competencias |
| RF-026 | Anulación manual | MVP | Competencias | Con justificación | T-026 | PROPUESTO | Flexibilidad |
| RF-027 | Registro de logro | MVP | Competencias | Fecha, nivel, evidencia | T-027 | APROBADO | Competencias |
| RF-028 | Panel de competencias | MVP | Competencias | Estado por nivel | T-028 | PROPUESTO | UX |
| RF-029 | Informe de competencias | IMP | Competencias | Generar informe | T-029 | PROPUESTO | Evaluación |
| RF-030 | Importar PDFs | MVP | Documental | Importación correcta | T-030 | APROBADO | Bibliografía |
| RF-031 | Metadatos | MVP | Documental | Título, autor, páginas, TOC | T-031 | APROBADO | Bibliografía |
| RF-032 | Texto nativo | MVP | Documental | Texto extraído | T-032 | APROBADO | Bibliografía |
| RF-033 | PDFs sin texto | MVP | Documental | Notificación | T-033 | APROBADO | RF-033 |
| RF-034 | Duplicados | MVP | Documental | Detección por hash | T-034 | APROBADO | Integridad |
| RF-035 | PDFs dañados | MVP | Documental | Mensaje explícito | T-035 | APROBADO | Robustez |
| RF-036 | PDFs protegidos | MVP | Documental | Mensaje explícito | T-036 | APROBADO | Robustez |
| RF-037 | Procesamiento por lotes | MVP | Documental | Memoria controlada | T-037 | APROBADO | RNF-016 |
| RF-038 | Metadatos y vigencia | MVP | Documental | Estado y licencia | T-038 | APROBADO | Licencias |
| RF-039 | FTS5 | MVP | Documental | Búsqueda indexada | T-039 | APROBADO | RNF-004 |
| RF-040 | Visor y anotaciones | MVP | Documental | Lectura y anotación | T-040 | APROBADO | UX |
| RF-041 | Asociar fragmento | MVP | Documental | Vínculo a etapa/lección | T-041 | APROBADO | Trazabilidad |
| RF-042 | Búsqueda global | MVP | Documental | Resultados relevantes | T-042 | APROBADO | RNF-004 |
| RF-043 | Navegar a página | MVP | Documental | Salto a página exacta | T-043 | APROBADO | UX |
| RF-044 | Log de importación | MVP | Documental | Errores registrados | T-044 | APROBADO | Robustez |
| RF-050 | Crear conceptos | MVP | Conocimiento | Concepto con definición | T-050 | APROBADO | Modelo híbrido |
| RF-051 | Relaciones tipadas | MVP | Conocimiento | Relación entre conceptos | T-051 | APROBADO | Modelo híbrido |
| RF-052 | Vínculo concepto-fragmento | MVP | Conocimiento | Documento, capítulo, página | T-052 | APROBADO | Trazabilidad |
| RF-053 | Vínculo concepto-actividad | MVP | Conocimiento | Concepto asociado | T-053 | APROBADO | Trazabilidad |
| RF-054 | Búsqueda de conceptos | MVP | Conocimiento | Resultados | T-054 | APROBADO | UX |
| RF-055 | Duplicados/conflictos | MVP | Conocimiento | Detección manual/asistida | T-055 | PROPUESTO | Calidad |
| RF-056 | Vigencia de concepto | MVP | Conocimiento | Estado registrado | T-056 | APROBADO | RF-110 |
| RF-060 | Preguntas MC | MVP | Evaluación | Crear y evaluar | T-060 | APROBADO | Evaluación |
| RF-061 | Preguntas abiertas | MVP | Evaluación | Crear y evaluar | T-061 | APROBADO | Evaluación |
| RF-062 | Ejercicios con rúbrica | MVP | Evaluación | Rúbrica funcional | T-062 | APROBADO | Evaluación |
| RF-063 | Proyectos con rúbrica | MVP | Evaluación | Rúbrica funcional | T-063 | APROBADO | Evaluación |
| RF-064 | Demostraciones | MVP | Evaluación | Registro de demostración | T-064 | PROPUESTO | Competencias |
| RF-065 | Instrumentos por actividad | MVP | Evaluación | Configuración | T-065 | APROBADO | Evaluación |
| RF-066 | Resultados con timestamp | MVP | Evaluación | Registro temporal | T-066 | APROBADO | Evaluación |
| RF-067 | Múltiples intentos | MVP | Evaluación | Intentos registrados | T-067 | APROBADO | Evaluación |
| RF-068 | Retroalimentación | MVP | Evaluación | Feedback registrado | T-068 | APROBADO | Evaluación |
| RF-069 | Puntuación por rúbrica | MVP | Evaluación | Cálculo correcto | T-069 | APROBADO | Evaluación |
| RF-070 | Historial | MVP | Evaluación | Historial completo | T-070 | APROBADO | Evaluación |
| RF-071 | Informe de evaluación | MVP | Evaluación | Informe generado | T-071 | PROPUESTO | Evaluación |
| RF-080 | Subir evidencias | MVP | Evidencias | Carga correcta | T-080 | APROBADO | Evidencias |
| RF-081 | Asociar a actividad | MVP | Evidencias | Vínculo | T-081 | APROBADO | Evidencias |
| RF-082 | Asociar a competencia | MVP | Evidencias | Vínculo | T-082 | APROBADO | Evidencias |
| RF-083 | Asociar a laboratorio | MVP | Evidencias | Vínculo | T-083 | APROBADO | Evidencias |
| RF-084 | SHA-256 | MVP | Evidencias | Hash almacenado | T-084 | APROBADO | RS-007 |
| RF-085 | Verificar integridad | MVP | Evidencias | Verificación | T-085 | APROBADO | RS-007 |
| RF-086 | Impedir ejecución | MVP | Evidencias | Sin ejecución | T-086 | APROBADO | RS-005/006 |
| RF-087 | Límite de archivos | MVP | Evidencias | Límite aplicado | T-087 | APROBADO | RS-005 |
| RF-088 | Portafolio | MVP | Evidencias | Vista por etapa | T-088 | APROBADO | UX |
| RF-089 | Exportar portafolio | FUT | Evidencias | Exportación | T-089 | PROPUESTO | Extensibilidad |
| RF-090 | Guías de laboratorio | MVP | Laboratorios | Pasos definidos | T-090 | APROBADO | Laboratorios |
| RF-091 | Comandos por paso | MVP | Laboratorios | Registro | T-091 | APROBADO | Laboratorios |
| RF-092 | Resultados por paso | MVP | Laboratorios | Registro | T-092 | APROBADO | Laboratorios |
| RF-093 | Capturas por paso | MVP | Laboratorios | Adjuntos | T-093 | APROBADO | Laboratorios |
| RF-094 | Inicio/fin/duración | MVP | Laboratorios | Registro temporal | T-094 | APROBADO | Laboratorios |
| RF-095 | Entorno/contexto | MVP | Laboratorios | Registro | T-095 | PROPUESTO | Laboratorios |
| RF-096 | Informe de laboratorio | MVP | Laboratorios | Informe generado | T-096 | PROPUESTO | Laboratorios |
| RF-097 | Vincular a etapa | MVP | Laboratorios | Vínculo | T-097 | APROBADO | Laboratorios |
| RF-100 | Backup manual | MVP | Administración | Archivo generado | T-100 | APROBADO | Recuperación |
| RF-101 | Backup automático | MVP | Administración | Programación | T-101 | PROPUESTO | Recuperación |
| RF-102 | Integridad de backup | MVP | Administración | Hash verificado | T-102 | APROBADO | RS-007 |
| RF-103 | Restaurar | MVP | Administración | Restauración correcta | T-103 | APROBADO | Recuperación |
| RF-104 | Validar contenido | MVP | Administración | Validación previa | T-104 | APROBADO | RS-007 |
| RF-105 | Cifrar backup | MVP | Administración | Opción disponible | T-105 | PROPUESTO | RS-008 |
| RF-106 | Exportar abierto | MVP | Administración | Formato abierto | T-106 | PROPUESTO | Portabilidad |
| RF-107 | Importar abierto | FUT | Administración | Importación | T-107 | PROPUESTO | Portabilidad |
| RF-108 | Visor de auditoría | MVP | Administración | Visualización | T-108 | APROBADO | RS-014 |
| RF-109 | Limpieza temporal | MVP | Administración | Limpieza | T-109 | APROBADO | Mantenimiento |
| RF-110 | Estado de vigencia | MVP | Vigencia | Registro | T-110 | APROBADO | RF-056 |
| RF-111 | Fecha de revisión | MVP | Vigencia | Registro | T-111 | APROBADO | Vigencia |
| RF-112 | Alerta de obsolescencia | MVP | Vigencia | Alerta configurable | T-112 | PROPUESTO | Vigencia |
| RF-113 | Flujo de revisión | MVP | Vigencia | Revisión manual | T-113 | APROBADO | Vigencia |
| RF-114 | Decisión de revisión | MVP | Vigencia | Decisión registrada | T-114 | APROBADO | Vigencia |
| RF-115 | Historial de cambios | MVP | Vigencia | Historial | T-115 | PROPUESTO | Vigencia |
| RF-120 | Advertencia ofensiva | MVP | Ética | Advertencia visible | T-120 | APROBADO | RS-009 |
| RF-121 | Aceptación explícita | MVP | Ética | Términos aceptados | T-121 | APROBADO | RS-009 |
| RF-122 | Registro de aceptación | MVP | Ética | Registro | T-122 | APROBADO | RS-014 |
| RF-123 | Guía ética | MVP | Ética | Guía disponible | T-123 | APROBADO | RS-009 |
| RNF-001 | Offline | MVP | Global | Sin red funciona | T-200 | APROBADO | Restricción |
| RNF-002 | Bind 127.0.0.1 | MVP | Global | No expuesto | T-201 | APROBADO | RS-004 |
| RNF-003 | Prueba de rendimiento | MVP | Global | Entorno definido y medido | T-202 | APROBADO | Medición |
| RNF-004 | Búsqueda < 2s | MVP | Documental | 50 libros | T-203 | APROBADO | Rendimiento |
| RNF-005 | Compatibilidad Fedora | MVP | Global | Fedora 44 | T-204 | APROBADO | Entorno |
| RNF-006 | UI 1366x768 | MVP | UI | Responsiva | T-205 | APROBADO | UX |
| RNF-007 | MVT | MVP | Global | Separación | T-206 | APROBADO | Mantenibilidad |
| RNF-008 | Transacciones | MVP | Global | Integridad | T-207 | APROBADO | Datos |
| RNF-009 | CSRF/XSS/SQLi | MVP | Global | Protecciones | T-208 | APROBADO | RS-010/011/012 |
| RNF-010 | Timeout probado | MVP | Identidad | Prueba directa | T-209 | APROBADO | RS-009 |
| RNF-011 | Backup íntegro | MVP | Administración | Verificación | T-210 | APROBADO | RS-007 |
| RNF-012 | Python estable | MVP | Global | Versión fijada | T-211 | APROBADO | Stack |
| RNF-013 | Django soportado | MVP | Global | Versión fijada | T-212 | APROBADO | Stack |
| RNF-014 | FTS5 verificado | MVP | Documental | Compilación | T-213 | APROBADO | Stack |
| RNF-015 | Assets locales | MVP | UI | Sin CDN | T-214 | APROBADO | Offline |
| RNF-016 | PyMuPDF batch | MVP | Documental | Memoria controlada | T-215 | APROBADO | RNF-016 |
| RNF-017 | Logging | MVP | Global | Log generado | T-216 | APROBADO | Auditoría |
| RNF-018 | Sin telemetría | MVP | Global | Sin llamadas | T-217 | APROBADO | Privacidad |
| RNF-019 | Documentación | MVP | Global | Guía disponible | T-218 | APROBADO | Mantenibilidad |
| RNF-020 | Sesión limpia | MVP | Identidad | Memoria limpia | T-219 | PROPUESTO | RS-009 |
| RS-001 | Auth obligatoria | MVP | Identidad | Sin acceso anónimo | T-300 | APROBADO | Seguridad |
| RS-002 | Argon2 | MVP | Identidad | Hash Argon2 | T-301 | APROBADO | Seguridad |
| RS-003 | Frase de rescate | MVP | Identidad | ≥128 bits, hash, un uso | T-302 | APROBADO | Seguridad |
| RS-004 | Bind 127.0.0.1 | MVP | Global | Sin 0.0.0.0 | T-303 | APROBADO | Seguridad |
| RS-005 | Validación de archivos | MVP | Evidencias | MIME/extensión/tamaño | T-304 | APROBADO | Seguridad |
| RS-006 | Archivos fuera de web root | MVP | Evidencias | Servido como adjunto | T-305 | APROBADO | Seguridad |
| RS-007 | Backup íntegro | MVP | Administración | Hash + validación | T-306 | APROBADO | Seguridad |
| RS-008 | Cifrado de backup | MVP | Administración | Opción disponible | T-307 | PROPUESTO | Seguridad |
| RS-009 | Timeout probado | MVP | Identidad | Sin bypass | T-308 | APROBADO | Seguridad |
| RS-010 | CSRF | MVP | Global | Token en forms | T-309 | APROBADO | Seguridad |
| RS-011 | XSS | MVP | Global | Escape + CSP | T-310 | APROBADO | Seguridad |
| RS-012 | SQLi | MVP | Global | ORM parametrizado | T-311 | APROBADO | Seguridad |
| RS-013 | Cabeceras | MVP | Global | CSP, X-Frame | T-312 | APROBADO | Seguridad |
| RS-014 | Auditoría | MVP | Global | Log de eventos | T-313 | APROBADO | Seguridad |
| RS-015 | Documentar LUKS | MVP | Global | Doc. de límites | T-314 | APROBADO | Seguridad |
| RS-016 | Política de contraseñas | MVP | Identidad | Longitud/complejidad | T-315 | APROBADO | Seguridad |
| RS-017 | Bloqueo N intentos | MVP | Identidad | Bloqueo configurable | T-316 | PENDIENTE | Seguridad |
| RS-018 | Minimización | MVP | Global | Datos mínimos | T-317 | APROBADO | Privacidad |
| RS-019 | Deps actualizadas | MVP | Global | Registro | T-318 | APROBADO | Mantenibilidad |
| RS-020 | Errores no expuestos | MVP | Global | Mensajes genéricos | T-319 | APROBADO | Seguridad |

*(Nota: Las pruebas T-xxx son referencias a pruebas a definir en el Plan de Pruebas; su existencia en esta matriz no implica que ya estén implementadas.)*

---

## 6. Decisiones, Riesgos y Evolución

### 6.1. Stack Tecnológico Fijado

| Componente | Decisión | Justificación |
|:---|:---|:---|
| **Lenguaje** | Python 3.12+ (versión estable disponible en Fedora 44) | Compatibilidad con Django LTS y librerías de extracción. |
| **Backend** | Django LTS con soporte vigente (versión a fijar en implementación según disponibilidad y soporte oficial) | ORM seguro, autenticación integrada, admin, protección CSRF/XSS/SQLi, bajo consumo configurable. |
| **Base de datos** | SQLite con FTS5 verificado en la compilación del sistema | Monousuario, sin proceso servidor, rápido en NVMe. |
| **Frontend** | Ventana desktop nativa de Electron (Chromium embebido). Capa web interna con HTML5 + HTMX + Bootstrap 5 + 12 temas CSS con glassmorphism (archivos locales, sin CDN). | Interfaz de aplicación independiente, sin navegador externo, offline, responsivo. |
| **PDF** | PyMuPDF (fitz) en modo batch | Rápido, bajo consumo controlado. |
| **Hashing** | Argon2 | Recomendación OWASP. |

**Notas:**
*   Las versiones exactas de Python, Django y librerías se fijarán en el `requirements.txt` al momento de la implementación, verificando compatibilidad con Fedora 44 y soporte vigente.
*   El objetivo de "menos de 300 MB en reposo" es un **objetivo de rendimiento a validar** mediante prueba formal (RNF-003), no una garantía.
*   OCR (Tesseract) queda fuera del MVP.

### 6.2. Integración ASCENSO — Validación

*   **RF-010** y **RF-011** garantizan que las 33 etapas estén representadas y que las no desarrolladas permanezcan visibles y marcadas.
*   **RF-012** garantiza que las dependencias se tomen del documento maestro, no inventadas.
*   La selección de etapas del MVP (0, 1, 2, 3, 8, 17, 21) se mantiene como **propuesta de contenido inicial**, no como modificación de la estructura ASCENSO.
*   **Regla estricta:** no se inventará contenido de ASCENSO. La fuente de verdad es el documento maestro consolidado 3.1.

### 6.3. Distinción entre Requisitos, Decisiones y Propuestas

*   **Requisitos APROBADOS:** marcados como tal en la Sección 3 y en la matriz. Constituyen la línea base del MVP.
*   **Requisitos PENDIENTES:** requieren decisión del usuario antes de implementación (ej. RF-006, RS-017: definir N intentos).
*   **Requisitos PROPUESTOS:** recomendaciones del equipo técnico para evaluación (ej. cifrado de backup, panel de competencias). No son obligatorios hasta aprobación explícita.
*   **Decisiones de arquitectura:** documentadas en esta sección; algunas son autónomas del equipo técnico y quedan sujetas a validación final.

### 6.4. Riesgos y Mitigaciones

| Riesgo | Impacto | Mitigación |
|:---|:---|:---|
| RAM limitada (2.9 GiB disponibles) | Ralentización | Django en modo producción local, 1 worker, sin DEBUG, batch en PDFs. |
| Backups trasladados sin cifrado | Exposición de datos | RS-008: opción de cifrado; documentar límites de LUKS (RS-015). |
| Contenido ASCENSO inventado | Desviación académica | RF-010/011/012 + regla estricta de fuente de verdad. |
| Versiones abiertas de stack | Incompatibilidad | RNF-012/013/014: fijar versiones en implementación. |
| Archivos subidos ejecutables | Ejecución maliciosa | RS-005/006 + RF-086. |
| Duplicados/dañados en importación | Corrupción de datos | RF-033/034/035/036/044. |
| Sesión evadida por acceso directo | Exposición | RNF-010/RS-009 + pruebas T-209/T-308. |
| Pérdida de datos por fallo del SSD | Pérdida total | Backups verificados + recordatorio de copia externa. |

### 6.5. Evolución Prevista

1.  **Fase 1 (MVP actual):** Aplicación desktop independiente, servidor Django embebido, ventana Electron (Chromium), SQLite, autenticación local, frase de rescate, panel principal, roadmap ASCENSO 3.1 con progreso, seguridad (CSP, CSRF, XSS, SQLi), backups verificados, estilos profesionales y 12 temas.
2.  **Fase 2:** Cifrado de backup, OCR por lotes, panel de competencias avanzado, informes.
3.  **Fase 3:** Tutor IA local (LLM cuantizado), búsqueda semántica.
4.  **Fase 4:** Multiusuario, sincronización, comunidad (solo si se justifica).

### 6.6. Empaquetado y Distribución

La aplicación se distribuye para Windows en formato `.exe` mediante dos etapas: **PyInstaller** empaqueta el servidor Django autónomo (intérprete Python, Django, PyMuPDF, Argon2, plantillas, estáticos y el JSON de ASCENSO) en `dist-server/CodeGuardServer/`; después **electron-builder** integra Electron, el servidor y los recursos en un instalador **NSIS** y una versión **portable**. Ambos artefactos se generan en Windows con `build_windows.bat`.

El servidor Django embebido escucha exclusivamente en `127.0.0.1` y no expone la aplicación a la red local ni a Internet. Electron elige un puerto libre, espera la disponibilidad del servidor y detiene el árbol de procesos al cerrar. Los datos escribibles (base de datos, logs, medios y clave secreta local) se guardan en `%APPDATA%\CodeGuard Pro`, nunca dentro del directorio de instalación.

---

*Este documento distingue explícitamente requisitos aprobados, pendientes y propuestos. Las decisiones de arquitectura autónomas del equipo técnico quedan sujetas a validación final del usuario antes de la implementación.*