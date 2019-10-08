import re
from fractions import Fraction

def skalli(u, s):
    if u.isdigit() or ('/') in u:
        if '/' in u and ' ' in u:
            u = u.split(' ')
            a = Fraction(u[0]) + Fraction(u[1])
            a *= Fraction(s)
            b = Fraction(a)
            if int(b) != 0:
                rest = b - int(b)
                e = str(int(b)) + ' ' + str(Fraction(rest))
        elif '/' in u:
            b = Fraction(u) * Fraction(s)
            c = Fraction(b)
            if int(c) != 0:
                rest = c - int(c)
                e = str(int(c)) + ' ' + str(Fraction(rest))
        elif '/' in u:
        b = Fraction(u) * Fraction(s)
        e = Fraction(b)
        if int(e) != 0:
            if int(e) != e:
                rest = e - int(e)
                e = str(int(e)) + ' ' + str(Fraction(rest))
        else:
            b = Fraction(u) * Fraction(s)
            c = Fraction(b)
            if int(c) != 0:
                if int(c) != c:
                    rest = c - int(c)
                    e = str(int(c)) + ' ' + str(Fraction(rest))
    return

print(scale('''Ingredients

    4 skinless, boneless chicken thighs
    1/2 cup soy sauce
    1/2 cup ketchup
    1 1/3 cup honey
    3 cloves garlic, minced
    1 teaspoon dried basil''', '1/2'))

'''Ingredients

    2 skinless, boneless chicken thighs
    1/4 cup soy sauce
    1/4 cup ketchup
    1/6 cup honey
    1 1/2 cloves garlic, minced
    1/2 teaspoon dried basil'''


print(skalli('4', '1/2'))
