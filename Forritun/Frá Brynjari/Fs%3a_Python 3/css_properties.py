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


#print(css_properties('',))
print(css_properties('a { color:pink; }',))
print(css_properties('''{margin:   0;}
{outline   :thin dotted;}
{font-size:   2em;margin:0.67em 0;}
{font-weight:bold;}
{font-style    :italic;}
{-moz-box-sizing:content-box;box-sizing:content-box;height:0;}
{background:#ff0;color:#000;}
{font-family: monospace, serif;font-size:1em;}
{white-space:pre-wrap;}
{font-size:80%;}
{font-size:75%;line-height:0;position:relative;vertical-align:baseline;}
{top:-0.5em;}
{bottom:-0.25em;}\
{border:0;}
{margin:0;}'''))


