# [주의] 시험, 채점 사이트 제출할 때는 반드시 주석처리
import sys
# 우리 시스템의 표준 입력을 파일 입력으로 바꾸겠다.
sys.stdin = open("input.txt", "r")

t = int(input())


for tc in range(1, t+1):
    k = int(input()) # A 카운트 이 갯수만큼 자를 수 있음
    s = input()
    a_index = []
    for i in range(len(s)):
        if s[i] == 'A':
            a_index.append(i)
    result = 0
    # K개의 'A'를 포함하는 구간을 못 찾는 경우!
    if len(a_index) < k :
        print(f'#{tc} {result}')
        continue
    
    c = []
    for j in range(len(a_index)-k+1):
        start_index = a_index[j] # 스타트 인덱스
        end_index = a_index[j+k-1] # 끝나는 인덱스
        c.append(end_index-start_index)
    print(f'#{tc} {max(c)}')
