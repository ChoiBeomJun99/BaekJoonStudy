tmp = []

for i in range(3):
    a, b = map(int,input().split())
    tmp.append([a,b])

check_x = []
check_y = []

for i in tmp:
    check_x.append(i[0])
    check_y.append(i[1])

result_x = 0
result_y = 0

if check_x.count(min(check_x)) > check_x.count(max(check_x)):
    result_x = max(check_x)    
else:
    result_x = min(check_x)
        
if check_y.count(min(check_y)) > check_y.count(max(check_y)):
    result_y = max(check_y)    
else:
    result_y = min(check_y)

print(result_x, result_y)