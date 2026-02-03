n = int(input())

for _ in range(n):
    scores = []
    strike = 0
    s = list(input())
    for i in s:
        if i == 'O':
            strike += 1
            scores.append(strike)
        else:
            strike = 0
            scores.append(strike)
    print(sum(scores))