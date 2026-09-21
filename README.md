<h1 align="center">
  <br>
  <a href="https://github.com/Zer0Dev-exe/Red-BotDiscord"><img src="https://imgur.com/pY1WUFX.png" alt="Red - Discord Bot"></a>
  <br>
  Red Discord Bot
  <br>
</h1>

<h4 align="center">Music, Moderation, Trivia, Stream Alerts and Fully Modular.</h4>

<p align="center">
  <a href="https://discord.gg/red">
    <img src="https://discordapp.com/api/guilds/133049272517001216/widget.png?style=shield" alt="Discord Server">
  </a>
  <a href="https://pypi.org/project/Red-DiscordBot/">
     <img alt="PyPI" src="https://img.shields.io/pypi/v/Red-Discordbot">
  </a>
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Red-Discordbot">
  </a>
  <a href="https://github.com/Rapptz/discord.py/">
     <img src="https://img.shields.io/badge/discord-py-blue.svg" alt="discord.py">
  </a>
  <a href="https://www.patreon.com/Red_Devs">
    <img src="https://img.shields.io/badge/Support-Red!-red.svg" alt="Support Red on Patreon!">
  </a>
</p>
<p align="center">
  <a href="https://github.com/Zer0Dev-exe/Red-BotDiscord/actions">
    <img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="tests">
  </a>
  <a href="https://docs.discord.red/en/stable/?badge=stable">
    <img src="https://readthedocs.org/projects/red-discordbot/badge/?version=stable" alt="Red on readthedocs.org">
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black">
  </a>
  <a href="https://github.com/Zer0Dev-exe/Red-BotDiscord">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
  </a>
  <a href="https://crowdin.com/project/red-discordbot">
    <img src="https://img.shields.io/badge/languages-es%20%7C%20en-brightgreen.svg" alt="Languages">
  </a>
</p>

<p align="center">
  <a href="#overview">Overview</a>
  •
  <a href="#quick-start">Quick Start</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="https://docs.discord.red/en/stable/index.html">Documentation</a>
  •
  <a href="#plugins">Plugins</a>
  •
  <a href="#join-the-community">Community</a>
  •
  <a href="#créditos--licencia">Credits & License</a>
</p>

# Overview

Red is a fully modular bot – meaning all features and commands can be enabled/disabled to your liking, making it completely customizable. This is a *self-hosted bot* – meaning you will need to host and maintain your own instance. You can turn Red into an admin bot, music bot, trivia bot, new best friend or all of these together!  

Red is built for [Discord](https://discord.com/), a popular VOIP and instant messaging platform. It's best suited for use in guilds (also known as servers), where it utilizes Discord's well-documented API to communicate and deliver its many features. Discord offers its API to encourage developers to explore their creativity by building programs, tools, and services that enhance the Discord experience.

[Installation](#installation) is easy, and you do **NOT** need to know anything about coding! Aside from installing and updating, every part of the bot can be controlled from within Discord.

**The default set of modules includes and is not limited to:**

- Moderation features (kick/ban/softban/hackban, mod-log, filter, chat cleanup)
- Trivia (lists are included and can be easily added)
- Music features (YouTube, SoundCloud, local files, playlists, queues)
- Stream alerts (Twitch, Youtube, Picarto)
- Bank (slot machine, user credits)
- Custom commands
- Imgur/gif search
- Admin automation (self-role assignment, cross-server announcements, mod-mail reports)
- Customisable command permissions

**Additionally, other [plugins](#plugins) (cogs) can be easily found and added from our growing community of cog repositories.**

# Quick Start

To clone and run this bot in seconds:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Zer0Dev-exe/Red-BotDiscord.git
   cd Red-BotDiscord
   ```

2. **Start the bot:**
   - On Windows: Double-click **`iniciar.bat`** (or run `.\iniciar.ps1` in PowerShell).
   - The script automatically configures the Python 3.11 virtual environment, installs requirements and turns on your bot.

# Installation

**The following platforms are officially supported:** 

- [Windows](https://docs.discord.red/en/stable/install_guides/windows.html)
- [MacOS](https://docs.discord.red/en/stable/install_guides/mac.html)
- [Most major linux distributions](https://docs.discord.red/en/stable/install_guides/index.html)

If after reading the guide you are still experiencing issues, feel free to join the
[Official Discord Server](https://discord.gg/red) and ask in the **#support** channel for help.

# Plugins

Red is fully modular, allowing you to load and unload plugins of your choice, and install 3rd party plugins directly from Discord! A few examples are:

- Cleverbot integration (talk to Red and she talks back)
- Ban sync
- Welcome messages
- Casino
- Reaction roles
- Slow Mode
- AniList
- And much, much more!

Feel free to take a [peek](https://index.discord.red) at a list of available 3rd party cogs!

# Join the community!

**Red** is in continuous development, and it’s supported by an active community which produces new content (cogs/plugins) for everyone to enjoy. New features are constantly added. If you can’t [find](https://index.discord.red) the cog you’re looking for, consult our [guide](https://docs.discord.red/en/stable/guide_cog_creation.html) on building your own cogs!

Join us on our [Official Discord Server](https://discord.gg/red)!

# Créditos & Licencia

Este proyecto está basado en el software de código abierto **[Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot)**, originalmente desarrollado y mantenido por el equipo de **Cog-Creators** y Twentysix26.

### 🛠️ Versión Optimizada por Zer0Dev-exe
Esta adaptación fue preparada por **[Zer0Dev-exe](https://github.com/Zer0Dev-exe)** para ofrecer una versión optimizada, ligera y enfocada en un clonado y despliegue rápido:
* **Limpieza de idiomas:** Se eliminaron más de 1.200 archivos de idiomas no requeridos, conservando de forma nativa únicamente el soporte en **Español** (`es-ES`) e **Inglés** (`en-US`).
* **Estructura ligera:** Se retiraron las suites pesadas de tests, linters, archivos de integración continua (CI) y documentación web para acelerar drásticamente el tiempo de clonado y reducir el tamaño del repositorio.
* **Arranque en 1 clic:** Se agregaron scripts automatizados para Windows (`iniciar.bat` e `iniciar.ps1`) que configuran el entorno virtual con Python 3.11, instalan dependencias y encienden el bot automáticamente.
* **Seguridad:** Configuración de `.gitignore` y `.env.example` para prevenir la exposición accidental de tokens de Discord o claves privadas.

---

### 📜 Reconocimientos & Licencia
* **Licencia:** Distribuido bajo los términos de la licencia [GNU General Public License v3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html).
* **Personaje e Inspiración:** Red toma su nombre de la protagonista de *Transistor*, un videojuego de [Supergiant Games](https://www.supergiantgames.com/games/transistor/).
* **Ilustración:** Arte de portada creado por [Sinlaire](https://sinlaire.deviantart.com/) en DeviantArt para el proyecto Red-DiscordBot.
* **Paquete de terceros:** Incluye el paquete `discord.ext.menus` creado por Danny Y. (Rapptz) bajo licencia MIT ([ver licencia](redbot/vendored/discord-ext-menus.LICENSE)).

