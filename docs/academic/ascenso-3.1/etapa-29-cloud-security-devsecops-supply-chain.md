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
