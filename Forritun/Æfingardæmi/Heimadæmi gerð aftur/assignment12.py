import string



# def build_wordlist():
#     a_list=[]
#     file_stream=open('test.txt','r')
#     for i in file_stream:
#         thestuff=i.strip(string.punctuation).strip().split(' ')
#         for k in thestuff:
#             a_list.append(k)
#     return a_list

# #will take this wordlist as a parameter 
# #and return another wordlist comprising of all unique words found in the wordlist.
# def find_unique(info):
#     uniques_list=[]
#     for i in info:
#         if i not in uniques_list:
#             uniques_list.append(i)
#     uniques_list.sort()
#     print(uniques_list)




# info=build_wordlist()
# find_unique(info)

# #['another', 'file', 'in', 'line', 'test', 'the']



# def merge_lists(list1,list2):
#     alpha_list=[]
#     tmp=[]
#     tmp = list1 + list2
#     tmp=list(set(tmp))
#     print(tmp)


# list1 = input("Enter elements of list separated by commas: ").split(',')
# list2 = input("Enter elements of list separated by commas: ").split(',')
# print(merge_lists(list1, list2))


# def game_of_eights(a_list):
#     found_two=False
#     try:
#         for i in range(len(a_list)):
#             if int(a_list[i]) == 8 and int(a_list[i+1]) == 8:
#                 found_two=True
#         return found_two

#     except IndexError:
#         return found_two
#     except:
#         print('Error. Please enter only integers.')

# def main():
#     a_list=input('Enter elements of list separated by commas: ').split(',')
#     print(game_of_eights(a_list))



# main()