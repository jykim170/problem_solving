t = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    y, x = 0, 0
    d = 0 
    num = 1
    
    while num <= n*n:
        arr[y][x] = num
        
        if num == n*n:
            break
        
        ny = y + dy[d]
        nx = x + dx[d]
        
        if not (0 <= ny < n and 0 <= nx < n) or arr[ny][nx] != 0:
            d = (d + 1) % 4
            ny = y  +dy[d]
            nx = x + dx[d]

        arr[ny][nx] = num
        num += 1
        y, x = ny, nx
    
    print(arr)