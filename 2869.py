# a, b, c = input().split()

# a = int(a)
# b = int(b)
# c = int(c)

# sun = 1
# moon = 0

# distance = 0
# while c > distance:

#     if sun > moon:
#         distance += a    
#         moon+=1
#     elif sun == moon:
#         distance -= b
#         sun+=1

# print(int((sun+moon)//2))

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

days = (c-b) / (a-b)
print(int(days) if days==int(days) else int(days)+1)
