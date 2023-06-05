from math import factorial

n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
count = 0

for i in str(result)[::-1]:
    
    if i != '0':
        break

    count += 1

print(count)