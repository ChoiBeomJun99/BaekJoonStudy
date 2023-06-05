N ,K = input().split()

N = int(N)
K = int(K)

ans = 1
for i in range(K):
    ans *= N
    N -= 1

share = 1
while K != 0:
    share *= K
    K-=1

print(int(ans/share))