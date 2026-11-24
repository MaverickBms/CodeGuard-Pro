# Etapa 29 — Cloud Security, DevSecOps y Supply Chain Security

**Prioridad:** P2 · Especialización avanzada  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** aprender a proteger aplicaciones, infraestructura y servicios desplegados en la nube.  
**Proyecto oficial:** crear un pipeline DevSecOps que construya, pruebe, analice y despliegue una aplicación de manera automatizada, integrando controles de seguridad.

## Resultados de aprendizaje
Aplicar el modelo de responsabilidad compartida; configurar IAM, redes y almacenamiento cloud; reconocer controles de AWS, Azure y Google Cloud; proteger imágenes y clústeres; generar SBOM y verificar artefactos; y automatizar controles de seguridad en CI/CD.

## 29.1 — Cloud Security
El modelo de responsabilidad compartida distribuye responsabilidades entre proveedor y cliente según el servicio. IAM controla identidades, roles, políticas y permisos. Cloud Networking incluye redes virtuales, subredes, rutas y segmentación. Cloud Storage Security exige clasificación, cifrado, control de acceso, retención y prevención de exposición pública. Secrets Management protege credenciales y claves. Cloud Logging y Monitoring permiten auditoría, detección y respuesta.

Revisa configuraciones por región, exposición pública, permisos excesivos, backups, cifrado, claves y registros. No crees recursos facturables ni modifiques cuentas reales sin autorización.

## 29.2 — AWS Security
Estudia IAM users/roles/policies, EC2, S3, VPC, Security Groups, CloudTrail, CloudWatch y GuardDuty (introducción). Comprende identidades temporales, mínimo privilegio, límites de red, buckets privados, logging de actividad y detección administrada. No confundas Security Groups con firewall de aplicación ni CloudTrail con monitor de rendimiento.

**Ejercicio:** diseña una cuenta/laboratorio ficticio con rol de lectura, bucket privado, red segmentada y registro de auditoría. Si se utiliza cuenta real, limita permisos y costos con aprobación explícita.

## 29.3 — Azure Security
Microsoft Entra ID gestiona identidad; Azure RBAC controla acceso a recursos; Azure Policy evalúa y aplica gobernanza; Key Vault administra secretos/llaves/certificados; Defender for Cloud ofrece capacidades de postura y protección según plan. Distingue identidad de tenant, suscripción, grupo de recursos y recurso.

**Ejercicio:** crea una matriz de roles y políticas en diagrama, sin desplegar recursos facturables.

## 29.4 — Google Cloud Security
Estudia IAM, service accounts, VPC, Cloud Logging y Cloud Monitoring. Evita claves de cuenta de servicio de larga duración cuando existan identidades administradas o federación. Revisa roles predefinidos y personalizados, scopes y auditoría.

## 29.5 — Docker Security
Image Security requiere imágenes base confiables, actualizadas y mínimas. Container Isolation depende del kernel, namespaces, capabilities y configuración. Ejecuta procesos como non-root, limita privilegios, analiza vulnerabilidades, protege secrets y aplica Dockerfiles seguros. No incluyas credenciales en capas ni argumentos de build.

## 29.6 — Kubernetes Security
Aplica RBAC, NetworkPolicies, gestión de Secrets, Pod Security, control de imágenes, hardening de clúster y runtime security. Restringe service accounts, capabilities, host namespaces y privilegios. Revisa admission policies, actualización de componentes y exposición de API server. Kubernetes Secret no implica por sí solo cifrado adecuado en reposo.

## 29.7 — Supply Chain Security
Dependency Security y scanning identifican dependencias vulnerables o sospechosas. SBOM (Software Bill of Materials) inventaría componentes. Artifact Integrity comprueba que el artefacto no cambió; Artifact Signing y provenance aportan evidencia de origen y proceso. Revisa typosquatting, paquetes abandonados, scripts de instalación, dependencias transitivas y software malicioso.

Una SBOM no garantiza que el software sea seguro; ofrece visibilidad. Firma y procedencia requieren protección de claves, identidad del builder y verificación en consumo.

## 29.8 — DevSecOps
Secure SDLC integra seguridad en diseño, código, build, despliegue y operación. SAST analiza código sin ejecutarlo; DAST prueba comportamiento en ejecución; SCA analiza dependencias; container scanning revisa imágenes; infrastructure scanning evalúa configuración; secrets scanning detecta credenciales expuestas. Security Gates deben tener reglas, severidad, excepciones con vencimiento y responsables. CI/CD Security protege runners, tokens, artifacts y workflows.

