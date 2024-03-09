def remove_duplicates(l,n):
    unique=[]
    for x in l:
        if x not in unique:
            unique.append(x)
    return unique
def find_runnerUp_score(l,n):
    max1=min(l)
    secondmax=min(l)
    for x in l:
        if(max1<x):
            secondmax=max1
            max1=x
        else:
            secondmax=max(secondmax,x)
    return secondmax