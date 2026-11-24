# Etapa 19 — DevOps, Docker, CI/CD y servidores

**Prioridad:** P1 (fundamentos) · P2 (profundización avanzada)  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** aprender a ejecutar, desplegar, mantener y administrar aplicaciones en infraestructura real.  
**Proyecto oficial:** desplegar una aplicación Full Stack en un servidor Linux mediante Docker, Nginx y un pipeline CI/CD.

## Resultados de aprendizaje
Explicar colaboración Dev/Ops, automatizar integración y entrega, construir imágenes reproducibles, administrar un servidor Linux, configurar Nginx como servidor/proxy, diseñar pipelines seguros, comparar servicios cloud, comprender fundamentos Kubernetes y gestionar infraestructura mediante Terraform.

## 19.1 — Fundamentos DevOps
DevOps combina prácticas culturales, procesos y herramientas para mejorar colaboración entre desarrollo y operaciones. Continuous Integration integra cambios frecuentemente y ejecuta validaciones automatizadas. Continuous Delivery mantiene software listo para desplegar; Continuous Deployment automatiza el despliegue tras superar controles. Infrastructure as Code declara infraestructura de forma versionable y repetible.

Automatización no elimina responsabilidad operativa. Define observabilidad, rollback, gestión de incidentes, control de cambios y recuperación. Mide tiempo de entrega, frecuencia, tasa de fallos y tiempo de recuperación con contexto; evita utilizar métricas como ranking individual.

**Ejercicio:** dibuja un flujo desde commit hasta despliegue, identifica controles, aprobaciones, artefactos y rollback.

## 19.2 — Docker
Un contenedor ejecuta procesos aislados utilizando mecanismos del kernel; una imagen es una plantilla inmutable por capas. Un Dockerfile describe cómo construirla. Estudia contexto de build, capas, caché, tags, registries y lifecycle. Usa imágenes base confiables, versiones fijadas, usuario no root, dependencias mínimas y builds multi-stage.

Volumes persisten datos fuera del ciclo de vida del contenedor. Networks conectan servicios. Docker Compose describe aplicaciones multicontenedor para desarrollo y entornos controlados. No confundas contenedor con máquina virtual ni supongas que aislamiento de contenedores elimina todos los riesgos.

**Laboratorio:** empaqueta una aplicación con build multi-stage, ejecuta como usuario no privilegiado, conecta una base de datos en red privada y conserva datos en volumen. Documenta puertos expuestos.

## 19.3 — Servidores
Administra Linux Server con cuentas individuales, SSH, permisos mínimos, firewall, servicios, logs, almacenamiento y procesos. Usa claves SSH protegidas y políticas de acceso; deshabilitar contraseña o root remoto depende de una configuración probada y acceso alternativo de recuperación. Mantén sistema actualizado y registra cambios.

**Laboratorio:** prepara una VM Linux, crea un usuario administrador separado, configura SSH y firewall, ejecuta un servicio de prueba y revisa logs y consumo.

## 19.4 — Nginx
Nginx puede servir archivos estáticos, actuar como reverse proxy y balancear solicitudes. Comprende server blocks/virtual hosts, upstreams, headers de proxy, TLS, límites de tamaño y logs. El proxy debe preservar información necesaria sin confiar en headers de cliente falsificables. Protege endpoints internos y paneles administrativos.

**Laboratorio:** publica frontend estático y enruta /api hacia un backend privado. Configura TLS en laboratorio con certificado apropiado, headers y límites; prueba rutas y errores.

## 19.5 — CI/CD
Un pipeline ejecuta etapas reproducibles: checkout, instalación, lint, pruebas, análisis, build, publicación de artefacto y despliegue según política. GitHub Actions permite workflows definidos en YAML. Separa entornos, restringe permisos de tokens, usa secrets del proveedor y evita imprimirlos. Fija acciones/dependencias con estrategia de versiones y revisa cambios.

