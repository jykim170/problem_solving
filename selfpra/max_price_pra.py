# max_price_pra.py

def dfs(num_list, depth):
    global answer
    
    if depth == change: #이 만큼 교환하면 max로 치환
        answer = max(answer, int(''.join(num_list)))
        return

    # 그리고 하나 더 종료 조건을 넣어줘야돼 visited 관련해서
    # 현재 상태 state
    state = (int(''.join(num_list)), depth) # 이 튜플
    if state in visited:
        return
    
    # 이제 다 통과했다면
    visited.add(state)
    
    n = len(num_list)
    
    for i in range(n-1):
        for j in range(i, n):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            dfs(num_list, depth + 1)
            num_list[i], num_list[j] = num_list[j], num_list[i]
            

t = int(input())

for tc in range(1, t+1):
    number, change = input().split()
    change = int(change)
    answer = 0
    visited = set()
    dfs(list(number), 0)

    print(f"#{tc} {answer}")