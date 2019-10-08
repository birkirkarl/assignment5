field = ''
#Set inn upphafsskilyrði
position = int(input('Input a position between 1 and 10: '))

#Nota for lykkju til að láta notandann setja inn o eða x
for i in range(0,10):
    if i == position -1:
        field += 'o'
    else:
        field += 'x'
print(field)

#Prenta út skilyrðin
print('l - for moving left')
print('r - for moving right')
print('Any other letter for quitting')


direction = input('Input your choice: ')
#Nota while lykkju til að fara úr forritunni ef það kemur hvorki r né l.

while direction == 'r' or direction == 'l':
    
    field = ''

    #Keyrum for lykkjuna aftur og bætum við einum.
    if direction == 'r':
        position += 1
        #Set hámarksskilyrði 10
        if position > 10:
            position = 10
        for i in range(0,10):
            if i == position -1:
                field += 'o'
            else:
                field += 'x'
        print(field)
    elif direction == 'l':
        #Set núna lágmarksskilyrði fyrir notandann
        position -= 1
        if position < 1:
            position = 1
        for i in range(0,10):
            if i == position -1:
                field += 'o'
            else:
                field += 'x'
        
        print(field)
    
    direction = input('Input your choice: ')


print(field)