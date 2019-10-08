# The function definition goes here
def lengd(x):
    if x>1 and x<555:
        print(x,'is in range.')
    else:
        print(x,'is outside the range!')

num = int(input("Enter a number: "))

lengd(num)