Herramientas del roadmap: Trivy, Gitleaks, OWASP Dependency-Check, GitHub Dependabot, Semgrep, Terraform y GitHub Actions. Verifica versiones, licencias y resultados; no conviertas alertas automáticas en conclusiones sin triage.

## Proyecto oficial — Pipeline DevSecOps
### Requisitos
1. Pipeline reproducible en repositorio de laboratorio.
2. Build y pruebas automatizadas.
3. SAST y análisis de dependencias.
4. Escaneo de secretos con datos sintéticos.
5. Escaneo de imagen de contenedor.
6. Revisión de IaC.
7. SBOM del artefacto.
8. Firma o evidencia de procedencia según capacidad del entorno.
9. Gates con severidad, excepción y caducidad.
10. Despliegue únicamente a entorno autorizado.
11. Logs y artefactos sin secretos.
12. Procedimiento de rollback y respuesta.

### Entregables
Workflow, configuración de herramientas, SBOM, reportes sanitizados, matriz de gates, evidencia de build, documentación de secretos y guía de reproducción.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Modelo de responsabilidad cloud e IAM | 15 |
| Redes y almacenamiento | 10 |
| Docker/Kubernetes security | 15 |
| Supply chain y SBOM | 20 |
| SAST/DAST/SCA y escaneos | 20 |
| Seguridad CI/CD y secretos | 10 |
| Documentación y operación | 10 |

Criterio orientativo: 80/100 y sin secretos expuestos ni despliegue no autorizado.

## Autoevaluación
1. ¿Qué cambia en responsabilidad compartida entre IaaS y SaaS?
2. ¿Por qué preferir roles temporales frente a claves persistentes?
3. ¿Qué diferencia existe entre IAM y RBAC?
4. ¿Qué controles reducen riesgo en imágenes Docker?
5. ¿Por qué Kubernetes Secret requiere controles adicionales?
6. ¿Qué información aporta una SBOM?
7. ¿Qué diferencia hay entre SAST, DAST y SCA?
8. ¿Por qué debe protegerse el runner de CI?
9. ¿Qué significa provenance de un artefacto?
10. ¿Cómo debe gestionarse una excepción a un security gate?

## Recursos audiovisuales
No se incluyen videos aprobados. Se añadirán solo con audio español confirmado y correspondencia directa con cloud IAM, Docker/Kubernetes hardening, SBOM, firma de artefactos o DevSecOps.

## Referencias oficiales
- AWS Security: https://docs.aws.amazon.com/security/
- AWS IAM: https://docs.aws.amazon.com/IAM/latest/UserGuide/
- Microsoft Entra: https://learn.microsoft.com/en-us/entra/
- Azure Security: https://learn.microsoft.com/en-us/azure/security/
- Google Cloud Security: https://cloud.google.com/security
- Docker Security: https://docs.docker.com/engine/security/
- Kubernetes Security: https://kubernetes.io/docs/concepts/security/
- NIST SSDF: https://csrc.nist.gov/Projects/ssdf
- SPDX: https://spdx.dev/
- CycloneDX: https://cyclonedx.org/
- SLSA: https://slsa.dev/
- Trivy: https://trivy.dev/
- Gitleaks: https://github.com/gitleaks/gitleaks
- OWASP Dependency-Check: https://owasp.org/www-project-dependency-check/
- Semgrep: https://semgrep.dev/docs/
- GitHub Actions Security: https://docs.github.com/en/actions/security-for-github-actions

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se ejecutó pipeline ni se desplegaron recursos cloud en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 29

Este desglose conserva los títulos y el orden del roadmap maestro. Las orientaciones organizan el estudio y la aplicación en proyectos controlados; no equivalen a validación de proveedores, certificación, ejecución de laboratorios ni experiencia laboral demostrada.

### Módulo 29.1 — Cloud Security

#### 29.1.01 — Shared Responsibility Model
Shared Responsibility Model distribuye responsabilidades de seguridad entre proveedor cloud y cliente según el servicio contratado. Documenta quién protege infraestructura, sistema operativo, aplicación, identidades y datos; la responsabilidad del cliente nunca desaparece por usar un servicio gestionado.


**Práctica y evidencia:** Asigna responsabilidades de seguridad entre proveedor cloud y cliente para IaaS, PaaS y SaaS. **Evidencia:** matriz de controles por modelo.

#### 29.1.02 — Cloud IAM
Cloud IAM administra identidades, roles, políticas y permisos sobre recursos de nube. Aplica mínimo privilegio, MFA y credenciales temporales; evita claves permanentes compartidas.


**Práctica y evidencia:** Diseña roles cloud con permisos mínimos y credenciales temporales. **Evidencia:** demuestra que una identidad de lectura no puede modificar recursos.

