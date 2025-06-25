import json
import netmiko
from netmiko import ConnectHandler

conexion = {
    "ip": "192.168.56.101",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!"
}

comando = "show ip int br"

with ConnectHandler(**conexion) as net_connect:
    salida = net_connect.send_command(comando)

# Buscar la línea que contiene Loopback30
for linea in salida.splitlines():
    if "Loopback30" in linea:
        # Dividir la línea por espacios múltiples y obtener el estado
        partes = linea.split()
        estado = partes[4]  # El estado está en la 5ta columna (índice 4)
        print(f"El estado de Loopback30 es: {estado}")
        break
else:
    print("No se encontró la interfaz Loopback30")
