import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input() # str 1에 들어있는 글자들을 돌면서, str 2 에 각각 몇개씩 들어있는지 최대갯수만 찾자
    contain = []

    for i in str1: #중복있어도 뭐 ,,
        contain.append(str2.count(i))

    print(f'#{tc}',max(contain))
