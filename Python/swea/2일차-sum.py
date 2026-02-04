for _ in range(10):
    tc = int(input())
    box = [list(map(int, input().split())) for _ in range(100)]

    answer_arr = []
    right_down = 0
    for i in range(100):
        right_down += box[i][i]
    answer_arr.append(right_down)

    left_down = 0
    for i in range(100):
        left_down += box[100-i-1][i]
    answer_arr.append(left_down)

    row = 0
    for i in range(100):
        row = max(row,sum(box[i]))
    answer_arr.append(row)
        
    column = 0
    for i in range(100):
        hap = 0
        for j in range(100):
            hap += box[j][i]
        column = max(column, hap)
    answer_arr.append(column)
    print(max(answer_arr))