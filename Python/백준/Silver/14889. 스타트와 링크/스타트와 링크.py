import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
min_diff = float('inf')

def dfs(depth, start):
    global min_diff
    
    # 팀 구성 완료
    if depth == N // 2:
        team1, team2 = 0, 0
        
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team1 += S[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += S[i][j]
        
        min_diff = min(min_diff, abs(team1 - team2))
        return
    
    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(min_diff)