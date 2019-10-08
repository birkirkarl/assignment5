
def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

listi=get_list()
print(listi)
val=input('Enter choice (m,r): ')
if val== 'r':
    nr=int(input())
    remove_ch(listi,nr)
elif val== 'm':
    nr=input()
    nr1,nr2=nr.split(",")
    nr1=int(nr1)
    nr2=int(nr2)
    mutate_list(listi,nr1,nr2)
print(listi)