# 연속 3개 run
# 같은 3개 triplet
# cnt 횟수로 비교 하면 될 듯 숫자올려서
# 0 에서 9까지인 숫자 카드 4세트를 섞은 후
# 6개인 카드 
# 근데 그 전에 끝나는 경우는 ?
import sys
sys.stdin = open("input.txt", "r")

def is_baby_gin(player):
    # run
    for i in range(8):
        if player[i] >= 1 and player[i+1] >= 1 and player[i+2] >= 1:
            return True
    # triplet 
    for i in range(10):
        if player[i] == 3:
            return True        

    return False


t = int(input())

for tc in range(1, t+1):
    result = 0

    arr = list(map(int, input().split()))
    
    player1 = [0] * 10
    player2 = [0] * 10
    
    for i in range(len(arr)):
        card = arr[i]
        
        if i % 2 == 0:
            player1[card] += 1
            if i >= 4 and is_baby_gin(player1):
                result = 1
                break
        else:
            player2[card] += 1
            if i >= 5 and is_baby_gin(player2):
                result = 2
                break
    
    print(f'#{tc} {result}')