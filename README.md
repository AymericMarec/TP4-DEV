# I. Simple bs program

- 🌞fichier client :

- 🌞fichier server : 


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


## 2. User friendly

- fichier serveur :

- fichier client :

## 3. You say client I hear control

- fichier client :

# II. You say dev I say good practices

