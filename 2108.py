# n = int(input())

# case = []

# for i in range(n):
#     tmp = int(input())
#     case.append(tmp)

# #산술평균
# avg = sum(case) / len(case)
# print(int(round(avg, 0)))

# #중앙값
# case.sort()
# index = int(len(case) / 2)
# print(case[index])

# #최빈값
# counts = []

# for i in case:
#     count = case.count(i)
#     counts.append(count)

# flag = 0
# max_count = max(counts)

# for i in counts:
#     if i == max_count:
#         flag += 1

# if flag == 1: #최빈값이 하나일때
#     max_count = max(counts)
#     index = counts.index(max_count)

#     print(case[index])
# else:
#     choi = []

#     for i in range(len(counts)):
#         if max_count == counts[i]:
#             choi.append(i)
    
#     print(choi)

#     new_case = []
#     for i in choi:
#         if i not in new_case:
#             new_case.append(case[i])

#     new_case.sort()
#     print(new_case)
    

# #범위
# case.sort()
# diff = case[len(case)-1] - case[0]
# print(diff)

import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
 
# 산술평균 - 다 더해서 / n
print(round(sum(li)/n))
 
# 중앙값 - 오름차순 -> 중간값
li.sort()
print(li[n//2])
 
# 최빈값 - 빈출
cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
 
# 범위 - 최댓값-최솟값
print(max(li)-min(li))