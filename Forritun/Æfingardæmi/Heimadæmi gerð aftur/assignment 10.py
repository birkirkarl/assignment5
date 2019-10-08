import string

# sentence = input("Input a sentence: ")

# unique_letters=[]
# for i, letter in enumerate(sentence):
#     if not letter in unique_letters and sentence[i].isalpha():
#         unique_letters.append(letter)


# print("Unique letters:", unique_letters)


# def to_list(strengur):
#     strengur=strengur.replace(","," ").split(" ")
#     print(strengur)

# strengur=input('Enter the string: ')
# to_list(strengur)

# NotExit= True
# the_list=[]
# while NotExit:
#     value=input("Enter value to be added to list: ").lower()
#     if value == 'exit':
#         NotExit=False
#     else:
#         the_list.append(value)
# for i in the_list*3:
#     print(i)


# def make_new_row(row):
#     new_row = []
#     for i in range(0,len(row)+1):
#         if i == 0 or i == len(row):
#             new_row.append(1)
#         else:
#             new_row.append(row[i]+row[i-1])
#     return new_row
    
    

# # Main program starts here - DO NOT CHANGE
# height = int(input("Height of Pascal's triangle (n>=1): "))
# new_row = []
# for i in range(height):
#     new_row = make_new_row(new_row)
#     print(new_row)

def input_vector(size):
    vector = []
    for i in range(0,size):
        vector.append(float(input("Element no {}: ".format(i+1))))
    return vector


def dot_product(vector_1,vector_2):
    sum = 0
    for i in range(0,size):
        sum += vector1[i]*vector2[i]
    return sum
# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))










