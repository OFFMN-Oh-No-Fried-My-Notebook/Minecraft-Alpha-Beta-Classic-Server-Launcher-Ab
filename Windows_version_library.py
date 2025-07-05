import wget
import datetime
import webbrowser
import requests
import os
#select=int("1")
def still_alive():
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
	url = f"https://github.com/offmn-sv-cheats-1/OFFMN-s-Miscellaneous-Repository/releases/download/macseverpack1/{jarname}"
	import os
	dirpath= os.path.dirname(os.path.abspath(__file__))
	path = os.path.join(dirpath, jarname)
	if not os.path.exists(path):
		wget.download(url,out=path)
		os.system("cls")
		os.system(fr'java -Xmx{m1}M -Xms{m2}M -jar ""{path}"" nogui')
		os.system("cls")
		os.system("pause")
	else:
		os.system("cls")
		os.system(fr'java -Xmx{m1}M -Xms{m2}M -jar ""{path}"" nogui')
		os.system("cls")
		os.system("pause")
def mcsever(jarname:str,m1:int,m2:int):
	url = f"https://github.com/offmn-sv-cheats-1/OFFMN-s-Miscellaneous-Repository/releases/download/macseverpack1/{jarname}"
	import os
	dirpath= os.path.dirname(os.path.abspath(__file__))
	path = os.path.join(dirpath, jarname)
	if not os.path.exists(path):
		wget.download(url,out=path)
		os.system(f"cls")
		os.system(fr'java -Xmx{m1}M -Xms{m2}M -jar ""{path}""')
		os.system("cls")
		os.system("pause")
	else:
		os.system("cls")
		os.system(fr'java -Xmx{m1}M -Xms{m2}M -jar ""{path}""')
		os.system("cls")
		os.system("pause")
def installjava(version:str):
	import os
	if version == "8":
		url = "https://repo.huaweicloud.com/java/jdk/8u202-b08/jdk-8u202-windows-x64.exe"
		file_name = "jdk-8u202-windows-x64.exe"
		wget.download(url, out=file_name)
		os.system(f"{file_name} /s")
		print("Java 8 installed successfully.")

def installfrp(version:str):
	print("fixing......")
	exit_launcher()
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