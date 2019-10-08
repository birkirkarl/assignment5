
def game_of_eights(a_list):
    try:
        for i in range(len(a_list)-1):
            for j in range(len(a_list)):
                int(a_list[j])
            if a_list[i]=='8' and a_list[i+1]=='8':
                return print(True)
        return print(False)    
    except ValueError:
        print('Error. Please enter only integers.')

def main():
    
    a_list =(input("Enter elements of list separated by commas: ").split(','))
    game_of_eights(a_list)

main()