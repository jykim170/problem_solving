import heapq
 
t = int(input()) # 테케
 
for tc in range(1, t+1):
    n, m = map(int, input().split()) # 정점의 수, 간선의 수
    arr = [[] for _ in range(n)]
 
    for _ in range(m):
        a, b, w = map(int, input().split())
        arr[a].append((b, w)) # a에서 b 로 가는데 w 만큼 cost 듬
         
    # 0에서 시작해서 N-1 노드에 도착해야함
    INF = 10**15
    dist = [INF] * n
     
    dist[0] = 0
    pq = [(0, 0)]
     
    while pq:
        cur_cost, nc = heapq.heappop(pq)
        if cur_cost > dist[nc]:
            continue
        for v, w in arr[nc]:
            new_cost = cur_cost + w 
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
     
    if dist[n-1] == INF:
        print(f'#{tc} impossible')
    else:
        print(f'#{tc} {dist[n-1]}')
        
        