


def get_input():
    a_name = input("Name: ")
    a_ssn = input("Number: ")
    get_more_data = input("More data (y/n)? ")
    return a_name, a_ssn, get_more_data

def add_to_dict(a_dict, key, value):
    a_dict[key] = value

def crea_list_of_tuples_from_dict(a_dict):
    a_list = []
    for key, value in a_dict.items():
        a_tuple=(key, value)
        a_list.append(a_tuple)
    return a_list
    


a_dict = {}

get_more_data="y"
while get_more_data=="y":
    a_name, a_ssn, get_more_data=get_input()
    add_to_dict(a_dict, a_name, a_ssn)
a_list=crea_list_of_tuples_from_dict(a_dict)
print(sorted(a_list))