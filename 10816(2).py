from sys import stdin
from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

C = Counter(cards)

for i in nums:
    if i in C:
        print(C[i], end=' ')
    else:
        print(0, end=' ')

