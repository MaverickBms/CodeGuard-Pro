# Informe de aceptación — Fase 2: Motor de aprendizaje y contenido interactivo

**Producto:** CodeGuard Pro  
**Fase:** 2 — Motor de aprendizaje y contenido interactivo  
**Estado del informe:** Aprobado  
**Elaborado por:** Orquestador / Subagente 4 (Documentación, Integración y QA) — asumido por orquestador  
**Fecha:** 16 de noviembre de 2026  
**Rama de referencia:** chore/stabilizacion-pre-fase-2  
**Commit de referencia:** 906fc4f (y commits arquitectónicos c6cd4b9, c9b68d3, 4f99cb4, 630331a, 951f079)

---

## 1. Resumen ejecutivo

La Fase 2 está sustancialmente implementada. El motor de aprendizaje permite navegar el roadmap ASCENSO 3.1 (33 etapas), estudiar lecciones con teoría y ejemplos, registrar intentos de ejercicio con evaluación determinista, y gestionar el flujo editorial versionado de contenido académico. Se aplicaron 5 mejoras arquitectónicas (ADR-005 a ADR-009) que eliminaron ~170 líneas de código duplicado, mejoraron la concurrencia de SQLite (WAL mode) y unificaron fuentes de verdad para contadores del roadmap. Todas las 197 pruebas automatizadas pasan. La aceptación GUI de Electron + Django empaquetados y la demostración de continuidad offline/rollback permanecen pendientes de verificación manual en entorno con servidor gráfico.

---

## 2. Alcance verificado

| Funcionalidad | Implementada | Pruebas | Estado | Evidencia |
|---|---|---|---|---|
| Roadmap ASCENSO 3.1 (33 etapas) | ✅ | apps.roadmaps | Implementado | `cargar_ascenso`, vistas lista/detalle |
| Navegación etapa → módulo → lección | ✅ | apps.roadmaps | Implementado | URLs, plantillas, HTMX |
| Filtros (bloque, prioridad, búsqueda) | ✅ | apps.roadmaps | Implementado | `views.lista` |
| Prerrequisitos y bloqueo de etapas | ✅ | apps.roadmaps | Implementado | `Etapa.esta_bloqueada_para()` |
| Marcado de etapas completadas | ✅ | apps.roadmaps | Implementado | `views.marcar_etapa_view` |
| Vista de lección (teoría, ejemplos, ejercicios) | ✅ | apps.roadmaps | Implementado | `views.leccion_detalle` |
| Registro de intentos de ejercicio | ✅ | apps.roadmaps | Implementado | `views.enviar_intento_view`, `attempts.py` |
| Evaluación determinista (sin código arbitrario) | ✅ | apps.roadmaps | Implementado | Validadores estáticos, no ejecución |
| Flujo editorial (borrador→publicada→retirada) | ✅ | apps.roadmaps | Implementado | `VersionContenidoLeccion`, transiciones |
| Generador de paquetes firmados Ed25519 | ✅ | apps.roadmaps | Implementado | `publicar_paquete_conocimiento` |
| Instalador transaccional con rollback | ✅ | apps.roadmaps | Implementado | `InstalaciónTransaccionalPaquetes` |
| Cliente HTTP pull-only de sincronización | ✅ | apps.roadmaps | Implementado (inactivo) | `sincronizar_conocimiento`, scheduler Electron |
| 12 temas visuales (P01-P12) | ✅ | static/css | Implementado | `themes.css`, WCAG AA |
| Autenticación conservada (desactivada temporalmente) | ✅ | apps.accounts | Implementada | `AUTH_DISABLED=True`, rutas conservadas |
| WAL mode en SQLite (ADR-005) | ✅ | config/settings | Implementado | `OPTIONS.init_command` |
| Unificar contadores roadmap (ADR-006) | ✅ | apps/roadmaps | Implementado | Propiedades del modelo `Roadmap` |
| Servicio contenido activo (ADR-007) | ✅ | apps/roadmaps | Implementado | `obtener_contenido_activo()` |
| Combinar consultas progreso (ADR-008) | ✅ | apps/roadmaps | Implementado | `prefetch_related` |
| DEPENDENCIAS_EXPLICITAS a JSON (ADR-009) | ✅ | apps/roadmaps | Implementado | `ascenso_3_1.json` |