#### 29.1.03 — Cloud Networking
Cloud Networking conecta recursos mediante redes virtuales, subredes, rutas, gateways y controles de tráfico. Diseña segmentación y flujos explícitos y limita interfaces administrativas.


**Práctica y evidencia:** Dibuja VPC/VNet, subredes, rutas, gateways y controles de entrada/salida. **Evidencia:** identifica flujos y zonas de confianza.

#### 29.1.04 — Network Segmentation
Network Segmentation separa cargas y datos por función y nivel de confianza dentro de la nube. Usa subredes, grupos de seguridad y políticas de red para reducir movimiento lateral.


**Práctica y evidencia:** Separa redes públicas, privadas y administrativas mediante subredes y reglas. **Evidencia:** prueba matriz de conectividad deseada.

#### 29.1.05 — Cloud Storage Security
Cloud Storage Security protege objetos, discos y sistemas de archivos mediante políticas de acceso, cifrado, versionado y retención. Revisa exposición pública y permisos cross-account y prueba restauración.


**Práctica y evidencia:** Configura política de almacenamiento privado, cifrado y bloqueo de acceso público en un entorno de laboratorio. **Evidencia:** verifica acceso permitido/denegado.

#### 29.1.06 — Encryption
Encryption protege datos en tránsito y reposo mediante algoritmos y gestión de claves adecuados. Define quién administra claves, rotación, recuperación y acceso; cifrar no compensa permisos excesivos.


**Práctica y evidencia:** Compara cifrado en tránsito y reposo y documenta gestión de claves. **Evidencia:** identifica propietario, rotación y recuperación.

#### 29.1.07 — Secrets Management
Secrets Management almacena y entrega credenciales y claves mediante servicios controlados, con rotación y auditoría. Evita incrustar secretos en código, imágenes, variables públicas o logs.


**Práctica y evidencia:** Diseña ciclo de vida de secretos con gestor dedicado, rotación y auditoría. **Evidencia:** demuestra que no aparecen en variables públicas, logs o repositorio.

#### 29.1.08 — Cloud Logging
Cloud Logging registra operaciones de control plane, recursos y aplicaciones. Centraliza eventos, protege integridad, sincroniza tiempo y define retención y acceso según sensibilidad.


**Práctica y evidencia:** Centraliza logs cloud de identidad, red y recursos con retención y acceso controlado. **Evidencia:** comprueba timestamp y origen.

#### 29.1.09 — Cloud Monitoring
Cloud Monitoring recoge métricas, logs y alertas sobre salud, seguridad y costes. Define señales accionables y responsables, y prueba alertas para detectar fallos de ingestión.


**Práctica y evidencia:** Define métricas y alertas de seguridad cloud para cambios de IAM y exposición pública. **Evidencia:** relaciona señal con respuesta.

#### 29.1.10 — Security Misconfigurations
Security Misconfigurations incluyen recursos públicos, políticas amplias, redes abiertas y servicios sin controles. Mantén baseline como código, revisiones de configuración y detección continua de desviaciones.


**Práctica y evidencia:** Audita configuraciones de almacenamiento, red, identidad y logging contra baseline. **Evidencia:** prioriza desviaciones y plan de remediación.

### Módulo 29.2 — AWS Security

#### 29.2.01 — IAM
AWS IAM controla identidades y acceso a servicios mediante usuarios, roles y políticas. Prefiere roles y credenciales temporales, aplica MFA y revisa políticas efectivas.


**Práctica y evidencia:** Inspecciona políticas IAM de AWS en un entorno de lectura y calcula permisos efectivos. **Evidencia:** identifica wildcard y permisos innecesarios.

#### 29.2.02 — Roles
Roles AWS permiten que usuarios o servicios asuman permisos temporales mediante relaciones de confianza. Restringe quién puede asumir cada rol y define duración y condiciones.


**Práctica y evidencia:** Crea o modela un rol con trust policy restringida y permisos mínimos. **Evidencia:** explica principal autorizado y condiciones.

#### 29.2.03 — Policies
Policies son documentos que permiten o deniegan acciones sobre recursos bajo condiciones. Evalúa políticas identity-based y resource-based, denegaciones explícitas y límites de permisos.


**Práctica y evidencia:** Evalúa una policy con acciones, recursos, condiciones y denegaciones explícitas. **Evidencia:** prueba escenarios permitidos y rechazados.

#### 29.2.04 — EC2
EC2 ofrece instancias de cómputo virtual. Endurece AMIs, limita Security Groups, protege metadata service y asigna roles mínimos; parchea sistema operativo y agentes.


**Práctica y evidencia:** Diseña una instancia EC2 privada con acceso administrativo controlado. **Evidencia:** documenta red, rol, almacenamiento y sin desplegar recursos facturables.

