import re
def css_properties(c):
    a = []
    b = []
    d = []

    if re.fullmatch('^[ ]*$', c):
        return []

    c = c.replace('\n', '')

    c = re.sub('}.*?{', '', c)
    c = re.sub('^.*?{', '', c)
    c = re.sub('}.*?$', '', c)
    c = re.sub('[ ]*:[ ]*', ':', c)
    c = c.split(';')

    for i in c:
        if re.fullmatch('^[ ]*$', i):
            break
        i = i.lstrip()
        i = i.rstrip()
        i = i.split(':')
        a.append(tuple(i))

    return a

