list = []

for i in range(9):
    n = int(input())
    list.append(n)

max = list[0]
max_result = 0
for i in range(len(list)):
    if max < list[i]:
        max_result = i
        max = list[i]
    
print(max)
print(max_result+1)
