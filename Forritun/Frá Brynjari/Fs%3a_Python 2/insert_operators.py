from itertools import zip_longest as zl
from itertools import product as pro
def insert_operators(r, s):
    t = []
    a = []

    for i in pro((' + ', ' - ', ''), repeat=len(r) - 1):
        t.append(i)
        a.append(''.join((''.join(map(str, l))) for l in list(zl(r, i, fillvalue=''))))

    for i in a:
        if eval(i) == s:
            return i + ' = ' + str(s)

print(insert_operators([1,2,3,4],13))