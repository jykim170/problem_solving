import math
x, y, w, h = map(int, input().split())

# 네개의 좌표 가 있을 텐데
# (0, 0) (0, h) (w, 0) (w, h)
# 그리고 그냥 직선 사이의 거리들이 있지 않나 ?
# 예를들어 h-y or y
# 그리고 w-x or x
# 점 사이의 거리 
distance = [x, y, h-y, w-x]
distance.append(math.sqrt((x-0)**2+(y-0)**2))
distance.append(math.sqrt((x-0)**2+(y-h)**2))
distance.append(math.sqrt((x-w)**2+(y-0)**2))
distance.append(math.sqrt((x-w)**2+(y-h)**2))

print(min(distance))