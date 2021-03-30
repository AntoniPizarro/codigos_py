import os

def toSeg(years, months, days, hours, minutes, seconds):
    yearSec = years * 3600 * 24 * 30 * 12
    monthSec = months * 3600 * 24 * (6 * 31 + 5 * 30 + 28) / 12
    daySec = days * 3600 * 24
    hourSec = hours * 3600
    minSec = minutes * 60
    sec = seconds
    res = yearSec + monthSec + daySec + hourSec + minSec + sec
    return res

if __name__ == "__main__":
    years = int(input("years: "))
    months = int(input("months: "))
    days = int(input("days: "))
    hours = int(input("hours: "))
    minutes = int(input("minutes: "))
    seconds = int(input("seconds: "))
    print(toSeg(years, months, days, hours, minutes, seconds))
    os.system("pause")