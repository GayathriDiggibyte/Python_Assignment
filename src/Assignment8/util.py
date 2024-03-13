from collections import namedtuple
def find_avg_marks_of_stds():
    N, student = int(input()), namedtuple('student', input().split())
    sum1=sum([int(student(*input().split()).MARKS) for _ in range(N)])
    avg = sum1 / N
    return "{:.2f}".format(avg)
''' n = int(input())
    columns = input().split()
    student_data = []
    for i in range(n):
        data = input().split()
        student_data.append(data)
    dict = {}
    for i in range(4):
        l = []
        for j in range(n):
            l.append(student_data[j][i])
            dict[columns[i]] = l

    marks = dict["MARKS"]
    sum = 0
    for x in marks:
        sum += int(x)'''







