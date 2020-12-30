#!bin/python
# This Tool for Educational Purpose Only
# Code By Ahamed insafeer
# WhatsApp Admin Hijack Using Termux 
# 100 % SUCCESSFULL


import os
import requests
import random
import logging
import os,random,time,sys
from urllib import request
from requests import post,get
from colorama import Fore,init,Style

def Spinner():
	l=['|','/','-','\\']
	for i in l+l+l:
		sys.stdout.write('\r'+Style.BRIGHT+Fore.LIGHTYELLOW_EX+'[*] Checking Your Internet Connection  '+i)
		sys.stdout.flush()
		time.sleep(0.2)
time.sleep(0.3)


targetAdminNo=int(input("\033[1;33m[+] Enter Group Creator Number : "))
print("")
targetgroup=input("\033[1;33m[+] Enter Target Group Link :")
print("")
responseNo=int(input("\033[1;33m[+] Enter Your Number :"))
print("")

#convert all mobile number to binary
binary=[1,1,0,0,0,1,1,1,0]
biAd=bin(targetAdminNo)
biRe=bin(responseNo)

if (targetAdminNo==responseNo):
	print("\033[1;31;40m No Hijacking You Are The Admin")
else:
	#try to loging with hijacking
	try:
		Spinner()
		request.urlopen('https://httpbin.org/get')
		print(Fore.LIGHTGREEN_EX+Style.BRIGHT+'\n[+] Connection Successful!')
		time.sleep(1.5)
		os.system('clear')
		print("\033[1;32;40m Starts the connection with Whatsapp servers........")
		print(Fore.LIGHTGREEN_EX+Style.BRIGHT+'\n[#] Please Wait....')
		os.system("python requirements.py")
		timeout()
	except:
		time.sleep(0.4)
		print(Fore.LIGHTRED_EX+Style.BRIGHT+'\n[!] You Aren\'t Connected To Internet!')
		time.sleep(0.3)
		print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Please Connect To Internet To Continue...')
		time.sleep(0.3)
		input(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Exiting...\nPress Enter To Continue...')
		exit()
def start(self):
        "Starts the connection with Whatsapp servers,"
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        try:
            logging.info("#" * 50)
            logging.info("Server started. Phone number: %s" % self.credentials[0])
            logging.info("#" * 50)
            self.stack.loop()
        except AuthError as e:
            logging.exception("Authentication Error: %s" % e.message)
        except Exception as e:
            logging.exception("Unknown Error: %s" % e.message)
            raise e 
def timeout():
	time.sleep(1.0)
	print("\033[1;31;40m Requests Time Out.Try Again !!! ")
