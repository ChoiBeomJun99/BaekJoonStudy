A, B = map(int, input().split())


a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(A+B - 2*(len(list(a&b))))