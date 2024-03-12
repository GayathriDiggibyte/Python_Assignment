def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    parts=k
    p=parts
    string_parts=[]
    for i in range(0,n,p):
        s=string[i:p]
        p=p+parts
        string_parts.append(s)
    res=[]
    for x in string_parts:
        unique_parts = ""
        for y in x:
            if y not in unique_parts:
                unique_parts = unique_parts + y
        res.append(unique_parts)
    s1='\n'.join(res)
    return s1
