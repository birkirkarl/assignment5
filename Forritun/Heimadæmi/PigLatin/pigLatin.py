piglatin='a' #til að byrja forritið
#geri her tæmandi lista af því sem ég þarf að hafa auga á.
samhljodar= ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z","w","y"]
tveir = ["bl", "br", "ch", "ck", "cl", "cr", "dr", "fl", "fr", "gh", "gl", "gr", "ng", "ph", "pl", "pr", "qu", "sc", "sh", "sk", "sl", "sm", "sn", "sp", "st", "sw", "th", "tr", "tw", "wh", "wr"]
serhljodar = ["a", "e", "i", "o", "u"]
thrir=["scr"]
punktur='.'


while piglatin != '.': #stoppa í punkti
    piglatin=str(input('Enter a word:'))
    counter=0
    for i in range(0, len(piglatin)):
        if piglatin[i] in serhljodar: #herna er ég að checka á sértilfelli hvort það sé enginn sérhljóði í orði
            counter=counter+1
    if piglatin == punktur:
        break
    if piglatin[0:3] in thrir and counter>0:
        print(' '+piglatin[3:]+piglatin[0:3]+'ay')
    elif piglatin[0] in serhljodar:
        print(' '+piglatin+'yay')
    elif piglatin[0:2] in tveir and counter>0:
        print(' '+piglatin[2:]+piglatin[0:2]+'ay')
    elif piglatin[0] in samhljodar and counter>0:
        print(' '+piglatin[1:]+piglatin[0]+'ay')
    else:
        print(' '+piglatin+'ay')

        #athuga að ég fór fyrst eftir wikipedia og notaði translator og áttaði mig eftir á að það átti eftir að fara eftir skilyrðum í bók
