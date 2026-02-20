n = int(input())
ys = 0
ms = 0
a = list(map(int, input().split()))
for i in a:
    ys += ((i // 30)+1) * 10
    ms += ((i // 60)+1) * 15

if ys<ms:
    print('Y', ys)
elif ys == ms:
    print('Y M', ys)
else:
    print('M', ms)