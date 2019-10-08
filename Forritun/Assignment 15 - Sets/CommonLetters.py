def get_input():
    a_list=input('Input a list of integers separated with a comma: ').split(',')
    b_list=input('Input a list of integers separated with a comma: ').split(',')
    a_list=[int(i) for i in a_list]
    b_list=[int(i) for i in b_list]
    return a_list, b_list

def set_lists(a_list,b_list):
    a_set=set(a_list)
    b_set=set(b_list)
    return a_set,b_set
    
def print_sets(a_set,b_set):
    print(a_set)
    print(b_set)

def set_operation(a_set,b_set):
    operation=1
    while operation != 4:
        print('1. Intersection')
        print('2. Union')
        print('3. Difference')
        print('4. Quit')
        operation=int(input('Set operation: '))
        if operation == 1:
            print(a_set & b_set)
        elif operation == 2:
            print(a_set | b_set)
        elif operation ==3:
            print(a_set-b_set)
     

def main():
    a_list,b_list=get_input()
    a_set,b_set=set_lists(a_list,b_list)
    print_sets(a_set,b_set)
    set_operation(a_set,b_set)

main()