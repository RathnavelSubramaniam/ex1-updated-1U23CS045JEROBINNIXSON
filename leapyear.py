def leapyear(year):
    if year%4 == 0:
        return "Leap year"
    else:
        return "Not leap year"
print(leapyear(2006))