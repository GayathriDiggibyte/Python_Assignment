def order_words():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    unique = {}
    res = ""
    for x in s:
        if x in unique:
            unique[x] += 1
        else:
            unique[x] = 1

    for x in unique:
        res = res + str(unique[x]) + " "
    return str(len(unique))+"\n"+res
