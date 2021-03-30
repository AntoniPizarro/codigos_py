import os

def toMin(years, months, days, hours, minutes, seconds):
    yearMin = years * 60 * 24 * 30 * 12
    monthMin = months * 60 * 24 * (6 * 31 + 5 * 30 + 28) / 12
    dayMin = days * 60 * 24
    hourMin = hours * 60
    minu = minutes
    secMin = seconds / 60
    res = yearMin + monthMin + dayMin + hourMin + minu + secMin
    return res

if __name__ == "__main__":
    years = int(input("years: "))
    months = int(input("months: "))
    days = int(input("days: "))
    hours = int(input("hours: "))
    minutes = int(input("minutes: "))
    seconds = int(input("seconds: "))
    print(toMin(years, months, days, hours, minutes, seconds))
    os.system("pause")