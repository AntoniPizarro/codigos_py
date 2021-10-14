import os

def decToBin(decNum):
    decimal = decNum
    res = ""
    while decimal > 0:
        res += str(decimal % 2)
        decimal = int(decimal / 2)
    return res[::-1]

if __name__ == "__main__":
    num = int(input())
    print(decToBin(num))
    os.system("pause")