n = int(input())

result = ''

while n != 1:
    result += str(n%2)
    n //= 2
    if n == 1:
        result += str(1)

print(result[::-1])