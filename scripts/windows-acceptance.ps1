# CodeGuard Pro — aceptación automatizada en Windows
#
# Ejecuta sobre los artefactos generados por `npm run build:win`:
#  1. instalación silenciosa del NSIS;
#  2. arranque, health check y rutas principales;
#  3. tema persistido tras reiniciar;
#  4. progreso local persistido tras reiniciar;
#  5. cierre sin procesos huérfanos;
#  6. desinstalación;
#  7. arranque y cierre del ejecutable portable.
#
# Requiere un runner Windows con escritorio (GitHub windows-latest), Python,
# Node.js y los artefactos en dist/. No sustituye una prueba manual en hardware
# real, pero valida el ciclo instalable completo.

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

function Assert-True([bool]$Condition, [string]$Message) {
    if (-not $Condition) { throw $Message }
}

function Wait-ForPage([int]$Port, [int]$TimeoutSeconds = 180) {
    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
    while ((Get-Date) -lt $deadline) {
        try {
            $pages = @(Invoke-RestMethod -Uri "http://127.0.0.1:$Port/json" -TimeoutSec 2)
            $page = $pages | Where-Object { $_.url -like 'http://127.0.0.1:*' } | Select-Object -First 1
            if ($page) {
                return $page
            }
        } catch {
            # Electron todavía está extrayendo o Django aún no cargó.
        }
        Start-Sleep -Seconds 1
    }
    throw "CDP no quedó disponible en el puerto $Port."
}

function Wait-ForHealth([int]$TimeoutSeconds = 240) {
    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
    while ((Get-Date) -lt $deadline) {
        $servers = @(Get-Process -Name 'CodeGuardServer' -ErrorAction SilentlyContinue)
        foreach ($server in $servers) {
            $connections = @(
                Get-NetTCPConnection -State Listen -OwningProcess $server.Id -ErrorAction SilentlyContinue |
                    Where-Object { $_.LocalAddress -eq '127.0.0.1' }
            )
            foreach ($connection in $connections) {
                try {
                    $health = Invoke-RestMethod -Uri "http://127.0.0.1:$($connection.LocalPort)/healthz/" -TimeoutSec 3
                    if (
                        $health.status -eq 'ok' -and
                        $health.database -eq 'ok' -and
                        $health.migrations -eq 'ok' -and
                        $health.roadmap -eq 'ok'
                    ) {
                        return $health
                    }
                } catch {
                    # Servidor arrancando.
                }
            }
        }
        Start-Sleep -Seconds 2
    }
    throw 'El servidor Django no alcanzó /healthz/ con estado ok.'
}

