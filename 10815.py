# #순차탐색
# n = int(input())
# cards = list(map(int, input().split()))

# m = int(input())
# nums = list(map(int, input().split()))

# result = []

# for i in range(m):
#     if nums[i] in cards:
#         result.append(1)
#     else :
#         result.append(0)

# for i in result:
#     print(i, end=' ')


#set
# input()
# n = set(map(int, input().split()))

# input()
# m = list(map(int, input().split()))

# for i in m:
#     if i in n:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


#이진 탐색
import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is None:
        print(0, end=' ')
    else:
        print(1, end=' ')