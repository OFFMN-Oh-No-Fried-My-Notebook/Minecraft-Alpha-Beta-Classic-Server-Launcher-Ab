#minecraft alpha and beta server launcher
import wget
select=int("1")
def stillaive():
	import time
	song = """
_________________________________________________________________
|This was a triumph.											|
|I'm making a note here: huge success.							|
|It's hard to overstate my satisfaction.						|
|Aperture Science.												|
|We do what we must because we can.								|
|For the good of all of us.										|
|Except the ones who are dead.									|
|But there's no sense crying over every mistake.				|
|You just keep on trying till you run out of cake.				|
|And the science gets done.										|
|And you make a neat gun.										|
|For the people who are still alive.							|
|																|
|I'm not even angry.											|
|I'm being so sincere right now.								|
|Even though you broke my heart.								|
|And killed me.													|
|And tore me to pieces.											|
|And threw every piece into a fire.								|
|As they burned it hurt because I was so happy for you.			|
||Now these points of data make a beautiful line.				|
|And we're out of beta.											|
|We're releasing on time.										|
|So I'm GLaD. I got burned.										|
|Think of all the things we learned.							|
|For the people who are still alive.							|
|																|
|Go ahead and leave me.											|
|I think I prefer to stay inside.								|
|Maybe you'll find someone else to help you.					|
|Maybe Black Mesa...											|
|THAT WAS A JOKE. FAT CHANCE.									|
|Anyway, this cake is great.									|
|It's so delicious and moist.									|
|Look at me still talking when there's science to do.			|
|When I look out there, it makes me GLaD I'm not you.			|
|I've experiments to run.										|
|There is research to be done.									|
|On the people who are still alive.								|
|And believe me I am still alive.								|
|I'm doing science and I'm still alive.							|
|I feel FANTASTIC and I'm still alive.							|
|While you're dying I'll be still alive.						|
|And when you're dead I will be still alive.					|		
|Still alive.													|
|Still alive.													|
ˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉ
	"""
	for line in song.split('\n'):
		print(line)
		time.sleep(0.5)
def 无效选择():
	print("无效选择，请重新输入。")
	return
def mcsevernogui(jarname:str,m1:int,m2:int):
	import os
	dirpath= os.path.dirname(os.path.abspath(__file__))
	path = os.path.join(dirpath, jarname)
	os.path.exists(jarname)
	if not os.path.exists(jarname):
		wget.download("https://github.com/offmn-sv-cheats-1/OFFMN-s-Miscellaneous-Repository/blob/main/" + jarname, path)
		os.system("cls")
		os.system("java -Xmx"+str(m1)+"M -Xms"+str(m2)+"M -jar " + jarname + " nogui")
		os.system("pause")
	else:
		os.system("cls")
		os.system("java -Xmx"+str(m1)+"M -Xms"+str(m2)+"M -jar " + jarname + " nogui")
		os.system("pause")
def mcsever(jarname:str,m1:int,m2:int):
	import os
	dirpath= os.path.dirname(os.path.abspath(__file__))
	path = os.path.join(dirpath, jarname)
	os.path.exists(jarname)
	if not os.path.exists(jarname):
		wget.download("https://github.com/offmn-sv-cheats-1/OFFMN-s-Miscellaneous-Repository/blob/main/" + jarname, path)
		os.system("cls")
		os.system("java -Xmx"+str(m1)+"M -Xms"+str(m2)+"M -jar " + jarname)
		os.system("pause")
	else:
		os.system("cls")
		os.system("java -Xmx"+str(m1)+"M -Xms"+str(m2)+"M -jar " + jarname)
		os.system("pause")
def installjava(version:str):
	import os
	import webbrowser
	if version == "8":
		webbrowser.open("https://1drv.ms/u/c/0b6198fc22ae2330/EY09U1Q-ryZBpM00iwBAwHEBP5HQQDhsiHx5tRGgBnhuGQ")
	else:
		print("Invalid Java version specified.")
		return
	print(f"Java {version} installed successfully.")

def installfrp(version:str):
	import os
	if version == 1:
		os.system("frp1.exe /s")
		print("FRP version 1 installed successfully.")
	else:
		print("Invalid FRP version specified.")
		return
	print(f"FRP {version} installed successfully.")	
