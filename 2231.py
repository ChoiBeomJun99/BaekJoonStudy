n = int(input())

result = 0

for i in range(n+1):
    i_str = str(i)
    
    tmp = 0
    for j in range(len(i_str)):
        tmp += int(i_str[j])

    tmp += i

    if tmp == n:
        result = i
        break

print(result)