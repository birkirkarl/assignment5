all_cards=[]
for number in range(1,14):
    for letter in 'SHDC':
        if number==1:
            all_cards.append('A'+letter)
        elif number==11:
            all_cards.append('J'+letter)
        elif number==12:
            all_cards.append('Q'+letter)
        elif number==13:
            all_cards.append('K'+letter)
        else:
            all_cards.append(str(number)+letter)


for i in range(4):
    print (" ".join(all_cards[i*13:(i+1)*13]) + "\n")