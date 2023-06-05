from math import factorial

T = int(input())

results = []

for i in range(T):
    N, M = map(int, input().split())
    result = factorial(M) // (factorial(N) * factorial(M-N))
    results.append(result)


for i in results:
    print(i)