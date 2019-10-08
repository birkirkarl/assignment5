#Folksfjoldi verkefni1

upphafsfjoldi= 307357870

arafjoldi=input('Years: ')
arafjoldi= int(arafjoldi)

sekiari=365*24*60*60

faed= sekiari/7
ded=sekiari/13
imm=sekiari/35

fjolgunaari= faed+imm-ded

fjoldi=upphafsfjoldi+arafjoldi*fjolgunaari

if arafjoldi >= 0:
    print('New population after''years is')
else:
    print('Invalid input')
