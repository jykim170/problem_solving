h, m = map(int, input().split())

whole = 60 * h + m

whole += (60 - 45)

ah = (whole // 60) - 1
if ah < 0: 
    ah = 23
am = whole % 60
print(ah, am)

