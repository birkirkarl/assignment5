
def make_sublists(a_list):
    tomur=[]
    counter=0
    for i in a_list:
        if i==',':
            continue
        tomur.append(list(i))
        counter+=1
    return tomur,counter

def bull(tomur,counter):
    ehv=[]
    teljari=0
    for i in tomur:
        if teljari==counter:
            continue
        elif teljari==0:
            ehv.append(i)
            teljari+=1
        else:
            ehv.append(i)
            for j in range(teljari):
                ehv.append(i)
            teljari+=1



#main
a_list=input('Enter a list separated with commas: ')
tomur,counter=make_sublists(a_list)
bull(tomur,counter)
