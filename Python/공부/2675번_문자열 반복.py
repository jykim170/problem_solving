# [주의] 시험, 채점 사이트 제출할 때는 반드시 주석처리
import sys
# 우리 시스템의 표준 입력을 파일 입력으로 바꾸겠다.
sys.stdin = open("input.txt", "r")

t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    for i in s:
        for _ in range(r):
            print(i, end='')
    print()