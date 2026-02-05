# 슬라이딩 윈도우
# - 창(범위)이 미끄러지면서 범위에 대한 계산을 하는 문제들에서 활용
# - 해당 범위값을 반복문이 아니라
#   - 제외되는 부분을 없애주고
#   - 추가되는 부분만 계산해주는 방식

# 연속된 K개 숫자의 합 중 가장 큰 합을 구하여라
arr = [20, 32, 16, 25, 36]

K = 3
window = sum(arr[:K])
max_sum = window   # 첫 윈도우 값으로 초기화
print("첫 최대 합:", window)

for i in range(len(arr) - K):
    window = window - arr[i] + arr[i + K]
    print(f'{i}위치 합 : {window}')
    if window > max_sum:
        max_sum = window

print("최대 합:", max_sum)