Automated builds y tests deben producir evidencia. Deployment requiere estrategia de release, health checks y rollback. Un pipeline verde no prueba por sí solo que producción esté sana.

**Laboratorio:** crea pipeline que ejecute lint, tests, build y genere artefacto. El despliegue debe limitarse a entorno de prueba; producción requiere autorización explícita.

## 19.6 — Cloud
Cloud computing ofrece recursos bajo demanda. IaaS entrega infraestructura virtual; PaaS abstrae parte de operación de plataforma; SaaS entrega una aplicación gestionada. Estudia máquinas virtuales, storage, networking, IAM, regiones, zonas, disponibilidad, observabilidad y costos.

Diseña IAM con mínimo privilegio y roles temporales. Comprende responsabilidad compartida: el proveedor protege partes de la plataforma, pero configuración, identidades, datos y código siguen requiriendo controles del cliente. Evita crear recursos facturables sin aprobación.

## 19.7 — Proveedores
El roadmap inicia con AWS y después compara servicios equivalentes de Azure y Google Cloud. Aprende categorías, no solo nombres comerciales: cómputo, redes, almacenamiento, IAM, bases de datos, colas, observabilidad y despliegue. Compara disponibilidad regional, SLA, costos, portabilidad y límites. Verifica documentación y precios vigentes antes de estimar.

**Ejercicio:** elabora una matriz de equivalencias AWS/Azure/GCP para una arquitectura de laboratorio. No despliegues recursos pagos sin autorización.

## 19.8 — Kubernetes
Kubernetes orquesta cargas en contenedores. Un Pod agrupa contenedores; Nodes ejecutan cargas; Deployments administran réplicas y actualizaciones; Services proporcionan descubrimiento y acceso; ConfigMaps almacenan configuración no secreta; Secrets almacenan datos sensibles con controles adicionales; Volumes proporcionan persistencia; Ingress o mecanismos equivalentes publican tráfico; scaling ajusta réplicas o recursos.

Comprende probes, requests/limits, namespaces, RBAC, networking y actualizaciones. Un objeto Secret no implica cifrado automático suficiente en cualquier instalación. Kubernetes añade complejidad y no es requisito para toda aplicación.

**Laboratorio:** despliega una aplicación de prueba en clúster local, define Deployment, Service, configuración, límites y probes. No expongas servicios sensibles.

## 19.9 — Terraform
Terraform declara infraestructura mediante configuración. Providers conectan APIs; resources describen objetos; variables parametrizan; modules reutilizan; state registra relación entre configuración y recursos reales. Protege el state: puede contener datos sensibles. Usa backend seguro y locking cuando corresponda. Revisa plan antes de apply y no compartas archivos de estado.

**Laboratorio:** define infraestructura local o simulada con módulo, variables y outputs. Ejecuta validate/plan; no apliques cambios remotos ni crees recursos con costo sin autorización.

## Proyecto oficial — Despliegue Full Stack
Despliega una aplicación en servidor Linux de laboratorio con Docker, Nginx y CI/CD.

### Requisitos
1. Arquitectura y diagrama de red.
2. Dockerfile multi-stage y usuario no root.
3. Servicios separados y redes/volúmenes declarados.
4. Nginx como reverse proxy y frontend estático.
5. TLS y headers según el entorno.
6. CI con lint, tests y build.
7. Artefacto identificable y estrategia de despliegue.
8. Secretos y permisos mínimos.
9. Health checks, logs y monitorización básica.
10. Procedimiento de rollback y backup.
11. Instrucciones de reproducción y limitaciones.
12. Costos y recursos cloud documentados si aplica.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Flujo DevOps y automatización | 10 |
| Docker e imágenes seguras | 20 |
| Administración Linux/SSH/firewall | 15 |
| Nginx y TLS | 10 |
| CI/CD y gestión de secretos | 15 |
| Cloud/IAM/costos | 10 |
| Kubernetes/Terraform fundamentos | 10 |
| Observabilidad, rollback y documentación | 10 |

