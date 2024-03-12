import datetime
def calendar_module(s):
    s1=s.split(" ")
    year=int(s1[2])
    month=int(s1[0])
    day=int(s1[1])
    date1=datetime.date(year,month,day)
    return date1.strftime("%A").upper()
