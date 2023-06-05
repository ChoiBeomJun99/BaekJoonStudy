t = int(input())

test = []

for i in range (0,t):
    a, b, c = input().split()

    a = int(a)
    b = int(b)
    c = int(c)

    tmp = [a, b, c]

    test.append(tmp)



for i in test:
    count = 0

    h = i[0]
    w = i[1]
    n = i[2]

    for j in range(1,w+1):
        for k in range(1,h+1):
            count += 1

            if count == n:
                if j >= 10:
                    print("%d%d" % (k,j))
                else:
                    print("%d0%d" % (k,j))
                
                
    


          
    
