gi = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def tn(c):
    if c.isnumeric():
        return int(c)
    else:
        return gi[c]

def rank_hand(l):
    n = 0
    r = ['T', 'J', 'Q', 'K', 'A']
    sp = [2, 3, 4, 5, 14]

    g = []
    for i in l:
        g.append(tn(i[0]))

    t = []
    for i in l:
        t.append(i[1])

    if len(set(t)) != 1:
        if max(g) - min(g) == 4:
            n = 4
        elif sorted(g) == sp:
            n = 4

    rc = 0
    for i in l:
        if i[0] in r:
            rc += 1

    if (len(set(t))) == 1:
        if rc == 5:
            n = 9
        elif max(g) - min(g) == 4 or sorted(g) == sp:
            n = 8
        elif len(set(g)) == 5:
            n = 5

    if len(set(i for i in g if g.count(i) == 4)):
        n = 7

    if len(set(i for i in g if g.count(i) == 3)):
        if len(set(g)) == 2:
            n = 6
        elif len(set(g)) > 2:
            n = 3

    if len(set(i for i in g if g.count(i) == 2)) and len(set(g)) == 3:
        n = 2

    if len(set(i for i in g if g.count(i) == 2)) and len(set(g)) == 4:
        n = 1

    return n
