box = [list(input()) for _ in range(5)]
max_len = 0
for i in box:
    if max_len < len(i):
        max_len = len(i)

result = []
for x in range(max_len):
    # x 값 고정 시키고 y 값을 늘리는데 , 이제 존재하지 않을때는 건너뛰어 !
    for y in range(5):
        try:
            result.append(box[y][x])
        except:
            pass
print(*result, sep='')