Criterio orientativo: 80/100 y sin secretos expuestos ni servicios de administración abiertos innecesariamente.

## Autoevaluación
1. Diferencia CI, Continuous Delivery y Continuous Deployment.
2. ¿Qué diferencia hay entre imagen y contenedor?
3. ¿Por qué un contenedor no equivale a una VM?
4. ¿Para qué sirven volumes y networks?
5. ¿Qué función cumple Nginx como reverse proxy?
6. ¿Cómo limitas permisos de un workflow?
7. ¿Qué significa responsabilidad compartida cloud?
8. ¿Qué diferencia hay entre Pod, Deployment y Service?
9. ¿Por qué Terraform state debe protegerse?
10. ¿Qué evidencia necesitas antes de afirmar que un despliegue funciona?

## Recursos audiovisuales
No se incluyen videos aprobados. Se añadirán solo con audio español confirmado y pertinencia específica para Docker, Nginx, GitHub Actions, cloud IAM, Kubernetes o Terraform.

## Referencias oficiales
- DevOps: https://learn.microsoft.com/en-us/devops/
- Docker Docs: https://docs.docker.com/
- Nginx Documentation: https://nginx.org/en/docs/
- GitHub Actions: https://docs.github.com/en/actions
- AWS Documentation: https://docs.aws.amazon.com/
- Microsoft Azure: https://learn.microsoft.com/en-us/azure/
- Google Cloud: https://cloud.google.com/docs
- Kubernetes: https://kubernetes.io/docs/home/
- Terraform: https://developer.hashicorp.com/terraform/docs
- OpenTelemetry: https://opentelemetry.io/docs/

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se desplegó infraestructura ni se ejecutó pipeline en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 19

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados orientan el estudio de los conceptos dentro de la guía y el proyecto de la etapa; no constituyen resultados de pruebas ni evidencias de implementación.

### Módulo 19.1 — Fundamentos DevOps

#### 19.1.01 — Development
Development construye y mantiene el producto mediante diseño, implementación, pruebas y evolución. La colaboración con operaciones debe incorporar restricciones de ejecución, observabilidad y seguridad desde el diseño, no después de terminar el código.

#### 19.1.02 — Operations
Operations mantiene sistemas en ejecución, gestionando disponibilidad, capacidad, incidentes, cambios y continuidad. Diseña servicios que puedan desplegarse, monitorizarse y recuperarse con procedimientos documentados.

#### 19.1.03 — Continuous Integration
Continuous Integration integra cambios frecuentemente en una rama compartida y ejecuta controles automatizados. Mantén builds reproducibles, pruebas rápidas y feedback oportuno; CI no es solo configurar un workflow que termine en verde.

#### 19.1.04 — Continuous Delivery
Continuous Delivery mantiene el software en estado potencialmente desplegable, con validaciones y artefactos listos. La decisión de publicar puede ser manual; documenta criterios de promoción y evidencia entre entornos.

#### 19.1.05 — Continuous Deployment
Continuous Deployment automatiza el paso a producción cuando los cambios superan todos los controles definidos. Requiere pruebas confiables, monitoreo, rollback y gestión de riesgo; no debe habilitarse por defecto sin madurez operativa.

#### 19.1.06 — Infrastructure as Code
Infrastructure as Code describe infraestructura mediante archivos versionados y revisables. Permite repetir entornos y detectar cambios; protege state y secretos, revisa planes y aplica controles antes de modificar recursos reales.

#### 19.1.07 — Automation
Automation reduce tareas manuales repetibles mediante scripts y pipelines. Automatiza procesos con validación, idempotencia, logs y manejo de errores; una automatización sin controles puede propagar un error a muchos sistemas.

### Módulo 19.2 — Docker

#### 19.2.01 — Containers
Containers aíslan procesos mediante mecanismos del kernel y empaquetan dependencias de ejecución, sin equivaler a máquinas virtuales completas. Comprende namespaces, cgroups y límites de aislamiento; un contenedor no es una frontera de seguridad absoluta.

