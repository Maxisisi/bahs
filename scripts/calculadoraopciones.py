import json
import netmiko
from netmiko import ConnectHandler

conexion = {
    "ip":"192.168.56.101",
    "device_type":"cisco_ios",
    "username":"cisco",
    "password":"cisco123!"
}

opcion = 0

while opcion !=5:
    print("1-------VER CONFIGURACION GLOBAL")
    print("2-------VER INFORMACION DE INTERFACES")
    print("3-------VER TABLA DE RUTAS")
    print("4-------VER VERSION")
    print("5-------SALIR")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        comando = "show runn"

        with ConnectHandler(**conexion) as net_connect:
            salida = net_connect.send_command(comando)

        print(salida)
        print("-----------------------------------------------")
    elif opcion == 2:
        comando = "show ip int br"

        with ConnectHandler(**conexion) as net_connect:
            salida = net_connect.send_command(comando)

        print(salida)
        print("-----------------------------------------------")
    elif opcion == 3:
        comando = "show ip route"

        with ConnectHandler(**conexion) as net_connect:
            salida = net_connect.send_command(comando)

        print(salida)
        print("-----------------------------------------------")
    elif opcion == 4:
        comando = "show version"

        with ConnectHandler(**conexion) as net_connect:
            salida = net_connect.send_command(comando)

        print(salida)
        print("-----------------------------------------------")

print("Adiós...")
