n = int(input())

count = 0

if n // 5 == 0:
    if n != 3 :
        print(-1)
    else:
        print(1)
else:
    tmp = n%5
    if tmp % 3 == 0 and tmp != 0:
        kg_5 = n//5
        kg_3 = (n-5*kg_5) // 3

        print(kg_5+kg_3)
    else:
        kg_3 = 0
        kg_5 = 0

        if n%5 == 0:
            kg_5 = n//5
        else:
            while True:
                n -= 3
                kg_3 += 1
            
                if n % 5 == 0 and n >= 5:
                    kg_5 = n//5
                    break

                if n == 0:
                    break
            
        print(kg_5+kg_3)

    

        




