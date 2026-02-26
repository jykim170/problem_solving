arr = [[0] * 102 for _ in range(102)]

t = int(input())

for _ in range(t):
    x, y = map(int , input().split())
    for i in range(y, y+10):
        arr[i][x:x+10] = [1] * 10
        
ans = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            if arr[i-1][j] == 0: ans += 1
            if arr[i+1][j] == 0: ans += 1
            if arr[i][j-1] == 0: ans += 1
            if arr[i][j+1] == 0: ans += 1
            
print(ans)
            