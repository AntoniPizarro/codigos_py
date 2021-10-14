import os

def decToHex(decNum):
    codes = '0123456789abcdef'
    decimal = decNum
    res = ""
    while decimal > 0:
        res += codes[decimal % 16]
        decimal = int(decimal / 16)
    return res[::-1]

if __name__ == "__main__":
    num = int(input())
    print(decToHex(num))
    os.system("pause")