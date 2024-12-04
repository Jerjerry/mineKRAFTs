import ollama
from mcrcon import MCRcon
import os
from dotenv import load_dotenv

load_dotenv()

RCON_PASSWORD = os.getenv('RCON_PASSWORD', 'your_rcon_password')
RCON_HOST = os.getenv('RCON_HOST', 'localhost')
RCON_PORT = int(os.getenv('RCON_PORT', '25575'))

class MinecraftBuilder:
    def __init__(self):
        self.mcr = MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT)
        
    def connect(self):
        try:
            self.mcr.connect()
            print("Connected to Minecraft server!")
        except Exception as e:
            print(f"Failed to connect to Minecraft server: {e}")
            
    def disconnect(self):
        self.mcr.disconnect()
        
    def execute_command(self, command):
        try:
            response = self.mcr.command(command)
            print(f"Command executed: {command}")
            print(f"Response: {response}")
            return response
        except Exception as e:
            print(f"Failed to execute command: {e}")
            return None

    async def generate_building_instructions(self, prompt):
        try:
            # Use Ollama to generate building instructions
            response = await ollama.chat(
                model='llama2',
                messages=[{
                    'role': 'user',
                    'content': f"Generate Minecraft building instructions for: {prompt}. "
                              f"Provide step-by-step commands using /setblock or /fill commands. "
                              f"Keep it simple and focused on basic blocks."
                }]
            )
            return response['message']['content']
        except Exception as e:
            print(f"Failed to generate instructions: {e}")
            return None

    def build_structure(self, instructions):
        # Split instructions into individual commands
        commands = [cmd.strip() for cmd in instructions.split('\n') 
                   if cmd.strip().startswith('/')]
        
        # Execute each command
        for cmd in commands:
            if cmd.startswith('/'):
                cmd = cmd[1:]  # Remove leading slash
            self.execute_command(cmd)

async def main():
    # Example usage
    builder = MinecraftBuilder()
    builder.connect()
    
    try:
        # Example: Generate and build a simple house
        instructions = await builder.generate_building_instructions(
            "Create a small 5x5 house with a door and two windows"
        )
        
        if instructions:
            print("\nGenerated Instructions:")
            print(instructions)
            print("\nBuilding structure...")
            builder.build_structure(instructions)
    finally:
        builder.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
