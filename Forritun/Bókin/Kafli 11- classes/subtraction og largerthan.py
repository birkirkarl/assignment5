# Example:

# if list1 = [1,2,3,4,5,6,7,8,9] and list2 = [100,200,300] and the range is 4:7

# then the result of calling the transform function is:

 

# list1 = ['1', '2', '3', '4', '8', '9']
# ['100', '200', '300', '7', '6', '5']



# def get_list():
#     a_list=input("Enter elements of list separated by commas: ").split(',')
#     return a_list

# def transform(list1, list2, index1, index2):
#     tmp=list1[index1:index2]
#     del list1[index1:index2]
#     tmp.reverse()
#     list2=list2.extend(tmp)
#     return list1,list2

# def get_integer(x):
#     integer=int(input(x))
#     return integer



# list1 = get_list()
# list2 = get_list()
# index1 = get_integer("Enter from value: ")
# index2 = get_integer("Enter to value: ")
# transform(list1, list2, index1, index2)
# print(list1)
# print(list2)





# def music_func(music_type='Classic Rock',music_group='The Beatles',vocalist='Freddie Mercury'):
#     MT=music_type
#     MG=music_group
#     V=vocalist
#     print('The best kind of music is {}\nThe best music group is {}\nThe best lead vocalist is {}.'.format(MT,MG,V))

# MT,MG,V=input('Input music, group, singer: ').split(',')
# music_func(MT,MG,V)
# music_func()



# def sort_list(a_list):
#     a_list=sorted(a_list)
#     return a_list
# def get_list():
#     a_list=[]
#     try:
#         while True:
#             x=int(input())
#             a_list.append(x)
#     except:
#         return a_list


# a_list=get_list()

# print(a_list)
# print(sort_list(a_list))
# print(a_list)



