import re
import socket
import argparse
import psutil
import sys as _sys

# class MyArgumentParser(argparse.ArgumentParser):

#     def print_help(self, file=None):
#         if file is None:
#             file = _sys.stdout
#         message = "Please go to http://some_website.com/help to understand more about our software"
#         file.write(message+"\n")


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
    # parser.add_argument("-h", "--help", action="store_true")
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

port,host = GetInfos()


#10.33.77.14
#10.1.1.253
#host = '10.33.77.14'
#port = 13337 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, int(port)))  

s.listen(1)
conn, addr = s.accept()
print('Un client vient de se co et son IP c\'est', str(addr).split("'")[1])


while True:
    try:
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")
        if"meo" in str(data) :
            conn.sendall(b"Meo a toi confrere.")
        elif"waf" in str(data):
            conn.sendall(b"ptdr t ki")
        else :
            conn.sendall(b"Mes respects humble humain.")

    except socket.error:

        print("Error Occured.")
        break

conn.close()

