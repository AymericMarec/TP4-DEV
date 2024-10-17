import socket
import sys
import re
host = '10.1.1.253'
port = 13337 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

UserInput = input("Entrez une opération ( nombre + opérateur + nombre), avec des nombres compris entre -100000 et 100000\n\nExemple :\n\n3 + 2\n5*6\n\n\n")
if not(re.search("\d+\s*[+\-*\/]\s*\d+",UserInput)):
    print("Mauvais Format d'entrée")
    exit(0)
UserInput = UserInput.replace(" ", "")

s.sendall(b'UserInput')

data = s.recv(1024)

s.close()

if data :
    print(f"Le serveur a répondu {repr(data)}")

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