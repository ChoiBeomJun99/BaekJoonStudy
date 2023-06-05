M, N = input().split()

M = int(M)
N = int(N)

for i in range(M , N+1):

    if i ==1 :
        continue
    
    for k in range(2, i):
        if i % k == 0:
            break
    
    else:
        print(i)


# x, y = map(int, input().split())

# for i in range(x, y+1):
#     if i == 1: #1은 소수가 아뉘지!
#         continue
#     for j in range(2, int(i** 0.5)+1 ):
#         if i%j==0:
#             break
#     else:
#         print(i)

