n = int(input())

result_list = [0]

for i in range(2, 10):
    for j in range(1, i):
        if i % 2 == 0:
            tmp = str(i-j)+ "/" + str(j)
            result_list.append(tmp)
        else:
            tmp = str(j)+ "/" + str(i-j)
            result_list.append(tmp)

print(result_list[n])     
