import socket
import sys
import re
#10.33.77.14
#10.1.1.253
host = '192.168.237.219'
port = 13337 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except :
    print("Probleme lors de la connexion au serveur")

UserInput = input("Que veux-tu envoyer au serveur : ")
if not type(UserInput) == str:
    raise TypeError("Le message n'est pas un string")
if not re.search(r".*(meo|waf).*",UserInput) :
    raise ValueError("Tu n'es pas un humain")

s.sendall(str.encode(UserInput))
data = s.recv(1024)
s.close()
print(f"Le serveur a répondu {repr(data)}")

sys.exit()