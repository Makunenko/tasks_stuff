
def permutation_main(lst):
    if len(lst) <= 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        if lst[i] == '0':
            continue
        m = lst[i]
        remlst = lst[:i] + lst[i + 1:]
        for p in permutation(remlst):
            n = m + p
            if n not in l:
                l.append(n)
    return l


def permutation(lst):
    if len(lst) <= 1:
        return lst
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remlst = lst[:i] + lst[i+1:]
        for p in permutation(remlst):
            l.append(m + p)
    return l


data = '1230'
print(permutation_main(data))
