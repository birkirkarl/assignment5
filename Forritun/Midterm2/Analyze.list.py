def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True


def get_numbers(get):
    nytt_inntak=[]
    nytt=get.split(',')
    try:
        for i in range(len(nytt)):
            tala=nytt[i]
            tala=int(tala)
            nytt_inntak.append(tala)
        print("Input list:",nytt_inntak)
        return nytt_inntak   
    except:
        return print('Incorrect input!')

def makeaverages(sumslist,totalint):
    averages_list = []
    for value_int in sumslist:
        averages_list.append(value_int/total_int) 
    return averages_list

def sortari(nytt_inntak):
    sortad=sorted(nytt_inntak,key=int)
    print('Sorted list: ',sortad)
    return sortad
def minmax(sortad):
    summa=0
    counter=0
    minval=sortad[0]
    maxval=sortad[-1]
    for i in sortad:
        summa+=int(i)
        counter+=1
    ave=float(summa/counter)
    print("Min:"'%d'', Max:'"%d"', Average:',"%.2f" %minval,%maxval,%ave)
    return maxval,minval,ave
def allarprim(nytt_inntak):
    prime_tolur=[]
    for i in nytt_inntak:
        if is_prime(int(i)):
            prime_tolur.append(int(i))
    print('Prime list: ',sorted(list(set(prime_tolur))))
# The main program starts here

get=input("Enter integers separated with commas: ")
nytt_inntak=get_numbers(get)
sortad=sortari(nytt_inntak)
allarprim(nytt_inntak)
minmax(sortad)


