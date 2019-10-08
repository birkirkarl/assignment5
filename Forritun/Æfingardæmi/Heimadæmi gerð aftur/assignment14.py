# Example:

# Name: pranshu

# Number: 517-244-2426

# More data (y/n)? y

# Name: rich

# Number: 517-842-5425

# More data (y/n)? y

# Name: alireza

# Number: 517-432-5224

# More data (y/n)? n


# [('alireza', '517-432-5224'), ('pranshu', '517-244-2426'), ('rich', '517-842-5425')]


def dictmaker():
    global More_data
    while More_data:
        a_dict={}
        key=input('Name: ')
        value=input('Number: ')
        a_dict[key]=value
        more=input("More data (y/n)? ")
        if more== 'n':
            More_data=False

    return a_dict

More_data= True
a_dict=dictmaker()
print(a_dict)
