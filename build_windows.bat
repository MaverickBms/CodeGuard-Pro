@echo off
REM ============================================================================
REM Script de construcción para Windows - CodeGuard Pro
REM Genera el ejecutable .exe usando PyInstaller
REM ============================================================================

echo [CodeGuard Pro] Iniciando construccion para Windows...

REM Verificar que Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado o no esta en el PATH.
    echo Instale Python desde https://www.python.org y vuelva a intentar.
    pause
    exit /b 1
)

REM Verificar que pip esta instalado
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip no esta instalado.
    pause
    exit /b 1
)

REM Instalar dependencias
echo [CodeGuard Pro] Instalando dependencias...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Fallo al instalar dependencias.
    pause
    exit /b 1
)

REM Instalar PyInstaller si no esta presente
python -m pip install pyinstaller pyinstaller-hooks-contrib >nul 2>&1

REM Aplicar migraciones de Django
echo [CodeGuard Pro] Aplicando migraciones de Django...
python manage.py migrate
if errorlevel 1 (
    echo [ERROR] Fallo al aplicar migraciones.
    pause
    exit /b 1
)

REM Construir ejecutable con PyInstaller
echo [CodeGuard Pro] Construyendo ejecutable .exe...
python -m PyInstaller --noconfirm --clean CodeGuard.spec
if errorlevel 1 (
    echo [ERROR] Fallo al construir el ejecutable.
    pause
    exit /b 1
)

echo.
echo [CodeGuard Pro] Construccion completada exitosamente.
echo El ejecutable se encuentra en: dist\Code Guard Pro.exe
echo.
pause
