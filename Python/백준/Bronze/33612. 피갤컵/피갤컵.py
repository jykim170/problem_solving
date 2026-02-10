y = 2024
m = 1

n = int(input())

m += 7 * n
y += m // 13

m = m % 12
if m == 0:
    m = 12

print(y, m)