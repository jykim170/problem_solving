import sys, heapq
input = sys.stdin.readline

# n 장을 갖고 있다. i 번 카드엔 a i 가 쓰여있다.
# 카드 합체 놀이
# 가장 작게 만드는 것이 놀이임

n, m = map(int, input().split())
card = list(map(int, input().split()))

h = []
for c in card:
    heapq.heappush(h, c)

for _ in range(m):
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    heapq.heappush(h, a+b)
    heapq.heappush(h, a+b)

print(sum(h))