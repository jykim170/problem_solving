import sys
input = sys.stdin.readline

n = int(input())
target = int(input())

arr = [[0]*n for _ in range(n)]

x = y = n//2
arr[x][y] = 1

num = 2
step = 1

dirs = [(-1,0),(0,1),(1,0),(0,-1)]  # 위 오른쪽 아래 왼쪽

tx, ty = x, y
if target == 1:
    tx, ty = x, y

while num <= n*n:
    for d in range(4):
        dx, dy = dirs[d]
        for _ in range(step):
            if num > n*n:
                break
            x += dx
            y += dy
            arr[x][y] = num
            if num == target:
                tx, ty = x, y
            num += 1
        if d % 2 == 1:
            step += 1

for row in arr:
    print(*row)

print(tx+1, ty+1)