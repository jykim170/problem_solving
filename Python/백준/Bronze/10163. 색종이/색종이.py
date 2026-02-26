arr = [[0] * 1001 for _ in range(1001)]

t = int(input())
for tc in range(1, t+1):
    
    x, y, w, h = map(int, input().split())
    for i in range(y, y+h):
        for j in range(x, x + w):
            arr[i][j] = tc

ans = [0] * (t+1)

for ar in arr:
    for a in ar:
        ans[a] += 1
        
print(*ans[1:], sep ='\n')