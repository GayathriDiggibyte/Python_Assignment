import numpy as np
def floor_ceil_rint(s):
    res=[]
    s1=s.split(" ")
    l=[]
    for x in s1:
        l.append(float(x))
    array1=np.array(l)
    np.set_printoptions(legacy='1.13')
    res.append(np.floor(array1))
    res.append(np.ceil(array1))
    res.append(np.rint(array1))
    res[0]=str(res[0])
    res[1] = str(res[1])
    res[2] = str(res[2])
    return '\n'.join(res)
