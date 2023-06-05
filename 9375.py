from collections import Counter
t = int(input())

results = []

for i in range(t):
    n = int(input())
    wear = []
    
    for j in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    results.append(cnt-1)

for i in results:
    print(i)