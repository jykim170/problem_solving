c = int(input())

for i in range(c):
    n = list(map(int, input().split()))
    score = n[1:]
    avg = sum(score)/n[0]
    cnt = 0
    for p in score:
        if avg < p:
            cnt += 1
    result = cnt / n[0] * 100
    print(f'{result:0.3f}%')