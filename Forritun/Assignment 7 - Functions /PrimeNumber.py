def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            print(x,'is not a prime')
            break
    else:
        print(x,'is a prime')
    
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
is_prime(num)