# 내가 가진 경건한 파리채는 십자가 모양임
import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_kill = 0
    l_y, l_x = 0, 0
    kill_range = [-1, 0, 1]
    for sy in range(n): #시작 (0, 0) 부터 돌자
        for sx in range(n):
            kill = 0
            for i in kill_range: # 0이 중복으로 들어가니까 한 번빼주자
                if 0 <= sy + i < n:
                    kill += box[sy+i][sx]
                if 0 <= sx + i < n:
                    kill += box[sy][sx+i]
            kill -= box[sy][sx]
            if kill > max_kill:
                max_kill = kill
                l_y = sy
                l_x = sx

    print(f'#{tc} {max_kill} {l_y} {l_x}')
