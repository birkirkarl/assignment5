# def filereader(x):
#     try:
#         file_name=open(x,'r')
#         return file_name
#     except:
#         return False

# def word_tool(the_file):
#     file_list=[]
#     longest=0
#     for i in the_file:
#         file_list.append(i.strip())
#     for i in range(len(file_list)):
#         if len(file_list[i])>longest:
#             longest=len(file_list[i])
#             the_word=file_list[i]
#     print('Longest word is \'{}\' of length {}'.format(the_word,longest))




# def main():
#     x=input('Enter name of file: ')
#     the_file=filereader(x)
#     if the_file == False:
#         print('File {} not found!'.format(x))
#     else:
#         word_tool(the_file)
# #main()


# def is_prime(n):
#     '''Returns True if the given positive number is prime and False otherwise'''
#     if n == 1:
#         return False
#     if n == 2:
#         return True
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     else:
#         return True

# def get_numbers(get):
#     basic_list=[]
#     prime_list=[]
#     try:
#         for i in get:
#             basic_list.append(int(i))
#             if is_prime(int(i)):
#                 prime_list.append(int(i))
#         return basic_list, prime_list
#     except:
#         print('Incorrect input!')

# def basic_stuff(basic_list,prime_list):
#     print('Input list: {}'.format(basic_list))
#     print('Sorted list: {}'.format(sorted(basic_list)))
#     prime_stuff(prime_list)
#     Average=(sum(basic_list)/len(basic_list))
#     minimum=min(basic_list)
#     maximum=max(basic_list)
    
#     print('Min: {}, Max: {}, Average: {:.2f}'.format(maximum,minimum,Average))


# def prime_stuff(prime_list):
#     correct_prime=list(set(prime_list))
#     print('Prime list: {}'.format(sorted(correct_prime)))

# get=input("Enter integers separated with commas: ").split(',')
# basic_list,prime_list=get_numbers(get)
# basic_stuff(basic_list,prime_list)










