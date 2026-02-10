n, m = map(int, input().split())

arr = [0] * (n+1)

for _ in range(m):
    i, j, k = map(int, input().split())

    for l in range(i-1, j):
        arr[l] = k

print(*arr[:n])