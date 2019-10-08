gi = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def toNum(c):
    if c.isnumeric():
        return int(c)
    else:
        return gi[c]

def rank_hand(l):
    n = 0
    r = ['T', 'J', 'Q', 'K', 'A']
    sp = [2, 3, 4, 5, 14]

    # Gildi spila
    g = []
    for i in l:
        g.append(toNum(i[0]))

    gs = sorted(g)

    #Tegund spila
    t = []
    for i in l:
        t.append(i[1])

    # Straight
    if len(set(t)) != 1:
        if max(g) - min(g) == 4:
            n = 4
        if sorted(g) == sp:
            n = 4

    # Flush
    rc = 0
    for i in l:
        if i[0] in r:
            rc += 1

    # Royal flush eða straight flush eða flush
    if (len(set(t))) == 1:
        if rc == 5:
            n = 9
        if max(g) - min(g) == 4 or sorted(g) == sp:
            n = 8
        if len(set(g)) == 5:
            n = 5

    # Four of a kind
    if len(set(i for i in g if g.count(i) == 4)):
        n = 7

    # Full house eða three of a kind
    if len(set(i for i in g if g.count(i) == 3)):
        if len(set(g)) == 2:
            n = 6
        if len(set(g)) > 2:
            n = 3

    # Two pair
    if len(set(i for i in g if g.count(i) == 2)) and len(set(g)) == 3:
        n = 2

    if len(set(i for i in g if g.count(i) == 2)) and len(set(g)) == 4:
        n = 1

    return n

print(rank_hand([ 'JD', 'KD', 'TD', 'QD', 'AD'])) #9
print(rank_hand([ '9H', '8H', '7H', '6H', '5H'])) #8
print(rank_hand([ '9L', '9S', '9D', '9H', '8H'])) #7
print(rank_hand([ '3L', '3H', '3D', '6L', '6H'])) #6
print(rank_hand([ '1H', '2H', '5H', 'TH', 'QH'])) #5
print(rank_hand([ '7L', '6S', '5S', '4H', '3H'])) #4
print(rank_hand([ '2D', '2H', '2L', 'KS', '6H'])) #3
print(rank_hand([ 'JH', 'JL', '4L', '4S', '9H'])) #2
print(rank_hand([ '4H', '4S', 'KS', 'TD', '5S'])) #1
print(rank_hand([ '3C', '4C', '2C', '5C', '6C'])) #8
print(rank_hand([ '9H', 'KS', '4H', '8S', 'JS'])) #0
print(rank_hand([ '4D', '5D', '2D', 'AD', '3D'])) #8
print(rank_hand([ 'AH', '2C', '3S', '5D', '4D'])) #4
