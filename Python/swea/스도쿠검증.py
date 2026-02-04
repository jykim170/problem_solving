import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 검증 기본 값 (set으로 길이 할까..? 아니면 합? 둘다 예외가 있을 수도)
    answer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    check = True
    
    # 일단 가로 검증
    for i in range(9):
        comparison = sorted(arr[i])
        if answer != comparison:
            check = False
            continue
    
    # 세로 검증 

    for i in range(9):
        comparison_length = []
        for j in range(9):
            comparison_length.append(arr[j][i])
        comparison_length = sorted(comparison_length)
        if answer != comparison_length:
            check = False
            continue
    
    # 네모 박스 검증
    dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    for sy in range(0, 9, 3):
        for sx in range(0, 9, 3):
            temp = []
            for i in range(9):
                new_y = sy + dy[i]
                new_x = sx + dx[i]
                if new_y < 0 or new_y >= 9 or new_x < 0 or new_x >= 9:
                    continue
                temp.append(arr[new_y][new_x])
            comp_temp = sorted(temp)
            if answer != comp_temp:
                check = False
                continue
    
    if check:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')