import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

sizes = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            sizes.append(bfs(i, j))

sizes.sort()
print(len(sizes))
for s in sizes:
    print(s)