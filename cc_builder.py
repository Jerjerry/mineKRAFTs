import ollama
import os
import json

class MinecraftBuilder:
    def __init__(self):
        self.build_scripts_dir = "computer/0"  # ComputerCraft computer directory
        os.makedirs(self.build_scripts_dir, exist_ok=True)
        
    async def generate_building_instructions(self, prompt):
        system_prompt = """
        You are a Minecraft building expert. Generate ComputerCraft Lua code for building structures.
        Use turtle commands like:
        - turtle.forward()
        - turtle.back()
        - turtle.up()
        - turtle.down()
        - turtle.place()
        - turtle.placeDown()
        - turtle.placeUp()
        
        Return ONLY valid Lua code that can be executed by a ComputerCraft turtle.
        Include comments explaining each major step.
        """
        
        try:
            response = await ollama.chat(
                model='llama2',
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': f"Create ComputerCraft Lua code to build: {prompt}"}
                ]
            )
            
            # Extract code from the response
            code = response['message']['content']
            # Clean up the code (remove markdown if present)
            code = code.replace('```lua', '').replace('```', '').strip()
            return code
        except Exception as e:
            print(f"Failed to generate instructions: {e}")
            return None

    def save_build_script(self, code, name):
        """Save the Lua code to a file that ComputerCraft can read"""
        script_path = os.path.join(self.build_scripts_dir, f"{name}.lua")
        with open(script_path, 'w') as f:
            f.write(code)
        print(f"Saved build script to: {script_path}")
        print("\nTo use this in Minecraft:")
        print("1. Place a ComputerCraft turtle in your world")
        print("2. Right-click the turtle to open its interface")
        print(f"3. Type: edit {name}")
        print("4. Paste the contents of the generated script")
        print("5. Press Ctrl to save and exit")
        print("6. Type: {name} to run the build program")

async def main():
    builder = MinecraftBuilder()
    
    # Get user input
    print("What would you like to build in Minecraft?")
    prompt = input("> ")
    
    # Generate and save the building script
    code = await builder.generate_building_instructions(prompt)
    if code:
        builder.save_build_script(code, "build")
        
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
