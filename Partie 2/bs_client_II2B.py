import socket
import sys
import re
import time
import datetime
from colorama import Fore
import os

def WriteLog(message):
    logfile = open(LOG_PATH, "a")
    logfile.write(message+"\n")

def FormatLog(message,type):
    ts = time.time()
    if(type == "WARN"):
        return Fore.WHITE + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +" "+ '\033[33m' + type +Fore.WHITE +" "+ message
    elif(type == "ERROR"):
        return '\033[31m' + type +Fore.WHITE +" "+ message
    else :
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +" "+ type +" "+ message



pathfold = os.path.join("/var","log", "bs_server")
global LOG_PATH
LOG_PATH = os.path.join("/var","log", "bs_server", "bs_server.log")
if not(os.path.exists(pathfold) and os.path.isdir(pathfold)):
    os.makedirs(pathfold)

host = '10.1.1.253'
port = 13337 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    s.connect((host, port))
    msg = FormatLog(f"Connexion réussie à {host}:{port}","INFO")
    WriteLog(msg)
except :
    msg = FormatLog(f"Impossible de se connecter au serveur {host} sur le port {host}.","ERROR")
    print(msg)
    WriteLog(msg)

UserInput = input("Que veux-tu envoyer au serveur : ")
if not type(UserInput) == str:
    raise TypeError("Le message n'est pas un string")
if not re.search(r".*(meo|waf).*",UserInput) :
    raise ValueError("Tu n'es pas un humain")

s.sendall(str.encode(UserInput))
data = s.recv(1024)
msg = FormatLog(f"Message envoyé au serveur {host} : {UserInput}.","INFO")
WriteLog(msg)

s.close()
print(f"Le serveur a répondu {repr(data)}")
msg = FormatLog(f"Réponse reçue du serveur {host} : {UserInput}.","INFO")
WriteLog(msg)

sys.exit()