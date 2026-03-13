def dfs(num_list, depth):
    global answer
    
    if depth == change:
        answer = max(answer, int(''.join(num_list)))
        return
    
    state = (int(''.join(num_list)), depth)
    if state in visited:
        return
    
    visited.add(state)
    
    n = len(num_list)
    for i in range(n-1):
        for j in range(i+1, n):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            dfs(num_list, depth + 1)
            num_list[i], num_list[j] = num_list[j], num_list[i]
        




t = int(input())

for tc in range(1, t+1):
    number, change = map(int, input().split())
    visited =set()
    
    answer = 0
    dfs(list(str(number)), 0)
    print(f'#{tc} {answer}')