t = int(input())

for tc in range(1, t+1):
    n = int(input())
    c_l = list(map(int, input().split()))
    p = int(input())
    delta = [0] * len(c_l)
    now_delta = 0
    for i in range(p):
        s, e, c = map(int, input().split())
        delta[s] += c
        if e+1 < len(c_l):
            delta[e+1] -= c
    for j in range(len(delta)):
        now_delta += delta[j]
        c_l[j] += now_delta
    
    print(f'#{tc}', *c_l)