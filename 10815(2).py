def binarySearch(array, check, start, end):
    
    while(start <= end):
        mid = (start + end) //2

        if array[mid] == check:
            return mid
        elif array[mid] > check:
            end = mid-1
        else:
            start = mid+1
    return None

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

cards.sort()

for i in range(M):
    if binarySearch(cards, nums[i], 0, N-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')



