import string
punctuation=string.punctuation

def read_file(filename):
    with open(filename, 'r') as filename2:
        doc_list=[]
        tmp=''
        lines=filename2.readlines()[1:]
        for line in lines:
            if "NEW DOCUMENT" in line:
                doc_list.append(tmp)
                tmp=''        
                continue
            else:
                tmp += line
        doc_list.append(tmp)      
        return doc_list

def create_the_dict(doc_list): #dict with every word in the file
    a_dict={}
    for i,doc in enumerate(doc_list):
        doc=doc.split()
        for words in doc:
            word=words.strip(punctuation).lower()   
            if word not in a_dict:
                a_dict[word] = {i}
            else:
                a_dict[word].add(i)
    return a_dict


def ctrl_f(doc_list, a_dict):
    try:
        words_not_exist = True
        while words_not_exist:
            loc_list=[]
            
            search_list=[]
            search=input("> Enter search words: ").lower()
            search_list=search.split(" ")
            for key in search_list:
                loc_list.extend(a_dict[key])
            if len(search_list)==1: #bara eitt leitarorð og þarf ekki að crossreferenca
                reference_list=loc_list
            else:
                reference_list=set([x for x in loc_list if loc_list.count(x) > 1])
            ctrl_f_printer(reference_list)
            words_not_exist = False
            return reference_list
    except:
        reference_list=set([x for x in loc_list if loc_list.count(x) > 1])
        print("No match.")
        return reference_list

def ctrl_f_printer(reference_list):
    ref=" ".join(str(x) for x in reference_list)
    if len(ref)==0:
        ref=0
    print("Documents that fit search:",ref,"\n")
    return reference_list

def print_from_reference_list(reference_list, doc_list):
    choice=int(input("> Enter document number: "))
    print("Document #%d"%(choice))
    choice_not_found = True
    for i in reference_list:
        if i ==choice:
            print(doc_list[i])
            choice_not_found = False
    if choice_not_found:
        print("No match.")

def main():
    try:
        val=0
        filename=input('Document collection: ')
        print("")
        doc_list=read_file(filename)
        while val!=3:
            print("What would you like to do?")
            val=int(input("1. Search Documents\n2. Print Document\n3. Quit Program\n"))
            if val==1: #read doc, split it up and then search "field" and then print correlation.
                a_dict=create_the_dict(doc_list)
                reference_list=ctrl_f(doc_list,a_dict)
            elif val==2: #print out the results of the search "field"
                print_from_reference_list(reference_list,doc_list)
            else: # if not search or printing then exit
                print("> Exiting program.")
                val=3
    except:
        print("Documents not found.")

main()
