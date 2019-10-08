import string
def palindrome(x):# palindrome function definition goes here
    if x[::-1] == x:
        print('"'+in_str+'"'+" is a palindrome.")
    else:
        print('"'+in_str+'"' + " is not a palindrome.")
        
in_str = (input("Enter a string: "))
typpi=in_str.lower()
typpi=typpi.replace("!","")
typpi=typpi.replace(",","")
typpi=typpi.replace(" ","")
typpi=typpi.replace("'","")


palindrome(typpi)# call the function and print out the appropriate message