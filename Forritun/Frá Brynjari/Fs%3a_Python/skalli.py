import re
from fractions import Fraction

def skalli(u, s):
    if u.isdigit() or ('/') in u:
        if '/' in u and ' ' in u:
            u = u.split(' ')
            a = Fraction(u[0]) + Fraction(u[1])
            a *= Fraction(s)
            e = Fraction(a)
            if int(e) != 0:
                if int(e) != e:
                    rest = e - int(e)
                    e = str(int(e)) + ' ' + str(Fraction(rest))
        else:
            b = Fraction(u) * Fraction(s)
            e = Fraction(b)
            if int(e) != 0:
                if int(e) != e:
                    rest = e - int(e)
                    e = str(int(e)) + ' ' + str(Fraction(rest))
    return str(e)

def scale(n, m):
    tala = re.compile(r'[\d]+[ ][\d]+/[\d]+|[\d]+/[\d]+|[\d]+')
    tala.findall(n)
    return tala.sub(lambda ha: skalli(ha.group(), m), n)
