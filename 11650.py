n = int(input())

point = []

for i in range(n):
    a, b = input().split()
    point.append([int(a),int(b)])

point.sort(key=lambda x: (x[0],x[1]))
for i in point:
    print(i[0], i[1])