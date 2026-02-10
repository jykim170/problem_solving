def fibo(n):
    arr = [0] * (n + 1) 

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    arr[0] = 0
    arr[1] = 1

    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n]

N = int(input())
result = fibo(N)
print(result)

