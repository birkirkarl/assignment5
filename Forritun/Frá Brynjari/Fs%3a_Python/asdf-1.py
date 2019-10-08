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
    print('e', e)

    e = Counter(e)
    e = sorted(e.items())

    return dict(e)


print(jam("""1/1/1 22 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Wilma Ewart and Beryl Reid, excuses for being late.
2/1/2 29 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Sheila Hancock and Carol Binstead, bedrooms.
3/1/3 5 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Betty Marsden and Elisabeth Beresford, ?
4/1/4 12 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Isobel Barnett and Bettine Le Beau, ?
5/1/5 20 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Prunella Scales, the brownies
6/1/6 27 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Marjorie Proops and Millie Small, ?
7/1/7 2 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Aimi Macdonald and Una Stubbs, my honeymoon.
8/1/8 9 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Lucy Bartlett and Anona Winn, bloomer.
9/1/9 17 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, ?
10/1/10 23 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Barbara Blake and Renee Houston, my first grown-up dress."""))
