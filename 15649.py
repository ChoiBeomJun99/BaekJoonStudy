n, m = map(int, input().split())

s = []

def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s: #이미 들어가있는 같은 수는 배제 
      continue
    s.append(i)
    f()
    s.pop()

f()