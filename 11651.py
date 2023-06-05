n = int(input())

point = []

for i in range(n):
    a, b = input().split()
    point.append([int(a),int(b)])

point.sort(key=lambda y: (y[1],y[0]))
for i in point:
    print(i[0], i[1])