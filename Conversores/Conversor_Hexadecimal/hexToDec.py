import os

def hexToDec(hexNum):
    codes = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'a' : 10,
        'b' : 11,
        'c' : 12,
        'd' : 13,
        'e' : 14,
        'f' : 15
    }
    res = 0
    digits = {}
    for i in range(len(hexNum)):
        digits[i] = hexNum.lower()[::-1][i]
    for digit in digits:
        res += codes[digits[digit]] * 16 ** digit
    return res

if __name__ == "__main__":
    num = str(input())
    print(hexToDec(num))
    os.system("pause")