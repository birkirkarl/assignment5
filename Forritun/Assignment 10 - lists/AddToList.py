# Your functions should appear here
def populate_list(initial_list):
    value = input("Enter value to be added to list: ")    
    while value.upper() != 'EXIT':
        initial_list.append(value)
        value = input("Enter value to be added to list: ")                
    return initial_list


def triple_list(initial_list):
    new_list = initial_list*3
    return new_list
# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
