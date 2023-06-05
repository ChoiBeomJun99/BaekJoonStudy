M = int(input())
N = int(input())

result = 0
min = N
for i in range(M, N+1):
    error = 0
    for j in range(2, i):
        if i % j ==0:
            error += 1
            break

    if error == 0 :
        if i < min:
            min = i
        result += i

if result > 0:
    print(result)
    print(min)
else:
    print(-1)

