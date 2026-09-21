#!/usr/bin/env python3
"""
Lanzador y Gestor de Configuración para Red-DiscordBot basado en .env.

Permite arrancar Red-DiscordBot cargando toda la configuración desde el archivo .env,
evitando la necesidad de ejecutar `redbot-setup` o contestar preguntas en la consola.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, Any, List

ROOT_DIR = Path(__file__).parent.resolve()
ENV_FILE = ROOT_DIR / ".env"
ENV_EXAMPLE = ROOT_DIR / ".env.example"


def parse_env_fallback(filepath: Path) -> Dict[str, str]:
    """Parser de respaldo para leer archivos .env sin dependencias externas."""
    env_vars: Dict[str, str] = {}
    if not filepath.exists():
        return env_vars

    with filepath.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip("'\"")
                env_vars[k] = v
    return env_vars


def load_environment() -> Dict[str, str]:
    """Carga variables desde .env usando python-dotenv si está disponible."""
    # 1. Si no existe .env, crearlo a partir de .env.example
    if not ENV_FILE.exists():
        if ENV_EXAMPLE.exists():
            shutil.copyfile(ENV_EXAMPLE, ENV_FILE)
            print("=" * 65)
            print(" [AVISO] Se ha creado un archivo .env a partir de .env.example")
            print("=" * 65)
            print(" Por favor, abre el archivo .env y configura tu TOKEN de Discord:")
            print("   TOKEN=tu_token_de_discord_aqui\n")
            print(" Una vez configurado, vuelve a ejecutar este script.")
            sys.exit(1)
        else:
            print("[ERROR] No se encontró el archivo .env ni .env.example.")
            sys.exit(1)

    # 2. Intentar cargar con python-dotenv si está disponible
    try:
        from dotenv import dotenv_values
        env = dotenv_values(ENV_FILE)
    except ImportError:
        env = parse_env_fallback(ENV_FILE)

    # Actualizar os.environ para que cualquier librería interna también lo vea
    for key, val in env.items():
        if val is not None and key not in os.environ:
            os.environ[key] = str(val)

    return {k: v for k, v in env.items() if v is not None}


def get_platform_dirs():
    """Obtiene directorios de configuración de RedBot para la plataforma actual."""
    try:
        import platformdirs
        appdir = platformdirs.PlatformDirs("Red-DiscordBot")
        config_dir = appdir.user_config_path
        user_data_dir = Path(appdir.user_data_dir)
    except Exception:
        # Fallback estándar si platformdirs fallase
        if sys.platform == "win32":
            base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
        else:
            base = Path.home() / ".config"
        config_dir = base / "Red-DiscordBot"
        user_data_dir = base / "Red-DiscordBot"

    return config_dir, user_data_dir


def auto_provision_instance(env: Dict[str, str]) -> Dict[str, Any]:
    """
    Aprovisiona automáticamente la instancia en config.json de RedBot.
    Reemplaza totalmente la necesidad de `redbot-setup`.
    """
    instance_name = env.get("INSTANCE_NAME", "").strip() or "RedBot"
    data_path_raw = env.get("DATA_PATH", "").strip()
    storage_type = env.get("STORAGE_TYPE", "JSON").strip().upper()

    config_dir, user_data_dir = get_platform_dirs()
    config_dir.mkdir(parents=True, exist_ok=True)
    config_file = config_dir / "config.json"

    # Determinar ruta de almacenamiento de datos
    if data_path_raw:
        resolved_data_path = (ROOT_DIR / data_path_raw).resolve()
    else:
        # Si se deja vacío, usar la ruta estándar del sistema en AppData
        resolved_data_path = (user_data_dir / "data" / instance_name).resolve()

    resolved_data_path.mkdir(parents=True, exist_ok=True)

    # Detalles de almacenamiento según el backend
    storage_details: Dict[str, Any] = {}
    if storage_type == "POSTGRES":
        storage_details = {
            "host": env.get("POSTGRES_HOST", "localhost").strip(),
            "port": int(env.get("POSTGRES_PORT", "5432").strip() or 5432),
            "user": env.get("POSTGRES_USER", "postgres").strip(),
            "password": env.get("POSTGRES_PASSWORD", "").strip(),
            "database": env.get("POSTGRES_DB", "redbot").strip(),
        }

    # Leer o inicializar config.json de RedBot
    existing_config: Dict[str, Any] = {}
    if config_file.exists():
        try:
            with config_file.open(encoding="utf-8") as f:
                existing_config = json.load(f)
        except Exception:
            existing_config = {}

    instance_entry = {
        "DATA_PATH": str(resolved_data_path),
        "COG_PATH_APPEND": "cogs",
        "CORE_PATH_APPEND": "core",
        "STORAGE_TYPE": storage_type,
        "STORAGE_DETAILS": storage_details,
    }

    # Guardar si cambió o no existe
    if existing_config.get(instance_name) != instance_entry:
        existing_config[instance_name] = instance_entry
        with config_file.open("w", encoding="utf-8") as f:
            json.dump(existing_config, f, indent=4)
        print(f"[INFO] Instancia '{instance_name}' aprovisionada automáticamente en {config_file}")

    return {
        "instance_name": instance_name,
        "data_path": resolved_data_path,
        "storage_type": storage_type,
    }


def sync_json_settings(data_path: Path, token: str, prefixes: List[str], owner_id: str | None):
    """
    Sincroniza token, prefijos y owner en settings.json si se usa almacenamiento JSON.
    Garantiza que la base de datos interna de Red esté sincronizada con el .env.
    """
    core_dir = data_path / "core"
    core_dir.mkdir(parents=True, exist_ok=True)
    settings_file = core_dir / "settings.json"

    settings_data: Dict[str, Any] = {}
    if settings_file.exists():
        try:
            with settings_file.open(encoding="utf-8") as f:
                settings_data = json.load(f)
        except Exception:
            settings_data = {}

    global_data = settings_data.setdefault("0", {}).setdefault("GLOBAL", {})

    modified = False
    if global_data.get("token") != token:
        global_data["token"] = token
        modified = True

    if prefixes and global_data.get("prefix") != prefixes:
        global_data["prefix"] = prefixes
        modified = True

    if owner_id:
        try:
            numeric_owner = int(owner_id)
            if global_data.get("owner") != numeric_owner:
                global_data["owner"] = numeric_owner
                modified = True
        except ValueError:
            pass

    if modified:
        with settings_file.open("w", encoding="utf-8") as f:
            json.dump(settings_data, f, indent=4)


def build_cli_args(env: Dict[str, str], instance_name: str) -> List[str]:
    """Construye los argumentos de línea de comandos para redbot a partir de .env."""
    token = env.get("TOKEN") or env.get("DISCORD_TOKEN") or env.get("RED_TOKEN") or ""
    prefix_str = env.get("PREFIX", "!").strip()
    owner_id = env.get("OWNER_ID", "").strip()
    co_owners = env.get("CO_OWNERS", "").strip()
    dev_mode = env.get("DEV_MODE", "false").lower() in ("true", "1", "yes")
    team_members = env.get("TEAM_MEMBERS_ARE_OWNERS", "false").lower() in ("true", "1", "yes")
    log_level = env.get("LOG_LEVEL", "0").strip()

    args = [instance_name]

    if token:
        args.extend(["--token", token])

    # Soportar múltiples prefijos separados por espacios o comas
    if prefix_str:
        prefixes = [p.strip() for p in prefix_str.replace(",", " ").split() if p.strip()]
        for p in prefixes:
            args.extend(["--prefix", p])

    if owner_id:
        args.extend(["--owner", owner_id])

    if co_owners:
        for co in [c.strip() for c in co_owners.replace(",", " ").split() if c.strip()]:
            args.extend(["--co-owner", co])

    if team_members:
        args.append("--team-members-are-owners")

    if dev_mode:
        args.append("--dev")

    try:
        level = int(log_level)
        if level == 1:
            args.append("-v")
        elif level >= 2:
            args.append("-vv")
    except ValueError:
        pass

    # Evitar cualquier pregunta interactiva
    args.append("--no-prompt")

    return args


def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    # 1. Cargar .env
    env = load_environment()

    token = (env.get("TOKEN") or env.get("DISCORD_TOKEN") or env.get("RED_TOKEN") or "").strip()
    if not token or token == "tu_token_de_discord_aqui":
        print("\n" + "=" * 65, flush=True)
        print(" [ERROR] El TOKEN de Discord no está configurado.", flush=True)
        print("=" * 65, flush=True)
        print(" Por favor abre el archivo .env y asigna tu token en:", flush=True)
        print("   TOKEN=tu_token_aqui\n", flush=True)
        print(" Si aún no tienes un bot, créalo en:", flush=True)
        print("   https://discord.com/developers/applications", flush=True)
        print("=" * 65 + "\n", flush=True)
        sys.exit(1)

    # 2. Aprovisionar instancia en config.json
    inst_info = auto_provision_instance(env)
    instance_name = inst_info["instance_name"]
    data_path = inst_info["data_path"]
    storage_type = inst_info["storage_type"]

    # 3. Sincronizar configuraciones si es almacenamiento JSON
    if storage_type == "JSON":
        prefix_str = env.get("PREFIX", "!").strip()
        prefixes = [p.strip() for p in prefix_str.replace(",", " ").split() if p.strip()] or ["!"]
        owner_id = env.get("OWNER_ID", "").strip() or None
        sync_json_settings(data_path, token, prefixes, owner_id)

    # 4. Construir argumentos para RedBot
    bot_args = build_cli_args(env, instance_name)

    # Agregar argumentos adicionales pasados al ejecutar run.py
    extra_args = sys.argv[1:]
    for arg in extra_args:
        if arg not in bot_args:
            bot_args.append(arg)

    print("=" * 65, flush=True)
    print("           Iniciando Red-DiscordBot desde .env", flush=True)
    print("=" * 65, flush=True)
    print(f" Instancia   : {instance_name}", flush=True)
    print(f" Ruta Datos  : {data_path}", flush=True)
    print(f" Backend     : {storage_type}", flush=True)
    print(f" Prefijo(s)  : {env.get('PREFIX', '!')}", flush=True)
    if env.get("OWNER_ID"):
        print(f" Propietario : {env.get('OWNER_ID')}", flush=True)
    print("=" * 65 + "\n", flush=True)

    # 5. Ejecutar RedBot en un bucle que soporte reinicios ([p]restart)
    # Exit code 26 indica solicitud de reinicio por parte de RedBot
    RESTART_CODE = 26

    while True:
        cmd = [sys.executable, "-m", "redbot"] + bot_args
        process = subprocess.run(cmd, env=os.environ.copy())
        if process.returncode == RESTART_CODE:
            print("\n[INFO] Reiniciando RedBot...")
            continue
        sys.exit(process.returncode)


if __name__ == "__main__":
    main()
