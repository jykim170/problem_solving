arr = [[0] * 100 for _ in range(100)]
# y, x 
s = 0
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    # 가로 세로가 각 10 인 정사각형

    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] = 1

for ar in arr:
    s += sum(ar)

print(s)