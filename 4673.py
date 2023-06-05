
list = []

for i in range(1,10001):
    list.append(i)

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    
    if i in list:
        list.remove(i)    

for i in list:
    print(i)


