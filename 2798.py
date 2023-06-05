N, M = input().split()

N = int(N)
M = int(M)

arr = list(map(int , input().split()))

min = M
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = arr[i] + arr[j] + arr[k]
            
            if min >= M - tmp and M - tmp>=0:
                min = M-tmp
                result = tmp
            

print(result)                