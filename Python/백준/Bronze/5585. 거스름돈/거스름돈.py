n = int(input())
n = 1000 - n 
change = [500, 100, 50, 10, 5, 1]

result = 0

for i in change:
    result += n // i
    n = n % i 
    # print(i, n, result)

print(result)