import sys
input = sys.stdin.readline

n = int(input())

target = int(input())

arr = [[0] * n for _ in range(n)]

y = x = n//2
arr[y][x] = 1

num = 2
step = 1

# 상 우 하 좌

dy = [-1, 0 , 1 , 0]
dx = [0, 1, 0, -1]

while num <= n*n:
    for d in range(4):
        
        for _ in range(step):
            
            if num > n*n:
                break
            
            y += dy[d]
            x += dx[d]

            arr[y][x] = num
            
            if num == target:
                ty = y
                tx = x
            
            num += 1
        
        if d % 2 == 1:
            step += 1
            
    
for row in arr:
    print(*row)

print(ty+1, tx+1)