#### 29.2.05 — S3
S3 almacena objetos en buckets y requiere controles de acceso, cifrado, versionado y políticas. Bloquea acceso público salvo necesidad aprobada y revisa ACL, bucket policies y logging.


**Práctica y evidencia:** Configura un bucket S3 de laboratorio privado con bloqueo de acceso público y cifrado. **Evidencia:** verifica política y acceso.

#### 29.2.06 — VPC
VPC define una red virtual aislada con subredes, tablas de rutas y gateways. Diseña topología y flujos mínimos y controla acceso entre VPCs y redes externas.


**Práctica y evidencia:** Dibuja VPC con subredes, route tables y security boundaries. **Evidencia:** identifica rutas a Internet y segmentos privados.

#### 29.2.07 — Security Groups
Security Groups filtran tráfico de instancias y recursos asociados mediante reglas stateful. Limita orígenes y puertos, elimina reglas temporales y revisa exposición pública.


**Práctica y evidencia:** Define Security Groups con origen específico y puertos necesarios. **Evidencia:** demuestra reducción de exposición y evita reglas 0.0.0.0/0 injustificadas.

#### 29.2.08 — CloudTrail
CloudTrail registra actividad de API y cambios de control plane en AWS. Centraliza y protege trails, valida cobertura regional y crea alertas para acciones privilegiadas.


**Práctica y evidencia:** Consulta eventos CloudTrail de cambios de identidad y recursos. **Evidencia:** identifica actor, acción, recurso y hora.

#### 29.2.09 — CloudWatch
CloudWatch recopila métricas, logs y eventos para monitoreo y alertas. Define retención, alarmas y dashboards por servicio y evita almacenar secretos en logs.


**Práctica y evidencia:** Diseña una alarma CloudWatch para un indicador operativo de seguridad. **Evidencia:** registra métrica, umbral y acción de respuesta.

#### 29.2.10 — GuardDuty (introducción)
GuardDuty analiza señales y fuentes de AWS para identificar amenazas potenciales. Comprende fuentes, severidad y límites, valida hallazgos y establece respuesta sin automatizar acciones disruptivas sin control.


**Práctica y evidencia:** Analiza el propósito de GuardDuty y sus fuentes de señal. **Evidencia:** explica hallazgo, severidad y validación antes de responder.

### Módulo 29.3 — Azure Security

#### 29.3.01 — Entra ID
Entra ID administra identidades, aplicaciones y acceso en el ecosistema Microsoft. Configura MFA, acceso condicional, roles y protección de cuentas privilegiadas.


**Práctica y evidencia:** Dibuja tenant, identidad, aplicación y recurso de Entra ID. **Evidencia:** identifica autenticación, autorización y límites de administración.

#### 29.3.02 — RBAC
Azure RBAC asigna roles a identidades sobre ámbitos como management group, subscription, resource group o recurso. Asigna en el ámbito mínimo necesario y revisa herencia.


**Práctica y evidencia:** Asigna RBAC a recursos Azure con alcance mínimo. **Evidencia:** compara rol a nivel de recurso, grupo y suscripción.

#### 29.3.03 — Azure Policies
Azure Policy evalúa y puede imponer reglas de configuración sobre recursos. Distingue audit, deny y deploy effects y prueba políticas antes de aplicarlas a entornos productivos.


**Práctica y evidencia:** Define una Azure Policy para requerir cifrado o restringir ubicación en un entorno de diseño. **Evidencia:** explica cumplimiento, efecto y excepción.

#### 29.3.04 — Key Vault
Key Vault almacena secretos, claves y certificados con controles de acceso y auditoría. Usa identidades administradas, rotación y permisos mínimos y evita exportar secretos innecesariamente.


**Práctica y evidencia:** Guarda un secreto de prueba en Key Vault y diseña acceso mediante identidad administrada. **Evidencia:** demuestra rotación y ausencia de secreto hardcodeado.

#### 29.3.05 — Defender for Cloud (introducción)
Defender for Cloud ofrece postura de seguridad y protección de cargas en Azure y entornos conectados. Interpreta recomendaciones y alertas según cobertura y plan habilitado; valida antes de automatizar remediación.


**Práctica y evidencia:** Interpreta recomendaciones de Defender for Cloud y valida aplicabilidad antes de remediar. **Evidencia:** prioriza hallazgos por riesgo y contexto.

### Módulo 29.4 — Google Cloud Security

#### 29.4.01 — IAM
Google Cloud IAM controla acceso a recursos mediante principals, roles y policies. Prefiere roles predefinidos o personalizados mínimos y evita permisos básicos demasiado amplios.


