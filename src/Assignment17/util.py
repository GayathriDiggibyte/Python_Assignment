def find_probability():
    from itertools import combinations

    n = int(input())
    l = list(input().split())
    k = int(input())
    d = {char: [] for char in set(l)}

    indices = range(1, n + 1)
    for i in range(n):
        d[l[i]].append(i + 1)

    unordered_tuple = list(combinations(indices, k))
    count_a = 0
    if 'a' in d:
        count_a = sum(1 for pair in unordered_tuple if any(index in d['a'] for index in pair))
        res = count_a / len(unordered_tuple)
    else:
        res = 0.000000000000
    return round(res,12)
