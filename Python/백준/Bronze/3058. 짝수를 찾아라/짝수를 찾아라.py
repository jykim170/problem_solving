t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)

    print(sum(even), min(even))