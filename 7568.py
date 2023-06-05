n = int(input())
people = []

for x in range(n):
    a, b = input().split()
    tmp = [int(a), int(b)]
    people.append(tmp)


for x in people:
    ranking = 1

    for i in people:
        if x[0] < i[0] and x[1] < i[1]:
            ranking += 1


    print(ranking, end = " ")    
