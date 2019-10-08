option1='(N)orth'
option2='(S)outh'
option3='(E)ast'
option4='(W)est'

loc=11
while loc!=31:
    if loc== 11 or loc == 21:
        val=0
        print(" You can travel: %s." % (option1))
        while val==0:
            att=input('Direction:')
            if att=='n' or att=='N':
                val += 1
                loc += 1
            else:
                print(' Not a valid direction!')
    elif loc == 32:
        val=0
        print(" You can travel: %s or %s." %(option1,option2))
        while val==0:
            att=input('Direction:')
            if att=='n' or att=='N':
                val += 1
                loc += 1
            elif att=='s' or att=='S':
                val += 1
                loc -= 1
            else:
                print(' Not a valid direction!')
    elif loc == 12:
        val=0
        print(" You can travel: %s or %s or %s." %(option1,option3,option2))
        while val==0:
            att=input('Direction:')
            if att=='n' or att=='N':
                val += 1
                loc += 1
            elif att=='s' or att=='S':
                val += 1
                loc -= 1
            elif att=='e' or att=='E':
                val +=1
                loc +=10
            else:
                print(' Not a valid direction!')
    elif loc == 13:
        val=0
        print(" You can travel: %s or %s." %(option3,option2))
        while val==0:
            att=input('Direction:')
            if att=='s' or att=='S':
                val += 1
                loc -= 1
            elif att=='e' or att=='E':
                val += 1
                loc += 10
            else:
                print(' Not a valid direction!')
    elif loc == 22 or loc == 33:
        val=0
        print(" You can travel: %s or %s." %(option2,option4))
        while val==0:
            att=input('Direction:')
            if att=='s' or att=='S':
                val += 1
                loc -= 1
            elif att=='w' or att=='W':
                val += 1
                loc -= 10
            else:
                print(' Not a valid direction!')
    elif loc == 23:
        val=0
        print(" You can travel: %s or %s." %(option3,option4))
        while val==0:
            att=input('Direction:')
            if att=='w' or att=='W':
                val += 1
                loc -= 10
            elif att=='e' or att=='E':
                val += 1
                loc += 10
            else:
                print(' Not a valid direction!')

print(" Victory!")
