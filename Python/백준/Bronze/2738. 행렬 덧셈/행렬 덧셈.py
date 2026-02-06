n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
# 행 n , 열 m 개
arr2 = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j] = arr1[i][j] + arr2[i][j]

for s in result:
    print(*s)