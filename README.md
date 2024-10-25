# TP4 DEV : Socquettes

## I. Simple bs program

- 🌞fichier client : [client](./Partie%201/bs_client_I1.py)

- 🌞fichier server : [serveur](./Partie%201/bs_server_I1.py)


### 🌞 Commandes...


sur les 2 machines : 
```
sudo dnf install python3.0 -y
```

sur le serveur : 
```
[aymeric@serveur ~]$ sudo firewall-cmd --add-port=13337/tcp --permanent
success
[aymeric@serveur ~]$ sudo firewall-cmd --reload
success
[aymeric@serveur ~]$ python serveur.py &
[1] 1395
[aymeric@serveur ~]$ ss -lnpt | grep python
LISTEN 0      1         10.1.1.253:13337      0.0.0.0:*    users:(("python",pid=1395,fd=3))
```


### 2. User friendly

- fichier serveur : [serveur](./Partie%201/bs_server_I2.py)

- fichier client : [client](./Partie%201/bs_client_I2.py)

### 3. You say client I hear control

- fichier client : [client](./Partie%201/bs_client_I3.py)

## II. You say dev I say good practices

### 1. Args

- 🌞fichier client : [client](./Partie%202/bs_server_II1.py)

### 2. Logs

### A. Logs client

- 🌞fichier server : [serveur](./Partie%202/bs_server_II2A.py)

### B. Logs client

- fichier client : [client](./Partie%202/bs_client_II2B.py)

## III. COMPUTE

- fichier client : [client](./Partie%203/bs_client_III.py)

- 🌞fichier server : [serveur](./Partie%203/bs_server_III.py)
