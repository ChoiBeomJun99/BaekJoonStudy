# T = int(input())

# case = []

# for i in range(T):
#     tmp = int(input())
#     case.append(tmp)

# for i in case:
#     sosu = []
#     result = []
    
#     for j in range(2, i):
#         error = 0
#         for k in range(2, j):
#             if j % k == 0:
#                 error = 1
        
#         if error == 0 :
#             sosu.append(j)


#     for j in sosu:
#         tmp = i - j
#         if tmp in sosu:
#             result_case = [j, tmp]
#             result.append(result_case)
    
#     min = i
#     for j in result:
#         if j[1] - j[0] < min:
            

#에라토스테네스의 체 사용.
sosu = [0 for i in range(10001)]
sosu[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        sosu[j] = 1
t = int(input())
for i in range(t):
    a = int(input())
    b = a // 2
    for j in range(b, 1, -1):
        if sosu[a - j] == 0 and sosu[j] == 0:
            print(j, a - j)
            break