**Práctica y evidencia:** Diseña roles IAM en Google Cloud con permisos mínimos y grupos. **Evidencia:** evita asignar roles básicos amplios sin justificación.

#### 29.4.02 — Service Accounts
Service Accounts representan identidades para aplicaciones y servicios. Evita claves descargables cuando sea posible, limita permisos y usa identidades adjuntas o federadas.


**Práctica y evidencia:** Configura o modela una service account con identidad dedicada y rotación/credenciales federadas. **Evidencia:** demuestra que no se comparte entre aplicaciones.

#### 29.4.03 — VPC
VPC en Google Cloud conecta recursos mediante redes, subredes y reglas de firewall. Diseña alcance global/regional, rutas y controles de entrada/salida con mínimo privilegio.


**Práctica y evidencia:** Diseña VPC, subredes y reglas de firewall de Google Cloud. **Evidencia:** identifica rutas y flujos permitidos.

#### 29.4.04 — Cloud Logging
Cloud Logging centraliza logs de servicios, aplicaciones y auditoría. Configura sinks, retención y controles de acceso y valida que eventos críticos no se excluyan.


**Práctica y evidencia:** Consulta Cloud Logging para un evento de IAM de laboratorio. **Evidencia:** identifica actor, recurso y método.

#### 29.4.05 — Cloud Monitoring
Cloud Monitoring recoge métricas, uptime y alertas sobre recursos y servicios. Define umbrales basados en SLO y protege notificaciones y dashboards.


**Práctica y evidencia:** Define una métrica y alerta de Cloud Monitoring para servicio crítico. **Evidencia:** documenta umbral y runbook.

### Módulo 29.5 — Docker Security

#### 29.5.01 — Image Security
Image Security revisa imágenes de contenedor por origen, capas, paquetes, configuración y vulnerabilidades. Usa bases mínimas, digests y firmas cuando proceda y reconstruye imágenes vulnerables.


**Práctica y evidencia:** Escanea una imagen de contenedor de laboratorio y fija digest/base confiable. **Evidencia:** registra CVEs, severidad y política de aceptación.

#### 29.5.02 — Container Isolation
Container Isolation limita interacción entre procesos y host mediante namespaces, cgroups, capacidades y políticas. No consideres el contenedor una frontera absoluta; evita privilegios y montajes innecesarios.


**Práctica y evidencia:** Explica namespaces, cgroups y límites de contenedor. **Evidencia:** identifica qué aislamiento aporta el runtime y qué comparte con host.

#### 29.5.03 — Privileges
Privileges en contenedores determinan capacidades y permisos sobre host y recursos. Elimina capacidades no necesarias, evita `--privileged` y limita acceso a sockets y dispositivos.


**Práctica y evidencia:** Inspecciona capabilities y privilegios de un contenedor. **Evidencia:** elimina capacidades no necesarias en imagen de prueba.

#### 29.5.04 — Non-root Containers
Non-root Containers ejecutan procesos con UID no privilegiado para reducir impacto de compromiso. Ajusta permisos de archivos, puertos y volúmenes para que la aplicación funcione sin root.


**Práctica y evidencia:** Ejecuta contenedor como usuario no root y verifica UID efectivo. **Evidencia:** demuestra que el proceso no tiene privilegios de host.

#### 29.5.05 — Vulnerability Scanning
Vulnerability Scanning compara paquetes e imágenes con bases de vulnerabilidades conocidas. Revisa severidad, explotabilidad y disponibilidad de parche y establece proceso de excepción y actualización.


**Práctica y evidencia:** Compara resultados de escaneo de imagen antes/después de actualizar paquetes. **Evidencia:** documenta falsos positivos y riesgo residual.

#### 29.5.06 — Secrets
Secrets en Docker deben entregarse fuera de imágenes y capas versionadas. Utiliza mecanismos de secretos del entorno y limita montaje, acceso y duración.


**Práctica y evidencia:** Inyecta secreto de prueba en runtime desde almacén seguro y evita copiarlo en capas de imagen. **Evidencia:** inspecciona imagen y logs.

#### 29.5.07 — Secure Dockerfiles
Secure Dockerfiles fijan imágenes base, reducen paquetes, usan usuario no privilegiado y evitan secretos. Ordena instrucciones, valida builds y genera artefactos trazables.


**Práctica y evidencia:** Escribe Dockerfile con base fijada, paquetes mínimos, usuario no root y build multi-stage. **Evidencia:** inspecciona configuración final.

### Módulo 29.6 — Kubernetes Security

#### 29.6.01 — RBAC
Kubernetes RBAC define permisos sobre recursos del clúster mediante Roles, ClusterRoles y bindings. Evita `cluster-admin` generalizado y revisa service accounts y permisos heredados.


