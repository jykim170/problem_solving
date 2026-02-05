# 알파벳 찾기

# 인덱스는 없으면 어떤게 뜨나 ? 스트링 인덱스는 없을 때 어떻게 되는 지 알아보자
# -> 안 뜨고, ValueError 준다!
s = input()
result = []
for i in range(97, 123):
    try:
        result.append(s.index(chr(i)))
    except:
        result.append(-1)
print(*result)

