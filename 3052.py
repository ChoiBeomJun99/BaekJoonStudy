import re


tmp = []
for i in range(10):
    n = int(input())
    tmp.append(n%42)


remain = []
for i in range(10):

    if len(remain) == 0:
        remain.append(tmp[i])
    else:
        if tmp[i] not in remain:
            remain.append(tmp[i])

print(len(remain))

