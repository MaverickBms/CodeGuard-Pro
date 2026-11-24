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
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en fundamentos devops, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.1.02 — Operations
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en fundamentos devops, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.1.03 — Continuous Integration
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en fundamentos devops, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.1.04 — Continuous Delivery
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en fundamentos devops, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.1.05 — Continuous Deployment
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en fundamentos devops, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.1.06 — Infrastructure as Code
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en fundamentos devops, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.1.07 — Automation
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en fundamentos devops, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

### Módulo 19.2 — Docker

#### 19.2.01 — Containers
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.2.02 — Images
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.2.03 — Dockerfile
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.2.04 — Volumes
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.2.05 — Networks
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.2.06 — Registries
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.2.07 — Docker Compose
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.2.08 — Multi-stage builds
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.2.09 — Container lifecycle
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en docker, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

### Módulo 19.3 — Servidores

#### 19.3.01 — Linux Server
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.3.02 — SSH
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.3.03 — Usuarios
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.3.04 — Permisos
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.3.05 — Firewall
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.3.06 — Services
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.3.07 — Logs
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.3.08 — Storage
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.3.09 — Process management
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en servidores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

### Módulo 19.4 — Nginx

#### 19.4.01 — Web Server
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en nginx, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.4.02 — Reverse Proxy
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en nginx, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.4.03 — Virtual Hosts
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en nginx, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.4.04 — Static Files
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en nginx, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.4.05 — TLS
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en nginx, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.4.06 — Load Balancing
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en nginx, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

### Módulo 19.5 — CI/CD

#### 19.5.01 — Pipelines
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en ci/cd, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.5.02 — Automated Builds
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en ci/cd, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.5.03 — Automated Tests
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en ci/cd, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.5.04 — Deployment
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en ci/cd, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.5.05 — GitHub Actions
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en ci/cd, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.5.06 — Secrets
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en ci/cd, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.5.07 — Environments
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en ci/cd, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.5.08 — Rollbacks
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en ci/cd, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

### Módulo 19.6 — Cloud

#### 19.6.01 — Cloud Computing
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.6.02 — IaaS
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.6.03 — PaaS
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.6.04 — SaaS
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.6.05 — Virtual Machines
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.6.06 — Storage
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.6.07 — Networking
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.6.08 — IAM
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.6.09 — Monitoring
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en cloud, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

### Módulo 19.7 — Proveedores

#### 19.7.01 — AWS
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en proveedores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.7.02 — Azure
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en proveedores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.7.03 — Google Cloud
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en proveedores, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

### Módulo 19.8 — Kubernetes

#### 19.8.01 — Pods
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.02 — Nodes
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.03 — Deployments
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.04 — Services
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.05 — ConfigMaps
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.06 — Secrets
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.07 — Volumes
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.08 — Ingress
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.09 — Scaling
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.8.10 — Networking
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en kubernetes, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

### Módulo 19.9 — Terraform

#### 19.9.01 — Infrastructure as Code
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en terraform, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.9.02 — Providers
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en terraform, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.9.03 — Resources
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en terraform, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.9.04 — Variables
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en terraform, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.9.05 — State
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en terraform, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.

#### 19.9.06 — Modules
Comprender el alcance del concepto y los criterios técnicos que lo gobiernan; identificar cómo se aplica en terraform, cuándo resulta apropiado y qué limitaciones deben documentarse en el proyecto.
