from pathlib import Path
import re
prob = re.compile(r'Problem (\d[ ]*\w+)')
team = re.compile(r'Team[ ]*(\w+)')
dat = re.compile(r'Date[ ]*(\w+)')

def get_prob(skra):
    if 'Accepted' in skra:
        da = dat.findall(skra)
        te = team.findall(skra)
        pr = prob.findall(skra)
        sda = ''.join(da)
        ste = ''.join(te)
        spr = ''.join(pr)
        return (sda, ste, spr)

def parse_submissions(dire):
    p = Path(dire)
    lok = []
    verkefni = []
    for i in p.glob('*/data.tcl'):
        verk = get_prob(i.read_text(encoding='utf-8'))
        if verk != None:
            verkefni.append(verk)

    verkefni = sorted(verkefni, key=lambda x: x[0])

    for i in verkefni:
        lok.append(i[1:3])

    return lok

