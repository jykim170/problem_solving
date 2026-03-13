# 0 이상 9이하의 번호가 적힌 6장의 카드
# - 3장의 카드가 연속적인 번호를 갖는 경우 "run" 이라고 하고,
#   3장의 카드가 동일한 번호를 갖는 경우는 "triplet" 이라고 합니다.
# - 그리고 6장의 카드가 run과 triplet로만 구성된 경우를 "baby-gin" 으로 부릅니다.
# 0 1 7 2 7 7 (이 예시에서는 0 1 2 와 7 7 7 카드가 있으므로 baby-gin 입니다.)

# - 6장의 카드 번호를 입력 받고, 완전탐색으로 baby-gin 여부를 판단하는 프로그램을 작성하기



# 그럼 run // triplet 을 넣어서 그거를 빼면 안되나 ?
# 6자리의 수에서

def a_sub_b(a, b):
    sub = [x for x in a if x not in b]
    return sub

run = []
for i in range(8): # 0 ~ 7
    run.append([i, i+1, i+2])

baby_gin = []
for i in range(10):
    baby_gin.append([i,i,i])
    
# print(run)
# print(baby_gin)




a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
print(b in a)

# arr = list(map(int, input().split())) # 입력값.
# arr.sort()

# print(arr) # 0 1 1 1 2 3

# for i in range(10):
#     if baby_gin[i] in arr:
#         arr = a_sub_b(arr, baby_gin[i])
#         print(baby_gin[i])

# print(arr)

# for i in range(8):
#     if run[i] in arr:
#         arr = a_sub_b(arr, run[i])
#         print(run[i])

# print(arr)    


# if arr == []:
#     print('YES')
# else:
#     print('NO')

# 해결 못한거 통으로 그게 들어있을때 빼줘야됨
# 해결 못한것 777777 숫자가 하나로 쭉 넣엇을때  -> set 렝쓰 1이면 되고


# 일단 줄을 다 세워보자

import sys
