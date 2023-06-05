n = int(input())

word_list = []

for i in range(n):
    word = input()
    word_list.append(word)

result =0

for i in word_list:
    tmp_list = []
    before_word = "1"
    flag = 1    

    for j in i:
        if j in tmp_list:
            if before_word != j:
                before_word =j
                flag = 0
                break
        else:
            tmp_list.append(j)
            before_word = j

    if flag == 1:
        result += 1

print(result)