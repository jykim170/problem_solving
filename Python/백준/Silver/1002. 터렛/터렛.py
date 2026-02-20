import math
t = int(input())

for _ in range(t):
    # 원의 중심과 반지름 이라고 생각하자
    x1, y1, r1, x2, y2, r2 = map(int, input().split())  
    
    # 두 점 사이의 거리 d
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    # 두 점 사이의 거리가 0 (같고) , 반지름이 같을 때 =>> 완전히 같을 때
    if d == 0 and r1 == r2:
        print(-1)
    elif d == r1+r2: # 바깥에서 접할때 oo
        print(1)
    elif d == abs(r1-r2): # 안에서 접할 때
        print(1)
    elif abs(r1-r2) < d < r1+r2:
        print(2)
    elif d < abs(r1-r2) or d > r1+r2: # 안에서 안만날때와 바깥에서 안만날때
        print(0)
