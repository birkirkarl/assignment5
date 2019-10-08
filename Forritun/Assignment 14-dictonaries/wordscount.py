
def file_pointer(filename):
    fpointer=open(filename)
    return fpointer

def a_list_of_words_from_file(fpointer):
    a_list_of_words=[]
    for line in fpointer:
        linan=line.strip().replace(",", "").replace(".","").split(" ")
        a_list_of_words.extend(linan)
    return a_list_of_words

def a_list_of_words_to_dict_counter(a_list_of_words):
    a_dict = {}
    for i in a_list_of_words:
        if i.lower() in a_dict:
            a_dict[i.lower()]+=1
        else:
            a_dict[i.lower()]=1
    return a_dict

def crea_list_of_tuples_from_dict(a_dict):
    a_list = []
    for key, value in a_dict.items():
        a_tuple=(key, value)
        a_list.append(a_tuple)
    return a_list


def main():
    filename = input("Name of file: ")
    fpointer=file_pointer(filename)
    a_list_of_words=a_list_of_words_from_file(fpointer)
    a_dict=a_list_of_words_to_dict_counter(a_list_of_words)
    a_list=crea_list_of_tuples_from_dict(a_dict)
    # Transform the list to a dictionary of word-count pairs
    # Finally, makes a list of tuples from the dictionary
    print(sorted(a_list))
    
main()