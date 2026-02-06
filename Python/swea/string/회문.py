import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    w = list(input())
    length = len(w) ## 10
# 10개면 (짝수면)
# A B C D E // E D C B A            n // 2 == 5 
# 0 1 2 3 4 // 5 6 7 8 9

# 홀수면 ? 
# A B C D //E// D C B A             n // 2 == 4
# 0 1 2 3 //4// 5 6 7 8
    cutting = length // 2    
    front = w[:cutting]

    if length % 2 == 1:
        back = w[cutting+1:] 
    else:
        back = w[cutting:]
    
    back_reversed = back[::-1]

    if front == back_reversed:
        result = 1
    else:
        result = 0

    print(f'#{tc}', result)