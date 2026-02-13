# ##3
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# import sys
# sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")

# from collections import deque            # BFS에서 큐(deque) 사용

# N, M, V = map(int, input().split())      # N: 정점 개수, M: 간선 개수, V: 시작 정점

# graph = [[] for _ in range(N + 1)]       # 1번~N번까지 인접 리스트(0번은 안 씀)

# for _ in range(M):                       # 간선 M개 입력 받기
#     a, b = map(int, input().split())     # 간선 정보: a, b
#     graph[a].append(b)                   # a에 b 연결 추가
#     graph[b].append(a)

# for i in range(1, N+1):
#     graph[i].sort()

# dfs_visited = [0] * (N + 1)

# def dfs(u):
#     dfs_visited[u] = 1
#     print(u, end = ' ')

#     for v in graph[u]:
#         if dfs_visited[v]:
#             continue
#         dfs(v)

# bfs_visited = [0] * (N + 1)

# def bfs(start):
#     dq = deque([start])
#     bfs_visited[start] = 1

#     while dq:
#         u = dq.popleft()
#         print(u, end = ' ')

#         for v in graph[u]:
#             if bfs_visited[v]:
#                 continue
#             bfs_visited[v] = 1
#             dq.append(v) 

# dfs(V)

# print()

# bfs(V)
import sys
sys.setrecursionlimit(10**6)
from collections import deque


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs_visited = [0] * (N+1)

def dfs(u):
    dfs_visited[u] = 1
    print(u, end= ' ')



bfs_visited = [0] * (N+1)