#### 19.2.02 — Images
Images son plantillas inmutables por capas desde las que se crean contenedores. Usa imágenes base mantenidas, versiones/digests verificables y escaneo de vulnerabilidades; minimiza paquetes y evita incorporar secretos en capas.

#### 19.2.03 — Dockerfile
Dockerfile declara instrucciones para construir una imagen, como base, copia de archivos, dependencias y comando de inicio. Ordena capas para aprovechar caché, fija versiones y ejecuta procesos con usuario no privilegiado.

#### 19.2.04 — Volumes
Volumes persisten datos fuera del ciclo de vida del contenedor y permiten compartir almacenamiento. Define permisos, copias y ciclo de vida; no confundas volúmenes persistentes con backups ni almacenes secretos en volúmenes de aplicación.

#### 19.2.05 — Networks
Networks conecta contenedores mediante redes virtuales y reglas de resolución/aislamiento. Expón solo puertos necesarios y separa redes internas de públicas; la conectividad entre contenedores debe responder a una necesidad explícita.

#### 19.2.06 — Registries
Registries almacenan y distribuyen imágenes de contenedor. Usa registros confiables, autenticación, control de acceso, escaneo y firmas cuando estén disponibles; no publiques imágenes con credenciales, llaves o artefactos sensibles.

#### 19.2.07 — Docker Compose
Docker Compose define aplicaciones multi-contenedor, redes y volúmenes mediante un archivo declarativo. Es útil para desarrollo y entornos pequeños; gestiona variables y secretos fuera del YAML versionado y no asumas equivalencia con orquestación de producción.

#### 19.2.08 — Multi-stage builds
Multi-stage builds separa etapas de compilación y runtime para producir imágenes finales más pequeñas. Copia solo artefactos necesarios y evita que herramientas de build o secretos queden en capas de producción.

#### 19.2.09 — Container lifecycle
Container lifecycle comprende creación, ejecución, pausa, detención, eliminación y recreación. Diseña aplicaciones que manejen señales de terminación, logging a stdout/stderr y almacenamiento externo para datos que deban sobrevivir.

### Módulo 19.3 — Servidores

#### 19.3.01 — Linux Server
Linux Server ejecuta servicios y administra usuarios, procesos, red, almacenamiento y actualizaciones sin requerir escritorio. Mantén paquetes soportados, acceso mínimo, monitoreo y copias verificadas.

#### 19.3.02 — SSH
SSH proporciona acceso remoto cifrado y autenticación a sistemas. Usa claves protegidas, verifica host keys, limita usuarios y métodos de acceso y evita compartir claves privadas o habilitar root directo sin controles.

#### 19.3.03 — Usuarios
Los usuarios y grupos del servidor permiten asignar identidades y permisos a procesos y personas. Crea cuentas nominales, elimina accesos obsoletos y aplica separación de funciones.

#### 19.3.04 — Permisos
Permisos controlan lectura, escritura y ejecución sobre archivos y directorios, junto con ACL y atributos adicionales. Aplica mínimo privilegio y verifica propietario/grupo antes de modificar permisos recursivamente.

#### 19.3.05 — Firewall
Firewall filtra tráfico según origen, destino, protocolo, puerto y estado. Define reglas de entrada/salida necesarias, prueba que no bloqueen administración legítima y registra cambios con posibilidad de recuperación.

#### 19.3.06 — Services
Services son procesos administrados por el sistema de inicio, normalmente con políticas de arranque, reinicio y dependencias. Limita capacidades, usuario y recursos del servicio y revisa su estado después de cambios.

#### 19.3.07 — Logs
Logs registran eventos del sistema y aplicaciones para diagnóstico y auditoría. Centraliza con controles de acceso, sincroniza tiempo, define retención y elimina secretos o datos personales innecesarios.

