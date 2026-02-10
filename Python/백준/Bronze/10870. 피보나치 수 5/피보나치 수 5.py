# fibo(10) = fibo(9) + fibo(8)
def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

N = int(input())
print(fibo(N))