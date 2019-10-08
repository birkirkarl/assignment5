import datetime
import operator
import csv
def release_days(cast, dates, actors):
    usa = []
    mov = []
    rdat = {}
    with open(cast) as cfile:
        rcast = csv.reader(cfile)
        for i in rcast:
            if i[2] in actors:
                mov.append(i)

    with open(dates) as cfile:
        rdates = csv.reader(cfile)
        for i in rdates:
            if i[2] == 'USA':
                usa.append(i)
    for i in usa:
        for j in mov:
            if i[0] == j[0] and i[1] == j[1]:
                dagur = datetime.datetime.strptime(i[len(i) - 1], '%Y-%m-%d').strftime('%w')
                if dagur == '0':
                    dagur = '7'
                if eval(dagur) in rdat:
                    rdat[eval(dagur)].add(i[0])
                else:
                    rdat[eval(dagur)] = {i[0]}

    srdat = sorted(rdat.items(), key=operator.itemgetter(0))

    return dict(srdat)


#print(release_days('/Users/ellensigurdardottir/Documents/HR/cast.csv', '/Users/ellensigurdardottir/Documents/HR/date.csv', ['Meg Ryan', 'Tom Hanks']))
#{2: {'Kate & Leopold'},
 #3: {'A League of Their Own',
  #   'Catch Me If You Can',
  #   'Forrest Gump',
  #   'Innerspace',
  #   'Nothing in Common',
  #   'The Money Pit',
  #   'The Polar Express',
  #   'Toy Story',
  #   'Toy Story 2'},
# 5: {'Addicted to Love',
 #    'Against the Ropes',
 #    'Amityville 3-D',
 #    'Anastasia',
 #    'Angels & Demons',
 #    'Apollo 13',
 #    'Armed and Dangerous',
 #    'Bachelor Party',
 #    'Big',
 #    'Bridge of Spies',
 #    'Captain Phillips',
 #    'Cars',
 #    'Cast Away',
 #    "Charlie Wilson's War",
 #    'City of Angels',
 #    'Cloud Atlas',
 #    'Courage Under Fire',
 #    'D.O.A.',
 #    'Dragnet',
 #    'Extremely Loud & Incredibly Close',
 #    'Flesh and Bone',
 #    'French Kiss',
 #    'Hanging Up',
 #    "He Knows You're Alone",
 #    'Hurlyburly',
 #    'In the Cut',
 #    'In the Land of Women',
 #    "Io sono l'amore",
 #    'Joe Versus the Volcano',
 #    'Larry Crowne',
 #    'Philadelphia',
 #    'Prelude to a Kiss',
 #    'Proof of Life',
 #    'Punchline',
 #    'Radio Flyer',
 #    'Restoration',
 #    'Road to Perdition',
 #    'Saving Mr. Banks',
 #    'Saving Private Ryan',
 #    'Serious Moonlight',
 #    'Sleepless in Seattle',
 #    'Splash',
 #    'Sully',
 #    'That Thing You Do!',
 #    "The 'Burbs",
 #    'The Bonfire of the Vanities',
 #    'The Da Vinci Code',
 #    'The Doors',
 #    'The Great Buck Howard',
 #    'The Green Mile',
 #    'The Ladykillers',
 #    'The Man with One Red Shoe',
 #    'The Presidio',
 #    'The Queen',
 #    'The Simpsons Movie',
 #    'The Terminal',
 #    'Top Gun',
 #    'Toy Story 3',
 #    'Turner & Hooch',
 #    'Volunteers',
 #    'When Harry Met Sally...',
 #    'When a Man Loves a Woman',
 #    "You've Got Mail"},
 #7: {'I.Q.'}}

