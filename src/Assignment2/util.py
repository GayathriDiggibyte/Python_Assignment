def remove_duplicates(l,n):
    unique=[]
    for x in l:
        if x not in unique:
            unique.append(x)
    return unique
def find_runnerUp_score(s,n):
    l = list(map(int, s.split(" ")))
    unique=remove_duplicates(l,n)
    max1=min(unique)
    secondmax=min(unique)
    for x in unique:
        if(max1<x):
            secondmax=max1
            max1=x
        else:
            secondmax=max(secondmax,x)
    return secondmax