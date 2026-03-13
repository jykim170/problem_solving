# 완전탐색 문제 2. 연속 3장의 트럼프 카드
    # A, J, Q, K 네 종류의 카드들이 충분히 있음
    # 이 중, 5 장의 카드를 뽑아 나열
    
    # 같은 종류의 카드가 세 장 연속으로 나오는 경우의 수는?
   
   
card = ['A', 'J', 'Q', 'K'] 
path = []
cnt = 0
# 일단 5장을 뽑는 코드를 짜자
def choice(x):
    global cnt
    # 시작
    # 끝
    if x == 5:
        cnt += cnt_three(path)
        return 
    # 누적된 값
    for i in range(4):
        path.append(card[i])
        choice(x+1)
        path.pop()
        
def cnt_three(card_list):
    if card_list[0] == card_list[1] == card_list[2]: 
        return 1
    elif card_list[1] == card_list[2] == card_list[3]:
        return 1
    elif card_list[2] == card_list[3] == card_list[4]:
        return 1
    
    return 0
    

choice(0)
print(cnt)