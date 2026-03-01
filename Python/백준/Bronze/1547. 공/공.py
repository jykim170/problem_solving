m = int(input())
a = [0, 1, 0, 0] # 1,2,3 번만 쓸거고, 1번에 미리 넣어 놓을 거임
for _ in range(m):
    x, y = map(int, input().split())
    a[x], a[y] = a[y], a[x]

print(a.index(1))

