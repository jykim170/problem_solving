n, m = map(int, input().split())

arr = list(map(int, input().split()))

# 급여 
# 오차 x 
# 정해진 일 수 만큼
# 퇴직 후 재취직 x
# 연속해서 최댓값 ? 이거 슬라이딩 윈도우네 ! 라는 사고

count = sum(arr[:m]) # 최초의 값은 첫날부터 3일까지 0, 1, 2 예제
choidae = count

for i in range(n - m): # 0, 1, 2
    count = count - arr[i] + arr[i+m]
    if choidae < count:
        choidae = count

print(choidae)