# CodeGuard Pro — Windows

**Estado de la guía:** actualizado el 19-11-2026. La compilación Windows está definida; la aceptación de instalación limpia y primer arranque continúa pendiente. No considerar el paquete listo para distribución hasta cerrar los criterios de QA.

## Arquitectura actual

CodeGuard Pro utiliza:

- Electron como aplicación de escritorio.
- Django 5.2 como aplicación local.
- Waitress como servidor WSGI local.
- SQLite en el directorio de datos del usuario.
- PyInstaller para empaquetar el servidor Django como `CodeGuardServer.exe`.
- electron-builder para generar dos artefactos Windows x64: instalador NSIS y ejecutable portable. Ambos objetivos están declarados explícitamente en `package.json`.

La arquitectura anterior basada en PySide6/`desktop/main.py` ya no corresponde al producto activo.

## Requisitos para construir en Windows

- Windows 10/11 de 64 bits.
- Python y pip.
- Node.js 20+ y npm.
- Herramientas de compilación compatibles con las dependencias instaladas.
- Espacio libre suficiente para dependencias, archivos intermedios y artefactos.

El equipo destino que instala un paquete final no debería necesitar Python, Node.js, Django ni el entorno virtual del desarrollador. Esta independencia debe confirmarse con la prueba D-1 del plan QA.

## Archivos principales

| Archivo | Función |
|---|---|
| `build_windows.bat` | Orquesta la compilación Windows |
| `CodeGuardServer.spec` | Configuración PyInstaller del servidor Django |
| `package.json` | Configuración electron-builder y recursos empaquetados |
| `electron/main.js` | Ciclo de vida Electron, servidor local, ventana y sincronización opcional |
| `server_entry.py` | Entrada del servidor Django empaquetado |
| `requirements.txt` | Dependencias Python fijadas |
| [Informe QA integral](https://github.com/MaverickBms/CodeGuard-Pro/blob/documentation/docs/INFORME_QA_INTEGRAL_2026-11-16.md) | Hallazgos, riesgos y criterios de liberación |

## Construcción

Desde PowerShell o CMD, en la raíz del repositorio:

```bat
build_windows.bat
```

El script instala dependencias Python y ejecuta `npm run build:win`. Ese comando orquesta, en orden estricto:

1. `npm run build:server`: selecciona Python del entorno `.venv` (o Python del sistema), elimina el ejecutable anterior y genera `dist-server\\CodeGuardServer\\CodeGuardServer.exe` mediante PyInstaller.
2. Genera `dist-server\\.codeguard-server-build.json` con plataforma, arquitectura, nombre del ejecutable y SHA-256 del binario recién creado.
3. `npm run verify:server`: comprueba que el ejecutable existe, es ejecutable y coincide con el manifiesto de compilación.
4. Solo si las verificaciones anteriores terminan correctamente, ejecuta electron-builder para producir los objetivos NSIS y portable de Windows x64.

`build_windows.bat` delega la generación del servidor a este flujo para evitar dos rutas de build distintas. Instala las dependencias Node de forma reproducible con `npm ci`, respetando `package-lock.json`. No ejecutar `electron-builder` directamente para generar un paquete de distribución: usar `npm run build:win`, `npm run build:linux` o `npm run build`. Los ejecutables Windows se guardan en `dist/`; sus nombres finales los determina electron-builder.

La compilación no crea ni migra una base de datos de desarrollo. Las migraciones y la carga de ASCENSO se ejecutan en el primer arranque del usuario, dentro de su directorio `userData`.

## Datos locales

La aplicación empaquetada utiliza el directorio de datos administrado por Electron (`app.getPath('userData')`) o el valor explícito de `CODEGUARD_DATA_DIR`. Allí deben permanecer la base SQLite, logs, media y clave secreta. No se deben incluir datos personales del desarrollador dentro del instalador.

## Autenticación y tutor IA

- El modo sin autenticación está activo temporalmente (`AUTH_DISABLED = True`). No reactivar el flujo de autenticación sin la autorización del propietario.
- El tutor IA usa Ollama local de forma opcional. El equipo debe tener Ollama y el modelo instalado para obtener respuestas generativas; el resto del producto debe seguir funcionando si no están disponibles.
- No se debe enviar código ni datos académicos a servicios remotos en la configuración privada/offline.
- La ejecución arbitraria de código permanece bloqueada hasta disponer de un sandbox independiente y auditado.

## Estado de soporte

| Plataforma | Artefacto configurado | Estado |
|---|---|---|
| Windows x64 | NSIS installer + portable | Objetivos configurados; build real, instalación limpia y primer arranque pendientes |
| Linux x64 | AppImage | Build definido; aceptación GUI y offline E2E pendientes |
| macOS | No configurado | No soportado/validado todavía |
| ARM64 | No configurado | No soportado/validado todavía |

## Pruebas antes de distribución

1. Instalar en Windows limpio sin Python, Node.js ni Django.
2. Primer arranque con directorio de datos vacío.
3. Confirmar migraciones y carga de ASCENSO en el directorio correcto.
4. Abrir panel, roadmap, lección, ejercicio y evaluación.
5. Desconectar Internet y repetir los flujos esenciales.
6. Cerrar desde el menú y comprobar que no queden procesos ni puertos.
7. Reiniciar y verificar persistencia de progreso, preferencias e intentos.
8. Probar backup y restauración en un perfil aislado.

No declarar la distribución aceptada hasta completar estas pruebas.