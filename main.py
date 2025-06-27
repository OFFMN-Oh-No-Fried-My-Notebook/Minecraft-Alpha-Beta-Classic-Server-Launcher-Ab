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
    elif version_a_b_c == 2:
        list=str("1.[b1] | 2.[b2] | 3.[b3] | 4.[b4] | 5.[b5] | 6.[b6] | 7.[b7] | 8.[b8] | 9.[b9]\n | 10.[b10] | 11.[b11] | 12.[b12] | 13.[b13] | 14.[b14] | 15.[b15]")
    elif version_a_b_c == 3:
        list=str("1.[c1] | 2.[c2] | 3.[c3] | 4.[c4] | 5.[c5] | 6.[c6] | 7.[c7] | 8.[c8] | 9.[c9]")
    elif version_a_b_c == 4:
        list=str("1.[r1] | 2.[r2] | 3.[r3] | 4.[r4] | 5.[r5] | 6.[r6] | 7.[r7] | 8.[r8] | 9.[r9]")
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
    jarname = "a"+str(version_select)+".jar"
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
menu()
set=int(input("Please select an option (1-11): "))
if set==1:
    select(1)
elif set==2:
    select(2)
elif set==3:
    select(3)
elif set==4:
    select(4)
elif set==5:
    about()
elif set==6:
    exit_launcher()
elif set==7:
    print("(null)")
    exit_launcher()
elif set==8:
    print("(null)")
    exit_launcher()
elif set==9:
    print("(null)")
    exit_launcher()
elif set==10:
    print("(null)")
    exit_launcher()
elif set==11:
    webbrowser.open("https://minecraft.wiki/w/Server")
    exit_launcher()
else:
    still_alive()
    exit_launcher()