#group1
import wget
import datetime
import webbrowser
import requests
import os
import sys
from general_function_library import *
#group2
windows_or_linux=str(sys.platform)
def select(version_a_b_c:int):
    if  version_a_b_c == 1:
        list=str("1.[a1] | 2.[a2] | 3.[a3] | 4.[a4] | 5.[a5] | 6.[a6] | 7.[a7] | 8.[a8] | 9.[a9]")
        perdect="a"
    elif version_a_b_c == 2:
        list=str("1.[b1] | 2.[b2] | 3.[b3] | 4.[b4] | 5.[b5] | 6.[b6] | 7.[b7] | 8.[b8] | 9.[b9]\n | 10.[b10] | 11.[b11] | 12.[b12] | 13.[b13] | 14.[b14] | 15.[b15]")
        perdect="b"
    elif version_a_b_c == 3:
        list=str("1.[c1] | 2.[c2] | 3.[c3] | 4.[c4] | 5.[c5] | 6.[c6] | 7.[c7] | 8.[c8] | 9.[c9]")
        perdect="c"
    elif version_a_b_c == 4:
        list=str("1.[r1] | 2.[r2] | 3.[r3] | 4.[r4] | 5.[r5] | 6.[r6] | 7.[r7] | 8.[r8] | 9.[r9]")
        perdect="r"
    else:
        print("Invalid version selection.")
        exit_launcher()
    import os
    os.system("cls")
    print("<------------------------------McSeverLauncher--------------------------------->")
    print(f"versionselect:{list}")
    print("<------------------------------McSeverLauncher--------------------------------->")
    print("Please select a version (1-9): ", end="")
    version_select = int(input(":"))
    jarname = str(perdect)+str(version_select)+".jar"
    guiin = input("是否使用GUI模式？(y/n): ").strip().lower()
    if guiin == 'y':
        mcsever(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
    else:
        mcsevernogui(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
#group3
if windows_or_linux=="win32":
    from Windows_version_library import *
elif windows_or_linux=="linux":
    from Linux_version_library import *
else:
    print("Unsupported operating system. Please run this script on Windows or Linux.")
    sys.exit(1)
#main
while True:
    menu()
    set=int(input("Please select an option (1-11): "))
    if set==1:
        try:
            select(1)
        except Exception as e:
            print(f"Error occurred while selecting version: {e}")
    elif set==2:
        try:
            select(2)
        except Exception as e:
            print(f"Error occurred while selecting version: {e}")
    elif set==3:
        try:
            select(3)
        except Exception as e:
            print(f"Error occurred while selecting version: {e}")
    elif set==4:
        try:
            select(4)
        except Exception as e:
            print(f"Error occurred while selecting version: {e}")
    elif set==5:
       about()
    elif set==6:
        exit_launcher()
    elif set==7:
        try:
            if windows_or_linux=="win32":
                installjava("8")
            elif windows_or_linux=="linux":
                installjava("8")
        except Exception as e:
            print(f"Error occurred while installing Java: {e}")
    elif set==8:
        print("null")
        exit_launcher()
    elif set==9:
        print("null")
        exit_launcher()
    elif set==10:
        print("null")
        exit_launcher()
    elif set==11:
        webbrowser.open("https://minecraft.wiki/w/Server")
        exit_launcher()
    elif set==12:
        import os
        if not os.path.exists("server.properties"):
            print("server.properties file not found. Creating a new one.")
            settc=input("Do you want to create server.properties? (y/n): ")
            if settc.lower() == "y":
                with open("server.properties", "w") as f:
                    f.write("# Minecraft Server Properties\n")
                    f.write("motd=Welcome to the Minecraft Server!\n")
                    f.write("max-players=20\n")
                    f.write("level-name=world\n")
                    f.write("gamemode=survival\n")
                    f.write("difficulty=normal\n")
                    f.write("server-port=25565\n")
                    f.write("white-list=false\n")
                    f.write("spawn-protection=16\n")
                    f.write("enable-command-block=false\n")
                    f.write("view-distance=10\n")
                    f.write("simulation-distance=10\n")
                    f.write("max-build-height=256\n")
                    f.write("spawn-npcs=true\n")
                editor_server_properties_menu()
                edit_server_properties(input("Please select an option (1-13): "))
                view_server_properties()
                exit_launcher()
            else:
                exit_launcher()
        else:
            os.system("cls" if windows_or_linux == "win32" else "clear")
            editor_server_properties_menu()
            edit_server_properties(input("Please select an option (1-13): "))
            view_server_properties()
            exit_launcher()
    else:
        import time
        print("error: Invalid option selected.")
        time.sleep(1)
        exit_launcher()