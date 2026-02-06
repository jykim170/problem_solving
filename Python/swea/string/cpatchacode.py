import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))


    check = -1 
    answer = 1

    for i in passcode:
        try:
            check = sample.index(i, check+1)
        except:
            answer = 0
            break

    print(f'#{tc}', answer)
    
    