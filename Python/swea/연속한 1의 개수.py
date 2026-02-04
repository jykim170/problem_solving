t = int(input())

for tc in range(1, t+1):
    n = int(input())
    s = list(map(int, list(input())))
    sequence_one = False

    cnt = 0
    length = []
    for i in s:
        if i == 1:
            cnt += 1
            length.append(cnt)
        else:
            cnt = 0

    print(f'#{tc} {max(length)}')
