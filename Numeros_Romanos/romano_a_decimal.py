def from_roman(roman):
    romanValues = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    value = []
    res = 0
    for c in roman:
        value.append(c)
    if len(value) > 1:
        cont = 0
        while cont != len(value):
            if cont != len(value) - 1:
                if romanValues[value[cont]] < romanValues[value[cont + 1]]:
                    res += romanValues[value[cont + 1]] - romanValues[value[cont]]
                    cont += 2
                else:
                    res += romanValues[value[cont]]
                    cont += 1
            else:
                res += romanValues[value[cont]]
                cont += 1
    else:
        res += romanValues[value[0]]
    return res