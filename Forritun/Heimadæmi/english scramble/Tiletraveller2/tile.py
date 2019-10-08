#1. fyrri var auðveldari því ég byrjaði á því og gerði bara hlutina nákvæmlega eins og ég hugsaði.
#2. seinni er lesanlegri því það meikar allt meira sense ( brotið upp)
#3. við leystum það að koma kóðanum yfir í lesanlegra form.
#https://github.com/eirikuratli/tileTraveller/blob/master/filetraveller2.py
option1='(N)orth'
option2='(S)outh'
option3='(E)ast'
option4='(W)est'
# Staðsetning reitanna skilgreind
loc11 = 11
loc12 = 12
loc13 = 13
loc21 = 21
loc22 = 22
loc23 = 23
loc31 = 31
loc32 = 32
loc33 = 33
summan=0
loc = loc11
def box1(loc): 
    #reitur 1.1 og reitur 2.1, og sýnir hvaða möguleikar eru
    #í boði fyrir notanda og lætur hann svo ákveða
    #skilar svo nýrri staðsetningu
    val=0
    print('You can travel: %s.' % (option1))
    while val==0:
        direction=input('Direction: ')
        if direction=='n' or direction=='N':
            val += 1
            loc += 1
        else:
            print('Not a valid direction!')
    return loc
def box2(loc):
    
    #Reitur 1.2 og sýnir hvaða möguleikar eru
    #í boði fyrir notanda og lætur hann svo ákveða
    #skilar svo nýrri staðsetningu
    lever()
    val=0
    print('You can travel: %s or %s or %s.' %(option1,option3,option2))
    while val==0:
        direction=input('Direction: ')
        if direction=='n' or direction=='N':
            val += 1
            loc += 1
        elif direction=='s' or direction=='S':
            val += 1
            loc -= 1
        elif direction=='e' or direction=='E':
            val +=1
            loc += 10
        else:
            print('Not a valid direction!')
    return loc
def box3(loc):
    
    #reitur 1.3 og sýnir hvaða möguleikar eru
    #í boði fyrir notanda og lætur hann svo ákveða
    #skilar svo nýrri staðsetningu
    
    val=0
    print('You can travel: %s or %s.' %(option3,option2))
    while val==0:
        direction=input('Direction: ')
        if direction=='s' or direction=='S':
            val += 1
            loc -= 1
        elif direction=='e' or direction=='E':
            val += 1
            loc += 10
        else:
            print('Not a valid direction!')
    return loc
def box5(loc):
    
    #reitur 2.2 og reitur 3.3, og sýnir hvaða möguleikar eru
    #í boði fyrir notanda og lætur hann svo ákveða
    #skilar svo nýrri staðsetningu
    if loc == 22:
        lever()
    val=0
    print('You can travel: %s or %s.' %(option2,option4))
    while val==0:
        direction=input('Direction: ')
        if direction=='s' or direction=='S':
            val += 1
            loc -= 1
        elif direction=='w' or direction=='W':
            val += 1
            loc -= 10
        else:
            print('Not a valid direction!')
    return loc
def box6(loc):
    
    #reitur 2.3 og sýnir hvaða möguleikar eru
    #í boði fyrir notanda og lætur hann svo ákveða
    #skilar svo nýrri staðsetningu
    lever()
    val=0
    print('You can travel: %s or %s.' %(option3,option4))
    while val==0:
        direction=input('Direction: ')
        if direction=='w' or direction=='W':
            val += 1
            loc -= 10
        elif direction=='e' or direction=='E':
            val += 1
            loc += 10
        else:
            print('Not a valid direction!')
    return loc
def box8(loc):
    
    #reitur 3.2 og sýnir hvaða möguleikar eru
    #í boði fyrir notanda og lætur hann svo ákveða
    #skilar svo nýrri staðsetningu
    lever()
    val=0
    print('You can travel: %s or %s.' %(option1,option2))
    while val==0:
        direction=input('Direction: ')
        if direction=='n' or direction=='N':
            val += 1
            loc += 1
        elif direction=='s' or direction=='S':
            val += 1
            loc -= 1
        else:
            print('Not a valid direction!')
    return loc


def lever():
    global summan
    lev=input("Pull a lever (y/n): ")
    if lev == 'y' or lev == 'Y':
        summan += 1
        print("You received 1 coins, your total is now %d." %(summan))


def play():
    loc = loc11
    while loc!=loc31:
        if loc == loc11 or loc == loc21:
            loc = box1(loc)
        elif loc == loc12:
            loc = box2(loc)
        elif loc == loc13:
            loc = box3(loc)
        elif loc == loc22 or loc == loc33:
            loc = box5(loc)
        elif loc == loc23:
            loc = box6(loc)
        elif loc == loc32:
            loc = box8(loc)
    print('Victory!')
    aftur=input("Play again (y/n): ")
    if aftur == 'y':
        play()
#------------------------------
play()

