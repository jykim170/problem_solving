import sys
sys.stdin = open("input.txt", "r")

# input 받을 때 strip 사용
# 맨 오른쪽의 '#' 을 찾으면 되네
# '#' 찾으면 거기 ans로 두고 거기부터 오른쪽으로 또 찾아보기 

def binary(arr):
    left = 0
    right = len(arr) - 1
    ans = -1
    
    while left <= right:
        mid = (left+right) // 2
        
        if arr[mid] == '#':
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ans
    
t = int(input())

for tc in range(1, t+1):
    arr = input().strip()
    result = binary(arr) + 1
    
    print(f'#{tc} {(result*100)//len(arr)}%')    