n = int(input())
numbers = list(map(int, input().split()))

max = numbers[0]
min = numbers[0]

for i in range(n):
    
    if numbers[i] > max:
        max = numbers[i]
    
    if numbers[i] < min:
        min = numbers[i]

print(min, max)


