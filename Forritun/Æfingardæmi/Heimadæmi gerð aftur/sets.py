

# Write a program that prompts the user for a name.  The program then splits the name into first and last name (case insensitive).

# Then it:

# calls a function that returns a list of the common letters in first and last. The data structures used in this implementation can only be lists.
# calls a function that returns a set containing the common letters in first and last.  The data structures used in this implementation can only be sets.
# prints out a sorted list version of the results from 1) and 2)




# def find_union(first,last):
#     A=set(first)
#     B=set(last)
#     return sorted(list(A&B))

# first,last=input('Enter Name: ').lower().split(' ')
# print(find_union(first,last))





# def find_intersection(A,B):
#     return A&B
# def find_union(A,B):
#     return A|B
# def find_difference(A,B):
#     return A-B


# def get_list():
#     first=(input(text).split(','))
#     second=(input(text).split(','))
#     first=[int(i) for i in first]
#     second=[int(i) for i in second]
#     first=(set(first))
#     second=(set(second))
#     return first,second


# KeepGoing=True
# text='Input a list of integers separated with a comma: '
# menu='1. Intersection\n2. Union\n3. Difference\n4. Quit\nSet operation: '

# first_list,second_list=get_list()
# print(first_list)
# print(second_list)
# while KeepGoing:
#     choice=int(input(menu))
#     if choice==1:
#         print(find_intersection(first_list,second_list))
#     elif choice==2:
#         print(find_union(first_list,second_list))
#     elif choice==3:
#         print(find_difference(first_list,second_list))
#     else:
#         KeepGoing=False




# all words need to be converted to lower case
# all words need to be stripped of punctuations
# The keys in the bigram dictionary should be tuples (word1, word2)
# The values are the occurences of the given bigram in the text

import string
from operator import itemgetter

def file_opener():
    file_name=input('Enter the name of the file: ')
    all_data=open(file_name,'r')
    return all_data


def file_workbox(all_data):
    all_the_words=[]
    for line in all_data:
        linan=line.strip().split()
        linan2=[i.strip(string.punctuation).lower() for i in linan]
        all_the_words.extend(linan2)
    return all_the_words

def dictionary_creator(all_the_words):
    a_dict={}
    for i in range(len(all_the_words)-1):
        a_tuple=(all_the_words[i],all_the_words[i+1])
        if a_tuple not in a_dict:
            a_dict[a_tuple] = 1
        else:
            a_dict[a_tuple]+=1
    return a_dict

def dictionary_to_tuples(a_dict):
    a_list=[]
    for key,value in a_dict.items():
        a_tuple=(key,value)
        a_list.append(a_tuple)
    a_list=sorted(a_list,key=itemgetter(1),reverse=True)      
    return a_list[:10]        



def main():
    all_data=file_opener()
    all_the_words=file_workbox(all_data)
    a_dict=dictionary_creator(all_the_words)
    print(dictionary_to_tuples(a_dict))


main()


# import string
# from operator import itemgetter

# def read_file(filename):
#     with open(filename, 'r') as filename2:
#         word_list=[]
#         punctuations=string.punctuation
#         for line in filename2:
#             linan=line.strip().split()
#             linan2=[i.strip(punctuations).lower() for i in linan]
#             word_list.extend(linan2)
#         return word_list

# def word_list_to_counts(word_list):
#     word_count_dict={}
#     for i in range(len(word_list)-1):
#         word_tuple_small=(word_list[i],word_list[i+1])
#         if word_tuple_small in word_count_dict:
#             word_count_dict[word_tuple_small]+=1
#         else:
#             word_count_dict[word_tuple_small]=1
#     return word_count_dict

# def dict_to_list_of_tuples(word_count_dict):
#     a_list = [(key,value) for key, value in word_count_dict.items()]
#     return a_list        

# def main():
#     filename=input('Enter name of file: ')
#     word_list=read_file(filename)
#     word_count_dict=word_list_to_counts(word_list)
#     a_list=dict_to_list_of_tuples(word_count_dict)
#     a_list=sorted(a_list,key=itemgetter(1),reverse=True)
#     print(a_list[:10])

# main()