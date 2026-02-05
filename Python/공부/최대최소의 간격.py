t = int(input())

for tc in range(1, t+1):
    n = int(input())
    s = list(map(int, input().split()))
    
    max_num = max(s)
    min_num = min(s)
    max_index = 0
    min_index = 0

    for i in range(n-1, -1, -1):
        if s[i] == max_num:
            max_index = i
            break

    for j in range(n):
        if s[j] == min_num:
            min_index = j
            break

    print(f'#{tc} {abs(max_index - min_index)}')