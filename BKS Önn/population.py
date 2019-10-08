#Folksfjoldi verkefni1

upphafsfjoldi= 307357870

arafjoldi=input('Years: ')
arafjoldi= int(arafjoldi)

sekiari=365*24*60*60

faed= int(sekiari/7)
ded= int(sekiari/13)
imm=int(sekiari/35)

fjolgunaari= int(faed+imm-ded)

fjoldi=int(upphafsfjoldi+arafjoldi*fjolgunaari)

if arafjoldi >= 0:
    print('New population after years is', fjoldi)
else:
    print('Invalid input')
