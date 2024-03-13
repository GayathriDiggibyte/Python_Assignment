def piling_up():
    res = []
    no = int(input())

    for i in range(no):
        n = int(input())
        s = list(map(int, input().split()))

        for j in range(n - 1):
            if s[0] >= s[len(s) - 1]:
                a = s[0]
                s.pop(0)
            elif s[0] < s[len(s) - 1]:
                a = s[len(s) - 1]
                s.pop(len(s) - 1)
            else:
                pass

            if len(s) == 1:
                res.append("Yes")

            if ((s[0] > a) or (s[len(s) - 1] > a)):
                res.append("No")
                break

    return "\n".join(res)