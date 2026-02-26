import sys
input = sys.stdin.readline

arr = [[0] * 1001 for _ in range(1001)]

t = int(input())
max_x = 0
max_y = 0

for tc in range(1, t + 1):
    x, y, w, h = map(int, input().split())
    max_x = max(max_x, x + w)
    max_y = max(max_y, y + h)

    # 한 칸씩 말고, 한 줄씩 슬라이싱으로 덮어쓰기 (훨씬 빠름)
    for i in range(y, y + h):
        arr[i][x:x + w] = [tc] * w

ans = [0] * (t + 1)

# 전체 1001x1001 말고 실제로 칠해진 범위까지만 스캔
for i in range(max_y):
    row = arr[i]
    for v in row[:max_x]:
        if v:              # 0은 스킵 (조금 더 빠름)
            ans[v] += 1

print(*ans[1:], sep='\n')