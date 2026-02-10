# fibo(10) = fibo(9) + fibo(8)
def fibo(num):
    arr = [0] * (num + 1)
    arr[1] = 1

    for i in range(2, num+1):
        arr[i] = arr[i-2] + arr[i-1]
    return arr[num]

N = int(input())
print(fibo(N))