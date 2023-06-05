from math import factorial
N = int(input())

num = str(factorial(N))

count = 0
for i in num[::-1]:
    
    if(i == '0'):
        count +=1
    else:
        break

print(count)