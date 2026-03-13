def is_baby_gin(player):
    #run
    for i in range(10):
        if player[i] >= 3:
            return True
    
    for i in range(8):
        if player[i] >= 1 and player[i+1] >= 1 and player[i+2] >= 1:
            return True
    
    return False

t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    result = 0
    
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