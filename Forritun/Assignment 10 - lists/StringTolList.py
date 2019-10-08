def to_list(the_string):
    the_string = the_string.replace(","," ")
    the_list = the_string.split(" ")
    return the_list
    
the_string = input("Enter the string: ")
the_list = to_list(the_string)

print(the_list)
