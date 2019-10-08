
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(listi):
    tolur=[int(x) for x in listi if int(x)%2==0]
    summan=sum(tolur)
    return summan



# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))

