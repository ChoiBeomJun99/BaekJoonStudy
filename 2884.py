a, b = input().split()

a = int(a)
b = int(b)

if (a >=0 and a<=23) and (b>=0 and b<=59):
    

    if(b-45 < 0):
        a -= 1
        if(a < 0):
            a = 23
        
        b = 60 - (45 - b)
        
    else:
        b = b-45

print(a, b)

