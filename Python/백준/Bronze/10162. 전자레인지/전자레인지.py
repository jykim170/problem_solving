t = int(input())
change = [300, 60, 10] # 다 배수이기 때문에

result = [0, 0, 0]
for i in range(len(change)):
    mod = change[i]
    result[i] = t // mod
    t = t % mod

if t == 0:
    print(*result)
else:
    print(-1)