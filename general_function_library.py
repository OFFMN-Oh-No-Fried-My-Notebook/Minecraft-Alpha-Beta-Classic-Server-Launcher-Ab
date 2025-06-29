import datetime
import webbrowser
import sys
def menu():
    print(f"<------------------------------McSeverLauncher------------{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}>")
    print(f"Minecraft Alpha and Beta Server Launcher")
    print(f"1.[launch] Minecraft Alpha Server")
    print(f"2.[launch] Minecraft Beta Server")
    print(f"3.[launch] Minecraft classic Server")
    print(f"4.[launch] Minecraft Release Server launcher")
    print(f"5.[about] About Launcher")
    print(f"6.[exit] Exit Launcher")
    print(f"<------------------------------McSeverLauncher--------------------------------->")
    print(f"7.[install]java")
    print(f"8.[install](unknown)")
    print(f"9.[install](unknown)")
    print(f"<------------------------------McSeverLauncher--------------------------------->")
    print(f"10.[frp install]（未完成）")
    print(f"11.[wiki]minecraft wiki")
    print(f"12.[editor->'server.properties']Modify various server configurations")
    print(f"<------------------------------McSeverLauncher--------------------------------->")
def editor_server_properties_menu():
    # Code to modify server.properties
    print(f"<------------------------------McSeverLauncher------------{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}>")
    print(f"1.[title] Modify server title")
    print(f"2.[max-players] Modify max players")
    print(f"3.[level-name] Modify level name")
    print(f"4.[gamemode] Modify game mode")
    print(f"5.[difficulty] Modify difficulty")
    print(f"6.[server-port] Modify server port")
    print(f"7.[white-list] Modify white list")
    print(f"8.[spawn-protection] Modify spawn protection")
    print(f"9.[enable-command-block] Modify enable command block")
    print(f"10.[view-distance] Modify view distance")
    print(f"11.[tick-distance] Modify tick distance")
    print(f"12.[max-build-height] Modify max build height")
    print(f"13.[spawn-npcs] Modify spawn NPCs")
    print(f"<------------------------------McSeverLauncher--------------------------------->")
    print("Please select an option (1-13): ", end="")
def edit_server_properties(option):
    """根据选项修改server.properties配置"""
    config_mapping = {
        '1': ('motd', 'Server title (MOTD)'),
        '2': ('max-players', 'Maximum players'),
        '3': ('level-name', 'World name'),
        '4': ('gamemode', 'Game mode (survival/creative/adventure)'),
        '5': ('difficulty', 'Difficulty (easy/normal/hard/peaceful)'),
        '6': ('server-port', 'Server port (default: 25565)'),
        '7': ('white-list', 'Enable whitelist (true/false)'),
        '8': ('spawn-protection', 'Spawn protection radius (0-16)'),
        '9': ('enable-command-block', 'Enable command blocks (true/false)'),
        '10': ('view-distance', 'View distance (3-32)'),
        '11': ('simulation-distance', 'Simulation distance (3-32)'),
        '12': ('max-build-height', 'Max build height (64-320)'),
        '13': ('spawn-npcs', 'Spawn NPCs (true/false)')
    }

    if option not in config_mapping:
        print("Invalid option!")
        return

    prop_key, description = config_mapping[option]
    
    try:
        # 读取当前配置
        with open('server.properties', 'r') as file:
            lines = file.readlines()
        
        # 查找并修改配置
        found = False
        with open('server.properties', 'w') as file:
            for line in lines:
                if line.strip().startswith(prop_key + '='):
                    current_value = line.split('=')[1].strip()
                    print(f"\nCurrent {prop_key}: {current_value}")
                    print(f"Description: {description}")
                    new_value = input("Enter new value: ").strip()
                    file.write(f"{prop_key}={new_value}\n")
                    found = True
                else:
                    file.write(line)
            
            # 如果配置项不存在则添加
            if not found:
                print(f"\n{prop_key} not found, adding new entry")
                print(f"Description: {description}")
                new_value = input("Enter value: ").strip()
                file.write(f"\n{prop_key}={new_value}\n")
        
        print(f"\nSuccessfully updated {prop_key}!")
    
    except FileNotFoundError:
        print("Error: server.properties not found! Make sure the server has been started at least once.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
def view_server_properties():
    """查看server.properties配置"""
    try:
        with open('server.properties', 'r') as file:
            content = file.read()
            print("\nCurrent server.properties content:")
            print(content)
    except FileNotFoundError:
        print("Error: server.properties not found! Make sure the server has been started at least once.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")