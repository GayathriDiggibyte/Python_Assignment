from datetime import datetime
def time_delta(s):
    st=s.split("\n")
    print(len(st))
    n=int(st[0])
    diff_list=[]
    for i in range(1,len(st),2):
        t1=st[i]
        t2=st[i+1]
        format_str="%a %d %b %Y %H:%M:%S %z"
        t1=datetime.strptime(t1,format_str)
        t2=datetime.strptime(t2,format_str)
        diff=int(abs(t1-t2).total_seconds())
        diff_list.append(str(diff))
    return '\n'.join(diff_list)