# [주의] 시험, 채점 사이트 제출할 때는 반드시 주석처리
import sys
# 우리 시스템의 표준 입력을 파일 입력으로 바꾸겠다.
sys.stdin = open("input.txt", "r")

t = int(input())

s = [2, 3, 5, 7, 11]

for tc in range(1, t+1):
    result = [0] * 5
    n = int(input())
    
    for i in range(5):
        while n % s[i] == 0:
            n = n // s[i]
            result[i] += 1
    
    print(f'#{tc}', *result)