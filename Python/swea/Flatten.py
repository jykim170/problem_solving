# [주의] 시험, 채점 사이트 제출할 때는 반드시 주석처리
import sys
# 우리 시스템의 표준 입력을 파일 입력으로 바꾸겠다.
sys.stdin = open("input.txt", "r")


# 가로 길이는 100임

for tc in range(1, 11):
    dump_num = int(input()) 
    heights = list(map(int, input().split())) # 0 ~ 99 인덱스 // 총 100개
# max, min를 사용하면 시간복잡도가 높아질 것 같긴한데..
# 그때그때 가장 높은 층을 1 깎고, 그때그때 가장 낮은 층에 1을 쌓아야 됨.
# 그리고 dump 가 끝난 후 가장 높은 층과, 가장 아랫층 과의 차이는 몇 층인가 ?
    for i in range(dump_num):
        high = max(heights)
        low = min(heights)
        if high - low <= 1:
            print(high - low)
            break # 더 이상 평탄화가 필요없다면, 그대로 출력하고 그만두기

        for j in range(100): # 제일 높은 곳 발견하면 거기서 1 깎고 멈추기
            if high == heights[j]:
                heights[j] -= 1
                break 

        for k in range(100): # 제일 낮은 곳 발견하면 거기서 1 쌓고 멈추기
            if low == heights[k]:
                heights[k] += 1
                break
    
    print(f'#{tc} {max(heights) - min(heights)}')