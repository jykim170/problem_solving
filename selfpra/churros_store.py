import sys
sys.stdin = open("input.txt", "r")

def how(arr):
    left = 1
    right = max(arr)
    answer = 0
    
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        
        for chu in arr:
            cnt += chu // mid
            
        if cnt >= k:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer
        
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    churros = [int(input()) for _ in range(n)]
    print(f'#{tc} {how(churros)}')