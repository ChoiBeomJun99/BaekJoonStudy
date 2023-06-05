n = int(input())
test_list = list(map(int, input().split()))

max = max(test_list) 
hap = 0

for i in test_list:
    hap += (i/max)*100

print(hap/len(test_list))

