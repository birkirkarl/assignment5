skjal = open('words.txt')
lengsta = ''
for i in skjal: 
    if len(i) > len(lengsta):
        lengsta = i
        lengd = len(i)-1
print("Longest word is '"+lengsta.strip()+"' of length", lengd)
    
 