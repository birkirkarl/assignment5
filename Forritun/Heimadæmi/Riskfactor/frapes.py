import math

heart_disease = []
motor = []
teen_birth = []
smoking = []
obesity = []
state = []

## fall sem prentar út höfuðsetningar, er nýtt á tveimur stöðum.
def headline():
    print("{:<33} {:<20} {:>5} {:6} {:<13} {:>5}".format("Indicator", "Min","","","Max",""))
    print("-"*87)

## fall sem finnur hæsta og lægst gildi og prentar út niðurstöður í töfluformi. 
def maxmin(x,state):
    max1 = 0
    min1 = math.inf
    s = [float(s.replace('%','')) for s in x[1:]]
    for value in enumerate(s):
        if value[1] > max1:
            max1 = value[1]
            maxplacement = value[0]
        elif value[1] < min1:
            min1 = value[1]
            minplacement = value[0]
    
    print("{:<33} {:<20} {:>5.1f} {:6} {:<13} {:>5.1f}".format(x[0]+ ":", state[minplacement+1],float(min1),"",state[maxplacement+1], float(max1)))

## Hér er skráin lesinn inn og sett á viðeigandi form. 
def Testfile(filename):
    try:
        with open(filename) as file:
            state = []
            for line in file:
                list_line = line.split(',') 
                state.append(list_line)
        return state
    except FileNotFoundError:
        print('Cannot find file ' + filename)
        headline()
        exit()
    
# Aðalkóðinn skal byrja hér. 
filename = input('Enter filename containing csv data: ')
files = Testfile(filename)
for i in files:
    heart_disease.append(i[1])
    motor.append(i[5])
    state.append(i[0])
    teen_birth.append(i[7])
    smoking.append(i[11])
    obesity.append(i[13])
headline()

heart_disease = maxmin(heart_disease,state)
motor = maxmin(motor, state)
teen_birth = maxmin(teen_birth, state)
smoking = maxmin(smoking, state)
obesity = maxmin(obesity, state)