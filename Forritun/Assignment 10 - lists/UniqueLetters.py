import string

sentence = input("Input a sentence: ")

unique_letters=[]
for i, letter in enumerate(sentence):
    if not letter in unique_letters and sentence[i].isalpha():
        unique_letters.append(letter)


print("Unique letters:", unique_letters)