from src.Assignment2.util import find_runnerUp_score,remove_duplicates
def main():
    n=int(input("Enter the number of elements : "))
    l=list(map(int,input().split(" ")))
    unique_ele=remove_duplicates(l,n)
    runner_up_score=find_runnerUp_score(unique_ele,len(unique_ele))
    print(runner_up_score)
main()