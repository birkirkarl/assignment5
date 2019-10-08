def read_file(filename):
    with open(filename, 'r') as filename:
        word_list=[]
        for line in filename:
            linan=line.lower().strip().replace('.','').replace(',','').split(' ')
            word_list.extend(linan)
        return word_list

def tuple_list(word_list):
    word_list2=[]
    for i in range(len(word_list)-1):
        word_list_small=(word_list[i],word_list[i+1])
        word_tuple_small=tuple(word_list_small)
        word_list2.append(word_tuple_small)
    
    return word_list2

def word_list_to_counts(word_list2):
    word_count_dict={}
    for i in word_list2:
        if i.lower() in word_count_dict:
            word_count_dict[i.lower()]+=1
        else:
            word_count_dict[i.lower()]=1
    return word_count_dict
    
def main():
    filename=input('Enter name of file: ')
    word_list=read_file(filename)
    word_list2=tuple_list(word_list)
    word_count_dict=word_list_to_counts(word_list2)
    print(word_count_dict)

main()