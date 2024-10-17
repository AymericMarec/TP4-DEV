import socket


#10.33.77.14
#10.1.1.253
host = '10.33.77.14'
port = 13337 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  

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
