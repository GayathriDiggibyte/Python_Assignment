import numpy as np
def min_max():
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        ele=list(map(int,input().split()))
        l.append(ele)
    array1=np.array(l)
    min_ele=np.min(array1,axis=1)
    return np.max(min_ele)

