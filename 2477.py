K = int(input())

rectangle = []

horizon_max = 0
h_idx = 0
vertical_max = 0
v_idx = 0

for i in range(6):
    direction, distance = map(int,input().split())
    rectangle.append([direction, distance])

for i in range(len(rectangle)):

    if (rectangle[i][0] == 1 or rectangle[i][0] == 2) and rectangle[i][1] > horizon_max:
        horizon_max = rectangle[i][1]
        h_idx = i
    elif (rectangle[i][0] == 3 or rectangle[i][0] == 4) and rectangle[i][1] > vertical_max:
        vertical_max = rectangle[i][1]
        v_idx = i

subW = abs(rectangle[(h_idx-1)%6][1] - rectangle[(h_idx+1)%6][1])
subH = abs(rectangle[(v_idx-1)%6][1] - rectangle[(v_idx+1)%6][1])

result = horizon_max*vertical_max - (subW*subH)

print(result*K)





