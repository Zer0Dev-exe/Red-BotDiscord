# Script de arranque rápido para PowerShell
$ErrorActionPreference = "Stop"

Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "           Iniciando Red-DiscordBot                " -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

# 1. Comprobar entornos virtuales existentes
$VenvGlobal = "$HOME\redenv\Scripts\Activate.ps1"
$VenvLocal = ".\.venv\Scripts\Activate.ps1"

if (Test-Path $VenvGlobal) {
    Write-Host "[INFO] Activando entorno global $HOME\redenv..." -ForegroundColor Green
    & $VenvGlobal
} elseif (Test-Path $VenvLocal) {
    Write-Host "[INFO] Activando entorno local .\.venv..." -ForegroundColor Green
    & $VenvLocal
} else {
    Write-Host "[INFO] Creando entorno virtual local .venv con Python 3.11..." -ForegroundColor Yellow
    py -3.11 -m venv .venv
    & $VenvLocal
    Write-Host "[INFO] Instalando dependencias..." -ForegroundColor Green
    python -m pip install -U pip wheel
    pip install -r requirements.txt
}

# 2. Iniciar RedBot
Write-Host "[INFO] Encendiendo RedBot..." -ForegroundColor Cyan
try {
    redbot RedBot
} catch {
    Write-Host "[AVISO] Si es la primera vez que configuras la instancia, ejecuta 'redbot-setup'." -ForegroundColor Yellow
}
