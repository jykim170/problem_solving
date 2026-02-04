import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    # 그냥 완전탐색으로 푸는게 더 쉬운 문제 아닌가 이거?
    box = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    # 0 이면 검정색, 1이면 하얀색

    # 일단 가로 탐색 부터 하자
    for i in range(n):
        # box[i]를 깔아놓고 연속한 수 
        streak = 0
        for j in box[i]:
            if j == 1:
                streak += 1
            else: # j == 0







    # for i in range(n):
    #     for j in range(n):
    #         print(box[i][j])