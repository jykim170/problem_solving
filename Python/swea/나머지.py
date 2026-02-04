a = [int(input()) for _ in range(10)]
s = 42
b = []
for i in a:
    b.append(i%42)

b = list(set(b))
print(len(b))