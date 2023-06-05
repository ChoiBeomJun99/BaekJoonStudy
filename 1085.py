x, y, w, h = map(int, input().split())

result = []

result.append(x-0)
result.append(y-0)
result.append(h-y)
result.append(w-x)

print(min(result))