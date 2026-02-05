s = input()

length = len(s)

word_list = []

for i in range(length):
    word_list.append(s[i:])

word_list.sort()

for word in word_list:
    print(word)