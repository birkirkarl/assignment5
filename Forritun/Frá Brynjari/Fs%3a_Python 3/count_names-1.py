from urllib.request import urlopen
import json

def count_names(start):
    a = []
    f1 = []
    f2 = []
    s1 = 0
    s2 = 0

    with urlopen('http://mooshak.ru.is/~python/names.json') as op:
        dot = json.loads(op.read())

    for i in dot:
        for k in i:
            print(k)
            if k == 'Nafn' and i[k].startswith(start):
                a.append(i)

    print(a)

    for i in a:
        for k in i:
            if k == 'Fjoldi2':
                f1.append(i[k])
            elif k == 'Fjoldi1':
                f2.append(i[k])

    for i in f1:
        i = eval(i)
        s1 += i
    print(s1)

    for i in f2:
        i = eval(i)
        s2 += i
    print(s2)

    return (s2, s1)
