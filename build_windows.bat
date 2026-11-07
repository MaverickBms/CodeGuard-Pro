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

echo [INFO] Aplicando migraciones...
python manage.py migrate --settings=config.settings.development
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Fallo la migracion de la base de datos.
    pause
    exit /b 1
)

echo [INFO] Cargando roadmap ASCENSO 3.1...
python manage.py cargar_ascenso --settings=config.settings.development
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Fallo la carga del roadmap.
    pause
    exit /b 1
)

echo [INFO] Generando servidor Django con PyInstaller...
pyinstaller --clean --noconfirm --distpath dist-server --workpath build\pyinstaller-server CodeGuardServer.spec
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] PyInstaller fallo al generar el servidor.
    pause
    exit /b 1
)

if not exist "dist-server\CodeGuardServer\CodeGuardServer.exe" (
    echo [ERROR] No se genero dist-server\CodeGuardServer\CodeGuardServer.exe
    pause
    exit /b 1
)
echo [OK] Servidor generado: dist-server\CodeGuardServer\CodeGuardServer.exe

echo [INFO] Instalando dependencias Node.js...
if not exist "node_modules" (
    call npm install
    if !ERRORLEVEL! NEQ 0 (
        echo [ERROR] Fallo npm install.
        pause
        exit /b 1
    )
)

echo [INFO] Empaquetando Electron para Windows...
call npm run build:win
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] electron-builder fallo al generar el paquete Windows.
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
