n = int(input())

count = 0
tmp = 666

while True:
    if '666' in str(tmp):
        count += 1

    if n == count:
        print(tmp)
        break

    tmp += 1