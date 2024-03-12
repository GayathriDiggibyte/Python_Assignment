from src.Assignment2.util import find_runnerUp_score,remove_duplicates
def main():
    n=int(input("Enter the number of elements : "))
    s=input()
    runner_up_score=find_runnerUp_score(s,n)
    print(runner_up_score)
main()