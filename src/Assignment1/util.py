def find_average_score(dict,student_name):
    marks=dict[student_name]
    sum=0
    for x in marks:
        sum=sum+x
    avg=sum/3
    return "{:.2f}".format(avg)
