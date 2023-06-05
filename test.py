a = input().split()

# if len(a[0]) < 2:
#     a.insert(0, '0')

new = []

tmp = int(a[0][0]) + int(a[0][1])

if tmp > 10:
    tmp = tmp - 10

new.append(int(a[0][1]))
new.append(tmp)


print(new[0])
print(a[0][0])
