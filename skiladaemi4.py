def hreyfing(x):
    global pos   
    if x == 'l':
        if pos==1:
            print('New position is:',pos )
        else:
            pos= pos - 1
            print('New position is:',pos )
    elif x == 'r':
        if pos ==10:
            print('New position is:',pos )
        else:
            pos= pos + 1
            print('New position is:',pos )

val='l'
pos=int(input('Input a position between 1 and 10: '))
while val == 'l' or val == 'r':
    print('l - for moving left\nr - for moving right\nAny other letter for quitting')
    val=str(input('Input your choice: '))
    hreyfing(val)
print('New position is:',pos )