import sys
sys.stdin = open("input.txt", "r")

# 1. 입력
N = int(input())
# 한 줄씩 입력 받기
# for tc in range(1, N+1):
#     arr = list(map(int, input().split()))

# 여러 줄 입력 받기
arr = [list(map(int, input().split())) for _ in range(N)]

# 2. 가로부터 접근
# for y in range(5):
#     for x in range(5):
#         # print(y, x, end = ' ')
#         print(arr[y][x], end = ' ')
#     print()
# 3. 세로부터 접근
# for x in range(5):
#     for y in range(5):
#         print(arr[y][x], end= ' ')
#     print()
# 4. 대각선 접근
# 4.1 우하단 대각선 (\)
# for x in range(5):
#     print(arr[x][x], end= ' ')
# print()
# 4.2 좌하단 대각선 (/)
# for x in range(5):
#     print(arr[x][5-1-x], end = ' ')
# print()
# 5. 범위 접근
# - 3*3 사각형 범위값들을 한 번에 접근
# - 예시) 합이 가장 큰 3*3 범위 값을 구하여라 

totals = []


length = 5
scale = 3
# sy, sx = 0, 0
for sy in range(length - scale + 1):
    for sx in range(length - scale + 1):
        total = 0
        for y in range(sy, sy+scale):       # 출발지 ~ 출발지 + scale
            for x in range(sx, sx+scale):   
                total += arr[y][x]
        totals.append(total)
print(totals)

max_total = 0
max_y, max_x = 0, 0 
for sy in range(5):
    for sx in range(5):
        total = 0
        for y in range(sy, sy+3):
            for x in range(sx, sx+3):
                if y > 4 or y < 0 or x > 4 or x < 0:
                    continue
                total += arr[y][x]
                if total > max_total:
                    max_total = total
                    max_y, max_x = sy, sx
                # max_total = max(max_total, total)

print(max_total)
print(max_y,max_x)

sy, sx = 0, 3 # 계산하고자 하는 출발지
for y in range(sy, sy+3):
    for x in range(sx, sx+3):
        # 범위 밖 계산
        if y > 4 or y < 0 or x > 4 or x < 0:
            continue

        # 범위 안 계산
        if 0 <= y <= 4 and 0 <= x <= 4:
            total += arr[y][x]


# t = int(input())

# for tc in range(1, t+1):
#     arr = list(map(int, input().split()))
#     req_num = int(input())
