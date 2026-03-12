import sys, heapq
input = sys.stdin.readline
# 이건 사실 
# input() 이걸 sys.stdin.readline() 이걸로
# 바꿔주는겁니다 빨리 받아오는
# cheat key
n = int(input()) # 이 만큼 입력

h = [] # 힙리스트
for _ in range(n): 
    heapq.heappush(h, int(input()))
    # 자 이까지의 과정을 통해서 우리는
    # 힙리스트를 만들어줬습니다
    
    # 오케잉 이제 요리하자

# 아까 1번개념 하나만들때까지 계속합쳐준다
#  len(1) 될때까지 반복문

calcul = 0 # 연산횟수입니다.
while len(h) > 1: # 1보다크면 계속
    #2. 작은값 두개빼서 더해준다
    # 작은값빼는법? => 힙~
    
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    calcul += a+b # 연산 일어난거 더해줍니다
    #괜찮으시죠 ?
    
    #이제 작은값 두개 뺏으니 더해서 하나
    #로 만들어주죠 ? # 자 
    # 아까 예시로 보면 a = 10
    # b = 20 이죠 그럼 연산 10 +20 일어낫죠 
    heapq.heappush(h, a+b)
    # 그다음 2개 뽑아서 1개넣어줫음
    
# 이제 마지막에 그럼 연산 몇번 일어낫는지 
#출력
print(calcul)