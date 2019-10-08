import string
def merge_lists(list1, list2):
    listi3= list1+list2
    listi3=list(set(listi3))
    listi3.sort()
    return listi3



# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
