import json
import netmiko
from netmiko import ConnectHandler

conexion = {
    "ip":"192.168.56.101",
    "device_type":"cisco_ios",
    "username":"cisco",
    "password":"cisco123!"
}

com = "show version"

with ConnectHandler(**conexion) as net_connect:
    salida = net_connect.send_command(com)

print(salida)