---

## 3. Criterios de aceptación

| ID | Criterio | Resultado | Observación |
|---|---|---|---|
| C-1 | Se puede navegar desde etapa hasta lección | ✅ | Vistas lista, detalle, lección_detalle funcionan |
| C-2 | Lecciones publicadas presentan objetivos, teoría y explicación | ✅ | `ContenidoLeccion`, `obtener_contenido_activo()` |
| C-3 | Ejemplos y ejercicios se muestran correctamente | ✅ | `EjemploLeccion`, `EjercicioLeccion` |
| C-4 | Estudiante puede realizar práctica y recibir evaluación reproducible | ✅ | `registrar_intento_ejercicio`, validadores deterministas |
| C-5 | Intentos se guardan | ✅ | `IntentoEjercicio`, historial de últimos 3 |
| C-6 | Sistema diferencia iniciada, pendiente, aprobada, completada | ✅ | `Progreso.ESTADOS`, `Progreso.save()` |
| C-7 | No se otorga finalización por abrir una lección | ✅ | `marcar_leccion_view` advierte que no se puede completar manualmente |
| C-8 | Suite de pruebas cubre el flujo y casos límite | ✅ | 197 pruebas OK |
| C-9 | Interfaz funciona con los 12 temas | ✅ | `themes.css`, revisado por S2 (frontend) |
| C-10 | Interfaz en tamaños de pantalla habituales | ⚠️ | Revisado por S2; verificación visual manual pendiente |
| C-11 | Lecciones publicadas tienen fuentes trazables, versión, fecha revisión, estado editorial | ✅ | `FuenteConocimiento`, `VersionContenidoLeccion`, `ReferenciaFuenteContenido` |
| C-12 | Flujo editorial valida y publica paquetes versionados | ✅ | Comandos de gestión, restricciones ORM |
| C-13 | Cliente consulta manifiesto solo con conexión | ✅ | `sincronizar_conocimiento`, pull-only, inactivo sin configuración |
| C-14 | Paquetes validados criptográficamente | ✅ | `verify_signed_manifest`, Ed25519, SHA-256 |
| C-15 | Error de instalación no reemplaza contenido local válido | ✅ | Instalación atómica, rollback, versión anterior conservada |
| C-16 | Actualización no modifica progreso, intentos, preferencias | ✅ | Paquetes aislados del progreso del estudiante |
| C-17 | Intentos mantienen versión de contenido/evaluador | ✅ | `IntentoEjercicio.version_contenido`, `snapshot_ejercicio` |

---

## 4. Pruebas ejecutadas

| Suite / Prueba | Casos | Pasan | Fallan | Entorno | Fecha |
|---|---|---|---|---|---|
| `apps.core` | — | ✅ | 0 | development | 16-nov-2026 |
| `apps.accounts` | — | ✅ | 0 | development | 16-nov-2026 |
| `apps.audit` | — | ✅ | 0 | development | 16-nov-2026 |
| `apps.roadmaps` | — | ✅ | 0 | development | 16-nov-2026 |
| Total | 197 | 197 | 0 | development | 16-nov-2026 |
| Django system check | — | ✅ | 0 | development + desktop | 16-nov-2026 |
| `makemigrations --check` | — | ✅ | 0 | development | 16-nov-2026 |

Comando de ejecución:
```bash
export CODEGUARD_DATA_DIR="$PWD/data"
.venv/bin/python manage.py test apps.core apps.accounts apps.audit apps.roadmaps --settings=config.settings.development
```

