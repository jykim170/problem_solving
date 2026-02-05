import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    h = list(map(int, input().split()))
    
    answer = 0
    
    for i in range(2, N - 2):
        left1 = h[i - 1]
        left2 = h[i - 2]
        right1 = h[i + 1]
        right2 = h[i + 2]
        
        limit = max(left1, left2, right1, right2)
        
        if h[i] > limit:
            answer += h[i] - limit
    
    print(f"#{tc} {answer}")
