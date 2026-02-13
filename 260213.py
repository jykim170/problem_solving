import sys
sys.stdin = open("input.txt", "r")

# 그래프 자료구조의 시작은, 인접 행렬과 인접 리스트
from collections import deque

N, M = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start) # 양방향 그래프


def bfs(start):
    # 초기화 과정이 필요하다. 아래 2가지 과정
    dq = deque([start])

    visited = [0] * (N + 1)
    visited[start] = 1

    while dq:
        now = dq.popleft()
        # visited[now] = 1 여기에 하면 중복될 수 있다.
        print(now, end= ' ')

        for next_node in graph[now]:
            # 이미 방문한 노드면 continue
            if visited[next_node]:
                continue

            visited[next_node] = 1 # 후보군으로 등록하면서, 바로 방문처리
            dq.append(next_node)

bfs(1)