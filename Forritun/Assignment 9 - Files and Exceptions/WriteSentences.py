test = open('words.txt')
sentance = open('sentences.txt','w')
output_test = ''
for i in test:
    if i.strip() == "":
        output_test += "\n"
    else:
        output_test = output_test + i.strip() + " "  
print(output_test, file=sentance)
print(output_test)