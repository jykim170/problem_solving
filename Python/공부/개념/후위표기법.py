# 스택 두개 두고 result // oper_stack
# ★원칙★ : oper_stack 에 들어있는 연산자들 중 
#           나보다 우선순위가 크거나 같으면 
#           다 result 로 이동 시키고, 그 후에 oper_result 에 추가

# 그럼 후위표기법의 계산은? 
# stack 하나를 더 만들어서
# 1. 숫자는 망설임 없이 집어넣고, 연산자를 만나면 두개를 꺼내고
# 연산자를 수행하고 넣어줍니다.
# 마찬가지로 반복합니다.
# 최종 남아있는게 결과

import sys
sys.stdin = open("input.txt", "r")

def infix_to_postfix(tokens):
    result = []
    oper_stack = []
    
    # 1. 숫자면 그대로 result에 쌓는다.
    # 2. 연산자라면 
    #    - oper_stack 이 비어있을 때: oper_stack 에 추가
    #    - 아닐 때:
    #        나보다 우선순위가 크거나 같은 연산자들을 result 로 이동 후 추가

    for token in tokens:
        if token.isdigit():
            result.append(token)
        else:
            if oper_stack:
                result.append(oper_stack.pop())

            oper_stack.append(token) 
            
    result.append(oper_stack.pop()) # 남은 연산자 하나

    return result

def get_result(tokens):
    stack = []
    # 숫자라면 그냥 stack 에 넣기
    # 연산자라면, stack 에서 숫자 2개 꺼내서 계산 후 넣기
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num1 + num2)

    return stack[0]    

for tc in range(1, 11):
    N = int(input())
    row = input()
    postfix = infix_to_postfix(row)    # 후위 표기법 으로 변환
    result = get_result(postfix)    # 계산
    print(f'#{tc} {result}')
