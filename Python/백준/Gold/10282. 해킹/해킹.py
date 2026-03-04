import sys
import heapq

input = sys.stdin.readline

t = int(input())

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
    
for tc in range(1, t+1):
    n, d, c = map(int, input().split()) # 컴퓨터 n개, 의존성 개수 d, 해킹당한 컴 c 
    arr = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        # 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간
        arr[b].append((a, s))
        pass
    ans = dijkstra(c, arr, n)
    cnt = 0
    last = 0
    for i in range(1, len(ans)):
        if ans[i] != 10**15:
            cnt +=1 
            if ans[i] > last:
                last = ans[i]
    
    print(cnt, last)
            