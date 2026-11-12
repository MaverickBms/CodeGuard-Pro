# Validación de integración — Electron, Django y PyInstaller

**Rama:** `main`  
**Línea base de código:** `b82a249b203548f54b92c9fc85bc609bd2c7a478`  
**Fecha de actualización:** 2026-11-12  
**Alcance:** registrar la evidencia local confirmada por el propietario y separar las pruebas completadas de los criterios aún abiertos. No configura distribución remota.

## 1. Resultado confirmado

El propietario confirmó:

- **138 pruebas automatizadas:** todas aprobadas (OK).
- **PyInstaller:** compilación correcta de `dist-server/CodeGuardServer/CodeGuardServer`.
- **Smoke test:** el binario carga Django y ejecuta el despacho `--sync-knowledge`; el comando falla de forma controlada cuando faltan endpoints, allowlist y claves de confianza.
- **AppImage:** generación correcta de `dist/CodeGuard-Pro-1.0.0-x86_64.AppImage` (Linux x86_64).
- **Ejecución:** AppImage iniciado usando un directorio temporal para los datos. El proceso se terminó mediante SIGTERM y reportó código 143.

## 2. Límites de lo que demuestra la evidencia

Hay dos modos distintos de `CodeGuardServer`: el modo puntual `--sync-knowledge` y el modo servidor normal (migraciones, comprobación de ASCENSO, WSGI y Waitress en `127.0.0.1:<CODEGUARD_PORT>`).

El smoke test de `--sync-knowledge` **no demuestra** que el modo servidor normal haya arrancado, que Waitress esté escuchando, que Electron haya recibido una respuesta HTTP ni que la interfaz se haya cargado correctamente.

El código de salida 143 significa que el proceso terminó por SIGTERM. Por sí solo no demuestra que la aplicación haya ejecutado un cierre ordenado desde su menú ni que haya liberado todos los procesos hijos.

El puerto 11434 no se toma como evidencia de Django: es habitual en instalaciones de Ollama y no identifica por sí mismo el proceso ni el puerto dinámico que Electron asigna a CodeGuard.

## 3. Estado de aceptación

| Criterio | Estado | Evidencia / observación |
|---|---|---|
| Suite automatizada | **Confirmado** | 138 pruebas OK, según el propietario |
| Compilación PyInstaller | **Confirmado** | Binario generado |
| Despacho `--sync-knowledge` | **Confirmado** | Smoke test y error controlado por configuración ausente |
| Generación AppImage | **Confirmado** | AppImage Linux x86_64 generado |
| Inicio del AppImage | **Parcial** | Iniciado con directorio temporal |
| Modo servidor normal / Waitress | **Pendiente** | No hay evidencia aportada de listener HTTP asociado al proceso Django durante la ejecución |
| Carga de panel Electron | **Pendiente** | No se ha confirmado visualmente la carga de la interfaz |
| Navegación por ASCENSO y apertura de lección | **Pendiente** | No se ha realizado la comprobación gráfica |
| Listener exclusivamente en loopback | **Pendiente** | Debe verificarse el puerto dinámico mientras la aplicación está activa |
| Cierre desde el menú y procesos hijos | **Pendiente** | SIGTERM/código 143 no sustituye la prueba de cierre normal |
| Persistencia de perfil y progreso | **Pendiente** | Debe comprobarse sin modificar ni borrar el perfil real |
| Sincronización remota | **No configurada** | No hay endpoint, allowlist ni claves de producción |

**Conclusión:** la integración está parcialmente validada. No debe declararse la aceptación completa de Electron + Django ni que el producto está listo para distribución.

## 4. Consideración sobre ASCENSO en instalaciones nuevas

La revisión de `server_entry.py` en `b82a249` confirma que el servidor empaquetado ya no carga automáticamente el roadmap ASCENSO. Comprueba si existe en la base de datos y, si no existe, informa que debe ejecutarse `manage.py cargar_ascenso`.

Por tanto, un perfil nuevo puede iniciar el servidor sin contenido curricular cargado. La prueba de aceptación debe confirmar la carga explícita del roadmap en el directorio de datos de prueba y, posteriormente, navegar las etapas y lecciones desde la GUI. No ejecutar `cargar_ascenso --recrear` sobre datos reales: esa opción puede eliminar progreso.

## 5. Procedimiento pendiente de aceptación GUI

Realizar en una sesión gráfica Linux. Mantener aislados los datos de prueba:

```bash
cd ~/Documentos/CodeGuard

TEST_DATA="$(mktemp -d)"
CODEGUARD_DATA_DIR="$TEST_DATA" ./dist/CodeGuard-Pro-1.0.0-x86_64.AppImage
```

Con la aplicación abierta:

1. Confirmar que la ventana Electron muestra el panel principal.
2. Identificar el puerto dinámico asignado a CodeGuard y confirmar el listener con `ss -ltnp`; debe estar ligado únicamente a `127.0.0.1`.
3. Confirmar qué proceso mantiene ese listener. No asumir que el puerto 11434 pertenece a Django.
4. Si ASCENSO no está cargado en el perfil temporal, ejecutar el comando de carga curricular previsto para ese perfil; no usar `--recrear` sobre datos reales.
5. Navegar al menos una etapa, abrir un módulo y una lección. Confirmar que el contenido se muestra sin conexión a un servicio central.
6. Cerrar la aplicación desde su menú.
7. Comprobar que ya no quedan procesos hijos ni listeners de CodeGuard:
   ```bash
   pgrep -af 'CodeGuardServer|CodeGuard-Pro'
   ss -ltnp
   ```
8. Solo después de completar la prueba aislada, verificar la persistencia del perfil habitual sin borrar, reemplazar ni migrar destructivamente su base de datos.

Mantener ausentes las variables de configuración remota mientras no se haya aprobado y configurado un distribuidor confiable. La aplicación debe conservar el funcionamiento local aunque la sincronización esté desactivada.

## 6. Reglas de cierre

La aceptación de integración solo podrá cerrarse cuando se disponga de evidencia de:

- arranque del modo servidor normal y respuesta HTTP de Django;
- panel Electron cargado;
- navegación por ASCENSO y apertura de una lección;
- listener restringido a `127.0.0.1`;
- cierre normal desde el menú y ausencia de procesos/listeners huérfanos;
- preservación de los datos del perfil habitual;
- funcionamiento offline con sincronización remota desactivada.

## 7. Fuera del alcance

- Selección de proveedor de hosting o CDN.
- Publicación remota de manifiestos, firmas o ZIP.
- Creación o instalación de claves de producción.
- Prueba de descarga real desde un endpoint externo.
- Cambios de código fuera de las correcciones ya integradas en `main`.
- Despliegue o publicación de una versión de distribución.

Estas acciones requieren decisiones y autorizaciones independientes.