#### 19.3.08 — Storage
Storage incluye discos, particiones, sistemas de archivos, montajes y volúmenes. Monitoriza espacio, inodos y salud; planifica expansión y backup y no asumas que una copia en el mismo disco protege ante fallo físico.

#### 19.3.09 — Process management
Process management permite inspeccionar, priorizar, limitar y terminar procesos. Identifica propietario, PID y dependencias antes de intervenir; termina de forma gradual y evita usar kill indiscriminadamente en servicios críticos.

### Módulo 19.4 — Nginx

#### 19.4.01 — Web Server
Nginx puede actuar como servidor web, proxy inverso y balanceador. Configura bloques server, ubicaciones y upstreams con alcance claro y valida sintaxis antes de recargar el servicio.

#### 19.4.02 — Reverse Proxy
Reverse Proxy recibe solicitudes y las reenvía a servicios internos, ocultando topología y centralizando TLS o políticas. Configura headers de proxy confiables, timeouts y límites; no confíes en headers de IP reenviada si el origen no es confiable.

#### 19.4.03 — Virtual Hosts
Virtual Hosts permiten alojar varios nombres de sitio en una misma instancia mediante bloques de servidor. Define nombres explícitos, certificados y comportamiento por defecto para hosts desconocidos.

#### 19.4.04 — Static Files
Static Files sirve archivos como HTML, CSS, JavaScript e imágenes directamente desde el servidor web. Configura rutas y tipos MIME, controla permisos y evita exponer archivos de configuración o directorios internos.

#### 19.4.05 — TLS
TLS en Nginx protege el canal entre clientes y servidor mediante certificados y parámetros criptográficos. Automatiza renovación, redirige HTTP cuando corresponda y verifica cadena, nombre y vigencia sin desactivar validación.

#### 19.4.06 — Load Balancing
Load Balancing distribuye solicitudes entre servidores upstream mediante algoritmos y comprobaciones disponibles. Configura health checks, persistencia si se requiere y manejo de fallos; balancear no garantiza consistencia de sesión o datos.

### Módulo 19.5 — CI/CD

#### 19.5.01 — Pipelines
Pipelines describen etapas automatizadas de build, pruebas, análisis y entrega. Divide jobs por responsabilidad, controla permisos de runners y conserva artefactos trazables para poder reconstruir qué versión fue publicada.

#### 19.5.02 — Automated Builds
Automated Builds compilan o empaquetan software desde fuentes y dependencias declaradas. Usa entornos limpios y versiones fijadas, y genera artefactos reproducibles o al menos trazables.

#### 19.5.03 — Automated Tests
Automated Tests ejecuta suites como parte del pipeline y bloquea promoción ante fallos relevantes. Clasifica pruebas por duración y riesgo, publica resultados y evita deshabilitar controles para forzar un despliegue.

#### 19.5.04 — Deployment
Deployment publica un artefacto en un entorno mediante una estrategia definida. Separa build de deploy, controla permisos, verifica salud posterior y registra versión, parámetros y responsable del cambio.

#### 19.5.05 — GitHub Actions
GitHub Actions automatiza workflows mediante eventos, jobs y actions en runners. Fija versiones de actions, limita `GITHUB_TOKEN`, revisa permisos y protege secretos contra exposición en logs o ejecuciones de forks.

#### 19.5.06 — Secrets
Secrets son credenciales y valores confidenciales utilizados por workflows y aplicaciones. Guárdalos en un gestor apropiado, limita alcance y duración, rótalos y nunca los imprimas ni los escribas en artefactos.

#### 19.5.07 — Environments
Environments representan destinos como staging y production con variables, secretos y reglas de aprobación. Restringe quién puede desplegar y exige evidencia previa para promover artefactos entre entornos.

#### 19.5.08 — Rollbacks
Rollbacks restauran una versión o estado conocido cuando una publicación falla. Define qué puede revertirse, cómo se manejan migraciones de datos y cómo se valida recuperación; rollback de código no revierte automáticamente cambios de esquema.

