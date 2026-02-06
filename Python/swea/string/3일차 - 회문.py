import sys
sys.stdin = open("input.txt", "r")

t = int(input()) # 10개면 (짝수면)
# A B C D E // E D C B A            n // 2 == 5 
# 0 1 2 3 4 // 5 6 7 8 9

# 홀수면 ? 
# A B C D //E// D C B A             n // 2 == 4
# 0 1 2 3 //4// 5 6 7 8

for tc in range(1, t+1):    
    n, m = map(int, input().split())
    # 입력부터 받고  n * n 의 배열판
    arr = [list(input()) for _ in range(n)]
    # 우린 m 짜리의 회문을 찾을거야.
    # m 이 홀수 일때 // m 이 짝수 일때 다르겠지 ?
    # 일단 m 이 홀수 일때 먼저 가정을 해볼까 ? cutting_line 잡아주자
    cutting_line = m // 2
    if m % 2 == 1:
        cut_front = cutting_line
        cut_back = cutting_line+1 # 그리고, m은 빼고, [:m] 앞부분, [m+1:] 뒷부분 비교 하면 되겠다. (뒤집어서)
    else:
        cut_front = cutting_line # 짝수일때는 위에 경우니까. [:m] 앞부분, [m:] 뒷부분 즉 같은 값!
        cut_back = cutting_line
    
    # 전체 길이가 10일때 5짜리 회문을 돌린다고 가정을 해볼까?
    # A B C D E E D C B A 이거에서.
    # 0 1 2 3 4 5 6 7 8 9
    # [5:] 까지 index 에러 안나게 할 수 있는데 이걸 수치화 하면 n-m 이겠네 n-m 하고 
    # for i in range(n-m): 이렇게 하면 0, 1, 2, 3, 4 되겠다.
    # 짝수일때도 같으니까 넘어가자

    #n == m 인 경우도 있어서
    if n == m:
        length = 1
    else:
        length = n-m

    # 가로 검사 먼저 해보자! 
    for i in arr: # 가로줄
        for s in range(length):
            # s는 start 포인트 ,  
            front = arr[s:s+cut_front]
            back = arr[s+cut_back:s+length]            


    


