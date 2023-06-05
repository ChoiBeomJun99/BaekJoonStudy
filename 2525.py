a, b = input().split()
c = input().split()

a = int(a)
b = int(b)
c = int(c[0])

a += c // 60
b += c % 60

if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -= 24

print(a,b)