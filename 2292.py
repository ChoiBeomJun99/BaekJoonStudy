n = int(input())

count = 1
cnt = 1
while n > count:
    count += 6*cnt
    cnt += 1

print(cnt)