**Práctica y evidencia:** Define RBAC Kubernetes por namespace y ServiceAccount. **Evidencia:** demuestra que un rol no puede listar secretos fuera de su alcance.

#### 29.6.02 — Network Policies
Network Policies restringen comunicación entre Pods según etiquetas, namespaces y puertos, si el plugin de red las soporta. Define política por defecto y prueba flujos permitidos y denegados.


**Práctica y evidencia:** Crea NetworkPolicy para limitar tráfico entre namespaces en clúster local. **Evidencia:** prueba flujo permitido y bloqueado.

#### 29.6.03 — Secrets
Secrets en Kubernetes almacenan información sensible, pero requieren cifrado en reposo, RBAC mínimo y protección de etcd. Usa external secret management y rotación.


**Práctica y evidencia:** Restringe acceso a Secrets y usa cifrado en reposo según capacidad del clúster. **Evidencia:** explica por qué base64 no protege el secreto.

#### 29.6.04 — Pod Security
Pod Security aplica estándares y controles sobre privilegios, namespaces, capabilities y filesystem de Pods. Define nivel adecuado y excepciones justificadas; valida compatibilidad antes de bloquear workloads.


**Práctica y evidencia:** Aplica Pod Security Standards o controles equivalentes a un workload de laboratorio. **Evidencia:** comprueba non-root, capabilities y filesystem read-only cuando proceda.

#### 29.6.05 — Image Security
Image Security en Kubernetes exige imágenes confiables, escaneadas y fijadas por digest cuando corresponda. Aplica políticas de admisión y evita tags mutables sin trazabilidad.


**Práctica y evidencia:** Fija imágenes por digest y verifica procedencia antes del despliegue. **Evidencia:** registra origen y política de admisión.

#### 29.6.06 — Cluster Hardening
Cluster Hardening reduce superficie del plano de control, nodos, API server, etcd y componentes. Mantén versiones soportadas, acceso administrativo restringido, auditoría y backups.


**Práctica y evidencia:** Aplica baseline de clúster: API server, RBAC, audit logs, etcd y acceso administrativo. **Evidencia:** checklist con evidencia.

#### 29.6.07 — Runtime Security
Runtime Security observa comportamiento de contenedores y nodos durante ejecución. Define señales y respuesta, limita falsos positivos y protege telemetría del clúster.


**Práctica y evidencia:** Configura monitoreo de runtime en clúster de laboratorio y evalúa alertas. **Evidencia:** distingue señal de comportamiento sospechoso de falso positivo.

### Módulo 29.7 — Supply Chain Security

#### 29.7.01 — Dependency Security
Dependency Security gestiona riesgos de bibliotecas directas y transitivas. Mantén inventario, actualizaciones, revisión de licencias y controles de procedencia.


**Práctica y evidencia:** Inventaría dependencias directas/transitivas y asigna propietario de actualización. **Evidencia:** conserva lockfile y versión.

#### 29.7.02 — Dependency Scanning
Dependency Scanning compara dependencias con avisos y bases de vulnerabilidades. Revisa versiones afectadas y rutas de uso, prioriza riesgo y evita actualizar sin pruebas.


**Práctica y evidencia:** Ejecuta escaneo de dependencias y prioriza por explotabilidad y contexto. **Evidencia:** registra CVE, paquete y remediación.

#### 29.7.03 — SBOM
SBOM describe componentes de software y sus relaciones en un artefacto. Genera inventarios consistentes y vincúlalos a versión/build para apoyar respuesta a vulnerabilidades.


**Práctica y evidencia:** Genera SBOM para un artefacto y documenta formato y alcance. **Evidencia:** verifica que lista componentes reales.

#### 29.7.04 — Software Bill of Materials
Software Bill of Materials es la lista estructurada de componentes, versiones y relaciones de un software. Define formato y alcance, actualiza por build y valida completitud.


**Práctica y evidencia:** Compara CycloneDX y SPDX a nivel de propósito y metadatos. **Evidencia:** selecciona formato y justifica compatibilidad.

#### 29.7.05 — Artifact Integrity
Artifact Integrity verifica que artefactos no hayan sido alterados entre build, almacenamiento y despliegue. Usa hashes, firmas, controles de acceso y repositorios protegidos.


**Práctica y evidencia:** Verifica checksum/digest de un artefacto antes de promoverlo. **Evidencia:** demuestra rechazo de artefacto alterado.

#### 29.7.06 — Artifact Signing
Artifact Signing vincula un artefacto con una identidad de firma y permite verificar integridad y procedencia. Protege claves de firma, define confianza y automatiza verificación antes de desplegar.


