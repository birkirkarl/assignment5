
# student= {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}

# #student['phone'] = '555-5555'

# #student.update({'name':'jane','age':26, 'phone': '555-555'})

# #del student['age']

# #age = student.pop('age')

# #print(len(student)) gefur hve margir keys.

# #print(student.keys()) fáum alla keys

# #print(student.items()) fáum keys og values

# #for key, value in student.items()
# #   print(key,value)
# Name: pranshu

# Number: 517-244-2426

# More data (y/n)? y

# Name: rich

# Number: 517-842-5425

# More data (y/n)? y

# Name: alireza

# Number: 517-432-5224

# More data (y/n)? n




# def get_info():
#     name=input('Name: ')
#     number=input('Number: ')
#     return name, number

# def create_dictionary(name,number):
#     global main_dict
#     if name in main_dict:
#         pass
#     else:
#         main_dict[name]=number
#     return main_dict

# def create_list_tuples(main_dict):
#     a_list=[]
#     for key, value in main_dict.items():
#         a_tuple=(key,value)
#         a_list.append(a_tuple)
#     return a_list
# More_data = True
# main_dict={}
# while More_data:
#     name,number=get_info()
#     create_dictionary(name,number)
#     more=input('More data (y/n)?')
#     if more == 'n':
#         More_data = False

# a_list=create_list_tuples(main_dict)
# print(sorted(a_list))
# import string

# def fileopener():
#     filename=input('Input the filename: ')
#     the_file=open(filename,'r')
#     return the_file

# def file_worker(the_file):
#     word_dict={}
#     for sentence in the_file:
#         sentence=sentence.strip(string.punctuation).strip().lower().split(' ')
#         for word in sentence:
#             if word not in word_dict:
#                 word_dict[word]=1
#             else:
#                 word_dict[word]+=1
#     return word_dict

# def dictionary_to_tuple(word_dict):
#     a_list=[]
#     for key, value in word_dict.items():
#         a_tuple=(key,value)
#         a_list.append(a_tuple)
#     return sorted(a_list)

# def main():
#     the_file=fileopener()
#     word_dict=file_worker(the_file)
#     print(dictionary_to_tuple(word_dict))

# main()



def menu_selection():
    choice=input('Menu:\nadd(a),remove(r),find(f): ')
    return choice


def execute_selection(choice, a_dict):
    if choice=='a':
        a_dict=add_to_dict(a_dict)
    elif choice=='f':
        find_key(a_dict)
    elif choice=='r':
        remove_from_dict(a_dict)

def remove_from_dict(a_dict):
    key=input('key to remove: ')
    if key not in a_dict:
        print('No such key')
    else:
        del a_dict[key]
    return a_dict

def add_to_dict(a_dict):
    key=input('Key: ')
    value=input('Value: ')
    if key in a_dict:
        print('Error. Key already exists')
    else:
        a_dict[key]=value
    return a_dict


def find_key(a_dict):
    key=input('key to find: ')
    print(a_dict.get(key, 'key not found'))
    return a_dict

def dict_to_tuples(a_dict):
    a_list=[]
    for key,value in a_dict.items():
        a_tuple=(key,value)
        a_list.append(a_tuple)
    return a_list

def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()





