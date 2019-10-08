import itertools
def countdown(p, s):
    t = []
    r = []
    l = []

    with open(p) as text:
        for b in text:
            b = b.strip('\n')
            if len(b) > 3:
                t += [b]

    t = set(t)

    for i in range(4,10):
        l += list(''.join(w) for w in itertools.permutations(s, i))

    l = set(l)

    for i in t:
        if i in l:
            r += [i]

    return sorted(r)
