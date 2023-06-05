N = int(input())

circle = list(map(int, input().split()))

for i in range(N-1):
    x = circle[0]
    y = circle[i+1]

    while(x % y != 0): #최대공약수 구하기 (유클리드 호제법)
        r = x % y
        x = y 
        y = r

    denom = circle[0] // y
    numer = circle[i+1] // y
    print(f'{denom}/{numer}')