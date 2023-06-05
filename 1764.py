# N, M = map(int, input().split())

# S = set()

# for i in range(N):
#     S.add(input())

# result = set()

# count = 0
# for i in range(M):
#     t = input()
#     if t in S:
#         count += 1
#         result.add(t)

# print(count)
# for i in result:
#     print(i)

N, M = map(int, input().split())

a = set()
for i in range(N):
    a.add(input())

b = set()
for i in range(M):
    b.add(input())

result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)