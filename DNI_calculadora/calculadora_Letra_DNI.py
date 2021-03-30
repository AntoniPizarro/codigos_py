import os

def calculadora(num):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[num % 23]

if __name__ == "__main__":
    num = int(input())
    print(calculadora(num))
    os.system("pause")