import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    sy, sx = 0, 0
    n = int(input())
    box = [[0] * n for _ in range(n)] # 일단 박스를 만들자
    # 그리고 box의 좌표에 해당하는 숫자를 놓아 줘야 된다.
    # while 문 돌면서 n 에 도착하거나 아니면 이미 숫자가 들어있으면 방향 바꾸기 어떰
    direction = 'E'
    plus = 1
    while True:
        if box[sy][sx] == 0:
            box[sy][sx] = plus
        plus += 1
        if direction == 'E':
            if sx < n-1 and box[sy][sx+1] == 0: # 그 다음에 막혀있다는걸 표현 즉 끝이거나(이게 n 이겟지?) 이미 차 있거나
                        # 근데 차있다는 걸 표현하는게 인덱스로 0이 아니라는건데.. 
                sx += 1
            else:
                direction = 'S'
        
        if direction == 'S':
            if sy < n-1 and box[sy+1][sx] == 0:
                sy += 1
            else:
                direction = 'W'
        
        if direction == 'W':
            if sx > 0 and box[sy][sx-1] == 0:
                sx -= 1
            else:
                direction = 'N'

        if direction == 'N':
            if sy > 0 and box[sy-1][sx] == 0:
                sy -= 1
            else:
                direction = 'E'
                sx += 1                
        
        if plus > n**2:
            break
    
    print(f'#{tc}')
    for i in box:
        print(*i)                