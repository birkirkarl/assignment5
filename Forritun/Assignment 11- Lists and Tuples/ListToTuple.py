
def list_to_tuple(a_list):
    try:
        a_list=[int(a) for a in a_list]
        a_tuple=tuple(a_list)
    except:
        print("Error. Please enter only integers.")
        a_tuple=()
    return a_tuple





# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)