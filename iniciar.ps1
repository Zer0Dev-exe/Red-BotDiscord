# Script de arranque rápido para PowerShell con soporte para .env
$ErrorActionPreference = "Stop"

Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "       Iniciando Red-DiscordBot (.env)             " -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

# 1. Comprobar si existe el archivo .env
if (-not (Test-Path ".\.env")) {
    if (Test-Path ".\.env.example") {
        Copy-Item ".\.env.example" ".\.env"
        Write-Host ""
        Write-Host "=================================================================" -ForegroundColor Yellow
        Write-Host " [AVISO] Se ha creado un archivo .env a partir de .env.example   " -ForegroundColor Yellow
        Write-Host "=================================================================" -ForegroundColor Yellow
        Write-Host " Por favor, abre el archivo .env en tu editor y coloca tu TOKEN: " -ForegroundColor Yellow
        Write-Host "   TOKEN=tu_token_de_discord_aqui                                " -ForegroundColor White
        Write-Host ""
        Write-Host " Luego vuelve a ejecutar iniciar.ps1." -ForegroundColor Yellow
        Write-Host "=================================================================" -ForegroundColor Yellow
        Write-Host ""
        return
    }
}

# 2. Comprobar entornos virtuales existentes
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

# 3. Iniciar RedBot mediante run.py
try {
    python run.py $args
} catch {
    Write-Host "[INFO] El bot se ha detenido: $_" -ForegroundColor Yellow
}
