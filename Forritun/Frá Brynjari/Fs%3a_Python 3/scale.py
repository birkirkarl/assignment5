import re
from fractions import Fraction
def skal(m):

    tala = re.compile(r'[\d]+[ ][\d]+/[\d]+|[\d]+/[\d]+|[\d]+')
    #tala.findall(n)
    return


def scale(u, s):
#    l = []

 #   u = u.splitlines()

#    for i in u:
 #       i = i.lstrip()
  #      i = i.rstrip()
   #     i = i.split(' ')
    #    l.append(i)

#    l = list(filter(None, l))

    for i in l:
        if i[0].isdigit() or ('/') in i[0]:
            t = ' '.join(i)
            if '/' in t[3]:
                print(i[:2])
                a = Fraction(i[0]) + Fraction(i[1])
                a *= Fraction(s)
                b = Fraction(a)
                print(b)
                if int(b) != 0:
                    rest = b - int(b)
                    rest = str(int(b)) + ' ' + str(Fraction(rest))
                    print(rest)
            elif '/' in t[1]:
                print(i[:1])
                b = Fraction(i[0]) * Fraction(s)
                c = Fraction(b)
                print(c)
                if int(c) != 0:
                    rest = c - int(c)
                    rest = str(int(c)) + ' ' + str(Fraction(rest))
                    print(rest)
            else:
                print(i[:1])
                b = Fraction(i[0]) * Fraction(s)
                c = Fraction(b)
                print(c)
                if int(c) != 0:
                    if int(c) != c:
                        rest = c - int(c)
                        rest = str(int(c)) + ' ' + str(Fraction(rest))
                        print(rest)

    return 'Ellen er best'

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

