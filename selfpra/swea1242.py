import sys
sys.stdin = open("input.txt", "r")

t = int(input())

sixteen = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111'
}

# 비율 : 숫자
password = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    code = []

    for _ in range(n):
        s = input().strip()
        if s not in code and s != '0' * m:
            code.append(s)

    result = 0
    used = set()   # 같은 암호 중복 방지

    for cd in code:
        temporary = []
        for c in cd:
            if c in sixteen:
                temporary.append(sixteen[c])

        temporary = ''.join(temporary)

        if temporary == '':
            continue

        i = len(temporary) - 1
        numbers = []

        while i >= 0:
            if temporary[i] == '0':
                i -= 1
                continue

            c3 = 0
            c2 = 0
            c1 = 0

            # 뒤에서부터 1의 개수
            while i >= 0 and temporary[i] == '1':
                c3 += 1
                i -= 1

            # 그 앞의 0의 개수
            while i >= 0 and temporary[i] == '0':
                c2 += 1
                i -= 1

            # 그 앞의 1의 개수
            while i >= 0 and temporary[i] == '1':
                c1 += 1
                i -= 1

            # 앞쪽 불필요한 0 제거
            while i >= 0 and temporary[i] == '0':
                i -= 1

            if c1 == 0 or c2 == 0 or c3 == 0:
                continue

            mini = min(c1, c2, c3)
            key = (c1 // mini, c2 // mini, c3 // mini)

            if key in password:
                numbers.append(password[key])

                if len(numbers) == 8:
                    numbers.reverse()
                    num_tuple = tuple(numbers)

                    if num_tuple not in used:
                        odd = numbers[0] + numbers[2] + numbers[4] + numbers[6]
                        even = numbers[1] + numbers[3] + numbers[5] + numbers[7]

                        if (odd * 3 + even) % 10 == 0:
                            result += sum(numbers)
                            used.add(num_tuple)

                    numbers = []

        # 다음 줄 해독 전 초기화
    print(f"#{tc} {result}")