def dfs(idx):
    if idx == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            arr[idx] = i
            dfs(idx+1)
            visited[i] = False
    
n, m = map(int, input().split())
arr = [0] * m
visited = [False] * (n+1)

dfs(0)