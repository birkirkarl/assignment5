import re

def mavera(ord, k, g):
    l = []
    for i in range(len(k)):
        if k[i] == ord[i] or k[i] == '-' and ord[i] not in g and not ord[i].isupper():
            l.append(ord[i])

    l = ''.join(l)

    return ord == l


def hangman(f, k, g):
    moguleg = []

    bannstafir = []
    for i in g:
        bannstafir.append(i)

    with open(f) as text:
        for i in text:
            i = i.strip('\n')
            i = i.replace("'s", '')
            if re.match("^[a-z]*$", i):
                if len(i) == len(k):
                    moguleg += [i]

    skil = []

    for i in moguleg:
        if mavera(i, k, bannstafir) == True:
            skil.append(i)

    return set(skil)
