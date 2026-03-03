from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    
    while q:
        y, x = q.popleft()
        
        if y == n- 1 and x == m-1:
            return visited[y][x]
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if  0 <= ny < n and 0<= nx < m:
                if visited[ny][nx] ==0 and arr[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] +1
                    q.append((ny, nx))
                    
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

print(bfs())