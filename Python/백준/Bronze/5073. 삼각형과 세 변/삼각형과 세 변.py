while True:
    a, b, c = map(int, input().split())
    
    d = [a, b, c]
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if max(d) >= sum(d) - max(d):
        print('Invalid')
        continue
    
    if a == b == c:
        print('Equilateral')
        continue

    if len(set(d)) == 2:
        print('Isosceles')
        continue
    
    print('Scalene')