a, b, c = input().split()

a = (int(a))
b = (int(b))
c = (int(c))

list = []
list.append(a)
list.append(b)
list.append(c)

reward = 0

if a == b and b == c and a==c:
    reward = 10000 + (a*1000)

elif a==b or b==c or c==a :
    same =0

    if(a==b):
        same = a
    elif(b==c):
        same = b
    elif(a==c):
        same = c

    reward = 1000 + (same * 100)

else:
    bigest = 0

    for i in list:
        if i > bigest:
            bigest = i
    reward = bigest * 100
    
print(reward)