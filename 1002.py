from dis import dis
from unittest import result


T = int(input())

results = []

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    if distance == 0 and r1==r2: #동심원
        results.append(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance: #외접 또는 내접 할때
        results.append(1)
    elif abs(r1-r2) < distance < r1+r2:
        results.append(2)
    else:
        results.append(0)

for i in results:
    print(i)