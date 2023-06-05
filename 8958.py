n = int(input())

ox_list = []
for i in range(n):
    temp_list = list(input())
    ox_list.append(temp_list)

for i in ox_list:
    score = 0
    for j in range(len(i)):
        score_per = 0
        if i[j] == "O":  
            tmp2 = j
            tmp = i[tmp2]
            while tmp =="O":
                if(tmp2 < 0):
                    break
                else:
                    score += 1
                    tmp2 -= 1
                    tmp = i[tmp2]
        score += score_per
    print(score)