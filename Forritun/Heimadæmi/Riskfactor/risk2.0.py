

#hérna negli ég öllu í lista og túplur.
def create(filename):
    listinn=[]
    states=[]
    for line in filename:
        if "Heart" in line:
            continue
        line_list=line.split(',')
        #búum til túplu
        rate_tuple=(line_list[1], line_list[5], line_list[7], line_list[11], line_list[13])
        state_tuple=(line_list[0])
        listinn.append(rate_tuple)
        states.append(state_tuple)
    return listinn,states


# hérna finn ég max min og state.
def minmax(listinn,max_gildin,min_gildin):
    global states
    max_listi2=[]
    min_listi2=[]
    max_state=[]
    min_state=[]
    counter1=0
    counter2=0
    for rate_tuple in listinn:
        if rate_tuple[0]==listinn:
            max_listi2.append(rate_tuple)
        if rate_tuple[0] == listinn:
            min_listi2.append(rate_tuple)
        if max_listi2==[]:
            counter1+=1
        if min_listi2==[]:
            counter2+=1
    max_state.append(states[counter1])
    min_state.append(states[counter2])
    return max_listi2, min_listi2, max_state, min_state

def hvertgildi(listinn):
    print(listinn)
    max_gildin=[]
    min_gildin=[]
    for i in range(5):
        max_gildin.append(max(listinn)[i])
        min_gildin.append(min(listinn)[i])
    return max_gildin,min_gildin


#opna skránna
filename = open ("riskFactors.csv")
#kominn með þetta þokkalega flokkað
listinn, states = create(filename)
#finn max og min gildin
max_gildin, min_gildin = hvertgildi(listinn)
#staðset þau til að finna fylkin
state=minmax(listinn,max_gildin,min_gildin)
#negli þessu í prentun


