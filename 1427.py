n = input().split()

new = []
for i in n[0]:
    new.append(i)

new.sort(reverse=True)

result = ""
for i in new:
    result += str(i)

print(result)

