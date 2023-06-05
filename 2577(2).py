a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
result = list(str(mul))
print(result)
for i in range(10):
    print(result.count(str(i)))