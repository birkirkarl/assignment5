def sort_list(a_list):
    sorted_list = a_list.sort()
    return sorted_list 
    

def main():
    a_list = []
    while True:
        try:
            a = int(input())
            a_list.append(a)
        except:
            False
            break
    #loop to accept integers until a non-digit is entered goes here
    
    
    
    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()