n = int(input())

a = list(map(int, input().split()))

max_num = max(a)

for i in range(len(a)):
    a[i] = (a[i] / max_num) * 100

print(sum(a)/len(a))