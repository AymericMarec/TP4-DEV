import re
import socket
import argparse
import psutil
import sys as _sys
import os
import time
import datetime
from colorama import Fore
import threading

def ValidePort(port):
    try:
        port = int(port)
        if port < 0 or port > 65535:
            print(f"-p argument invalide. Le port spécifié {port} n'est pas un port valide (de 0 à 65535)")
            exit(1)
        elif port < 1024:
            print(f"ERROR -p argument invalide. Le port spécifié {port} est un port privilégié. Spécifiez un port au dessus de 1024.")
            exit(2)

    except:
        raise TypeError("Le port ca doit etre un nombre hein")

def ValideIP(ip):
    if not re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$",ip) :
        print(f"ERROR -l argument invalide. L'adresse {ip} n'est pas une adresse IP valide.")
        exit(3)
    elif not ip in str(psutil.net_if_addrs()):
        print(f"ERROR -l argument invalide. L'adresse {ip} n'est pas l'une des adresses IP de cette machine.")
        exit(4)
    
def GetInfos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store")
    parser.add_argument("-l", "--listen", action="store")
    args = parser.parse_args()
    if(args.port == None):
        port = 13337 
    else :
        ValidePort(args.port)
        port = args.port

    if(args.listen == None):
        host = ''
    else :
        ValideIP(args.listen)
        host = args.listen
    return port,host

def WriteLog(message):
    logfile = open(LOG_PATH, "a")
    logfile.write(message+"\n")

def FormatLog(message,type):
    ts = time.time()
    if(type == "WARN"):
        return Fore.WHITE + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +" "+ '\033[33m' + type +Fore.WHITE +" "+ message
    else :
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +" "+ type +" "+ message

def VerifyConnect():
    global Timer
    while True:
        if time.time() - Timer > 60 :
            msg = FormatLog(f"Aucun client depuis plus de une minute.","WARN")
            print(Fore.RED +msg)
            WriteLog(msg)
            Timer = time.time()
        time.sleep(1)

global Timer
Timer = time.time()
bg_task = threading.Thread(target=VerifyConnect)
bg_task.daemon = True
bg_task.start()

port,host = GetInfos()

pathfold = os.path.join("/var","log", "bs_server")
global LOG_PATH
LOG_PATH = os.path.join("/var","log", "bs_server", "bs_server.log")
if not(os.path.exists(pathfold) and os.path.isdir(pathfold)):
    os.makedirs(pathfold)




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, int(port)))  

s.listen(1)
msg = FormatLog(f"Le serveur tourne sur {host}:{port}","INFO")
print(msg)
WriteLog(msg)

conn, addr = s.accept()
ipclientConnect = str(addr).split("'")[1]
msg = FormatLog(f'Un client {ipclientConnect} s\'est connecté.',"INFO")
print(msg)
WriteLog(msg)

while True:
    try:
        data = conn.recv(1024)
        if not data: break
        Timer = time.time()
        IpClientMessage = str(conn.getpeername()).split("'")[1]
        msg = FormatLog('Le client {IpClientMessage} a envoyé "{data}".',"INFO")
        print(msg)
        WriteLog(msg)
        ToSend = bytes(eval(data))
        conn.sendall(ToSend)

        msg = FormatLog(f'Réponse envoyée au client {IpClientMessage} : "{message}".',"INFO")
        print(msg)
        WriteLog(msg)
    except socket.error:

        print("Error Occured.")
        break

conn.close()

