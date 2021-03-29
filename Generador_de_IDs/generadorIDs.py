import os
from random import randrange

def generar():
    cantidad = -1
    longitud = -1
    while cantidad <= 0:
        print("Cantidad de IDs que quieres generar")
        cantidad = int(input())
        if cantidad <= 0:
            print("introduce un numero mayor a 0")
    while longitud <= 0:
        print("Longitud de cada ID")
        longitud = int(input())
        if longitud <= 0:
            print("introduce un numero mayor a 0")
    os.system("echo " + str(cantidad) + " IDs de " + str(longitud) + " caracteres>>./generadorIDs/id.txt")
    os.system("echo.>>./generadorIDs/id.txt")
    for i in range(cantidad):
        os.system("echo " + generador(longitud) + ">>./generadorIDs/id.txt")
    os.system("echo.>>./generadorIDs/id.txt")

def generador(longitud):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    res = ""
    for i in range(longitud):
        res += chars[randrange(0, len(chars))]
    return res


if __name__ == "__main__":
    generar()