#fixing......
def about():
	print("This is a Minecraft Alpha and Beta Server Launcher.")
	print("It allows you to launch Minecraft servers with specified memory allocation.")
	print("You can also install different versions of Java and set up FRP for internal network penetration.")
	print("Version: 1.0")
def exit_launcher():
	import os
	import time
	print("Exiting the launcher in 3 seconds...")
	time.sleep(3)
	os.system("cls")
	print("Exiting the launcher. Goodbye!")
	exit()
#mcsever(inside1,int(input("请输入最大内存分配（单位M）：")),int(input("请输入最小内存分配（单位M）：")))
print("<------------------------------McSeverLauncher--------------------------------->")
print("Minecraft Alpha and Beta Server Launcher")
print("1.[launch] Minecraft Alpha Server")
print("2.[launch] Minecraft Beta Server")
print("3.[launch] Minecraft classic Server")
print("4.[about] About Launcher")
print("5.[exit] Exit Launcher")
print("<------------------------------McSeverLauncher--------------------------------->")
print("6.[install]java")
print("7.[install](unknown)")
print("8.[install](unknown)")
print("<------------------------------McSeverLauncher--------------------------------->")
print("9.[frp install]（未完成）")
print("10.[other] Minecraft Release Server launcher")
print("11.[song] Still Alive")
print("<------------------------------McSeverLauncher--------------------------------->")
print("Please select an option (1-11): ", end="")
select = int(input(":"))
if select == 1:
	import os
	os.system("cls")
	print("<------------------------------McSeverLauncher--------------------------------->")
	print("versionselect:1.[a1] | 2.[a2] | 3.[a3] | 4.[a4] | 5.[a5] | 6.[a6] | 7.[a7] | 8.[a8] | 9.[a9]")
	print("<------------------------------McSeverLauncher--------------------------------->")
	print("Please select a version (1-9): ", end="")
	version_select = int(input(":"))
	jarname = "a"+str(version_select)+".jar"
	guiin = input("是否使用GUI模式？(y/n): ").strip().lower()
	if guiin == 'y':
		mcsever(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
	else:
		mcsevernogui(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
elif select == 2:
	import os
	os.system("cls")
	print("<------------------------------McSeverLauncher--------------------------------->")
	print("versionselect:1.[b1] | 2.[b2] | 3.[b3] | 4.[b4] | 5.[b5] | 6.[b6] | 7.[b7] | 8.[b8] | 9.[b9]")
	print("              | 10.[b10] | 11.[b11] | 12.[b12] | 13.[b13] | 14.[b14] | 15.[b15]")
	print("<------------------------------McSeverLauncher--------------------------------->")
	print("Please select a version (1-9): ", end="")
	version_select = int(input(":"))
	jarname = "b"+str(version_select)+".jar"
	guiin = input("是否使用GUI模式？(y/n): ").strip().lower()
	if guiin == 'n':
		mcsevernogui(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
	else:
		mcsever(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
elif select == 3:
	import os
	os.system("cls")
	print("<------------------------------McSeverLauncher--------------------------------->")
	print("versionselect:1.[c1] | 2.[c2] | 3.[c3] | 4.[c4] | 5.[c5] | 6.[c6] | 7.[c7] | 8.[c8] | 9.[c9]")
	print("<------------------------------McSeverLauncher--------------------------------->")
	print("Please select a version (1-9): ", end="")
	version_select = int(input(":"))
	jarname = "c"+str(version_select)+".jar"
	guiin = input("是否使用GUI模式？(y/n): ").strip().lower()
	if guiin == 'n':
		mcsevernogui(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
	else:
		mcsever(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
elif select == 4:
	about()
elif select == 5:
	exit_launcher()
elif select == 6:
	installjava()
elif select == 7:
	print("此选项目前未完成。")
	exit_launcher()
elif select == 8:
	print("此选项目前未完成。")
	exit_launcher()
elif select == 9:
	print("此选项目前未完成。")
	exit_launcher()
elif select == 10:
	import os
	os.system("cls")
	jarname = "r1.jar"
	mcsever(jarname, int(input("请输入最大内存分配（单位M）：")), int(input("请输入最小内存分配（单位M）：")))
elif select == 11:
	stillaive()
else:
	无效选择()
	exit_launcher()