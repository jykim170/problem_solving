import sys
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    q = deque((p, i) for i, p in enumerate(priorities))

    cnt = 0

    while True:
        p, i = q[0]

        if p < max(x[0] for x in q):
            q.rotate(-1)
        else:
            q.popleft()
            cnt += 1
            if i == m:
                print(cnt)
                break