**Práctica y evidencia:** Firma un artefacto de laboratorio y valida firma con identidad pública esperada. **Evidencia:** registra cadena de confianza y rotación.

#### 29.7.07 — Provenance
Provenance documenta cómo, dónde y con qué materiales se construyó un artefacto. Registra workflow, fuentes, dependencias y parámetros y protege atestaciones frente a alteración.


**Práctica y evidencia:** Genera atestación de procedencia de build con repositorio, commit y workflow. **Evidencia:** vincula artefacto con proceso reproducible.

#### 29.7.08 — Malicious Dependencies
Malicious Dependencies son paquetes creados o comprometidos para robar datos, ejecutar código o abrir acceso. Verifica mantenedores, reputación, permisos, cambios y procedencia antes de incorporar dependencias.


**Práctica y evidencia:** Evalúa una dependencia sospechosa por mantenedor, historial, permisos y comportamiento documentado. **Evidencia:** documenta decisión de cuarentena sin ejecutar código desconocido.

#### 29.7.09 — Software Supply Chain Attacks
Software Supply Chain Attacks comprometen dependencias, herramientas, pipelines, repositorios o distribución. Aplica controles de origen, firma, aislamiento de builds, revisión y monitoreo.


**Práctica y evidencia:** Dibuja cadena de suministro desde código hasta distribución y enumera puntos de compromiso. **Evidencia:** asigna controles a cada transición.

### Módulo 29.8 — DevSecOps

#### 29.8.01 — Secure SDLC
Secure SDLC integra requisitos, diseño, desarrollo, pruebas, entrega y operación con controles de seguridad. Define responsables y evidencias en cada fase y revisa el proceso con cambios del riesgo.


**Práctica y evidencia:** Integra seguridad desde requisitos hasta mantenimiento en un SDLC. **Evidencia:** mapea controles y responsables por fase.

#### 29.8.02 — SAST
SAST analiza código fuente o compilado sin ejecutar la aplicación para detectar patrones vulnerables. Ajusta reglas al lenguaje, valida hallazgos y evita tratar el resultado como cobertura completa.


**Práctica y evidencia:** Ejecuta SAST en un proyecto de prueba y clasifica hallazgos. **Evidencia:** corrige uno y añade test.

#### 29.8.03 — DAST
DAST evalúa una aplicación en ejecución desde interfaces observables. Usa entornos y datos de prueba, define alcance y tasa y valida resultados manualmente.


**Práctica y evidencia:** Ejecuta DAST contra aplicación local autorizada y valida resultados. **Evidencia:** documenta alcance y limitaciones.

#### 29.8.04 — SCA
SCA analiza dependencias y licencias de componentes de terceros. Incluye dependencias transitivas, evalúa exposición real y establece proceso de actualización o excepción.


**Práctica y evidencia:** Ejecuta SCA sobre lockfile y revisa licencias y vulnerabilidades. **Evidencia:** prioriza actualización compatible.

#### 29.8.05 — Container Scanning
Container Scanning revisa imágenes y capas por vulnerabilidades, secretos y malas configuraciones. Escanea antes de publicar y vuelve a evaluar cuando cambian las bases de datos de vulnerabilidades.


**Práctica y evidencia:** Escanea contenedores en CI y define umbrales de bloqueo. **Evidencia:** demuestra gate con imagen vulnerable de prueba.

#### 29.8.06 — Infrastructure Scanning
Infrastructure Scanning evalúa configuraciones de cloud, redes y recursos frente a políticas de seguridad. Usa credenciales de solo lectura cuando sea posible y evita cambios automáticos sin revisión.


**Práctica y evidencia:** Escanea IaC antes de aplicar cambios y revisa findings manualmente. **Evidencia:** bloquea configuración insegura en pipeline.

#### 29.8.07 — Secrets Scanning
Secrets Scanning busca tokens, claves y credenciales expuestas en código, historial y artefactos. Ante un hallazgo, revoca/rota el secreto; borrar la línea no invalida la credencial filtrada.


**Práctica y evidencia:** Ejecuta secret scanning con datos sintéticos y configura revocación/rotación ante hallazgo. **Evidencia:** demuestra que secreto no llega al repositorio.

#### 29.8.08 — Security Gates
Security Gates bloquean promoción cuando se incumplen umbrales definidos de calidad o seguridad. Define criterios transparentes, excepciones con vencimiento y evidencia de aceptación de riesgo.


**Práctica y evidencia:** Define security gates proporcionales al riesgo y proceso de excepción temporal. **Evidencia:** documenta responsable y vencimiento de excepción.

