for _ in range(3):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    ans = sum(a)
    if ans > 0:
        print('+')
    elif ans == 0 :
        print(0)
    else:
        print('-')