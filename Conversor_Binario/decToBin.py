def decToBin(decNum):
    decimal = decNum
    res = ""
    while decimal > 0:
        res += str(decimal % 2)
        decimal = int(decimal / 2)
    return res[::-1]