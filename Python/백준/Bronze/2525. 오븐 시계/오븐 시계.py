h, m = map(int, input().split())
c = int(input())

whole = 60 * h + m
whole += c

if whole >= 1440: 
    whole -= 1440

ah = whole // 60
am = whole % 60
print(ah, am)

