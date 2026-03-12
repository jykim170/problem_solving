def dfs(idx):
    if idx == m:
        print(*arr)
        return    

    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = True
            arr[idx] = i
            dfs(idx + 1)
            visited[i] = False

n, m = map(int, input().split())
arr = [0] * m 
visited =[0] * (n+1)

dfs(0)