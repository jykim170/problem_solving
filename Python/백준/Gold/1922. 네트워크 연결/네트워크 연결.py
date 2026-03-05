import sys
sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결할 수 있는 선의 수

parent = [i for i in range(n+1)]

road = []
for _ in range(m):
    a, b, c = map(int, input().split())
    road.append((c, a, b))

road.sort()
answer = 0

for row in road:
    cost, first, second= row
    if find_parent(parent, first) != find_parent(parent, second):    
        union_parent(parent, first, second)
        answer += cost
    
print(answer)