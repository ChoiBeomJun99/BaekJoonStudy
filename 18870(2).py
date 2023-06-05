N = int(input())

numbers = list(map(int, input().split()))

numset = set(numbers)
a = list(numset)
a.sort()

numdict = {}

for i in range(len(a)):
    numdict[a[i]] = i

for i in numbers:
    print(numdict[i], end= " ")