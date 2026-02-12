import sys
sys.stdin = open("input.txt", "r")

priority = {'+': 1, '*': 2}

def infix_to_postfix(tokens):
    result = []
    oper_stack = []

    for token in tokens:
        if token.isdigit():
            result.append(token)
        else:
            while oper_stack and priority[oper_stack[-1]] >= priority[token]:
                result.append(oper_stack.pop())

            oper_stack.append(token)

    while oper_stack:
        result.append(oper_stack.pop())

    return result

def get_result(tokens):
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if token == '+':
                stack.append(num1+num2)
            elif token == '*':
                stack.append(num1*num2)
    
    return stack[0]

for tc in range(1, 11):
    n = int(input())
    string = input()
    postfix = infix_to_postfix(string)
    answer = get_result(postfix)

    print(f'#{tc} {answer}')


    # 백트래킹
# - 전체 경우의 수 (기본 재귀호출)
#   - N 중 for문

# 예시) 주사위 K개 (1, 1, 1) ~ (6, 6, 6)
# for a in range(1, 7):
#     for b in range(1, 7):
#         for c in range(1, 7):
#             print(a, b, c)

# K 중 재귀호출

# k = 3 
# # 주사위 3개
# def recur(cnt, path):
#     # 시작: 주사위 하나도 안던짐 (base case)
#     # 끝 : 주사위 k 개를 던짐
#     # 누적값
#     #   - cnt: 던진 횟수
#     #   - path: 던진 주사위 기록
#     if cnt == k:
#         print(path)
#         return

#     for i in range(1, 7):
#         path.append(i)           
#         recur(cnt+1, path)
#         path.pop()

# recur(0, [])
# - 부분 집합
#   - 전체 중 일부만 골라서 문제를 해결

        # 부분집합과 관련된 건 이 부분 집합에 이것을 포함 시킬 지 말 지만 고민하면 된다.

# arr = ['A', 'B', 'C', 'D']

# 전체 부분집합을 출력하는 재귀함수
# 시작: 0 개의 데이터를 부분집합에 넣을 지 말지 고려
# 끝: 2**len(arr)
# 누적값
#   - cnt: 몇 개의 데이터를 고려 했는가 ?
#   - subset: 현재 부분집합
# def recur2(idx, subset):
#     if idx == len(arr):
#         print(subset)
#         return
    
#     # 1. 현재 원소를 부분집합에 포함
#     subset.append(arr[idx])
#     recur2(idx + 1, subset)
#     subset.pop()

#     # 2. 현재 원소를 부분집합에 포함 X
#     recur2(idx + 1, subset)


# recur2(0, [])

# - 순열
#   - 전체 중 K개를 순서를 고려하면서 골라서 문제를 해결
# arr = ['A', 'B', 'C', 'D', 'E']
# used = [0] * len(arr)
# k = 3


# def recur(subset):
#     # 시작점: 0개의 알파벳을 선택
#     # 끝점(base case):len(subset) == 3 이 되면 끝내기
#     # 누적값:  
#     #   - subset
    
#     if len(subset) == 3:
#         print(*subset)
#         return
    
#     for i in range(len(arr)):
#         if used[i]:
#             continue
#         used[i] = 1        
#         subset.append(arr[i])
#         recur(subset)
#         subset.pop()
#         used[i] = 0 # 쓴적이 없다고 되돌리기
# 
# recur([])


# - 중복 순열 (같은 걸 여러 번 골라도 된다)

# def recur(subset):
#     # 시작점: 0개의 알파벳을 선택
#     # 끝점(base case):len(subset) == 3 이 되면 끝내기
#     # 누적값:  
#     #   - subset
    
#     if len(subset) == k:
#         print(*subset)
#         return
    
#     for word in arr:
#         subset.append(word)
#         recur(subset)
#         subset.pop()

# recur([])





# - 조합
#   - 전체 중 K개를 골라서 문제를 해결

arr = ['A','B','C','D']
K = 3

def recur5(cnt, pre, path):
    if cnt == K:
        print(*path)
        return
    
    for i in range(pre + 1, len(arr)):
        path.append(arr[i])
        # 현재 선택인 i 를 같이 전달
        recur5(cnt + 1, i, path)
        path.pop()

recur5(0, -1, [])































# 장훈이의 높은 선반 D4
# 이 문제는 전체 경우의 수를 보는 게 아니다.
# 부분집합을 보면서
# B 이상이면 더 쌓을 필요가 없는게 기저 조건 (base case)


# def recur(idx, subset):
#     global maxlist
#     # 기저 조건으로 b 이상 중에 가장 낮은걸 해야 되는데
#     if sum(subset) >= b:
#         maxlist.append(sum(subset))
#         return 
    
#     if idx == n:
#         return 


#     # 부분집합 현재걸 포함
#     subset.append(arr[idx])
#     recur(idx+1, subset)
#     subset.pop()

#     # 포함 x
#     recur(idx+1, subset)


# t = int(input())
# for tc in range(1, t+1):
#     n, b = map(int, input().split())
#     arr = list(map(int, input().split()))
#     maxlist = []
#     recur(0, [])
#     print(f'#{tc} {min(maxlist) - b}')


# Queue 
# - 가장 앞의 데이터만 활용할 때 ( 놀이공원 줄 설 때 )

# 우선순위 큐 (Priority Queue)
# - 큐 처럼 돌아가는데, 먼저 꺼내지는 우선순위 있다.

