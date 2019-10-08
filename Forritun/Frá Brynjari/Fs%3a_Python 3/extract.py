import re
def extract(s):
    l = []
    g = ['4', '5', '6', '7', '8', '9', '10', 'S', 'M']
    skil = []
    tiu = ['1', '0']

    if s == ',.':
        return []

    s = s.upper()
    s = s.replace(' ', '')
    s = s.replace('L', '1')
    s = s.replace('O', '0')
    s = s.replace('10', 'T')
    s = s.replace('1 0', 'T')

    for i in s:
        i = i.upper()
        i = i.replace('L', '10')
        if i.isalnum():
            if i == '100':
                i = i.replace('100', '10')
            l.append(i)

    if l == tiu:
        return ['10']

    c0 = 0
    c1 = 0
    for i in l:
        if i == '0':
            c0 += 1
        elif i == '1':
            c1 += 1

    if c0 > c1:
        return None

    for i in l:
        if i == '2' or i == '3' or i == '0':
            return None

    for i in l:
        if i == 'T' or i in g :
            i = i.replace('T', '10')
            skil.append(i)
        else:
            return None

    if skil == []:
        return None

    return skil
