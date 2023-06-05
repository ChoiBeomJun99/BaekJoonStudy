a = input().split()

if len(a[0]) < 2:
    a[0] = '0' + a[0][0]

count = 0
new = [a[0][0], a[0][1]]

while True:
    count += 1
    tmp = int(new[0]) + int(new[1])

    if tmp > 10:
        tmp = tmp - 10

    new[0] = int(new[1])
    new[1] = tmp
    
    # print(new)
    # print(a[0])
    
    if (new[0] == int(a[0][0]) and (new[1] == int(a[0][1]))):
        break
       
print(count)
    