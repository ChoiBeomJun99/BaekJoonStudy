word = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

minus = 0
for i in croatia:
    word = word.replace(i,'*')
    
print(len(word))