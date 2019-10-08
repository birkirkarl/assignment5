import datetime
import re
import csv
def release_days(cast, dates, actors):
    dick = {'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7}
    c = []
    ca = []
    d = []
    movie = []
    dagur = []
    rdagur = []
    da = []
    s = ''
    k = []
    di = []

    for i in actors:
        for j in open(cast):
            if i in j:
                c.append(j)
                print(j)

    for i in c:
        i = i.split(',')
        movie.append(i[0])

    for i in movie:
        for j in open(dates):
            if ('USA') in j:
                if i in j:
                    j = j.strip('\n')
                    d.append(j)

    d = set(d)

    for i in d:
        i = i.split(',')
        dagur.append(i)

    for i in dagur:
        if i[0] in movie:
            rdagur.append(i)

    for i in rdagur:
        for j in i:
            if re.match(r'^[\d]{4}-[\d]{2}-[\d]{2}$', j):
                j = datetime.datetime.strptime(j, '%Y-%m-%d').strftime('%w')
                if j == '0':
                    j = '7'
                da.append(j)
                da.append('*')
            else:
                da.append(j)

    s = ' '.join(da)
    s = s.split('*')

    for i in s:
        i = i.lstrip()
        i = i.rstrip()
        i = re.sub(r' [\d]{4} USA ', '', i)
        if i != '':
            k.append(i)

    #print(k)

    #for i in di:
     #   if i[len(i)-1] in di:
      #      (i[len(i) - 1]).append(i[0:len(i)-1])
       # else:


#    for i in k:
 #       i = (i[0:len(i)-1], eval(i[len(i)-1]))
  #      di.append(i)

#    di = dict(di)

#    print(di)


    #print('da', da)

    return 'ELLEN'







print(release_days('/Users/ellensigurdardottir/Documents/HR/cast.csv', '/Users/ellensigurdardottir/Documents/HR/date.csv', ['Meg Ryan', 'Tom Hanks']))
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
