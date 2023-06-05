n =  int(input())

tmp = 2
while n > 1:
    if n % tmp == 0:
        print(tmp)
        n = n / tmp
    else:
        tmp += 1
            
