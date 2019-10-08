import random
import string
punctuation="!,.?"
#get_word_string() and scramble_string() tveir functions

def get_word_string(x):
    word_string=''
    try:
        dataFile = open(x)
        for i in dataFile:
            if i.strip =="":
                word_string += "\n"
            else:
                word_string = word_string + i.strip() + " "
        return word_string
    except:
        print('File ' + x + " not found")
        word_string = []
    return word_string


def scramble_string(x):
    listinn=[]
    allt = x.split()
    for i in range(len(allt)):
        if len(allt[i])>3:
            word=allt[i]
            if word[-1] in punctuation:
                einn,midja,seinast,drasl=word[0], word[1:-2],word[-2],word[-1]
                midja=list(midja)
                random.shuffle(midja)
                midja=''.join(midja)
                nyjaord=einn+midja+seinast+drasl
                listinn.extend([nyjaord])
            else:
                einn,midja,seinast=word[0], word[1:-1],word[-1]
                midja=list(midja)
                random.shuffle(midja)
                midja=''.join(midja)
                nyjaord=einn+midja+seinast
                listinn.extend([nyjaord])
        else:
            listinn.extend([allt[i]])
    return ' '.join(listinn)



# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)