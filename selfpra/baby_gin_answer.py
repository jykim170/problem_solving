import sys
sys.stdin = open("input.txt", "r")

path = []               # 경로
used = [0] * 6       # 카드 사용 유무
result = False        # 전체 결과

# 1. 전체 순열을 먼저 구현
# - 종료조건 : 6개의 카드를 모두 줄 세우면 종료 (depth = 6)
# - 재귀호출 : 6개의 코드 (branch = 6)
# - 중복을 제거해줘야 한다.

# 2. baby-gin 검사
def is_baby_gin():
    cnt = 0
    
    # 앞의 3개 숫자
    # - run + triplet 비교
    a, b, c = path[0], path[1], path[2]
    if a == b == c :                # triplet
        cnt += 1
    elif a == (b-1) == (c-2):       # run
        cnt += 1
        
    # 뒤의 3개 숫자
    # - run + triplet 비교
    a, b, c = path[3], path[4], path[5]
    if a == b == c:
        cnt += 1
    elif a == (b-1) == (c-2) :
        cnt += 1
    
    return cnt == 2
    
def recur(cnt):
    global result
    
    if cnt == 6:
        # print(*path)
        if is_baby_gin():
            result = True
        return
    
    for i in range(6):
        if used[i]:
            continue
        
        used[i] = 1 # 사용 체크
        path.append(arr[i])
        recur(cnt + 1)
        path.pop()
        used[i] = 0 # 초기화

arr = list(map(int, input().split()))
recur(0)


print(result)