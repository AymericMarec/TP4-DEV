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
    msg = FormatLog(f"Impossible de se connecter au serveur {host} sur le port {port}.","ERROR")
    print(msg)
    WriteLog(msg)


UserInput = input("Entrez une opération ( nombre + opérateur + nombre), avec des nombres compris entre -100000 et 100000\n\nExemple :\n\n3 + 2\n5*6\n\n\n")
if not(re.search("^-{0,1}\d+\s*[+\-*\/]\s*-{0,1}\d+$",UserInput)):
    print("Mauvais Format d'entrée")
    exit(0)
UserInput = UserInput.replace(" ", "")

s.sendall(UserInput.encode())
msg = FormatLog(f"Message envoyé au serveur {host} : {UserInput}.","INFO")
WriteLog(msg)

data = s.recv(1024)

s.close()
print(f"Le serveur a répondu {repr(data)}")
msg = FormatLog(f"Réponse reçue du serveur {host} : {UserInput}.","INFO")
WriteLog(msg)

sys.exit()


# Voila un magnifique debut de fonction eval maison parce que j'ai oublié de lire la suite du tp qui demande d'utiliser la commande 

# def GetFirstNB(UserInput):
#     index = 1
#     while True:
#         try:
#             int(UserInput[0:index])
#             index+=1
#         except:
#             return int(UserInput[0:index-1]),index

# UserInput = input("Entrez une opération ( nombre + opérateur + nombre), avec des nombres compris entre -100000 et 100000\n\nExemple :\n\n3 + 2\n5*6\n\n\n")
# if not(re.search("\d+\s*[+\-*\/]\s*\d+",UserInput)):
#     print("Mauvais Format d'entrée")
#     exit(0)
# UserInput = UserInput.replace(" ", "")


# FirstNB , index = GetFirstNB(UserInput)
# Operator = UserInput[index-1]
# SecondNB = int(UserInput[index:len(UserInput)])
# match Operator :
#     case "+":
#         Result = FirstNB+SecondNB
#     case "-":
#         Result = FirstNB-SecondNB
#     case "/":
#         Result = FirstNB/SecondNB
#     case "*":
#         Result = FirstNB*SecondNB
#     case _ :
#         print("Opérateur inconnu : "+Operator)
#         exit(1)
# print(Result)