### Módulo 19.6 — Cloud

#### 19.6.01 — Cloud Computing
Cloud Computing ofrece recursos informáticos bajo demanda mediante redes y servicios gestionados. Evalúa responsabilidad compartida, coste, disponibilidad, residencia de datos y dependencia del proveedor antes de migrar cargas.

#### 19.6.02 — IaaS
IaaS ofrece recursos fundamentales como cómputo, red y almacenamiento virtualizados que el cliente administra en gran parte. Mantén parches, hardening, backups y control de identidades en el sistema operativo.

#### 19.6.03 — PaaS
PaaS abstrae parte de la administración de infraestructura y runtime para desplegar aplicaciones. Comprende límites de plataforma, escalado, configuración y portabilidad; el proveedor gestiona componentes, pero la aplicación sigue siendo responsabilidad del cliente.

#### 19.6.04 — SaaS
SaaS ofrece una aplicación completa administrada por el proveedor. Evalúa identidad, roles, integración, exportación de datos, retención y continuidad; contratar SaaS no elimina responsabilidades sobre usuarios y datos.

#### 19.6.05 — Virtual Machines
Virtual Machines ejecuta sistemas operativos invitados sobre un hipervisor. Dimensiona CPU, memoria y disco, aplica parches al host y guest y evita exponer servicios de administración a redes no confiables.

#### 19.6.06 — Storage
Cloud Storage ofrece almacenamiento de objetos, bloques o archivos según el servicio. Define cifrado, versionado, políticas de acceso, retención y recuperación; evita buckets públicos por defecto.

#### 19.6.07 — Networking
Cloud Networking conecta recursos mediante redes virtuales, subredes, rutas, gateways y reglas de seguridad. Diseña segmentación, flujos mínimos y conectividad privada antes de desplegar servicios.

#### 19.6.08 — IAM
IAM controla identidades, roles, políticas y permisos sobre recursos cloud. Aplica mínimo privilegio, credenciales temporales, MFA y revisión periódica; no uses claves de larga duración compartidas entre desarrolladores.

#### 19.6.09 — Monitoring
Monitoring recoge métricas, logs, trazas y eventos para observar salud y rendimiento. Define alertas accionables y SLOs, controla datos sensibles y prueba que las alertas lleguen a responsables.

### Módulo 19.7 — Proveedores

#### 19.7.01 — AWS
AWS ofrece servicios cloud de cómputo, almacenamiento, red, identidad y observabilidad. Aprende el modelo de cuenta, regiones, IAM y responsabilidad compartida antes de desplegar; limita permisos y presupuestos en laboratorios.

#### 19.7.02 — Azure
Azure integra servicios cloud y herramientas del ecosistema Microsoft con gestión de identidades y recursos. Comprende tenants, subscriptions, resource groups y RBAC; separa entornos y evita credenciales administrativas permanentes.

#### 19.7.03 — Google Cloud
Google Cloud ofrece servicios de infraestructura, datos, red e identidad organizados por proyectos y recursos. Configura IAM, billing, regiones y logging desde el inicio y evita claves de cuentas de servicio descargables cuando haya alternativas federadas.

### Módulo 19.8 — Kubernetes

#### 19.8.01 — Pods
Pods son la unidad desplegable mínima de Kubernetes y agrupan uno o más contenedores que comparten red y volúmenes. Define requests/limits y probes, y no uses un Pod aislado como estrategia de alta disponibilidad.

#### 19.8.02 — Nodes
Nodes son máquinas que ejecutan Pods y componentes del agente del clúster. Mantén versiones soportadas, capacidad y parches; separa nodos por necesidades de carga y confianza cuando corresponda.

#### 19.8.03 — Deployments
Deployments gestionan réplicas y actualizaciones declarativas de Pods. Configura estrategia de rollout, probes y réplicas; verifica disponibilidad antes de considerar exitosa una actualización.

