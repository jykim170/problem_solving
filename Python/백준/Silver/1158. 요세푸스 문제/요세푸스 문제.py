from collections import deque

n, k = map(int, input().split())

arr = deque(i for i in range(1, n+1))

answer = []

while arr:
    arr.rotate(-(k-1))
    answer.append(arr.popleft())

answer = list(map(str, answer))
result = ', '.join(answer)

print(f'<{result}>')