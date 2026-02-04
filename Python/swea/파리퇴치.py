import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    dy = [i for i in range(m)] # 0 ~ m-1
    dx = [i for i in range(m)] 
    # sy, sx (0, 0) 부터 돈다.
    result = 0
    for sy in range(n):
        for sx in range(n):
            total_kill = 0

            for i in range(m):
                for j in range(m):
                    new_y = sy + dy[i]
                    new_x = sx + dx[j]
                    if new_y < 0 or new_y >= n or new_x < 0 or new_x >= n:
                        continue
                    total_kill += box[new_y][new_x]
            result = max(result, total_kill)
    print(f'#{tc} {result}')