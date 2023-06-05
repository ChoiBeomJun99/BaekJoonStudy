import random

def make_question():
    a = random.randint(1, 40) #1~40 사이의 수를 무작위로 뽑아 a에 저장
    b = random.randint(1, 20) #1~20 사이의 수를 무작위로 뽑아 b에 저장
    op = random.randint(1, 3) #1~3 사이의 수를 무작위로 뽑아 op에 저장

    q = str(a) #a의 값을 문자열로 바꿔줍니다.

    if op == 1: #할당된 op의 값에 맞게 연산자를 할당해줍니다.
        q = q + " + "
    elif op == 2:
        q = q + " - "
    elif op == 3:
        q = q + " * "

    q += str(b) #문제를 낼 문자열을 완성

    return q #문제 문자열 반환 


correct_count = 0 #맞은 개수를 세는 변수
wrong_count = 0 #틀린 개수를 세는 변수 

for x in range(5): #5번 반복
    q = make_question()
    print(q)
    ans = input(" = ")
    r = int(ans)

    if eval(q) == r: #정답일시 
        print("정답입니다.")
        correct_count += 1
    else: #오답일시 
        print("오답입니다.")
        wrong_count += 1


#마지막 결과 창
print("정답 개수 : " + str(correct_count) + "오답 개수 : " + str(wrong_count))
if wrong_count == 0:
    print("다 맞추셨네요. 연산의 천재!")




