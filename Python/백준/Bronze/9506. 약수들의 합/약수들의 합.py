while True:
    n = int(input())
    if n == -1:
        break

    result = []
    for i in range(1, n): # 일부러 자기 자신 빼줌
        if n % i == 0:
            result.append(i)
    
    if sum(result) == n:
        print(f'{n} = ', end='')
        print(*result, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')
