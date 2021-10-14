import os

def binToDec(binNum):
    binary = str(binNum)[::-1]
    i = 0
    res = 0
    for n in binary:
        res += int(n) * pow(2, i)
        i += 1
    return res

if __name__ == "__main__":
    num = int(input())
    print(binToDec(num))
    os.system("pause")