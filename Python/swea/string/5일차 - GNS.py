import sys
sys.stdin = open("input.txt", "r")

t = int(input())

dic = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, 
       "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

for tc in range(1, t+1):
    a, b = input().split()
    arr = list(input().split())
    result = sorted(arr, key = lambda x: dic.get(x, 10**9))
    print(f'#{tc}')
    print(*result)