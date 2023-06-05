n = int(input())

info = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    info.append([age, name])

info.sort(key = lambda x: x[0])

for i in info:
    print(i[0], i[1])