#### 29.8.09 — Security Automation
Security Automation ejecuta tareas de análisis, enriquecimiento y remediación con controles y auditoría. Limita permisos, valida entradas y exige aprobación humana para acciones de alto impacto.


**Práctica y evidencia:** Automatiza validaciones de seguridad sin ocultar logs ni resultados. **Evidencia:** demuestra reproducibilidad y trazabilidad.

#### 29.8.10 — CI/CD Security
CI/CD Security protege repositorios, runners, workflows, artefactos, secretos y permisos de despliegue. Separa entornos, fija acciones y controla eventos de forks y pull requests externos.


**Práctica y evidencia:** Protege CI/CD con permisos mínimos, aislamiento de jobs y aprobación de entornos. **Evidencia:** analiza riesgo de ejecución desde pull request.

#### 29.8.11 — Herramientas
La entrada «Herramientas» agrupa utilidades de DevSecOps listadas en las siguientes lecciones. Se conserva como rótulo curricular y no como herramienta independiente.


**Práctica y evidencia:** Compara herramientas de seguridad por función, licencia, cobertura y mantenimiento. **Evidencia:** matriz de selección.

#### 29.8.12 — Trivy
Trivy escanea imágenes, repositorios, sistemas de archivos y configuraciones compatibles en busca de vulnerabilidades y errores. Fija versión, revisa severidad y contexto y valida hallazgos.


**Práctica y evidencia:** Ejecuta Trivy sobre imagen o filesystem de laboratorio y revisa hallazgos. **Evidencia:** conserva versión, comando y resultado.

#### 29.8.13 — Gitleaks
Gitleaks detecta posibles secretos en repositorios e historial. Configura exclusiones justificadas y, ante una exposición real, revoca y rota credenciales antes de limpiar historial.


**Práctica y evidencia:** Ejecuta Gitleaks sobre repositorio de prueba con secretos sintéticos. **Evidencia:** valida detección y evita usar credenciales reales.

#### 29.8.14 — OWASP Dependency-Check
OWASP Dependency-Check identifica dependencias y las relaciona con vulnerabilidades conocidas. Revisa precisión de identificación, fuentes y falsos positivos y no asumas que un resultado limpio implica ausencia de riesgo.


**Práctica y evidencia:** Configura OWASP Dependency-Check en un proyecto de prueba y revisa identificación de componentes. **Evidencia:** explica falsos positivos y fuentes de datos.

#### 29.8.15 — GitHub Dependabot
GitHub Dependabot alerta sobre dependencias vulnerables y puede proponer actualizaciones. Configura ecosistemas y frecuencia, revisa changelogs y ejecuta pruebas antes de fusionar actualizaciones.


**Práctica y evidencia:** Revisa alertas Dependabot y evalúa actualización en rama de prueba. **Evidencia:** ejecuta suite y documenta compatibilidad.

#### 29.8.16 — Semgrep
Semgrep analiza código mediante reglas configurables para detectar patrones y vulnerabilidades. Selecciona reglas mantenidas, revisa falsos positivos y controla el alcance del análisis.


**Práctica y evidencia:** Configura Semgrep con reglas mantenidas y revisa hallazgos en código de prueba. **Evidencia:** documenta regla, severidad y corrección.

#### 29.8.17 — Terraform
Terraform permite declarar infraestructura cloud y revisar cambios mediante planes. Protege state, limita credenciales, valida módulos y no apliques cambios sin revisión del plan.


**Práctica y evidencia:** Revisa un plan Terraform con controles de IAM, red y almacenamiento. **Evidencia:** no aplica recursos reales; registra cambios destructivos potenciales.

#### 29.8.18 — GitHub Actions
GitHub Actions ejecuta pipelines mediante workflows, jobs y runners. Fija versiones de acciones, restringe permisos de tokens, protege secretos y aísla ejecuciones de código no confiable.



**Práctica y evidencia:** Audita un workflow GitHub Actions por permisos, secrets, pinning de actions y eventos de PR. **Evidencia:** propone permisos mínimos y prueba de seguridad.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 71 orientaciones genéricas por explicaciones específicas de seguridad cloud, AWS/Azure/Google Cloud, Docker, Kubernetes, supply chain y DevSecOps.

**Revisión interna:** 71/71 entradas desarrolladas y cotejadas con el roadmap. Se aclaró «Herramientas» como rótulo curricular y se reforzaron responsabilidad compartida, IAM, almacenamiento, secretos, privilegios de contenedores, RBAC, SBOM, firma/procedencia y seguridad de pipelines. Pendiente: validar versiones de proveedores/herramientas, desplegar laboratorios efímeros con presupuesto limitado, probar gates y recuperación y obtener segunda revisión. No se desplegó infraestructura cloud ni se declara aprobación externa.
