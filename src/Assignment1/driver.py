from src.Assignment1.util import find_average_score
def main():
    dict={}
    n=int(input("Enter the number of students : "))
    for i in range(n):
        student_name=input("Enter the student name for key : ")
        marks=[]
        for j in range(3):
            m=int(input("Enter the marks : "))
            marks.append(m)
        dict[student_name]=marks
    specific_name=input("Enter the specific student name to find the average of marks : ")
    res=find_average_score(dict,specific_name)
    print(res)
main()

