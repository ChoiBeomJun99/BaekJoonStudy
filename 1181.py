n = int(input())

words = []

for i in range(n):
    word = input()
    words.append(word)

words = set(words)
words = list(words)
words.sort()
words.sort(key = len)

for i in words:
    print(i)