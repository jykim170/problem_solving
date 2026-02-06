import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    w = input()
    w = w[::-1]    
    # 거울이니까 좌우 반전
    # q -> p, b-> d
    result = []
    for i in w:
        if i == 'q':
            result.append('p')
        elif i == 'p':
            result.append('q')
        elif i == 'b':
            result.append('d')
        else:
            result.append('b')

    print(f'#{tc} ', *result, sep = '')
