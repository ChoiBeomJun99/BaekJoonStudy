from math import sqrt
test = []

while True:
    n = int(input())

    if n == 0:
        break
    else:
        test.append(n)

for i in test:
    count = 0
    for k in range(i+1 , 2*i+1):
        flag = 0
        
        if k == 1:
            continue
        elif k == 2:
            count+=1
            continue
        else:
            for j in range(2, int(k**0.5)+1):
                if k % j == 0:
                    break
            else:
                count+=1
        

    print(count)   
    
             
