n, m = map(int, input().split())

S = set()

for i in range(n):
    S.add(input())

ans = 0

for _ in range(m):
    t = input()
    if t in S:
        ans += 1

print(ans)



