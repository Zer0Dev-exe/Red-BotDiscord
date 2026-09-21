@echo off
chcp 65001 > nul
title Red-DiscordBot

echo ===================================================
echo           Iniciando Red-DiscordBot (.env)
echo ===================================================

REM 1. Comprobar si ya existe el entorno virtual global o local
if exist "%USERPROFILE%\redenv\Scripts\activate.bat" (
    echo [INFO] Activando entorno virtual en %%USERPROFILE%%\redenv...
    call "%USERPROFILE%\redenv\Scripts\activate.bat"
    goto RUN
)

if exist ".venv\Scripts\activate.bat" (
    echo [INFO] Activando entorno virtual local .venv...
    call ".venv\Scripts\activate.bat"
    goto RUN
)

REM 2. Si no existe ningun venv, crearlo automaticamente con Python 3.11
echo [INFO] No se encontro entorno virtual. Creando uno nuevo con Python 3.11...
py -3.11 -m venv .venv
if %errorlevel% neq 0 (
    echo [ERROR] No se pudo encontrar Python 3.11 en el sistema.
    echo Por favor instala Python 3.11: winget install Python.Python.3.11
    pause
    exit /b 1
)

echo [INFO] Activando nuevo entorno virtual...
call ".venv\Scripts\activate.bat"

echo [INFO] Instalando dependencias necesarias...
python -m pip install -U pip wheel
pip install -r requirements.txt

REM 3. Ejecutar RedBot mediante run.py
:RUN
python run.py %*
if %errorlevel% neq 0 (
    echo.
    echo [INFO] El bot se ha detenido con codigo de salida %errorlevel%.
    pause
)
