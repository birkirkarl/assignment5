def find_min(first,second):
    if first > second:
        minimum= second
    else:
        minimum=first
    return minimum

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
    
print("Minimum: ", find_min(first,second))