function Start-App([string]$Executable, [string]$DataDir, [int]$Port, [string]$LogPrefix, [string]$WorkingDirectory) {
    New-Item -ItemType Directory -Force -Path $DataDir | Out-Null
    $env:CODEGUARD_DATA_DIR = $DataDir
    $stdout = Join-Path $env:TEMP "$LogPrefix-out.log"
    $stderr = Join-Path $env:TEMP "$LogPrefix-err.log"
    $process = Start-Process -FilePath $Executable `
        -ArgumentList "--remote-debugging-port=$Port" `
        -WorkingDirectory $WorkingDirectory `
        -RedirectStandardOutput $stdout `
        -RedirectStandardError $stderr `
        -PassThru
    return $process
}

function Run-CdpSmoke([object]$Page, [string]$Mode, [string]$Theme = '') {
    $arguments = @('scripts/cdp-smoke.js', $Page.webSocketDebuggerUrl, $Mode)
    if ($Theme) { $arguments += $Theme }
    & node @arguments
    if ($LASTEXITCODE -ne 0) {
        throw "El smoke test CDP falló en modo $Mode."
    }
}

function Wait-AppClosed([int]$ProcessId, [string]$Context) {
    Wait-Process -Id $ProcessId -Timeout 60 -ErrorAction SilentlyContinue
    $deadline = (Get-Date).AddSeconds(45)
    while ((Get-Date) -lt $deadline) {
        $left = @(Get-Process -Name 'CodeGuardServer', 'CodeGuard Pro' -ErrorAction SilentlyContinue)
        if ($left.Count -eq 0) { return }
        Start-Sleep -Seconds 1
    }
    throw "Quedaron procesos de CodeGuard tras cerrar $Context."
}

function Assert-Preference([string]$DataDir, [string]$Expected) {
    $file = Join-Path $DataDir 'ui-preferences.json'
    Assert-True (Test-Path $file) 'No se creó ui-preferences.json.'
    $preference = Get-Content $file -Raw | ConvertFrom-Json
    Assert-True ($preference.theme -eq $Expected) "Tema persistido inesperado: $($preference.theme)"
}

$installer = Get-ChildItem -Path 'dist' -Filter '*Setup*.exe' | Select-Object -First 1
$portable = Get-ChildItem -Path 'dist' -Filter '*.exe' |
    Where-Object { $_.Name -notmatch 'Setup|Uninstall' } |
    Select-Object -First 1
Assert-True ($null -ne $installer) 'No se encontró el instalador NSIS.'
Assert-True ($null -ne $portable) 'No se encontró el ejecutable portable.'

Write-Host "[1/7] Instalación silenciosa: $($installer.Name)"
Start-Process -FilePath $installer.FullName -ArgumentList '/S' -Wait

$installedExe = Join-Path $env:LOCALAPPDATA 'Programs\CodeGuard Pro\CodeGuard Pro.exe'
$installDir = Split-Path -Parent $installedExe
if (-not (Test-Path $installedExe)) {
    $programs = Join-Path $env:LOCALAPPDATA 'Programs'
    $candidate = Get-ChildItem -Path $programs -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -like '*CodeGuard*' } |
        Select-Object -First 1
    Assert-True ($null -ne $candidate) 'El instalador no creó la carpeta de CodeGuard Pro.'
    $installDir = $candidate.FullName
    $installedExe = Join-Path $installDir 'CodeGuard Pro.exe'
}
Assert-True (Test-Path $installedExe) 'No se encontró el ejecutable instalado.'

$data1 = Join-Path $env:RUNNER_TEMP 'codeguard-win-data'
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue $data1

Write-Host '[2/7] Primer arranque, health check y rutas principales'
$app1 = Start-App -Executable $installedExe -DataDir $data1 -Port 9230 -LogPrefix 'cg-win-first' -WorkingDirectory $installDir
$page1 = Wait-ForPage -Port 9230
$health1 = Wait-ForHealth
Assert-True ($health1.status -eq 'ok') 'Health check inicial falló.'
Run-CdpSmoke -Page $page1 -Mode 'set' -Theme 'fantasy'
Wait-AppClosed -ProcessId $app1.Id -Context 'el primer arranque'
Assert-Preference -DataDir $data1 -Expected 'fantasy'

Write-Host '[3/7] Progreso local y reinicio'
$env:CODEGUARD_DATA_DIR = $data1
$env:DJANGO_SETTINGS_MODULE = 'config.settings.development'
& python scripts/windows-profile-check.py
if ($LASTEXITCODE -ne 0) { throw 'No se pudo sembrar el progreso local.' }

$app2 = Start-App -Executable $installedExe -DataDir $data1 -Port 9231 -LogPrefix 'cg-win-second' -WorkingDirectory $installDir
$page2 = Wait-ForPage -Port 9231
Wait-ForHealth | Out-Null
Run-CdpSmoke -Page $page2 -Mode 'expect' -Theme 'fantasy'
Wait-AppClosed -ProcessId $app2.Id -Context 'el segundo arranque'
& python scripts/windows-profile-check.py --verify
if ($LASTEXITCODE -ne 0) { throw 'El progreso no persistió tras reiniciar.' }

Write-Host '[4/7] Desinstalación silenciosa'
$uninstaller = Get-ChildItem -Path $installDir -Filter '*ninstall*.exe' | Select-Object -First 1
Assert-True ($null -ne $uninstaller) 'No se encontró el desinstalador NSIS.'
Start-Process -FilePath $uninstaller.FullName -ArgumentList '/S' -Wait
$deadline = (Get-Date).AddSeconds(60)
while ((Test-Path $installedExe) -and (Get-Date) -lt $deadline) {
    Start-Sleep -Seconds 2
}
Assert-True (-not (Test-Path $installedExe)) 'El desinstalador no eliminó el ejecutable instalado.'

Write-Host '[5/7] Ejecutable portable: arranque y health check'
$data2 = Join-Path $env:RUNNER_TEMP 'codeguard-win-portable'
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue $data2
$appPortable = Start-App -Executable $portable.FullName -DataDir $data2 -Port 9232 -LogPrefix 'cg-win-portable' -WorkingDirectory $root
$pagePortable = Wait-ForPage -Port 9232 -TimeoutSeconds 240
Wait-ForHealth | Out-Null
Run-CdpSmoke -Page $pagePortable -Mode 'basic'
Wait-AppClosed -ProcessId $appPortable.Id -Context 'el portable'

Write-Host '[6/7] Comprobación de procesos huérfanos'
$left = @(Get-Process -Name 'CodeGuardServer', 'CodeGuard Pro' -ErrorAction SilentlyContinue)
Assert-True ($left.Count -eq 0) "Procesos huérfanos: $($left | ForEach-Object { $_.ProcessName } | Out-String)"

Write-Host '[7/7] Aceptación Windows completada'
