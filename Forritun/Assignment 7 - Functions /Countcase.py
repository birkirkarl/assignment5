def countcase(x):
    lower=0
    upper=0
    for i in range(0,len(user_input)):
        if user_input[i].islower():
            lower=lower+1
        elif user_input[i].isupper():
            upper=upper+1
    return lower, upper

user_input = input("Enter a string: ")

# Call the function here
lower, upper = countcase(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)
