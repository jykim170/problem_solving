import heapq

n = int(input())
m = int(input())
city_arr = [[] for _ in range(n+1)]

for _ in range(m):
    sc, ac, cost = map(int, input().split())
    city_arr[sc].append((ac, cost))

gsc, gac = map(int, input().split())

INF = 10**15
dist = [INF] * (n+1)

dist[gsc] = 0

pq = [(0, gsc)]

while pq:
    cur_cost, nac = heapq.heappop(pq)
    
    if cur_cost > dist[nac]:
        continue
    
    for ncity, pcost in city_arr[nac]:
        new_cost = cur_cost + pcost
        if new_cost < dist[ncity]:
            dist[ncity] = new_cost
            heapq.heappush(pq, (new_cost, ncity))

print(dist[gac])