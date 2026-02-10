def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    return num * factorial(num-1)

N = int(input())

result = factorial(N)
print(result)