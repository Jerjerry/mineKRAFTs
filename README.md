# Minecraft AI Builder with ComputerCraft

This project uses Ollama and ComputerCraft to generate and build structures in Minecraft based on your descriptions.

## Required Downloads

1. **Minecraft Java Edition**
   - Recommended version: 1.20.1 (most stable with mods)
   - [Purchase and download from Minecraft.net](https://www.minecraft.net/en-us/store/minecraft-java-edition)

2. **Forge Installer**
   - Download Forge 1.20.1 from: [files.minecraftforge.net](https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.1.html)
   - Choose "Installer" not "Source" or "MDK"

3. **ComputerCraft Mod**
   - Download "CC: Tweaked" for Minecraft 1.20.1 from: [curseforge.com/minecraft/mc-mods/cc-tweaked](https://www.curseforge.com/minecraft/mc-mods/cc-tweaked/files)
   - Make sure to download the Forge version

4. **Python**
   - Download Python 3.9 or newer: [python.org/downloads](https://www.python.org/downloads/)
   - During installation, CHECK "Add Python to PATH"

5. **Ollama**
   - Download from: [ollama.ai/download](https://ollama.ai/download)

## Installation Steps

1. **Install Minecraft & Forge:**
   - Install Minecraft Java Edition
   - Run Minecraft once and close it
   - Run the Forge installer
   - Choose "Install client" and click OK
   - Wait for installation to complete

2. **Install ComputerCraft:**
   - Press Win+R
   - Type: %appdata%\.minecraft\mods
   - Press Enter
   - Copy the downloaded CC:Tweaked .jar file into this folder

3. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Ollama:**
   - Run the Ollama installer
   - Open Command Prompt and run:
   ```bash
   ollama pull llama2
   ```

## Usage

1. **Start Minecraft:**
   - Launch Minecraft Launcher
   - Select the "Forge" profile
   - Click Play
   - Create a new Creative world

2. **In Minecraft:**
   - Press 'E' to open inventory
   - Search for "turtle" (ComputerCraft turtle)
   - Place a turtle where you want to build
   - Right-click the turtle

3. **Run the Builder:**
   ```bash
   python cc_builder.py
   ```
   - Type what you want to build
   - Follow the on-screen instructions to copy the code to your turtle

## Troubleshooting

1. **If Forge doesn't appear in launcher:**
   - Make sure you ran the Forge installer
   - Try running Minecraft vanilla once, then close and try again

2. **If turtle doesn't appear in inventory:**
   - Check that the CC:Tweaked .jar is in the mods folder
   - Make sure you selected the Forge profile

3. **If Python script fails:**
   - Make sure Ollama is running
   - Check that you installed requirements with pip
   - Try running: ollama pull llama2

## Notes

- The first time you run Ollama with llama2, it will download the model (this may take a while)
- Turtles need fuel in Survival mode, but not in Creative
- You can reuse build scripts by saving them with different names
- The turtle will build relative to its starting position
