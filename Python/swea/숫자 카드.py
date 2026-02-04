# [주의] 시험, 채점 사이트 제출할 때는 반드시 주석처리
import sys
# 우리 시스템의 표준 입력을 파일 입력으로 바꾸겠다.
sys.stdin = open("input.txt", "r")


t = int(input())

# 카드 수 카운팅 배열 선언
# 카운팅
# 가장 많은 카드 구하기

for tc in range(1, t+1):
    box = [0] * 10
    n = int(input())
    s = list(map(int, list(input()))) # 한글자씩 나누고 다시 int로 저장하자
    for i in s:
        box[i] += 1
    max_num = 0
    for j in range(9, -1, -1):
        if box[j] > max_num:
            max_num = box[j]
            result_index = j
    print(f'#{tc} {result_index} {box[result_index]}')