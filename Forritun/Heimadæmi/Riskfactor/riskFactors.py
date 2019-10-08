counter=0
def headline(): #aðalheadline
    print("{:<33} {:<20} {:>5} {:6} {:<13} {:>5}".format("Indicator", "Min","","","Max",""))
    print("-"*87)

def create(file_name):#opna og prufa hvort sé rétt
    try:
        filename=open(file_name)
        return filename
    except FileNotFoundError:
        print('Cannot find file ' + file_name)
        headline()

def flokkar(filename):
    l1=[] # Heart Disease Death Rate [1]
    l2=[] # Motor Vehicle Death Rate [5]
    l3=[] # Teen Birth Rate [7]
    l4=[] # Adult Smoking [11]
    l5=[] # Adult Obesity [13]
    states=[] #duh
    for line in filename:
        line_list=line.replace("%","").split(",")
        if "Heart" in line:
            diseases_tuple=(line_list[1],line_list[5],line_list[7],line_list[11],line_list[13])
            continue
        states.append(line_list[0])
        l1.append(float(line_list[1]))
        l2.append(float(line_list[5]))
        l3.append(float(line_list[7]))
        l4.append(float(line_list[11]))
        l5.append(float(line_list[13]))

    return l1,l2,l3,l4,l5,states,diseases_tuple



def get_max_value(l,states): # max gildi og index reitur þess til að kalla í state

    max_val=max(l)
    state=states[l.index(max_val)]

    return max_val, state
  
def get_min_value(l, states): # min gildi og index reitur þess til að kalla í state

    min_val=min(l)
    state=states[l.index(min_val)]

    return min_val, state

#Hér hefst aðalloopan
file_name = input('Enter filename containing csv data: ')
name=create(file_name)

l1,l2,l3,l4,l5,states,diseases=flokkar(name)

headline()

list_tuple=[l1,l2,l3,l4,l5]

for i in list_tuple: # prentarinn
    maxval,maxstate=get_max_value(i,states)
    minval,minstate=get_min_value(i,states)
    ehv= diseases[counter]
    print("{:<33} {:<20} {:>5.1f} {:6} {:<13} {:>5.1f}".format(ehv+ ":", minstate,minval,"",maxstate,maxval))
    counter+=1






