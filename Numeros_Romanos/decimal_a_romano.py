import os

def to_roman(num):
    decimal = num
    res = ""
    while decimal >= 1000:
        res += "M"
        decimal -= 1000
    if decimal >= 900:
        res += "CM"
        decimal -= 900
    while decimal >= 500:
        res += "D"
        decimal -= 500
    if decimal >= 400:
        res += "CD"
        decimal -= 400
    while decimal >= 100:
        res += "C"
        decimal -= 100
    if decimal >= 90:
        res += "XC"
        decimal -= 90
    while decimal >= 50:
        res += "L"
        decimal -= 50
    if decimal >= 40:
        res += "XL"
        decimal -= 40
    while decimal >= 10:
        res += "X"
        decimal -= 10
    if decimal >= 9:
        res += "IX"
        decimal -= 9
    while decimal >= 5:
        res += "V"
        decimal -= 5
    if decimal >= 4:
        res +="IV"
        decimal -= 4
    while decimal >= 1:
        res += "I"
        decimal -= 1
    return res

if __name__ == "__main__":
    num = int(input())
    print(to_roman(num))
    os.system("pause")