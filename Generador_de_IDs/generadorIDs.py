import os
from random import randrange

def generar():
    cantidad = -1
    longitud = -1
    saltoLinea = "\n"
    try:
        fil = open(".\generadorIDs\IDs.txt", "w")
    except:
        os.system("mkdir generadorIDs")
        fil = open(".\generadorIDs\IDs.txt", "w", newline='')
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
    fil.write(str(cantidad) + " IDs de " + str(longitud) + " caracteres" + saltoLinea)
    fil.write("" + saltoLinea)
    for i in range(cantidad):
        fil.write(generador(longitud) + saltoLinea)
    fil.write("" + saltoLinea)
    f.close()

def generador(longitud):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    res = ""
    for i in range(longitud):
        res += chars[randrange(0, len(chars))]
    return res


if __name__ == "__main__":
    generar()