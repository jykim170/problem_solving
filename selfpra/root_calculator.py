# import sys
# sys.stdin = open("input.txt", "r")

# 루트 값의 정수 부분 구하기 ?

def bin(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > n:
            right = mid - 1 
        else:
            left = mid + 1

    return left
            
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    result = bin(n)
    result = int(result)
    print(f'#{tc} {result}')