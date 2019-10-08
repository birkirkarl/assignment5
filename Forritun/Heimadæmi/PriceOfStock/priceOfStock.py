#hef int i öllu til að checka hvort þetta séu tölur

def brefin():
    global out1
    global bref
    while out1==False:
        bref=input('Enter number of shares: ')
        try:
            bref = int(bref)
            out1=True
            return
        except ValueError or SyntaxError or NameError:
            print("Invalid number!")

def theprice():
    global out2
    global bref
    while out2==False:
        try:
            price=input('Enter price (dollars, numerator, denominator): ')
            x,y,z=price.split(" ")# splitta þessu í sitthvorar tölurnar frá því að vera í string
            num= int(x)
            num1= int(y)
            num2= int(z)
            verd="{0:.2f}".format(bref*(num+num1/num2))
            out2=True
            return print('%d shares with market price %d %d/%d have value $%s' %(bref,num,num1,num2,verd))
        except ValueError or SyntaxError or TypeError or NameError:# gerði alla þessa errors bara til að vera viss um að fara í exception en ekki að fá villu.
            print("Invalid price!")


out1=False
out2=False
afram='y'
while afram == 'y': # aðal loopan sem lætur allt keyrast
    brefin()
    theprice()
    afram=input("Continue: ")
    if afram=='y':
        out1=False # endurstilli gildin svo function keyrist aftur
        out2=False
