# 그룹 단어 체커  ?

n = int(input())

cnt = 0
for _ in range(n):
    s = input()

# 여러가지가 생각나는데 우선 생각나는 거 하나는, 그 현재 statement 와 같으면 넣은다음 set으로 비교 
    statement = 0   
    checklist = []
    for i in s:
        if statement != i:
            statement = i
            checklist.append(statement)
    
    if len(checklist) == len(set(checklist)):
        cnt += 1

print(cnt)