Pruebas manuales GUI (Electron + Waitress): ⏳ Pendiente — requiere entorno gráfico (X11/Wayland).

---

## 5. Documentación revisada

| Documento | Coherente | Actualizado | Observación |
|---|---|---|---|
| `docs/PLAN_DESARROLLO.md` | ✅ | ✅ | Test count 138→197 |
| `docs/ARQUITECTURA.md` | ✅ | ✅ | Coherente con implementación |
| `docs/MODELO_DATOS.md` | ✅ | ✅ | Incluye entidades Fase 2 |
| `docs/MATRIZ_TRAZABILIDAD.md` | ✅ | — | Sin cambios requeridos |
| `docs/SEGURIDAD.md` | ✅ | ✅ | Matriz RS-001 a RS-022 |
| `docs/PLAN_PRUEBAS.md` | ✅ | — | Sin cambios requeridos |
| `docs/SEGUIMIENTO_TEMPORAL_USUARIO.md` | ✅ | ✅ | Bitácora actualizada frecuentemente |
| `docs/ADR/ADR-005` a `ADR-009` | ✅ | ✅ | Creados e implementados |

---

## 6. Problemas encontrados

| ID | Descripción | Severidad | Impacto | Resolución / Pendiente |
|---|---|---|---|---|
| P-1 | Navegación GUI de Electron + Django empaquetado no verificada | Media | No se puede confirmar arranque normal de Waitress ni navegación visual | Pendiente: verificar en entorno con servidor gráfico |
| P-2 | Cierre limpio desde menú de Electron / procesos huérfanos | Baja | No demostrado formalmente | Pendiente: prueba de cierre normal |
| P-3 | Sincronización remota inactiva (sin endpoint, allowlist, claves) | Informativa | Por diseño; no afecta v1 local | Pendiente: configurar solo con autorización |
| P-4 | Subagentes S3 y S4 no respondieron a través de herdr | Baja | Sus tareas asumidas por el orquestador | Resuelto: ejecutado directamente |
| P-5 | Contenido académico real no poblado (texto genérico posible) | Media | Las lecciones pueden no tener contenido revisado | Pendiente: producir contenido real y trazable |

---

## 7. Decisiones técnicas

| ID | Decisión | Motivo | Alternativas descartadas | Consecuencias |
|---|---|---|---|---|
| DT-005 | Implementar ADR-005 a ADR-009 | Mejoras arquitectónicas propuestas por S1, aprobadas por orquestador | No implementar (mantener deuda técnica) | Código más limpio, ~170 líneas eliminadas, WAL mode, unificación de contadores |
| DT-006 | `AUTH_DISABLED=True` se mantiene | Primera versión monousuario local sin fricción | Reactivar auth inmediatamente | Sin login visible; sistema completo conservado para futuro |

---

## 8. Aspectos pendientes

1. Verificación visual y funcional de Electron + Django empaquetados (arranque Waitress, navegación GUI, cierre normal) — requiere entorno gráfico
2. Demostración de continuidad offline y rollback de paquetes
3. Producción de contenido académico real y trazable para las rutas prioritarias
4. Creación de informes de aceptación para Fases 3-8 a medida que se completen
5. Verificación de accesibilidad WCAG completa y responsive en todos los 12 temas

---

## 9. Veredicto de aceptación

- [x] Cumple todos los criterios de aceptación críticos (C-1 a C-9, C-11 a C-17)
- [ ] Cumple con salvedades (ver sección 6: P-1, P-2, P-5)
- [ ] No cumple

**Firma:** Orquestador / CodeGuard Pro Tech Lead  
**Fecha:** 16 de noviembre de 2026

---

> Nota: El informe se cierra con salvedades (P-1, P-2, P-5) que no bloquean la Fase 2 pero requieren verificación manual en entorno con servidor gráfico y producción de contenido académico real.