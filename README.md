<h1 align="center">
  <br>
  <a href="https://github.com/Zer0Dev-exe/Red-BotDiscord"><img src="https://imgur.com/pY1WUFX.png" alt="Red - Discord Bot"></a>
  <br>
  Red Discord Bot
  <br>
</h1>

<h4 align="center">Música, Moderación, Trivia, Economía y Totalmente Modular</h4>

<p align="center">
  <img alt="Python 3.11" src="https://img.shields.io/badge/python-3.11-blue.svg">
  <img alt="discord.py" src="https://img.shields.io/badge/discord-py-blue.svg">
  <img alt="Idiomas" src="https://img.shields.io/badge/idiomas-español%20%7C%20inglés-brightgreen.svg">
  <img alt="Licencia" src="https://img.shields.io/badge/licencia-GPL--3.0-orange.svg">
</p>

<p align="center">
  <a href="#descripción">Descripción</a>
  •
  <a href="#inicio-rápido">Inicio Rápido</a>
  •
  <a href="#módulos-incluidos">Módulos</a>
  •
  <a href="#cogs-y-plugins">Plugins</a>
  •
  <a href="#créditos-y-reconocimientos">Créditos</a>
</p>

---

## Descripción

**Red** es un bot de Discord totalmente modular y personalizable. Puedes activar y desactivar los módulos que quieras según las necesidades de tu servidor: conviértelo en un bot de música, un potente moderador, un centro de juegos y trivia, o todo a la vez.

Esta es una versión **auto-alojada (self-hosted)**: se ejecuta en tu propio equipo o servidor con control total sobre tus datos y configuraciones.

## ⚡ Inicio Rápido (Control Total con `.env`)

Para clonar y poner a funcionar este bot fácilmente:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Zer0Dev-exe/Red-BotDiscord.git
   cd Red-BotDiscord
   ```

2. **Configurar el archivo `.env`:**
   * Al ejecutar el bot por primera vez, se creará automáticamente el archivo `.env` a partir de `.env.example`.
   * Abre el archivo `.env` y pega el token de tu bot obtenido desde el [Discord Developer Portal](https://discord.com/developers/applications):
     ```env
     TOKEN=tu_token_de_discord_aqui
     PREFIX=!
     ```
   * *Opcional:* Puedes configurar en `.env` tu `OWNER_ID`, la carpeta de datos (`DATA_PATH`), el tipo de almacenamiento (`STORAGE_TYPE`), etc.

3. **Encender el bot:**
   * En Windows: Haz doble clic en **`iniciar.bat`** (o ejecuta `.\iniciar.ps1` en PowerShell).
   * O desde cualquier terminal con Python: `python run.py`
   * El script activará el entorno virtual, instalará dependencias, aprovisionará la instancia automáticamente y arrancará el bot de inmediato.

> **¡Sin `redbot-setup`!** Todo se administra desde el archivo `.env`, ofreciendo máxima comodidad, portabilidad y control.


## 📦 Módulos Incluidos

El bot incluye una selección de funciones esenciales listas para usar:

* 🛡️ **Moderación:** Expulsiones, baneos, silencios (`mutes`), registro de auditoría (`mod-log`), filtros de chat y limpieza masiva de mensajes (`cleanup`).
* 🎵 **Música (Audio):** Reproducción de pistas desde YouTube, SoundCloud, listas de reproducción locales y colas de reproducción.
* 🎯 **Trivia:** Sistema interactivo de preguntas y respuestas con listas temáticas incluidas y opción de crear las tuyas.
* 💰 **Economía & Banco:** Sistema de créditos, máquinas tragaperras, pagos periódicos (`payday`) y tablas de clasificación.
* ⚙️ **Comandos Personalizados:** Configura respuestas automáticas y comandos propios directamente desde Discord.
* 🔔 **Alertas de Streams:** Avisos automáticos cuando tus canales favoritos de Twitch o YouTube inicien directo.
* 🔐 **Permisos Granulares:** Control detallado de qué usuarios o roles pueden utilizar cada comando.

## 🧩 Cogs y Plugins Adicionales

Red permite instalar cientos de módulos creados por la comunidad directamente desde el chat de Discord:
```text
!load downloader
!repo add <nombre_repo> <url_del_repo>
!cog install <nombre_repo> <nombre_cog>
!load <nombre_cog>
```
Puedes buscar cogs verificados por la comunidad en [CogBoard](https://cogboard.red/).

---

## 📜 Créditos y Reconocimientos

* **Proyecto Original:** Creado y mantenido por el equipo de **[Cog-Creators](https://github.com/Cog-Creators/Red-DiscordBot)** y Twentysix26.
* **Edición Limpia y Optimizada:** Esta versión ha sido adaptada por **[Zer0Dev-exe](https://github.com/Zer0Dev-exe)** para ofrecer una base ligera, sin archivos de desarrollo o linters innecesarios, con soporte nativo únicamente en **Español** e **Inglés**, y con scripts de inicio automático en Windows (`iniciar.bat` / `iniciar.ps1`).
* **Licencia:** Distribuido bajo licencia [GNU General Public License v3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html).
* **Arte e Ilustración:** Personaje inspirado en Red del juego *Transistor* ([Supergiant Games](https://www.supergiantgames.com/games/transistor/)), con portada ilustrada por [Sinlaire](https://sinlaire.deviantart.com/).
