n = int(input())

result = 0
for i in range(1, n+1):
    i = str(i)
    
    if len(i) >= 2:
        count = 0
        interval = int(i[1]) - int(i[0])
        for j in range(len(i)):
            if j-1 >= 0:
                if int(i[j]) - int(i[j-1]) == interval:
                    count += 1
        if count == len(i)-1:
            result +=1

    elif len(i) == 1:
        result +=1
        
print(result)
    