#### 19.8.04 — Services
Services ofrecen una dirección estable y balanceo hacia un conjunto de Pods. Selecciona labels correctamente y limita tipos de exposición; un Service interno no debe convertirse accidentalmente en endpoint público.

#### 19.8.05 — ConfigMaps
ConfigMaps almacenan configuración no confidencial para consumirla en Pods. Versiona cambios y reinicia o recarga procesos cuando corresponda; no guardes tokens o contraseñas en ConfigMaps.

#### 19.8.06 — Secrets
Secrets almacenan datos sensibles en Kubernetes, pero su nombre no garantiza cifrado o protección suficiente por defecto. Configura cifrado en reposo, RBAC mínimo, rotación y external secret management cuando sea adecuado.

#### 19.8.07 — Volumes
Volumes conectan almacenamiento a contenedores y pueden persistir más allá del ciclo de vida de un Pod. Comprende StorageClasses y PersistentVolumeClaims y diseña backup/restauración independiente del montaje.

#### 19.8.08 — Ingress
Ingress define reglas de acceso HTTP/HTTPS hacia servicios del clúster mediante un controlador compatible. Configura TLS, hosts y rutas, limita exposición y verifica políticas del controlador instalado.

#### 19.8.09 — Scaling
Scaling ajusta réplicas o recursos según demanda mediante escalado manual o automático. Define métricas y límites, considera capacidad de nodos y dependencias y evita escalar sin observar latencia y coste.

#### 19.8.10 — Networking
Kubernetes Networking conecta Pods, Services y redes externas según el modelo de red del clúster. Comprende DNS, políticas de red y rutas; aplica NetworkPolicies cuando el plugin las soporte y valida aislamiento real.

### Módulo 19.9 — Terraform

#### 19.9.01 — Infrastructure as Code
Infrastructure as Code con Terraform define recursos mediante configuración declarativa y permite revisar cambios antes de aplicarlos. Mantén código versionado y módulos reutilizables y nunca ejecutes apply sin revisar el plan.

#### 19.9.02 — Providers
Providers permiten que Terraform interactúe con APIs de plataformas cloud y otros servicios. Fija versiones y fuentes confiables, configura autenticación temporal y revisa cambios de proveedor antes de actualizar.

#### 19.9.03 — Resources
Resources describen objetos administrados por Terraform y sus argumentos/atributos. Define dependencias explícitas cuando sea necesario, evita recursos duplicados y protege operaciones destructivas mediante revisión.

#### 19.9.04 — Variables
Variables parametrizan módulos y configuraciones para distintos entornos. Declara tipos, validaciones y valores sensibles; marcar una variable como sensitive oculta parte de la salida, pero no sustituye proteger state y backend.

#### 19.9.05 — State
State registra el mapeo entre configuración y recursos reales. Usa backend remoto con bloqueo y control de acceso, cifra y respalda state y nunca lo publiques porque puede contener valores sensibles.

#### 19.9.06 — Modules
Modules agrupan recursos y entradas/salidas para reutilizar infraestructura. Diseña interfaces pequeñas, versiona módulos y documenta supuestos; evita módulos excesivamente genéricos que dificulten entender qué infraestructura crean.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 67 orientaciones genéricas por explicaciones específicas de cada entrada oficial. Se desarrollaron fundamentos DevOps, contenedores e imágenes, servidores Linux, Nginx, CI/CD, proveedores cloud, IAM, observabilidad, Kubernetes y Terraform.

**Revisión interna:** 67/67 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron riesgos de secretos en imágenes y pipelines, privilegios, state de Terraform, exposición de servicios, lifecycle de contenedores, límites de recursos, NetworkPolicies y responsabilidad compartida cloud. Pendiente: construir imágenes, ejecutar pipelines, desplegar infraestructura efímera y validar recuperación en cuentas/clústeres de laboratorio autorizados. No se declara despliegue ni aprobación externa.
