import sys
input = sys.stdin.readline
import heapq

n, e = map(int, input().split())
k = int(input())

arr = [[] for _ in range(n+1)]
    
for _ in range(e):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))
    
INF = 10**15
dist = [INF] * (n+1)

dist[k] = 0
pq = [(0, k)]

while pq:
    cur_cost, loc = heapq.heappop(pq)
    if cur_cost > dist[loc]:
        continue
    
    for al, ac in arr[loc]:
        new_cost = cur_cost + ac
        
        if new_cost < dist[al]:
            dist[al] = new_cost
            heapq.heappush(pq, (new_cost, al))

for i in range(1, len(dist)):
    if dist[i] == 10**15:
        print('INF')
    else:
        print(dist[i])
    