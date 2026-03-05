t = int(input())

for _ in range(t):
    s = input()
    b = len(s)//2
    a = b - 1
    
    if s[a] == s[b] :
        print('Do-it')
    else:
        print('Do-it-Not')    
            