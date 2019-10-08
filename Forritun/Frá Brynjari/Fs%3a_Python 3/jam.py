import re
from collections import Counter
def jam(s):
    l = []
    a = []
    b = []
    c = []
    d = []
    e = []

    s = s.splitlines()
    for i in s:
        l.append(i)

    for i in l:
        i = re.split(', ', i)
        a.append(i)


    for i in a:
        b.append(i[1:-1])

    for i in b:
        for j in i:
            c.append(j)

    for i in c:
        i = re.split(' with | and ', i)
        d.append(i)

    for i in d:
        for j in i:
            if j[0].isupper():
                e.append(j)
            else:
                j = j.replace('plus ', '')
                e.append(j)

    e = Counter(e)
    e = sorted(e.items())

    return dict(e)
