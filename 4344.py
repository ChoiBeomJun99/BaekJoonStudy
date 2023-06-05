n = int(input())

testCase = []
for i in range(n):
    temp_list = list(map(int, input().split()))
    testCase.append(temp_list)

for i in testCase:
    student_count = i[0]
    hap = 0

    for j in range(1, student_count+1):
        hap += i[j]

    avg = hap / student_count

    overAvg = 0
    for k in range(1, student_count+1):
        if i[k] > avg:
            overAvg += 1
            
    print("%.3f%%" % (overAvg/student_count * 100))