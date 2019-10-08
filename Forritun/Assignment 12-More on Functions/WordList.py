#build_wordlist() function goes here
import string

def build_wordlist(infile):
    word_string=''
    for i in infile:
        if i.strip =="":
            word_string += "\n"
        else:
            word_string = word_string + i.strip() + " "
    loka = ""
    for c in word_string:
        if c not in string.punctuation:
            loka += c
    return loka

        
#find_unique() function goes here
def find_unique(text):
    words=text.split()
    new_wordlist=set(words)
    new_wordlist=list(new_wordlist)
    return new_wordlist

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()