def find_avg_marks_of_stds():
    n = int(input())
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
        sum += int(x)
    avg = sum / n
    print("{:.2f}".format(avg))






