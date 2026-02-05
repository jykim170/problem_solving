s = input()

s = s.upper()

word = {}
for i in s:
    if i not in word:
        word[i] = 1
    else:
        word[i] += 1

for k, v in word.items():
    print(k, v)