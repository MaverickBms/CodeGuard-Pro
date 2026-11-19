@echo off
setlocal EnableExtensions EnableDelayedExpansion

REM ==========================================================================
REM  CodeGuard Pro - Construccion del paquete Windows (.exe)
REM
REM  Requisitos:
REM    - Windows 10/11 de 64 bits
REM    - Python 3.12+ en PATH (o el lanzador "py")
REM    - Node.js 20+ y npm en PATH
REM
REM  Resultado:
REM    dist-server\CodeGuardServer\CodeGuardServer.exe  (servidor Django)
REM    dist\CodeGuard-Pro-1.0.0-x64.exe                 (instalador NSIS)
REM    dist\CodeGuard-Pro-1.0.0-portable.exe            (portable)
REM
REM  NOTA: electron-builder no puede compilar para Windows desde Fedora.
REM        Este script debe ejecutarse en Windows.
REM ==========================================================================

cd /d "%~dp0"

echo =============================================
echo    CodeGuard Pro - Build Windows
echo =============================================

REM --- Verificar Python ---
where py >nul 2>nul
if %ERRORLEVEL%==0 (
    set "PY_CMD=py -3"
) else (
    where python >nul 2>nul
    if !ERRORLEVEL! NEQ 0 (
        echo [ERROR] Python no esta instalado o no esta en PATH.
        pause
        exit /b 1
    )
    set "PY_CMD=python"
)

REM --- Verificar version minima de Python ---
%PY_CMD% -c "import sys; raise SystemExit(0 if sys.version_info >= (3,12) else 1)"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Se requiere Python 3.12 o superior para compilar CodeGuard Pro.
    pause
    exit /b 1
)

REM --- Verificar Node.js ---
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Node.js no esta instalado o no esta en PATH.
    pause
    exit /b 1
)
where npm >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] npm no esta instalado o no esta en PATH.
    pause
    exit /b 1
)

REM --- Crear y activar entorno virtual ---
if not exist ".venv\Scripts\python.exe" (
    echo [INFO] Creando entorno virtual .venv...
    %PY_CMD% -m venv .venv
    if !ERRORLEVEL! NEQ 0 (
        echo [ERROR] No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

call ".venv\Scripts\activate.bat"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] No se pudo activar el entorno virtual.
    pause
    exit /b 1
)

echo [INFO] Actualizando pip...
python -m pip install --upgrade pip

echo [INFO] Instalando dependencias Python...
python -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Fallo la instalacion de dependencias Python.
    pause
    exit /b 1
)

REM La base de datos y ASCENSO se inicializan en el primer arranque del usuario.
REM build:win genera el servidor con PyInstaller, verifica su hash y solo entonces
REM permite que electron-builder empaquete el ejecutable recien generado.

echo [INFO] Instalando dependencias Node.js desde package-lock.json...
call npm ci
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Fallo npm ci. Revisa package-lock.json y la conexion a npm.
    pause
    exit /b 1
)

echo [INFO] Generando servidor y empaquetando Electron para Windows...
call npm run build:win
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Fallo la generacion/verificacion del servidor o electron-builder.
    pause
    exit /b 1
)

echo.
echo =============================================
echo    Build completado
echo =============================================
echo Instalador NSIS y portable en la carpeta dist\:
dir /b dist\*.exe 2>nul
echo.
echo Servidor local incluido en resources\server por electron-builder.
pause
endlocal
