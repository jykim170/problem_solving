n, x = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:x])

hap_list = []
hap_list.append(window)

for i in range(n - x):
    window = window - arr[i] + arr[i+x]
    hap_list.append(window)

if max(hap_list) != 0:
    print(max(hap_list))
    print(hap_list.count(max(hap_list)))
else:
    print('SAD')