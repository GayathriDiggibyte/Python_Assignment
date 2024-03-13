import re

def fun(s):
    pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
    return pattern.match(s)

def filter_mail():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = []
    for x in emails:
        match = fun(x)
        if match:
            filtered_emails.append(x)
    filtered_emails.sort()
    return filtered_emails
