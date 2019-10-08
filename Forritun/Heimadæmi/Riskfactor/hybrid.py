def create(filename):
    listinn=[]
    states=[]
    for line in filename:
        line_list=line.replace("%","").split(",")
        #búum til túplur
        rate_tuple=(line_list[1], line_list[5], line_list[7], line_list[11], line_list[13])
        state_tuple=(line_list[0])
        listinn.append(rate_tuple)
        states.append(state_tuple)
    return listinn,states
#þarf að búa til nýja túplu sem hefur 1) disease 2)max gildi 3)það state )4 min gildi 5) það state
def minmax(listinn,states):
    nyjilistinn=[]
    max_gildi=[]
    min_gildi=[]
    # fyrst þarf ég að finna max og min gildi í öllum listum.
    #(listinn[1:]) gefur mér allt fyrir utan heart og það
    for i in range(5):
        max_gildi.append(max(listinn[1:])[i])
        min_gildi.append(min(listinn[1:])[i])
    
    for rate_tuple in listinn:
        if rate_tuple[0] == max_gildi:
            nyjilistinn.append(rate_tuple)
        if rate_tuple[0] == min_gildi:
            nyjilistinn.append(rate_tuple)

    return max_milage_list, min_milage_list




#opna skránna
filename = open ("riskFactors.csv")
#kominn með þetta þokkalega flokkað
listinn, states = create(filename)
#finn max og min gildin
max_gildin, min_gildin = minmax(listinn,states)
#staðset þau til að finna fylkin
state=minmax(listinn,max_gildin,min_gildin)
#negli þessu í prentun








