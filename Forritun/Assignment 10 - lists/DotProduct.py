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