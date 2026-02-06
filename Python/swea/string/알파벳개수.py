import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    alphabet = [0 for _ in range(97, 123)]
    w = input()
    for i in w:
        s = ord(i)
        alphabet[s-97] += 1

    print(f'#{tc}', *alphabet)