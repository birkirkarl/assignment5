def get_list():
    listi = input("Enter elements of list separated by commas: ").strip().split(',')
    return listi

def get_integer(x):
    tala = int(input(x))
    return tala

def transform(l1, l2, i1, i2):
    ehv = l1[i1:i2]
    ehv.reverse()
    for i in range(0,len(ehv)):
        l1.remove(ehv[i])
        l2.append(ehv[i])


# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)