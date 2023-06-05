n = int(input())

list_tmp = []
for i in range(n):
    tmp_i = list(input())
    list_tmp.append(tmp_i)

new_list = []
for i in list_tmp:
    tmp = ""
    for k in range(2,len(i)):
        for j in range(int(i[0])):
            tmp += i[k]
    
    new_list.append(tmp)        

for i in new_list:
    print(i)
            
        