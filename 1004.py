T = int(input())

results = []

for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    count = 0

    n = int(input())
    for i in range(n):
        cx, cy, r = map(int, input().split())

        distance_1 = ((cx-x1)**2 + (cy-y1)**2)**0.5
        distance_2 = ((cx-x2)**2 + (cy-y2)**2)**0.5

        #속하는지 안속하는지만 판단
        if(distance_1 < r and distance_2 > r) or (distance_1>r and distance_2<r):
            count+=1

    results.append(count)        

for i in results:
    print(i)