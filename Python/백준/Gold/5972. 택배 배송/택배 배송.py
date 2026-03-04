import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, graph, n):
    INF = 10**15
    dist = [INF] * (n+1)
    
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        cur_cost, nc = heapq.heappop(pq)
        if cur_cost > dist[nc]:
            continue
        for v, w in graph[nc]:
            new_cost = cur_cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    
    return dist

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)] # n 개의 헛간
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

ans = dijkstra(1, arr, n)
print(ans[n])