tmp = []

for i in range(3):
    n = int(input())
    tmp.append(n)


mul = tmp[0] * tmp[1] * tmp[2]

result = list(str(int(mul)))
for i in range(10):
    print(result.count(str(i)))