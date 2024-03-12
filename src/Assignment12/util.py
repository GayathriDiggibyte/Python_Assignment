import numpy as np
def determinant():
    n=int(input())
    l=[]
    for i in range(n):
        e=list(map(float,input().split()))
        l.append(e)
    return round(np.linalg.det(l),2)