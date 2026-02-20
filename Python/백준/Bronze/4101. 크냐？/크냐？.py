while True:
    o, t = map(int, input().split())
    if o == 0 and t == 0:
        break
    if o > t :
        print('Yes')
    else:
        print('No')